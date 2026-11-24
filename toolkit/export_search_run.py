#!/usr/bin/env python3
"""Export machine results without source bodies, prompts, responses or credentials."""
import argparse
from copy import deepcopy
import hashlib
import json
import os
from pathlib import Path


def export_run(source, target):
    source, target = Path(source), Path(target)
    files = {}
    for name in ('manifest.json', 'summary.json', 'report.md', 'policy_calibration.json'):
        path = source / name
        if path.is_file():
            files[name] = path.read_bytes()
    results = []
    result_file = source / 'results.jsonl'
    if result_file.exists():
        for line in result_file.read_text(encoding='utf-8').splitlines():
            result = deepcopy(json.loads(line))
            for candidate in result.get('evidence_candidates', []):
                candidate.pop('text', None)
                candidate['source_body_in_export'] = False
            results.append(result)
            key = hashlib.sha256(result['claim_id'].encode()).hexdigest()[:24]
            name = f'jobs/{key}/result.json'
            files[name] = (json.dumps(result, ensure_ascii=False, indent=2) + '\n').encode()
    files['results.jsonl'] = ''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in results).encode()
    provenance = {
        'commit': os.getenv('GITHUB_SHA'), 'run_id': os.getenv('GITHUB_RUN_ID'),
        'run_attempt': os.getenv('GITHUB_RUN_ATTEMPT'),
        'parent_run_id': os.getenv('PREVIOUS_RUN') or None,
        'run_url': (f"https://github.com/{os.getenv('GITHUB_REPOSITORY')}/actions/runs/"
                    f"{os.getenv('GITHUB_RUN_ID')}") if os.getenv('GITHUB_RUN_ID') else None,
        'completed_results': len(results), 'human_semantic_review': False,
        'export_note': 'Source bodies and API request/response bodies omitted. Results are machine judgments.',
        'file_sha256': {name: hashlib.sha256(data).hexdigest() for name, data in files.items()},
        'raw_result_sha256': hashlib.sha256(result_file.read_bytes()).hexdigest() if result_file.exists() else None,
    }
    files['provenance.json'] = (json.dumps(provenance, ensure_ascii=False, indent=2) + '\n').encode()
    secrets = [os.getenv(name, '').encode() for name in
               ('BOOKPRED_DEEPSEEK_API_KEY', 'DEEPSEEK_API_KEY', 'EXA_API_KEY') if os.getenv(name)]
    if any(secret in data for data in files.values() for secret in secrets):
        raise ValueError('credential_detected_export_refused')
    if target.exists():
        raise ValueError('export_directory_must_be_new')
    for name, data in files.items():
        path = target / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    print(json.dumps({'exported_results': len(results), 'files': len(files), 'output': str(target)}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--target', type=Path, required=True)
    args = parser.parse_args()
    export_run(args.source, args.target)
