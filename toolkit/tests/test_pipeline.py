import copy
import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
spec=importlib.util.spec_from_file_location('pipeline',Path(__file__).resolve().parents[1]/'pipeline.py')
p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)

class FourCategoryAssessment(unittest.TestCase):
    def setUp(self):
        self.cfg=patch.object(p,'config',return_value={'book':'test','cutoff':'2026-11-08','publication_year_proxy':2013,'rules_version':'test'})
        self.cfg.start();self.addCleanup(self.cfg.stop)
        self.claim=dict(id='x',quote='这个制度会继续存在',source_verified=True,duplicate_of=None)
        self.e={'e':{'verified':True,'date':'2025-01-01'}}
        self.r=dict(id='x',inclusion='forecast',verdict='正确',basis='observed_window',
            scope='仅评价2013至2025年的制度持续，不判定永久存在',reason='2025年制度文件仍在实行',
            limitation='文件不能证明未来永远不变',evidence_ids=['e'],method='制度惯性',
            method_basis='inferred',observation_end='2025-01-01',future_time_text='',condition_state='unconditional')

    def validate(self):p.validate_assessment(self.r,self.claim,self.e)

    def test_no_author_deadline_needed_for_disclosed_observed_window(self):self.validate()

    def test_unresolved_future_is_valid_but_cannot_score(self):
        self.r.update(verdict='暂无法判断',basis='future',observation_end=None,future_time_text='2035年')
        self.validate()
        self.r['verdict']='正确'
        with self.assertRaises(ValueError):self.validate()

    def test_unknown_condition_cannot_score(self):
        self.r['condition_state']='unknown'
        with self.assertRaises(ValueError):self.validate()
        self.r.update(verdict='暂无法判断',basis='conditional')
        self.validate()

    def test_partial_is_not_a_substitute_for_missing_evidence(self):
        self.r.update(verdict='部分符合',basis='evidence',evidence_ids=[])
        with self.assertRaises(ValueError):self.validate()

    def test_future_trend_can_be_partial_but_not_final_correct(self):
        self.r.update(verdict='部分符合',trend_aligned=True,future_time_text='2035年')
        self.validate()
        self.r['verdict']='正确'
        with self.assertRaises(ValueError):self.validate()
        self.r.update(verdict='部分符合',basis='future')
        with self.assertRaises(ValueError):self.validate()

    def test_trend_still_needs_evidence_and_unknown_premise_cannot_score_correct(self):
        self.r.update(verdict='部分符合',trend_aligned=True,evidence_ids=[])
        with self.assertRaises(ValueError):self.validate()
        self.r.update(evidence_ids=['e'],condition_state='unknown')
        self.validate()
        self.r['verdict']='正确'
        with self.assertRaises(ValueError):self.validate()
        self.r.update(verdict='部分符合',condition_state='unconditional',trend_aligned='true')
        with self.assertRaises(ValueError):self.validate()

    def test_trend_summary_is_a_subset_not_extra_verdict(self):
        rows=[{'assessment':dict(self.r,verdict='部分符合',trend_aligned=True)},
              {'assessment':dict(self.r,verdict='部分符合')}]
        result=p.assessment_summary(rows,[])
        self.assertEqual(result['trend_aligned_n'],1)
        self.assertEqual(result['verdicts']['部分符合'],2)
        self.assertEqual(result['forecast_n'],2)

    def test_evidence_and_observation_cannot_leak_future(self):
        self.r['observation_end']='2030-01-01'
        with self.assertRaises(ValueError):self.validate()
        self.r['observation_end']='2025-01-01';self.e['e']['date']='2027-01-01'
        with self.assertRaises(ValueError):self.validate()

    def test_exclusions_and_known_duplicates_cannot_score(self):
        self.r.update(inclusion='nonforecast',basis='excluded')
        with self.assertRaises(ValueError):self.validate()
        self.r['verdict']=None;self.validate()
        self.claim['duplicate_of']='original'
        with self.assertRaises(ValueError):self.validate()
        self.r['inclusion']='duplicate';self.validate()

    def test_local_capture_cannot_escape_project(self):
        with self.assertRaises(ValueError):p.evidence_path({'id':'e','local_archive':'../secret'})
        with self.assertRaises(ValueError):p.evidence_path({'id':'e','local_archive':'/tmp/secret'})

    def test_rejected_full_book_apply_does_not_partially_write(self):
        with tempfile.TemporaryDirectory() as d,patch.object(p,'ROOT',Path(d)):
            root=Path(d);(root/'output').mkdir();(root/'data').mkdir()
            p.save(root/'config.json',{'cutoff':'2026-11-08','rules_version':'test'})
            claims=[self.claim,dict(self.claim,id='y')]
            p.table(root/'data/claims.jsonl',claims);before=(root/'data/claims.jsonl').read_bytes()
            p.table(root/'data/evidence.jsonl',[dict(id='e',verified=True)])
            p.table(root/'response.jsonl',[self.r])
            with self.assertRaises(ValueError):p.apply_assessment(root/'response.jsonl')
            bad=dict(self.r,id='y',condition_state='unknown')
            p.table(root/'response.jsonl',[self.r,bad])
            with self.assertRaises(ValueError):p.apply_assessment(root/'response.jsonl')
            self.assertEqual((root/'data/claims.jsonl').read_bytes(),before)
            self.assertEqual(list((root/'output').iterdir()),[])

    def test_denominators_do_not_treat_unknown_or_excluded_as_errors(self):
        rows=[{'assessment':self.r}, {'assessment':dict(self.r,verdict='部分符合')},
              {'assessment':dict(self.r,verdict='暂无法判断',basis='future')},
              {'assessment':dict(self.r,inclusion='nonforecast',verdict=None)}, {}]
        s=p.assessment_summary(rows,[])
        self.assertEqual(s['decided_n'],2);self.assertEqual(s['forecast_n'],3)
        self.assertEqual(s['correct_share_of_decided'],.5)
        self.assertAlmostEqual(s['evaluation_coverage'],2/3)
        self.assertEqual(s['excluded']['nonforecast'],1);self.assertEqual(s['unreviewed'],1)
        self.assertIsNone(s['partial_numeric_weight'])
        self.assertIsNone(p.assessment_summary([],[])['correct_share_of_decided'])

    def test_evidence_coverage_does_not_count_exclusions_or_completion_as_research(self):
        rows=[{'assessment':dict(self.r,verdict='暂无法判断')},
              {'assessment':dict(self.r,id='y',verdict='暂无法判断',evidence_ids=[])},
              {'assessment':dict(self.r,id='z',inclusion='nonforecast',verdict=None)}]
        s=p.assessment_summary(rows,[])
        self.assertTrue(s['whole_candidate_pass_complete'])
        self.assertEqual(s['forecasts_with_bound_evidence'],1)
        self.assertEqual(s['forecasts_without_bound_evidence'],1)
        self.assertTrue(s['no_decidable_outcomes'])
        self.assertIsNone(s['correct_share_of_decided'])
        rows[0]['assessment']['verdict']='正确'
        self.assertFalse(p.assessment_summary(rows,[])['no_decidable_outcomes'])
        self.assertFalse(p.assessment_summary([],[])['no_decidable_outcomes'])

    def test_full_extraction_preserves_original_and_old_review(self):
        with tempfile.TemporaryDirectory() as d,patch.object(p,'ROOT',Path(d)):
            root=Path(d);(root/'output').mkdir();(root/'data').mkdir()
            p.save(root/'config.json',{'rules_version':'test'})
            old=dict(self.claim,kind='prediction',extraction={'reason':'旧抽取'},review={'reason':'旧核查'})
            p.table(root/'data/claims.jsonl',[old])
            new=dict(id='x',kind='duplicate',claim='重复解释',time_text='',condition_text='',
                method='不适用',method_basis='unknown',reason='本条是另一条的重复表达')
            p.table(root/'full.jsonl',[new]);p.apply_full_extract(root/'full.jsonl')
            got=p.lines(root/'data/claims.jsonl')[0]
            for key in old:self.assertEqual(got[key],old[key])
            self.assertEqual(got['extraction_v2']['kind'],'duplicate')
            self.assertIn('receipt',got['extraction_v2'])
