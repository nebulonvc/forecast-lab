"""A terminal production failure must not leave an audit arm running."""
from pathlib import Path
import sys
import tempfile
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import verify_prediction as vp
from test_verify_prediction import FakeLLM, FakeExa, packet


class ReviewAuditTerminalTests(unittest.TestCase):
    def test_two_invalid_review_responses_end_the_formal_arm_as_failed(self):
        class InvalidReviewLLM(FakeLLM):
            review_attempts = 0
            def call(self, stage, request, cases, batch_number):
                if stage == 'semantic_review':
                    self.review_attempts += 1
                    digest = str(self.review_attempts) * 64
                    raise vp.rp.ResponseValidationError(digest, ValueError('semantic_review_quote_not_in_supplied_text'))
                return super().call(stage, request, cases, batch_number)
        with tempfile.TemporaryDirectory() as temporary:
            p = packet('terminal-review')
            p['review_audit'] = True
            llm = InvalidReviewLLM()
            result = vp.run_job(p, Path(temporary), llm, FakeExa())
        self.assertEqual(llm.review_attempts, 2)
        self.assertEqual(len(result['schema_repairs']), 1)
        self.assertEqual(len([x for x in result['request_receipts'] if x.get('validation_error')]), 2)
        self.assertEqual(result['task_state'], 'partial')
        self.assertIsNone(result['assessment'])
        self.assertFalse(result['autonomous_decision'])
        arm = result['review_audit']['arms']['shared_nohint']
        self.assertEqual(arm['status'], 'failed')
        self.assertEqual(arm['error'], result['errors'][-1]['error'])
        self.assertTrue(arm['schema_repaired'])
        self.assertTrue(arm['common_input_sha256'])

    def test_later_revision_failure_does_not_relabel_completed_first_review(self):
        class FailedRevisionLLM(FakeLLM):
            def call(self, stage, request, cases, batch_number):
                if stage == 'revise_assessment':
                    raise TimeoutError('synthetic revision interruption')
                return super().call(stage, request, cases, batch_number)
        with tempfile.TemporaryDirectory() as temporary:
            p = packet('later-failure')
            p['review_audit'] = True
            result = vp.run_job(p, Path(temporary), FailedRevisionLLM(review_script=['revise']), FakeExa())
        self.assertEqual(result['task_state'], 'partial')
        self.assertIsNone(result['assessment'])
        self.assertEqual(result['review_audit']['arms']['shared_nohint']['status'], 'completed')


if __name__ == '__main__':
    unittest.main()
