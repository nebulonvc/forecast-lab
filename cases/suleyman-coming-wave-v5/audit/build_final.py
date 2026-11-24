"""Merge machine results + manual decisions into output/verify-final (2026-11-15)."""
import json, collections
from pathlib import Path
root = Path(__file__).resolve().parents[1]
ns = {}; exec((root/'audit/manual_decisions_2026-11-15.py').read_text(), ns)
NF, V, MA, AU, IH, RR = ns['NF'], ns['V'], ns['MA'], ns['AU'], ns['IH'], ns['RR']
claims = {json.loads(l)['id']: json.loads(l) for l in open(root/'data/claims.jsonl')}
rows = [json.loads(l) for l in open(root/'output/verify-v5-combined/results.jsonl')]
ORDER = ['正确','趋势符合','部分符合','错误','暂无法判断']
def disp(a):
    if not a or not a.get('verdict'): return None
    return '趋势符合' if a.get('trend_aligned') and a.get('verdict')=='部分符合' else a['verdict']
def stats(vs):
    c = collections.Counter(vs); out = {k: c.get(k,0) for k in ORDER}
    dec = sum(out[k] for k in ORDER[:4]); n = sum(out.values())
    out.update(可判定=dec, 计分样本=n,
        严格胜率=round(out['正确']/dec,4) if dec else None,
        加权胜率=round((out['正确']+.75*out['趋势符合']+.5*out['部分符合'])/dec,4) if dec else None,
        错误率=round(out['错误']/dec,4) if dec else None,
        未定占比=round(out['暂无法判断']/n,4) if n else None)
    return out
stage = {'machine':[], 'after_manual_stuck':[], 'after_audit':[], 'after_implicit_horizon':[]}
final=[]; slim=[]; nf_count=0; changes=[]
for i, d in enumerate(rows, 1):
    c = claims[d['claim_id']]; ext = c.get('extraction_v2') or {}
    a = dict(d.get('assessment') or {}) if d['task_state']=='completed' else {}
    mv = disp(a)
    if mv: stage['machine'].append(mv)
    rec = dict(d); rec['machine_task_state'] = d['task_state']; rec['machine_display_verdict'] = mv
    src = d['merge_source']; review = None
    if i in NF:
        t, why = NF[i]
        a = dict(a or {'id': d['claim_id']}); a.update(verdict='暂无法判断', trend_aligned=False,
            nonforecast=True, nonforecast_type=t, reason='非预测（'+t+'）：'+why)
        review = MA if d['task_state']!='completed' else AU
    elif i in V:
        v, tr, why, tag, ev = V[i]
        a = dict(a or {'id': d['claim_id']}); a.update(verdict=v, trend_aligned=tr, reason=why,
            manual_evidence=[{'url':u,'quote':q} for u,q in ev])
        a.pop('remaining_gap', None)
        review = tag
    elif i in RR:
        assert mv == '暂无法判断'
        a = dict(a); a['machine_reason'] = a.get('reason'); a['reason'] = RR[i]; review = AU
    dv = disp(a)
    nonf = bool(a.get('nonforecast'))
    if nonf: nf_count += 1
    # stage tracking (non-forecasts excluded from scored stages after audit)
    if review==MA or (mv and review is None) or (mv and review in (AU, IH)):
        pass
    s_stuck = dv if (d['task_state']!='completed' and review==MA) else mv
    if s_stuck and not (review==MA and nonf): stage['after_manual_stuck'].append(s_stuck if not (review==MA and nonf) else None)
    s_audit = None if nonf else (mv if review==IH else dv)
    if review==MA and not nonf: s_audit = dv
    if s_audit: stage['after_audit'].append(s_audit)
    if not nonf: stage['after_implicit_horizon'].append(dv)
    if review: changes.append(dict(idx=i, claim_id=d['claim_id'], review_source=review, before=mv, after=('非预测' if nonf else dv)))
    rec.update(assessment=a, task_state='completed', display_verdict=dv, review_source=review)
    final.append(rec)
    slim.append(dict(claim_id=d['claim_id'], task_state='completed', display_verdict=dv, quote=c.get('quote',''),
        claim=ext.get('expanded_claim') or ext.get('claim') or c.get('claim',''),
        horizon_source=ext.get('horizon_source'), merge_source=src, review_source=review,
        assessment={k: a.get(k) for k in ['verdict','trend_aligned','reason','limitation','observation_end','future_time_text','nonforecast','nonforecast_type'] if a.get(k) is not None},
        evidence_urls=[e['url'] for e in a.get('manual_evidence',[])] or
            [e.get('url') for e in d.get('evidence_candidates') or [] if e.get('id') in (a.get('evidence_ids') or [])]))
out = root/'output/verify-final'; out.mkdir(parents=True, exist_ok=True)
with open(out/'results.jsonl','w') as f:
    for r in final: f.write(json.dumps(r, ensure_ascii=False).replace('\u2028',' ').replace('\u2029',' ')+'\n')
with open(out/'results.slim.jsonl','w') as f:
    for r in slim: f.write(json.dumps(r, ensure_ascii=False).replace('\u2028',' ').replace('\u2029',' ')+'\n')
byh = collections.defaultdict(list)
for r in slim:
    if r['assessment'].get('nonforecast'): continue
    byh[r['horizon_source'] or 'unspecified'].append(r['display_verdict'])
summary = dict(case='suleyman-coming-wave-v5', cutoff='2026-11-15', publication='2023-09-05 (English original The Coming Wave, Crown)',
    reviewed_at_asia_shanghai='2026-11-15', n_candidates_verified=len(rows), 非预测=nf_count, 预测=len(rows)-nf_count,
    machine_completed=stats(stage['machine']),
    after_audit=stats(stage['after_audit']), after_implicit_horizon=stats(stage['after_implicit_horizon']),
    by_horizon={k: stats(v) for k,v in byh.items()},
    review_counts=dict(collections.Counter(c['review_source'] for c in changes)),
    manual_stuck_items=sum(1 for c in changes if c['review_source']==MA),
    changes=changes)
json.dump(summary, open(out/'summary.json','w'), ensure_ascii=False, indent=1)
print(json.dumps({k:v for k,v in summary.items() if k!='changes'}, ensure_ascii=False, indent=1))
