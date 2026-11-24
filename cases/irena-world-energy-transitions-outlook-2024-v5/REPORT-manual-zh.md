# 国际可再生能源署（IRENA）《世界能源转型展望2024：1.5°C路径》（World Energy Transitions Outlook 2024: 1.5°C Pathway）：出版后预测人工核查

- 案例目录：`cases/irena-world-energy-transitions-outlook-2024-v5/`
- 出版日期：**2024-11-11**（COP29巴库会议期间发布，PDF生成日；ISBN 978-92-9260-634-3）。正文用IRENA官方PDF（sha256 `90f34b24…`，与队列记录一致），用 `pdftotext -enc UTF-8` 转成TXT（sha256 `55a09338…`，338,475字符），TXT不入库。观察窗口为2024-11-11至2026-11-15，约两年。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

抽取：用仓库 prepare_book v5 流水线（toolkit main 85e6da1）把全文切成98块（3500字符、600字符上下文），助手逐块通读，按 DISCOVER_PROMPT_V5 写出模型本应返回的JSON（不做关键词筛选）。1.5°C情景与PES情景的路径数字属情景设定，只在报告明说“预计/将会”时才抽取；参考文献和附表未抽取。仓库代码完成引文对齐、历史句剔除（3条）、归属降级（1条第三方预测降为unclear）和去重，导入26条候选，其中25条可核验（密度约0.26条/块）。核验：每条先写scope，各做一次support和counter的Exa检索，对第8、9、13、18、23条补了第二轮、第15条补了第三轮；只从检索返回的URL中选源，原文用Exa contents抓取存档在data/sources（sha256），写入data/evidence.jsonl（40条）；助手阅读后按四分类规则判断，再经 pipeline.py apply assess → check → report。data/claims.jsonl与txt_import/claims_proposals.jsonl的context字段已清空。本稿由助手逐条对照报告原文与存档证据人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 25 条，剔除非预测 1 条，计入 **24 条预测**，其中 **10 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 6 |
| 趋势符合 | 3 |
| 部分符合 | 1 |
| 错误 | 0 |
| 暂无法判断 | 14 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **60.0%**（6/10） |
| 加权胜率 | **87.5%** |
| 错误率 | **0.0%**（0/10） |
| 未定占比（暂无法判断/预测） | 58.3%（14/24） |

## 总体评价

这是一份情景报告，大部分数字是1.5°C情景“需要做到”的路径，不是预测；真正的预测多以2030、2050为终点，窗口只有两年，24条预测中14条记暂无法判断（另有1条经复核为出版前史实，已剔除）。可判定的10条里，说对的6条都是短期、可直接观察的事：2024年为有记录最暖年份、COP29通过NCQG、AI推高用电、电池储能投资继续增长、技能短缺加剧、风光成为新增发电主力。趋势符合3条：光伏继续领跑新增装机、清洁氢投资大增（但欧洲大量项目取消、统计口径不同）、全球经济年增约3%。部分符合1条：美国《通胀削减法》的推动作用被2025年《大而美法案》削弱，欧盟一侧成立。原第23条（第二次需求确定报告“预计2024年第四季度发布”）经2026-11-16复核，报告已于2024-09-04发布、早于本书出版日2024-11-11，属出版前史实，按METHOD.md剔除，不计入可判定。没有判为错误的条目。光伏“正按轨道走向5.5 TW”、578 GW年增量“可以实现”两条，IRENA口径2025年新增511 GW仍低于所需年均值，记暂无法判断而非趋势符合。“2025年版展望上调情景结果”一条，未找到2025年版全球展望（下一版为2026年10月），2026版存档摘要也无可比数字，记暂无法判断。可判定样本只有10条且多为短期事实，胜率不宜外推到报告的长期情景。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（6 条）

- **#1** 「The proliferation of AI will clearly contribute to electricity demand」  
  判断：**正确**。IEA《能源与AI》（2025-04）：2024年全球数据中心用电约415 TWh，且在快速增长，AI是主要驱动；IEA称AI将推动数据中心用电激增。窗口内（2024-11至2026-11）AI确实在推高用电需求，方向已出现。反方（The Verge 2025-09）只质疑远期预测幅度，不否认用电上升。  
  来源：<https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai>；<https://www.iea.org/news/ai-is-set-to-drive-surging-electricity-demand-from-data-centres-while-offering-the-potential-to-transform-how-the-energy-sector-works>；<https://www.theverge.com/report/782952/ai-electricity-demand-inflated-forecast-report>
- **#7** 「The year 2024 is likely to represent the warmest on record globally」  
  判断：**正确**。WMO于2025-01-10确认2024年为有记录以来最暖年份，约比工业化前高1.55°C；Copernicus、NOAA、Berkeley Earth结论相同。  
  来源：<https://wmo.int/news/media-centre/wmo-confirms-2024-warmest-year-record-about-155degc-above-pre-industrial-level>；<https://climate.copernicus.eu/second-warmest-december-confirms-2024-warmest-year>
- **#15** 「As costs decline, these investments are expected to grow.」  
  判断：**正确**。书中称电池储能等电网配套投资（2023年410亿美元）会随成本下降继续增长。韩华引述IEA《世界能源投资2025》：电池储能投资2025年预计达660亿美元，较前几年明显增加；IEA 2026-05评论称2025年全球电池储能新增108 GW，同比增长约40%，再创纪录。方向已出现。  
  来源：<https://www.hanwha.com/newsroom/news/feature-stories/iea-world-energy-investment-report-2025-where-is-global-capital-flowing.do>；<https://www.iea.org/commentaries/battery-storage-is-scaling-up-and-taking-on-a-larger-system-role>
- **#19** 「the broader distribution and lower costs associated with VRE make them a more likely source for future bulk el…」  
  判断：**正确**。书中称风光等波动性可再生能源更可能成为未来大宗发电的来源（未写时点，按窗口检验方向）。Ember《全球电力评论2026》：2025年光伏创纪录增长，清洁电力满足了全部新增用电需求，可再生能源发电量超过煤电；IEA《全球能源评论2026》称2025年新增发电量绝大部分来自可再生能源。方向已出现。  
  来源：<https://ember-energy.org/latest-insights/global-electricity-review-2026/>；<https://www.iea.org/reports/global-energy-review-2026/electricity-supply>
- **#21** 「Many countries and industries are already experiencing acute skills shortages, a gap that is likely to widen a…」  
  判断：**正确**。书中称技能短缺“可能扩大”。IEA《世界能源就业2025》（2025-12）称能源就业大增，但技能短缺正在加剧，超过一半受访企业把熟练工短缺列为主要问题。方向已出现。  
  来源：<https://www.iea.org/news/energy-employment-has-surged-but-growing-skills-shortages-threaten-future-momentum>
- **#24** 「The NCQG will be established at CMA68 linked to the 2024 Baku Climate Conference (COP29).」  
  判断：**正确**。COP29（巴库，CMA6）于2024-11-24通过新的集体量化资金目标（NCQG）：发达国家牵头到2035年每年至少3000亿美元。  
  来源：<https://news.un.org/en/story/2024/11/1157416>；<https://unctad.org/news/countries-agree-300-billion-2035-new-climate-finance-goal-what-next>

### 趋势符合（3 条）

- **#3** 「The leading role played by solar PV is expected to continue for the rest of the decade」  
  判断：**趋势符合**。IRENA统计：2024年新增可再生装机585 GW中光伏约452 GW；2025年新增692 GW中光伏约511 GW，仍是新增最多的电源。窗口内光伏继续领先，与“本十年剩余时间保持领先”方向一致；终点2030年未到，只记趋势符合。  
  来源：<https://www.irena.org/News/articles/2025/Apr/Renewables-in-2024-5-Key-Facts-Behind-a-Record-Breaking-Year>；<https://www.pv-tech.org/irena-world-adds-510gw-of-new-solar-pv-capacity-in-2025/>
- **#16** 「The total is expected to soar because large-scale projects that recently reached financial close are expected …」  
  判断：**趋势符合**。书中称清洁氢投资（2023年按投运项目约20亿美元）未来几年将猛增。IEA《全球氢能评论2025》：2024年低排放氢项目资本支出43亿美元，增长80%，按已作出的最终投资决定，2025年可能再增80%以上至近80亿美元；同时欧洲多个项目取消（S&P Global）。统计口径（资本支出vs投运项目）不同，2025年为预估，只记趋势符合。  
  来源：<https://www.iea.org/reports/global-hydrogen-review-2025/investment-and-innovation>；<https://www.spglobal.com/energy/en/news-research/latest-news/energy-transition/110525-green-hydrogen-developers-reckon-with-reality-check-in-europe>
- **#25** 「Under the current business-as-usual assumptions, the global economic system is projected to grow at around 3% …」  
  判断：**趋势符合**。书中称按基准假设全球经济年增约3%、到2050年翻番。IMF 2025年10月WEO：全球增长2024年3.3%、2025年3.2%、2026年预计3.1%，与约3%一致；翻番终点为2050年，只记趋势符合。  
  来源：<https://www.imf.org/en/blogs/articles/2025/10/14/global-economic-outlook-shows-modest-change-amid-policy-shifts-and-complex-forces>

### 部分符合（1 条）

- **#20** 「These policies are anticipated to continue driving energy transition investments in the years ahead.」  
  判断：**部分符合**。书中称美国《通胀削减法》与欧盟绿色新政将继续推动能源转型投资。欧盟方面成立：IEA称2025年欧盟清洁能源投资近3900亿美元。美国方面不成立：2025年7月《大而美法案》加速取消风电、光伏税收抵免，E2统计2025年清洁能源项目取消额达348亿美元。一半应验。  
  来源：<https://www.iea.org/reports/world-energy-investment-2025/european-union>；<https://www.nixonpeabody.com/insights/alerts/2025/07/24/renewable-energy-after-the-big-beautiful-bill>；<https://e2.org/reports/clean-economy-works-2025-year-end-analysis/>

### 暂无法判断（14 条）

- **#2** 「Current national plans and targets are set to deliver only half of the required growth in renewable power by 2…」  
  判断：**暂无法判断**。书中判断“现有国家计划和目标到2030年只能交付所需增长的一半”。IRENA 2025年跟踪报告称现有目标比三倍目标少5.8 TW，与判断一致；但Ember等称实际装机增速已快于国家目标，结果要到2030年才能检验。  
  来源：<https://www.irena.org/Digital-Report/Tracking-progress-toward-tripling-renewable-energy-capacity-and-doubling-energy-efficiency-by-2030>；<https://ember-energy.org/latest-insights/renewable-additions-in-2025-are-once-again-expected-to-surge-putting-tripling-within-reach/>
- **#4** 「At the current pace of progress, an estimated 660 million people in developing countries will remain without a…」  
  判断：**暂无法判断**。“按现行进度2030年仍有6.6亿人无电”为2030年终点预测。Tracking SDG7 2025估计2030年约6.45亿人仍无电，与之接近；IEA称2025年无电人口降至约7.2亿（口径不同）。终点未到。  
  来源：<https://unstats.un.org/sdgs/report/2025/goal-07/>；<https://www.iea.org/commentaries/a-record-number-of-people-in-africa-gained-electricity-access-in-2025>
- **#5** 「Even if the energy transition follows the 1.5°C Scenario pathway, significant disparities are likely to remain…」  
  判断：**暂无法判断**。“即使按1.5°C情景，全球福利差距仍会存在”为情景条件下的长期判断，前提（全球按1.5°C路径转型）未出现，终点2050年，无法检验。  
  来源：—
- **#6** 「reductions are projected to be insufficient to keep global average temperatures from rising above 1.5°C of pre…」  
  判断：**暂无法判断**。“减排不足以在本世纪中叶前把升温控制在1.5°C以内”：UNEP《排放差距报告2025》称按现有NDC升温2.3–2.5°C、未来十年内很可能超过1.5°C，方向一致，但这是模型预估而非观测，终点为本世纪中叶，记暂无法判断。  
  来源：<https://www.unep.org/en/news-and-stories/press-release/new-climate-pledges-only-slightly-lower-dangerous-global-warming>
- **#8** 「The scenario results presented herein are subject to upward revision in the 2025 edition of the World Energy T…」  
  判断：**暂无法判断**。书中称情景结果“可能在2025年版《世界能源转型展望》中上调”（措辞为可能性）。检索到的IRENA展望页面与出版物列表在2024版之后只见2026年10月发布的2026版，未找到2025版全球展望；2026版的存档摘要未给出与2024版可比的光伏、储能数字，无法确认是否上调。  
  来源：<https://www.irena.org/Publications/2026/Oct/World-Energy-Transitions-Outlook-2026>；<https://www.irena.org/home/publications>
- **#9** 「solar PV deployment, at 347 GW added, is on track to hit the 5.5 TW needed to meet the tripling target」  
  判断：**暂无法判断**。书中称光伏“正按轨道走向三倍目标所需的5.5 TW”。IRENA：2024年新增光伏约452 GW，2025年约511 GW，逐年增加，但仍低于书中所需的年均578 GW（交流口径）；能否在2030年达到5.5 TW要到期再看。  
  来源：<https://www.irena.org/News/articles/2025/Apr/Renewables-in-2024-5-Key-Facts-Behind-a-Record-Breaking-Year>；<https://www.pv-tech.org/irena-world-adds-510gw-of-new-solar-pv-capacity-in-2025/>
- **#10** 「Net annual additions of 578 GW of solar PV capacity seem achievable considering the technology’s cost competit…」  
  判断：**暂无法判断**。“年净增578 GW光伏似乎可以实现”：IRENA交流口径2025年新增约511 GW，尚未达到；SolarPower Europe与IEA-PVPS的直流口径为664–690 GW，口径不同不能直接比较。指标为2030年前的年均值，终点未到。  
  来源：<https://www.pv-tech.org/irena-world-adds-510gw-of-new-solar-pv-capacity-in-2025/>；<https://www.pv-magazine.com/2026/09/28/global-solar-additions-hit-690-gw-in-2025/>
- **#11** 「global renewable power capacity is expected to reach 7.4 TW by 2030, still short of the target by more than 30…」  
  判断：**暂无法判断**。PES情景下2030年全球可再生装机7.4 TW、比目标少30%以上，为2030年终点预测。IEA《可再生能源2025》预计2025–2030年新增约4600 GW，与三倍目标仍有差距，但终点未到。  
  来源：<https://www.iea.org/reports/renewables-2025/executive-summary>
- **#12** 「cumulative offshore wind capacity under PES fails to meet the tripling goal by nearly one-third」  
  判断：**暂无法判断**。PES下海上风电累计装机比三倍目标（494 GW）少近三分之一：GWEC 2025年报告预计2030年约238 GW、GOWA称各国目标足以支持三倍增长，各方说法不一，终点2030年未到。  
  来源：<https://gowa-energy.org/news/offshore-wind-is-still-on-track-to-triple-globally-by-2030-despite-us-uncertainty>；<https://www.gwec.net/policy/offshorewind>
- **#13** 「the current battery EV and plug-in hybrid EV stock would need to rise to 360 million by 2030 from 40 million t…」  
  判断：**暂无法判断**。“按现有增速无法在2030年达到3.6亿辆电动车保有量”：IEA称2024年电动车销量超1700万、2025年超2000万（占新车四分之一），保有量快速增长；能否达到3.6亿要到2030年才能判断。  
  来源：<https://www.iea.org/reports/global-ev-outlook-2026/executive-summary>；<https://www.iea.org/reports/global-ev-outlook-2025/executive-summary>
- **#14** 「the rate of their deployment in industrial process heat supply is expected to remain low in 2030」  
  判断：**暂无法判断**。“工业过程热中热泵部署到2030年仍将偏低”：EHPA等称工业热泵仍是“沉睡的巨人”，部署有限；终点2030年未到。  
  来源：<https://ehpa.org/news-and-resources/publications/annual-report-2025-the-industrial-sleeping-giant/>
- **#17** 「Estimates show that an additional USD 704 billion will be invested through 2027 in factories manufacturing equ…」  
  判断：**暂无法判断**。“到2027年还将有7040亿美元投入能源转型设备工厂”为2027年终点的累计数。Rhodium称2025年全球清洁技术制造投资1550亿美元，比2023年峰值下降40%以上，累计额能否达到要到2027年才能判断。  
  来源：<https://www.cleaninvestmentmonitor.org/reports/global-clean-investment-2025>
- **#18** 「The United States and Europe are expected to make up for a greater share of investments, at a combined 20.5% (…」  
  判断：**暂无法判断**。“美国和欧洲在2024–2027年工厂投资中占比升至20.5%”：BNEF称2024年76%的清洁技术工厂投资仍在中国大陆；Rhodium称2025年中、美、欧制造投资均下降，美国多个工厂项目被取消。未找到2024–2025年美欧份额的直接数字，终点2027年未到。  
  来源：<https://about.bnef.com/insights/clean-energy/china-dominates-clean-technology-manufacturing-investment-as-tariffs-begin-to-reshape-trade-flows-bloombergnef/>；<https://www.cleaninvestmentmonitor.org/reports/global-clean-investment-2025>
- **#22** 「the SDG7 target on universal energy access looks increasingly likely to be missed」  
  判断：**暂无法判断**。“SDG7普遍用能目标看起来越来越可能落空”：Tracking SDG7 2025称进展偏离轨道，按现行趋势2030年仍有约6.45亿人无电；IEA称2025年无电人口降幅创纪录。目标年为2030年，未到期。  
  来源：<https://www.iea.org/reports/tracking-SDG7-the-energy-progress-report-2025>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| 23 | The Second Report is anticipated to be r… | historical | 出版前已发生的史实：UNFCCC常设财务委员会《第二次需求确定报告》已于2024-09-04作为SCF/2024/35/4文件发布（UNFCCC文件页“Publication date 04 Sep 2024”），Down To Earth 2024-09-18报道称报告于2024-09-10发布，均早于本书出版日2024-11-11，写作时“预计第四季度发布”在出版时已不是未定事项；按METHOD.md视为historical剔除，不计入可判定（原判部分符合）。 |

## 文件

- 本文：`cases/irena-world-energy-transitions-outlook-2024-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/irena-world-energy-transitions-outlook-2024-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/irena-world-energy-transitions-outlook-2024-v5/audit/manual_review_2026-11-15.py`
