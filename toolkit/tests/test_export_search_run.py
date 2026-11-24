import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from export_search_run import export_run


class ExportSearchRunTests(unittest.TestCase):
    def test_exports_failed_tasks_and_integrity_without_source_or_request_bodies(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / 'raw'
            source.mkdir()
            row = {'claim_id': 'one', 'task_state': 'partial', 'errors': ['provider_timeout'],
                   'evidence_candidates': [{'text': 'FULL SOURCE', 'archive_sha256': 'sourcehash'}]}
            (source / 'results.jsonl').write_text(json.dumps(row) + '\n')
            (source / 'request.json').write_text('PRIVATE REQUEST')
            export_run(source, root / 'export')
            data = (root / 'export/results.jsonl').read_bytes()
            self.assertNotIn(b'FULL SOURCE', data)
            self.assertIn(b'provider_timeout', data)
            self.assertFalse((root / 'export/request.json').exists())
            provenance = json.loads((root / 'export/provenance.json').read_text())
            self.assertEqual(provenance['file_sha256']['results.jsonl'], hashlib.sha256(data).hexdigest())

    def test_credential_leak_prevents_any_export(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / 'raw'
            source.mkdir()
            (source / 'report.md').write_text('leaked-test-key')
            with patch.dict(os.environ, {'EXA_API_KEY': 'leaked-test-key'}):
                with self.assertRaisesRegex(ValueError, 'credential_detected'):
                    export_run(source, root / 'export')
            self.assertFalse((root / 'export').exists())
