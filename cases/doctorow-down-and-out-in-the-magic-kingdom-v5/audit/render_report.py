"""Use canonical report generator then replace inapplicable zero-case boilerplate, not shared tools."""
from pathlib import Path
import subprocess,sys,json
c=Path(__file__).resolve().parents[1]
canonical=Path(sys.argv[1]) if len(sys.argv)>1 else Path('/workspace/forecast-line-b/tools/manual_report.py')
subprocess.run([sys.executable,str(canonical),str(c)],check=True)
p=c/'REPORT-manual-zh.md';t=p.read_text();a=t.index('## 方法说明');b=t.index('五级判断：',a)
t=t[:a]+(c/'audit/REPORT-method.md').read_text()+t[b:]
t=t.replace('候选 0 条，剔除非预测 0 条，计入 **0 条预测**，其中 **0 条可判定**。','原始候选102条；原代码排除rebutted 1条，保留候选101条（全部unclear、resolvable=0）；归属复核101/101，计入 **0条现实作者预测、0条可判定**。严格/加权/错误率均为N/A（null），不是0%。')
t=t.replace('| — | （无） | — | 候选为人工挑选，未收入非预测 |','| — | 101条保留候选见data/claims.jsonl | reported归属 | 全文逐块抽取，非人工挑选；101条均不进入可核验预测序列 |')
p.write_text(t)
s=c/'output/manual-final/summary.json';st=json.loads(s.read_text());st.update(raw_candidates=102,retained_candidates=101,resolvable=0,source_chunks=91,boundary_evidence_records=3);s.write_text(json.dumps(st,ensure_ascii=False,indent=2)+'\n')
