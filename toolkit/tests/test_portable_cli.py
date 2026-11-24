import csv
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

TOOLS=Path(__file__).resolve().parents[1]


class PortableCaseTests(unittest.TestCase):
    def test_new_case_has_its_own_publication_year_and_no_archive_dependency(self):
        with tempfile.TemporaryDirectory() as folder:
            case=Path(folder)/'a new case'
            def run(script,*args):
                return subprocess.run([sys.executable,str(TOOLS/script),'--case',str(case),*args],
                    cwd=folder,check=True,capture_output=True,text=True)
            run('pipeline.py','init','--book','Synthetic case','--publication-year','2007','--cutoff','2025-12-31')
            assessment=dict(id='one',inclusion='forecast',verdict='暂无法判断',basis='future',
                scope='2030 endpoint',reason='No observed trend evidence yet',limitation='Not resolved',
                evidence_ids=[],method='No reasoning in source',method_basis='unknown',
                observation_end=None,future_time_text='2030',condition_state='unconditional')
            claim=dict(id='one',page=1,quote='A future statement',context='Synthetic context',speaker='Author',
                source_verified=True,duplicate_of=None,assessment=assessment,extraction=None,review=None)
            (case/'data/claims.jsonl').write_text(json.dumps(claim)+'\n')
            run('pipeline.py','check');run('pipeline.py','report')
            summary=json.loads((case/'output/summary.json').read_text())
            self.assertEqual(summary['display_verdicts']['暂无法判断'],1)
            self.assertEqual(sum(summary['display_verdicts'].values()),1)
            with (case/'output/claims.csv').open(encoding='utf-8-sig') as f:
                self.assertEqual(next(csv.DictReader(f))['display_verdict'],'暂无法判断')
            run('run_parallel.py','--prepare-only')
            request=json.loads(next((case/'output/parallel_run').glob('*.extract.plan.json')).read_text())
            packet=json.loads(request['messages'][1]['content'])
            self.assertEqual(packet['publication_year_proxy'],2007)
            self.assertNotIn('2013',request['messages'][0]['content'])
            run('pipeline.py','freeze-review')
            run('review_unresolved.py','--prepare-only')
            manifest=json.loads((case/'output/review/api/manifest.json').read_text())
            self.assertEqual(manifest['requested'],1)

