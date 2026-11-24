# 世界银行《贫困、繁荣与地球报告2024：走出多重危机的路径》（Poverty, Prosperity, and Planet Report 2024: Pathways Out of the Polycrisis）：出版后预测人工核查

- 案例目录：`cases/world-bank-poverty-prosperity-planet-2024-v5/`
- 出版日期：世界银行 **2024 年 10 月**发布（PDF CreationDate 2024-10-04；正文数据为 PIP 2024 年 9 月版），按 2024-10 起算。正文用 `reading-library/2026-11-15-未来判断扩展100本/04-经济与资源/053-poverty-prosperity-and-planet-report-2024-pathways-out-of-the-polycrisis.pdf`（sha256 `0f22fde0…af746`，CC BY 3.0 IGO，DOI 10.1596/978-1-4648-2123-3），经 `pdftotext -enc UTF-8` 生成 TXT（sha256 `306554dd…9d4b`，805,294 字符；TXT 不入库）。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

本稿按 METHOD.md 复刻 DeepSeek 流水线，只把模型调用换成助手人工阅读。抽取：用仓库 prepare_book v5（toolkit 来自 main `85e6da1`）把全文切成 234 块（3500 字符、600 字符上下文），助手逐块通读，按 DISCOVER_PROMPT_V5 写出模型本应返回的 JSON（可为空），再由仓库代码完成引文对齐、非预测筛除、归属降级和去重，得到 83 条候选、82 条可核验（resolvable）。核验：每条可核验候选先定 scope，用 Exa 各做一次 support/counter 检索（6 条做了适应性补充检索），只从检索返回的 URL 中选源，存档到 `data/sources/`（sha256），写入 `data/evidence.jsonl`，再经 `pipeline.py apply assess → check → report`。2026-11-16 返工：为证据独立性另做一轮 Exa 检索（4 组 support/counter/extra 查询），新增 5 份第三方存档。本稿由助手逐条对照书中原文与存档证据人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 82 条，剔除非预测 0 条，计入 **82 条预测**，其中 **36 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 16 |
| 趋势符合 | 16 |
| 部分符合 | 4 |
| 错误 | 0 |
| 暂无法判断 | 46 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **44.4%**（16/36） |
| 加权胜率 | **83.3%** |
| 错误率 | **0.0%**（0/36） |
| 未定占比（暂无法判断/预测） | 56.1%（46/82） |

## 总体评价

这是一份出版仅两年的机构报告，大部分预测的终点在 2030 年或 2050 年，因此 82 条预测中有 46 条记为暂无法判断。可判定的 36 条里没有错误：报告对短期内可观察的事项判断较准，例如 2025 年 PIP 更新会采用 2021 年 PPP 和印度新数据、国际贫困线上调而印度估计下调、关键结论在新数据下仍然成立、极端贫困进一步集中于撒哈拉以南非洲和脆弱冲突国家、国家间不平等扩大而国内不平等下降、撒哈拉以南非洲 2025 年人均增长约 1.5%、三分之一低收入国家人均收入仍低于 2019 年。对“2020—2030 年是失去的十年”、2030 年无法消除极端贫困、气候灾害加剧等方向性判断，到 2026 年的证据方向一致，记为趋势符合。关于高收入和中高收入国家排放“下降”的判断在 2024—2025 年并未普遍出现（美国 2025 年排放上升、中国基本持平），只有“远不足以控制在 1.5°C”一半成立，记为部分符合。需要注意：核验证据大量来自世界银行自己后续的 PIP、GEP 和 2026 年报告，独立性有限。2026-11-16 返工时为 11 条关键判定补了第三方来源（联合国经社部 WESP 2026、联合国 SDG 报告 2025、Our World in Data、IMF），均与原判断一致、未改判；但联合国和 Our World in Data 的贫困数字本身仍引自世界银行 PIP，只有 IMF 和 WESP 的增长/趋同判断基于各自数据。高胜率主要反映报告对自身监测指标的短期判断较稳，而不是对远期结果的验证。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（16 条）

- **#23** 「extreme poverty will be concentrated increasingly in Sub-Saharan Africa and fragile and conflict-affected coun…」  
  判断：**正确**。世界银行2025年10月《贫困与不平等更新》称极端贫困日益集中于撒哈拉以南非洲和受冲突与脆弱影响地区，自2022年起多数极端贫困人口生活在脆弱与冲突国家；该地区占全球极端贫困人口的71%。“How has the profile…”博客称其份额从2013年的十分之四升至十分之七。第三方来源：联合国经社部《2026年世界经济形势与展望》执行摘要称贫困“日益集中于撒哈拉以南非洲和面临冲突与脆弱的国家”；联合国《2025年可持续发展目标报告》称到2025年超过四分之三的极端贫困人口生活在撒哈拉以南非洲或脆弱冲突国家（两者的贫困数据仍引自世界银行PIP）  
  来源：<https://thedocs.worldbank.org/en/doc/229ff18129687a785f08af7cfb28e5e1-0350012025/original/WBG-Poverty-and-Inequality-Update-Fall-2025.pdf>；<https://blogs.worldbank.org/en/opendata/how-has-the-profile-of-extreme-poverty-changed-over-the-last-dec>；<https://desapublications.un.org/sites/default/files/publications/2026-01/WESP%202026_Executive%20Summary_English.pdf>；<https://unstats.un.org/sdgs/report/2025/Goal-01>
- **#37** 「Estimates using these new sources of data are expected to be published in the Poverty and Inequality Platform …」  
  判断：**正确**。预测兑现：世界银行于2025年6月5日在贫困与不平等平台（PIP）发布更新，采用2021年PPP并纳入包括印度2022年调查在内的新数据，同时修订全球贫困线。第三方来源：联合国SDG报告2025与Our World in Data均记载世界银行于2025年6月采用2021年PPP修订全球贫困估计，并把国际贫困线从2.15美元上调到3美元（二者只是转述世界银行的发布）  
  来源：<https://blogs.worldbank.org/en/opendata/june-2025-global-poverty-update-from-the-world-bank--2021-ppps-a>；<https://unstats.un.org/sdgs/report/2025/Goal-01>；<https://ourworldindata.org/new-international-poverty-line-3-dollars-per-day>
- **#38** 「key conclusions of the report are robust, such as the increasing concentration of extreme poverty in Sub-Sahar…」  
  判断：**正确**。纳入印度新数据和2021年PPP后，报告的关键结论仍然成立：世界银行2025年10月更新称极端贫困日益集中于撒哈拉以南非洲和脆弱冲突地区；2026年报告称减贫停滞，按过去十年增速2030年极端贫困率将高于现在，2030年消除极端贫困无望  
  来源：<https://thedocs.worldbank.org/en/doc/229ff18129687a785f08af7cfb28e5e1-0350012025/original/WBG-Poverty-and-Inequality-Update-Fall-2025.pdf>；<https://www.worldbank.org/en/publication/poverty-prosperity-and-planet>
- **#39** 「Progress in poverty reduction is projected to remain slow, and the goal of eradicating poverty is far out of r…」  
  判断：**正确**。“减贫进展仍将缓慢”在窗口内兑现：PIP 2026年9月更新称全球极端贫困率预计仅从2024年的10.1%微降至2026年的9.8%；2026年报告称这一比例自2019年以来没有变化。第三方来源：联合国经社部WESP 2026称极端贫困人数2024年回到疫情前水平后，2025年仅“略有下降”；联合国SDG报告2025称2030年消除极端贫困“看来极不可能”，届时仍有8.9%人口处于极端贫困；Our World in Data（2025年11月）称按当前趋势减贫进展将停止（三者的贫困数据仍基于世界银行）  
  来源：<https://blogs.worldbank.org/en/opendata/september-2026-global-poverty-update-from-the-world-bank--one-in>；<https://www.worldbank.org/en/publication/poverty-prosperity-and-planet>；<https://desapublications.un.org/sites/default/files/publications/2026-01/WESP%202026_Executive%20Summary_English.pdf>；<https://unstats.un.org/sdgs/report/2025/Goal-01>；<https://ourworldindata.org/end-progress-extreme-poverty>
- **#44** 「One-third of low-income countries is projected to have lower per capita incomes in 2026 than in 2019」  
  判断：**正确**。GEP 2026年1月称，近乎所有发达经济体的人均收入已高于疫情前，但四分之一的发展中国家、超过三分之一的低收入经济体将比五年前更穷，与“三分之一低收入国家2026年人均收入低于2019年”一致  
  来源：<https://blogs.worldbank.org/en/voices/global-economic-resilience-masks-an-uneven-growth-outlook>
- **#52** 「The concentration of poverty in Sub-Saharan Africa and FCS is forecasted to intensify」  
  判断：**正确**。预测在窗口内兑现：世界银行称极端贫困日益集中于撒哈拉以南非洲和脆弱冲突地区，自2022年起多数穷人生活在脆弱与冲突国家；撒哈拉以南非洲占全球极端贫困人口的比例从2013年的十分之四升至十分之七。第三方来源：联合国经社部《2026年世界经济形势与展望》执行摘要称贫困“日益集中于撒哈拉以南非洲和面临冲突与脆弱的国家”；联合国《2025年可持续发展目标报告》称到2025年超过四分之三的极端贫困人口生活在撒哈拉以南非洲或脆弱冲突国家（两者的贫困数据仍引自世界银行PIP）  
  来源：<https://thedocs.worldbank.org/en/doc/229ff18129687a785f08af7cfb28e5e1-0350012025/original/WBG-Poverty-and-Inequality-Update-Fall-2025.pdf>；<https://blogs.worldbank.org/en/opendata/how-has-the-profile-of-extreme-poverty-changed-over-the-last-dec>；<https://desapublications.un.org/sites/default/files/publications/2026-01/WESP%202026_Executive%20Summary_English.pdf>；<https://unstats.un.org/sdgs/report/2025/Goal-01>
- **#53** 「Per capita income growth in Sub-Saharan Africa is expected to remain at a meager 1.5 percent in 2025」  
  判断：**正确**。圣路易斯联储ALFRED收录的世界银行WDI数据显示，撒哈拉以南非洲发展中国家不变价人均GDP从2024年的1587.53美元升至2025年的1613.54美元，约增长1.6%，与预测的1.5%基本一致；GEP 2026年6月称该地区人均增速2026年“保持在1.6%”  
  来源：<https://alfred.stlouisfed.org/series?seid=NYGDPPCAPKDSSA>；<https://thedocs.worldbank.org/en/doc/2b672b3b0415d6b66c45b66579db4ef5-0050012026/related/GEP-Jun-2026-Regional-Highlights-SSA.pdf>
- **#55** 「robustness checks suggest that key findings of the report would not be affected in a meaningful way」  
  判断：**正确**。使用印度新数据后，报告关键结论确实没有实质改变：PIP 2025年6月更新把南亚贫困率下调，但撒哈拉以南非洲上调；世界银行2025年10月更新称极端贫困日益集中于撒哈拉以南非洲和脆弱冲突地区  
  来源：<https://blogs.worldbank.org/en/opendata/june-2025-global-poverty-update-from-the-world-bank--2021-ppps-a>；<https://thedocs.worldbank.org/en/doc/229ff18129687a785f08af7cfb28e5e1-0350012025/original/WBG-Poverty-and-Inequality-Update-Fall-2025.pdf>
- **#56** 「If the India estimate is revised down also for the recent past, extreme poverty will be further concentrated i…」  
  判断：**正确**。前提成立（印度估计被下调：PIP 2025年6月更新把南亚2022年贫困率从9.7%下调到7.3%）；同表撒哈拉以南非洲贫困人口从4.48亿上调到5.588亿，占全球8.38亿的约三分之二，高于旧版的4.48/7.128亿，极端贫困更加集中于该地区  
  来源：<https://blogs.worldbank.org/en/opendata/june-2025-global-poverty-update-from-the-world-bank--2021-ppps-a>；<https://blogs.worldbank.org/en/opendata/how-has-the-profile-of-extreme-poverty-changed-over-the-last-dec>
- **#58** 「extreme poverty in India was already projected to fall below 3 percent by the end of this decade」  
  判断：**正确**。按原2.15美元（2017年PPP）口径，世界银行新数据显示印度2022—23年极端贫困率已降至2.3%，在本十年末之前已低于3%  
  来源：<https://indianexpress.com/article/business/world-bank-poverty-line-rate-falls-2022-23-10051890/>
- **#61** 「While the new data in India are expected to bring down India’s estimate of extreme poverty, it is possible tha…」  
  判断：**正确**。两项都兑现：国际贫困线从2.15美元上调到3.00美元，世界银行说明其中大部分变化来自各国国家贫困线的更新，而不只是价格变动；同时印度新数据使南亚2022年极端贫困率从9.7%下调到7.3%，印度在3美元线下为5.3%  
  来源：<https://blogs.worldbank.org/en/opendata/june-2025-global-poverty-update-from-the-world-bank--2021-ppps-a>；<https://indianexpress.com/article/business/world-bank-poverty-line-rate-falls-2022-23-10051890/>
- **#62** 「they are likely to be adopted once the World Bank’s researchers and the broader scholarly community have had a…」  
  判断：**正确**。改进已被采用：PIP 2025年6月更新采用了2021年PPP，纳入新的国家调查数据（含印度新消费方法），并据此修订全球贫困线。第三方来源：联合国SDG报告2025与Our World in Data均记载世界银行于2025年6月采用2021年PPP修订全球贫困估计，并把国际贫困线从2.15美元上调到3美元（二者只是转述世界银行的发布）  
  来源：<https://blogs.worldbank.org/en/opendata/june-2025-global-poverty-update-from-the-world-bank--2021-ppps-a>；<https://unstats.un.org/sdgs/report/2025/Goal-01>；<https://ourworldindata.org/new-international-poverty-line-3-dollars-per-day>
- **#63** 「Regardless of the driver, the World Bank’s extreme poverty line will remain anchored to how the poorest countr…」  
  判断：**正确**。世界银行2025年6月的说明称极端贫困标准“基于世界上最贫困国家如何定义贫困”，新国际贫困线取低收入国家国家贫困线的中位数，仍以最贫困国家为锚。第三方来源：Our World in Data说明新国际贫困线取低收入国家国家贫困线的中位数（转述世界银行方法）  
  来源：<https://www.worldbank.org/en/news/factsheet/2025/06/05/june-2025-update-to-global-poverty-lines>；<https://blogs.worldbank.org/en/opendata/june-2025-global-poverty-update-from-the-world-bank--2021-ppps-a>；<https://ourworldindata.org/new-international-poverty-line-3-dollars-per-day>
- **#65** 「In the most recent period, between-country inequality is expected to worsen (increase), which will dampen the …」  
  判断：**正确**。世界银行称2019—2025年低收入国家与发达经济体之间的人均收入差距扩大了约10%，脆弱冲突国家差距更大；2026年报告称繁荣差距自2013年以来每年仅缩小约1%，国家间不平等上升拖慢了共享繁荣。第三方来源：联合国经社部WESP 2026称全球增长疲弱伴随着“经济趋同放缓”，许多发展中经济体（包括最不发达国家）近年人均收入增长减弱；IMF博客（2025年6月）称最贫困和脆弱冲突国家“日益落后”，2022—2024年最贫困的32个低收入国家平均增长3.3%、脆弱冲突国家仅2.6%，威胁其人均收入向发达经济体趋同（IMF使用自身数据，与世界银行独立）  
  来源：<https://blogs.worldbank.org/en/developmenttalk/the-post-pandemic-recovery--stronger-than-expected--but-not-for->；<https://www.worldbank.org/en/publication/poverty-prosperity-and-planet>；<https://desapublications.un.org/sites/default/files/publications/2026-01/WESP%202026_Executive%20Summary_English.pdf>；<https://www.imf.org/en/blogs/articles/2025/06/26/poorest-countries-and-fragile-states-are-increasingly-falling-behind>
- **#66** 「Average within-country inequality, on the other hand, is expected to decrease」  
  判断：**正确**。世界银行博客（2025年1月）称在疫情前后都有数据的72个国家中，52个国家内部不平等下降、20个上升，国内不平等平均下降的趋势在疫情后仍在延续  
  来源：<https://blogs.worldbank.org/en/opendata/declining-trends-in-national-inequality>
- **#74** 「Going forward, as shown in chapter 1, extreme poverty will be concentrated increasingly in Sub-Saharan Africa …」  
  判断：**正确**。极端贫困日益集中于撒哈拉以南非洲及脆弱冲突国家已在窗口内被证实：世界银行称自2022年起多数极端贫困人口生活在脆弱与冲突国家，撒哈拉以南非洲占全球极端贫困人口的71%。第三方来源：联合国经社部《2026年世界经济形势与展望》执行摘要称贫困“日益集中于撒哈拉以南非洲和面临冲突与脆弱的国家”；联合国《2025年可持续发展目标报告》称到2025年超过四分之三的极端贫困人口生活在撒哈拉以南非洲或脆弱冲突国家（两者的贫困数据仍引自世界银行PIP）  
  来源：<https://thedocs.worldbank.org/en/doc/229ff18129687a785f08af7cfb28e5e1-0350012025/original/WBG-Poverty-and-Inequality-Update-Fall-2025.pdf>；<https://blogs.worldbank.org/en/opendata/how-has-the-profile-of-extreme-poverty-changed-over-the-last-dec>；<https://desapublications.un.org/sites/default/files/publications/2026-01/WESP%202026_Executive%20Summary_English.pdf>；<https://unstats.un.org/sdgs/report/2025/Goal-01>

### 趋势符合（16 条）

- **#1** 「Global poverty reduction has slowed to a near standstill, with 2020–30 set to be a lost decade.」  
  判断：**趋势符合**。2020—2030年的“失去的十年”终点尚未到来；但世界银行《贫困、繁荣与地球报告2026》称2026年仍有8.11亿人（约十分之一）每天生活费不足3美元，比例自2019年以来没有变化，减贫已停滞，方向与“失去的十年”一致。第三方来源：联合国经社部WESP 2026称极端贫困人数2024年回到疫情前水平后，2025年仅“略有下降”（贫困数据仍基于世界银行）  
  来源：<https://www.worldbank.org/en/publication/poverty-prosperity-and-planet>；<https://blogs.worldbank.org/en/opendata/september-2026-global-poverty-update-from-the-world-bank--one-in>；<https://desapublications.un.org/sites/default/files/publications/2026-01/WESP%202026_Executive%20Summary_English.pdf>
- **#4** 「Climate change will likely lead to more frequent and more intense extreme weather events, which will negativel…」  
  判断：**趋势符合**。世界气象组织《2025年全球气候状况》称2015—2025年是有记录以来最热的11年，并称“我们的天气已变得更加极端”，2025年热浪、野火、干旱、热带气旋和洪水造成数千人死亡；方向与预测一致，但两年窗口不足以确立频率趋势  
  来源：<https://wmo.int/news/media-centre/earths-climate-swings-increasingly-out-of-balance>；<https://news.un.org/en/story/2025/05/1163176>
- **#16** 「Shocks are expected to increase with more frequent and severe extreme weather events.」  
  判断：**趋势符合**。世界气象组织称2025年热浪、野火、干旱、热带气旋和洪水造成重大影响、天气“变得更加极端”；IDMC称2024年灾害导致的流离失所达4580万人次，几乎是过去十年年均的两倍。冲击增加的方向与预测一致，但窗口仅两年  
  来源：<https://wmo.int/news/media-centre/earths-climate-swings-increasingly-out-of-balance>；<https://news.un.org/en/story/2025/05/1163176>
- **#17** 「Without more rapid action, climate-related hazards will likely intensify.」  
  判断：**趋势符合**。前提“未更快行动”成立：EDGAR显示2024、2025年全球温室气体排放仍创新高；世界气象组织称2015—2025年为最热11年、天气更加极端。灾害加剧的方向与预测一致，终点未定  
  来源：<https://wmo.int/news/media-centre/earths-climate-swings-increasingly-out-of-balance>；<https://joint-research-centre.ec.europa.eu/jrc-news-and-updates/six-16-major-emitters-reduced-their-emissions-2025-2026-09-07_en>
- **#18** 「If GHG emissions are not reduced, climate risks will worsen.」  
  判断：**趋势符合**。前提“温室气体排放未减少”成立（EDGAR：2025年全球排放540亿吨CO2当量，再创新高）；世界气象组织称地球能量失衡在2025年创新高、天气更加极端，气候风险恶化的方向与预测一致  
  来源：<https://joint-research-centre.ec.europa.eu/jrc-news-and-updates/six-16-major-emitters-reduced-their-emissions-2025-2026-09-07_en>；<https://wmo.int/news/media-centre/earths-climate-swings-increasingly-out-of-balance>
- **#21** 「Even if currently pledged Nationally Determined Contributions (NDCs)18 were to be enacted, emissions would not…」  
  判断：**趋势符合**。UNEP《2025年排放差距报告》称全面落实国家自主贡献，本世纪升温仍将达2.3—2.5°C，并且“很可能”在本十年突破1.5°C；全球碳预算称1.5°C已不再可行。方向与预测一致，但这是更新后的评估而非最终结果  
  来源：<https://www.carbonbrief.org/unep-new-country-climate-plans-barely-move-needle-on-expected-warming>；<https://globalcarbonbudget.org/fossil-fuel-co2-emissions-hit-record-high-in-2025/>
- **#26** 「By 2030, one-half of the global extreme poor will be in today’s FCS within Sub-Saharan Africa, and an addition…」  
  判断：**趋势符合**。2030年终点未到；但世界银行2025年更新的预测继续指向同一格局：到2030年撒哈拉以南非洲的脆弱国家将容纳全球近一半极端贫困人口（3.67亿），全地区接近80%；2024年该地区已占70%  
  来源：<https://blogs.worldbank.org/en/dev4peace/when-poverty-meets-fragility--why-the-next-decade-of-global-pove>；<https://thedocs.worldbank.org/en/doc/229ff18129687a785f08af7cfb28e5e1-0350012025/original/WBG-Poverty-and-Inequality-Update-Fall-2025.pdf>
- **#27** 「The share of poor in FCS and Sub-Saharan Africa will have grown from one-quarter to more than four-fifths.」  
  判断：**趋势符合**。2030年终点未到；世界银行《贫困、繁荣与地球报告2026》称到2030年87%的极端贫困人口将在撒哈拉以南非洲、脆弱与冲突国家或两者兼有，且自2022年起多数穷人已在脆弱与冲突国家，集中度持续上升  
  来源：<https://www.worldbank.org/en/publication/poverty-prosperity-and-planet>；<https://thedocs.worldbank.org/en/doc/229ff18129687a785f08af7cfb28e5e1-0350012025/original/WBG-Poverty-and-Inequality-Update-Fall-2025.pdf>
- **#36** 「Global poverty reduction has slowed to a near standstill, with 2020–30 set to mark a lost decade」  
  判断：**趋势符合**。2020—2030年的“失去的十年”终点尚未到来；但世界银行《贫困、繁荣与地球报告2026》称2026年仍有8.11亿人（约十分之一）每天生活费不足3美元，比例自2019年以来没有变化，减贫已停滞，方向与“失去的十年”一致。第三方来源：联合国经社部WESP 2026称极端贫困人数2024年回到疫情前水平后，2025年仅“略有下降”（贫困数据仍基于世界银行）  
  来源：<https://www.worldbank.org/en/publication/poverty-prosperity-and-planet>；<https://blogs.worldbank.org/en/opendata/september-2026-global-poverty-update-from-the-world-bank--one-in>；<https://desapublications.un.org/sites/default/files/publications/2026-01/WESP%202026_Executive%20Summary_English.pdf>
- **#49** 「Extreme poverty in the Middle East and North Africa is projected to continue to rise to 2030」  
  判断：**趋势符合**。PIP 2025年6月更新称2022—2025年中东和北非是唯一贫困上升的地区（8.5%升至9.4%）；2026年9月更新称中东、北非、阿富汗和巴基斯坦地区极端贫困仍在上升。方向一致，但2030年终点未到，地区口径已调整  
  来源：<https://blogs.worldbank.org/en/opendata/june-2025-global-poverty-update-from-the-world-bank--2021-ppps-a>；<https://blogs.worldbank.org/en/opendata/september-2026-global-poverty-update-from-the-world-bank--one-in>
- **#57** 「Another conclusion of this report is that extreme poverty eradication will take longer than the original targe…」  
  判断：**趋势符合**。2030年期限尚未到；世界银行2026年报告称2026年仍有8.11亿极端贫困人口，比例自2019年以来没有变化，并预测按过去十年增速2030年人数将高于现在，消除极端贫困将晚于2030年的方向非常明确。第三方来源：联合国SDG报告2025称2030年消除极端贫困“看来极不可能”；Our World in Data（2025年11月）据世界银行与IMF增长预测称2030年后极端贫困人数预计回升，世界“显然不在”实现该目标的轨道上（数据仍基于世界银行）  
  来源：<https://www.worldbank.org/en/publication/poverty-prosperity-and-planet>；<https://unstats.un.org/sdgs/report/2025/Goal-01>；<https://ourworldindata.org/end-progress-extreme-poverty>
- **#59** 「India’s contribution to global extreme poverty is projected to decline significantly over the next decade」  
  判断：**趋势符合**。印度占全球极端贫困比例下降的方向已出现：PIP 2025年6月更新称南亚是2022—2025年极端贫困降幅最大的地区；2026年9月更新称纳入南亚最新调查后，南亚极端贫困率下降带动全球估计下调。“未来十年显著下降”的终点未到  
  来源：<https://blogs.worldbank.org/en/opendata/june-2025-global-poverty-update-from-the-world-bank--2021-ppps-a>；<https://blogs.worldbank.org/en/opendata/september-2026-global-poverty-update-from-the-world-bank--one-in>；<https://indianexpress.com/article/business/world-bank-poverty-line-rate-falls-2022-23-10051890/>
- **#67** 「Building resilience is also key for reducing inequality, so households do not slide back as the result of shoc…」  
  判断：**趋势符合**。世界气象组织称2025年天气“变得更加极端”，极端事件造成广泛破坏；IDMC称2024年灾害引发的流离失所几乎是过去十年年均的两倍，并指出天气灾害的频率、强度和持续时间在持续恶化。方向与预测一致，但窗口较短  
  来源：<https://wmo.int/news/media-centre/earths-climate-swings-increasingly-out-of-balance>；<https://news.un.org/en/story/2025/05/1163176>
- **#70** 「Without faster action, climate-related hazards will likely intensify」  
  判断：**趋势符合**。前提“未加快行动”成立（EDGAR：2025年全球排放再创新高）；世界气象组织称2015—2025年为最热11年、天气更加极端，灾害加剧的方向一致，终点未定  
  来源：<https://wmo.int/news/media-centre/earths-climate-swings-increasingly-out-of-balance>；<https://joint-research-centre.ec.europa.eu/jrc-news-and-updates/six-16-major-emitters-reduced-their-emissions-2025-2026-09-07_en>
- **#79** 「Climate change will exacerbate the frequency and severity of hazardous events, increasing climate risks to peo…」  
  判断：**趋势符合**。世界气象组织《2025年全球气候状况》称天气已变得更加极端，2025年各类极端事件造成重大人员和经济损失；IDMC称天气灾害的频率、强度和持续时间在持续恶化，方向与预测一致  
  来源：<https://wmo.int/news/media-centre/earths-climate-swings-increasingly-out-of-balance>；<https://news.un.org/en/story/2025/05/1163176>
- **#80** 「Without radical change, problems of too much, too little, or too polluted water will only increase.」  
  判断：**趋势符合**。联合国粮农组织2025年12月称，过去十年人均可再生水资源又下降7%，北非等地取水增加16%，淡水资源压力在加大，方向与“水问题只会加剧”一致  
  来源：<https://www.fao.org/newsroom/detail/renewable-water-availability-per-person-plunges-7-percent-in-a-decade-as-global-scarcity-deepens--fao-data-shows/>

### 部分符合（4 条）

- **#7** 「Although emissions in those settings are projected to decline under current policies, the current progress is …」  
  判断：**部分符合**。后半句“下降速度远不足以限制全球变暖”成立：EDGAR称2024、2025年全球温室气体排放连创新高，全球碳预算称1.5°C已不再可行；但前半句“中高收入和高收入国家排放下降”在窗口内未普遍出现——2024年欧盟、日本下降，中国、美国基本持平或微增，2025年美国增加2.2%、中国+0.1%  
  来源：<https://joint-research-centre.ec.europa.eu/jrc-news-and-updates/world-emissions-hit-record-high-eu-leads-trend-reversal-2025-09-09_en>；<https://joint-research-centre.ec.europa.eu/jrc-news-and-updates/six-16-major-emitters-reduced-their-emissions-2025-2026-09-07_en>；<https://globalcarbonbudget.org/fossil-fuel-co2-emissions-hit-record-high-in-2025/>
- **#24** 「Under current policies, GHG emissions from high-income and upper-middle-income countries are projected to decl…」  
  判断：**部分符合**。后半句“远不足以把升温控制在1.5°C左右”成立（UNEP：全球排放2024年增加2.3%；全球碳预算：1.5°C已不再可行）；前半句高收入和中高收入国家排放下降在窗口内并未普遍出现：2025年美国排放增加2.2%、中国+0.1%，只有欧盟、日本等下降  
  来源：<https://www.carbonbrief.org/unep-new-country-climate-plans-barely-move-needle-on-expected-warming>；<https://joint-research-centre.ec.europa.eu/jrc-news-and-updates/six-16-major-emitters-reduced-their-emissions-2025-2026-09-07_en>；<https://globalcarbonbudget.org/fossil-fuel-co2-emissions-hit-record-high-in-2025/>
- **#29** 「Per capita income growth is expected to remain at a meager 1.5 percent in Sub-Saharan Africa and 2.3 percent i…」  
  判断：**部分符合**。撒哈拉以南非洲部分基本兑现：据圣路易斯联储ALFRED收录的世界银行WDI数据，该地区发展中国家不变价人均GDP从2024年的1587.53美元升至2025年的1613.54美元，增长约1.6%；GEP 2026年6月称该地区人均增速2026年“保持在1.6%”。但IDA国家2.3%这一部分没有找到实际数据  
  来源：<https://alfred.stlouisfed.org/series?seid=NYGDPPCAPKDSSA>；<https://thedocs.worldbank.org/en/doc/2b672b3b0415d6b66c45b66579db4ef5-0050012026/related/GEP-Jun-2026-Regional-Highlights-SSA.pdf>
- **#75** 「GHG emissions from high- and upper-middle-income countries emissions are projected to decline under current po…」  
  判断：**部分符合**。“远不足以把升温限制在1.5°C左右”成立（全球碳预算：1.5°C已不再可行；EDGAR：2025年全球排放再创新高）；但“高收入和中高收入国家排放下降”在2024—2025年并未普遍出现，美国2025年排放增加2.2%，中国基本持平  
  来源：<https://joint-research-centre.ec.europa.eu/jrc-news-and-updates/six-16-major-emitters-reduced-their-emissions-2025-2026-09-07_en>；<https://globalcarbonbudget.org/fossil-fuel-co2-emissions-hit-record-high-in-2025/>；<https://joint-research-centre.ec.europa.eu/jrc-news-and-updates/world-emissions-hit-record-high-eu-leads-trend-reversal-2025-09-09_en>

### 暂无法判断（46 条）

- **#2** 「At the current pace of progress, it would take decades to eradicate extreme poverty」  
  判断：**暂无法判断**。“按目前速度需要几十年才能消除极端贫困”涉及几十年后的结果，截至2026-11-15无法检验；世界银行2026年报告只说明减贫停滞，不能据此判定所需年限  
  来源：<https://www.worldbank.org/en/publication/poverty-prosperity-and-planet>
- **#3** 「more than a century to lift people above $6.85 per day」  
  判断：**暂无法判断**。“让所有人超过每天6.85美元需要一个多世纪”是百年尺度推算，且2025年6月起该贫困线已改为2021年PPP下的8.30美元，截至核验日无法检验  
  来源：<https://blogs.worldbank.org/en/opendata/june-2025-global-poverty-update-from-the-world-bank--2021-ppps-a>
- **#5** 「Economic growth in the poorest countries is projected to remain weaker than in the decade before the pandemic.」  
  判断：**暂无法判断**。缺少“最贫困国家”整体增速与疫情前十年平均的直接对比数据；GEP 2026年1月只说明低收入国家2025年增长5%、人均增速不足以弥补疫情损失，不构成对该比较的决定性证据  
  来源：<https://thedocs.worldbank.org/en/doc/7ce50b5aa95bef66048680bba9926ec8-0050012026/related/GEP-Jan-2026-Box-1-3.pdf>
- **#6** 「Without action, their emissions will increase over the next decades and surpass those of upper-middle-income c…」  
  判断：**暂无法判断**。“未来几十年排放增加并超过中高收入和高收入国家”的终点在数十年后；EDGAR显示2024年印度排放增加3.9%，但2025年印度排放基本持平（-0.2%），窗口内趋势不稳定，无法判断  
  来源：<https://joint-research-centre.ec.europa.eu/jrc-news-and-updates/world-emissions-hit-record-high-eu-leads-trend-reversal-2025-09-09_en>；<https://joint-research-centre.ec.europa.eu/jrc-news-and-updates/six-16-major-emitters-reduced-their-emissions-2025-2026-09-07_en>
- **#8** 「by the end of this decade, a projected 7.3 percent of the world population will be living in extreme poverty」  
  判断：**暂无法判断**。2030年7.3%（2.15美元、2017年PPP口径）的终点未到；且2025年6月起国际贫困线改为3.00美元（2021年PPP），口径已变，截至核验日无法判断  
  来源：<https://blogs.worldbank.org/en/opendata/june-2025-global-poverty-update-from-the-world-bank--2021-ppps-a>；<https://www.worldbank.org/en/publication/poverty-prosperity-and-planet>
- **#9** 「between now and 2030, only 69 million people are projected to escape extreme poverty」  
  判断：**暂无法判断**。“2030年前只有6900万人脱贫”的终点未到，截至核验日无法检验；PIP数据只到2024年并有2025—2026年临近预测  
  来源：<https://blogs.worldbank.org/en/opendata/september-2026-global-poverty-update-from-the-world-bank--one-in>
- **#10** 「slightly less than 40 percent of the global population being projected to live on less than $6.85 per person p…」  
  判断：**暂无法判断**。2030年约40%人口低于6.85美元的终点未到，且该贫困线已改为8.30美元（2021年PPP），无法判断  
  来源：<https://blogs.worldbank.org/en/opendata/june-2025-global-poverty-update-from-the-world-bank--2021-ppps-a>
- **#11** 「If economic growth continues to be slow and inequality remains unchanged, the 3 percent goal will remain out o…」  
  判断：**暂无法判断**。“3%目标几十年内无法实现”的检验期在几十年后；现有证据只说明到2026年减贫停滞，不能判定“几十年”  
  来源：<https://www.worldbank.org/en/publication/poverty-prosperity-and-planet>
- **#12** 「If gross domestic product (GDP) per capita growth stays at the average rates observed during 2010–19, extreme …」  
  判断：**暂无法判断**。“到2050年极端贫困率都高于7%”终点为2050年，截至核验日无法检验  
  来源：<https://thedocs.worldbank.org/en/doc/229ff18129687a785f08af7cfb28e5e1-0350012025/original/WBG-Poverty-and-Inequality-Update-Fall-2025.pdf>
- **#13** 「students in low-income and lowermiddle-income countries could face future earning losses of up to 10 percent b…」  
  判断：**暂无法判断**。学生未来收入损失最多10%需要等这一代人进入劳动力市场后才能观察，截至核验日没有决定性证据  
  来源：—
- **#14** 「The loss in schooling is likely to have a larger effect on poverty in the future than the immediate effect of …」  
  判断：**暂无法判断**。学业损失对未来贫困的影响是否大于疫情即时影响，属于远期结果，截至核验日无法检验  
  来源：—
- **#15** 「GDP growth in IDA countries is forecast to strengthen in 2024–25 but remain weaker than in the decade before t…」  
  判断：**暂无法判断**。未找到IDA国家整体2024—25年实际增速及其与疫情前十年平均的对比；GEP 2026年1月显示低收入国家增速由2024年3.6%升至2025年5%，但IDA口径的决定性数据缺失  
  来源：<https://thedocs.worldbank.org/en/doc/7ce50b5aa95bef66048680bba9926ec8-0050012026/related/GEP-Jan-2026-Box-1-3.pdf>
- **#19** 「At present, the expected increase is 3 percent, showing that transformations have already occurred over the pa…」  
  判断：**暂无法判断**。“到2030年排放只增加3%”的终点未到；窗口内全球排放2024年增加2.3%（UNEP）、2025年增加0.7%（EDGAR），只是中间过程，无法判定2030年结果  
  来源：<https://www.carbonbrief.org/unep-new-country-climate-plans-barely-move-needle-on-expected-warming>；<https://joint-research-centre.ec.europa.eu/jrc-news-and-updates/six-16-major-emitters-reduced-their-emissions-2025-2026-09-07_en>
- **#20** 「with current policies, temperatures are projected to increase close to 2°C」  
  判断：**暂无法判断**。“到2050年升温接近2°C”终点在2050年；气候行动追踪组织和UNEP的最新评估针对本世纪末升温，口径不同，截至核验日无法判断  
  来源：<https://climateactiontracker.org/press/release-global-update-2025/>
- **#22** 「While CBAM is not likely to have a large effect on countries’ GDP or trade balances, it may negatively affect …」  
  判断：**暂无法判断**。欧盟CBAM于2026年1月才进入正式征费阶段，截至核验日没有找到其对各国GDP或贸易差额实际影响的事后评估，无法判断  
  来源：<https://blogs.worldbank.org/en/trade/how-developing-countries-can-measure-exposure-eus-carbon-border-adjustment-mechanism>；<https://www.iisd.org/articles/explainer/eu-carbon-border-adjustment-mechanism-bigger-trade-implications>
- **#25** 「lower-middle-income countries do not contribute much to emissions today, but without action, they will have a …」  
  判断：**暂无法判断**。“几十年后中低收入国家在总排放中占重要地位”终点在数十年后，截至核验日无法检验  
  来源：<https://joint-research-centre.ec.europa.eu/jrc-news-and-updates/world-emissions-hit-record-high-eu-leads-trend-reversal-2025-09-09_en>
- **#28** 「Current IDA countries will comprise 82 percent of the global poor in 2030 with the currently projected growth …」  
  判断：**暂无法判断**。“现有IDA国家占2030年全球贫困人口82%、2050年90%”终点未到，且没有找到按IDA口径更新的份额，无法判断  
  来源：<https://www.worldbank.org/en/publication/poverty-prosperity-and-planet>
- **#30** 「Accelerating economic growth in these settings will not lead to significantly higher GHG emissions.」  
  判断：**暂无法判断**。加快低收入国家增长对排放的影响属于情景推算，截至核验日没有可观察的决定性事实  
  来源：<https://www.worldbank.org/en/publication/poverty-prosperity-and-planet>
- **#31** 「their emissions will increase over the next decades under current policies and surpass those of highincome cou…」  
  判断：**暂无法判断**。中低收入国家排放“到2030年超过高收入国家、2040年代超过中高收入国家”的终点未到；窗口内印度排放2024年增加3.9%、2025年-0.2%，无法判断  
  来源：<https://joint-research-centre.ec.europa.eu/jrc-news-and-updates/world-emissions-hit-record-high-eu-leads-trend-reversal-2025-09-09_en>；<https://joint-research-centre.ec.europa.eu/jrc-news-and-updates/six-16-major-emitters-reduced-their-emissions-2025-2026-09-07_en>
- **#32** 「Climate adaptation costs alone for developing countries are expected to be between $160 billion and $340 billi…」  
  判断：**暂无法判断**。“到2030年发展中国家适应成本每年1600亿至3400亿美元”是对2030年的估算，截至核验日无法检验；新的估算口径（2035年）不同，不能用来判对错  
  来源：—
- **#33** 「Based on the current trajectory, 7.3 percent of the global population is projected to live in extreme poverty …」  
  判断：**暂无法判断**。2030年7.3%的终点未到，且国际贫困线口径已改为3.00美元（2021年PPP），无法判断  
  来源：<https://blogs.worldbank.org/en/opendata/june-2025-global-poverty-update-from-the-world-bank--2021-ppps-a>
- **#34** 「nearly 40 percent of the world’s population will likely live on less than $6.85 per day」  
  判断：**暂无法判断**。2030年近40%人口低于6.85美元的终点未到，且该贫困线口径已改，无法判断  
  来源：<https://blogs.worldbank.org/en/opendata/june-2025-global-poverty-update-from-the-world-bank--2021-ppps-a>
- **#35** 「If growth does not accelerate and become more inclusive, it will take decades to eradicate extreme poverty and…」  
  判断：**暂无法判断**。“需要几十年”和“需要一个多世纪”都是长期推算，截至核验日无法检验  
  来源：<https://www.worldbank.org/en/publication/poverty-prosperity-and-planet>
- **#40** 「Poverty rates are projected to continue to decline only gradually until 2030.」  
  判断：**暂无法判断**。2030年终点未到；窗口内2024—2026年极端贫困率临近预测只从10.1%微降至9.8%，而世界银行2026年报告预测按过去十年增速，2030年极端贫困率将高于现在，与“逐步下降”方向相悖。证据相互冲突，暂无法判断  
  来源：<https://blogs.worldbank.org/en/opendata/september-2026-global-poverty-update-from-the-world-bank--one-in>；<https://www.worldbank.org/en/publication/poverty-prosperity-and-planet>
- **#41** 「At this rate, 7.3 percent of the global population will remain in extreme poverty in 2030, more than double th…」  
  判断：**暂无法判断**。2030年7.3%的终点未到，且贫困线口径已改，无法判断  
  来源：<https://blogs.worldbank.org/en/opendata/june-2025-global-poverty-update-from-the-world-bank--2021-ppps-a>
- **#42** 「less than 20 percent will have less than $3.65 per day」  
  判断：**暂无法判断**。2030年低于3.65美元的人口比例不到20%，终点未到，且该贫困线已改为4.20美元，无法判断  
  来源：<https://blogs.worldbank.org/en/opendata/june-2025-global-poverty-update-from-the-world-bank--2021-ppps-a>
- **#43** 「In 2023, GDP per capita grew only by 1 percent in low-income countries, and it is expected to rise to only 2.5…」  
  判断：**暂无法判断**。GEP 2026年1月称低收入国家2025年GDP增长5%，但没有给出2025年人均增速的确切数值；缺少决定性数据，无法核对“只升至2.5%”  
  来源：<https://thedocs.worldbank.org/en/doc/7ce50b5aa95bef66048680bba9926ec8-0050012026/related/GEP-Jan-2026-Box-1-3.pdf>
- **#45** 「extreme poverty will not change much between 2030 and 2050」  
  判断：**暂无法判断**。“2030—2050年间极端贫困变化不大”的检验期在未来，无法判断  
  来源：<https://thedocs.worldbank.org/en/doc/229ff18129687a785f08af7cfb28e5e1-0350012025/original/WBG-Poverty-and-Inequality-Update-Fall-2025.pdf>
- **#46** 「According to the current forecast, 26 percent of the global population would remain below the upper poverty li…」  
  判断：**暂无法判断**。2050年26%低于6.85美元的终点在2050年，无法判断  
  来源：—
- **#47** 「While poverty is projected to fall in Sub-Saharan Africa, progress will not be nearly fast enough to eradicate…」  
  判断：**暂无法判断**。2030年终点未到；PIP显示撒哈拉以南非洲极端贫困率2024年为46.0%（2025年9月版），2026年9月更新称该地区“仍然很高”，窗口内是否下降缺乏决定性证据  
  来源：<https://blogs.worldbank.org/en/opendata/september-2025-global-poverty-update-from-the-world-bank--new-da>；<https://blogs.worldbank.org/en/opendata/september-2026-global-poverty-update-from-the-world-bank--one-in>
- **#48** 「About one in three people in Sub-Saharan Africa in 2030 is projected to still be living with less than $2.15」  
  判断：**暂无法判断**。2030年撒哈拉以南非洲约三分之一人口低于2.15美元的终点未到，且国际贫困线口径已改，无法判断  
  来源：<https://blogs.worldbank.org/en/opendata/september-2025-global-poverty-update-from-the-world-bank--new-da>
- **#50** 「In South Asia, poverty rates will continue to fall faster, widening the gap with Sub-Saharan Africa, but 64 pe…」  
  判断：**暂无法判断**。PIP 2025年6月更新称2022—2025年南亚极端贫困降幅最大，GEP 2026年1月称南亚人均收入追赶进展较大、撒哈拉以南非洲有限；但这些是3美元线和人均收入口径，且2022—2025年数据大部分在出版前或为临近预测，6.85美元线下“差距扩大”和2030年64%缺少决定性证据  
  来源：<https://blogs.worldbank.org/en/opendata/june-2025-global-poverty-update-from-the-world-bank--2021-ppps-a>；<https://thedocs.worldbank.org/en/doc/7ce50b5aa95bef66048680bba9926ec8-0050012026/related/GEP-Jan-2026-Box-1-2.pdf>
- **#51** 「East Asia and Pacific as well as Europe and Central Asia will continue to make progress, while in Latin Americ…」  
  判断：**暂无法判断**。对东亚太平洋、欧洲中亚、拉美和中东北非四个地区2030年前减贫幅度的预测，截至核验日没有按原口径的完整对比数据，而中东北非贫困反而上升，暂无法判断  
  来源：<https://blogs.worldbank.org/en/opendata/september-2026-global-poverty-update-from-the-world-bank--one-in>
- **#54** 「in 2030 almost 1 in 10 people in the region is projected to live in extreme poverty」  
  判断：**暂无法判断**。2030年中东北非近十分之一人口处于极端贫困，终点未到，地区口径（已并入阿富汗、巴基斯坦）和贫困线都已调整，无法判断  
  来源：<https://blogs.worldbank.org/en/opendata/september-2025-global-poverty-update-from-the-world-bank--new-da>
- **#60** 「This suggests that the impacts of the India revision on global poverty measured at this line will be smaller.」  
  判断：**暂无法判断**。没有找到量化“印度数据修订对6.85美元线全球贫困影响较小”的公开结果；2025年6月起该线已改为8.30美元，无法判断  
  来源：—
- **#64** 「At current growth rates, a typical upper-middle-income country will need 100 years to close the Prosperity Gap…」  
  判断：**暂无法判断**。“典型中高收入国家需要100年才能消除繁荣差距”是百年尺度推算，无法检验  
  来源：<https://www.worldbank.org/en/publication/poverty-prosperity-and-planet>
- **#68** 「Poorer countries and people will suffer stronger negative consequences from climate-related hazards, leading t…」  
  判断：**暂无法判断**。“较贫穷国家和人群承受更强的气候灾害后果、导致贫困增加”需要分国家的灾害福利损失对比，截至核验日没有找到决定性事后证据  
  来源：—
- **#69** 「These exposure numbers are expected to increase as climate change is increasing the frequency and intensity of…」  
  判断：**暂无法判断**。世界银行2026年报告称暴露于主要气候灾害的人数在2010—2024年增加约5.5亿，但这段数据基本在出版前；出版后暴露人数的变化没有单独数据，按严格口径暂无法判断  
  来源：<https://www.worldbank.org/en/publication/poverty-prosperity-and-planet>
- **#71** 「However, figure 3.8 shows that with current policies, temperatures are projected to increase close to 2°C.」  
  判断：**暂无法判断**。2050年升温接近2°C的终点在2050年；最新评估针对本世纪末（现行政策2.6—2.8°C），口径不同，无法判断  
  来源：<https://climateactiontracker.org/press/release-global-update-2025/>；<https://www.carbonbrief.org/unep-new-country-climate-plans-barely-move-needle-on-expected-warming>
- **#72** 「Reductions in coal production are likely to not have substantial impacts on national employment and output in …」  
  判断：**暂无法判断**。削减煤炭生产对全国就业和产出的影响属于情景判断，截至核验日没有找到针对报告所述经济体的决定性事后证据  
  来源：—
- **#73** 「While CBAM is not likely to have a large impact on countries’ GDP or trade balances, it may negatively impact …」  
  判断：**暂无法判断**。CBAM于2026年1月才开始正式征费，截至核验日没有对各国GDP或贸易收支实际影响的事后评估，无法判断  
  来源：<https://blogs.worldbank.org/en/trade/how-developing-countries-can-measure-exposure-eus-carbon-border-adjustment-mechanism>；<https://www.iisd.org/articles/explainer/eu-carbon-border-adjustment-mechanism-bigger-trade-implications>
- **#76** 「lower-middle-income countries do not contribute much to emissions today but without action, they will have a s…」  
  判断：**暂无法判断**。“几十年后在全球总排放中占重要地位”的终点在数十年后，无法判断  
  来源：<https://joint-research-centre.ec.europa.eu/jrc-news-and-updates/world-emissions-hit-record-high-eu-leads-trend-reversal-2025-09-09_en>
- **#77** 「Lowincome countries barely contribute to emissions, and emissions are not expected to grow significantly under…」  
  判断：**暂无法判断**。没有找到低收入国家整体排放在2024—2026年变化的公开统计，无法判断  
  来源：—
- **#78** 「with current policies their emissions will increase over the next decades (figure 3.13, panel c) and will surp…」  
  判断：**暂无法判断**。“到2030年超过高收入国家、2040年代超过中高收入国家”的终点未到；印度排放2024年增加3.9%、2025年-0.2%，趋势不稳定，无法判断  
  来源：<https://joint-research-centre.ec.europa.eu/jrc-news-and-updates/world-emissions-hit-record-high-eu-leads-trend-reversal-2025-09-09_en>；<https://joint-research-centre.ec.europa.eu/jrc-news-and-updates/six-16-major-emitters-reduced-their-emissions-2025-2026-09-07_en>
- **#81** 「slow-onset changes such as sea level rise, desertification, and water scarcity are making some regions less ha…」  
  判断：**暂无法判断**。IDMC记录的2024年灾害流离失所主要由气旋、洪水等突发灾害引起；海平面上升、荒漠化等缓发变化导致的迁移缺乏可比统计，无法判断  
  来源：<https://news.un.org/en/story/2025/05/1163176>
- **#82** 「If historical growth performances continue in the coming decades, then extreme poverty is unlikely to fall dra…」  
  判断：**暂无法判断**。“未来几十年极端贫困不会大幅下降”的检验期在几十年后；2026年报告只说明减贫停滞，无法判定几十年后的结果  
  来源：<https://www.worldbank.org/en/publication/poverty-prosperity-and-planet>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/world-bank-poverty-prosperity-planet-2024-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/world-bank-poverty-prosperity-planet-2024-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/world-bank-poverty-prosperity-planet-2024-v5/audit/manual_review_2026-11-15.py`

## 说明

- 报告出版后（2025 年 6 月）国际贫困线由 2.15 美元（2017 年 PPP）改为 3.00 美元（2021 年 PPP），6.85 美元线改为 8.30 美元。凡以旧贫困线给出 2030/2050 年具体数值的预测，口径已变且终点未到，一律记暂无法判断；只有第 58 条（印度按 2.15 美元线本十年末前降到 3% 以下）有世界银行按旧线公布的结果（2022—23 年 2.3%），记为正确。
- 第 50、69 条的支持数据大部分在出版前或为临近预测，按严格口径记暂无法判断。
- 第 7、24、75 条（高收入和中高收入国家排放在现行政策下下降，但远不足以控制在 1.5°C）只有后半句在窗口内成立，记部分符合。
- 第 17、18、70 条为“若不加快行动/若排放不减少”的条件句，前提在窗口内成立（2024、2025 年全球排放连创新高），方向一致，记趋势符合。
- 多处重复出现的同一判断（如“失去的十年”、极端贫困向撒哈拉以南非洲集中、排放路径）是报告不同章节的不同句子，流水线未判为重叠重复，按候选分别计入。
- 第三方独立来源（2026-11-16 返工补充）：第 23、52、74 条（极端贫困向撒哈拉以南非洲和脆弱冲突国家集中）补联合国经社部 WESP 2026 执行摘要和联合国 SDG 报告 2025；第 1、36、39、57 条（减贫停滞、2030 年无法消除极端贫困）补 WESP 2026、SDG 报告 2025、Our World in Data《The end of progress against extreme poverty?》；第 65 条（国家间不平等扩大）补 WESP 2026（经济趋同放缓）和 IMF 博客（最贫困和脆弱国家日益落后）；第 37、62、63 条（2025 年 PIP 更新、新贫困线）补 SDG 报告 2025 和 Our World in Data 的转述。所有新增来源都支持原判断，未改判。局限：联合国和 Our World in Data 的贫困数字引自世界银行 PIP，只是第三方转述；真正独立数据只有 IMF 的增长数据和 WESP 的趋同判断。

