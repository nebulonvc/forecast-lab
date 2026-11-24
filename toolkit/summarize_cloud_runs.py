#!/usr/bin/env python3
"""Combine a cloud run and its focused recoveries without rejudging any claim."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path


def summarize(runs, output):
    output = Path(output).resolve()
    output.mkdir(parents=True, exist_ok=True)
    final, locations, history = {}, {}, []
    previous_id = None
    costs = {'estimated_CNY': 0, 'committed_CNY': 0, 'estimated_USD': 0, 'committed_USD': 0}
    for folder in runs:
        folder = Path(folder).resolve()
        provenance = json.loads((folder / 'provenance.json').read_text())
        for name, checksum in provenance['file_sha256'].items():
            path = (folder / name).resolve()
            if not path.is_relative_to(folder) or hashlib.sha256(path.read_bytes()).hexdigest() != checksum:
                raise ValueError('cloud_export_integrity_failed')
        if provenance.get('parent_run_id') != previous_id:
            raise ValueError('cloud_run_chain_mismatch')
        summary = json.loads((folder / 'summary.json').read_text())
        rows = [json.loads(line) for line in (folder / 'results.jsonl').read_text().splitlines()]
        manifest = json.loads((folder / 'manifest.json').read_text())
        if len(rows) != len(manifest['ids']) or {r['claim_id'] for r in rows} != set(manifest['ids']):
            raise ValueError('cloud_result_inventory_mismatch')
        if history and set(manifest['ids']) != {i for i, r in final.items() if r['task_state'] != 'completed'}:
            raise ValueError('recovery_must_cover_only_incomplete_tasks')
        for row in rows:
            ident = row['claim_id']
            final[ident] = row
            key = hashlib.sha256(ident.encode()).hexdigest()[:24]
            locations[ident] = (folder / 'jobs' / key / 'result.json').relative_to(output).as_posix()
        for provider, currency in (('deepseek', 'CNY'), ('exa', 'USD')):
            costs['estimated_' + currency] += summary[provider]['estimated_cost_' + currency]
            costs['committed_' + currency] += summary[provider]['budget_committed_' + currency]
        history.append({'run_id': provenance['run_id'], 'url': provenance['run_url'],
                        'commit': provenance['commit'], 'requested': len(rows),
                        'task_states': summary['task_states'],
                        'deepseek': summary['deepseek'], 'exa': summary['exa']})
        previous_id = provenance['run_id']
    states = Counter(r['task_state'] for r in final.values())
    verdicts = Counter('趋势符合' if r['assessment'].get('trend_aligned') else r['assessment']['verdict']
                       for r in final.values() if r['task_state'] == 'completed')
    combined = {'unique_predictions': len(final), 'task_attempts': sum(r['requested'] for r in history),
                'task_states': dict(states), 'completed_verdicts': dict(verdicts),
                'costs': {k: round(v, 8) for k, v in costs.items()},
                'human_semantic_review': False, 'runs': history}
    (output / 'summary.json').write_text(json.dumps(combined, ensure_ascii=False, indent=2) + '\n')
    lines = ['# 整书云端 API 运行结果', '',
             '统计由程序从各轮产物生成，没有人工检查或改判预测。任务内由 API 搜证、初判、复核及有限修正；技术完成不等于预测获证实。', '',
             f"独立预测：{len(final)}；任务尝试：{combined['task_attempts']}（含技术失败后的恢复）。", '',
             '最终技术状态：' + json.dumps(dict(states), ensure_ascii=False) + '。', '',
             '已完成任务的判断：' + json.dumps(dict(verdicts), ensure_ascii=False) + '。', '',
             f"累计费用估计：LLM ¥{costs['estimated_CNY']:.6f}；Exa ${costs['estimated_USD']:.6f}。失败尝试计入，未知预留见 summary.json；未核对正式账单。", '',
             '|运行|任务数|技术状态|', '|---|---:|---|']
    for row in history:
        lines.append(f"|[{row['run_id']}]({row['url']})|{row['requested']}|{json.dumps(row['task_states'], ensure_ascii=False)}|")
    lines.extend(['', '|预测ID|最终运行状态|判断|缺口或技术错误|', '|---|---|---|---|'])
    for ident, row in final.items():
        item = row.get('assessment') or {}
        verdict = '趋势符合' if item.get('trend_aligned') else item.get('verdict', '未产生有效建议')
        detail = row.get('remaining_gap') or ''
        if row.get('errors'):
            detail += ' ' + json.dumps(row['errors'], ensure_ascii=False)
        detail = detail.replace('|', '\\|').replace('\n', ' ')
        lines.append(f"|[{ident}]({locations[ident]})|{row['task_state']}|{verdict}|{detail}|")
    lines.extend(['', '各轮原始机器导出分目录保存，引用、反证及复核过程见逐条结果。来源全文与 API 原始正文未导出；未覆盖历史已接受案例。', ''])
    (output / 'report.md').write_text('\n'.join(lines), encoding='utf-8')
    print(json.dumps({k: v for k, v in combined.items() if k != 'runs'}, ensure_ascii=False))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('runs', nargs='+', type=Path, help='Initial export, then recoveries in order')
    parser.add_argument('--output-dir', required=True, type=Path)
    args = parser.parse_args()
    summarize(args.runs, args.output_dir)
