import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import review_unresolved as rr
import run_parallel as rp


class UnresolvedReviewTests(unittest.TestCase):
    def setup_root(self, root):
        (root/'data').mkdir()
        research=root/'output/unresolved_round2'
        research.mkdir(parents=True)
        rp.save_json(root/'config.json', {'book':'test','cutoff':'2026-11-08'})
        claims=[dict(id=str(n),page=n,quote='未来人口下降',context='语境',speaker='作者',source_verified=True,
                     extraction_v2={'method':'人口趋势外推','method_basis':'inferred'},
                     assessment={'verdict':'暂无法判断' if n<3 else '正确','evidence_ids':['e1']})
                for n in range(7)]
        frozen=research/'before_book_index.json'
        rp.save_json(frozen,claims)
        # Current outcomes cannot silently change which frozen IDs get reviewed.
        current=copy.deepcopy(claims)
        current[0]['assessment']['verdict']='正确'
        rp.save_jsonl(root/'data/claims.jsonl',current)
        rp.save_jsonl(root/'data/evidence.jsonl',[
            {'id':'e1','verified':True,'excerpt':'2013至2025人口持续下降'},
            {'id':'e2','verified':True,'excerpt':'新材料'},
            {'id':'unused','verified':True,'excerpt':'无关材料'}])
        rp.save_jsonl(research/'research_test.jsonl',[
            {'id':'0','change_reason':'趋势证据','recommendation':{'verdict':'部分符合','trend_aligned':True,
               'evidence_ids':['e2'],'method':'研究员的查表流程'}}])
        return frozen,research

    def test_frozen_subset_and_research_evidence_is_scoped(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); frozen,research=self.setup_root(root)
            rows,batches,coverage=rr.prepare_batches(root,frozen,research)
            self.assertEqual(len(rows),3)
            self.assertEqual([r['id'] for r in rows],[str(n) for n in range(3)])
            self.assertEqual(coverage['research_covered'],1)
            first=batches[0][2][0]
            self.assertEqual(first['allowed_evidence_ids'],['e1','e2'])
            self.assertEqual(first['extraction']['method'],'人口趋势外推')
            self.assertNotIn('method',first['research_notes']['recommendation'])
            self.assertNotIn('无关材料',json.dumps(batches,ensure_ascii=False))
            self.assertTrue(all(len(rp.canonical(request))<=rp.MAX_REQUEST_BYTES for _,request,_ in batches))
            self.assertTrue(all('只审阅任务包原文与上下文，不使用事后结果' not in request['messages'][0]['content']
                                for _,request,_ in batches))

    def test_invalid_raw_response_recovery_is_explicit_and_no_network(self):
        request=rp.payload('assess',{'cases':[{'id':'x'}]},8000)
        raw={'choices':[{'finish_reason':'stop','message':{'content':json.dumps({'items':[{'id':'x'}]})}}]}
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            digest=hashlib.sha256(rp.canonical(request)).hexdigest()
            rp.save_json(root/(digest+'.response.json'),raw)
            items,status=rr.recover_raw_items(root,request,[{'id':'x'}])
            self.assertEqual(items,[{'id':'x'}])
            self.assertEqual(status,'recovered_for_local_review_only')
            _,status=rr.recover_raw_items(root,request,[{'id':'wrong'}])
            self.assertEqual(status,'raw_id_coverage_mismatch')

    def test_runner_trend_validation_needs_partial_and_evidence(self):
        item=dict(id='x',inclusion='forecast',verdict='部分符合',basis='observed_window',
                  scope='2013至2025人口连续下降',reason='趋势符合，最终结果待验证',limitation='2035终点待验证',
                  evidence_ids=['e1'],method='人口趋势外推',method_basis='inferred',
                  observation_end='2025-12-31',future_time_text='2035年',condition_state='unconditional',trend_aligned=True)
        cases=[{'id':'x','allowed_evidence_ids':['e1'],'source_verified':True}]
        def wrapped():
            return {'choices':[{'finish_reason':'stop','message':{'content':json.dumps({'items':[item]})}}]}
        rp.validate_items('assess',wrapped(),cases)
        item['evidence_ids']=[]
        with self.assertRaises(ValueError):rp.validate_items('assess',wrapped(),cases)
        item.update(evidence_ids=['e1'],condition_state='unknown')
        self.assertEqual(rp.validate_items('assess',wrapped(),cases)[0]['verdict'],'部分符合')
        item.update(condition_state='unconditional',verdict='正确')
        with self.assertRaises(ValueError):rp.validate_items('assess',wrapped(),cases)


if __name__=='__main__':unittest.main()
