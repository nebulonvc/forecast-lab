"""v5 extraction screen: non-forecasts stay out of the scored set, v4 records still load."""
import hashlib
import json
from pathlib import Path
import sys
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import decision_policy
import pipeline
import prepare_book as pb
import run_parallel as rp
import verify_prediction as vp


def pred(quote, **kw):
    base = dict(quote=quote, kind='prediction', speaker='作者', attribution='author', future_oriented=True,
                claim='c', expanded_claim='e', reference_resolutions=[], unresolved_references=[],
                time_text='', condition_text='', method='m', method_basis='unknown', reason='r')
    base.update(kw)
    return base


def scored(ident='x'):
    return dict(id=ident, inclusion='forecast', verdict='正确', basis='observed_window',
                scope='只评价写明的窗口', reason='证据与主要结果一致', limitation='窗口有限',
                evidence_ids=['e'], method='趋势', method_basis='inferred', observation_end='2025-01-01',
                future_time_text='', condition_state='unconditional', trend_aligned=False,
                evidence_notes=[], remaining_gap='')


class ScreenFixtures(unittest.TestCase):
    """The sentences below are the ones case runs had been scoring as 正确."""

    def screen(self, quote, year=None, **kw):
        return pb.screen_claim(pred(quote, **kw), quote, year)

    def test_america_metaphor_and_trivial_ceremony_are_not_forecasts(self):
        # 《美国反对美国》(1991)
        claim_type, reason, _flags = self.screen('同样的肉有各种烧法', 1991)
        self.assertEqual((claim_type, reason), ('aphorism', 'aphorism'))
        claim_type, reason, _flags = self.screen('新任总统要发表就职演说', 1991)
        self.assertEqual((claim_type, reason), ('trivial', 'trivial'))

    def test_clash_aphorism_history_advice_mechanism_and_hypotheticals(self):
        # 《文明的冲突》(1996)
        cases = {
            '信任和友谊将是罕见的': 'aphorism',
            '1980年代科索沃提出了共和国地位要求。': 'historical',
            '1990–1994年南斯拉夫战争分裂了该地区。': 'historical',
            '1990-94年的南斯拉夫战争已经结束。': 'historical',
            '南斯拉夫的分裂是此前民族政策的结果。': 'historical',
            '各国应该加强文明之间的对话与合作。': 'normative',
            '民族矛盾导致了科索沃冲突的升级。': 'mechanism',
            '如果1980年科索沃已被承认，后来的战争就不会爆发。': 'hypothetical',
            '假如文明之间爆发全面战争，世界将因此分裂。': 'hypothetical',
        }
        for quote, expected in cases.items():
            with self.subTest(quote=quote):
                claim_type, reason, _flags = self.screen(quote, 1996)
                self.assertEqual((claim_type, reason), (expected, expected))

    def test_dated_change_and_conditional_forecast_stay_forecasts(self):
        kept = [
            '到2010年，核心国家之间的冲突将会上升。',
            '1980年代的危机将在今后十年重演。',
            '如果利率上升，今后五年出口将下降。',
        ]
        for quote in kept:
            with self.subTest(quote=quote):
                claim_type, reason, flags = self.screen(quote, 1996)
                self.assertEqual(claim_type, 'forecast')
                self.assertIsNone(reason)
                self.assertNotIn('not_resolvable_forecast', flags)

    def test_mechanism_word_does_not_swallow_a_future_modal(self):
        quote = '政府承担着沉重的由于家庭分化而产生的负担。这个包袱可能会越来越大。'
        claim_type, reason, flags = self.screen(quote, 1991)
        self.assertEqual(claim_type, 'forecast')
        self.assertIsNone(reason)
        self.assertIn(pb.HORIZON_IMPLICIT, flags)
        self.assertIsNone(pb.correct_verdict_block(quote, {}, 1991))

    def test_undated_directional_claim_keeps_an_implicit_window(self):
        for quote in ('差距将会扩大', '美国的价值体系将会衰落。'):
            with self.subTest(quote=quote):
                claim_type, reason, flags = self.screen(quote, 1991)
                self.assertEqual(claim_type, 'forecast')
                self.assertIsNone(reason)
                self.assertIn(pb.HORIZON_IMPLICIT, flags)
                self.assertNotIn(pb.HORIZON_EXPLICIT, flags)

    def test_sentence_without_a_direction_stays_unresolved(self):
        claim_type, reason, flags = self.screen('这本书讨论美国社会。', 1991)
        self.assertEqual(claim_type, 'unclear')
        self.assertIsNone(reason)
        self.assertIn('not_resolvable_forecast', flags)

    def test_english_wrapped_changes_and_horizon_stay_explicit_forecast(self):
        quote = 'economic growth will\ncontinue to slow\nby the end of\n2030.'
        claim_type, reason, flags = self.screen(
            quote, 2020, changes='will continue to slow', horizon='by the end of 2030')
        self.assertEqual(claim_type, 'forecast')
        self.assertIsNone(reason)
        self.assertIn(pb.HORIZON_EXPLICIT, flags)
        text = 'Context. ' + quote
        kept, _rejected = pb.validate_chunk_predictions(
            [pred(quote, changes='will continue to slow', horizon='by the end of 2030')],
            pb.split_text(text)[0])
        _kind, excluded, _flags = pb.classify_prediction(
            kept[0], text, kept[0]['source_char_start'], kept[0]['source_char_end'], (), 2020)
        self.assertIsNone(excluded)
        self.assertTrue(kept[0]['resolvable'])
        self.assertEqual(kept[0]['horizon_source'], pb.HORIZON_EXPLICIT)
        self.assertEqual(kept[0]['horizon'], 'by the end of 2030')
        claim_type, _reason, flags = self.screen(
            'Economic growth in 2030.', 2020, changes='will collapse', horizon='by 2030')
        self.assertEqual(claim_type, 'unclear')
        self.assertIn('not_resolvable_forecast', flags)

    def test_english_historical_comparison_and_pure_history(self):
        quote = 'Unlike 1914, in the coming decades competition will intensify.'
        claim_type, reason, flags = self.screen(quote, 2012, changes='competition will intensify')
        self.assertEqual(claim_type, 'forecast')
        self.assertIsNone(reason)
        self.assertIn(pb.HORIZON_EXPLICIT, flags)
        for historical in (
            'In 1980, Kosovo demanded republic status.',
            'By 1980, the bloc had splintered.',
            'Within five years of 1914, the empire collapsed.',
        ):
            with self.subTest(quote=historical):
                claim_type, reason, _flags = self.screen(historical, 1996)
                self.assertEqual((claim_type, reason), ('historical', 'historical'))

    def test_english_undated_directional_forecast_stays_implicit(self):
        claim_type, reason, flags = self.screen(
            'The wealth gap will widen.', 2012, changes='wealth gap will widen')
        self.assertEqual(claim_type, 'forecast')
        self.assertIsNone(reason)
        self.assertIn(pb.HORIZON_IMPLICIT, flags)
        self.assertNotIn(pb.HORIZON_EXPLICIT, flags)

    def test_model_label_excludes_and_cannot_override_a_detected_nonforecast(self):
        claim_type, reason, flags = self.screen('到2010年，核心国家之间的冲突将会上升。', 1996, claim_type='hypothetical')
        self.assertEqual((claim_type, reason), ('hypothetical', 'hypothetical'))
        self.assertIn('model_claim_type', flags)
        claim_type, reason, flags = self.screen('同样的肉有各种烧法', 1991, claim_type='forecast',
                                                changes='烧法会变', horizon='今后')
        self.assertEqual(reason, 'aphorism')
        self.assertIn('model_claim_type_overridden', flags)

    def test_invented_horizon_stays_implicit(self):
        quote = '美国的价值体系将会衰落。'
        claim_type, reason, flags = self.screen(quote, 1991, horizon='今后十年', changes='价值衰落')
        self.assertEqual(claim_type, 'forecast')
        self.assertIsNone(reason)
        self.assertIn(pb.HORIZON_IMPLICIT, flags)
        text = '前文。' + quote
        kept, _rejected = pb.validate_chunk_predictions([pred(quote, horizon='今后十年')], pb.split_text(text)[0])
        _kind, excluded, _flags = pb.classify_prediction(kept[0], text, kept[0]['source_char_start'], kept[0]['source_char_end'], (), 1991)
        self.assertIsNone(excluded)
        self.assertEqual(kept[0]['horizon_source'], pb.HORIZON_IMPLICIT)
        self.assertEqual(kept[0]['horizon'], '')

    def test_prompt_names_the_examples_and_v4_prompt_stays_untyped(self):
        for phrase in ['同样的肉有各种烧法', '信任和友谊将是罕见的', '新任总统要发表就职演说', '差距将会扩大',
                       'claim_type', 'aphorism', 'normative', 'trivial', 'historical', 'mechanism', 'hypothetical']:
            self.assertIn(phrase, pb.DISCOVER_PROMPT)
        self.assertIn(pb.HORIZON_IMPLICIT, rp.ASSESS_PROMPT)
        self.assertIn('到案例cutoff', rp.ASSESS_PROMPT)
        self.assertIn('出版年到案例截止日', decision_policy.DECISION_CONTRACT)
        self.assertIn('出版年到cutoff', vp.sr.REVIEW_PROMPT)
        self.assertNotIn('claim_type', pb.DISCOVER_PROMPT_V4)
        self.assertEqual(pb.EXTRACTION_VERSION, 'v5')


class ExtractionPolicy(unittest.TestCase):
    def claims(self, text, quotes, year=1996, **kw):
        chunks = pb.split_text(text)
        report = {}
        preds = [pred(quote, **kw) for quote in quotes]
        kept, _rejected = pb.validate_chunk_predictions(preds, chunks[0])
        claims = pb.claims_from_results([dict(id=chunks[0]['id'], predictions=kept)], chunks, text,
                                        'a' * 64, {'book': '测试', 'publication_year_proxy': year}, None, report)
        return claims, report

    def test_examples_are_excluded_from_the_candidate_list_and_counted(self):
        text = '同样的肉有各种烧法。新任总统要发表就职演说。信任和友谊将是罕见的。到2010年冲突将会上升。'
        quotes = ['同样的肉有各种烧法', '新任总统要发表就职演说', '信任和友谊将是罕见的', '到2010年冲突将会上升。']
        claims, report = self.claims(text, quotes, 1996)
        self.assertEqual([c['quote'] for c in claims], ['到2010年冲突将会上升。'])
        self.assertEqual(claims[0]['extraction_v2']['extraction_version'], 'v5')
        self.assertEqual(claims[0]['extraction_v2']['claim_type'], 'forecast')
        self.assertTrue(claims[0]['extraction_v2']['resolvable'])
        self.assertEqual(claims[0]['extraction_v2']['confidence'], 'unknown')
        self.assertEqual(claims[0]['extraction_v2']['horizon_source'], pb.HORIZON_EXPLICIT)
        reasons = sorted(row['reason'] for row in report['excluded'])
        self.assertEqual(reasons, ['aphorism', 'aphorism', 'trivial'])
        self.assertTrue(all(row['claim_type'] == row['reason'] for row in report['excluded']))

    def test_author_confidence_and_horizon_are_kept_when_the_quote_states_them(self):
        text = '甲国将在今后十年增加出口。'
        claims, _report = self.claims(text, ['甲国将在今后十年增加出口。'], confidence='medium',
                                      horizon='今后十年', changes='增加出口')
        extra = claims[0]['extraction_v2']
        self.assertEqual(extra['confidence'], 'medium')
        self.assertEqual(extra['horizon'], '今后十年')
        self.assertEqual(extra['changes'], '增加出口')
        self.assertIn('extraction_version', extra['provenance'])
        self.assertEqual(extra['provenance']['extraction_version'], 'v5')
        pb.validate_extraction_provenance(claims[0], {'book': '测试', 'publication_year_proxy': 1996})

    def test_undated_direction_is_stored_separately_from_a_dated_forecast(self):
        text = '差距将会扩大。到2010年冲突将会上升。'
        claims, report = self.claims(text, ['差距将会扩大。', '到2010年冲突将会上升。'], 1991)
        by_quote = {c['quote']: c['extraction_v2'] for c in claims}
        implicit = by_quote['差距将会扩大。']
        explicit = by_quote['到2010年冲突将会上升。']
        self.assertEqual(implicit['claim_type'], 'forecast')
        self.assertEqual(implicit['kind'], 'prediction')
        self.assertTrue(implicit['resolvable'])
        self.assertEqual(implicit['horizon_source'], pb.HORIZON_IMPLICIT)
        self.assertEqual(implicit['horizon'], '')
        self.assertEqual(explicit['horizon_source'], pb.HORIZON_EXPLICIT)
        self.assertEqual(report['duplicates'], 0)

    def test_overlapping_spans_of_one_sentence_collapse_below_the_old_threshold(self):
        text = '甲国将在今后十年增加出口，并且乙国将同步下降。下一句今后将会另有变化。'
        first = '甲国将在今后十年增加出口，并且乙国'
        second = '并且乙国将同步下降'
        third = '下一句今后将会另有变化。'
        overlap = len('并且乙国')
        self.assertLess(overlap, 0.8 * min(len(first), len(second)))
        claims, report = self.claims(text, [first, second, third])
        self.assertEqual(report['duplicates'], 1)
        self.assertEqual([c['quote'] for c in claims], [first, third])

    def test_non_overlapping_forecasts_in_one_sentence_both_stay(self):
        text = '甲国今后将增加出口，乙国今后将减少进口。'
        claims, report = self.claims(text, ['甲国今后将增加出口', '乙国今后将减少进口'])
        self.assertEqual(report['duplicates'], 0)
        self.assertEqual(len(claims), 2)

    def test_v4_receipt_ignores_the_v5_prompt(self):
        claim = dict(quote='q', context='c', speaker='作者', source_location={}, source_verified=True,
                     source_verification={}, extraction_v2=dict(
                         kind='prediction', claim='c', time_text='', condition_text='', method='m',
                         method_basis='unknown', reason='r'))
        receipt = pb.extraction_provenance(claim, {'book': '测试'}, 'a' * 64)
        self.assertNotIn('extraction_version', receipt)
        self.assertEqual(receipt['prompt_sha256'], hashlib.sha256(pb.DISCOVER_PROMPT_V4.encode()).hexdigest())
        self.assertNotEqual(receipt['prompt_sha256'], hashlib.sha256(pb.DISCOVER_PROMPT_V5.encode()).hexdigest())


class VerifierGuard(unittest.TestCase):
    def validate(self, claim, year=1991):
        evidence = {'e': {'verified': True, 'date': '2025-01-01'}}
        with mock.patch.object(pipeline, 'config', return_value={
                'book': 't', 'cutoff': '2026-11-08', 'publication_year_proxy': year, 'rules_version': 't'}):
            pipeline.validate_assessment(scored(claim['id']), claim, evidence)

    def test_v5_label_and_rescreen_block_a_correct_verdict(self):
        labeled = dict(id='x', quote='生活还会继续向前。', source_verified=True, duplicate_of=None,
                       extraction_v2=dict(extraction_version='v5', claim_type='aphorism', kind='prediction',
                                         resolvable=False))
        with self.assertRaisesRegex(ValueError, 'Non-forecast cannot be scored correct'):
            self.validate(labeled)
        unresolved = dict(id='x', quote='到2010年，核心国家之间的冲突将会上升。', source_verified=True,
                          duplicate_of=None, extraction_v2=dict(
                              extraction_version='v5', claim_type='unclear', kind='unclear', resolvable=False,
                              time_text='到2010年', horizon='到2010年', changes='冲突上升'))
        with self.assertRaisesRegex(ValueError, 'Non-forecast cannot be scored correct'):
            self.validate(unresolved, 1996)
        lied = dict(id='x', quote='1980年代科索沃提出了共和国地位要求。', source_verified=True, duplicate_of=None,
                    extraction_v2=dict(extraction_version='v5', claim_type='forecast', kind='prediction',
                                      resolvable=True))
        with self.assertRaisesRegex(ValueError, 'Non-forecast cannot be scored correct'):
            self.validate(lied, 1996)

    def test_v5_forecast_can_still_be_correct_and_v4_acceptance_still_loads(self):
        forecast = dict(id='x', quote='这个制度今后将会继续存在。', source_verified=True, duplicate_of=None,
                        extraction_v2=dict(extraction_version='v5', claim_type='forecast', kind='prediction',
                                          resolvable=True, time_text='今后', horizon='今后', changes='继续存在'))
        self.validate(forecast, 1991)
        implicit = dict(id='x', quote='差距将会扩大', source_verified=True, duplicate_of=None,
                        extraction_v2=dict(extraction_version='v5', claim_type='forecast', kind='prediction',
                                          resolvable=True, horizon_source=pb.HORIZON_IMPLICIT, horizon='',
                                          changes='扩大'))
        self.validate(implicit, 1991)
        accepted = dict(id='x', quote='同样的肉有各种烧法', source_verified=True, duplicate_of=None)
        self.validate(accepted, 1991)

    def test_assess_and_search_verifier_reject_the_same_sentences(self):
        item = scored('a')
        raw = {'choices': [{'finish_reason': 'stop', 'message': {'content': json.dumps({'items': [item]})}}]}
        for quote, year in [('同样的肉有各种烧法', 1991), ('新任总统要发表就职演说', 1991),
                            ('信任和友谊将是罕见的', 1996), ('1980年代科索沃提出了共和国地位要求。', 1996)]:
            case = dict(id='a', quote=quote, allowed_evidence_ids=['e'], source_verified=True,
                        publication_year_proxy=year)
            with self.subTest(quote=quote):
                with self.assertRaisesRegex(ValueError, 'nonforecast_cannot_be_scored_correct'):
                    rp.validate_items('assess', raw, [case])
                with self.assertRaisesRegex(ValueError, 'nonforecast_cannot_be_scored_correct'):
                    vp.validate_stage('assess', [item], [dict(case, extraction=None, publication_year=year)])
        kept = dict(id='a', quote='到2010年，核心国家之间的冲突将会上升。', allowed_evidence_ids=['e'],
                    source_verified=True, publication_year_proxy=1996)
        self.assertEqual(rp.validate_items('assess', raw, [kept])[0]['verdict'], '正确')
        undated = dict(id='a', quote='差距将会扩大', allowed_evidence_ids=['e'], source_verified=True,
                       publication_year_proxy=1991, extraction=dict(
                           extraction_version='v5', claim_type='forecast', kind='prediction', resolvable=True,
                           horizon_source=pb.HORIZON_IMPLICIT, horizon=''))
        self.assertEqual(rp.validate_items('assess', raw, [undated])[0]['verdict'], '正确')


if __name__ == '__main__':
    unittest.main()
