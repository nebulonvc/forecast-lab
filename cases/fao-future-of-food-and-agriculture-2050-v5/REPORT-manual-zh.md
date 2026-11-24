# 联合国粮食及农业组织（FAO）《粮食和农业的未来：通向2050的不同路径》（The future of food and agriculture – Alternative pathways to 2050）：出版后预测人工核查

- 案例目录：`cases/fao-future-of-food-and-agriculture-2050-v5/`
- 出版日期：**2018 年**（FAO，罗马，ISBN 978-92-5-130158-6，I8429EN/1/10.18）。正文取自 FAO 官网 PDF `https://www.fao.org/3/I8429EN/i8429en.pdf`（sha256 `01643346…397`，与队列登记一致），pdftotext 提取文本 sha256 `6825ca2453b54afa2a401dcfb2930242100f1f6d59015c621ed182c2e831b215`。观察窗口为 2018→2026-11-15；书中明示的终点（2025、2030、2050、本世纪后期等）分别适用。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

本稿按 METHOD.md 执行。抽取：用仓库 prepare_book v5 流水线（toolkit 85e6da1）把全文切成 176 块（3500 字符、600 字符上下文；无跳过的前后附文）。助手逐块通读，按 DISCOVER_PROMPT_V5 写出模型本应返回的 JSON，再由仓库代码完成引文对齐、归属降级、去重和导入，得到 46 条候选，其中 40 条可核验预测（约 0.23 条/块）。本书是情景研究：第 2、3 章情景叙事与假设、附件的情景假设表不作为作者预测；第 4 章“基准情景（BAU）”结果作为以 BAU 为条件的预测抽取；联合国、OECD-FAO 等第三方预测除 FAO 明确采纳者外降为 unclear。核验：按 23 个主题先写 scope，各做一次 support 和一次 counter 的 Exa 检索（共三轮 50 次请求），只使用检索返回的 URL。所选来源经 Exa 内容接口抓取并存档于 data/sources（52 份，sha256），写入 data/evidence.jsonl（52 条），由助手逐条阅读存档文本后按四分类规则评断，再经 pipeline.py apply assess → check → report。本稿以 v5 抽取的候选句（`data/claims.jsonl` 中可判定的条目）为起点，由助手逐条对照书中原文与存档证据人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 40 条，剔除非预测 0 条，计入 **40 条预测**，其中 **27 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 9 |
| 趋势符合 | 10 |
| 部分符合 | 5 |
| 错误 | 3 |
| 暂无法判断 | 13 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **33.3%**（9/27） |
| 加权胜率 | **70.4%** |
| 错误率 | **11.1%**（3/27） |
| 未定占比（暂无法判断/预测） | 32.5%（13/40） |

## 总体评价

FAO 对 2018 年后大方向的判断多数成立：全球农业产出与粮食需求继续增长，需求增量转向中低收入国家；营养不足持续存在，2030 年“零饥饿”远未达成；撒哈拉以南非洲仍是营养不足发生率最高的地区；人口增长普遍放缓、非洲和南亚继续增长；农业就业比重持续下降；中国仍是最大生猪生产国；穷国与富国的收入差距未见收敛；谷物单产、农场内温室气体排放沿 BAU 方向上升。主要误判：以“趋势延续”为前提预计 2025 年五岁以下儿童超重率达 11%，实际仅约 5.5%；预计第一代生物燃料原料使用下降，实际继续增长并主导市场；BAU 下高收入国家和中国走向农产品净出口，实际中国与美国的农产品贸易逆差扩大。中国人口负增长比预测提前（2022 年即转负），耕地扩张远慢于 BAU 路径，粮价上涨主要来自供给与能源冲击而非需求，均只部分符合。2030、2050 年的定量情景终点（城市化、耕地、单产减产、价格、农业占比等）尚未到期，记为暂无法判断。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（9 条）

- **#1** 「If food and agricultural systems remain on their current path, the evidence points to a future characterized b…」  
  判断：**正确**。粮农系统并未转向报告设想的可持续路径；SOFI 2026显示2025年仍约6.45亿人（7.8%）面临饥饿，中度或重度粮食不安全仍广泛存在，粮食不安全持续。  
  来源：<https://www.fao.org/newsroom/detail/sofi-2026--hunger-not-inevitable--fao-says-as-global-hunger-report-shows-progress/en>；<https://www.who.int/news/item/21-07-2026-un-report--global-hunger-levels-ease-for-third-consecutive-year-as-regional-disparities-persist>；<https://news.un.org/en/story/2025/07/1165514>
- **#2** 「Agricultural production is expected to rise worldwide in response to population growth, dietary changes and in…」  
  判断：**正确**。2018年后全球农业产出继续上升：FAO统计年鉴与JIRCAS摘要显示全球农业生产价值按实际值20年增长89%，2022年达3.8万亿美元，人口与收入增长推动需求。  
  来源：<https://www.jircas.go.jp/en/program/proc/blog/20241127>；<https://openknowledge.fao.org/server/api/core/bitstreams/d784864f-7f28-49d2-903e-6680d09a9d97/content/cd2971en.html>
- **#7** 「the evidence points to persistent undernourishment in the future.」  
  判断：**正确**。2018年后营养不足持续存在：2022年峰值后虽连续三年下降，2025年仍有约6.45亿人面临饥饿，远未消除。  
  来源：<https://www.fao.org/newsroom/detail/sofi-2026--hunger-not-inevitable--fao-says-as-global-hunger-report-shows-progress/en>；<https://news.un.org/en/story/2025/07/1165514>
- **#8** 「significant and persistent increases are expected in Africa and South Asia」  
  判断：**正确**。联合国《世界人口展望2024》显示撒哈拉以南非洲人口继续快速增长，印度等南亚国家人口仍在增加，非洲和南亚人口持续显著增长。  
  来源：<https://population.un.org/wpp/assets/Files/WPP2024%5FSummary-of-Results.pdf>；<https://ourworldindata.org/un-population-2024-revision/>
- **#30** 「SSA remains the most foodinsecure region, with the highest prevalence of undernourishment if trends continue.」  
  判断：**正确**。SOFI 2025/2026显示非洲营养不足发生率约20%，远高于亚洲（约6%）和拉美，2025年非洲首次成为饥饿人口最多的地区，仍是粮食最不安全的地区。  
  来源：<https://www.fao.org/newsroom/detail/progress-on-hunger-continues--but-africa-and-new-crises-raise-concerns--fao-chief-economist/en>；<https://www.fao.org/newsroom/detail/beating-hunger-through-social-protection--investments-and-resilience--fao-chief-economist/en>
- **#34** 「China, which remains the largest producer of pigs.」  
  判断：**正确**。美国农业部及中国统计显示2024年中国猪肉产量约5706万吨，约占全球45%，仍是全球最大生猪生产国。  
  来源：<https://www.fas.usda.gov/data/production/0113000>；<https://husfarm.com/production/pork/china/>
- **#37** 「Population and income growth will continue to drive up food demand and change people’s dietary preferences.」  
  判断：**正确**。OECD-FAO展望显示收入增长推动中等收入国家动物源食品消费上升，德国联邦统计局整理的数据显示全球人均肉类消费由2013年41.5公斤升至2023年45.3公斤；人口与收入增长继续推高需求并改变膳食结构。  
  来源：<https://www.fao.org/markets-and-trade/news-and-events/news-detail/oecd-fao-agricultural-outlook-2025-2034--emerging-economies-will-drive-growth-in-animal-source-food-consumption-and-production/en>；<https://www.fao.org/newsroom/detail/oecd-fao-agricultural-outlook--emerging-economies-will-continue-driving-agricultural-markets/en>；<https://www.destatis.de/EN/Themes/Countries-Regions/International-Statistics/Data-Topic/AgricultureForestryFisheries/livestock_meat.html>
- **#38** 「Unaddressed climate change will increasingly affect yields and rural livelihoods while agriculture will keep e…」  
  判断：**正确**。IPCC AR6确认气候变化已减缓农业生产率增长并加剧粮食不安全；FAO统计显示2023年农场内排放仍达8.1 Gt CO2当量，农业持续排放温室气体。  
  来源：<https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_SPM.pdf>；<https://www.ipcc.ch/report/ar6/wg2/downloads/outreach/IPCC_AR6_WGII_FactSheet_FoodAndWater.pdf>；<https://www.fao.org/statistics/highlights-archive/highlights-detail/greenhouse-gas-emissions-from-agrifood-systems.-global--regional-and-country-trends--2001-2023/en>
- **#40** 「The ongoing wider process of economic transformation has led in many instances to fewer people being engaged i…」  
  判断：**正确**。ILO模型估计显示全球农业就业占总就业比重由1991年的42.8%持续降至2025年的25.8%（历史最低），2025年较2024年再降约0.3个百分点；农业就业减少的趋势在2018年后延续。  
  来源：<https://www.pyzia.app/entities/world/employment-in-agriculture-percent-of-total-employment-modeled-ilo-estimate>；<https://agriculture.statizoid.com/stat/employment-in-agriculture-percent-of-total-employment-modeled-ilo-estimate/world/>

### 趋势符合（10 条）

- **#9** 「Driven by these important demographic forces, the demand for food is expected to significantly increase, parti…」  
  判断：**趋势符合**。OECD-FAO显示上一个十年全球农业消费增长中中国占28%，未来增长转向印度、东南亚和撒哈拉以南非洲，且几乎全部来自中低收入国家；需求持续增长、重心向非洲和南亚转移，方向符合，但“显著增长”的大部分依据为展望期数字，按趋势符合计。  
  来源：<https://www.fao.org/newsroom/detail/oecd-fao-agricultural-outlook--emerging-economies-will-continue-driving-agricultural-markets/en>；<https://www.oecd.org/en/publications/2025/07/oecd-fao-agricultural-outlook-2025-2034_3eb15914.html>；<https://www.oecd.org/en/publications/oecd-fao-agricultural-outlook-2025-2034_601276cd-en/full-report/agricultural-and-food-markets-trends-and-prospects_d3812d71.html>
- **#14** 「even the recently-established objective of eradicating hunger by 2030, set by the 2030 Agenda for Sustainable …」  
  判断：**趋势符合**。SOFI 2026指出尽管饥饿连续三年下降，世界仍远未按期在2030年实现零饥饿，2030年预计仍有约5亿人挨饿；方向符合“目标无法实现”，最终结果待2030年验证。  
  来源：<https://sdg.iisd.org/news/hunger-food-insecurity-down-but-regional-progress-uneven-sofi-2026/>；<https://www.who.int/news/item/21-07-2026-un-report--global-hunger-levels-ease-for-third-consecutive-year-as-regional-disparities-persist>
- **#15** 「At the current pace of convergence, very high per capita income differentials between HIC and LMIC could persi…」  
  判断：**趋势符合**。世界银行2024年报告称最脆弱的75个国家中半数与最富经济体的收入差距本世纪首次扩大；近年数据也未见穷国更快增长，收入差距持续，趋势符合，“数十年”待验证。  
  来源：<https://www.worldbank.org/en/news/press-release/2024/04/14/the-great-reversal-prospects-risks-and-policies-in-international-development-association-countries>；<https://www.chat-gdp.org/p/we-were-wrong-about-convergence>
- **#16** 「demographic dynamics are expected to result in a spike in the number of young people who will join the ranks o…」  
  判断：**趋势符合**。国际劳工组织指出未来15年非洲约3.75亿青年将进入工作年龄，联合国2026年青年人口要点显示低收入和中低收入国家青年人口仍在增长；趋势符合。  
  来源：<https://www.ilo.org/resource/article/creating-decent-jobs-rapidly-expanding-young-african-labour-force>；<https://www.un.org/development/desa/pd/sites/www.un.org.development.desa.pd/files/undesa_pd_2026_world_population_highlights-youth.pdf>
- **#18** 「it is likely that the additional amounts of food needed in the coming decades will have to be produced mainly …」  
  判断：**趋势符合**。FAO土地统计显示2022年全球耕地约15.73亿公顷，较2012年变化有限，而谷物单产2023年创历史新高；美国农业部指出全要素生产率是产出增长主因；卫星研究显示耕地仍有扩张，故按趋势符合计。  
  来源：<https://www.fao.org/statistics/highlights-archive/highlights-detail/land-statistics-2001-2022.-global--regional-and-country-trends/en>；<https://data.pispace.eu/countries/world/cereal-yield>；<https://ers.usda.gov/sites/default/files/_laserfiche/publications/108650/EIB-268.pdf?v=47411>；<https://www.nature.com/articles/s43016-021-00429-z>
- **#26** 「Under BAU, the world’s gross agricultural output (in terms of value) is projected to grow by around 50 percent…」  
  判断：**趋势符合**。全球农业生产价值2002–2022年按实际值增长89%，2012年后的增长速度与“2012–2050年增长约50%”的路径一致；最终结果待2050年验证。  
  来源：<https://www.jircas.go.jp/en/program/proc/blog/20241127>；<https://openknowledge.fao.org/server/api/core/bitstreams/d784864f-7f28-49d2-903e-6680d09a9d97/content/cd2971en.html>
- **#29** 「In the BAU scenario the PoU decreases to about 7 percent in 2030, which is well above the SDG2 target of elimi…」  
  判断：**趋势符合**。SOFI 2026显示营养不足发生率由2022年8.6%降至2025年7.8%，正朝2030年约7%的方向变化，且仍远未达到SDG2；最终结果待2030年验证。  
  来源：<https://www.fao.org/newsroom/detail/sofi-2026--hunger-not-inevitable--fao-says-as-global-hunger-report-shows-progress/en>；<https://www.fao.org/newsroom/detail/progress-on-hunger-continues--but-africa-and-new-crises-raise-concerns--fao-chief-economist/en>
- **#32** 「Under BAU, average yields for cereals (wheat, rice and maize) increase globally by around 30 percent between 2…」  
  判断：**趋势符合**。全球谷物单产2023年达约4229公斤/公顷，创历史新高，2012年以来持续上升，速度不低于年均0.7%的预测路径；最终结果待2050年验证。  
  来源：<https://data.pispace.eu/countries/world/cereal-yield>；<https://exponentialtracker.com/data/world_cereal_yield.csv>
- **#36** 「Quite significant growth in gross agricultural output (see Section 4.2), which was not adequately compensated …」  
  判断：**趋势符合**。FAO统计显示2023年农场内（作物与畜牧）排放8.1 Gt CO2当量，较2001年增长17%，在亚洲和非洲上升明显，方向符合BAU下农业排放增加；2050年增20%的终点待验证。  
  来源：<https://www.fao.org/statistics/highlights-archive/highlights-detail/greenhouse-gas-emissions-from-agrifood-systems.-global--regional-and-country-trends--2001-2023/en>
- **#39** 「In this context, LMIC look highly unlikely to catch up with HIC for several decades」  
  判断：**趋势符合**。世界银行指出最脆弱国家与富国的收入差距本世纪首次扩大，近十余年未见穷国整体追赶；“几十年内难以赶上”趋势符合，最终待验证。  
  来源：<https://www.worldbank.org/en/news/press-release/2024/04/14/the-great-reversal-prospects-risks-and-policies-in-international-development-association-countries>；<https://www.chat-gdp.org/p/we-were-wrong-about-convergence>

### 部分符合（5 条）

- **#4** 「Climate change and population growth may exacerbate water scarcity.」  
  判断：**部分符合**。联合国《世界水资源开发报告2024》指出全球淡水取用量近年每年增长近1%，约一半人口一年中至少部分时间严重缺水，人口与城市化推高用水；但SDG 6.4.2显示全球平均取水比例约18%，统计上未见全球水压力显著上升，只部分符合“水资源短缺加剧”。  
  来源：<https://www.unesco.org/reports/wwdr/en/2024/s>；<https://www.unwater.org/publications/progress-level-water-stress-2024-update>
- **#19** 「Expanding food demand, particularly if left unmanaged, may put an upward pressure on prices」  
  判断：**部分符合**。粮价在2021–2022年创纪录并在2025年仍比2014–2016基期高约27%，但联合国与FAO将2022年高点主要归因于能源、投入品与乌克兰战争等供给冲击，需求推高粮价只部分成立。  
  来源：<https://news.un.org/en/story/2022/03/1113332>；<https://www.fao.org/new-york/news/news-detail/War-largely-drives-food-prices-to-record-levels-threatens-global-food-security/en>；<https://www.fao.org/newsroom/detail/fao-food-price-index-dips-in-december-despite-higher-world-cereal-quotations/en>
- **#20** 「Population growth is projected to slow down in all regions.」  
  判断：**部分符合**。联合国人口司2024年报告指出撒哈拉以南非洲因生育率持续偏高将贡献2050年前全球一半以上的人口增量，其他地区人口增长率多为正但在下降；OWID指出全球增长率因生育率下降而迅速放缓。除撒哈拉以南非洲外各地区放缓已获证实，撒哈拉以南非洲增速放缓的直接证据不足，部分符合。  
  来源：<https://www.un.org/development/desa/pd/sites/www.un.org.development.desa.pd/files/undesa_pd_2024_e_cn.9_2024_2_advance-unedited.pdf>；<https://ourworldindata.org/un-population-2024-revision/>；<https://population.un.org/wpp/assets/Files/WPP2024%5FSummary-of-Results.pdf>
- **#21** 「China where – on the contrary – growth rates are almost zero by 2030 and become negative thereafter.」  
  判断：**部分符合**。中国人口在2022年已出现1961年以来首次负增长，比预测的“2030年接近零、此后转负”提前；方向正确但时间点不符，部分符合。  
  来源：<https://www.stats.gov.cn/english/PressRelease/202302/t20230227_1918979.html>；<https://www.bbc.com/news/world-asia-china-64300190>
- **#35** 「The BAU scenario projects arable land to rise globally by 165 million hectares (11 percent), from 1 567 millio…」  
  判断：**部分符合**。FAO土地统计显示2022年全球耕地约15.73亿公顷，仅比书中2012年基数15.67亿公顷略增；方向一致但增幅远低于“2050年增至17.32亿公顷”的路径，部分符合。  
  来源：<https://www.fao.org/statistics/highlights-archive/highlights-detail/land-statistics-2001-2022.-global--regional-and-country-trends/en>；<https://www.nature.com/articles/s43016-021-00429-z>

### 错误（3 条）

- **#12** 「If this trend continues, by 2025 the percentage of overweight, including obese, children under five will reach…」  
  判断：**错误**。2025年联合国儿童基金会/世卫组织/世界银行联合估计：2024年五岁以下儿童超重率约5.5%（3550万），世卫组织预计2025年约5.6%，远低于预测的11%（7000万）。  
  来源：<https://www.who.int/data/gho/data/themes/topics/joint-child-malnutrition-estimates-unicef-who-wb>；<https://data.unicef.org/wp-content/uploads/2025/07/JME-Brochure-2025.pdf>；<https://apps.who.int/gb/ebwha/pdf_files/EB154/B154_22-en.pdf>
- **#22** 「whereas the use of biomass feedstock for first-generation biofuels is expected to decline.」  
  判断：**错误**。OECD-FAO展望显示2021–2023年生物燃料产量连续增长，第一代生物燃料（玉米、糖料、植物油）继续主导市场；纤维素乙醇发展停滞，第一代原料使用并未下降。  
  来源：<https://www.oecd.org/en/publications/oecd-fao-agricultural-outlook-2024-2033_4c5d2cfb-en/full-report/component-13.html>；<https://www.oecd.org/en/publications/oecd-fao-agricultural-outlook-2025-2034_601276cd-en/full-report/biofuels_6d29857a.html>；<https://task39.ieabioenergy.com/publications/global-study-reveals-why-cellulosic-ethanol-stalled-and-where-it-is-finally-gaining-momentum/>
- **#31** 「HIC and China are projected to raise their production more than their domestic absorption」  
  判断：**错误**。实际走向与预测相反：中国2023年农产品贸易逆差1351.8亿美元，谷物、油籽进口继续增长；美国在2023、2024财年出现创纪录农产品贸易逆差。欧盟虽保持顺差，但中国和美国等主要经济体并未出现产量增长快于国内需求、走向净出口的趋势。  
  来源：<https://www.moa.gov.cn/ztzl/nybrl/rlxx/202401/t20240123_6446367.htm>；<https://www.fb.org/intel/markets/record-u-s-agricultural-trade-deficit-forecasted-to-keep-growing>；<https://ec.europa.eu/eurostat/en/web/products-eurostat-news/w/ddn-20250513-2>

### 暂无法判断（13 条）

- **#3** 「If the entire range of production and consumption costs is taken into account, including resource degradation …」  
  判断：**暂无法判断**。“若计入资源退化和温室气体等全部成本”这一前提并未实施，无法检验粮价会否因此显著上涨。  
  来源：<https://www.fao.org/newsroom/detail/fao-food-price-index-dips-in-december-despite-higher-world-cereal-quotations/en>
- **#5** 「Such impacts are likely to become even stronger later in this century.」  
  判断：**暂无法判断**。“本世纪后期影响更强”的终点远在截止日之后；IPCC AR6仅确认气候变化已对农业产生负面影响。  
  来源：<https://www.ipcc.ch/report/ar6/wg2/downloads/outreach/IPCC_AR6_WGII_FactSheet_FoodAndWater.pdf>
- **#6** 「Unaddressed climate change, which is associated, inter alia, with unsustainable agricultural practices, is lik…」  
  判断：**暂无法判断**。条件“不应对气候变化”及其导致更多土地与用水的因果路径无法在截止日前单独识别，暂无法判断。  
  来源：<https://www.ipcc.ch/report/ar6/wg2/downloads/outreach/IPCC_AR6_WGII_FactSheet_FoodAndWater.pdf>；<https://www.nature.com/articles/s43016-021-00429-z>
- **#10** 「by 2050, two-thirds of the global population could be living in urban areas」  
  判断：**暂无法判断**。“2050年三分之二人口居住城市”的终点未到；且联合国2025年新版城市化展望改用新口径，暂无法判断。  
  来源：<https://www.un.org/development/desa/pd/world-urbanization-prospects-2025>；<https://www.un.org/en/desa/68-world-population-projected-live-urban-areas-2050-says-un>
- **#11** 「should per capita income grow at sustained rates in LMIC (excluding China), as observed in China, in upcoming …」  
  判断：**暂无法判断**。前提“中低收入国家人均收入像中国那样持续高速增长”并未出现（世界银行称半数最脆弱国家收入差距扩大），条件预测无法检验。  
  来源：<https://www.worldbank.org/en/news/press-release/2024/04/14/the-great-reversal-prospects-risks-and-policies-in-international-development-association-countries>
- **#13** 「under a business as usual scenario, by 2030 more than 650 million people will be undernourished」  
  判断：**暂无法判断**。2030年终点未到；SOFI 2026预计2030年约5.1–5.2亿人营养不足，低于预测的6.5亿以上，但终点尚未到来，暂无法判断。  
  来源：<https://sdg.iisd.org/news/hunger-food-insecurity-down-but-regional-progress-uneven-sofi-2026/>；<https://www.fao.org/newsroom/detail/sofi-2026--hunger-not-inevitable--fao-says-as-global-hunger-report-shows-progress/en>
- **#17** 「Without sufficient employment opportunities, this population trend may lead to faster rates of outmigration an…」  
  判断：**暂无法判断**。条件“缺乏足够就业机会”与外迁、城市化加速的因果关系无法在截止日前单独识别，暂无法判断。  
  来源：<https://www.ilo.org/resource/article/creating-decent-jobs-rapidly-expanding-young-african-labour-force>
- **#23** 「These model results suggest that climate change will have mostly negative impacts on yields, with reductions o…」  
  判断：**暂无法判断**。2050年气候变化使单产减少约5%的终点未到，暂无法判断。  
  来源：<https://www.ipcc.ch/report/ar6/wg2/downloads/outreach/IPCC_AR6_WGII_FactSheet_FoodAndWater.pdf>
- **#24** 「In general, by 2050 technical progress should outweigh the impacts of climate change」  
  判断：**暂无法判断**。2050年技术进步抵消气候影响的终点未到，暂无法判断。  
  来源：<https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_SPM.pdf>
- **#25** 「Under the BAU scenario the agricultural sectors become smaller in LMIC, with the share of value added diminish…」  
  判断：**暂无法判断**。2050年中低收入国家农业增加值占比约5%的终点未到，公开数据未直接给出可比口径，暂无法判断。  
  来源：<https://data.worldbank.org/indicator/NV.AGR.TOTL.ZS>
- **#27** 「much higher growth is expected mainly in SSA」  
  判断：**暂无法判断**。公开资料未提供2018年以来按地区可比的农业产出增长数据，无法确认增长是否主要集中在撒哈拉以南非洲，暂无法判断。  
  来源：<https://www.ers.usda.gov/data-products/chart-gallery/chart-detail?chartId=102911>；<https://www.oecd.org/en/publications/oecd-fao-agricultural-outlook-2025-2034_601276cd-en/full-report/agricultural-and-food-markets-trends-and-prospects_d3812d71.html>
- **#28** 「In the second half of the projection period prices begin to rise steadily, and by 2050 they are 13 percent hig…」  
  判断：**暂无法判断**。2050年价格比2012年高13%的终点未到，暂无法判断。  
  来源：<https://www.fao.org/newsroom/detail/fao-food-price-index-dips-in-december-despite-higher-world-cereal-quotations/en>
- **#33** 「Under BAU, harvested areas are projected to increase globally by around 238 million hectares (around 18 percen…」  
  判断：**暂无法判断**。公开资料未提供可比的全球收获面积数据，2050年终点也未到，暂无法判断。  
  来源：<https://www.fao.org/statistics/highlights-archive/highlights-detail/land-statistics-2001-2022.-global--regional-and-country-trends/en>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/fao-future-of-food-and-agriculture-2050-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/fao-future-of-food-and-agriculture-2050-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/fao-future-of-food-and-agriculture-2050-v5/audit/manual_review_2026-11-15.py`

## 说明

- 本书主体是三种情景（BAU、TSS、SSS）的模型比较。报告本身说明情景不是预测，因此 TSS、SSS 叙事及第 2、3 章的情景假设一律不计入；仅 BAU 结果和作者以自身口吻表述的趋势判断进入核验。
- BAU 条件按“现实大体延续既有趋势、未出现 TSS 式转型”处理：判对错（第 1、30、31、35 条等）时视为条件成立；判趋势符合的 BAU 条目（第 14、26、29、32、36 条）保持条件未知，只计趋势分。
- 第 3、6、11、17 条为条件句，前提未出现或无法单独识别，记为暂无法判断；第 27 条找不到可比的分地区产出增长数据，记为暂无法判断。
- 候选中 6 条因第三方归属或情景叙事被流水线降为 unclear，不进入核验；txt-00091“BAU 下前半段价格大体稳定”被仓库校验判为非预测而排除。
- 统计以 pipeline.py report 的 summary.json 为准；本表的加权胜率按 manual_report.py 的权重计算。

