# Cory Doctorow《魔法王国的落魄》（Down and Out in the Magic Kingdom，2003）：出版后预测人工核查

- 案例目录：`cases/doctorow-down-and-out-in-the-magic-kingdom-v5/`
- 出版日期：2003年1月（原版；队列年份2003）
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

实际方法：对队列SHA256精确匹配的原生TXT按原代码3500/600分块，**91/91块全部顺序通读**，包括两套许可证、2003/2004说明、正文、致谢与RDF元数据；无关键词筛选，无双栏或表格需恢复。按DISCOVER_PROMPT_V5逐块手写JSON，由未修改的85e6da1原代码验证、归属筛选、重叠处理并导入。102条原始候选的quote全部精确匹配；1条rebutted由原代码排除，0条重叠去重，保留101条unclear。所有context已清空。

**本例resolvable=0。** 101条均是明确具名叙述者/角色或推荐人的表述，原代码以`third_party_view_not_endorsed`自动降为unclear；未因无日期、体裁或语义重复排除。为防将“小说没有作者预测”当作预设，保留了死亡治愈、声望、脑机接口、远程机器人、无期限社会方向、极远宇宙期限等具体候选，并逐条完成归属ASSESS和六维semantic review。99条角色场景的作者背书证据为unknown，2条封面推荐人归属明确；均不进入现实真假判分。这里的101项nonforecast是严格作者归属口径，不是101项错误或未定预测。

实际辅助研究为**1轮WebSearch正反各1查询**，SELECT选择3个搜索返回URL，WebFetch阅读后用urllib公开HTTPS抓取、存档并记sha256；未调用Exa或DeepSeek，无第3轮。3条evidence仅支持作品/归属边界，不是技术结果证据。零resolvable意味着逐预测PLAN任务数为0；不能据此声称逐条做了101项技术结果检索。原`pipeline.py apply assess → check → report`已执行；后由canonical manual_report.py生成，再对该报告中不适用于零分母案例的固定Exa/人工挑选模板句作如实的本案例修正，共享工具未改。

归属边界：2010年访谈（2015重刊）中Doctorow称自己“predict the present”，也把Free Energy称为思想实验的前提；同一访谈又承认自己预期过某些Disney设施会继续存在，且讨论Whuffie可能呈幂律分布。两面均保留，不能用一句“从不预测”就认定其全部设定无预测意味；也不能把2010新断言回填为2003原书预测。零分母只是在本次原严格归属规则下的结论，建议协调者复核后归档，不表示小说没有前瞻性。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

原始候选102条；原代码排除rebutted 1条，保留候选101条（全部unclear、resolvable=0）；归属复核101/101，计入 **0条现实作者预测、0条可判定**。严格/加权/错误率均为N/A（null），不是0%。

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

严格归属口径的零分母边界案例：102个原始候选中，1个被原代码按rebutted排除，其余101个按reported自动unclear，resolvable=0。没有可评分的作者现实预测，不把这解释成小说没有前瞻性，也不把101条归属排除记作“未定预测”。建议协调者复核该边界后归档。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | 101条保留候选见data/claims.jsonl | reported归属 | 全文逐块抽取，非人工挑选；101条均不进入可核验预测序列 |

## 文件

- 本文：`cases/doctorow-down-and-out-in-the-magic-kingdom-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/doctorow-down-and-out-in-the-magic-kingdom-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/doctorow-down-and-out-in-the-magic-kingdom-v5/audit/manual_review_2026-11-15.py`
101条原句与具体人物归属见 data/claims.jsonl 和 output/verify-v5-run/assess.jsonl；全部91块的逐块阅读日志见audit/reading-log.jsonl。
