# 国际能源署《能源与人工智能》（Energy and AI，2025）：出版后预测人工核查

- 案例目录：`cases/iea-energy-and-ai-v5/`
- 出版日期：国际能源署（IEA）**2025 年 4 月 10 日**发布（PDF CreationDate 2025-04-10），按 2025-04 起算。正文用 `reading-library/2026-11-15-未来判断扩展100本/05-技术与科学/077-energy-and-ai.pdf`（sha256 `2c9fbc54…a24dbec51d`，与 IEA 官网 PDF 一致），经 `pdftotext -enc UTF-8` 生成 TXT（sha256 `d3d4afc2…be0c51b1`，777,649 字符；TXT 不入库）。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

本稿按 METHOD.md 复刻 DeepSeek 流水线，只把模型调用换成助手人工阅读。抽取：用仓库 prepare_book v5（toolkit 来自 main `85e6da1`）把全文切成 225 块（3500 字符、600 字符上下文），助手逐块通读，按 DISCOVER_PROMPT_V5 写出模型本应返回的 JSON（可为空），再由仓库代码完成引文对齐、非预测筛除、归属降级和去重：75 条人工抽取项中 3 条被确定性规则按“historical”筛除，得到 72 条候选，全部可核验（resolvable）。核验：选出 22 条在窗口内可能观测的候选，先定 scope，用 Exa 各做一次 support/counter 检索，只从检索返回的 URL 中选源，存档到 `data/sources/`（sha256），写入 `data/evidence.jsonl`；其余以 2030/2035 为终点的情景预测和无可观测指标的定性判断记暂无法判断。再经 `pipeline.py apply assess → check → report`。本稿由助手逐条对照书中原文与存档证据人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 72 条，剔除非预测 0 条，计入 **72 条预测**，其中 **21 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 10 |
| 趋势符合 | 6 |
| 部分符合 | 4 |
| 错误 | 1 |
| 暂无法判断 | 51 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **47.6%**（10/21） |
| 加权胜率 | **78.6%** |
| 错误率 | **4.8%**（1/21） |
| 未定占比（暂无法判断/预测） | 70.8%（51/72） |

## 总体评价

这是一份 2025 年 4 月发布的情景展望，绝大多数预测以 2030 年、2035 年为终点，到截止日只过去约 19 个月，所以 72 条预测中 51 条暂无法判断。可判定的 21 条中，10 条正确：工业自动化继续加深、AI/数据中心成为半导体需求主要驱动、模型效率持续提升、便宜模型带来更多使用和算力（反弹效应）、印度数据中心快速增长、美中欧仍是最大数据中心地区、化石燃料在一次能源中的占比下降（2025 年 86%，为历史最低）、SPE 与阿美合作的行业 LLM 开放授权、AI 天气预报与物理模式并行而非取代、科技公司在能源部门的角色加大。6 条趋势符合：数据中心用电 2025 年增约 17%，快于 2030 年翻倍所需速度（执行摘要和正文各抽到一次，共 2 条）；燃气轮机交货排到 2029—2030 年；联网设备增速快于翻倍路径；数据中心投资 2025 年超过 5800 亿美元、2026 年有望超过 1 万亿美元（2 条）。4 条部分符合：约 20% 数据中心项目面临延误（实际估计为 30%—50%，量级被低估）、端侧推理有增长但负载仍以云端为主、天然气在美国数据中心自建电源中占优但电网增量以太阳能为主、电力占比上升但没有加速。1 条错误：AI 在近期加快设备更换周期（窗口内换机主要由 Windows 10 停服驱动，手机持有周期反而延长）。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（10 条）

- **#12** 「The industry of the future will be increasingly digitalised and automated」  
  判断：**正确**。IFR统计2025年全球工业机器人安装量首次超过60万台、运行存量增长9%至创纪录的500万台，工业自动化在窗口内继续加深。  
  来源：<https://ifr.org/news/five-million-robots-now-operate-in-factories-globally/>
- **#15** 「data centres and especially AI are expected to be the key drivers of semiconductor demand in the years to come…」  
  判断：**正确**。WSTS统计2025年全球半导体销售增长26%至7956亿美元，德勤等指出增长主要由AI基础设施/数据中心推动；BNP提醒2026年增长部分来自涨价和工业补库，但AI/数据中心仍是关键驱动。  
  来源：<https://www.wsts.org/76/103/Global-Semiconductor-Market-grows-26-in-2025-to-796B>；<https://www.deloitte.com/us/en/insights/industry/technology/technology-media-telecom-outlooks/semiconductor-industry-outlook.html>；<https://cib.bnpparibas/semiconductor-market-2026-it-is-not-solely-about-ai/>
- **#16** 「substantial progress has been made in making models more efficient, and this is certain to continue」  
  判断：**正确**。Epoch AI（2026-09）测算过去三年同等性能AI的成本每季度下降约47%，模型效率在窗口内持续快速提升；反证（彭博2025-12）显示推理模型单次耗电更高，但不否定同等性能效率提升。  
  来源：<https://epoch.ai/publications/the-plunging-price-of-thought>；<https://www.bloomberg.com/news/articles/2025-12-04/the-rise-of-ai-reasoning-models-comes-with-a-big-energy-tradeoff>
- **#17** 「cheaper, more efficient models are likely not only to incentivise greater use but also more compute use to imp…」  
  判断：**正确**。Silicon Data指数显示单个token价格自2023年降逾90%而LLM支出仍翻倍；Dell’Oro统计2025年数据中心资本开支增长57%，更便宜的模型带来更多使用与更多算力投入。  
  来源：<https://finance.yahoo.com/technology/ai/articles/tokens-getting-cheaper-companies-spending-185229986.html>；<https://www.prnewswire.com/news-releases/data-center-capex-surges-57-percent-in-2025-as-ai-deployments-accelerate-according-to-delloro-group-302715242.html>
- **#22** 「However, the sector appears poised for rapid growth.」  
  判断：**正确**。印度2025年新增数据中心容量387MW IT，较2024年的191MW翻倍；2026年上半年再新增约258MW、同比增59%，行业在窗口内快速增长。  
  来源：<https://ddnews.gov.in/en/indias-data-centre-capacity-more-than-doubled-in-2025/>；<https://www.savills.in/research_articles/165611/237969-0>
- **#31** 「The United States, China and Europe are projected to remain the largest regions for data」  
  判断：**正确**。Synergy（2025-07）显示北弗吉尼亚和北京地区占全球超大规模容量约20%、美国占比最高；Visual Capitalist汇总显示美国、欧洲、中国为装机最大的地区，窗口内仍为三大地区。  
  来源：<https://www.srgresearch.com/articles/synergy-updates-its-ranking-of-the-worlds-top-20-hyperscale-data-center-locations>；<https://www.visualcapitalist.com/data-center-capacity-around-the-world/>
- **#54** 「fossil fuels still dominate primary energy supply, but their share is set to decline」  
  判断：**正确**。能源研究所《世界能源统计年鉴2026》显示2025年化石燃料占一次能源86%，为历史最低（Carbon Brief）；IER强调仍为86%，但份额下降方向成立。  
  来源：<https://www.carbonbrief.org/six-charts-show-how-clean-power-was-worlds-largest-source-of-new-energy-in-2025>；<https://www.instituteforenergyresearch.org/fossil-fuels/fossil-fuels-dominate-global-energy-supply-in-2025/>
- **#57** 「The Society of Petroleum Engineers, in collaboration with Aramco for financing, is delivering its catalogue of…」  
  判断：**正确**。JPT（SPE，2026-09）称EnRG-LLM在2025年进入会员测试后不久即开放给油气公司授权使用，预测的商业可用已实现（但需求不及预期）。  
  来源：<https://jpt.spe.org/industry-executives-offer-practical-advice-on-how-to-use-modern-ai-models-wisely>；<https://jpt.spe.org/curiosity-meets-comprehension-how-energy-llm-is-bridging-knowledge-gaps>
- **#59** 「AI methods will probably complement rather than replace physics-based numerical weather prediction in the」  
  判断：**正确**。ECMWF在2025年2月和7月先后让AIFS单一与集合AI预报投入业务运行，均与传统物理模式IFS并行，AI补充而非取代数值预报。  
  来源：<https://www.ecmwf.int/en/about/media-centre/news/2025/ecmwfs-ensemble-ai-forecasts-become-operational>；<https://www.ecmwf.int/en/about/media-centre/news/2025/ecmwfs-ai-forecasts-become-operational>
- **#68** 「In the medium term, the digital sector will play a greater role in the energy sector as demand」  
  判断：**正确**。Alphabet于2025-12以47.5亿美元收购清洁能源开发商Intersect；Meta在一年内出资建设至少十几座燃气电厂，数字/科技部门在能源部门的角色在窗口内明显加大。  
  来源：<https://www.reuters.com/technology/alphabet-buy-data-center-infrastructure-firm-intersect-475-billion-deal-2025-12-22/>；<https://techcrunch.com/2026/07/23/meta-drops-out-of-a-major-clean-energy-pact-as-its-natural-gas-buildout-accelerates/>

### 趋势符合（6 条）

- **#1** 「Data centre electricity consumption is set to more than double to around 945 TWh by 2030.」  
  判断：**趋势符合**。第三方（CFA Institute 2026-08）引用的估计显示全球数据中心用电从2024年约415TWh升至2025年约485TWh（约+17%），快于到2030年翻倍所需的约12%年增速；终点2030年未到，方向持续符合。  
  来源：<https://www.cfainstitute.org/insights/articles/data-centers-driving-alternative-energy-investment>；<https://www.iea.org/news/data-centre-electricity-use-surged-in-2025-even-with-tightening-bottlenecks-driving-a-scramble-for-solutions>
- **#18** 「In the Base Case, electricity consumption from data centres rises to around 945 TWh by 2030, more than doublin…」  
  判断：**趋势符合**。与第1条同一预测（正文重复）：2025年全球数据中心用电约485TWh、较2024年增约17%，增速快于2030年翻倍路径；终点未到。  
  来源：<https://www.cfainstitute.org/insights/articles/data-centers-driving-alternative-energy-investment>；<https://www.iea.org/news/data-centre-electricity-use-surged-in-2025-even-with-tightening-bottlenecks-driving-a-scramble-for-solutions>
- **#37** 「The uptick in activity has meant that other elements of supply chains, including labour and other goods, are a…」  
  判断：**趋势符合**。大型燃气轮机交货期已排至2029-2030年（Turbomachinery），GE Vernova积压约116GW、相当于数年产能（East Daley）；新燃气电厂投运推迟的方向已明确，是否推迟到2030年后尚待观察。  
  来源：<https://www.turbomachinerymag.com/view/steam-turbines-gas-turbine-bottleneck-siemens-energy>；<https://eastdaley.com/daley-note/get-in-line-turbine-delays-stall-demand-growth-in-gas-market>
- **#56** 「the number of connected devices is set to double from 2024 to 2030」  
  判断：**趋势符合**。IoT Analytics统计2025年联网IoT设备增长14%至211亿台，高于2024-2030年翻倍所需的约12%年增速；蜂窝IoT增速放缓至13%，终点未到，方向符合。  
  来源：<https://iot-analytics.com/number-connected-iot-devices/>；<https://iot-analytics.com/cellular-iot-market-update-spring-2026/>
- **#65** 「Cumulative data centre investment totals USD 4.2 trillion to 2030 in the Base Case.」  
  判断：**趋势符合**。2025年全球数据中心投资超过5800亿美元（Colliers），Dell’Oro预计2026年资本开支超过1万亿美元；按此路径2025-2030年累计4.2万亿美元的方向成立，终点未到。  
  来源：<https://www.datacenterdynamics.com/en/news/colliers-data-center-investment-tops-580-billion-beating-oil-investment-for-the-first-time/>；<https://convergedigest.com/delloro-ai-infrastructure-spending-pushes-2026-data-center-capex-above-1-trillion/>
- **#69** 「albeit at a slower rate, surpassing USD 800 billion per annum before 2030 to accommodate」  
  判断：**趋势符合**。Dell’Oro称2026年全球数据中心资本开支有望超过1万亿美元，2026年二季度同比增长92%；超过每年8000亿美元已接近实现，但全年数据尚未出，暂记趋势符合。  
  来源：<https://convergedigest.com/delloro-ai-infrastructure-spending-pushes-2026-data-center-capex-above-1-trillion/>；<https://www.prnewswire.com/news-releases/data-center-capex-grew-92-percent-in-2q-2026-driven-by-surging-ai-demand-and-memory-costs-according-to-delloro-group-302879910.html>

### 部分符合（4 条）

- **#10** 「we estimate that unless these risks are addressed, around 20% of planned data centre projects could be at risk…」  
  判断：**部分符合**。Sightline Climate/Currence等第三方估计2026年计划投运的大型数据中心容量有30%-50%可能延误，延误风险确实兑现且风险未被消除；但比例明显高于书中“约20%”，量级不符。  
  来源：<https://www.networkworld.com/article/4201941/up-to-50-of-data-center-capacity-slated-for-2026-could-be-delayed.html>；<https://www.axios.com/2026/02/24/ai-data-center-boom-projects-numbers>
- **#21** 「some AI inferencing workloads could move from data centres to end-user devices such as mobile phones and lapto…」  
  判断：**部分符合**。端侧推理在窗口内确有增长（NPU手机/AI PC），但Futurum指出多数助手与智能体体验仍依赖云端，推理负载并未明显从数据中心转出，仅部分符合。  
  来源：<https://rcrtech.com/semiconductor-news/ai-is-shifting-to-the-edge/>；<https://futurumgroup.com/press-release/ai-capable-devices-slow-to-deliver-on-cloudless-agentic-ai-experiences/>
- **#46** 「Natural gas is set to continue to dominate the near-term data centre」  
  判断：**部分符合**。Axios（2026-02）称燃气是数据中心自建电源的明显赢家；但Ember显示2025年美国新增用电需求的61%由太阳能满足，电网层面增量并非燃气主导，只部分符合。  
  来源：<https://www.axios.com/2026/02/04/ai-natural-gas-power-data-centers>；<https://ember-energy.org/latest-updates/solar-met-61-of-us-electricity-demand-growth-in-2025/>
- **#55** 「The overall share of total final energy consumption met by electricity has been steadily rising and is project…」  
  判断：**部分符合**。2025年全球电力需求增长约3.0%，快于能源总供应的1.7%，电力份额继续上升；但电力需求增速从2024年的4.4%放缓至约2.8%-3%，“加速”未出现。  
  来源：<https://ember-energy.org/latest-insights/energy-institute-statistical-review-of-world-energy/>；<https://asian-power.com/news/global-electricity-demand-hits-record-31779-twh-in-2025-growth-pace-eases>

### 错误（1 条）

- **#35** 「could accelerate device replacement cycles in the near term」  
  判断：**错误**。窗口内PC换机主要由Windows 10停服驱动（Gartner），Constellation称AI PC换机周期“爬行”；手机持有周期反而延长（Kadence），未见AI加速设备更换。  
  来源：<https://www.constellationr.com/insights/news/ai-pc-upgrade-cycle-crawling-amid-murky-value>；<https://www.gartner.com/en/newsroom/press-releases/2025-10-16-gartner-says-worldwide-pc-shipments-grew-8-percent-in-third-quarter-of-2025>；<https://kadence.com/en-us/knowledge/why-tech-buyers-are-saying-not-yet/>

### 暂无法判断（51 条）

- **#2** 「In the United States, data centres account for nearly half of electricity demand growth between now and 2030.」  
  判断：**暂无法判断**。预测终点（2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。  
  来源：—
- **#3** 「By the end of the decade, the country is set to consume more electricity for data centres than for the product…」  
  判断：**暂无法判断**。预测终点（By the end of the decade）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。  
  来源：—
- **#4** 「our Base Case sees global data centre electricity consumption rising to around 1 200 TWh by 2035.」  
  判断：**暂无法判断**。预测终点（by 2035）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。  
  来源：—
- **#5** 「Renewables generation is projected to grow by over 450 TWh to meet data centre demand to 2035」  
  判断：**暂无法判断**。预测终点（to 2035）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。  
  来源：—
- **#6** 「Natural gas expands by 175 TWh to meet growing data centre demand, notably in the United States.」  
  判断：**暂无法判断**。表述为无具体指标的方向性/定性判断，或依赖情景模型的长期结果，在2025-04至2026-11的短窗口内缺少可判定的公开观测，暂无法判断。  
  来源：—
- **#7** 「The first small modular reactors come online around 2030.」  
  判断：**暂无法判断**。预测终点（around 2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。  
  来源：—
- **#8** 「Data centres account for around one-tenth of global electricity demand growth to 2030」  
  判断：**暂无法判断**。预测终点（to 2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。  
  来源：—
- **#9** 「In this group of countries, data centres account for more than 20% of demand growth to 2030」  
  判断：**暂无法判断**。预测终点（to 2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。  
  来源：—
- **#11** 「By 2035, the range of data centre electricity demand across our cases spans from 700 to 1 700 TWh.」  
  判断：**暂无法判断**。预测终点（By 2035）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。  
  来源：—
- **#13** 「Our estimates indicate that in 2030, demand for gallium for data centres could reach over 10% of today's suppl…」  
  判断：**暂无法判断**。预测终点（in 2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。  
  来源：—
- **#14** 「Emissions from electricity use by data centres grows from 180 million tonnes (Mt) today to 300 Mt in the Base …」  
  判断：**暂无法判断**。预测终点（by 2035）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。  
  来源：—
- **#19** 「The United States sees by far the largest absolute growth, followed by China and Europe.」  
  判断：**暂无法判断**。预测终点（2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。  
  来源：—
- **#20** 「Efficiency improvements are expected to continue playing a pivotal role in limiting strong growth in energy co…」  
  判断：**暂无法判断**。表述为无具体指标的方向性/定性判断，或依赖情景模型的长期结果，在2025-04至2026-11的短窗口内缺少可判定的公开观测，暂无法判断。  
  来源：—
- **#23** 「over 2 GW of further maximum designed capacity is in the pipeline and planned to come online over the next two…」  
  判断：**暂无法判断**。书中“两年内上线逾2GW（最大设计容量）”终点约为2027年4月；窗口内实际新增IT容量约650MW（2025年387MW+2026年上半年258MW），步伐明显偏慢，但口径（设计容量与IT负载）不同且终点未到，暂无法判断。  
  来源：—
- **#24** 「This means that total installed capacity is on track to reach nearly 5 GW by 2030」  
  判断：**暂无法判断**。预测终点（by 2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。  
  来源：—
- **#25** 「the dominance of coal in the mix is likely to continue beyond 2030」  
  判断：**暂无法判断**。预测终点（2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。  
  来源：—
- **#26** 「while coal dominates the electricity mix in India, the share of renewables increases to 35% by then」  
  判断：**暂无法判断**。预测终点（2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。  
  来源：—
- **#27** 「The total stock of servers is projected to increase by more than 60% by 2030」  
  判断：**暂无法判断**。预测终点（by 2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。  
  来源：—
- **#28** 「In the Base Case, the total installed capacity of data centres more than doubles from around」  
  判断：**暂无法判断**。预测终点（2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。  
  来源：—
- **#29** 「The global weighted average PUE is projected to improve, decreasing from 1.41 to 1.29 on average」  
  判断：**暂无法判断**。预测终点（2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。  
  来源：—
- **#30** 「conventional servers are expected to see significant efficiency improvements over the next decade」  
  判断：**暂无法判断**。预测终点（over the next decade）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。  
  来源：—
- **#32** 「electricity demand from data centres is expected to more than double by 2030」  
  判断：**暂无法判断**。预测终点（by 2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。  
  来源：—
- **#33** 「In China it increases by around 175 TWh (up 170%).」  
  判断：**暂无法判断**。预测终点（2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。  
  来源：—
- **#34** 「the shift towards AI inference at the edge is likely to reduce energy use in data centres with only a limited …」  
  判断：**暂无法判断**。表述为无具体指标的方向性/定性判断，或依赖情景模型的长期结果，在2025-04至2026-11的短窗口内缺少可判定的公开观测，暂无法判断。  
  来源：—
- **#36** 「AI is unlikely to have a noticeable impact on network energy use, especially」  
  判断：**暂无法判断**。表述为无具体指标的方向性/定性判断，或依赖情景模型的长期结果，在2025-04至2026-11的短窗口内缺少可判定的公开观测，暂无法判断。  
  来源：—
- **#38** 「Global electricity generation to supply data centres is projected to grow from 460 TWh in」  
  判断：**暂无法判断**。预测终点（2030、2035）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。  
  来源：—
- **#39** 「renewables remain the fastest-growing source of electricity for data centres」  
  判断：**暂无法判断**。预测终点（2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。  
  来源：—
- **#40** 「Natural gas and coal together are expected to meet over 40% of the additional electricity demand」  
  判断：**暂无法判断**。预测终点（2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。  
  来源：—
- **#41** 「the resulting increase in nuclear electricity generation leads to an absolute decline in coal-fired generation…」  
  判断：**暂无法判断**。预测终点（by 2035）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。  
  来源：—
- **#42** 「CO2 emissions from electricity generation for data centres peak at around 320 Mt CO2 by」  
  判断：**暂无法判断**。预测终点（2030、2035）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。  
  来源：—
- **#43** 「natural gas is the largest source of additional supply, adding over 130 TWh of annual generation until 2030.」  
  判断：**暂无法判断**。预测终点（until 2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。  
  来源：—
- **#44** 「adding 110 TWh to data centre electricity supply between 2024 and 2030.」  
  判断：**暂无法判断**。预测终点（between 2024 and 2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。  
  来源：—
- **#45** 「sources account for over 55% of the US data centre electricity supply mix」  
  判断：**暂无法判断**。预测终点（2035）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。  
  来源：—
- **#47** 「both coal and renewables – mostly solar PV and wind – add about 90 TWh to the data centre」  
  判断：**暂无法判断**。预测终点（2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。  
  来源：—
- **#48** 「By 2035, both sources together make up 60% of China’s data centre electricity supply」  
  判断：**暂无法判断**。预测终点（By 2035）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。  
  来源：—
- **#49** 「In Europe, renewables and nuclear are set to supply most of the additional electricity required, with their co…」  
  判断：**暂无法判断**。预测终点（by 2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。  
  来源：—
- **#50** 「In both regions, coal remains a key pillar of the data centre electricity supply, but renewables are projected…」  
  判断：**暂无法判断**。预测终点（by 2035）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。  
  来源：—
- **#51** 「capacity is commissioned between 2030 and 2035, mostly from SMRs in the United States」  
  判断：**暂无法判断**。预测终点（between 2030 and 2035）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。  
  来源：—
- **#52** 「their share of system-wide peak electricity demand is set to increase from 6% today to 13% by 2030」  
  判断：**暂无法判断**。预测终点（by 2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。  
  来源：—
- **#53** 「studies suggest that 30-50% of workloads are delay tolerant, a figure likely to rise with the uptake of AI tra…」  
  判断：**暂无法判断**。表述为无具体指标的方向性/定性判断，或依赖情景模型的长期结果，在2025-04至2026-11的短窗口内缺少可判定的公开观测，暂无法判断。  
  来源：—
- **#58** 「the sector contributes to 70% of peak electricity demand on average in advanced economies, and this share is s…」  
  判断：**暂无法判断**。表述为无具体指标的方向性/定性判断，或依赖情景模型的长期结果，在2025-04至2026-11的短窗口内缺少可判定的公开观测，暂无法判断。  
  来源：—
- **#60** 「The implementation of AI solutions will face regulatory hurdles.」  
  判断：**暂无法判断**。表述为无具体指标的方向性/定性判断，或依赖情景模型的长期结果，在2025-04至2026-11的短窗口内缺少可判定的公开观测，暂无法判断。  
  来源：—
- **#61** 「The desire to preserve some element of human control is likely to persist.」  
  判断：**暂无法判断**。表述为无具体指标的方向性/定性判断，或依赖情景模型的长期结果，在2025-04至2026-11的短窗口内缺少可判定的公开观测，暂无法判断。  
  来源：—
- **#62** 「are likely to remain a major bottleneck in bringing new products to market.」  
  判断：**暂无法判断**。表述为无具体指标的方向性/定性判断，或依赖情景模型的长期结果，在2025-04至2026-11的短窗口内缺少可判定的公开观测，暂无法判断。  
  来源：—
- **#63** 「energy-dense fuels are likely to be indispensable for some use cases, such as aviation.」  
  判断：**暂无法判断**。表述为无具体指标的方向性/定性判断，或依赖情景模型的长期结果，在2025-04至2026-11的短窗口内缺少可判定的公开观测，暂无法判断。  
  来源：—
- **#64** 「However, the recent wave of AI growth is not likely to further accelerate nuclear fusion」  
  判断：**暂无法判断**。预测终点（2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。  
  来源：—
- **#66** 「Data centres are on track to account for 3% of the power sector and 1% of total energy」  
  判断：**暂无法判断**。预测终点（2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。  
  来源：—
- **#67** 「Natural gas demand to power data centres is expected to grow by nearly 35 billion cubic」  
  判断：**暂无法判断**。预测终点（2035）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。  
  来源：—
- **#70** 「Nevertheless, data centres are unlikely to fundamentally alter the environment for」  
  判断：**暂无法判断**。表述为无具体指标的方向性/定性判断，或依赖情景模型的长期结果，在2025-04至2026-11的短窗口内缺少可判定的公开观测，暂无法判断。  
  来源：—
- **#71** 「developing economies excluding China, electricity demand is on track to rise faster than in」  
  判断：**暂无法判断**。十年期相对增速预测；2025年印度能源需求增速仅约1%、美国电力需求增约3.1%，与预测方向相反，但仅一年且受季风天气影响，不足以判断十年结果。  
  来源：—
- **#72** 「560 billion litres per year, and this could rise to around 1200 billion litres per year in 2030」  
  判断：**暂无法判断**。预测终点（2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。  
  来源：—

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/iea-energy-and-ai-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/iea-energy-and-ai-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/iea-energy-and-ai-v5/audit/manual_review_2026-11-15.py`

## 说明

- 前后附文人工排除：`prepare_book` 没有识别出 matter 区段（`excluded_matter_spans=[]`），225 块都进入了抽取。txt-00001—00007（封面、版权、前言/Foreword、致谢、同行评审名单、目录）和 txt-00191 后段起的附录（Annex A 方法与数据表、Annex B 定义与缩略语、Annex C 参考文献，至 txt-00225）按“前后附文不算预测”的规则人工排除，回答为空。附录 A 的数据表只重复正文情景数值，不另行抽取。
- 执行摘要与正文重复的同一判断，大多只保留首次出现；“2030 年约 945 TWh”在执行摘要（第 1 条）和第 2 章（第 18 条）各保留一次，判定相同。Widespread Adoption Case 中“若广泛采用 AI 可节省 X”的潜力数字属于假设情景，不抽取。
- 确定性筛除：3 条人工抽取项（美国数据中心用电较 2024 年增 240 TWh、中国人均数据中心用电将超过欧洲、2024—2035 年新增 320 GW 装机）的引文含 ≤ 出版年的年份，被 `claims_from_results` 的 historical 规则排除，未进入候选。
- 抽取密度约 0.32 条可核验 / 块（72/225），按正文块计约 0.38，处于 METHOD §5 英文书参考区间（约 0.2—0.35）上沿，因为这是以数值情景为主的展望报告。
- 证据尽量用 IEA 以外的第三方来源（WSTS、IFR、Epoch AI、Dell’Oro、Colliers、Energy Institute/Carbon Brief、Ember、IoT Analytics、ECMWF、Gartner、Synergy 等）；第 1/18 条的 2025 年 485 TWh 数字源于 IEA 2026 年更新，经 CFA Institute 转引，已在 limitation 注明。
- 窗口很短（2025-04 → 2026-11-15），胜率样本小，趋势符合多为“2030 年终点未到、方向一致”。
- 案例的 `context` 字段按协调者口径清空。

