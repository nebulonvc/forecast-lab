import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from diagnose_search_run import ARMS, diagnose, review_audit_summary, write_report


class DiagnoseSearchRunTests(unittest.TestCase):
    def test_stage_coverage_survives_candidate_field_omission_and_keeps_missing_bytes_unknown(self):
        a = {'id': 'a', 'source_bytes': 100, 'shown_bytes': 60, 'context_truncated': True}
        b = {'id': 'b', 'source_bytes': 20, 'shown_bytes': 20, 'context_truncated': False}
        rows = [
            {'claim_id': 'new', 'evidence_candidates': [{'id': 'a'}], 'context_coverage': {
                'assess-2': [a, b], 'semantic_review-1': [a, b],
                'semantic_review-2': [dict(a, shown_bytes=50), {'id': 'missing-byte-metadata'}]}},
            {'claim_id': 'legacy', 'evidence_candidates': [{'id': 'legacy-source'}]},
        ]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'results.jsonl').write_text(''.join(json.dumps(row) + '\n' for row in rows))
            report = diagnose([root])
        self.assertEqual(report['search']['context_truncation_not_recorded'], 2)
        coverage = report['context_coverage']
        self.assertEqual(coverage['tasks_with_recorded_stages'], 1)
        self.assertEqual(coverage['tasks_missing_coverage_field'], 1)
        assess = coverage['by_stage']['assess']
        self.assertEqual((assess['source_appearances'], assess['truncated_appearances']), (2, 1))
        self.assertEqual((assess['shown_bytes'], assess['source_bytes']), (80, 120))
        review = coverage['by_stage']['semantic_review']
        self.assertEqual((review['tasks'], review['stage_snapshots'], review['source_appearances']), (1, 2, 4))
        self.assertEqual((review['truncated_appearances'], review['truncation_unknown_appearances']), (2, 1))
        self.assertIsNone(review['shown_bytes'])
        self.assertIsNone(review['source_bytes'])
        self.assertEqual((review['known_shown_bytes'], review['known_source_bytes']), (130, 220))

    def test_repaired_or_unrecorded_protocol_is_excluded_from_paired_conclusions(self):
        arms = {name: {'status': 'completed', 'common_input_sha256': 'a' * 64,
                       'schema_repaired': False, 'review': {'decision': 'accept'}} for name in ARMS}
        repaired = {name: dict(arm) for name, arm in arms.items()}
        repaired['shared_nohint'].update(schema_repaired=True, review={'decision': 'revise'})
        missing = {name: dict(arm) for name, arm in arms.items()}
        missing['shared_hint'].pop('schema_repaired')
        result = review_audit_summary([{'review_audit': {'selected': True, 'arms': sample}}
                                       for sample in (repaired, missing)])
        self.assertEqual(result['all_four_same_material_hash'], 2)
        self.assertEqual(result['all_four_same_protocol'], 0)
        self.assertEqual(result['all_four_excluded_schema_repair_or_missing'], 2)
        pair = result['paired_changes'][1]
        self.assertEqual(pair['all_material_hash_pairs'], 2)
        self.assertEqual(pair['same_protocol_pairs'], 0)
        self.assertEqual(pair['changed_decisions_same_material'], 0)
        self.assertEqual(pair['excluded_schema_repair_pairs'], 1)
        self.assertEqual(pair['excluded_missing_schema_repair_flag_pairs'], 1)

    def test_latest_results_trace_precedence_and_paired_audit_keep_unknown_costs(self):
        def row(ident, draft, final, decision='accept', warning=False):
            return {'claim_id': ident, 'version': 'search-verifier-v1', 'task_state': 'completed',
                    'raw_assessment': {'verdict': '正确', 'evidence_ids': ['ev']},
                    'draft_history': [{'verdict': draft}], 'assessment': {'verdict': final},
                    'semantic_reviews': [{'decision': decision}],
                    'validation_warnings': [{'code': 'publication_date_unconfirmed'}] if warning else [],
                    'evidence_candidates': [{'id': 'ev', 'published_date': None}]}

        a = row('a', '正确', '暂无法判断', warning=True)
        b = row('b', '暂无法判断', '暂无法判断')
        c = row('c', '正确', '暂无法判断', decision='revise')
        d = row('d', '暂无法判断', '暂无法判断')
        d['decision_trace'] = [{'round': 1, 'draft_verdict': '正确', 'mechanical_verdict': '正确',
                                'warnings': [], 'review_decision': 'revise'}]
        arms = {name: {'status': 'completed', 'common_input_sha256': 'a' * 64, 'schema_repaired': False,
                       'review': {'decision': 'revise' if name.endswith('_hint') else 'accept', 'checks': {}}} for name in ARMS}
        a['review_audit'] = {'selected': True, 'arms': arms}
        d['review_audit'] = {'selected': True, 'arms': {name: dict(arm) for name, arm in arms.items()}}
        d['review_audit']['arms']['shared_nohint'] = {'status': 'failed', 'error': 'timeout', 'common_input_sha256': 'a' * 64}
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            runs = [root / 'first', root / 'recovery']
            for path, records, fee in zip(runs, [[a, b, c, d], [row('b', '正确', '正确')]], [1, .5]):
                path.mkdir()
                (path / 'results.jsonl').write_text(''.join(json.dumps(r) + '\n' for r in records))
                (path / 'summary.json').write_text(json.dumps({'deepseek': {'estimated_cost_CNY': fee}}))
            report = diagnose(runs)
            self.assertEqual((report['unique_predictions'], report['task_attempts']), (4, 5))
            self.assertEqual(report['terminal_origins'], {
                'mechanical_downgrade': 1, 'determinate': 1, 'last_review_rejected': 1, 'draft_already_unresolved': 1})
            exposure = report['initial_date_exposure_cross']
            self.assertEqual(sum(r['count'] for r in exposure if r['method'] == 'legacy_metadata_reconstruction'), 3)
            self.assertEqual(sum(r['count'] for r in exposure if r['method'] == 'recorded_decision_trace' and r['exposure'] == 'no_mechanical_downgrade'), 1)
            audit = report['same_material_review_audit']
            self.assertEqual((audit['selected_samples'], audit['all_four_completed'], audit['all_four_same_material_hash']), (2, 1, 2))
            self.assertEqual(audit['arms']['shared_nohint']['failed_or_missing'], 1)
            self.assertEqual(audit['paired_changes'][1]['changed_decisions_same_material'], 1)
            self.assertEqual(report['fees_by_currency']['deepseek_CNY']['estimated_cost_CNY']['total'], 1.5)
            self.assertEqual(report['adaptive_search']['tasks_with_adaptive_rounds'], 0)
            self.assertIsNone(report['fees_by_currency']['exa_USD']['estimated_cost_USD']['total'])
            write_report(report, root / 'report')
            self.assertTrue((root / 'report/diagnosis.md').stat().st_size > 0)


if __name__ == '__main__':
    unittest.main()
