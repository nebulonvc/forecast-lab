import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from prepare_cloud_retry import prepare_retry


class PrepareCloudRetryTests(unittest.TestCase):
    def fixture(self, root):
        previous = root / 'previous'
        previous.mkdir()
        data = {
            'manifest.json': json.dumps({'ids': ['done', 'broken'], 'budget_CNY': 10, 'exa_budget_USD': 3}),
            'summary.json': json.dumps({'deepseek': {'budget_committed_CNY': 6}, 'exa': {'budget_committed_USD': 2}}),
            'results.jsonl': '\n'.join(json.dumps(r) for r in [
                {'claim_id': 'done', 'task_state': 'completed', 'assessment': {'verdict': '暂无法判断'}},
                {'claim_id': 'broken', 'task_state': 'partial'}]),
        }
        for name, text in data.items():
            (previous / name).write_text(text)
        (previous / 'provenance.json').write_text(json.dumps({
            'run_id': '123', 'file_sha256': {name: hashlib.sha256(text.encode()).hexdigest() for name, text in data.items()}}))
        return previous

    def test_retries_only_technical_failures_with_remaining_committed_budget(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            prepare_retry(self.fixture(root), root / 'retry')
            self.assertEqual(json.loads((root / 'retry/ids.json').read_text()), ['broken'])
            self.assertEqual(json.loads((root / 'retry/limits.json').read_text()), {'budget_CNY': 4, 'exa_budget_USD': 1})

    def test_tampered_parent_is_rejected_before_retry(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            previous = self.fixture(root)
            (previous / 'results.jsonl').write_text('{}\n')
            with self.assertRaisesRegex(ValueError, 'hash_mismatch'):
                prepare_retry(previous, root / 'retry')
            self.assertFalse((root / 'retry').exists())
