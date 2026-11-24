"""Post-production shadows preserve decisions, failures and provenance."""
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
sys.path[:0] = [str(Path(__file__).resolve().parents[1])]
import review_audit as ra
import verify_prediction as vp
from test_verify_prediction import FakeLLM, FakeExa, packet


class ReviewAuditTests(unittest.TestCase):
    def fixture(self, root):
        p = packet('audit-synthetic')
        p['review_audit'] = True
        formal = vp.run_job(p, root, FakeLLM(), FakeExa())
        self.assertEqual(formal['task_state'], 'completed')
        return p, formal, vp.job_directory(root, p['id'])

    def read_result(self, directory):
        result = json.loads((directory / 'result.json').read_text())
        receipt = json.loads((directory / 'receipt.json').read_text())
        self.assertEqual(receipt['sha256'], hashlib.sha256((directory / 'result.json').read_bytes()).hexdigest())
        return result

    def test_three_shadows_preserve_formal_result_and_record_comparable_inputs(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            p, before, directory = self.fixture(root)
            llm = FakeLLM()
            ra.run_audits([p], root, llm)
            after = self.read_result(directory)
            for key in ('assessment', 'task_state', 'errors', 'semantic_reviews', 'decision_trace'):
                self.assertEqual(after[key], before[key])
            self.assertEqual(len(llm.calls), 3)
            self.assertEqual(after['diagnostic_llm_calls'], 3)
            primary = after['review_audit']['arms']['shared_nohint']
            for name in ra.ARMS:
                arm = after['review_audit']['arms'][name]
                self.assertEqual(arm['status'], 'completed')
                self.assertFalse(arm['schema_repaired'])
                self.assertEqual(arm['common_input_sha256'], primary['common_input_sha256'])
                self.assertEqual(arm['primary_material_sha256'], primary['common_input_sha256'])
                self.assertTrue(arm['request_sha256'])
                self.assertTrue(arm['prompt_sha256'])
            later = FakeLLM()
            ra.run_audits([p], root, later)
            self.assertEqual(later.calls, [])

    def test_budget_failure_stays_in_audit_and_is_not_retried(self):
        class NoFunds(FakeLLM):
            count = 0
            def call(self, *args, **kwargs):
                self.count += 1
                raise ValueError('estimated_budget_reservation_exceeded')
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            p, before, directory = self.fixture(root)
            llm = NoFunds()
            ra.run_audits([p], root, llm)
            after = self.read_result(directory)
            self.assertEqual(after['assessment'], before['assessment'])
            self.assertEqual(after['task_state'], 'completed')
            self.assertEqual(after['errors'], [])
            self.assertEqual(llm.count, 3)
            for name in ra.ARMS:
                arm = after['review_audit']['arms'][name]
                self.assertEqual(arm['status'], 'failed')
                self.assertTrue(arm['request_sha256'])
                self.assertTrue(arm['prompt_sha256'])
            ra.run_audits([p], root, llm)
            self.assertEqual(llm.count, 3)

    def test_tampered_snapshot_data_or_context_cannot_reach_the_api(self):
        for field in ('data', 'context'):
            with self.subTest(field=field), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                p, before, directory = self.fixture(root)
                path = directory / 'review-audit-input.json'
                snap = json.loads(path.read_text())
                if field == 'data':
                    snap['data']['cases'][0]['quote'] = 'Tampered original.'
                else:
                    snap['context']['original_text'] = 'Tampered validation text.'
                path.write_text(json.dumps(snap))
                llm = FakeLLM()
                ra.run_audits([p], root, llm)
                after = self.read_result(directory)
                self.assertEqual(llm.calls, [])
                self.assertEqual(after['assessment'], before['assessment'])
                self.assertTrue(all(after['review_audit']['arms'][a]['status'] == 'failed' for a in ra.ARMS))

    def test_missing_snapshot_is_recorded_without_changing_completion(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            p, before, directory = self.fixture(root)
            (directory / 'review-audit-input.json').unlink()
            llm = FakeLLM()
            ra.run_audits([p], root, llm)
            after = self.read_result(directory)
            self.assertEqual(llm.calls, [])
            self.assertEqual(after['task_state'], 'completed')
            self.assertTrue(all(after['review_audit']['arms'][a]['status'] == 'missing' for a in ra.ARMS))


if __name__ == '__main__':
    unittest.main()
