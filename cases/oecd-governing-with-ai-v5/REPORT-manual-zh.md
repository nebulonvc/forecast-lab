# OECD《用人工智能治理：核心政府职能的现状与方向》（Governing with Artificial Intelligence: The State of Play and Way Forward in Core Government Functions）：出版后预测人工核查

- 案例目录：`cases/oecd-governing-with-ai-v5/`
- 出版日期：**2025-09-18** 正式出版（Public Governance Committee 批准并解密日期 05/09/2025）。工作正文取自官方 PDF https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/06/governing-with-artificial-intelligence_398fa287/795de142-en.pdf（doi 10.1787/795de142-en），浏览器 UA 下载，5,581,859 字节，sha256 `d208d9eed5b435750edc07cb8c6146220b97a7e65e63c78869ab44c24a429808`，与队列完全一致。pdftotext -enc UTF-8 得到 TXT，sha256 `a96b5639323a5d6d82f0d409204e3413f35a80762f32c70e8594f34f7d8dcf18`，1,007,753 字节，UTF-8 无 BOM、仅 LF，1,002,029 字符。预测窗口按 2025-09-18→2026-11-15 计。PDF/TXT 不入库。publication_year_proxy 2025。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

本稿按 METHOD.md 复刻 DeepSeek 流水线，只把模型调用换成助手人工阅读。抽取：用仓库 prepare_book v5（toolkit 来自 main `85e6da1dc0f185830a6ea9037d731fd39a27411e`，prepare_book.py md5 `01fc49ad64795a345ca1cb32bb2e4366`）把全文切成 291 块（3500 字符、600 字符上下文），助手逐块通读（含前后附文、章末参考文献与注释），按 DISCOVER_PROMPT_V5 写出模型本应返回的 JSON（可为空），再由仓库代码完成引文对齐、非预测筛除、归属降级和去重。英文 changes 均为 quote 的逐字单行子串；horizon/time_text 仅在引文中原文出现时填写。核验：对每条可核验候选先定 scope，用 Exa 各做至多两轮 support/counter 检索（密钥仅按文件路径读取 `~/.config/forecast-lab/exa-new-2.key`，未打印、未入库），只从检索返回的 URL 中选源，存档到 `data/sources/`（sha256），写入 `data/evidence.jsonl`（3 条），再经 `pipeline.py apply assess → check`。报告由 canonical `/workspace/forecast-line-b/tools/manual_report.py`（md5 `682248fa9f6c63e3492a559ccac12761`）生成，未手改。claims 的 context 在报告生成后全部清空。本稿由助手逐条对照书中原文与存档证据人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 1 条，剔除非预测 0 条，计入 **1 条预测**，其中 **0 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 0 |
| 趋势符合 | 0 |
| 部分符合 | 0 |
| 错误 | 0 |
| 暂无法判断 | 1 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **—**（0/0） |
| 加权胜率 | **—** |
| 错误率 | **—**（0/0） |
| 未定占比（暂无法判断/预测） | 100.0%（1/1） |

## 总体评价

这是 2025 年 9 月出版的 OECD 政府治理报告，正文大量为已发生的用例、规范性“应当/需要”、进行中试点与无期限路线图。导入候选 5 条：1 条可核验的作者背书预测（OECD 税收征管论坛计划于 2026 年发布其税收征管 AI 部署框架试点研究结果），判定暂无法判断；4 条第三方转述（Global Coalition 2025–2026 审议大会、英国 DWP 至 2030 年节约 16 亿英镑、葡萄牙 gov.pt 2025 年交易功能、TBI 至 2040 年每年 60 亿英镑预防性医疗节约）按 v5 归属规则降为 unclear、不可核验，不改归属以求计分。可判定 0。严格胜率、加权胜率与错误率在无可判定样本时记为未定义。另有 1 条（OECD (2024[24]) 今后十年生产率 0.25–0.6 个百分点）被 year-screen 标为 historical 排除，完整引文保留在真实 policy_report 中，见人工复核记录，未剪年份、未改 toolkit、未强行计入得分。出版至截止仅约 14 个月，短窗从严，未把“in 2026”在年尚未结束时判为错误。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 暂无法判断（1 条）

- **#1** 「The Forum on Tax Administration plans to publish its findings from this work in 2026.」  
  判断：**暂无法判断**。书中承诺的是OECD税收征管论坛（FTA）就其正在试点的、基于OECD可信AI原则、覆盖AI生命周期的税收征管AI部署框架“在2026年发布研究结果”。截至截止日2026-11-15：2026-04-29 OECD税务博客仍称FTA已设立专项工作组、旨在把原则转化为具体框架与工具，未宣布该试点研究结果已经出版；2026-06-29日本财务省研讨会上FTA主席办公室材料将“Trustworthy AI in Tax Administration”列为2026年TA3.0项目组合中的进行中项目；2026-11-12出版的《Digitalisation and Digital Transformation in Tax Administrations》是108个辖区ITTI技术应用概览，虽提及AI使用与保障，但对象是数字化调查报告，不能视为上述AI部署框架试点研究结果的发表。因视窗“in 2026”在2026-11-15尚未结束，且未发现该特定研究结果已发表的充分证据，也不能因年尚未结束而判错误。短窗从严，判定暂无法判断。  
  来源：<https://www.oecd.org/en/blogs/2026/04/artificial-intelligence-in-tax-administration-from-early-innovation-to-modern-transformation.html>；<https://www.mof.go.jp/pri/research/seminar/fy2026/tff2026_14.pdf>；<https://www.oecd.org/en/publications/digitalisation-and-digital-transformation-in-tax-administrations_5976063c-en.html>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/oecd-governing-with-ai-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/oecd-governing-with-ai-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/oecd-governing-with-ai-v5/audit/manual_review_2026-11-15.py`


## 说明

- 抽取密度：1 条可核验 / 291 总块 ≈ 0.0034。本书 2025 年 9 月出版、截止 2026-11-15，前瞻窗口极短，正文又以现状、案例与规范建议为主，低密度符合预期。未为凑密度放宽 DISCOVER_PROMPT_V5；未把规范“should/will need”、无期限“is developing/upcoming/coming months”、含糊 could/may/expected to，或政策文本中的法定义务本身收为预测。
- 前后附文人工排除记录：仓库中文 `MATTER_HEADING` 正则无法匹配本报告英文封面、目录、参考文献与 Notes 标题，故 toolkit `skipped_matter_chunks=[]`、`excluded_matter_spans=[]`，须人工排除并记录。

| 区段 | 字符偏移 | 内容 | 块 | 抽取 |
| --- | --- | --- | --- | --- |
| 前附文 COVER/LEGAL | 0–3522 | 封面、版权与法律声明 | txt-00001；txt-00002 开头 | 不抽 |
| 前附文 FOREWORD | 3522 起 | Foreword | 中段 txt-00002 | 不抽 |
| 前附文 ACKNOWLEDGEMENTS | 6895 起 | Acknowledgements | txt-00003；txt-00004 开头 | 不抽 |
| 前附文 TOC | 11425 起 | 目录及图表目录 | 中段 txt-00004 至中段 txt-00005 | 不抽 |
| 前附文 EXECUTIVE SUMMARY | 16541–23588 | 执行摘要（已通读；与后文章节去重） | 中段 txt-00005 至中段 txt-00007 | 不抽新条（无独立候选留下） |
| 前附文 ACRONYMS | 23588–26243 | 缩略语 | 中段 txt-00007 至中段 txt-00008 | 不抽 |
| 正文 BODY | 26243–926451 | 第 1–5 章正文（第 1–4 章参考文献与注释已通读并排除抽取） | 中段 txt-00008 至中段 txt-00269 | 导入 5 条候选均在此区间 |
| 后附文 REFERENCES | 926451–994756 | 全书末参考文献 | 中段 txt-00269 至中段 txt-00289 | 不抽 |
| 后附文 NOTES | 994756–1000916 | 章末注释（URL 与定义） | 中段 txt-00289 至中段 txt-00291 | 不抽 |
| 后附文 BACK COVER | 1000916–1002029 | 封底介绍与 ISBN | 中段/末 txt-00291 | 不抽 |

- 第 4 章参考文献约自中段 txt-00141 至中段 txt-00150，第 4 章 Notes 自中段 txt-00150 至中段 txt-00155；第 5 章正文标题在字符 532868 / 中段 txt-00155。这些章末文献与注释已通读，未抽取。
- 一致性复核：全文读完后对照 145 段以后的标准，复查 001–144 排除日志。仅补记 txt-00138（Global Coalition 于 2025 和 2026 年将举办审议大会）：有明确年份的机构计划，与后段葡萄牙 2025 年功能上线同类；“intend to reach more than 10 000 citizens”只作意向、不作硬目标。补记见 `work/AUDIT_consistency_001-144.md`。韩国《AI 基本法》2026 年 1 月生效是已立法的施行日程而非未实现的工作成果预测；英国 digital leader by 2026、美国 180 天战略是政策文本义务描述；无期限或含糊 could/may/coming months 各项仍不补。001–144 其余原答案未改写。
- txt-00013 筛选：完整引文含 “OECD (2024[24]) … over the next 10 years”，被 year-screen 标为 historical（2024 < 2025，且英文 “the next 10 years” 不匹配中文 `_FUTURE_WINDOW`）。十年窗口锚定 Filippucci, Gal and Schief, OECD AI Papers No. 29（2024-11-22），约自 2024 年末至 2030 年代中期，不随本书 2025-09-18 重置。人工阅读仍视为未关闭的生产率预测。按要求保留真实 `policy_report`（副本 `work/policy_report_authentic.json`），另写 `work/HUMAN_REVIEW_txt-00013.md` 与 `work/AUDIT_txt-00013.md`；不剪年份、不改 toolkit、不强制计入得分。
- 归属：4 条 reported 按 v5 降为 unclear / 不可核验，不改成 author 或 author_endorsed 以求计分。
- 可核验条（FTA 2026 年发表研究结果）：2026-04-29 OECD 税务博客仍称 FTA 项目组旨在把原则转化成框架；2026-06-29 FTA 主席办公室材料将 Trustworthy AI in Tax Administration 列为 2026 年进行中项目；2026-11-12 ITTI 数字化报告对象不匹配。视窗 “in 2026” 在 2026-11-15 尚未结束，短窗从严记暂无法判断，不判错误。
- 检索摘录取自公开页面存档。候选引文之间无连续 300 字符重合。案例 `data/claims.jsonl` 的 `context` 在 canonical 报告生成后全部清空。toolkit 保持 main `85e6da1`，未改。

