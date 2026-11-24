# 斯台普顿《最后与最初的人》（1930）：出版后预测人工核查

- 案例目录：`cases/stapledon-last-and-first-men-v5/`
- 出版日期：1930
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

本书实际流程：对未经改动的队列TXT按原3500/600分块，213/213块逐块全文阅读并手写候选；本轮从161块接读，保留此前160块经hash验证的答案，仅139项按要求真实连续扩引文。203项同样跨204块连续扩至完整句尾，均经原validate_chunk_predictions与claims_from_results处理。原始782候选（759 forecast、23 unclear）全部保留，没有语义去重、没有ASSESS duplicate；原代码自动重叠去重0。

全书后逐条复核作者/角色归属：此前607候选结合完整读书日志及逐条首尾引文归属索引复核；新增175项在本轮全文阅读、手写及复核。不是把“小说”或“无日期”当排除条件。735项为末人叙述者，47项为其嵌入角色/群体；现实作者明确说正文第一人称并非自己，并区分审美安排的毁灭与现实和平希望。引言中“Yet the story is true”是叙述者的宣称，同段明确说实际作者自己不相信；没有因此虚构作者背书。序言中实际作者自己的未来判断，依METHOD §1关于序言的规定不抽取，而非因其小说体裁排除。

原归属规则将782项保留为unclear，resolvable=0。本次仍为每个保留候选记录归属决定、ASSESS排除及六维语义复核，并跑apply/check/report；不是把未成熟的前缀unclear统计当整书结论。没有须事实判分的作者预测，故事实核验PLAN/support/counter/SELECT及Exa检索均未触发，搜索查询0。公开原典TXT实际抓取1次，响应SHA256与队列原件完全一致；仅4段短归属边界摘录存入data/sources并逐条sha256，不存全书。不声称这4段能验证任何科幻情节的现实成败。

四张时间轴图此前已实际视觉通读，本轮核对manifest及阅读记录：相关文明、战争、迁徙和终结事件在正文抽取。TXT仅有图占位，独立图内刻度及“若无意外地球仍宜居”的括示不能冒充TXT逐字quote，未强行导入；这是TXT主源表示限制，非语义去重。原图无标注的精确年份也未杜撰。图内独立信息不能视为已单独完成事实判分。

评分窗口为1930→2026-11-15（Asia/Shanghai）。作者预测0、可判定0，正确/趋势/部分/错误/未定均0；strict、weighted、error rate均N/A（JSON null），不表示准确率0%。此结论只适用于严格作者明确断言/采纳口径，不否认该书的情景研究价值。

## 统计

原始及保留候选均782条，原提取resolvable=0。782条归属排除已逐项记录；计入 **0 条作者预测**，其中 **0 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 0 |
| 趋势符合 | 0 |
| 部分符合 | 0 |
| 错误 | 0 |
| 暂无法判断 | 0 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **—**（0/0） |
| 加权胜率 | **—** |
| 错误率 | **—**（0/0） |
| 未定占比（暂无法判断/预测） | —（0/0） |

## 总体评价

全书213块、737199字符，手写782候选（759原始forecast、23原始unclear）；并非小说一律排除。实际作者序言明确说正文第一人称不是实际作者，并明确区分审美安排的毁灭与现实和平运动成功的可能。逐项复核后，735项为未来叙述者陈述、47项为嵌入角色/群体预期，未发现正文中实际作者另行明确采纳的可判定预测。原代码将782项保留为unclear、resolvable=false；0额外语义去重、0 ASSESS duplicate。作者预测0，评分N/A/null，不是782条错误或782条暂无法判断。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 全部782个候选仍保留，逐项归属决定见audit/attribution_review.jsonl，不在此重复整表 |

## 文件

- 本文：`cases/stapledon-last-and-first-men-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/stapledon-last-and-first-men-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/stapledon-last-and-first-men-v5/audit/manual_review_2026-11-15.py`
完整候选与逐项归属决定见data/claims.jsonl、audit/attribution_review.jsonl；四条公开原典边界存档见data/evidence.jsonl。
