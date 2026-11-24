#!/usr/bin/env python3
"""Portable forecast assessment: two JSONL tables, one case directory."""
import argparse
import collections
import csv
from datetime import date
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path.cwd()
VERDICTS = ('正确', '部分符合', '错误', '暂无法判断')
DISPLAY_VERDICTS = ('正确', '趋势符合', '部分符合', '错误', '暂无法判断')
ASSESSMENT_BASES = {'endpoint','observed_window','conditional','future','definition','evidence','attribution','excluded'}


def local_path(value):
    relative=Path(value)
    require(not relative.is_absolute(), 'Evidence path must be relative to the case')
    target=(ROOT/relative).resolve()
    require(target.is_relative_to(ROOT.resolve()), 'Evidence path outside case')
    return target

def evidence_path(e):
    require(bool(e.get('local_archive')), 'Evidence local_archive missing: '+e['id'])
    return local_path(e['local_archive'])

def verify_evidence(e):
    path=evidence_path(e)
    require(e.get('verified') is True and path.is_file() and sha(path)==e.get('sha256'),
            'Evidence integrity failed: '+e['id'])
    if e.get('local_text') and e.get('text_sha256'):
        require(sha(local_path(e['local_text']))==e['text_sha256'],'Evidence text integrity failed: '+e['id'])

def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))

def lines(path):
    return [json.loads(s) for s in Path(path).read_text(encoding='utf-8').splitlines() if s.strip()]

def save(path, obj):
    Path(path).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def table(path, rows):
    path = Path(path)
    tmp = path.with_suffix('.tmp')
    tmp.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows), encoding='utf-8')
    tmp.replace(path)

def sha(path):
    with Path(path).open('rb') as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()

def require(ok, message):
    if not ok:
        raise ValueError(message)

def config():
    return read(ROOT / 'config.json')


def case_order(c):
    return ((c.get('source_location') or {}).get('line_start') or c.get('page') or 0,c['id'])


def location_label(c):
    loc=c.get('source_location') or {}
    if loc.get('type')=='txt':
        start,end=loc['line_start'],loc['line_end']
        return f'TXT 第 {start} 行' if start==end else f'TXT 第 {start}—{end} 行'
    return f"PDF 第 {c['page']} 页" if c.get('page') is not None else '位置未记录'

def validate_assessment(r, claim, evidence):
    """Structural guardrails for retrospective, four-category assessment.

    The programme cannot prove semantic entailment or that a partial verdict
    describes a genuine mixed result. Those remain evidence-review obligations.
    """
    require(r.get('id') == claim['id'], 'Assessment ID differs from claim')
    require(r.get('inclusion') in {'forecast','nonforecast','duplicate'}, 'Bad assessment inclusion')
    require(r.get('basis') in ASSESSMENT_BASES, 'Bad assessment basis')
    for k in ('scope','reason','limitation','method'):
        require(isinstance(r.get(k),str) and bool(r[k].strip()), 'Assessment text missing: '+k)
    require(isinstance(r.get('future_time_text'),str), 'future_time_text must be a string')
    require(r.get('method_basis') in {'explicit','inferred','unknown'}, 'Bad method attribution')
    require(r.get('condition_state') in {'unconditional','satisfied','not_met','unknown'}, 'Bad condition state')
    require(isinstance(r.get('trend_aligned',False),bool), 'trend_aligned must be boolean')
    if r.get('trend_aligned',False):
        require(r.get('inclusion') == 'forecast' and r.get('verdict') == '部分符合',
                'Trend progress must be a partial forecast verdict')
        require(r['basis'] in {'observed_window','conditional'}, 'Trend progress needs an observed window')
    refs = r.get('evidence_ids')
    require(isinstance(refs,list) and all(isinstance(i,str) for i in refs), 'evidence_ids must be a string list')
    require(len(set(refs)) == len(refs), 'Duplicate evidence reference')
    for i in refs:
        require(i in evidence and evidence[i].get('verified') is True,
                'Unknown or unverified evidence: '+i)
    cutoff = date.fromisoformat(config()['cutoff'])
    for i in refs:
        published = evidence[i].get('date')
        if isinstance(published,str) and len(published)>=10 and published[4:5]=='-' and published[7:8]=='-':
            require(date.fromisoformat(published[:10]) <= cutoff, 'Evidence published after cutoff: '+i)
    require('verdict' in r and 'observation_end' in r, 'Missing assessment outcome fields')
    end = r.get('observation_end')
    if end is not None:
        require(isinstance(end,str), 'observation_end must be an ISO date or null')
        require(date.fromisoformat(end) <= cutoff, 'Observation ends after cutoff')
    if claim.get('duplicate_of'):
        require(r['inclusion'] == 'duplicate', 'Known duplicate cannot enter forecast denominator')
    if r['inclusion'] != 'forecast':
        require(r.get('verdict') is None and r['basis'] == 'excluded', 'Excluded item cannot receive a verdict')
        return
    require(r.get('verdict') in VERDICTS, 'Bad four-category verdict')
    require(r['basis'] != 'excluded', 'Forecast cannot have excluded basis')
    extra=claim.get('extraction_v2') or {}
    if r.get('verdict')=='正确' and (extra.get('extraction_version')=='v5' or extra.get('claim_type')
                                   or extra.get('resolvable') is False):
        from prepare_book import correct_verdict_block
        blocked=correct_verdict_block(claim.get('quote') or '', extra, config().get('publication_year_proxy'))
        require(blocked is None, 'Non-forecast cannot be scored correct')
    if r['basis'] == 'future':
        require(bool(r['future_time_text'].strip()), 'Future outcome needs original future horizon')
        require(r['verdict'] == '暂无法判断', 'Future outcome cannot be scored')
    if r['verdict'] == '暂无法判断':
        return
    require(claim.get('source_verified') is True, 'Scored source must be verified')
    require(bool(claim.get('quote','').strip()), 'Scored source quote is empty')
    require(bool(refs), 'Scored assessment needs evidence')
    require(end is not None, 'Scored assessment needs an observation endpoint')
    bounded_unknown = r['condition_state'] == 'unknown' and r['verdict'] == '部分符合'
    require(r['condition_state'] in {'unconditional','satisfied'} or bounded_unknown,
            'Unestablished condition cannot be scored')
    require(r['basis'] in {'endpoint','observed_window','conditional'}, 'Unresolved basis cannot be scored')

def apply_assessment(path):
    """Accept a complete book pass atomically; retain old reviews and receipts."""
    rows = lines(ROOT/'data/claims.jsonl')
    index = {c['id']:c for c in rows}
    proposals = lines(path)
    require(len(index) == len(rows), 'Duplicate claim IDs')
    require(len({r['id'] for r in proposals}) == len(proposals), 'Duplicate assessment IDs')
    require(set(index) == {r['id'] for r in proposals}, 'Assessment must cover all current book IDs exactly')
    ev = lines(ROOT/'data/evidence.jsonl')
    em = {e['id']:e for e in ev}
    require(len(em) == len(ev), 'Duplicate evidence IDs')
    for r in proposals:
        validate_assessment(r,index[r['id']],em)
    for i in {i for r in proposals for i in r['evidence_ids']}:
        verify_evidence(em[i])
    digest = sha(path)
    before = sha(ROOT/'data/claims.jsonl')
    receipt = dict(rules=config()['rules_version'],response_sha256=digest,
        input_claims_sha256=before,evidence_table_sha256=sha(ROOT/'data/evidence.jsonl'),
        config_sha256=sha(ROOT/'config.json'),reviewer='llm_with_session_review',
        human_reviewed=False,assessment_timing='retrospective')
    # Accepted response + the exact pre-change table make revisions inspectable.
    table(ROOT/f'output/claims_before_assessment_{before[:12]}.jsonl',rows)
    table(ROOT/f'output/accepted_assessment_{digest[:12]}.jsonl',proposals)
    for r in proposals:
        index[r['id']]['assessment'] = dict(r,receipt=receipt)
    table(ROOT/'data/claims.jsonl',rows)
    print('accepted assess',len(proposals))

def apply_full_extract(path):
    """Retain a complete new extraction without rewriting v1 interpretation."""
    rows = lines(ROOT/'data/claims.jsonl')
    index = {c['id']:c for c in rows}
    proposals = lines(path)
    require(len(index) == len(rows), 'Duplicate claim IDs')
    require(len({r['id'] for r in proposals}) == len(proposals), 'Duplicate extraction IDs')
    require(set(index) == {r['id'] for r in proposals}, 'Extraction must cover all current book IDs exactly')
    for r in proposals:
        require(r.get('kind') in {'prediction','nonforecast','unclear','duplicate'}, 'Bad full extraction kind')
        require(r.get('method_basis') in {'explicit','inferred','unknown'}, 'Bad extraction method attribution')
        for k in ('claim','time_text','condition_text','method','reason'):
            require(isinstance(r.get(k),str), 'Full extraction text missing: '+k)
        require(bool(r['reason'].strip()), 'Full extraction needs an interpretation reason')
        if 'expanded_claim' in r:
            from prepare_book import validate_expansion
            c=index[r['id']]
            validate_expansion(r,c.get('quote','')+'\n'+c.get('context',''),normalized=True)
    digest = sha(path); before = sha(ROOT/'data/claims.jsonl')
    receipt = dict(rules=config()['rules_version'],response_sha256=digest,input_claims_sha256=before,
        config_sha256=sha(ROOT/'config.json'),reviewer='llm',human_reviewed=False)
    table(ROOT/f'output/claims_before_extract_full_{before[:12]}.jsonl',rows)
    table(ROOT/f'output/accepted_extract_full_{digest[:12]}.jsonl',proposals)
    for r in proposals:
        index[r['id']]['extraction_v2'] = dict(r,receipt=receipt)
    table(ROOT/'data/claims.jsonl',rows)
    print('accepted extract-full',len(proposals))

def display_verdict(assessment):
    if assessment.get('verdict') == '部分符合' and assessment.get('trend_aligned',False):
        return '趋势符合'
    return assessment.get('verdict')

def assessment_summary(rows, evidence):
    counts = collections.Counter({v:0 for v in VERDICTS})
    display_counts = collections.Counter({v:0 for v in DISPLAY_VERDICTS})
    excluded = collections.Counter({'nonforecast':0,'duplicate':0})
    missing = 0
    for c in rows:
        r = c.get('assessment')
        if not r:
            missing += 1
        elif r['inclusion'] == 'forecast':
            counts[r['verdict']] += 1
            display_counts[display_verdict(r)] += 1
        else:
            excluded[r['inclusion']] += 1
    forecast_n = sum(counts.values())
    decided = forecast_n-counts['暂无法判断']
    with_evidence = sum(bool(c['assessment'].get('evidence_ids')) for c in rows
                        if (c.get('assessment') or {}).get('inclusion') == 'forecast')
    return dict(book=config()['book'],cutoff=config()['cutoff'],rules_version=config()['rules_version'],
        candidates=len(rows),assessment_reviewed=len(rows)-missing,unreviewed=missing,
        extraction_v2_reviewed=sum(bool(c.get('extraction_v2')) for c in rows),
        expanded_claims_n=sum(bool((c.get('extraction_v2') or {}).get('expanded_claim')) for c in rows),
        unresolved_references_n=sum(bool((c.get('extraction_v2') or {}).get('unresolved_references')) for c in rows),
        legacy_extraction_reviewed=sum(bool(c.get('extraction')) for c in rows),
        whole_candidate_pass_complete=missing==0,candidate_completion_rate=(len(rows)-missing)/len(rows) if rows else None,
        forecast_n=forecast_n,verdicts=dict(counts),display_verdicts=dict(display_counts),
        display_schema='five-categories-trend-separate',excluded=dict(excluded),decided_n=decided,
        forecasts_with_bound_evidence=with_evidence,
        forecasts_without_bound_evidence=forecast_n-with_evidence,
        no_decidable_outcomes=forecast_n > 0 and decided == 0,
        trend_aligned_n=sum((c.get('assessment') or {}).get('trend_aligned',False) is True for c in rows),
        evaluation_coverage=decided/forecast_n if forecast_n else None,
        correct_share_of_decided=counts['正确']/decided if decided else None,
        unresolved_bases=dict(collections.Counter(c['assessment']['basis'] for c in rows
            if (c.get('assessment') or {}).get('verdict')=='暂无法判断')),
        evidence=len(evidence),evidence_hash_verified=sum(e.get('verified') is True for e in evidence),
        method_attribution=dict(collections.Counter(c['assessment']['method_basis'] for c in rows if c.get('assessment'))),
        interpretation='Retrospective parent-record counts, not independent forecast accuracy or prospective skill.',
        brier=None,partial_numeric_weight=None,
        prepublication_observation_warning_ids=[c['id'] for c in rows if c.get('assessment')
            and c['assessment'].get('verdict') in VERDICTS[:3]
            and c['assessment'].get('observation_end')
            and c['assessment']['observation_end'][:4] < str(config()['publication_year_proxy'])])

def assessment_report():
    rows = lines(ROOT/'data/claims.jsonl')
    ev = lines(ROOT/'data/evidence.jsonl'); em = {e['id']:e for e in ev}
    for c in rows:
        if c.get('assessment'):
            validate_assessment(c['assessment'],c,em)
    used = {i for c in rows if c.get('assessment') for i in c['assessment']['evidence_ids']}
    for i in used:
        verify_evidence(em[i])
    summary = assessment_summary(rows,ev)
    horizon_sources=collections.Counter((c.get('extraction_v2') or {}).get('horizon_source')
                                        for c in rows if (c.get('extraction_v2') or {}).get('horizon_source'))
    if horizon_sources:
        summary['horizon_sources']=dict(horizon_sources)
    audit_path = ROOT/'output/execution_audit.json'
    audit = read(audit_path) if audit_path.exists() else {}
    accepted_hashes = {c['assessment'].get('receipt',{}).get('response_sha256')
                       for c in rows if c.get('assessment')}
    audited_run = (summary['whole_candidate_pass_complete'] and audit.get('session_adjudication_complete')
                   and accepted_hashes == {audit.get('accepted_assessment_sha256')}
                   and audit.get('accepted_assessment_sha256') is not None)
    if audited_run:
        summary['execution'] = {k:audit[k] for k in ('request_count','response_count','api_peak_concurrency',
            'api_wall_seconds','usage','estimated_cost_CNY_range','automatic_retries','final_accepted_records')}
        summary['session_review'] = audit.get('review_changes',{})
    save(ROOT/'output/summary.json',summary)
    ordered = sorted(rows,key=case_order)
    save(ROOT/'output/next_batch.json',dict(reason='unassessed candidates only; unresolved conclusions are completed reviews',
        ids=[c['id'] for c in ordered if not c.get('assessment')],remaining=sum(not c.get('assessment') for c in rows)))
    pct = lambda v:'暂无' if v is None else f'{v:.1%}'
    text = [f"# {config()['book']}：五类评估",'',
        f"证据截止日：{summary['cutoff']}。已处理 {summary['assessment_reviewed']}/{summary['candidates']} 条全书候选；尚未处理 {summary['unreviewed']} 条。",'',
        f"累计已完成全量抽取复核 {summary['extraction_v2_reviewed']} 条；保留旧抽样抽取 {summary['legacy_extraction_reviewed']} 条，两者不重复相加。",'',
        f"已补充扩展观点 {summary['expanded_claims_n']} 条；其中 {summary['unresolved_references_n']} 条仍有待确认的代指、对象或范围，已逐条标记。扩展观点不自动改变原有评估。",'',
        '本轮沿用候选清单逐条核查，不保证没有漏抽。PDF记录使用PDF页码，TXT记录使用原始文本行号。扩展观点是依据所给语境的解释，原文短引文另行保留。', '',
        '|类别|父记录数|','|---|---:|']
    if summary['no_decidable_outcomes']:
        text[2:2] = ['研究提示：本轮没有可判定结果，需要复查搜证覆盖与未决理由；候选全部处理不代表证据研究已完成。','']
    text += [f'|{v}|{summary["display_verdicts"][v]}|' for v in DISPLAY_VERDICTS]
    text += [f'|排除：非预测|{summary["excluded"]["nonforecast"]}|',
        f'|排除：重复|{summary["excluded"]["duplicate"]}|',f'|尚未处理|{summary["unreviewed"]}|','',
        f"可判定覆盖率：{summary['decided_n']}/{summary['forecast_n']} = {pct(summary['evaluation_coverage'])}。",
        f"绑定外部证据的预测：{summary['forecasts_with_bound_evidence']}/{summary['forecast_n']}；未绑定：{summary['forecasts_without_bound_evidence']}。绑定不代表证据充分或研究已完成。",
        f"“正确”占已判定记录：{summary['verdicts']['正确']}/{summary['decided_n']} = {pct(summary['correct_share_of_decided'])}。",'',
        f"趋势符合 {summary['trend_aligned_n']} 条单独列出，与部分符合互不重复；它表示已有持续证据支持方向，最终结果仍待验证。",'',
        '以上是回顾性的记录统计，不是独立预测准确率或事前预测能力检验。部分符合不折算成 0.5 分；暂无法判断不算错误。跨章相关判断尚未完全去重，同一父记录也不因多个观察而增加命中次数。没有作者明确给出的概率，不计算 Brier 分数。','',
        '## 评估口径','',
        '正确：在列明口径和观察窗口内，主要可检验内容符合。趋势符合：已有持续客观证据支持预测方向，最终结果尚待验证。部分符合：具体分项部分成立、部分不符，或合理口径产生不同结果。错误：所评内容与已发生结果相反。暂无法判断：无法确认趋势或结果、条件不明、对象难测或证据仍不足；缺证据不能自动换成趋势符合或部分符合。', '',
        '明确未来终点尚未到达时，可以评价已有趋势，并保留原期限；这类进展单列为趋势符合，不作终局正确。单次波动、未来预测数据或仅有因果解释不算趋势证据。真正的前提条件仍须确认成立，作者的因果解释不自动增加为额外触发门槛。无期限持续判断可评价已观察阶段，不能证明永久成立。出版年只是未找到发言日期时的研究起点代理，出版前已知事实不是新的预见力证据。', '',
        '“不太可能”没有被转换为数值概率；低概率事件发生可记录为方向反例，不能据单次结果证明概率失准。官方声明证明立场或制度安排，不自动证明实际成效；同时出现的政策与结果不自动证明因果。','',
        '## 暂无法判断的原因','', '|原因类型|记录数|','|---|---:|']
    if audited_run:
        # Keep run facts and examples reproducible, tied to this exact accepted response.
        marker = text.index('## 评估口径')
        execution = summary['execution']; costs = execution['estimated_cost_CNY_range']
        insert = ['## 本轮执行与复核','',
            f"DeepSeek 实际返回 {execution['response_count']}/{execution['request_count']} 次调用；峰值 {execution['api_peak_concurrency']} 并发；API 阶段耗时 {execution['api_wall_seconds']:.1f} 秒（不含检索和本地复核）。",'',
            f"供应商返回用量合计 {execution['usage']['total_tokens']:,} tokens；按归档峰谷费率估计本轮 ¥{costs[0]:.4f}—¥{costs[1]:.4f}，不是供应商账单。自动重试 {execution['automatic_retries']} 次。",'',
            '原始请求和响应均保留。模型初答经本地 LLM 复核后才导入，非独立人类审阅；初始校验拒绝与修订明细见 execution_audit.json 和案例 audit/ 目录。','',
            '## 便于核查的例子','', '|原文位置|原判断|本轮判定|','|---|---|---|']
        review_round = audit.get('review_round')
        if isinstance(review_round,dict):
            reviewed = review_round.get('reviewed_unresolved',review_round.get('requested'))
            carried = review_round.get('carried_forward')
            if isinstance(reviewed,int) and isinstance(carried,int):
                insert[2:2] = [f'本轮仅复核上一轮暂无法判断的 {reviewed} 条，其余 {carried} 条沿用。','']
        by_id = {c['id']:c for c in rows}
        for ident in audit.get('example_ids',[]):
            c = by_id[ident]
            insert.append(f"|{location_label(c)}|{c['quote'].replace('|','／')}|{display_verdict(c['assessment']) or '排除'}|")
        insert += ['', '## 从原文归纳的思考办法','']
        insert += [x+'\n' for x in audit.get('method_findings',[])]
        insert += ['这些方法是文本归纳，结果符合不等于解释机制成立。未经过历史基准比较，不能据此证明某一种方法具有预测优势。','']
        text[marker:marker] = insert
    basis_labels = dict(endpoint='明确终点',observed_window='已观察阶段',conditional='条件未确认或未触发',
        future='明确未来期限未到',definition='定义或可测量性不足',evidence='证据不足',attribution='归属不明',excluded='排除')
    text += [f'|{basis_labels[k]}|{v}|' for k,v in sorted(summary['unresolved_bases'].items())]
    if summary.get('horizon_sources'):
        sources=summary['horizon_sources']
        text += [f"时间窗口来源：原文写出 {sources.get('explicit',0)} 条，隐含的出版年至截止日 {sources.get('implicit_publication_to_cutoff',0)} 条。",'']
    text += ['', '## 逐条结果','']
    if summary['prepublication_observation_warning_ids']:
        text += ['注意：以下记录的已判定观察终点早于出版年，属于背景或需修订项目，不能作为新预见力证据：'+
                 '、'.join(summary['prepublication_observation_warning_ids']),'']
    csvrows = []
    method_labels = dict(explicit='原文明确',inferred='研究者归纳',unknown='无法确定')
    for n,c in enumerate(ordered,1):
        r = c.get('assessment')
        extra=c.get('extraction_v2') or {};loc=c.get('source_location') or {}
        csvrows.append(dict(n=n,id=c['id'],pdf_page=c.get('page'),source_location=location_label(c),
            source_type=loc.get('type','pdf'),line_start=loc.get('line_start',''),line_end=loc.get('line_end',''),
            quote=c['quote'],expanded_claim=extra.get('expanded_claim',''),
            reference_resolutions=json.dumps(extra.get('reference_resolutions',[]),ensure_ascii=False),
            unresolved_references=json.dumps(extra.get('unresolved_references',[]),ensure_ascii=False),context=c['context'],
            claim=(c.get('extraction_v2') or {}).get('claim',c.get('claim','')),
            extraction_v2_kind=(c.get('extraction_v2') or {}).get('kind',''),
            inclusion=r['inclusion'] if r else '',display_verdict=display_verdict(r) or '' if r else '',
            verdict=r.get('verdict') or '' if r else '',
            trend_aligned=r.get('trend_aligned',False) if r else False,
            previous_verdict=r.get('previous_verdict','') if r else '',change_reason=r.get('change_reason','') if r else '',
            basis=r['basis'] if r else '',scope=r['scope'] if r else '',reason=r['reason'] if r else '',
            limitation=r['limitation'] if r else '',observation_end=r.get('observation_end') or '' if r else '',
            future_time_text=r['future_time_text'] if r else '',condition_state=r['condition_state'] if r else '',
            method=r['method'] if r else '',method_basis=r['method_basis'] if r else '',
            evidence_ids=';'.join(r['evidence_ids']) if r else '',
            evidence_urls=';'.join(em[i].get('url') or '' for i in r['evidence_ids']) if r else '',
            family=c.get('family',''),duplicate_of=c.get('duplicate_of') or ''))
        if summary.get('horizon_sources'):
            csvrows[-1]['horizon_source']=extra.get('horizon_source','')
        label = '尚未处理' if not r else display_verdict(r) or ('排除：重复' if r['inclusion']=='duplicate' else '排除：非预测')
        if r and r.get('trend_aligned',False):
            label += '（最终结果待验证）'
        text += [f"### {n}. {location_label(c)} · {label}",'',f"记录：`{c['id']}`",'',f"原文：{c['quote'] or '旧候选无独立引文，见排除说明。'}",'']
        if extra.get('horizon_source')=='implicit_publication_to_cutoff':
            text += [f"时间窗口：隐含，从出版年 {config()['publication_year_proxy']} 到截止日 {config()['cutoff']}。原文未写期限；该窗口内方向发生即按此评分。",'']
        elif extra.get('horizon_source')=='explicit':
            written=extra.get('horizon') or extra.get('time_text') or '见原文'
            text += [f"时间窗口：原文写出（{written}）。",'']
        if extra.get('expanded_claim'):
            text += [f"扩展观点（解释，非原文）：{extra['expanded_claim']}",'']
            for ref in extra.get('reference_resolutions',[]):
                text += [f"指代展开：{ref['expression']} → {ref['referent']}；上下文依据：{ref['support_quote']}"]
            if extra.get('unresolved_references'):
                text += ['仍待确认的代指：'+'；'.join(extra['unresolved_references'])]
            text += ['']
        if not r:
            continue
        if r.get('change_reason'):
            text += [f"本轮复核：{r.get('previous_verdict') or '原判定'} → {display_verdict(r) or '排除'}；{r['change_reason']}",'']
        refs = '；'.join(f"[{i}]({em[i]['url']})" if em[i].get('url') else i for i in r['evidence_ids'])
        text += [f"口径与范围：{r['scope']}",f"判定：{r['reason']}",f"限制：{r['limitation']}",
            f"观察终点：{r.get('observation_end') or '未形成可判定观察终点'}；条件状态：{r['condition_state']}。",
            f"思考方法：{r['method']}（{method_labels[r['method_basis']]}；方法有效性未由此证明）。",
            f"证据：{refs or '尚无足以判定的外部证据；本条仅作原文范围或条件审阅。'}",'']
    text += ['## 证据登记','',
        '哈希校验只证明本地保存内容未改变。检索摘录与完整原始文件会按证据记录注明；两者均不能代替对来源与命题对应关系的判断。','']
    for e in ev:
        if e['id'] in used:
            label = f"[{e['id']}]({e['url']})" if e.get('url') else e['id']
            text += [f"- {label}；资料日期：{e.get('date') or '未确定'}；覆盖：{e.get('coverage') or '见逐条说明'}。限制：{e.get('limitation') or '见来源原文及逐条评估'}"]
    (ROOT/'output/report.md').write_text('\n'.join(text)+'\n',encoding='utf-8')
    with (ROOT/'output/claims.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w = csv.DictWriter(f,fieldnames=list(csvrows[0]) if csvrows else ['id'])
        w.writeheader()
        # Keep CSV safe to open in spreadsheet software; JSONL remains exact text.
        for row in csvrows:
            w.writerow({k:("'"+v if isinstance(v,str) and v.startswith(('=','+','-','@')) else v) for k,v in row.items()})
    print(json.dumps(summary,ensure_ascii=False))

def check():
    cs=lines(ROOT/'data/claims.jsonl');es=lines(ROOT/'data/evidence.jsonl')
    require(len({c['id'] for c in cs})==len(cs),'Duplicate claim IDs')
    require(len({e['id'] for e in es})==len(es),'Duplicate evidence IDs')
    em={e['id']:e for e in es}
    for e in es:verify_evidence(e)
    for c in cs:
        if 'expanded_claim' in (c.get('extraction_v2') or {}):
            from prepare_book import validate_expansion
            validate_expansion(c['extraction_v2'],c.get('quote','')+'\n'+c.get('context',''),normalized=True)
        if c.get('assessment'):validate_assessment(c['assessment'],c,em)
    print('OK:',len(cs),'claims;',len(es),'verified evidence records')

def main(argv=None):
    global ROOT
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--case',type=Path,required=True)
    sub=parser.add_subparsers(dest='command',required=True)
    start=sub.add_parser('init')
    start.add_argument('--book',required=True);start.add_argument('--author',default='')
    start.add_argument('--publication-year',type=int,required=True)
    start.add_argument('--cutoff',required=True)
    for cmd in ['check','report','freeze-review']:sub.add_parser(cmd)
    apply=sub.add_parser('apply');apply.add_argument('mode',choices=['assess','extract-full']);apply.add_argument('file',type=Path)
    args=parser.parse_args(argv);ROOT=args.case.resolve()
    if args.command=='init':
        date.fromisoformat(args.cutoff)
        require(1<=args.publication_year<=9999,'Invalid publication year')
        require(not (ROOT/'config.json').exists() and not (ROOT/'data/claims.jsonl').exists(),'Case already exists')
        (ROOT/'data/sources').mkdir(parents=True,exist_ok=True);(ROOT/'output').mkdir(exist_ok=True)
        save(ROOT/'config.json',dict(book=args.book,author=args.author,cutoff=args.cutoff,
            publication_year_proxy=args.publication_year,rules_version='simple-v3-trend-four-class'))
        table(ROOT/'data/claims.jsonl',[]);table(ROOT/'data/evidence.jsonl',[])
        print('Initialized',ROOT)
        return
    require((ROOT/'config.json').is_file(),'Case config.json not found')
    (ROOT/'output').mkdir(exist_ok=True)
    if args.command=='check':check()
    elif args.command=='report':assessment_report()
    elif args.command=='apply':
        if args.mode=='assess':apply_assessment(args.file)
        else:apply_full_extract(args.file)
    elif args.command=='freeze-review':
        target=ROOT/'output/review/before_book_index.json'
        require(not target.exists(),'Frozen review already exists; choose a separate review directory for another round')
        target.parent.mkdir(parents=True,exist_ok=True)
        rows=sorted(lines(ROOT/'data/claims.jsonl'),key=case_order)
        save(target,[dict(n=n+1,**c) for n,c in enumerate(rows)])
        print('Frozen',len(rows),'records;',sum((c.get('assessment') or {}).get('verdict')=='暂无法判断' for c in rows),'unresolved')

if __name__=='__main__':
    try:main()
    except (ValueError,KeyError,OSError) as e:
        print('Rejected:',e,file=sys.stderr);sys.exit(2)
