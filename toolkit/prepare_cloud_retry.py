#!/usr/bin/env python3
"""Freeze only technically incomplete tasks and the previous run's remaining caps."""
import argparse
import hashlib
import json
import math
from pathlib import Path


def prepare_retry(previous, target):
    previous, target = Path(previous), Path(target)
    provenance = json.loads((previous / 'provenance.json').read_text())
    required = {'manifest.json', 'summary.json', 'results.jsonl'}
    if not required.issubset(provenance['file_sha256']):
        raise ValueError('retry_integrity_receipts_missing')
    for name in required:
        if hashlib.sha256((previous / name).read_bytes()).hexdigest() != provenance['file_sha256'][name]:
            raise ValueError('retry_export_hash_mismatch')
    manifest = json.loads((previous / 'manifest.json').read_text())
    summary = json.loads((previous / 'summary.json').read_text())
    rows = [json.loads(line) for line in (previous / 'results.jsonl').read_text().splitlines()]
    if len(rows) != len(manifest['ids']) or {r['claim_id'] for r in rows} != set(manifest['ids']):
        raise ValueError('retry_requires_complete_previous_task_inventory')
    ids = [r['claim_id'] for r in rows if r['task_state'] != 'completed']
    if not ids:
        raise ValueError('no_technically_incomplete_tasks')
    limits = {
        'budget_CNY': manifest['budget_CNY'] - summary['deepseek']['budget_committed_CNY'],
        'exa_budget_USD': manifest['exa_budget_USD'] - summary['exa']['budget_committed_USD'],
    }
    if any(not math.isfinite(v) or v <= 0 for v in limits.values()):
        raise ValueError('previous_budget_exhausted')
    target.mkdir(parents=True, exist_ok=True)
    (target / 'ids.json').write_text(json.dumps(ids) + '\n')
    (target / 'limits.json').write_text(json.dumps(limits) + '\n')
    print(json.dumps({'retry_count': len(ids), 'parent_run_id': provenance['run_id'], **limits}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--previous', type=Path, required=True)
    parser.add_argument('--target', type=Path, required=True)
    args = parser.parse_args()
    prepare_retry(args.previous, args.target)
