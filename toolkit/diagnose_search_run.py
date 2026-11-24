#!/usr/bin/env python3
"""Diagnose recorded decision paths without adjudicating claims or calling APIs."""
import argparse
from collections import Counter
import json
import math
from pathlib import Path


UNRESOLVED = '暂无法判断'
ARMS = ('legacy_hint', 'legacy_nohint', 'shared_hint', 'shared_nohint')


def verdict(assessment):
    assessment = assessment or {}
    return '趋势符合' if assessment.get('trend_aligned') else assessment.get('verdict') or 'not_recorded'


def counter_rows(counter, fields):
    return [dict(zip(fields, key)) | {'count': count} for key, count in sorted(counter.items())]


def terminal_origin(row):
    """Mutually exclusive paths, not a judgment about the truth of any verdict."""
    if row.get('task_state') != 'completed' or not row.get('assessment'):
        return 'technical_incomplete'
    if verdict(row['assessment']) != UNRESOLVED:
        return 'determinate'
    drafts = row.get('draft_history') or [row.get('raw_assessment') or {}]
    if verdict(drafts[-1]) == UNRESOLVED:
        return 'draft_already_unresolved'
    reviews = row.get('semantic_reviews') or []
    if row.get('semantic_validation') == 'unresolved' or (reviews and reviews[-1].get('decision') in {'revise', 'unresolved'}):
        return 'last_review_rejected'
    trace = row.get('decision_trace') or []
    changed = (trace and trace[-1].get('draft_verdict') != UNRESOLVED
               and trace[-1].get('mechanical_verdict') == UNRESOLVED)
    if verdict(drafts[-1]) != 'not_recorded' and (row.get('validation_warnings') or changed):
        return 'mechanical_downgrade'
    return 'unattributed_unresolved'


def initial_date_exposure(row):
    """Legacy metadata reconstruction is not a rule for newer policies."""
    if 'decision_trace' in row:
        trace = row['decision_trace']
        if not isinstance(trace, list) or not trace:
            return 'recorded_decision_trace', 'not_recorded'
        first = trace[0]
        if not first.get('draft_verdict') or not first.get('mechanical_verdict'):
            return 'recorded_decision_trace', 'not_recorded'
        changed = first['draft_verdict'] != UNRESOLVED and first['mechanical_verdict'] == UNRESOLVED
        return 'recorded_decision_trace', 'mechanical_unresolved' if changed else 'no_mechanical_downgrade'
    if row.get('version') != 'search-verifier-v1':
        return 'policy_not_recorded', 'not_inferred'
    sources = {e['id']: e for e in row.get('evidence_candidates', [])}
    references = (row.get('raw_assessment') or {}).get('evidence_ids')
    if not isinstance(references, list) or any(ident not in sources for ident in references):
        return 'legacy_metadata_reconstruction', 'not_recorded'
    return 'legacy_metadata_reconstruction', 'yes' if any(not sources[ident].get('published_date') for ident in references) else 'no'


def review_audit_summary(rows):
    selected = [row['review_audit'] for row in rows if (row.get('review_audit') or {}).get('selected')]

    def review(arm):
        return arm.get('review') or arm

    def completed(arm):
        return (arm.get('status') in {'completed', 'success'} and not arm.get('error')
                and review(arm).get('decision') in {'accept', 'revise', 'unresolved'})

    def fingerprint(arm):
        value = arm.get('common_input_sha256')
        return value if isinstance(value, str) and len(value) == 64 else None

    arms = {}
    for name in ARMS:
        entries = [sample.get('arms', {}).get(name, {}) for sample in selected]
        valid = [arm for arm in entries if completed(arm)]
        arms[name] = {
            'statuses': dict(Counter(arm.get('status', 'not_recorded') for arm in entries)),
            'completed': len(valid), 'failed_or_missing': len(entries) - len(valid),
            'schema_repaired': sum(arm.get('schema_repaired') is True for arm in entries),
            'schema_repair_flag_missing': sum(type(arm.get('schema_repaired')) is not bool for arm in entries),
            'decisions': dict(Counter(review(arm)['decision'] for arm in valid)),
            'nonpass_checks': counter_rows(Counter((key, value) for arm in valid for key, value in review(arm).get('checks', {}).items() if value != 'pass'), ('check', 'value')),
        }
    pairs = []
    for left, right in [('legacy_hint', 'legacy_nohint'), ('shared_hint', 'shared_nohint'),
                        ('legacy_hint', 'shared_hint'), ('legacy_nohint', 'shared_nohint')]:
        decisions, completed_pairs, same_hash, comparable = Counter(), 0, 0, 0
        excluded_repair, excluded_missing_flag = 0, 0
        for sample in selected:
            a, b = (sample.get('arms', {}).get(name, {}) for name in (left, right))
            if completed(a) and completed(b):
                completed_pairs += 1
                if fingerprint(a) and fingerprint(a) == fingerprint(b):
                    same_hash += 1
                    if a.get('schema_repaired') is False and b.get('schema_repaired') is False:
                        comparable += 1
                        decisions[(review(a)['decision'], review(b)['decision'])] += 1
                    elif a.get('schema_repaired') is True or b.get('schema_repaired') is True:
                        excluded_repair += 1
                    else:
                        excluded_missing_flag += 1
        pairs.append({'left': left, 'right': right, 'completed_pairs': completed_pairs,
                      'all_material_hash_pairs': same_hash,
                      'same_material_pairs': comparable, 'same_protocol_pairs': comparable,
                      'excluded_schema_repair_or_missing_pairs': same_hash - comparable,
                      'excluded_schema_repair_pairs': excluded_repair,
                      'excluded_missing_schema_repair_flag_pairs': excluded_missing_flag,
                      'changed_decisions_same_material': sum(n for (a, b), n in decisions.items() if a != b),
                      'transitions_same_material': counter_rows(decisions, ('left_decision', 'right_decision'))})
    same_all, completed_all, comparable_all, excluded_all = 0, 0, 0, 0
    for sample in selected:
        entries = [sample.get('arms', {}).get(name, {}) for name in ARMS]
        hashes = [fingerprint(arm) for arm in entries]
        same = all(hashes) and len(set(hashes)) == 1
        success = all(completed(arm) for arm in entries)
        same_all += same
        completed_all += success
        if same and success:
            clean_protocol = all(arm.get('schema_repaired') is False for arm in entries)
            comparable_all += clean_protocol
            excluded_all += not clean_protocol
    return {'selected_samples': len(selected), 'all_four_completed': completed_all,
            'all_four_same_material_hash': same_all, 'all_four_same_protocol': comparable_all,
            'all_four_excluded_schema_repair_or_missing': excluded_all,
            'comparison_policy': 'Primary comparisons require completed arms, identical material hashes and explicit schema_repaired=false on both sides. Repaired or unrecorded protocols remain counted as exclusions.',
            'arms': arms, 'paired_changes': pairs,
            'limitation': 'Paired changes measure recorded prompt/hint sensitivity, not correctness against an independent truth standard.'}


def fee_totals(summaries, provider, currency):
    result = {}
    for field in ('estimated_cost_' + currency, 'budget_committed_' + currency,
                  'unknown_or_inflight_reserved_' + currency):
        values = [(summary.get(provider) or {}).get(field) for summary in summaries]
        known = [v for v in values if type(v) in (int, float) and math.isfinite(v) and v >= 0]
        result[field] = {'total': round(sum(known), 8) if len(known) == len(values) else None,
                         'known_subtotal': round(sum(known), 8), 'missing_runs': len(values) - len(known)}
    return result


def context_coverage_summary(rows):
    """Stage snapshots are separate from optional candidate-level metadata."""
    stages, tasks_with_stages = {}, set()
    missing, invalid, empty = 0, 0, 0
    for task_number, row in enumerate(rows):
        if 'context_coverage' not in row:
            missing += 1
            continue
        coverage = row['context_coverage']
        if not isinstance(coverage, dict):
            invalid += 1
            continue
        empty += not coverage
        for stage_key, sources in coverage.items():
            if not isinstance(sources, list):
                continue
            tasks_with_stages.add(task_number)
            name, _, suffix = stage_key.rpartition('-')
            stage = name if name and suffix.isdigit() else stage_key
            record = stages.setdefault(stage, {'tasks': set(), 'stage_keys': Counter(), 'sources': []})
            record['tasks'].add(task_number)
            record['stage_keys'][stage_key] += 1
            record['sources'].extend(source if isinstance(source, dict) else {} for source in sources)
    by_stage = {}
    for stage, record in sorted(stages.items()):
        sources = record['sources']
        summary = {'tasks': len(record['tasks']), 'stage_snapshots': sum(record['stage_keys'].values()),
                   'recorded_stage_keys': dict(record['stage_keys']), 'source_appearances': len(sources),
                   'truncated_appearances': sum(source.get('context_truncated') is True for source in sources),
                   'not_truncated_appearances': sum(source.get('context_truncated') is False for source in sources),
                   'truncation_unknown_appearances': sum(type(source.get('context_truncated')) is not bool for source in sources)}
        for field in ('shown_bytes', 'source_bytes'):
            known = [source[field] for source in sources if type(source.get(field)) is int and source[field] >= 0]
            summary[field] = sum(known) if len(known) == len(sources) else None
            summary['known_' + field] = sum(known)
            summary['missing_' + field + '_appearances'] = len(sources) - len(known)
        by_stage[stage] = summary
    return {'tasks_total': len(rows), 'tasks_with_recorded_stages': len(tasks_with_stages),
            'tasks_without_recorded_stages': len(rows) - len(tasks_with_stages),
            'tasks_missing_coverage_field': missing, 'tasks_invalid_coverage_field': invalid,
            'tasks_empty_coverage': empty, 'by_stage': by_stage,
            'meaning': 'Prepared stage/round snapshots, not proof of successful API consumption. Sources appearing in multiple snapshots count repeatedly; byte totals refer to the supplied source body, not necessarily the full original page. Missing byte values stay null.'}


def adaptive_summary(rows):
    """Count extra search rounds recorded by the verifier. Absence means the field was not recorded."""
    with_history = with_adaptive = resolved = 0
    round_count = 0
    for row in rows:
        history = row.get('round_history')
        if not isinstance(history, list):
            continue
        with_history += 1
        adaptive = [entry for entry in history if isinstance(entry, dict) and entry.get('kind') == 'adaptive']
        if not adaptive:
            continue
        with_adaptive += 1
        round_count += len(adaptive)
        if verdict(row.get('assessment')) != UNRESOLVED:
            resolved += 1
    return {'tasks_with_round_history': with_history, 'tasks_with_adaptive_rounds': with_adaptive,
            'adaptive_rounds': round_count, 'tasks_resolved_after_adaptive_rounds': resolved,
            'tasks_still_unresolved_after_adaptive_rounds': with_adaptive - resolved}


def diagnose(run_dirs):
    latest, summaries, runs, attempts = {}, [], [], 0
    paths = [Path(path).resolve() for path in run_dirs]
    if not paths or len(set(paths)) != len(paths):
        raise ValueError('distinct_ordered_run_directories_required')
    for path in paths:
        rows = [json.loads(line) for line in (path / 'results.jsonl').read_text().splitlines() if line.strip()]
        ids = [row['claim_id'] for row in rows]
        if len(ids) != len(set(ids)):
            raise ValueError('duplicate_claim_within_run')
        summary_path = path / 'summary.json'
        summaries.append(json.loads(summary_path.read_text()) if summary_path.exists() else {})
        runs.append({'directory': str(path), 'task_attempts': len(rows)})
        attempts += len(rows)
        latest.update({row['claim_id']: row for row in rows})
    rows = list(latest.values())
    transitions, first_reviews, dates = Counter(), Counter(), Counter()
    reviews = [review for row in rows for review in row.get('semantic_reviews', [])]
    sources = [source for row in rows for source in row.get('evidence_candidates', [])]
    queries = [query for row in rows for query in row.get('queries', [])]
    for row in rows:
        raw = verdict(row.get('raw_assessment'))
        draft = verdict((row.get('draft_history') or [row.get('raw_assessment')])[-1])
        transitions[(raw, draft, verdict(row.get('assessment')))] += 1
        first = (row.get('semantic_reviews') or [{}])[0].get('decision', 'not_recorded')
        first_reviews[(raw, first)] += 1
        method, exposure = initial_date_exposure(row)
        dates[(method, exposure, raw, first)] += 1
    result_counts = [q.get('result_count') for q in queries]
    known_hits = [v for v in result_counts if type(v) is int and v >= 0]
    return {
        'unique_predictions': len(rows), 'task_attempts': attempts, 'runs_in_override_order': runs,
        'task_states': dict(Counter(row.get('task_state', 'not_recorded') for row in rows)),
        'raw_verdicts': dict(Counter(verdict(row.get('raw_assessment')) for row in rows)),
        'last_draft_verdicts': dict(Counter(verdict((row.get('draft_history') or [row.get('raw_assessment')])[-1]) for row in rows)),
        'final_verdicts': dict(Counter(verdict(row.get('assessment')) for row in rows)),
        'transitions': counter_rows(transitions, ('raw', 'last_draft', 'final')),
        'first_review_cross': counter_rows(first_reviews, ('raw', 'decision')),
        'terminal_origins': dict(Counter(terminal_origin(row) for row in rows)),
        'initial_date_exposure_cross': counter_rows(dates, ('method', 'exposure', 'raw', 'first_review')),
        'recorded_initial_mechanical_warning_codes': dict(Counter(w.get('code', 'not_recorded') for row in rows for w in ((row.get('decision_trace') or [{}])[0].get('warnings') or []))),
        'final_warning_codes': dict(Counter(w.get('code', 'not_recorded') for row in rows for w in row.get('validation_warnings', []))),
        'review_decisions': dict(Counter(review.get('decision', 'not_recorded') for review in reviews)),
        'review_nonpass_checks': counter_rows(Counter((key, value) for review in reviews for key, value in review.get('checks', {}).items() if value != 'pass'), ('check', 'value')),
        'search': {
            'queries': len(queries), 'query_states': dict(Counter(q.get('state', 'not_recorded') for q in queries)),
            'tasks_without_query_log': sum('queries' not in row for row in rows),
            'query_roles': dict(Counter(q.get('role', 'not_recorded') for q in queries)),
            'reported_hits': sum(known_hits) if len(known_hits) == len(queries) else None,
            'known_hit_subtotal': sum(known_hits), 'missing_hit_counts': len(queries) - len(known_hits),
            'tasks_with_both_query_roles': sum({'support', 'counter'}.issubset({q.get('role') for q in row.get('queries', [])}) for row in rows),
            'new_source_records': sum(e.get('source_kind') == 'exa_contents' for e in sources),
            'tasks_with_new_source': sum(any(e.get('source_kind') == 'exa_contents' for e in row.get('evidence_candidates', [])) for row in rows),
            'source_statuses': dict(Counter(s.get('status', 'not_recorded') for row in rows for s in row.get('source_statuses', []))),
            'source_date_statuses': counter_rows(Counter((e.get('source_kind', 'not_recorded'), e.get('date_status', 'not_recorded')) for e in sources), ('source_kind', 'date_status')),
            'source_bodies_present': sum(isinstance(e.get('text'), str) for e in sources),
            'context_truncation_not_recorded': sum('context_truncated' not in e for e in sources),
            'context_truncation_not_recorded_scope': 'Candidate field only; absence does not mean stage coverage is missing. See context_coverage.',
            'provider_limit_reached': sum(e.get('provider_text_may_be_truncated') is True for e in sources),
        },
        'context_coverage': context_coverage_summary(rows),
        'adaptive_search': adaptive_summary(rows),
        'evidence_note_relations': {stage: dict(Counter(note.get('relation', 'not_recorded') for row in rows for note in (row.get(field) or {}).get('evidence_notes', []))) for stage, field in [('raw', 'raw_assessment'), ('final', 'assessment')]},
        'fees_by_currency': {'deepseek_CNY': fee_totals(summaries, 'deepseek', 'CNY'), 'exa_USD': fee_totals(summaries, 'exa', 'USD')},
        'same_material_review_audit': review_audit_summary(rows),
        'limitations': [
            'These are recorded transitions, not human adjudications or proof that any original verdict was correct.',
            'Search success and body retrieval do not establish relevance, coverage or truth.',
            'Observational transitions cannot isolate prompt causality; use a same-material API comparison.',
            'Legacy undated exposure reconstructs the old metadata-only rule; it is not applied when a newer decision trace is present.',
            'Missing fees remain null with known subtotals, never zero-cost claims.',
        ],
    }


def write_report(report, output_dir):
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    (output / 'diagnosis.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    lines = ['# 自动判断流程诊断', '', '只统计程序记录，不人工判定预测，也不调用付费API。后面的运行按预测ID覆盖前面的运行；费用保留全部尝试。', '',
             f"独立预测：{report['unique_predictions']}；任务尝试：{report['task_attempts']}。", '',
             '|阶段|判断分布|', '|---|---|']
    for field, label in [('raw_verdicts', '初判'), ('last_draft_verdicts', '最后草稿'), ('final_verdicts', '最终输出')]:
        lines.append('|' + label + '|' + json.dumps(report[field], ensure_ascii=False) + '|')
    lines.extend(['', '末端路径（互斥统计）：' + json.dumps(report['terminal_origins'], ensure_ascii=False), '',
                  '路径顺序：技术未完成 → 已判定 → 末稿已未定 → 最后复核拒绝 → 机械校验直接降级 → 无法归因；这不是对研究判断的正确性评分。', '',
                  '检索统计：' + json.dumps(report['search'], ensure_ascii=False), '',
                  '按阶段准备的上下文覆盖：' + json.dumps(report['context_coverage'], ensure_ascii=False), '',
                  '自适应补检索：' + json.dumps(report.get('adaptive_search', {}), ensure_ascii=False), '',
                  '候选记录缺少 context_truncated 字段，不等于任务没有阶段截断记录；上表独立读取 context_coverage。相同来源在多轮出现会重复计数，记录本身不证明该次 API 已成功读取。', '',
                  '费用（原币种；null 表示有缺失）：' + json.dumps(report['fees_by_currency'], ensure_ascii=False), '',
                  '同材料四臂 API 对照：' + json.dumps(report['same_material_review_audit'], ensure_ascii=False), '',
                  '现有记录只能显示状态变化，不能证明 prompt 导致错误，也不能因为更多结论可判定就认为修复成功。需冻结相同材料做 API 对照。旧版日期暴露是旧规则的重建；新版优先读取记录的 trace，缺失时不套用旧规则。', '',
                  '[完整结构统计、交叉表及限制](diagnosis.json)', ''])
    (output / 'diagnosis.md').write_text('\n'.join(lines), encoding='utf-8')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('runs', nargs='+', type=Path)
    parser.add_argument('--output-dir', required=True, type=Path)
    args = parser.parse_args()
    result = diagnose(args.runs)
    write_report(result, args.output_dir)
    print(json.dumps({'unique_predictions': result['unique_predictions'], 'terminal_origins': result['terminal_origins'], 'output_dir': str(args.output_dir)}, ensure_ascii=False))
