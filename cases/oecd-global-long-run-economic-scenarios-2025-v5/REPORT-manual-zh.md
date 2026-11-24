# 经合组织《全球长期经济情景：2025年更新》（OECD Global Long-run Economic Scenarios: 2025 Update，OECD Economic Policy Paper No. 36）：出版后预测人工核查

- 案例目录：`cases/oecd-global-long-run-economic-scenarios-2025-v5/`
- 出版日期：OECD Publishing, Paris，2025-09-04（OECD Economic Policy Paper No. 36），作者 Yvan Guillemette（OECD 经济部），CC BY 4.0。**按 2025-09 起算**，观察窗口约 14 个月（2025-09-04 至 2026-11-15）。报告的情景从 2025 年展望到 **2100 年**，大部分数字终点在 2030 年代至 2100 年。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

按仓库 DeepSeek 管线手工代替模型调用：以 `pdftotext -enc UTF-8` 生成全文 TXT（PDF sha256 `d7a8003a…`，TXT sha256 `351ec289…`，242,974 字符），`prepare_book.split_text(3500, 600)` 得到 71 个 chunk，逐块通读，没有用关键词筛选。参考文献、附表和方法附录中的历史数据没有抽取。主要发现与正文重复的同一判断只抽一次。加速转型（ET）情景与基准（BAU）情景的两条反事实对比按假设处理、排除在外。经 `validate_chunk_predictions` 与 `claims_from_results` 导入 51 条可解析预测（全部 `claim_type=forecast`，显式时点 37 条、隐含时点 14 条，降级 0、重复 0）。引文均为 TXT 逐字片段，`changes` 不跨行。全文未入库。本稿由助手逐条对照报告原文，依据 2025-09 至 2026-11-15 窗口内可公开访问的来源人工复核（Exa 检索，结果存档于 `data/sources/`，带 sha256，共 29 条证据）：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 51 条，剔除非预测 0 条，计入 **51 条预测**，其中 **7 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 0 |
| 趋势符合 | 6 |
| 部分符合 | 1 |
| 错误 | 0 |
| 暂无法判断 | 44 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **0.0%**（0/7） |
| 加权胜率 | **71.4%** |
| 错误率 | **0.0%**（0/7） |
| 未定占比（暂无法判断/预测） | 86.3%（44/51） |

## 总体评价

这是一份模型情景报告，不是一本预言集：几乎所有数字都是 2030–2100 年的模型路径（潜在增速、劳动效率、生活水平趋同、气候损失），在约 14 个月的窗口里无法检验，所以 51 条中有 44 条记为“暂无法判断”。能在窗口内检验的 7 条主要是方向性或现状延续的判断，整体没有被推翻：2025 年全球气温仍处于有记录以来最高的三年之列，2015–2025 年为最暖的 11 年；按购买力平价中国仍是最大经济体，印度第三；韩国劳动年龄人口占比首次跌破 70%；Kotz 等人的气候损失研究于 2025 年 12 月被撤回，说明水平效应与增长效应之争远未解决；变压器和电网设备短缺、价格上涨持续到 2026 年；ILO 2026 年数据显示北非、阿拉伯国家和南亚的就业人口比仍明显低于其他地区。唯一的部分符合是阿根廷与土耳其的宏观稳定：土耳其通胀继续回落（2026 年 10 月 29.77%），阿根廷同比通胀却从 2025 年的 31.5% 回升到 33.1%。没有一条记为“错误”，但也没有一条能记为“正确”，因为能观察到的只是方向，数值和终点都还远。另需注意：全球化石能源 CO2 排放 2025 年创新高，但全球碳计划预计 2026 年下降约 0.4%，与“持续增加到 2040 年前后”的路径出现分歧，本稿记为暂无法判断。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 趋势符合（6 条）

- **#2** 「China remains the world’s largest economy until the mid-2060s when it is surpassed by India.」  
  判断：**趋势符合**。世界银行2025年PPP GDP表：中国约41.26万亿国际元居首，美国约30.77万亿、印度约17.20万亿；窗口内中国仍是按PPP最大经济体、印度位列第三，与"中国保持最大直到2060年代中期"方向一致；印度何时超越仍未到期，故只记趋势符合。  
  来源：<https://datacatalogfiles.worldbank.org/ddh-published/0038129/DR0046438/GDP_PPP.pdf>；<https://www.statisticstimes.com/economy/china-vs-india-economy.php>
- **#4** 「The global average surface temperature anomaly continues to increase throughout the projection period and reac…」  
  判断：**趋势符合**。WMO确认2025年为有记录以来最暖的三年之一，2015–2025年为最暖的11年；Copernicus称2025年比工业化前高约1.47°C，为第三暖年（比2024年低0.13°C，受拉尼娜影响）。长期升温方向持续，与"气温持续上升"一致；2100年约2½°C的数值无法检验，故只记趋势符合。  
  来源：<https://wmo.int/news/media-centre/wmo-confirms-2025-was-one-of-warmest-years-record>；<https://www.ecmwf.int/en/about/media-centre/news/2025/2025-third-warmest-year>
- **#18** 「In a few countries the pure demographic component (trend working-age population share) contributes positively …」  
  判断：**趋势符合**。韩国2025年人口住房普查（2026年7月发布）：劳动年龄人口（15–64岁）为3587万，比上年减少39.3万（-1.1%），占总人口比重从70.0%降至69.2%、首次跌破70%，65岁以上人口占比20.7%、首次超过20%。人口结构拖累方向得到确认；每年0.7个百分点的拖累幅度无法检验，故只记趋势符合。  
  来源：<https://www.asiae.co.kr/en/article/2026072811224929162>；<https://en.sedaily.com/economy/2026/07/29/as-workers-shrink-by-400000-elderly-grow-by-600000>
- **#31** 「Such empirical questions are unlikely to be resolved soon, as many more years of experience and data on a chan…」  
  判断：**趋势符合**。2025年12月3日，Kotz等人在Nature发表的气候经济损失研究（支持增长效应、损失较大）在两篇"Matters Arising"批评后被撤回，作者表示将重新投稿；NGFS同日就其长期情景的物理风险估计发表声明。窗口内这一实证争论仍未解决，与"短期内难以解决"一致；"短期"的终点不明确，故只记趋势符合。  
  来源：<https://www.pik-potsdam.de/en/news/latest-news/authors-retract-nature-study-on-economic-damages-from-climate-change-will-resubmit-for-peer-review>；<https://www.ngfs.net/en/press-release/statement-regarding-physical-risk-estimates-phase-v-ngfs-long-term-scenarios>
- **#34** 「the costs of some labour-intensive tasks, such as insulating old buildings or reshaping electric grids, may ri…」  
  判断：**趋势符合**。2026年资料：POWER杂志（2026年1月）引用Wood Mackenzie称美国变压器市场结构性失衡、需求超过产能；Rystad称2026年全球电网资本开支将超6500亿美元、比2020年翻倍以上，主要原因之一是价格上涨。电网改造成本上升的方向与书中一致；建筑保温成本没有检索到可比数据，故只记趋势符合。  
  来源：<https://www.powermag.com/transformers-in-2026-shortage-scramble-or-self-inflicted-crisis/>；<https://www.pv-magazine.com/2026/06/06/global-grid-capex-to-surpass-650-billion-in-2026-says-rystad-energy/>
- **#39** 「Aggregate employment rates in South Asia and Middle East and North Africa remain substantially lower than in o…」  
  判断：**趋势符合**。ILO《2026年就业与社会趋势》区域表：2025年就业人口比北非38.7%、阿拉伯国家44.8%、南亚51.8%，而撒哈拉以南非洲66.2%、东亚61.8%、东南亚65.1%；FRED（ILO模型估计）显示2025年世界平均约58.06%。窗口内"南亚和中东北非就业率明显偏低"依然成立；书中说的是长期持续，故只记趋势符合。  
  来源：<https://www.themimu.info/sites/themimu.info/files/documents/Report_Employment_and_Social_Trends_2026_ILO_0.pdf>；<https://fred.stlouisfed.org/series/SLEMPTOTLSPZSWLD>

### 部分符合（1 条）

- **#24** 「Recent improvements in the macroeconomic situation of both countries portend well for the future」  
  判断：**部分符合**。土耳其：央行2026年10月物价报告显示年通胀为29.77%，低于2025年10月的32.87%，通胀继续回落（支持）。阿根廷：2025年通胀31.5%、为8年最低，但2026年10月同比通胀回升至33.1%，月度通胀连续两个月上升（反向）。两国中一国改善延续、一国回升，记部分符合。  
  来源：<https://www.tcmb.gov.tr/wps/wcm/connect/7e9a7146-8c69-492f-8834-15ee5098fd12/mpriceoctober26.pdf?MOD=AJPERES>；<https://www.infobae.com/economia/2026/11/12/la-inflacion-en-octubre-fue-de-22-y-acumulo-331-en-los-ultimos-doce-meses/>

### 暂无法判断（44 条）

- **#1** 「global annual potential output growth is projected to moderate gradually from around 2.9% today to 2.7% in the…」  
  判断：**暂无法判断**。全球潜在产出增速放缓到2030年代初2.7%属中期情景；IMF 2026年10月WEO只给出近两年实际增速预测（2026年3.1%左右），不是潜在增速，终点在2030年代以后（或长期情景），观察窗口仅约14个月（2025-09至2026-11），无法判断。  
  来源：<https://www.imf.org/en/publications/weo/issues/2026/10/13/world-economic-outlook-october-2026>
- **#3** 「Global annual potential output per capita growth slows by less than the overall output, falling from about 2% …」  
  判断：**暂无法判断**。全球人均潜在增速降至2050年1¼%为长期情景；终点在2030年代以后（或长期情景），观察窗口仅约14个月（2025-09至2026-11），无法判断。  
  来源：<https://www.worldbank.org/en/news/press-release/2026/01/13/global-economic-prospects-january-2026-press-release>
- **#5** 「The reduction in global output associated with climate change, estimated to be approximately 1¾ per cent of gl…」  
  判断：**暂无法判断**。2100年气候损失近9%为模型终点值；终点在2030年代以后（或长期情景），观察窗口仅约14个月（2025-09至2026-11），无法判断。  
  来源：—
- **#6** 「With a steeper climate damage curve, at the high end of recent estimates, projected climate damages reduce glo…」  
  判断：**暂无法判断**。高损害曲线情景（BAU2）下2100年损失36%：条件为模型参数假设，无法观察，终点2100。  
  来源：—
- **#7** 「This scenario limits the global temperature increase to 1.6°C by 2100, meeting the Paris climate agreement goa…」  
  判断：**暂无法判断**。加速转型（ET）情景2100年1.6°C：前提为各国加速脱碳，窗口内未见该条件成立，终点2100。  
  来源：—
- **#8** 「East Asia and Pacific disproportionately so: its growth contribution declines from more than one percentage po…」  
  判断：**暂无法判断**。东亚太平洋对全球增长贡献到本世纪末降至0.2个百分点以下；终点在2030年代以后（或长期情景），观察窗口仅约14个月（2025-09至2026-11），无法判断。  
  来源：—
- **#9** 「China accounts for most of this slowdown, its individual contribution to global annual growth falling from abo…」  
  判断：**暂无法判断**。中国对全球增长贡献到2050年代后期降为零；终点在2030年代以后（或长期情景），观察窗口仅约14个月（2025-09至2026-11），无法判断。  
  来源：—
- **#10** 「the share of East Asia and Pacific in global output continues to rise through to the early-2030s before starti…」  
  判断：**暂无法判断**。东亚太平洋占全球产出份额"持续上升至2030年代初"：已检索到的IMF/世界银行区域份额页面多为动态数据页，未能取得可存档的东亚太平洋PPP份额时间序列；另有资料称中国名义份额2021年后下降，口径不同，不足以判断。  
  来源：—
- **#11** 「sub-Saharan Africa, the latter projected to account for some 13% of global output by the end of the projection…」  
  判断：**暂无法判断**。撒哈拉以南非洲2100年占全球产出13%；终点在2030年代以后（或长期情景），观察窗口仅约14个月（2025-09至2026-11），无法判断。  
  来源：—
- **#12** 「carbon-based sources still account for three quarters of the global primary energy mix in 2050 and more than 6…」  
  判断：**暂无法判断**。2050年碳基能源仍占一次能源约四分之三；IEA WEO 2025的现行政策情景与既定政策情景本身也是预测而非观测，终点在2030年代以后（或长期情景），观察窗口仅约14个月（2025-09至2026-11），无法判断。  
  来源：<https://www.iea.org/reports/world-energy-outlook-2025/current-policies-scenario>
- **#13** 「global net GHG emissions are projected to keep increasing through around 2040 before starting to decline」  
  判断：**暂无法判断**。全球碳预算：2025年化石CO2排放预计增1.1%创新高（支持继续增加）；但2026年11月全球碳计划预计2026年化石CO2排放下降约0.4%（受伊朗冲突能源冲击）。证据方向相互矛盾，且书中说的是持续增加到约2040年的轨迹，单年数据不足以判断。  
  来源：<https://globalcarbonbudget.org/fossil-fuel-co2-emissions-hit-record-high-in-2025/>；<https://www.carbonbrief.org/analysis-fossil-fuel-co2-emissions-set-to-dip-in-2026-as-iran-conflict-hits-oil-use>
- **#14** 「Peak oil occurs in the mid-2040s.」  
  判断：**暂无法判断**。石油需求2040年代中期见顶：IEA WEO 2025的情景分歧很大（现行政策情景到2050年不见顶，既定政策情景约2030年前后见顶），都是预测；终点在2040年代，无法判断。  
  来源：<https://www.iea.org/reports/world-energy-outlook-2025/overview-and-key-findings>
- **#15** 「the growth contribution of the trend working-age population component, currently around 1.2 pp, declines stead…」  
  判断：**暂无法判断**。劳动年龄人口对全球增长贡献2080年代初转负；终点在2030年代以后（或长期情景），观察窗口仅约14个月（2025-09至2026-11），无法判断。  
  来源：—
- **#16** 「In the OECD area, annual growth in potential output per capita is projected to average 1½ per cent to 2050」  
  判断：**暂无法判断**。OECD人均潜在产出到2050年年均1½%；终点在2030年代以后（或长期情景），观察窗口仅约14个月（2025-09至2026-11），无法判断。  
  来源：—
- **#17** 「Projected average annual growth rates exceed 2% in a few countries (Chile, Costa Rica, Estonia, Greece, Lithua…」  
  判断：**暂无法判断**。智利等国2025–2050年人均增速超2%：OECD 2026年6月展望预计智利2026年GDP增速放缓到1.7%、2027年回升至2.5%，只是短期数据，终点在2030年代以后（或长期情景），观察窗口仅约14个月（2025-09至2026-11），无法判断。  
  来源：<https://www.oecd.org/en/publications/2026/06/oecd-economic-outlook-volume-2026-issue-1_8be0dba6/full-report/chile_670cc596.html>
- **#19** 「Growth in per capita potential output is substantially stronger in the G20 emerging economies than in the adva…」  
  判断：**暂无法判断**。2025–2050年G20新兴经济体人均增速年均2.6%、明显高于发达经济体：世界银行称2021–25年发达经济体人均GDP约增13%、新兴与发展中经济体整体复苏更弱，但这是全体EMDE而非G20新兴经济体，口径不符；终点2050，无法判断。  
  来源：<https://blogs.worldbank.org/en/developmenttalk/the-post-pandemic-recovery--stronger-than-expected--but-not-for->
- **#20** 「At the global level, annual trend labour efficiency growth is projected to average 1.3% to 2050」  
  判断：**暂无法判断**。全球趋势劳动效率年均1.3%至2050；终点在2030年代以后（或长期情景），观察窗口仅约14个月（2025-09至2026-11），无法判断。  
  来源：—
- **#21** 「By construction, these momentum components are assumed to taper off over time, implying a gradual improvement …」  
  判断：**暂无法判断**。多数OECD国家趋势劳动效率增速逐步改善：书中说明这是模型"按构造"的假设；OECD生产率汇编2026称2024年OECD劳动生产率增1.2%、是2023年的两倍，但这是实际值而非趋势值，单年波动不能判定趋势，无法判断。  
  来源：<https://www.oecd.org/en/publications/oecd-compendium-of-productivity-indicators-2026_734a5e68-en/full-report/productivity-growth-in-a-challenging-global-environment_d888e417.html>
- **#22** 「In the G20 emerging-market economies annual trend labour efficiency growth is projected to average 2.1% to 205…」  
  判断：**暂无法判断**。G20新兴经济体趋势劳动效率年均2.1%至2050；终点在2030年代以后（或长期情景），观察窗口仅约14个月（2025-09至2026-11），无法判断。  
  来源：—
- **#23** 「As for many OECD countries, this implies rising trend labour efficiency growth as the negative momentum effect…」  
  判断：**暂无法判断**。撒哈拉以南非洲趋势劳动效率增速上升：世界银行称该地区2025年GDP增速升至约4.0%，但这不是劳动效率趋势指标，而且是长期模型假设，无法判断。  
  来源：<https://thedocs.worldbank.org/en/doc/7ce50b5aa95bef66048680bba9926ec8-0050012026/related/GEP-Jan-2026-Regional-Highlights-SSA.pdf>
- **#25** 「The standard of living of the median OECD country progresses from 66% of the benchmark US level in 2025 to 73%…」  
  判断：**暂无法判断**。OECD中位国家相对美国生活水平到2050年升至73%；终点在2030年代以后（或长期情景），观察窗口仅约14个月（2025-09至2026-11），无法判断。  
  来源：—
- **#26** 「a country’s standard of living may barely converge toward the US level between 2025 and 2050 or even diverge s…」  
  判断：**暂无法判断**。欧元区与美国生活水平2025–2050年几乎不趋同或略有拉大：2025年欧元区GDP增1.4%，美国四个季度累计增2.0%，两者口径不同（年均与四季度同比），也不是人均数据；一年数据无法判断25年的趋同趋势。  
  来源：<https://www.eunews.it/en/2026/03/06/gdp-grows-in-all-eu-countries-in-2025-with-ireland-leading-at-12-3-per-cent/>；<https://www.govinfo.gov/content/pkg/ERP-2026/pdf/ERP-2026-chapter14.pdf>
- **#27** 「By 2100, living standards in Denmark, Iceland, the Netherlands and Sweden are projected to surpass those in th…」  
  判断：**暂无法判断**。北欧国家与荷兰到2100年生活水平超过美国；终点在2030年代以后（或长期情景），观察窗口仅约14个月（2025-09至2026-11），无法判断。  
  来源：—
- **#28** 「Conversely, in Ireland, Luxembourg and Switzerland, living standards converge toward those of the US from abov…」  
  判断：**暂无法判断**。爱尔兰、卢森堡、瑞士从上方向美国收敛属长期情景；终点在2030年代以后（或长期情景），观察窗口仅约14个月（2025-09至2026-11），无法判断。  
  来源：—
- **#29** 「Among broad regions, East Asia and Pacific, Europe and Central Asia, Latin America and the Caribbean and South…」  
  判断：**暂无法判断**。多个地区到2100年向美国靠近10–20个百分点；终点在2030年代以后（或长期情景），观察窗口仅约14个月（2025-09至2026-11），无法判断。  
  来源：—
- **#30** 「By contrast, the Middle East and North Africa and Sub-Saharan Africa are held back by slower convergence speed…」  
  判断：**暂无法判断**。中东北非和撒哈拉以南非洲趋同受限，为长期情景，无法判断。  
  来源：—
- **#32** 「By 2050, cumulative output losses amount to about 4% at the global level」  
  判断：**暂无法判断**。2050年全球产出损失约4%；终点在2030年代以后（或长期情景），观察窗口仅约14个月（2025-09至2026-11），无法判断。  
  来源：—
- **#33** 「In the alternative baseline scenario BAU2, identical to BAU1 except for the alternative damage curve, climate …」  
  判断：**暂无法判断**。高损害情景2050年损失17%：条件为模型参数，无法观察。  
  来源：—
- **#35** 「It seems reasonable to suppose that technological progress will be the dominant factor and will gradually flat…」  
  判断：**暂无法判断**。技术进步逐步压平减排成本曲线：IRENA称2025年光伏度电成本保持在每兆瓦时44美元、与2024年持平，陆上风电降至33美元，可再生能源成本"趋于稳定"；2026年组件价格又因上游成本和关税上涨。证据有正有反，而且是长期命题，无法判断。  
  来源：<https://www.irena.org/Publications/2026/Jul/Renewable-Power-Generation-Costs-in-2025>；<https://www.pv-magazine.com/2026/08/28/china-topcon-solar-module-prices-rise-on-upstream-cost-pressure-as-deals-lag-offers/>
- **#36** 「While population growth is projected to decline in both blocks, the growth discrepancy is projected to persist…」  
  判断：**暂无法判断**。2070年世界大部分人口位于新增经济体；终点在2030年代以后（或长期情景），观察窗口仅约14个月（2025-09至2026-11），无法判断。  
  来源：—
- **#37** 「It is natural to expect the collective economic weight of this new block to increase over time, purely on demo…」  
  判断：**暂无法判断**。新增经济体占全球经济比重上升，无明确时点且缺少可比口径数据，无法判断。  
  来源：—
- **#38** 「the global aggregate employment rate is projected to rise by 5 percentage points through 2100」  
  判断：**暂无法判断**。全球就业率到2100年上升5个百分点：FRED/ILO显示2025年世界就业人口比约58.06%，只是起点数据，终点在2030年代以后（或长期情景），观察窗口仅约14个月（2025-09至2026-11），无法判断。  
  来源：<https://fred.stlouisfed.org/series/SLEMPTOTLSPZSWLD>
- **#40** 「In the East Asia and Pacific region, trend labour efficiency growth continues to slow but remains well above t…」  
  判断：**暂无法判断**。东亚太平洋趋势劳动效率增速继续放缓但高于1%：世界银行2025年10月称该地区GDP增速放缓，但没有趋势劳动效率数据；属长期情景，无法判断。  
  来源：<https://www.worldbank.org/en/publication/east-asia-and-pacific-economic-update-october-2025>
- **#41** 「In all other regions, and at the global level, trend labour efficiency growth strengthens initially before con…」  
  判断：**暂无法判断**。其他地区与全球趋势劳动效率增速先走强：没有检索到窗口内全球趋势劳动效率的可比数据，无法判断。  
  来源：—
- **#42** 「Projected trend labour efficiency growth remains below the global average until the mid-2040s.」  
  判断：**暂无法判断**。撒哈拉以南非洲趋势劳动效率到2040年代中期低于全球平均；终点在2030年代以后（或长期情景），观察窗口仅约14个月（2025-09至2026-11），无法判断。  
  来源：—
- **#43** 「Even with its projected upturn, trend labour efficiency in Sub-Saharan Africa would remain below 20% of the US…」  
  判断：**暂无法判断**。2100年撒哈拉以南非洲劳动效率低于美国的20%；终点在2030年代以后（或长期情景），观察窗口仅约14个月（2025-09至2026-11），无法判断。  
  来源：—
- **#44** 「At the global level, the investment share of GDP is projected to decline by about 5 pp by 2100.」  
  判断：**暂无法判断**。全球投资率到2100年下降约5个百分点；终点在2030年代以后（或长期情景），观察窗口仅约14个月（2025-09至2026-11），无法判断。  
  来源：—
- **#45** 「By the mid-2040s, Sub-Saharan African is projected to have the highest investment rate across regions」  
  判断：**暂无法判断**。撒哈拉以南非洲到2040年代中期投资率最高；终点在2030年代以后（或长期情景），观察窗口仅约14个月（2025-09至2026-11），无法判断。  
  来源：—
- **#46** 「In the East Asia and Pacific, and South Asia, investment rates are at initially high levels, implying continue…」  
  判断：**暂无法判断**。东亚太平洋与南亚资本产出比中期继续上升，缺少窗口内可比数据，无法判断。  
  来源：—
- **#47** 「gaps with the United States still remain substantial by 2100, except in Europe and Central Asia which reaches …」  
  判断：**暂无法判断**。欧洲中亚到2100年达到美国生活水平的70%以上；终点在2030年代以后（或长期情景），观察窗口仅约14个月（2025-09至2026-11），无法判断。  
  来源：—
- **#48** 「Some countries show a decline, or little change, in relative living standards by 2050, but an increase by 2100…」  
  判断：**暂无法判断**。意大利相对美国生活水平到2050年下降；终点在2030年代以后（或长期情景），观察窗口仅约14个月（2025-09至2026-11），无法判断。  
  来源：—
- **#49** 「Some countries with living standards initially below those of the United States match or surpass it by 2100 (e…」  
  判断：**暂无法判断**。爱沙尼亚到2100年追平或超过美国；终点在2030年代以后（或长期情景），观察窗口仅约14个月（2025-09至2026-11），无法判断。  
  来源：—
- **#50** 「Economic damages in the median country rise from about 2% today to 8.4% of output by 2100」  
  判断：**暂无法判断**。中位国家气候损失到2100年为8.4%；终点在2030年代以后（或长期情景），观察窗口仅约14个月（2025-09至2026-11），无法判断。  
  来源：—
- **#51** 「The least affected country (Iceland) shows little damage, whereas the most affected country (Niger) loses 17% …」  
  判断：**暂无法判断**。2100年尼日尔损失17%、冰岛几乎无损；终点在2030年代以后（或长期情景），观察窗口仅约14个月（2025-09至2026-11），无法判断。  
  来源：—

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/oecd-global-long-run-economic-scenarios-2025-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/oecd-global-long-run-economic-scenarios-2025-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/oecd-global-long-run-economic-scenarios-2025-v5/audit/manual_review_2026-11-15.py`

## 说明

- 抽取密度：71 个 chunk 中有 51 条可解析预测（约每 chunk 0.72 条，每 10 万字符约 21 条），高于英文书 0.2–0.35 的参考值。原因是本书是预测密集的情景报告，“主要发现”和各章 BAU 情景段几乎每段都给出带年份的预测数字；已对重复表述去重。
- ET 与 BAU2（高损害曲线）等情景条件下的数字（#6、#7、#33）按条件句处理，条件未成立或不可观察，记暂无法判断。
- 趋势符合只用于窗口内方向已被存档证据明确证实、但数值或终点尚未到期的条目。

