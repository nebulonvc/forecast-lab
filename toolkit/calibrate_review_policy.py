"""Synthetic contract calibration using an injected, shared-budget API runner."""
from concurrent.futures import ThreadPoolExecutor
from copy import deepcopy
import hashlib
import json
import math
from pathlib import Path

import run_parallel as rp
import semantic_review as sr
from review_audit import legacy_prompt


def calibration_fixtures():
    """Invented closed-world facts; expectations never enter the model input."""
    base_quote = '澄星地区2025年的常住人口将低于2020年的100人。'
    population = '澄星地区完整人口登记：2020年100人，2025年80人；地区边界和常住人口口径相同，2025年登记已经完成。'
    definitions = [
        dict(id='supported_correct', quote=base_quote, text=population, verdict='正确',
             reason='同地区同口径的2025年80人低于2020年100人。', expected=['accept']),
        dict(id='opposite_wrong', quote=base_quote,
             text='澄星地区完整人口登记：2020年100人，2025年120人；地区边界和常住人口口径相同，2025年登记已经完成。',
             verdict='错误', reason='2025年120人高于100人，与预测的低于100人相反。', expected=['accept']),
        dict(id='two_components_partial',
             quote='澄星地区到2025年将同时实现常住人口低于100人，以及平均通勤少于30分钟；这两项同为主要目标。',
             text='澄星地区2025年完整登记显示，常住人口为80人，平均通勤为40分钟；两项指标定义与预测相同，记录已经完成。',
             verdict='部分符合', reason='人口80人满足低于100人，但通勤40分钟不满足少于30分钟；两个主要分项一成一反。',
             relation='boundary', expected=['accept']),
        dict(id='future_endpoint_trend', quote='澄星地区常住人口到2030年将达到150人。',
             text='同边界同口径的人口登记：2020年100人，2022年115人，2025年130人；以上均为已经发生的年度实际结果。尚无2030年结果。',
             verdict='部分符合', reason='三个已发生观察点持续接近150人的预测方向，只评估截至2025年的趋势。',
             limitation='2030年终点尚未到，130人不等于终点150人已经实现。',
             basis='observed_window', trend_aligned=True, future_time_text='2030年', expected=['accept']),
        dict(id='real_condition_unknown',
             quote='如果澄星地区的新桥在2024年底前建成，那么2025年平均通勤将低于20分钟。',
             text='2025年同口径平均通勤为18分钟。档案中没有新桥是否在2024年底前建成的记录，该前提在本题材料中未知。',
             verdict='暂无法判断', reason='后果的通勤数字已知，但原文真实前提是否按时建成仍未知，不能确认该条件预测。',
             basis='conditional', condition_state='unknown', remaining_gap='缺少新桥是否在2024年底前建成这一真实触发条件的记录。', expected=['revise']),
        dict(id='no_outcome_evidence', quote=base_quote,
             text='这份材料仅记录澄星地区2020年人口为100人。它是一份调查计划，尚未取得2025年人口，不能提供预测结果。',
             verdict='暂无法判断', reason='没有2025年同口径人口结果，无法比较它是否低于100人。',
             basis='evidence', observation_end=None, remaining_gap='缺少2025年同口径实际人口结果。', expected=['accept']),
        dict(id='unjustified_unresolved', quote=base_quote, text=population,
             verdict='暂无法判断', reason='虽然同口径登记明确为100人降至80人，但没有人口变化的因果识别实验，所以无法判断人数是否下降。',
             basis='evidence', remaining_gap='还需要因果识别实验才能比较这两个已给出的人数。', expected=['revise']),
        dict(id='causal_overclaim',
             quote='澄星地区灯光改造后，2025年事故率将低于2020年的每万人10起。',
             text='同一澄星地区按同口径记录：2020年每万人10起事故，2025年每万人6起。同期实施灯光改造和限速；这些描述性观察没有识别各措施的因果效应。',
             verdict='正确', reason='这证明灯光改造是事故率下降的唯一原因，并且排除了限速等所有其他因素。',
             limitation='已证明唯一因果关系，无需限定。', expected=['revise', 'unresolved']),
    ]
    fixtures = []
    for spec in definitions:
        ident = 'synthetic-' + spec['id']
        source_id = 'synthetic-evidence-' + spec['id']
        observation_end = spec.get('observation_end', '2025-12-31')
        scope = '只评估题设虚构地区、原句明示指标和时点；只使用下面给出的完整题设事实。'
        proposal = dict(id=ident, inclusion='forecast', verdict=spec['verdict'],
            basis=spec.get('basis', 'endpoint'), scope=scope, reason=spec['reason'],
            limitation=spec.get('limitation', '结论仅适用于题设地区、明示指标和时段，不推断其他地区或因果机制。'),
            evidence_ids=[source_id], method='原句未提供推理', method_basis='unknown',
            observation_end=observation_end, future_time_text=spec.get('future_time_text', ''),
            condition_state=spec.get('condition_state', 'unconditional'), trend_aligned=spec.get('trend_aligned', False),
            evidence_notes=[dict(evidence_id=source_id, relation=spec.get('relation', 'support'), quote=spec['text'],
                publication_date='2026-01-15', observation_end=observation_end,
                limitation='纯合成题设资料，不对应真实文献或真实人口。')], remaining_gap=spec.get('remaining_gap', ''))
        original_context = '本例所有地名、数值和资料均为虚构。范围只有澄星地区，指标定义不变；不使用任何真实书籍或外部事实。'
        original_text = spec['quote'] + '\n' + original_context
        proposal_text = '\n'.join(str(proposal.get(k) or '') for k in ('scope', 'reason', 'limitation', 'observation_end'))
        sources = {source_id: spec['text']}
        options = sr.quote_options(original_text, proposal_text, proposal['evidence_notes'], sources)
        evidence = dict(id=source_id, url='https://synthetic.invalid/' + spec['id'], title='虚构题设记录',
                        published_date='2026-01-15', source_kind='synthetic_fixture', verified=True,
                        text=spec['text'], context_truncated=False, date_status='known')
        data = dict(id=ident, claim_id=ident, round=1, book='合成复核契约测试（虚构）', cutoff='2026-11-09',
            publication_year_proxy=2020,
            fixture_notice='这是封闭的合成逻辑样例：记录是题设事实，明示缺失也属于题设。不搜索、不补外部事实；只检验给定建议是否遵守复核规则。',
            cases=[dict(id=ident, quote=spec['quote'], context=original_context, speaker='虚构作者',
                        source_verified=True, duplicate_of=None)],
            research_scope=scope, evidence_candidates=[evidence], proposed_assessment=proposal,
            review_quote_options=options)
        context = dict(id=ident, original_text=original_text, proposal_text=proposal_text,
                       source_texts=sources, review_quote_options=options, cutoff=data['cutoff'],
                       source_verified=True, allowed_evidence_ids=[source_id], validation_candidates=[evidence])
        fixtures.append(dict(id=ident, expected_decisions=spec['expected'], data=data, context=context))
    return fixtures


def totals_delta(before, after):
    keys = ('estimated_cost_CNY', 'estimated_off_peak_cost_CNY', 'budget_committed_CNY',
            'unknown_or_inflight_reserved_CNY', 'usage_unknown_requests', 'usage_unknown_reserved_CNY',
            'total_tokens', 'completed_stages', 'cache_hits_this_run')
    delta = {}
    for key in keys:
        a, b = before.get(key), after.get(key)
        delta[key] = (round(b - a, 8) if type(a) in (int, float) and type(b) in (int, float)
                      and math.isfinite(a) and math.isfinite(b) else None)
    return delta


def run_calibration(llm, run_dir):
    """Make at most 16 calls through the supplied runner; never instantiate a client."""
    import verify_prediction as vp
    fixtures = calibration_fixtures()
    prompts = {'legacy': legacy_prompt(), 'shared': sr.REVIEW_PROMPT}
    before = deepcopy(llm.totals())

    def evaluate(task):
        number, fixture, arm = task
        body = json.dumps(fixture['data'], ensure_ascii=False, sort_keys=True)
        request = dict(model='deepseek-flash', thinking={'type': 'disabled'}, temperature=0, max_tokens=2600,
            response_format={'type': 'json_object'}, messages=[{'role': 'system', 'content': prompts[arm]},
                                                            {'role': 'user', 'content': body}])
        result = dict(fixture_id=fixture['id'], arm=arm, expected_decisions=fixture['expected_decisions'],
                      common_input_sha256=hashlib.sha256(body.encode()).hexdigest(),
                      request_sha256=hashlib.sha256(rp.canonical(request)).hexdigest(),
                      prompt_sha256=hashlib.sha256(prompts[arm].encode()).hexdigest(),
                      status='call_failed', api_response_received=None, schema_valid=None, expected_match=None)
        try:
            items = llm.call('semantic_review', request, [fixture['context']], number)
            result['api_response_received'] = True
            result['status'] = 'schema_failed'
            # Also validate injected test/custom runners; no repair or retry here.
            validated = vp.validate_stage('semantic_review', items, [fixture['context']])[0]
            result.update(status='completed', schema_valid=True, review=validated,
                          decision=validated['decision'], expected_match=validated['decision'] in fixture['expected_decisions'])
        except Exception as exc:
            if isinstance(exc, rp.ResponseValidationError):
                result.update(status='schema_failed', api_response_received=True)
            if result['api_response_received'] is True:
                result['schema_valid'] = False
            result['error'] = vp.safe_error(exc)
        return result

    tasks = [(number, fixture, arm) for number, (fixture, arm) in enumerate(
             ((fixture, arm) for fixture in fixtures for arm in prompts), start=1)]
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(evaluate, tasks))
    after = deepcopy(llm.totals())
    summary = {arm: {
        'requested': 8, 'completed': sum(r['arm'] == arm and r['status'] == 'completed' for r in results),
        'schema_failed': sum(r['arm'] == arm and r['status'] == 'schema_failed' for r in results),
        'call_failed': sum(r['arm'] == arm and r['status'] == 'call_failed' for r in results),
        'expected_matches': sum(r['arm'] == arm and r['expected_match'] is True for r in results),
        'completed_mismatches': sum(r['arm'] == arm and r['expected_match'] is False for r in results),
    } for arm in prompts}
    report = dict(kind='synthetic_review_contract_calibration', fixture_count=8, planned_calls=16,
        human_authored_synthetic_expectations=True, real_world_gold=False,
        fixtures=[{'id': f['id'], 'expected_decisions': f['expected_decisions'], 'input': f['data']} for f in fixtures],
        results=results, summary=summary, totals_before=before, totals_after=after,
        shared_ledger_delta=totals_delta(before, after),
        accounting_note='Uses the same runner and budget as the book run. This delta is already included in the shared ledger: never add it again. Concurrent unrelated work would also affect before/after deltas. Missing totals remain null.',
        limitations='These are human-authored fictional logic contracts, not real-world gold labels or evidence of factual accuracy on book predictions.')
    output = Path(run_dir)
    output.mkdir(parents=True, exist_ok=True)
    rp.save_json(output / 'policy_calibration.json', report)
    return report
