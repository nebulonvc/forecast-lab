#!/usr/bin/env python3
"""Review only the frozen unresolved set; retain all responses, never import them.

Uses the shared DeepSeek runner for bounded concurrency, request caching and
conservative accounting. Supplementary research is advisory, never a gold label.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import fcntl
import hashlib
import json
import os
from pathlib import Path
import sys

import run_parallel as rp

ROOT = Path.cwd()


def without_receipt(value):
    return {k: v for k, v in value.items() if k != 'receipt'}


def compact_research(note):
    result = {k: note[k] for k in ('change_reason', 'evidence_ids', 'reason', 'notes') if k in note}
    suggestion = note.get('recommendation')
    if isinstance(suggestion, dict):
        result['recommendation'] = {k: suggestion[k] for k in
            ('inclusion', 'verdict', 'basis', 'scope', 'reason', 'limitation', 'evidence_ids',
             'trend_aligned', 'observation_end', 'future_time_text', 'condition_state') if k in suggestion}
    elif suggestion is not None:
        result['recommendation'] = suggestion
    return result


def prepare_batches(root, frozen_file, research_dir, batch_size=6, max_tokens=8000, model='deepseek-flash'):
    config = rp.read_json(root / 'config.json')
    frozen = rp.read_json(frozen_file)
    rows = [c for c in frozen if (c.get('assessment') or {}).get('verdict') == '暂无法判断']
    ids = [c['id'] for c in rows]
    if len(ids) != len(set(ids)):
        raise ValueError('duplicate_frozen_unresolved_ids')
    current = {c['id']: c for c in rp.read_jsonl(root / 'data/claims.jsonl')}
    if any(i not in current for i in ids):
        raise ValueError('frozen_id_missing_from_current_claims')
    evidence = {e['id']: e for e in rp.read_jsonl(root / 'data/evidence.jsonl')}
    research = {}
    for path in sorted(research_dir.glob('research_*.jsonl')):
        for note in rp.read_jsonl(path):
            ident = note['id']
            if ident in research:
                raise ValueError('duplicate_research_id_' + ident)
            research[ident] = note
    links_path = root / 'output/evidence_links.json'
    links = rp.read_json(links_path) if links_path.exists() else {}
    cases = []
    for prior in rows:
        c = current[prior['id']]
        note = research.get(c['id'], {})
        recommendation = note.get('recommendation') or {}
        ref_lists = [prior['assessment'].get('evidence_ids', []), note.get('evidence_ids', []),
                     links.get(c['id'], [])]
        if isinstance(recommendation, dict):
            ref_lists.append(recommendation.get('evidence_ids', []))
        refs = sorted({i for group in ref_lists for i in group})
        if any(i not in evidence for i in refs):
            raise ValueError('research_evidence_not_registered_' + c['id'])
        refs = [i for i in refs if evidence[i].get('verified')]
        cases.append({**{k: c.get(k) for k in ('id', 'page', 'quote', 'context', 'speaker', 'duplicate_of', 'source_verified')},
                      'extraction': without_receipt(c.get('extraction_v2') or {}),
                      'prior_assessment': without_receipt(prior['assessment']),
                      'research_notes': compact_research(note),
                      'allowed_evidence_ids': refs})
    batches = []

    def append_batch(group):
        refs = sorted({i for case in group for i in case['allowed_evidence_ids']})
        packet = {'book': config['book'], 'cutoff': config['cutoff'],
                  'publication_year_proxy': config.get('publication_year_proxy'),
                  'task': '仅复核冻结的暂无法判断记录；允许有证据的趋势归部分符合，不能为了减少未知强行改判。',
                  'cases': group,
                  'evidence': [{k: evidence[i].get(k) for k in
                               ('id', 'url', 'date', 'coverage', 'excerpt', 'summary', 'limitation', 'verified')}
                              for i in refs]}
        request = rp.payload('assess', packet, max_tokens, model)
        if len(rp.canonical(request)) > rp.MAX_REQUEST_BYTES:
            if len(group) == 1:
                raise ValueError('single_review_case_exceeds_request_limit_' + group[0]['id'])
            mid = len(group) // 2
            append_batch(group[:mid])
            append_batch(group[mid:])
        else:
            batches.append((len(batches) + 1, request, group))

    for start in range(0, len(cases), batch_size):
        append_batch(cases[start:start + batch_size])
    return rows, batches, {'research_covered': sum(i in research for i in ids),
                           'research_missing_ids': [i for i in ids if i not in research]}


def recover_raw_items(directory, request, cases):
    """Recover reviewable JSON from a rejected response without calling again."""
    digest = hashlib.sha256(rp.canonical(request)).hexdigest()
    path = directory / (digest + '.response.json')
    if not path.exists():
        return [], 'no_response'
    try:
        raw = rp.read_json(path)
        choices = raw.get('choices') or []
        if not choices or choices[0].get('finish_reason') != 'stop':
            return [], 'response_incomplete'
        items = json.loads(choices[0]['message']['content'])['items']
        if not isinstance(items, list) or any(not isinstance(x, dict) for x in items):
            return [], 'invalid_items'
        ids = [x.get('id') for x in items]
        if len(ids) != len(set(ids)) or set(ids) != {c['id'] for c in cases}:
            return [], 'raw_id_coverage_mismatch'
        return items, 'recovered_for_local_review_only'
    except (ValueError, KeyError, TypeError):
        return [], 'raw_json_unreadable'


def main(argv=None):
    global ROOT
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--case', type=Path, required=True)
    parser.add_argument('--key-file', type=Path)
    parser.add_argument('--workers', type=int, default=12)
    parser.add_argument('--batch-size', type=int, default=6)
    parser.add_argument('--budget-cny', type=float, default=5.0)
    parser.add_argument('--max-tokens', type=int, default=8000)
    parser.add_argument('--model', default='deepseek-flash')
    parser.add_argument('--timeout', type=int, default=180)
    parser.add_argument('--prepare-only', action='store_true')
    parser.add_argument('--frozen-file', type=Path, default=None)
    parser.add_argument('--research-dir', type=Path, default=None)
    parser.add_argument('--output-dir', type=Path, default=None)
    args = parser.parse_args(argv)
    ROOT = args.case.resolve()
    args.research_dir = args.research_dir or ROOT / 'output/review'
    args.frozen_file = args.frozen_file or args.research_dir / 'before_book_index.json'
    args.output_dir = args.output_dir or args.research_dir / 'api'
    if not (1 <= args.workers <= 20 and 1 <= args.batch_size <= 32 and args.budget_cny > 0
            and 1 <= args.max_tokens <= 8192 and args.timeout > 0):
        parser.error('workers 1..20; batch-size 1..32; max-tokens 1..8192; positive budget and timeout')
    args.output_dir.mkdir(parents=True, exist_ok=True)
    with (args.output_dir / 'run.lock').open('a') as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise ValueError('another_runner_owns_output_directory') from None
        rows, batches, research_coverage = prepare_batches(ROOT, args.frozen_file, args.research_dir,
                                                          args.batch_size, args.max_tokens, args.model)
        manifest = {'prepared_at': rp.now(), 'stage': 'assess_only', 'requested': len(rows),
                    'ids': [c['id'] for c in rows], 'workers': args.workers, 'batches': len(batches),
                    'model': args.model, 'budget_CNY': args.budget_cny, 'max_tokens': args.max_tokens,
                    'frozen_sha256': hashlib.sha256(args.frozen_file.read_bytes()).hexdigest(),
                    'config_sha256': hashlib.sha256((ROOT / 'config.json').read_bytes()).hexdigest(),
                    'request_bytes': [len(rp.canonical(request)) for _, request, _ in batches],
                    'actual_batch_sizes': [len(cases) for _, _, cases in batches], **research_coverage}
        rp.save_json(args.output_dir / 'manifest.json', manifest)
        if args.prepare_only:
            for number, request, _ in batches:
                rp.save_json(args.output_dir / f'batch_{number:03d}.assess.plan.json', request)
            print(json.dumps({'event': 'prepared', **manifest}, ensure_ascii=False))
            return 0
        secret = (args.key_file.read_text().strip() if args.key_file else
                  (os.getenv('BOOKPRED_DEEPSEEK_API_KEY') or os.getenv('DEEPSEEK_API_KEY', '')).strip())
        if not secret:
            raise ValueError('missing_DeepSeek_key_use_environment_or_key_file')
        runner = rp.Runner(args.output_dir, secret, args.budget_cny, args.timeout)
        validated, proposals, failures = [], [], []
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            futures = {pool.submit(runner.call, 'assess', request, cases, number): (number, request, cases)
                       for number, request, cases in batches}
            for future in as_completed(futures):
                number, request, cases = futures[future]
                try:
                    result = future.result()
                    validated.extend(result)
                    proposals.extend(result)
                except Exception as exc:
                    recovered, status = recover_raw_items(args.output_dir, request, cases)
                    proposals.extend(recovered)
                    failures.append({'batch': number, 'error': str(exc) if isinstance(exc, ValueError) else type(exc).__name__,
                                     'recovery_status': status, 'recovered_items': len(recovered)})
        order = {c['id']: n for n, c in enumerate(rows)}
        rp.save_jsonl(args.output_dir / 'assessment_validated.jsonl', sorted(validated, key=lambda x: order[x['id']]))
        rp.save_jsonl(args.output_dir / 'assessment_proposals.jsonl', sorted(proposals, key=lambda x: order[x['id']]))
        summary = {'complete': not failures and len(validated) == len(rows),
                   'requested': len(rows), 'validated_records': len(validated), 'raw_proposal_records': len(proposals),
                   'raw_proposal_coverage_complete': {x['id'] for x in proposals} == set(order),
                   'imported': False, 'full_book_complete': False, 'stage': 'assess_only',
                   'failures': failures, **runner.totals()}
        rp.save_json(args.output_dir / 'summary.json', summary)
        print(json.dumps(summary, ensure_ascii=False), flush=True)
        return 0 if summary['complete'] else 2


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (ValueError, OSError) as exc:
        print('Review stopped: ' + (str(exc) if isinstance(exc, ValueError) else type(exc).__name__), file=sys.stderr)
        sys.exit(2)
