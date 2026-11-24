from pathlib import Path
import json,hashlib,shutil
w=Path('/workspace/forecast-bot3-w20');c=w/'repo/cases/doctorow-down-and-out-in-the-magic-kingdom-v5'
def jl(p,rs):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rs))
def js(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
cs=[json.loads(x) for x in (c/'data/claims.jsonl').read_text().splitlines()]
assert len(cs)==101 and not any(x['extraction_v2']['resolvable'] for x in cs)
quotes={'80455d5225a7':'I’ve never really done anything predictive in my life. I always say that I try to predict the present.','cc6c5faae217':'Meritocracy and reputation economics were the subject of my debut novel, 2003’s Down and Out in the Magic Kingdom , which, ironically, is often held up as an example of “utopian” fiction.','641191f5ce77':'My first novel was published in January 2003.'}
ev=[]
for stem,q in quotes.items():
 p=c/'data/sources'/f'{stem}.json';d=json.loads(p.read_text());assert q in d['text'],(stem,q)
 ev.append(dict(id='ev-'+stem,url=d['url'],date=d['date'],coverage='仅归属和作品边界审计，不是技术/社会结果评分证据',excerpt=q,limitation=d['limitation'],local_archive='data/sources/'+p.name,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),verified=True))
jl(c/'data/evidence.jsonl',ev);em={x['id']:x for x in ev}
interview=json.loads((c/'data/sources/80455d5225a7.json').read_text())['text']
counter='there are a few things that I predicted would still be in Disney World that have just shut down.'
assert counter in interview
rows=[]
for n,x in enumerate(cs,1):
 ex=x['extraction_v2'];speaker=x['speaker'];blurb=n<=2
 scope='归属核查：'+x['claim']
 reason=(f'该句由封面推荐人{speaker}提出，是第三方对作品影响的预期，不能转记为Doctorow本人预测。' if blurb else f'该具体场景或判断是{speaker}的声音：{x["claim"]}原书未在作者自身声音中明确采用此命题；原代码据reported自动unclear，不是无日期或语义重复排除。')
 limitation='这不是判定命题真伪，也不是认定所有小说均无预测。2010年访谈虽称“predict the present”，也承认预期某些Disney设施会继续存在，故不能仅凭作者泛称否认预测一刀切；本例坚持2003原文逐句归属，不把后来访谈的新断言反向加回原书。'
 ids=['ev-641191f5ce77'] if blurb else ['ev-80455d5225a7','ev-cc6c5faae217','ev-641191f5ce77']
 notes=[dict(evidence_id=i,relation='background' if blurb else 'boundary',quote=em[i]['excerpt'],publication_date=em[i]['date'],observation_end=None,limitation=em[i]['limitation']) for i in ids]
 if not blurb:notes.append(dict(evidence_id='ev-80455d5225a7',relation='counter',quote=counter,publication_date='2015-04-08',observation_end=None,limitation='作者后来承认部分设施延续预期，是对其“从不预测”泛称的反例；不能据此证明每个小说技术设定均是2003现实断言。'))
 sem=dict(object_match='pass',condition_logic='pass',time_alignment='pass',evidence_support='unknown' if not blurb else 'pass',counterevidence='pass',verdict_logic='pass')
 rows.append(dict(id=x['id'],inclusion='nonforecast',verdict=None,basis='excluded',scope=scope,reason=reason,limitation=limitation,evidence_ids=ids,method='逐块全文人工抽取；原85e6da1 validate_chunk_predictions/claims_from_results归属后处理；逐条复核reported边界。resolvable=0，无逐预测PLAN任务；另做1轮WebSearch正反各1查询、WebFetch阅读及urllib公开HTTPS存档3源，非Exa。',method_basis='explicit',observation_end=None,future_time_text=ex.get('horizon',''),condition_state='unknown',trend_aligned=False,evidence_notes=notes,remaining_gap='如把具体小说世界设定视为作者默示背书，会改变归属口径；本包保留全部候选供复核，不把边界不明充当可评分现实预测。',semantic_review=sem,semantic_review_notes='逐条将引文、说话者和claim对齐；不虚构截止前技术结果证据；evidence_support=unknown指作者背书未被证实，不是未读原文。'))
o=c/'output/verify-v5-run';o.mkdir(parents=True,exist_ok=True)
jl(o/'assess.jsonl',rows);jl(o/'results.jsonl',rows);jl(o/'tasks.jsonl',[])
for n in ['exa','llm']:(o/n).mkdir(exist_ok=True)
js(o/'summary.json',dict(candidates=len(cs),resolvable=0,per_forecast_search_tasks=0,boundary_reviewed=len(rows),boundary_search_rounds=1,boundary_queries=2,selected_urls=3,actual_search='WebSearch',actual_fetch='WebFetch read + urllib HTTPS archive',scored_forecasts=0,third_round=False,semantic_evidence_support_unknown=99))
(o/'report.md').write_text('# 归属边界核查\n\n101条候选全部逐条复核；原归属规则resolvable=0，无逐预测PLAN/SELECT/结果评分。辅助归属检索1轮正反各1查询，存档3个公开URL。\n\n未使用Exa、DeepSeek；未把真实相似技术或小说情节当现实结果评分。作者2010访谈的预测否认与设施延续承认均保留，不能断章取义。\n')
js(o/'boundary-plan.json',dict(scope='检验具体未来场景是否可归属于2003作者自身现实断言；查找支持其预测解读及反对的作者说明，不把类型当排除条件。',round=1,queries=[dict(role='support',query='Cory Doctorow Down and Out Magic Kingdom Whuffie predictions reputation economy future author 2026'),dict(role='counter',query='Cory Doctorow Down and Out Magic Kingdom not prediction Whuffie novel 2026')],selected_urls=[e['url'] for e in ev],selection_reason='3个返回URL包括作者主页/作者2016评论及完整2010访谈2015重刊；访谈既有反预测表述也有反例，均保留。',not_a_per_forecast_PLAN=True))
f=c/'output/verify-final';f.mkdir(parents=True,exist_ok=True)
for name in ['results.jsonl','results.slim.jsonl']:jl(f/name,rows)
js(f/'summary.json',dict(candidates=len(cs),forecast_n=0,decidable_n=0,正确=0,趋势符合=0,部分符合=0,错误=0,暂无法判断=0,strict=None,weighted=None,error_rate=None,excluded_nonforecast=101,excluded_duplicate=0,evidence=3))
meta=dict(title='Cory Doctorow《魔法王国的落魄》（Down and Out in the Magic Kingdom，2003）',pub='2003年1月（原版；队列年份2003）',overall='严格归属口径的零分母边界案例：102个原始候选中，1个被原代码按rebutted排除，其余101个按reported自动unclear，resolvable=0。没有可评分的作者现实预测，不把这解释成小说没有前瞻性，也不把101条归属排除记作“未定预测”。建议协调者复核该边界后归档。',method='详见实际方法补充。',basis='',extra='101条原句与具体人物归属见 data/claims.jsonl 和 output/verify-v5-run/assess.jsonl；全部91块的逐块阅读日志见audit/reading-log.jsonl。')
(c/'audit/manual_review_2026-11-15.py').write_text('META = '+repr(meta)+'\nNF = {}\nV = {}\n')
js(c/'audit/coverage.json',dict(chunks=91,fully_read_chunks=91,first='txt-00001',last='txt-00091',characters=301956,covered_characters=301956,matter_skipped=0,raw_candidates=102,deterministic_excluded=1,overlap_duplicates=0,retained_candidates=101,resolvable=0,manual_semantic_dedupe=0,assess_duplicate=0,licenses_and_acknowledgements_read=True,tables_or_two_columns=False,source_sha256='d2d6e549b1c5f62173eebd97e1f2f2259199d1c3fde2abca7243038757b42a93'))
shutil.copyfile(w/'repo/SOURCE_COMMIT.txt',c/'audit/TOOLKIT_COMMIT.txt')
print('wrote',len(rows),'ASSESS boundary reviews; 3 evidence archives; zero scored forecasts')
