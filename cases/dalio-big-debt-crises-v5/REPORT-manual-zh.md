# 瑞·达利欧《债务危机》（Principles for Navigating Big Debt Crises，2018年9月）：出版后预测人工核查

- 案例目录：`cases/dalio-big-debt-crises-v5/`
- 出版日期：**2018年9月**（桥水于雷曼危机十周年发布英文全本，PDF 创建日期 2018-09-27 CST）。正文为 reading-library/2026-11-15-未来判断书单/04-经济和金融/30-债务危机.pdf（桥水公开英文 PDF，480 页），sha256 `7730b3be98d735950c28b1e47c8f9ca289b85d6c7588afdbd7c2cba63160ddb9`。TXT 由 `pdftotext -enc UTF-8`（默认版式，保留换页符）生成，sha256 `9893c02dfaa68c3cd2eb7c7501c8f7e54589bce629f76173e67558c9889de6ef`。观察窗口为 2018-09→2026-11-15。中文版《债务危机》2019 年出版，不作为本文本依据。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

本稿是按 METHOD.md 的全文重读重建版（worker f7），替代 f5 的 5 条低召回版本（该版已改名为 pr-book-dalio-big-debt-crises-v5-f5-lowrecall，未开 PR）。抽取：用仓库 toolkit main 85e6da1 的 prepare_book v5 把全文切成 361 块（3500 字符、600 字符上下文），助手独立于 f5、逐块通读全部 361 块（无跳读），按 DISCOVER_PROMPT_V5 写出模型本应返回的 JSON（逐块记录见 PR 说明），再由仓库代码完成引文对齐、非预测筛除、归属降级、去重和导入，得到 9 条候选、8 条可核验预测。核验：f5 已存档证据覆盖的 4 条直接复用其来源与判断；新增 4 条按 METHOD.md §4 先写 scope，各做一次 support 与 counter 的 Exa 检索（池密钥第 4 条，只按文件路径读取），原文存档于 data/sources/（sha256 记于 data/evidence.jsonl），由助手阅读后按四分类规则评断，经 pipeline.py apply assess → check → report。claims.jsonl 的 context 字段已清空。manual_report.py 使用规范版（md5 682248fa…）。趋势符合从严（规则 10）：仅在存档证据清楚确认方向时使用，不以“尚未被证伪”记为趋势符合。本稿以 v5 抽取的候选句（`data/claims.jsonl` 中可判定的条目）为起点，由助手逐条对照书中原文人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 8 条，剔除非预测 0 条，计入 **8 条预测**，其中 **7 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 3 |
| 趋势符合 | 1 |
| 部分符合 | 3 |
| 错误 | 0 |
| 暂无法判断 | 1 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **42.9%**（3/7） |
| 加权胜率 | **75.0%** |
| 错误率 | **0.0%**（0/7） |
| 未定占比（暂无法判断/预测） | 12.5%（1/8） |

## 总体评价

本书主体是长期债务周期模板和 48 个历史案例复盘，明确指向 2018 年出版之后、当时尚未结算的可核验判断很少；全文重读后共得到 8 条预测（约 0.022 条/块）。正确 3 条：政策制定者最终总会印钞（2020 年各大央行大规模扩表）；美国下一次刺激将超越 QE 转向 MP3（2020 年零利率、大规模 QE 与 CARES 直接发钱）；国内民粹与大国对抗并存时冲突概率远高于常态（UCDP 记录 2024 年国家间/涉国家冲突创 1946 年以来新高，俄乌战争）。趋势符合 1 条：长期货币化促使资金转向黄金（金价大涨，但美元储备地位仍在）。部分符合 3 条：储备货币国印钞容忍通胀会侵蚀储备地位（美国确有高通胀和通胀式减债，但美元储备份额经汇率调整后大体稳定）；本币/外币债务危机不对称（成立，但本币国付出高通胀代价）；美国各部门债务/GDP 附图投影（政府债务确升但远超缓升路径）。暂无法判断 1 条：约 25 年后监管被规避、新杠杆引发新债务危机（已有 2018 年放松监管与 2023 年硅谷银行等迹象，终点未到）。f5 版本中的希腊“尚未进入美丽去杠杆”一句经重读判定为 2018 年当时状态描述，不是对出版后的预测，已不计入。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（3 条）

- **#1** 「In the end, policy makers always print.」  
  判断：**正确**。出版后的下一次重大衰退（2020年新冠冲击）中，各主要央行最终都选择了“印钱”：美联储在2020年3月后以前所未有的速度扩表，资产负债表于2020年7月超过7万亿美元；欧央行推出规模最终达1.85万亿欧元的疫情紧急购债计划（PEPP），BIS总结称发达经济体央行迅速大规模购债并与财政配合。“政策制定者最终总会印钞”在出版后的首个重大危机中得到验证。  
  来源：<https://www.federalreserve.gov/monetarypolicy/bsd-overview-202008.htm>；<https://www.reuters.com/article/us-usa-fed-assets/fed-kicks-off-main-street-lending-balance-sheet-tops-7-trillion-idUSKCN24H38P/>；<https://www.ecb.europa.eu/mopo/implement/pepp/html/index.en.html>；<https://www.bis.org/publications/bulletin-21-central-banks-response-covid-19-advanced-economies.pdf>
- **#3** 「and now in the US), which can lead to “pushing on a string.” When this happens, policy makers need to look bey…」  
  判断：**正确**。2020年3月美联储将联邦基金利率降至0–0.25%，并启动大规模资产购买；同时国会通过约2.2万亿美元的CARES法案，向符合条件的成年人直接发放最高1,200美元、儿童500美元的经济影响付款，后续两轮合计超过476百万笔、约8,140亿美元。这正是作者所说把钱更直接交到支出者手中、财政与货币协同的第三种货币政策。  
  来源：<https://home.treasury.gov/policy-issues/coronavirus/assistance-for-american-families-and-workers/economic-impact-payments>；<https://home.treasury.gov/policy-issues/coronavirus/about-the-cares-act>；<https://www.brookings.edu/articles/fed-response-to-covid19/>；<https://www.federalreserve.gov/newsevents/testimony/powell20200519a.htm>；<https://pandemicoversight.gov/data-interactive-tools/data-stories/update-three-rounds-stimulus-checks-see-how-many-went-out-and>
- **#5** 「the poor/proletariat/political left that lead to conflicts that result in populist, autocratic, nationalistic,…」  
  判断：**正确**。条件在出版后出现：多国民粹/民族主义政治力量上台，中美之间形成实力相近的大国经济与战略对抗。结果方面，乌普萨拉冲突数据项目（UCDP）记录2024年有61场涉及国家的武装冲突，为1946年有统计以来最多，其中11场达到战争级别，为2016年以来最多；PRIO称2025年有65场活跃冲突，为冷战后最暴力的年份之一；2022年俄罗斯全面入侵乌克兰，成为二战后欧洲最大规模的武装冲突。破坏性冲突概率“远高于常态”与事实一致。  
  来源：<https://www.uu.se/en/press/press-releases/2025/2025-06-11-ucdp-sharp-increase-in-conflicts-and-wars>；<https://www.prio.org/publications/14802>；<https://www.cfr.org/articles/the-invasion-that-shook-the-world>；<https://www.rusi.org/explore-our-research/publications/commentary/chinas-position-ukraine-war-mirrors-its-global-pursuits>

### 趋势符合（1 条）

- **#2** 「there is a real risk that prolonged monetization will lead people to question the currency’s suitability as a …」  
  判断：**趋势符合**。金价从2018年9月约1,190美元/盎司升至2025年年均约3,431美元，并在2026年1月盘中超过5,500美元，央行购金与官方黄金储备占比上升，资金确已转向黄金。但美联储2026年9月说明黄金并未真正取代国债成为全球首选储备资产，IMF称美元储备份额在汇率调整后仍大体稳定，美元储备地位未被动摇。方向成立，法币价值储藏功能被系统性抛弃这一端点尚未出现。  
  来源：<https://www.gold.org/goldhub/research/gold-demand-trends/gold-demand-trends-full-year-2025>；<https://www.gold.org/goldhub/research/gold-mid-year-outlook-2026>；<https://www.federalreserve.gov/econres/notes/feds-notes/why-gold-didnt-actually-overtake-treasury-securities-as-the-worlds-favorite-reserve-asset-accessible-20260903.htm>；<https://www.stlouisfed.org/open-vault/2026/feb/us-dollar-role-as-reserve-currency>；<https://www.imf.org/en/blogs/articles/2025/10/01/dollars-share-of-reserves-held-steady-in-second-quarter-when-adjusted-for-fx-moves>；<https://www.chartgoldprice.com/gold-price/september-2018>

### 部分符合（3 条）

- **#4** 「If a reserve-currency country permits much higher inflation in order to keep growth stronger by printing lots …」  
  判断：**部分符合**。条件部分成立：美国在2020–2021年大规模印钞并配合财政扩张，CPI同比在2022年6月升至9.1%，为1981年以来最高，通胀确实侵蚀了政府债务实际价值（圣路易斯联储估算2021年意外通胀使债务实际价值减少约GDP的3.3%），去杠杆带有通胀成分。但美元储备地位并未被明显侵蚀：美元在全球外汇储备中的份额由2015年的64%降至2025年的约56–57%，纽约联储与IMF均指出这一变化主要来自汇率估值和个别国家构成，经汇率调整后大体稳定；且美联储2022年起大幅加息，并未长期“容忍更高通胀”。结果只部分符合。  
  来源：<https://www.bls.gov/opub/ted/2022/consumer-prices-up-9-1-percent-over-the-year-ended-june-2022-largest-increase-in-40-years.htm>；<https://www.stlouisfed.org/on-the-economy/2022/mar/how-much-are-we-taxed-surprise-inflation>；<https://libertystreeteconomics.newyorkfed.org/2026/09/are-central-banks-moving-out-of-dollar-assets/>；<https://data.imf.org/en/news/imf-data-brief-december-19>；<https://www.imf.org/en/blogs/articles/2025/10/01/dollars-share-of-reserves-held-steady-in-second-quarter-when-adjusted-for-fx-moves>
- **#6** 「managing debt crises is all about spreading out the pain of the bad debts, and this can almost always be done …」  
  判断：**部分符合**。出版后出现的主权违约浪潮主要集中在外币或无法自主印钞的债务国（斯里兰卡、赞比亚、加纳、黎巴嫩等），本币储备货币国未出现主权债务违约，本币/外币不对称得到证实。但美国、英国等本币债务国在2021–2023年经历了显著通胀，说明“几乎总能管理好”低估了本币路径的通胀代价，不能整条记为正确。  
  来源：<https://www.reuters.com/world/countries-grip-debt-crises-2023-02-24/>；<https://www.reuters.com/markets/poor-nations-default-wave-peaks-cash-shortage-could-take-its-place-2024-10-21/>；<https://www.bankofcanada.ca/2024/07/staff-analytical-note-2024-19/>；<https://www.imf.org/-/media/files/publications/gfsr/2023/april/english/text.pdf>；<https://www.federalreserve.gov/newsevents/speech/files/brainard20220930a.pdf>
- **#8** 「charts show existing and projected debt-to-GDP ratios」  
  判断：**部分符合**。书中附图（第184页）显示政府债务/GDP从约100%继续缓升、非金融企业续升、家庭小幅回升、金融部门续降，终点约在2028年。FRED显示联邦债务/GDP在2026年第一季度为122.6%、第二季度为121.2%，方向与政府债务上升一致，但升幅远超附图约至110%的缓升路径，主要受2020年疫情冲击。各部门路径并不整齐一致，且投影终点尚未到达，故记为部分符合。  
  来源：<https://fred.stlouisfed.org/series/GFDEGDQ188S/>；<https://fred.stlouisfed.org/data/GFDEGDQ188S>；<https://fred.stlouisfed.org/series/QUSNAM770A>；<https://www.federalreserve.gov/releases/z1/dataviz/z1/nonfinancial_debt/table/>；<https://fred.stlouisfed.org/data/HDTGPDUSQ163N>

### 暂无法判断（1 条）

- **#7** 「over long time frames (e.g., 25 years), as the hangover wears off and a new euphoria sets in, these laws are i…」  
  判断：**暂无法判断**。本条说的是在约25年的长周期里，危机后的监管被日益规避、新主体产生新杠杆并最终引发新的债务危机，以2008年危机计终点约在2033年前后，尚未到来。出版后已有方向性迹象：2018年《经济增长、监管放松与消费者保护法》放松了Dodd-Frank的部分要求，美联储复盘认为这与2023年硅谷银行倒闭有关；IMF指出非银金融机构（私募信贷等）快速增长带来新的金融稳定风险。但“新的债务危机”尚未发生，按规则10不记趋势符合。  
  来源：<https://www.federalreserve.gov/newsevents/pressreleases/bcreg20230428a.htm>；<https://www.reuters.com/business/finance/us-fed-points-finger-trump-era-rollback-svb-demise-2023-04-29/>；<https://www.imf.org/en/blogs/articles/2025/10/14/growth-of-nonbanks-is-revealing-new-financial-stability-risks>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/dalio-big-debt-crises-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/dalio-big-debt-crises-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/dalio-big-debt-crises-v5/audit/manual_review_2026-11-15.py`
