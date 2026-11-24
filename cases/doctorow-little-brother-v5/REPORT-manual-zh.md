# Cory Doctorow《小兄弟》（Little Brother，2008）：出版后预测人工核查

- 案例目录：`cases/doctorow-little-brother-v5/`
- 出版日期：2008（只采用已知出版年，不杜撰月日）
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

本例按全文及小说特别规则逐项审归属和现实时间边界；19项unclear/reported，无resolvable。下面是canonical工具固定通用流程，逐条Exa本例未触发；实际仅WebSearch+curl补充同期作者采访边界证据。先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 0 条，剔除非预测 0 条，计入 **0 条预测**，其中 **0 条可判定**。

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

完整全文审读后没有满足“具体有期限的现实社会/技术预测且由作者独立认领”的可判分项。19项全部保留供复核；不将小说虚构现状、角色叙述或相似的后来现实当成作者预测胜负。建议协调者优先复核本零分母案例的归属边界。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/doctorow-little-brother-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/doctorow-little-brother-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/doctorow-little-brother-v5/audit/manual_review_2026-11-15.py`
## 本书特殊边界与实际执行

- 200/200块全文已读，658893字符；包含导言、所有章节、后记、两篇后语、书目、致谢及CC许可。单栏TXT，无双栏重排或OCR。
- 原始19候选，原代码保留19 unclear/reported，resolvable0。无语义去重，自动重叠去重0，ASSESS duplicate0。原始即unclear，不谎称自动demote19；原代码自动将claim_type规范为forecast，但kind/resolvable未变。
- canonical上文“候选0”指resolvable子集；19条边界逐项审读在output/verify-v5-run/assess.jsonl。无评分预测，不能将19条叫“暂无法判断”。
- 实际检索为WebSearch正反各1问、1轮，SELECT两个搜索返回URL，curl抓取2008年采访的文章片段。Exa/逐条现实结果核验通用段本例不适用，无第三轮、无DeepSeek调用。
- 作者在2008年同期采访将其称为YA adventure novel、“predicts the present”及“presentist”；仅据此补强边界，不把体裁单独作为排除每条的唯一依据，也不把采访外的新断言追加为原书候选。
- strict/weighted/error rate均null（分母0），不是0%或100%；五级计数均0，不能据本案断言作者预测全对或全错。
- 原文是作者分发TXT的精确GitHub队列blob，sha256与队列完全一致；含2008-11-27导言更新及后改书店信息，不称“初版逐字转录”。依METHOD不抽序言/后语，出版基准仅已知2008年，未杜撰具体首版日，隐含评分窗仍2008→2026-11-15。
- toolkit快照没有.git，不能git log；已用GitHub原提交85e6da1递归树逐个Git blob SHA-1核对toolkit全部38文件，38/38一致，零缺失/差异。原代码未改。

