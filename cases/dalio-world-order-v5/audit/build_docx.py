import json,re
from docx import Document
from docx.shared import Pt
from docx.oxml.ns import qn
clean=lambda x: re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]','',str(x or ''))
order=['正确','趋势符合','部分符合','错误','暂无法判断']
base='/workspace/dalio/repo/cases/dalio-world-order-v5/output/verify-final/'
rows=[]
for l in open(base+'results.slim.jsonl'):
    d=json.loads(l); a=d.get('assessment') or {}
    if not a or a.get('nonforecast') or d['display_verdict'] not in order: continue
    rows.append(tuple(clean(x) for x in (d['display_verdict'],d.get('claim',''),d.get('quote',''),a.get('reason',''),a.get('future_time_text',''))))
doc=Document()
st=doc.styles['Normal']; st.font.name='Microsoft YaHei'; st.font.size=Pt(10.5)
st.element.rPr.rFonts.set(qn('w:eastAsia'),'Microsoft YaHei')
doc.add_heading('达利欧《原则：应对变化中的世界秩序》：预测判断最终结果',0)
doc.add_paragraph('判定截止日期：2026-11-15，观察窗口从英文原版出版（2021-11-30）算起。只收录真正的预测，一般机制、格言、方法说明、假想情景等非预测已剔除；没写时间的趋势判断，按「从出版到现在是否已经发生」评判。')
doc.add_heading('结论',1)
cnt={k:sum(1 for r in rows if r[0]==k) for k in order}
dec=sum(cnt[k] for k in order[:4])
strict=cnt['正确']/dec; w=(cnt['正确']+0.75*cnt['趋势符合']+0.5*cnt['部分符合'])/dec
doc.add_paragraph(f'共 {len(rows)} 条预测。其中正确 {cnt["正确"]} 条，趋势符合 {cnt["趋势符合"]} 条，部分符合 {cnt["部分符合"]} 条，错误 {cnt["错误"]} 条，暂无法判断 {cnt["暂无法判断"]} 条。')
doc.add_paragraph(f'在 {dec} 条可判定的预测中，严格胜率（完全正确的占比）为 {strict:.1%}；加权胜率为 {w:.1%}，按正确 1 分、趋势符合 0.75 分、部分符合 0.5 分、错误 0 分计算。')
for k in order:
    sub=[r for r in rows if r[0]==k]
    if not sub: continue
    doc.add_heading(f'{k}（{len(sub)} 条）',1)
    for i,(v,c,q,r,t) in enumerate(sub,1):
        p=doc.add_paragraph(); p.add_run(f'{i}. {c}').bold=True
        if q: doc.add_paragraph('原文：'+q.replace('\n',''))
        if t: doc.add_paragraph('时间范围：'+t)
        doc.add_paragraph('结果：'+v)
        doc.add_paragraph('原因：'+re.sub(r'且?trend_aligned=(true|false)|（理由按人工复核改写，结论不变）','',r))
fn='/workspace/final-docs/达利欧《原则：应对变化中的世界秩序》-预测判断.docx'
doc.save(fn); print(fn,len(rows),cnt,f'{strict:.3f} {w:.3f}')
