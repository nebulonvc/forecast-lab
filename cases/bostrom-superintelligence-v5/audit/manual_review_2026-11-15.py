# Manual review source for bostrom-superintelligence-v5 (worker-f6)
# Loaded by canonical manual_report.py. V is defined in V.py.
from pathlib import Path
import runpy

_V = runpy.run_path(str(Path(__file__).resolve().parent / "V.py"))
V = _V["V"]
NF = {}

META = {
    "title": "尼克·博斯特罗姆《超级智能》（Superintelligence: Paths, Dangers, Strategies，2014）",
    "pub": "**2014年7月**（牛津大学出版社第一版第一次印刷，英国发行日期 2014-07-03）。正文为 reading-library/2026-11-15-未来判断书单/03-科技和AI/15-超级智能.pdf（书内题名为 Superintelligence: Paths, Dangers, Strategies，版权页载明 © Nick Bostrom 2014、First Edition published in 2014、Impression: 1），sha256 `654b8bed510be5def0117192a56c99c53d0cb9a3b49a92f82f97834c366b7364`，已与 catalog.json / SHA256SUMS 核对。TXT 由 `pdftotext -enc UTF-8`（不加 `-layout`）生成，sha256 `24d36f2b5e065f8ee57ba20a189607d195ff2b5cd456f65571f6b1a5a85298a2`。观察窗口为 2014-07→2026-11-15。书中写明的终点（本世纪、本世纪中叶、未来十五年、十年到二十年、二十二世纪之前、本世纪下半叶、本世纪晚些时候）按各自时点判断；以“人类水平机器智能 / 起飞 / 超级智能已经出现”为前提的判断，前提未出现则记暂无法判断。",
    "method": "本稿是按 METHOD.md 的全文通读重做版（替代此前关键词筛选、证据为空的 30 条旧稿，对应仍打开的 PR #26）。抽取：用仓库 toolkit main 85e6da1 的 prepare_book v5 把全文切成 310 块（3500 字符、600 字符上下文；txt-00001…txt-000310，覆盖第 1–15 章、注释、参考文献与索引），助手逐块通读、按 DISCOVER_PROMPT_V5 写出模型本应返回的 JSON，再由仓库代码 `validate_chunk_predictions` 与 `claims_from_results` 完成引文对齐、非预测筛除、归属降级、去重和导入，得到 100 条候选、95 条可核验预测（另 5 条转述第三方观点被降为 unclear）。核验：按 METHOD.md 用 Exa 检索公开来源（池密钥第 4 条，只按文件路径读取）并抓取存档（data/sources/，sha256 记于 data/evidence.jsonl，共 65 条），由助手阅读后按规则 10 从严对待“趋势符合”，经 pipeline.py apply assess → check → report。claims.jsonl 的 context 字段已清空。manual_report.py 使用 /workspace/forecast-line-b/tools/manual_report.py（md5 682248fa9f6c63e3492a559ccac12761）。本稿未使用 DeepSeek API。",
    "basis": "本稿由助手逐条对照书中原文与存档证据人工复核：",
    "overall": "本书的核心论题（机器超级智能的默认结局是存在性灾难、起飞速度、人类水平机器智能本世纪或本世纪中叶的机会）在截止日前大多仍无法判定：前提（超级智能或人类水平机器智能已被创造）尚未出现，或写明的远期终点尚未到达，故 95 条预测中有 51 条记暂无法判断。可判定的 44 条集中在较短窗口：监控与行为数据积累、软件任务范围扩大、硬件与算力继续提升、实验室竞赛、脑机接口尚未作为认知增强被广泛使用、化学路径难以带来戏剧性智商跃升、意外概念突破（Transformer，2017）等 21 条为正确；全脑仿真约 2029 年难以实现、生殖系基因改造在本世纪中叶前难有显著人口影响、控制问题现有方法在数十年尺度上仍不足等 9 条为趋势符合；围棋击败世界冠军（时点早于线性外推、路径为深度学习而非每年一段）、自然语言理解接近但仍非全面人类水平、2014 年已有原型的技术后来产生重大影响但 Transformer 当时尚未出现等 14 条为部分符合。错误 0 条。严格胜率 47.7%，与旧稿 50.0% 接近；加权胜率 79.0%，略低于旧稿 82.8%，主要因为新方法覆盖面更宽，并按规则 10 对“趋势符合”更严。这首先反映作者把大胆判断收在条件句和远期窗口里，而不是超级智能的核心故事已被证实。",
    "extra": """
## 说明

- 旧关键词稿（PR #26）抽出 30 条候选、26 条预测（可判定 16 条：正确 8、趋势符合 5、部分符合 3、错误 0、暂无法判断 10；严格胜率 50.0%，加权 82.8%），且 data/evidence.jsonl 为空。本稿覆盖了旧稿全部 30 条判断所对应的命题（含 4 条当时被标为非预测、现按全文规则重新归类的条目），并补入全书其余可核验预测。
- 密度为 95 条可核验预测 / 310 块 ≈ 0.31 条/块；若只计正文块，略高于 METHOD.md 英语书 0.2–0.35 条/块的参考区间。这是体裁决定的：本书是关于超级智能路径、风险与策略的预测专著，显式、对冲、条件与定量判断密集。助手通读了全部 310 块（含注释中两条正文未重复的作者预测；参考文献与索引未抽新预测），未用机制句或未触发的玩具情景凑密度。
- 5 条 resolvable=false 的候选是流水线将“转述第三方、作者未背书”的观点降为 unclear（专家调查中位数、Chalmers/Moravec 时点、全脑仿真路线图、干细胞专家、人口学家），不进入预测分母。
- 统计以 pipeline.py report 的 summary.json 与本稿 summary.json 为准；二者对 正确 / 趋势符合 / 部分符合 / 错误 / 暂无法判断 的计数一致。
""",
}
