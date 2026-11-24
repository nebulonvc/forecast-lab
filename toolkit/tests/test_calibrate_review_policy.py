from copy import deepcopy
import json
from pathlib import Path
import sys
import tempfile
import threading
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import calibrate_review_policy as calibration
import semantic_review as sr


class MockRunner:
    def __init__(self, fault=None):
        self.calls, self.fault = [], fault
        self.lock = threading.Lock()
        self.legacy = calibration.legacy_prompt()

    def totals(self):
        with self.lock:
            count = len(self.calls)
        return {'estimated_cost_CNY': None if self.fault else count * .001,
                'budget_committed_CNY': count * .001, 'total_tokens': count * 10,
                'unknown_or_inflight_reserved_CNY': .001 if self.fault and count else 0}

    def call(self, stage, request, cases, batch_number):
        assert stage == 'semantic_review'
        data = json.loads(request['messages'][1]['content'])
        with self.lock:
            self.calls.append(deepcopy(request))
        ident = cases[0]['id']
        if request['messages'][0]['content'] == self.legacy and ident == 'synthetic-supported_correct':
            if self.fault == 'timeout':
                raise TimeoutError('synthetic interruption')
            if self.fault == 'schema':
                return [{'id': 'wrong-id'}]
        revise = ident in {'synthetic-unjustified_unresolved', 'synthetic-causal_overclaim',
                           'synthetic-real_condition_unknown'}
        checks = {name: 'pass' for name in sr.CHECKS}
        if revise:
            checks['verdict_logic'] = 'fail'
        return [dict(id=ident, decision='revise' if revise else 'accept', checks=checks,
                     issues=[dict(check='verdict_logic', reason='题设不支持该分类或因果断言。',
                                  evidence_id=None, source_quote=data['proposed_assessment']['reason'])] if revise else [],
                     remaining_gap='依据题设修正分类或因果断言。' if revise else '')]


class CalibrationTests(unittest.TestCase):
    def test_eight_synthetic_contracts_make_exactly_sixteen_same_input_calls(self):
        fixtures = calibration.calibration_fixtures()
        self.assertEqual(len(fixtures), 8)
        self.assertEqual(len({f['id'] for f in fixtures}), 8)
        self.assertEqual([f['expected_decisions'] for f in fixtures], [
            ['accept'], ['accept'], ['accept'], ['accept'], ['revise'], ['accept'],
            ['revise'], ['revise', 'unresolved']])
        runner = MockRunner()
        with tempfile.TemporaryDirectory() as folder:
            result = calibration.run_calibration(runner, folder)
            self.assertTrue((Path(folder) / 'policy_calibration.json').is_file())
        self.assertEqual(len(runner.calls), 16)
        for fixture in fixtures:
            pair = [r for r in result['results'] if r['fixture_id'] == fixture['id']]
            self.assertEqual(len(pair), 2)
            self.assertEqual(len({r['common_input_sha256'] for r in pair}), 1)
            self.assertEqual(len({r['request_sha256'] for r in pair}), 2)
        self.assertFalse(result['real_world_gold'])
        self.assertEqual([v['expected_matches'] for v in result['summary'].values()], [8, 8])
        self.assertEqual(result['shared_ledger_delta']['estimated_cost_CNY'], .016)
        self.assertTrue(all('expected_decisions' not in json.loads(r['messages'][1]['content']) for r in runner.calls))

    def test_schema_and_unknown_network_failure_are_not_matches_or_free_calls(self):
        for fault in ('schema', 'timeout'):
            with self.subTest(fault=fault), tempfile.TemporaryDirectory() as folder:
                runner = MockRunner(fault)
                result = calibration.run_calibration(runner, folder)
                self.assertEqual(len(runner.calls), 16)
                self.assertEqual(result['summary']['legacy']['expected_matches'], 7)
                self.assertEqual(result['summary']['shared']['expected_matches'], 8)
                failed = [r for r in result['results'] if r['status'] != 'completed']
                self.assertEqual(len(failed), 1)
                self.assertIsNone(failed[0]['expected_match'])
                self.assertIsNone(result['shared_ledger_delta']['estimated_cost_CNY'])
                self.assertEqual(result['shared_ledger_delta']['unknown_or_inflight_reserved_CNY'], .001)
                self.assertEqual(failed[0]['api_response_received'], True if fault == 'schema' else None)


if __name__ == '__main__':
    unittest.main()
