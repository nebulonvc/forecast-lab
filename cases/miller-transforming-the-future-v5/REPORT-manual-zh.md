# Riel Miller 主编《转化未来：21世纪的预见》（Transforming the Future: Anticipation in the 21st Century，2018）：出版后预测人工核查

- 案例目录：`cases/miller-transforming-the-future-v5/`
- 出版日期：Riel Miller 主编《Transforming the Future: Anticipation in the 21st Century》于 **2018** 年由 UNESCO 与 Routledge 首次出版（UNESCO ISBN 978-92-3-100268-7）。所用文件为公开下载英文 PDF，301 页。PDF sha256 `be3081299c5d6e46f0456087ed6c488d97366244d3aa5770eed86529be9567ca`（17,149,399 字节，已与队列及 catalog source_url 逐字节核对一致）。观察窗口按 2018 年起算，至 2026-11-15。PDF/TXT 不入库。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

本稿按 METHOD.md 复刻 DeepSeek 流水线，只把模型调用换成助手人工阅读。抽取：用仓库 prepare_book v5（toolkit 来自 main `85e6da1`）把 pdftotext 全文切成 243 块（3500 字符、600 字符上下文），助手逐块通读正文，按 DISCOVER_PROMPT_V5 写出模型本应返回的 JSON（前后附文块回答为空），再由仓库代码完成引文对齐、非预测筛除和去重，得到 7 条候选，全部为可核验。核验：每条可核验候选先定 scope，用 Exa 各做一次 support/counter 检索，只从检索返回的 URL 中选源，存档到 `data/sources/`（sha256），写入 `data/evidence.jsonl`，再经 `pipeline.py apply assess → check → report`。本稿由助手逐条对照书中原文与存档证据人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 7 条，剔除非预测 0 条，计入 **7 条预测**，其中 **6 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 0 |
| 趋势符合 | 1 |
| 部分符合 | 5 |
| 错误 | 0 |
| 暂无法判断 | 1 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **0.0%**（0/6） |
| 加权胜率 | **54.2%** |
| 错误率 | **0.0%**（0/6） |
| 未定占比（暂无法判断/预测） | 14.3%（1/7） |

## 总体评价

这是一部关于预见素养与预期系统的方法论文集，可核验的作者本人未来判断很少。243 块中有 7 条可核验预测。可判定的 6 条中，0 条正确，1 条趋势符合（预见思维的流通与影响在增强，但远未达到“大得多”的终点），5 条部分符合（生活方式与体育、信息获取与舒适边界、性别流动条件句、女权理论的持续推动、崩溃与保守反弹），0 条错误。过滤气泡是否“更强”因文献争议判为暂无法判断。实验室工作坊中的情景与期望按转述/假想未计为作者预测。窗口仅约八年，趋势符合按严格口径使用。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 趋势符合（1 条）

- **#2** 「we are beginning to make out a not too distant future in which futures thinking enjoys far greater currency an…」  
  判断：**趋势符合**。UNESCO and some governments continued to expand futures-literacy and foresight work after 2018, including World Futures Day 2025 and a Global Anticipatory Policy coalition, which supports a direction of greater currency. Independent public-management research in 2026 still finds strategic foresight largely marginal, so the stated endpoint of far greater currency and impact has not been reached.  
  来源：<https://www.unesco.org/en/articles/world-futures-day-2025-unesco-advances-futures-literacy>；<https://www.emerald.com/ijpsm/article/doi/10.1108/IJPSM-05-2026-0275/1392510/From-a-peripheral-tool-to-a-core-principle>

### 部分符合（5 条）

- **#1** 「our lifestyles are likely to be deeply transformed. Sport will not escape such challenges」  
  判断：**部分符合**。COVID-19 and digitalization did change how people live and how sport is performed and consumed, so sport did not escape societal shock. But French and other participation series also show continuity and later recovery or even a slight rise in regular sport after 2018, so lifestyles and sport were not generally “deeply transformed” as a lasting, across-the-board result by 2026-11-15.  
  来源：<https://doi.org/10.2478/pcssr-2022-0011>；<https://www.sports.gouv.fr/sport-en-france-une-progression-continue-depuis-2018-boostee-par-les-jeux-de-paris-2024-10055>
- **#4** 「We will most likely know more overall in the future and will be able to find desired information very quickly,…」  
  判断：**部分符合**。Search and generative-AI tools after 2018 made desired information quicker to reach, and work on the “narrow search effect” supports comfort- or confirmation-bounded knowing. But reviews also show information overload and weaker science learning on social media, so it is not established that people “know more overall.”  
  来源：<https://www.pnas.org/doi/abs/10.1073/pnas.2408175122?af=R>；<https://www.scientificamerican.com/article/information-overload-helps-fake-news-spread-and-social-media-knows-it/>
- **#5** 「as long as gendered fluidity is repressed and penalised, and as long as our future imaginings are based on one…」  
  判断：**部分符合**。The condition only partly holds. ILGA and other records show expanded legal gender recognition in some jurisdictions, while CIVICUS, ILGA-Europe and reporting on the United States document a sharp 2020s rollback and repression of gender-fluid and trans rights in others. Where the condition holds, civic space is more constrained; it is not a uniform global “stifled present.”  
  来源：<https://publications.civicus.org/publications/2026-state-of-civil-society-report/gender-rights-rollback-and-resistance/>；<https://database.ilga.org/legal-gender-recognition>
- **#6** 「the influence of postmodern as well as feminist theories will continue to push towards such futures.」  
  判断：**部分符合**。Feminist and LGBTQ-inclusive policy work continued in some international and national settings after 2018, so a push toward more inclusive futures is visible. The same window also shows a documented global backlash and rollback of gender justice, so that push does not unambiguously continue as the dominant direction.  
  来源：<https://centreforfeministforeignpolicy.org/wordpress/wp-content/uploads/2023/10/Guidebook-Final-Web-Version.pdf>；<https://cdn.unrisd.org/assets/library/reports/2026/strategic-responses-to-backlash-against-gender-justice.pdf>
- **#7** 「economic and ecological collapse, increases in social conservatism and fundamentalism, various forms of backla…」  
  判断：**部分符合**。Democratic backsliding, conservative and ‘green’ backlash, and climate-policy strain after 2018 are well documented and pull toward less equitable climate and civic outcomes. International IDEA and other sources do not show a general economic or ecological collapse, so that half of the claim is not borne out.  
  来源：<https://www.nature.com/articles/s41558-025-02384-0>；<https://www.idea.int/publications/catalogue/html/global-state-democracy-2026-democracy-age-of-conflict>

### 暂无法判断（1 条）

- **#3** 「two contradictory occurrences are expected to continue and become even stronger in the future.」  
  判断：**暂无法判断**。A 2025 systematic review and other studies still disagree on whether filter bubbles and echo chambers exist, intensified, or usefully describe most users’ media diets. Because the claimed strengthening of both global communication and Filter Bubble limits is empirically contested, the claim cannot be scored on the archived record.  
  来源：<https://link.springer.com/article/10.1007/s42001-025-00381-z>；<https://mediatechdemocracy.com/files/publications/echo-chambers-filter-bubbles_2023.pdf>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/miller-transforming-the-future-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/miller-transforming-the-future-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/miller-transforming-the-future-v5/audit/manual_review_2026-11-15.py`

## 说明

- 抽取密度（7 条可核验 / 243 块 ≈ 0.029）低于 METHOD §5 英文书参考区间（约 0.2—0.35）。本书以预期理论、实验室方法和已发生的工作坊案例为主；参与者情景、规范性倡议与研究议程未计为预测；序言、致谢、术语表与索引按前后附文排除。未为提高数量而放宽标准。
- 趋势符合只在存档证据明确证实方向、且明确终点尚未到达时使用。过滤气泡是否增强因系统综述仍有分歧，判为暂无法判断。
- 证据以独立第三方为主（学术期刊、联合国教科文组织、ILGA、International IDEA、政府体育统计等）。
- `data/claims.jsonl`、`output/txt_import/claims_proposals.jsonl` 及评估快照中的 `context` 字段已清空。

