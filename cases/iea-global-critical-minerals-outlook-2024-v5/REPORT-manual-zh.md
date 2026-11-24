# 国际能源署《全球关键矿产展望2024》（Global Critical Minerals Outlook 2024）：出版后预测人工核查

- 案例目录：`cases/iea-global-critical-minerals-outlook-2024-v5/`
- 出版日期：2024-05-17
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

按仓库原 DeepSeek 管线逐步操作（pdftotext 转 TXT、3500 字符切块共 137 块、逐块完整通读并按 DISCOVER_PROMPT_V5 手写抽取 JSON、用仓库代码 validate_chunk_predictions + claims_from_results 做确定性后处理），只把模型调用换成助手通读，不使用 DeepSeek API。核验阶段对 107 条可核验候选逐条先写 scope，再各做一次 support/counter 的 Exa 检索，对暂无法判断或证据不足的条目改换策略做第二轮检索，只从检索返回的 URL 中选源，再抓取存档并阅读存档全文后下判断。抽取共得 108 条候选（附录“Key projection results”数值表按“矿种×需求/供应”整表各收 1 条，同一轨迹不按年份或情景拆分计分），其中 1 条为 unclear（作者明言不确定、无方向判断），流水线判为不可核验并剔除；本稿以其余 107 条可核验候选为起点，由助手逐条对照报告原文与存档证据复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 107 条，剔除非预测 2 条，计入 **105 条预测**，其中 **63 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 42 |
| 趋势符合 | 5 |
| 部分符合 | 14 |
| 错误 | 2 |
| 暂无法判断 | 42 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **66.7%**（42/63） |
| 加权胜率 | **83.7%** |
| 错误率 | **3.2%**（2/63） |
| 未定占比（暂无法判断/预测） | 40.0%（42/105） |

## 总体评价

本报告是国际能源署2024年5月发布的关键矿产年度展望，大量判断针对2030、2035、2040年的情景（STEPS/APS/NZE）。截至2026-11-15只过去约两年半，这类长期情景值（需求翻倍、市场价值、2030/2040年集中度等）一律记为暂无法判断，共42条。其中包括第4章回收部分的6条（回收原料结构转变、2030年报废电池量、2040年回收减量、回收率上升、2030年回收产能、2030年原料构成），以及附录数值表的13条（六种矿产的需求与基准供应轨迹），这些条目终点未到或条件未出现。可判定的63条主要是“近期”市场判断：关键矿产需求继续增长，电动车与可再生能源持续扩张，电池价格因产能过剩下降，锂、镍、钴、石墨在2024–2025年供应过剩、价格低迷，低价抑制新项目并导致BHP等停产，精炼环节进一步集中，2020年代中期可再生发电超过煤电，中国锂矿产量超过智利等。这些大多被出版后数据证实。明显说错的有两条：对俄金属禁令并未抑制LME镍库存增长（2024年交易所镍库存增至年初的两倍多）；欧盟电池法规的碳足迹强制披露没有在2025年落地。部分符合主要来自2025年的转折：刚果（金）出口禁令使钴价反弹，铂、钯价格在2025年暴涨，原铝在2025年转为短缺，重稀土出口管制使“总量充足”与“可得性”分离，以及美国风电2024年不升反降。另有2条（印度2024年下调电动车补贴、神行电池2024年装车）在出版日前已经发生，按规则剔除、不计分。由于窗口短、判断多为“近期延续”型，较高的严格胜率不代表其长期情景的准确性。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（42 条）

- **#1** 「Today’s well-supplied market may not be a good guide for the future, as demand for critical minerals continues…」  
  判断：**正确**。IEA《全球关键矿产展望2025》称2024年关键能源矿产需求继续强劲增长：锂需求增近30%，镍、钴、石墨、稀土增6–8%；《2026》亦称2025年需求继续强劲增长。需求上升的判断在窗口内成立。  
  来源：<https://www.iea.org/reports/global-critical-minerals-outlook-2025/executive-summary>；<https://www.iea.org/reports/global-critical-minerals-outlook-2026/market-overview>
- **#3** 「continued growth is projected as major markets progress and adoption increases in emerging economies.」  
  判断：**正确**。IEA《全球电动汽车展望2025》：2024年全球电动汽车销量超过1700万辆、同比增长逾25%；《展望2026》：2025年销量超过2000万辆、增长约20%，新兴经济体采用率上升。“继续增长”成立。  
  来源：<https://www.iea.org/reports/global-ev-outlook-2025/trends-in-electric-car-markets-2>；<https://www.iea.org/reports/global-ev-outlook-2026/trends-in-electric-cars%C2%A0>
- **#12** 「Announced projects indicate that refined material production is set to remain highly concentrated in a few cou…」  
  判断：**正确**。IEA《2025展望》指出2020–2024年精炼与加工的集中度不降反升，铜、锂、镍、钴、石墨、稀土前三大精炼国平均份额由2020年82%升至2024年86%；精炼生产继续高度集中于少数国家。  
  来源：<https://www.iea.org/news/diversification-is-the-cornerstone-of-energy-security-yet-critical-minerals-are-moving-in-the-opposite-direction>；<https://www.iea.org/reports/global-critical-minerals-outlook-2025/executive-summary>
- **#14** 「government unveiled an objective to conduct annual auctions for 50 GW of renewable energy capacity that promis…」  
  判断：**正确**。JMK Research数据：印度2024年新增太阳能24.5GW（超过2023年的两倍、单年最高）、风电3.4GW（增21%）；pv magazine：2025年新增太阳能37.9GW、风电6.3GW再创纪录。可再生能源部署显著加速。  
  来源：<https://economictimes.indiatimes.com/industry/renewables/india-added-24-5-gw-solar-and-3-4-gw-wind-capacity-in-2024-sets-new-records/articleshow/117085849.cms>；<https://www.pv-magazine.com/2026/01/14/india-deploys-37-9-gw-of-solar-in-2025/>
- **#16** 「Overall, the world is poised for a signficant acceleration in renewable capacity in the coming years driven by…」  
  判断：**正确**。IRENA：2024年全球可再生能源新增585GW，创纪录、增速15.1%；IEA《全球能源回顾2026》：2025年新增约800GW、增长16%。可再生能源装机显著加速。  
  来源：<https://www.irena.org/News/articles/2025/Apr/Renewables-in-2024-5-Key-Facts-Behind-a-Record-Breaking-Year>；<https://www.iea.org/reports/global-energy-review-2026/technology-solar-pv-and-wind>
- **#17** 「Renewables are expected to surpass coal to become the largest source of electricity generation」  
  判断：**正确**。Ember《全球电力评论2026》：2025年可再生能源占全球发电33.8%，首次超过煤电；2025年上半年已首次超过煤电。原文同句写明“到2020年代中期”，时间与结果均吻合。  
  来源：<https://ember-energy.org/latest-insights/global-electricity-review-2026/>；<https://ember-energy.org/latest-insights/global-electricity-mid-year-insights-2025/>
- **#18** 「It is estimated that around 45% of all cars sold in China in 2024 could be electric.」  
  判断：**正确**。IEA称2024年中国电动车占新车销量近一半；乘联会零售口径新能源车占比47.6%，中汽协口径新能源车销量1286.6万辆、占40.9%，均与“约45%”相符。  
  来源：<https://evmagazine.com/articles/iea-global-ev-sales-are-soaring-despite-challenges>；<https://www.france24.com/en/live-news/20250109-china-s-electric-and-hybrid-vehicle-sales-jump-40-7-in-2024>；<https://cnevpost.com/2025/01/13/china-nev-sales-dec-2024-caam/>
- **#20** 「As the market matures and subsidies are phased out, growth rates may decrease somewhat.」  
  判断：**正确**。全球电动车销量增速：2024年“逾25%”、2025年约20%（IEA）；BNEF 2024年11月判断“增速放缓但销量仍创新高”。增速有所下降成立。  
  来源：<https://www.iea.org/reports/global-ev-outlook-2025/trends-in-electric-car-markets-2>；<https://www.iea.org/reports/global-ev-outlook-2026/trends-in-electric-cars%C2%A0>；<https://about.bnef.com/insights/finance/are-global-ev-sales-really-slowing-down/>
- **#21** 「However, robust growth in EV sales is still expected to continue in the near and long term」  
  判断：**正确**。2024年全球电动车销量增长逾25%，2025年突破2000万辆、增长约20%；尽管美国2025年下滑，全球仍保持强劲增长。  
  来源：<https://www.iea.org/reports/global-ev-outlook-2025/trends-in-electric-car-markets-2>；<https://www.iea.org/reports/global-ev-outlook-2026/trends-in-electric-cars%C2%A0>
- **#26** 「If excess production is pushed on to export markets, battery prices and EV prices may fall」  
  判断：**正确**。条件成立：BNEF称中国电芯产量一直超过国内电动车和储能需求、几乎供应全球LFP需求；结果成立：锂电池包均价2024年降20%至115美元/kWh、2025年再降8%至108美元/kWh，BNEF点名电芯制造产能过剩与激烈竞争。  
  来源：<https://about.bnef.com/insights/commodities/lithium-ion-battery-pack-prices-see-largest-drop-since-2017-falling-to-115-per-kilowatt-hour-bloombergnef/>；<https://about.bnef.com/insights/clean-transport/lithium-ion-battery-pack-prices-fall-to-108-per-kilowatt-hour-despite-rising-metal-prices-bloombergnef/>
- **#27** 「However, in addition to further rapid acceleration in today’s core markets, capacity growth is expected to bro…」  
  判断：**正确**。BNEF 2025年6月《全球储能增长由新市场支撑》：在中美两大市场变动之际，沙特、南非、澳大利亚、荷兰、智利等地都有大型储能项目投运或开工。储能增长扩散到核心市场之外成立。  
  来源：<https://about.bnef.com/insights/clean-energy/global-energy-storage-growth-upheld-by-new-markets/>
- **#28** 「Lithium-ion battery technology is set to remain a key part of short-duration (eight hours or less) storage」  
  判断：**正确**。Volta Foundation《电池报告2025》：锂离子电池仍占储能电池市场90%以上；IDTechEx亦称锂电占电化学储能装机90%以上。  
  来源：<https://report.volta.foundation/2025/193>；<https://www.idtechex.com/en/research-report/batteries-for-stationary-energy-storage/1021>
- **#29** 「lower price environment, which is likely to continue in 2024.」  
  判断：**正确**。IEA《2025展望》：供应大增使电池金属价格在2024年持续承压；锂、镍、钴价格2024年跌至多年低位。低价环境延续。  
  来源：<https://www.iea.org/reports/global-critical-minerals-outlook-2025/executive-summary>；<https://kleanindustries.com/insights/market-analysis-reports/battery-metal-sector-prices/>
- **#31** 「Limited growth in mined supply is anticipated for 2024.」  
  判断：**正确**。ICSG初步数据：2024年全球铜矿产量仅增长约2.3%（SX-EW增4%），矿产供应增长有限成立。  
  来源：<https://www.scrapmonster.com/news/copper/icsg-world-refined-copper-market-surplus-2024/94964>
- **#34** 「However, a significant price surge in the near term is difficult to envision.」  
  判断：**正确**。近期（2024至2025年中）锂价未出现大幅上涨：Fastmarkets称2024年价格在5美元/kg区间内窄幅波动，2025年5月跌至四年低点；2025年下半年起才因宁德时代矿山停产等出现反弹。近期判断成立。  
  来源：<https://www.fastmarkets.com/uploads/2024/11/Fastmarkets-webinar_BRM-global-outlook_Nov_2024.pdf>；<https://www.fastmarkets.com/uploads/2025/05/Global-Outlook_Webinar_-May_2025-1.pdf>
- **#35** 「the enduring low prices may dampen investment appetite for new greenfield projects」  
  判断：**正确**。路透2024年12月：锂价两年内下跌90%后多座矿山减产或推迟扩产，CRU估计2025年减少22.8万吨产量；Arcadium 2024年8月因低价暂停加拿大、阿根廷部分扩产项目。低价抑制新项目投资成立。  
  来源：<https://www.spglobal.com/energy/en/news-research/latest-news/metals/080724-arcadium-to-pause-some-lithium-expansion-projects-in-canada-argentina-amid-low-prices-ceo>；<https://www.reuters.com/markets/commodities/lithium-mines-that-have-cutback-output-due-low-prices-2024-12-10/>
- **#36** 「prices could remain suppressed given the numerous projects in the pipeline」  
  判断：**正确**。路透：镍价2024年末收于四年低点，印尼过量供应压价；INN：2025年在持续过剩下年终走低；S&P 2026年11月：镍价跌破1.6万美元/吨，全球过剩库存约75万吨。价格持续受压成立。  
  来源：<https://www.reuters.com/markets/commodities/only-indonesia-can-help-nickel-recover-price-bust-andy-home-2025-01-22/>；<https://investingnews.com/daily/resource-investing/base-metals-investing/nickel-investing/nickel-price-update/>；<https://www.spglobal.com/energy/en/news-research/latest-news/metals/110226-indonesia-signals-further-nickel-ore-quota-cuts-as-global-surplus-weighs-on-prices>
- **#37** 「Cobalt prices are expected to remain subdued in 2024 as supply growth continues to outpace demand growth.」  
  判断：**正确**。Fastmarkets：标准级钴价2024年9月跌至年内新低，原因是需求疲弱和持续过剩；Benchmark：洛阳钼业扩产使2024年钴市场出现约3.7万吨的历史性大额过剩。  
  来源：<https://www.fastmarkets.com/insights/cobalt-price-slips-to-new-low-amid-persistent-oversupply/>；<https://source.benchmarkminerals.com/article/cmoc-supply-ramp-up-drives-cobalt-market-to-its-lowest-ebb-cobalt-2024-in-review>
- **#39** 「the current low-price environments could delay projects planned outside China」  
  判断：**正确**。Benchmark 2024年9月：低价下多数稀土矿山难以盈亏平衡，早期项目面临延误和资金缺口，中国以外约半数预期新增供应的16个项目受影响最大；彭博（mining.com转载）称中国控制压低价格，使美日等项目目标难以实现。  
  来源：<https://source.benchmarkminerals.com/article/unsustainable-prices-hit-rare-earths-projects-worldwide>；<https://www.mining.com/web/chinas-grip-on-rare-earths-undercuts-projects-from-us-to-japan/>
- **#40** 「Another area of concern could be tightened supply of HREEs in the medium term.」  
  判断：**正确**。2025年中国对镝、铽等重稀土实施出口管制后，Argus称中国以外受限稀土供应偏紧；路透2025年11月称西方建设磁体供应链时面临镝、铽等重稀土稀缺。中期重稀土供应趋紧成立。  
  来源：<https://www.argusmedia.com/metals-platform/newsandanalysis/article/2685377-China-s-export-controls-fragment-rare-earths-market>；<https://www.reuters.com/sustainability/climate-energy/west-scrambles-fill-heavy-rare-earth-gap-china-rivalry-deepens-2025-11-19/>
- **#41** 「Consequently, this could lead to further geographical concentration of production」  
  判断：**正确**。IEA 2025年：在价格下行期，几乎全部供应增量来自单一头部供应国（印尼镍、中国其他矿种），前三大精炼国平均份额2020–2024年由82%升至86%。集中度进一步提高成立。  
  来源：<https://www.iea.org/reports/global-critical-minerals-outlook-2025/executive-summary>；<https://www.miningweekly.com/article/lack-of-geographic-diversification-in-critical-minerals-supply-a-cause-for-concern-iea-report-shows-2025-05-21>
- **#43** 「In the current lower price and oversupply environment, there is anticipation that China may continue to increa…」  
  判断：**正确**。USGS数据（Measured World整理）：2025年中国锂矿产量6.2万吨、同比增49.8%，超过智利；OilPrice 2025年6月：尽管价格暴跌，中国仍在扩产，预计2026年超过澳大利亚成为最大锂生产国。低价期中国继续扩大供应、夺取份额成立。  
  来源：<https://measuredworld.com/categories/resources/lithium-production>；<https://oilprice.com/Energy/Energy-General/As-Prices-Crash-China-Tightens-Stranglehold-on-Lithium-Supply.html>
- **#45** 「This high level may subside in the near term, however, as consumption picks up」  
  判断：**正确**。上期所铜库存2024年7月12日当周减少1.72%至31.6万吨、降至一个半月新低（文华财经/SMM）；2024年8月报道称铜价受库存下降和需求改善支撑。近期回落成立。  
  来源：<https://news.smm.cn/news/102851784>；<https://energynews.oedigital.com/mineral-resources/2024/08/22/copper-increases-on-falling-stocks-improving-demand>
- **#46** 「In the next year, we expect to see more bilateral agreements and strategic partnerships emerge with a focus on…」  
  判断：**正确**。出版后一年内：2024年9月美国与乌兹别克斯坦签署关键矿产谅解备忘录，2024年10月印美签署关键电池矿产供应链合作协议；2025年10月美澳签署关键矿产与稀土供应框架。双边协议增多成立。  
  来源：<https://www.reuters.com/markets/commodities/india-us-cooperate-critical-battery-minerals-trade-minister-says-2024-10-03/>；<https://gov.uz/en/mingeo/news/view/21761>；<https://www.industry.gov.au/publications/united-states-australia-framework-securing-supply-mining-and-processing-critical-minerals-and-rare-earths>
- **#47** 「Emerging producer countries are also expected to continue signing agreements to boost investment into critical…」  
  判断：**正确**。2025年11月南非与欧盟签署关键矿产协议；同月卡塔尔投资局与艾芬豪矿业在刚果（金）总统会见卡塔尔埃米尔之际签署关键矿产勘探开发谅解备忘录。新兴生产国继续签约引资成立。  
  来源：<https://www.reuters.com/world/china/south-africa-eu-sign-critical-minerals-deal-vow-defend-multilateralism-2025-11-20/>；<https://www.ivanhoemines.com/news-stories/news-release/ivanhoe-mines-and-qatar-investment-authority-qia-announce-memorandum-of-understanding-mou-to-further-exploration-development-and-mining-of-critical-minerals/>
- **#58** 「The tight supply market is likely to increase prices which could support investment in lower-grade plays」  
  判断：**正确**。IEA 2026年3月：铜价2025年12月首次突破1.2万美元/吨，2026年1月盘中超过1.45万美元/吨创纪录，推动因素包括多座大矿供应中断；路透2026年1月：铜价创历史新高。偏紧供应推高价格成立；“支持低品位项目投资”部分未核实。  
  来源：<https://www.iea.org/commentaries/copper-prices-have-hit-record-highs-but-smelters-face-mounting-strategic-pressures>；<https://www.reuters.com/world/china/copper-sets-record-amid-geopolitical-risks-weak-dollar-2026-01-29/>
- **#60** 「Lithium-ion batteries’ role in fuelling the growth of the EV industry remains unchallenged in the near term.」  
  判断：**正确**。IEA 2026年评论：2025年钠离子电池全球产量不足锂离子电池的1%；MIT科技评论2025年6月称钠电池只在电动两轮车和储能等小众领域起步。锂离子电池地位近期未受挑战。  
  来源：<https://www.iea.org/commentaries/sodium-ion-battery-momentum-grows-but-challenges-remain>；<https://www.technologyreview.com/2025/06/12/1118556/sodium-batteries-niche/>
- **#61** 「In the base case, it overtakes Chile and becomes the world’s second-largest lithium producer」  
  判断：**正确**。USGS数据（Measured World整理）：2025年锂矿产量澳大利亚9.2万吨、中国6.2万吨（增49.8%）、智利5.6万吨；REDIMIN称智利降至第三、被中国超过。原文同句写明“2020年代中期”，时间吻合。  
  来源：<https://measuredworld.com/categories/resources/lithium-production>；<https://www.redimin.cl/chile-cae-al-tercer-lugar-mundial-en-produccion-de-litio-pese-a-crecer-14-5-en-2025>
- **#62** 「price volatility may delay the projects coming up, particularly those outside of incumbent country producers」  
  判断：**正确**。2024年8月Arcadium因供应过剩和价格长期低迷暂停或推迟加拿大Galaxy、阿根廷等两项扩产；路透2024年12月列出多座因低价减产或推迟扩产的矿山。价格波动推迟锂项目成立。  
  来源：<https://www.bloomberg.com/news/articles/2024-08-06/arcadium-lithium-pauses-expansion-plans-on-prices-supply-glut>；<https://www.reuters.com/markets/commodities/lithium-mines-that-have-cutback-output-due-low-prices-2024-12-10/>
- **#63** 「Short-term supply is expected to keep up with demand」  
  判断：**正确**。智利铜委会（2025年1月）：全球锂市场2024年过剩约8.9万吨、2025年约14.1万吨；路透2025年6月：锂供应持续超过不断增长的需求。短期供应跟上需求成立。  
  来源：<https://www.miningweekly.com/article/chiles-mining-agency-expects-another-global-lithium-surplus-this-year-2025-01-24>；<https://www.reuters.com/business/autos-transportation/lithium-industry-bemoans-paradox-low-prices-rising-demand-2025-06-26/>
- **#66** 「In the near term, there could be some oversupply in the mined nickel market as a result of high investment int…」  
  判断：**正确**。INSG：2024年镍市场过剩约17万吨；2025年10月预计2025年过剩20.9万吨、2026年26.1万吨。近期镍供应过剩成立。  
  来源：<https://insg.org/index.php/about-nickel/themarket202412/>；<https://www.miningweekly.com/article/nickel-market-forecast-to-be-in-209-000-t-surplus-in-2025-says-insg-2025-10-07>
- **#68** 「there is a potential downside: it may lead to further closures of nickel mines or halt ongoing developments.」  
  判断：**正确**。BHP于2024年7月宣布自2024年10月起暂停西澳Nickel West运营及West Musgrave项目，2027年2月前复审，理由是全球镍过剩和低价。更多镍矿关闭/停建成立。  
  来源：<https://www.bhp.com/news/media-centre/releases/2024/07/western-australia-nickel-to-temporarily-suspend-operations>；<https://www.abc.net.au/news/2024-07-11/bhp-to-close-nickel-west-mines-until-2027/104087638>
- **#69** 「In both the base case and high production case, Indonesia’s role in the global nickel market continues to expa…」  
  判断：**正确**。印尼镍矿产量份额由2024年约62%（USGS）升至2025年约66.6%（S&P），镍产业仍在扩张。作用继续扩大成立。  
  来源：<https://www.usgs.gov/centers/national-minerals-information-center/indonesia>；<https://www.spglobal.com/energy/en/news-research/latest-news/metals/081326-infographic-indonesias-shifting-policies-drive-market-volatility>
- **#70** 「Without a shift in the business plans, technology choices and regulation of such plants, growth is likely to c…」  
  判断：**正确**。CREA/GEM 2024年11月：2023–2024年印尼燃煤装机增15%、计7.2GW，其中自备4.5GW，另有15.2GW自备煤电在建或规划，总量将达26.2GW；路透2026年1月：自备电厂增长快于预期。持续增长成立（政策与商业模式未见根本改变）。  
  来源：<https://energyandcleanair.org/wp/wp-content/uploads/2024/11/EN-CREA_GEM_Indonesia-Captive_2024.pdf>；<https://www.reuters.com/sustainability/climate-energy/indonesias-captive-power-plants-putting-energy-transition-risk-researchers-say-2026-01-27/>
- **#71** 「it is difficult to imagine a significant premium emerging voluntarily」  
  判断：**正确**。路透2024年7月：BHP的西澳“绿色镍”中心随Nickel West停产搁置；LME Insight 2026年称可持续性框架尚“不能证明持久溢价正在形成”。足以支撑高成本生产的自愿低排放镍溢价未出现。  
  来源：<https://www.reuters.com/markets/commodities/search-elusive-green-nickel-premium-2024-07-23/>；<https://www.lmeinsight.com/green-nickel-different-market-how-sustainability-could-redefine-nickel-pricing/>
- **#73** 「Mined cobalt production in the DRC is poised for significant growth in the near future as several new mines ra…」  
  判断：**正确**。洛阳钼业2024年在刚果（金）TFM、KFM两矿产钴11.4万吨，比标称产能高31%，创纪录（钴协会、MINING.COM）；新矿爬坡带来显著增长成立。  
  来源：<https://www.mining.com/cmoc-sets-cobalt-production-record-in-2024/>；<https://cobaltinstitute.org/wp-content/uploads/2025/05/Cobalt-Market-Report-2024.pdf>
- **#74** 「In the near term, the current oversupply may continue with supplies from new mines and previously stockpiled v…」  
  判断：**正确**。Benchmark：2024年钴市场出现约3.7万吨的历史性过剩；S&P 2024年12月预计2025年过剩收窄但延续；直到2025年2月刚果（金）出口禁令才改变格局（见路透）。近期过剩延续成立。  
  来源：<https://source.benchmarkminerals.com/article/cmoc-supply-ramp-up-drives-cobalt-market-to-its-lowest-ebb-cobalt-2024-in-review>；<https://www.spglobal.com/energy/en/news-research/latest-news/metals/121924-commodities-2025-cobalt-market-oversupply-to-ease-in-2025>
- **#75** 「As the low price persists, there could be additional stockpiling schemes introduced from the government.」  
  判断：**正确**。路透独家（2024年5月）：低价期中国国家储备计划从国内生产商收储最多1.5万吨钴，为单次最大规模；2025年3月国家粮食和物资储备局就钴、铜、镍、锂询价招标。追加收储成立。  
  来源：<https://www.reuters.com/markets/commodities/china-state-stockpiler-aims-buy-up-15000-t-cobalt-sources-say-2024-05-23/>；<https://www.reuters.com/markets/commodities/cobalt-prices-surge-chinas-stockpiling-plan-export-ban-extension-threat-2025-03-24/>
- **#78** 「In EV batteries, while silicon is increasingly being doped in graphite anodes, it is unlikely to challenge gra…」  
  判断：**正确**。Mordor Intelligence：2025年石墨在电动车电池负极材料收入中占92.95%；SNE Research：2025年硅负极渗透率约2%。短期内硅未挑战石墨主导地位。  
  来源：<https://www.mordorintelligence.com/industry-reports/electric-vehicle-battery-anode-market>；<https://www.sneresearch.com/kr/insight/release_view/467/>
- **#79** 「the supply of needle coke is unlikely to be a limiting factor for synthetic graphite supply in the near term」  
  判断：**正确**。Mysteel 2024年5月：针状焦市场因供应过剩竞争加剧；2024年7月：上半年中国针状焦供需缺口收窄（供应52.1万吨）。未见针状焦限制人造石墨供应。  
  来源：<https://www.mysteel.net/news/5054090-needle-coke-market-competition-increasingly-intensive-on-oversupply>；<https://www.mysteel.net/news/5057545-needle-coke-supply-and-demand-gap-narrows-in-h1-2024>
- **#80** 「In the base case, the anticipated supply of battery-grade spherical graphite and synthetic graphite is project…」  
  判断：**正确**。Fastmarkets 2024年8月：石墨供应快于需求，人造石墨长期过剩使整体及电池级石墨市场持续承压；GraphiteHub引Fastmarkets称2025年市场预计仍过剩。近期电池级石墨供应充足成立。  
  来源：<https://www.fastmarkets.com/uploads/2024/09/Graphite-spotlight-August-2024.pdf>；<https://graphitehub.com/graphite-a-year-in-review-and-whats-next-for-2025/>
- **#84** 「Initial assessments indicate that iron nitride will struggle to compete with incumbent neodymium iron boron ma…」  
  判断：**正确**。磁学学会MagNews 2025年综述称Fe16N2实际报道的矫顽力仅相当于低档铁氧体、且无上升趋势，短期难有显著改进；Niron CEO称其首批车用产品是扬声器和辅助电机，驱动系统在后，量产工厂2027年才投产。窗口内氮化铁磁体未能在汽车驱动系统与钕铁硼竞争。  
  来源：<https://magsoc.org/wp-content/uploads/2025/07/MS_2025_FeN_Hype_or_Heavy_Hitter.pdf>；<https://autotechinsight.spglobal.com/news/5285351/our-first-products-in-cars-will-be-in-speakers-and-accessory-motors-followed-by-ev-drivetrains-jonathan-rowntree-ceo-niron-magnetics>；<https://www.prnewswire.com/news-releases/niron-magnetics-opens-niron-experience-center-to-showcase-rare-earth-free-iron-nitride-magnets-in-action-302938280.html>

### 趋势符合（5 条）

- **#24** 「increased doping and higher quantities of silicon are expected in the near future.」  
  判断：**趋势符合**。SNE Research（2025年7月）估计硅负极材料市场由2023年1万吨增至2025年4.1万吨、渗透率由1%升至2%；方向与“近期硅掺杂用量与比例提高”一致，但2025年数字为机构估算，未见实测统计，按趋势符合计。  
  来源：<https://www.sneresearch.com/kr/insight/release_view/467/>
- **#42** 「While the low-price environment may foster additional deployment of clean energy technologies in the medium te…」  
  判断：**趋势符合**。IEA：2024年上半年光伏新增增36%、电动车销量增25%；IEA PVPS：2024年全球新增光伏602GW。部署持续扩大，与“低价促进部署”方向一致，但证据未单独证明矿产低价是原因，且“中期”尚未结束，按趋势符合计。  
  来源：<https://www.iea.org/reports/clean-energy-market-monitor-november-2024/executive-summary>；<https://iea-pvps.org/wp-content/uploads/2025/05/Snapshot-2025-FS.pdf>
- **#51** 「In 2025 committed production is double both STEPS and APS demand, while being 40% higher than demand in the NZ…」  
  判断：**趋势符合**。BNEF：2024年全球已投运电芯产能3.1TWh，为当年锂电需求的2.5倍以上；CRU：2024年中国产能超2TWh、比总需求高60%；麦肯锡：2025年需求约1.6TWh；AlixPartners称全球产能远超需求。产能约为需求两倍的方向得到证实，但未找到2025年“已承诺产能/情景需求”的同口径比值；另有ESS News报道2025年10月储能100Ah电芯售罄、局部紧缺，按趋势符合计。  
  来源：<https://about.bnef.com/insights/commodities/lithium-ion-battery-pack-prices-see-largest-drop-since-2017-falling-to-115-per-kilowatt-hour-bloombergnef/>；<https://www.crugroup.com/en/communities/thought-leadership/2025/chinas-overcapacity-will-its-battery-industry-consolidate/>；<https://insideevs.com/news/778532/battery-capacity-outpacing-demand/>；<https://www.mckinsey.com/features/mckinsey-center-for-future-mobility/our-insights/battery-2035-building-new-advantages>；<https://www.ess-news.com/2025/10/29/battery-shortage-intensifies-as-100-ah-cells-sell-out-into-2026/>
- **#65** 「Geographical concentration is set to increase further in the base case, with the top three producing countries…」  
  判断：**趋势符合**。OECD 2026年：2025年镍产量印尼约占65%、菲律宾10%、俄罗斯5%，前三国合计约80%，高于原文所说的“当前70%”；S&P：印尼份额由2024年约62%升至2025年66.6%。集中度向83%持续上升，2040年终点未到，按趋势符合计。  
  来源：<https://www.oecd.org/en/publications/enhancing-resilience-through-traceability_a898687d-en/full-report/nickel_a87df29d.html>；<https://www.spglobal.com/energy/en/news-research/latest-news/metals/081326-infographic-indonesias-shifting-policies-drive-market-volatility>
- **#88** 「Palladium and rhodium demand are likely to decline structurally due to the uptake of EVs.」  
  判断：**趋势符合**。SFA《铂金标准2025》：2024年全球PGM尾气催化剂需求收缩54.5万盎司，超出预期，集中在中国和欧洲；Heraeus《铂金标准2026》提到2025年汽车需求继续下降。需求下降方向得到证实，但“结构性”下降为长期判断，且SFA指出新兴市场仍有增长空间，按趋势符合计。  
  来源：<https://www.sfa-oxford.com/media/1egf5xo3/platinum-standard-2025.pdf>；<https://www.heraeus-precious-metals.com/dam/jcr:6bd43a1c-db5f-4c5f-b0f1-bc04c029fe88/the-platinum-standard-2026-en.2026-05-20-11-08-35.pdf>

### 部分符合（14 条）

- **#15** 「Wind capacity additions are expected to increase significantly in the coming years thanks to the policy visibi…」  
  判断：**部分符合**。Wood Mackenzie：美国陆上风电2024年仅新增3.9GW，为十年最低；ACP：2025年新增6.9GW。2025年有回升，但2024年不升反降，“未来几年显著增加”只部分实现。  
  来源：<https://www.woodmac.com/press-releases/us-wind-market-installations-hit-a-decade-low/>；<https://www.windpowermonthly.com/article/1950734/us-onshore-wind-installations-continue-increase-despite-trump-%E2%80%93-american-clean-power-association>
- **#23** 「it is anticipated that LMFP will continue to take market share from nickel-based chemistries due to its increa…」  
  判断：**部分符合**。LMFP出货增长但规模很小：EVTank称2024年全球约1.3万吨、2025年预计3.5万吨；高工锂电称2024年LMFP增速放缓、装机不及预期，2025年出货超3万吨。“继续从镍基体系夺取份额”只在很小规模上、且2024年明显受阻。  
  来源：<https://chinaevhome.com/2025/10/16/lmfp-commercialization-accelerates-global-shipments-seen-exceeding-1-3-mt-by-2030/>；<https://www.eefocus.com/article/1951476.html>
- **#30** 「growth in China was predominantly underpinned by copper uses in construction and electricity networks, a trend…」  
  判断：**部分符合**。电网用铜需求强劲：IEA称过去两年中国电网投资快速扩张是铜需求增长的最大单一来源，国家电网2024年投资超6000亿元；但ING称中国房地产持续低迷（工业金属需求最大驱动）拖累金属需求。“建筑和电网共同支撑”只对电网一半成立。  
  来源：<https://www.iea.org/reports/global-critical-minerals-outlook-2025/executive-summary>；<https://www.chinadaily.com.cn/a/202407/26/WS66a36060a31095c51c5102a9.html>；<https://think.ing.com/articles/chinas-third-plenum-provides-little-support-to-metals/>
- **#32** 「However, in 2025 and 2026, several new projects and expansion plans are expected to ramp up」  
  判断：**部分符合**。洛阳钼业TFM/KFM扩产带动2025年一季度铜产量增15.7%；乌多坎已在设计二期（全部建成后产能超50万吨/年）；但存档证据未直接证实QB2爬坡，且ICSG称2025年全球铜矿产量仅增约1%、卡莫阿与Grasberg受扰动。所列项目只部分得到证实。  
  来源：<https://www.mining.com/web/cmoc-boosts-cobalt-output-at-congo-mines-despite-export-ban/>；<https://www.udokancopper.ru/en/press-center/5219/>；<https://www.scrapmonster.com/news/copper/icsg-data-shows-significant-copper-surplus-in-2025-2026-2-25/98563>
- **#38** 「significant price support in the near term is unlikely」  
  判断：**部分符合**。2024年钴价持续低迷符合预测；但刚果（金）2025年2月出口禁令及随后低于上年产量一半的配额“为钴价设下硬底”，钴协会报告称价格在禁令后上涨。此类政策冲击不属于原文列出的物流瓶颈或大矿意外中断例外，“近期难获支撑”只在前段成立。  
  来源：<https://www.cobaltinstitute.org/wp-content/uploads/2026/05/Cobalt-Market-Report-2025.pdf>；<https://www.reuters.com/markets/commodities/can-congo-tame-wild-cobalt-market-2025-10-09/>
- **#48** 「By 2026, solar PV becomes the largest contributor to installed electrical capacity in the STEPS, followed by w…」  
  判断：**部分符合**。Ember年度数据：2025年底全球光伏装机2391GW，首次超过煤电（2242GW）和气电（2088GW），成为最大装机来源，核心部分已提前实现；但风电1291GW仍低于煤、气和水电，“其后为风电”不符。  
  来源：<https://worldpowermonitor.com/blog/solar-capacity-passes-coal-2025/>
- **#55** 「Based on the current project pipeline, mined copper supply reaches around 25 Mt in 2026 then declines thereaft…」  
  判断：**部分符合**。ICSG 2026年10月：2025年全球铜矿产量2318万吨，2026年预计2349–2355万吨（增1.3%），2027年预计再增3.1%。2026年前增长方向成立，但数量较约2500万吨低约6%；ICSG预测2027年继续增长，而非原文所说的2026年后下降（后者尚待观测）。  
  来源：<https://icsg.org/download/2026-10-14-press-release-icsg-copper-market-forecast-2026-2027/?wpdmdl=9365>；<https://igmnir.org/en/forecasts/>
- **#67** 「In the near term, nickel sulphate may be adequately supplied to 2025.」  
  判断：**部分符合**。Wood Mackenzie 2025年5月：硫酸镍自2023年起过剩，全球镍过剩主要集中在一级镍和硫酸镍，与预测相符；但Mysteel 2025年11月称四季度硫酸镍受益于供应偏紧。到2025年大部分时间供应充足，年末一段与预测不符。  
  来源：<https://www.woodmac.com/news/opinion/nickel-looking-for-a-route-back-to-safety/>；<https://www.mysteel.net/analysis/5103005-nickel-sulfate-to-keep-benefiting-from-tight-supply-in-q4>
- **#76** 「the United States’ efforts to diversify its cobalt supply sources coupled with low commodity price could lead …」  
  判断：**部分符合**。美国国防后勤局2025年8月寻求采购最多5亿美元钴用于国防储备（三十多年来首次）；但2025年12月称正在重估策略、无重新招标日期，且钴价已较8月上涨50%，与“低价促成收储”的前提不符。新收储活动只部分出现。  
  来源：<https://www.reuters.com/world/us/us-defense-department-buy-cobalt-up-500-million-2025-08-21/>；<https://www.reuters.com/world/us/us-defense-agency-push-stockpile-cobalt-hits-pause-price-soars-2025-12-04/>
- **#81** 「the supply from today’s operating projects is sufficient to meet current demand, and this is broadly likely to…」  
  判断：**部分符合**。总量上，2025年中国稀土出口6.26万吨、为至少十年最高（Statista引海关数据）；但IEA称2025年4月起中国对7种重稀土及磁体实施出口管制，路透2025年8月称6月中国稀土磁体出口降75%，部分车企停产。“2025年供应大体满足需求”在总量上成立、在可得性上不成立。  
  来源：<https://www.iea.org/reports/rare-earth-elements/executive-summary>；<https://www.statista.com/chart/36059/annual-volume-of-rare-earth-exports-from-china/>；<https://www.reuters.com/world/us/us-defense-department-buy-cobalt-up-500-million-2025-08-21/>
- **#83** 「New project announcements from Neo Perfomance Materials in Estonia approved by the European Commission and som…」  
  判断：**部分符合**。Neo Performance Materials爱沙尼亚纳尔瓦烧结磁体厂于2025年9月投运（一期年产2000吨，欧盟资助），该项目在“未来几年投产”成立；但原文同时点名的韩国Star Group项目未找到存档证据，只能部分符合。  
  来源：<https://www.neomaterials.com/neo-opens-state-of-the-art-magnet-facility-europe/>；<https://ec.europa.eu/regional_policy/whats-new/newsroom/19-09-2025-eu-funded-europe-s-largest-rare-earth-magnet-factory-opens-in-narva-estonia_en>
- **#85** 「Global production levels are expected to be able to serve near-term demand increases.」  
  判断：**部分符合**。IAI：2024年全球原铝产量7276万吨、增2.89%；但WBMS数据显示2025年1–11月全球原铝供应缺口达153万吨。近期需求在2024年基本被满足、2025年未被产量满足。  
  来源：<https://www.mysteel.net/news/5074920-iai-global-primary-al-output-reaches-73-million-t-in-2024-up-3-yoy>；<https://www.aviationaluminum.com/news/global-primary-aluminum-supply-deficit-hits-1-53-million-tonnes-in-jan-nov-2025-wbms-data/>
- **#86** 「In the near term, prices for platinum, iridium and ruthenium are expected to remain stable, with platinum havi…」  
  判断：**部分符合**。加拿大自然资源部：2024年铂价相对稳定，月均900–1000美元/盎司、年均955美元，符合“稳定”；但路透：2025年铂价上涨146%，12月创2478.5美元/盎司纪录，远超“小幅上涨空间”。近期前段成立、后段严重偏离（铱、钌未核实）。  
  来源：<https://natural-resources.canada.ca/minerals-mining/mining-data-statistics-analysis/minerals-metals-facts/platinum-facts>；<https://www.reuters.com/business/autos-transportation/platinum-set-biggest-monthly-gain-39-years-eu-auto-policy-boost-2025-12-30/>
- **#87** 「Rhodium and palladium are likely to remain under pressure due to lower demand for internal combustion engine (…」  
  判断：**部分符合**。2024年钯价继续承压，年均983美元/盎司，较2023年1338美元大跌（加拿大自然资源部）；但2025年钯价年均1150美元、较2024年升16.9%（MetalCharts），FXStreet称2025年钯价涨65%、铑价涨79%。“继续承压”2024年成立，2025年不成立。  
  来源：<https://natural-resources.canada.ca/minerals-mining/mining-data-statistics-analysis/minerals-metals-facts/platinum-facts>；<https://metalcharts.org/palladium-price-history/2025>；<https://www.fxstreet.com/analysis/what-drove-the-strong-performance-of-platinum-group-metals-in-2025-202512151929>

### 错误（2 条）

- **#44** 「However, a ban on Russian-origin metal introduced in April 2024 may impact this growth going forward.」  
  判断：**错误**。原文认为2024年4月对俄金属禁令可能抑制LME镍库存增长；但诺镍2024年12月报告称2024年交易所镍库存由年初不足8万吨增至11月末19万吨，增至两倍多，其2024年报称过剩的中国高品级镍堆积在LME亚洲认证仓库。库存增长并未被抑制。  
  来源：<https://ar2024.nornickel.com/en/strategic-report/commodity-markets.html>；<https://nornik-upload.storage.yandexcloud.net/iblock/c52/0eoy8kajf9ubddw0lrkhgfwns3i0hewy/2024_12_10-Quintessentially-Nickel.pdf>
- **#72** 「the EU Battery Regulation which by 2025 will mandate battery producers to disclose the complete carbon footpri…」  
  判断：**错误**。欧盟电池法规的电动车电池碳足迹声明原定2025年起适用，但碳足迹计算方法授权法案截至2026年7–9月仍未通过，义务改为“法规日期或方法法案生效后12个月，以较晚者为准”，最早2027年下半年。“到2025年强制披露”未实现。  
  来源：<https://idpp.net/en/blog/battery-carbon-footprint-declaration-article-7>；<https://www.battery.mba/resources/eu-battery-regulation>；<https://www.nature.com/articles/s41560-025-01844-3>

### 暂无法判断（42 条）

- **#2** 「Mineral demand for clean energy technologies doubles between today and 2030 in a scenario that reflects today’…」  
  判断：**暂无法判断**。STEPS情景下“到2030年清洁能源技术矿产需求翻倍”的终点为2030年，截至2026-11-15尚未到期；2024–2025年需求虽持续增长，但不能据此判定2030年是否翻倍。  
  来源：<https://www.iea.org/reports/global-critical-minerals-outlook-2025/executive-summary>
- **#4** 「In a scenario that limits global warming to 1.5 °C (the Net Zero Emissions by 2050 [NZE] Scenario), the sales …」  
  判断：**暂无法判断**。该项为NZE（1.5°C）情景下2030年电动汽车销售份额65%的情景值；终点未到且情景条件（全球走上净零路径）并未成立，2025年实际份额约25%，无法按条件预测判定。  
  来源：<https://www.iea.org/reports/global-ev-outlook-2026/trends-in-electric-cars%C2%A0>
- **#5** 「The combined market value of key energy transition minerals – copper, lithium, nickel, cobalt, graphite and ra…」  
  判断：**暂无法判断**。NZE情景下2040年关键矿产市场总值7700亿美元，终点为2040年且依赖NZE情景条件，窗口内无法判定。  
  来源：<https://www.arabnews.com/business/market-size-of-energy-transition-minerals-to-hit-770bn-by-2040-iea-2512941>
- **#6** 「Latin America captures the largest amount of market value for mined output with around USD 120 billion by 2030…」  
  判断：**暂无法判断**。“到2030年拉美获得约1200亿美元最大开采市场价值”终点为2030年，尚未到期；IEA 2025年展望给出的新数值只是新预测，不是实现结果。  
  来源：<https://www.iea.org/reports/global-critical-minerals-outlook-2025/regional-snapshots>
- **#7** 「Indonesia sees the fastest growth, doubling its market value by 2030 due to its burgeoning nickel production.」  
  判断：**暂无法判断**。印尼市场价值“到2030年翻番”终点未到；2024–2025年印尼镍产量占全球60%以上并继续增长，但市场价值翻番属2030年终点结果，暂无法判断。  
  来源：<https://www.usgs.gov/centers/national-minerals-information-center/indonesia>
- **#8** 「Nearly 50% of the market value from refining is concentrated in China by 2030.」  
  判断：**暂无法判断**。“到2030年近50%的精炼市场价值集中于中国”终点为2030年，暂无法判断；IEA 2025年快照仍为新的预测。  
  来源：<https://www.iea.org/reports/global-critical-minerals-outlook-2025/regional-snapshots>
- **#9** 「There is a significant gap between prospective supply and demand for copper and lithium」  
  判断：**暂无法判断**。铜、锂在2035年（APS口径）的预期供应与需求缺口属长期情景判断，终点未到；IEA 2025年展望仍称铜存在主要担忧，但不构成实现结果。  
  来源：<https://www.iea.org/reports/global-critical-minerals-outlook-2025/overview-of-outlook-for-key-minerals>
- **#10** 「over 90% of battery-grade graphite and 77% of refined rare earths in 2030 originate from China.」  
  判断：**暂无法判断**。“2030年超过90%电池级石墨和77%精炼稀土来自中国”终点为2030年，窗口内无法判定；IEA 2025年区域快照称中国精炼市场价值份额预计由45%升至50%，仍属预测。  
  来源：<https://www.iea.org/reports/global-critical-minerals-outlook-2025/regional-snapshots>
- **#11** 「The geographical concentration of mining operations is set to rise further or remain high over the projection …」  
  判断：**暂无法判断**。原句指基准情形下“在整个预测期内”（至2040年）开采集中度进一步上升或保持高位，属长期情景判断；2024年印尼镍占比升至约62%等近况与之方向一致，但预测期远未结束，按严格口径暂无法判断。  
  来源：<https://www.usgs.gov/centers/national-minerals-information-center/indonesia>；<https://www.iea.org/reports/global-critical-minerals-outlook-2025/executive-summary>
- **#13** 「Between now and 2030, some 70-75% of projected supply growth for refined lithium, nickel, cobalt and rare eart…」  
  判断：**暂无法判断**。“2030年前精炼锂、镍、钴、稀土供应增量的70–75%来自当前前三大生产国”以2030年为终点，尚未到期；IEA称2020–2024年几乎全部供应增量来自单一头部供应国，只说明方向，未覆盖预测期。  
  来源：<https://www.iea.org/news/diversification-is-the-cornerstone-of-energy-security-yet-critical-minerals-are-moving-in-the-opposite-direction>
- **#25** 「Though ASSBs hold potential in the future, they are not expected to have significant impact until after 2030.」  
  判断：**暂无法判断**。“全固态电池在2030年之后才产生显著影响”的检验期延伸至2030年后；截至2026年宁德时代称2027年才小规模生产、曾毓群称拐点不早于2030年，与预测一致但终点未到，暂无法判断。  
  来源：<https://electrek.co/2026/06/25/catl-solid-state-battery-level-4-2030/>；<https://autonews.gasgoo.com/articles/market-industry/catl-small-scale-production-of-all-solid-state-batteries-in-2027-2115417224197840897>
- **#33** 「Possible sanctions on Russian copper may not materially affect the market」  
  判断：**暂无法判断**。所得证据（高盛称“无即时供需冲击”、ING分析）均为2024年4月中旬、出版日前的即时判断，缺少出版后对俄铜制裁影响铜市场的观测数据，暂无法判断。  
  来源：<https://www.kitco.com/news/article/2024-04-15/no-immediate-supply-demand-shock-lme-ban-russian-metals-goldman-says>；<https://think.ing.com/articles/what-do-the-new-russian-metal-sanctions-mean-for-global-trade/>
- **#49** 「This growth trajectory would see global renewable capacity increase to 2.5 times its current level by 2030, a …」  
  判断：**暂无法判断**。STEPS下2030年可再生能源装机达当前2.5倍、未达三倍，终点为2030年，暂无法判断；IEA《可再生能源2025》已下调2030年预测，但仍属预测。  
  来源：<https://www.iea.org/reports/renewables-2025/executive-summary>
- **#50** 「global EV sales (excluding two-/threewheelers) are set to grow strongly, more than tripling by 2030 in the STE…」  
  判断：**暂无法判断**。2030年电动车销量约4500万（STEPS）/5000万（APS）为2030年终点预测，尚未到期；BNEF 2026年已连续第二年下调展望，仍属预测。  
  来源：<https://news.bloomberglaw.com/esg/electric-vehicle-outlook-sinks-after-us-withdraws-policy-support>
- **#52** 「However, their share of the EV market is expected to decrease from 55% in 2023 to around 40% in 2040, as manga…」  
  判断：**暂无法判断**。高镍体系份额“到2040年降至约40%”终点为2040年，暂无法判断；2024年LFP继续占据主导只说明近况。  
  来源：<https://source.benchmarkminerals.com/article/lfp-leads-ncm-evolves-cathode-2024-year-in-review>
- **#53** 「lithium iron phosphate (LFP) and lithium manganese iron phosphate (LMFP) are set to become the leading chemist…」  
  判断：**暂无法判断**。LFP/LMFP“自2035年起”成为份额最大的电动车正极体系，起点为2035年，暂无法判断；2024年LFP已占全球电动车电池近半属近况。  
  来源：<https://www.iea.org/reports/global-critical-minerals-outlook-2025/beyond-nmc-batteries-supply-chain-issues-for-emerging-battery-technologies>
- **#54** 「Announced projects indicate that a mined copper supply gap may develop in the current decade in the base case.」  
  判断：**暂无法判断**。“本十年内可能出现铜矿供应缺口”的检验期至2030年；2025年铜精矿现货加工费自年初转负（路透）、ICSG 2025年10月预计2026年精炼铜短缺，与方向一致，但本十年未结束，暂无法判断。  
  来源：<https://www.reuters.com/markets/commodities/copper-smelters-are-facing-both-market-pricing-crises-2025-06-20/>；<https://www.reuters.com/business/slower-production-growth-will-push-copper-market-deficit-2026-says-icsg-2025-10-08/>
- **#56** 「Beyond the loss of one of the largest copper producing assets, the case is expected to deter mining investment…」  
  判断：**暂无法判断**。“Cobre Panama案将阻碍巴拿马矿业投资”：检索到的证据多为关停对经济与主权评级（降至垃圾级）的冲击及复产谈判，未找到直接衡量巴拿马矿业投资是否被阻吓的数据，证据不足，暂无法判断。  
  来源：<https://www.bnamericas.com/en/features/big-bucks-lost-the-repercussions-of-closing-cobre-panama>；<https://www.mining.com/panama-to-weigh-first-quantum-copper-mine-restart-by-early-2026/>
- **#57** 「China, however, continues to increase its dominance of copper processing, supplying around half of global refi…」  
  判断：**暂无法判断**。“自2030年起中国供应全球约一半精炼铜”终点为2030年，暂无法判断；路透称中国2025年精炼铜产量将创纪录，只属近况。  
  来源：<https://www.reuters.com/markets/commodities/china-2025-copper-output-set-hit-record-high-despite-feedstock-shortages-2025-08-01/>
- **#59** 「Lithium demand is set to rise almost threefold over this decade in the STEPS, expanding faster than all other …」  
  判断：**暂无法判断**。锂需求“本十年增长近三倍”（STEPS，至2030年）终点未到；2024年锂需求增近30%只说明方向。  
  来源：<https://www.iea.org/reports/global-critical-minerals-outlook-2025/executive-summary>
- **#64** 「Demand is set to grow further in all scenarios, increasing to 4.5 Mt in 2030 in the STEPS.」  
  判断：**暂无法判断**。“2030年镍需求达450万吨（STEPS）”终点未到；诺镍称2024年原生镍需求增4%至339万吨，只说明方向。  
  来源：<https://ar2024.nornickel.com/en/strategic-report/commodity-markets.html>
- **#77** 「the average emissions intensity associated with cobalt production is set to rise substantially as production g…」  
  判断：**暂无法判断**。“随着产量增长，钴生产平均排放强度将显著上升”：钴协会2024年报告记录印尼等产量增长，但未提供2024–2026年全球钴生产平均排放强度的同口径实测数据，暂无法判断。  
  来源：<https://www.cobaltinstitute.org/wp-content/uploads/2025/05/Cobalt-Market-Report-2024.pdf>
- **#82** 「Under these circumstances, China may prioritise supply for the domestic market, leaving a deficit globally.」  
  判断：**暂无法判断**。该句前提为“需求增长使供应缺口出现（NZE约2030年、APS约2035年）”时中国可能优先保障国内；该前提尚未出现。2025年出口管制属贸易反制，不是原文所设条件，暂无法判断。  
  来源：<https://www.csis.org/analysis/consequences-chinas-new-rare-earths-export-restrictions>
- **#89** 「this is set to change by the end of the decade as the first generation of electric vehicles reach the end of t…」  
  判断：**暂无法判断**。原文终点为“本十年末”（约2030年），尚未到达。IEA 2024年11月《关键矿产回收》称目前制造废料仍主导电池回收原料、平衡将向退役电动车电池快速转移；Robeco 2025年8月称目前及近期大部分回收材料仍来自生产废料而非报废电动车。窗口内只能看到“尚未转变”的现状与新预测，不能判定。  
  来源：<https://www.iea.org/reports/recycling-of-critical-minerals/executive-summary>；<https://www.robeco.com/en-int/insights/2025/08/battery-recycling-a-solvent-solution-for-critical-mineral-supplies>
- **#90** 「Globally, around 30 GWh of spent electric car batteries is expected to be available for recycling by the end o…」  
  判断：**暂无法判断**。原文终点为本十年末（约2030年），尚未到达；S&P Global Mobility与Circular Energy Storage在2026年给出的均是对2030年可回收废旧电池量的新预测，不构成结果。  
  来源：<https://www.mobilityglobal.com/en-us/automotive-insights/blog/why-battery-recyclers-should-manage-growth-with-caution>；<https://www.circularenergystorage.com/post/asset-or-liability-the-future-value-of-used-batteries>
- **#91** 「quantities of copper, lithium, nickel and cobalt from clean energy applications could reduce primary supply re…」  
  判断：**暂无法判断**。“到2040年回收可使关键矿产初级供应需求减少10–30%”属长期情景估算，终点未到；IEA 2024年11月《关键矿产回收》给出的也是到本世纪中叶的新情景估算，不是实现结果。  
  来源：<https://www.iea.org/reports/recycling-of-critical-minerals/executive-summary>；<https://www.iea.org/news/policy-momentum-behind-critical-minerals-recycling-gathering-pace-but-greater-uptake-required>
- **#92** 「growing policy attention and the rise of battery recycling are set to change the picture」  
  判断：**暂无法判断**。原文称政策关注与电池回收兴起“将改变”回收率增长有限的局面，未给时间。窗口内证据不一：IEA 2024年11月报告称回收电池金属产量近期快速增长但基数很低；伍德麦肯兹2025年12月称中国回收行业经营困难，我的钢铁网称2025年回收原料仍供不应求。未找到出版后二次供应占总需求比重上升的统计，暂无法判断。  
  来源：<https://www.iea.org/reports/recycling-of-critical-minerals/executive-summary>；<https://www.woodmac.com/reports/metals-chinas-battery-recycling-crisis-when-industry-leadership-meets-economic-reality-150425132/>；<https://www.mysteel.net/analysis/5113049-china-lithium-ion-battery-recycling-market-2026-outlook-and-2025-review>
- **#93** 「If all announced projects are developed in full and on time, global battery recycling capacity could exceed 1 …」  
  判断：**暂无法判断**。条件“所有已宣布项目全部按时建成”并未出现：弗劳恩霍夫ISI 2025年7月记录了欧洲多个回收项目取消（如Eramet、BASF），Canary Media 2025年5月报道Li-Cycle破产、其纽约大型工厂停建；终点2030年也未到。按规则记暂无法判断。  
  来源：<https://www.isi.fraunhofer.de/en/blog/themen/batterie-update/batterie-recycling_europa_kapazitaeten_bedarf_update_2025.html>；<https://www.canarymedia.com/articles/recycling-renewables/li-cycles-quest-to-recycle-lithium-ion-batteries-ends-in-bankruptcy>
- **#94** 「for battery recycling plants in 2030 will be EV battery production scrap, accounting for half of supply, and r…」  
  判断：**暂无法判断**。原文是对2030年回收原料结构的预测（生产废料约一半、退役电动车电池约20%），终点未到；IEA 2024年11月报告与Robeco 2025年8月文章只给出当前以生产废料为主的现状。  
  来源：<https://www.iea.org/reports/recycling-of-critical-minerals/executive-summary>；<https://www.robeco.com/en-int/insights/2025/08/battery-recycling-a-solvent-solution-for-critical-mineral-supplies>
- **#95** 「Net Zero by 2050 Unit: kt Cu 2021 2023 2030 2040 2050 2030 2040 2050 2030 2040 2050 Clean energy 5 380 6 311 1…」  
  判断：**暂无法判断**。附录表中铜需求（STEPS/APS/NZE）的未来值终点为2030、2040、2050年，均未到达。IEA《全球关键矿产展望2025》（铜章节）对同一指标给出了更新后的情景/基准预测，属新的预测而非实现结果；国际铜业研究组2025年10月仍在发布2025–2026年的短期供需预测，窗口内观测不足以判定表列终点值。  
  来源：<https://www.iea.org/reports/copper-2>；<https://icsg.org/download/2025-10-press-release-icsg-copper-market-forecast-2025-2026/?wpdmdl=8891>
- **#96** 「Copper supply Mining Historical Refining Base case Historical Unit: kt Cu 2021 2023 2030 2040 Chile 5 660 5 31…」  
  判断：**暂无法判断**。附录表中铜基准情形供应及前三国份额的未来值终点为2030、2040、2050年，均未到达。IEA《全球关键矿产展望2025》（铜章节）对同一指标给出了更新后的情景/基准预测，属新的预测而非实现结果；Mining.com.au称2025年是2019年以来铜矿供应首次收缩，窗口内观测不足以判定表列终点值。  
  来源：<https://www.iea.org/reports/copper-2>；<https://mining.com.au/ageing-mines-tighten-global-copper-supply-lines/>
- **#97** 「Lithium demand Stated Policies Announced Pledges Net Zero by 2050 Unit: kt Li 2021 2023 2030 2040 2050 2030 20…」  
  判断：**暂无法判断**。附录表中锂需求（STEPS/APS/NZE）的未来值终点为2030、2040、2050年，均未到达。IEA《全球关键矿产展望2025》（锂章节）对同一指标给出了更新后的情景/基准预测，属新的预测而非实现结果；2025–2026年锂需求仍在增长，窗口内观测不足以判定表列终点值。  
  来源：<https://www.iea.org/reports/lithium-2>；<https://mining.com.au/lithium-prices-expected-to-rise-as-demand-slows-down/>
- **#98** 「Lithium supply Raw materials Historical Chemicals Base case Unit: kt Li 2021 2023 2030 2040 Australia 50 84 14…」  
  判断：**暂无法判断**。附录表中锂基准情形供应及前三国份额的未来值终点为2030、2040、2050年，均未到达。IEA《全球关键矿产展望2025》（锂章节）对同一指标给出了更新后的情景/基准预测，属新的预测而非实现结果；澳大利亚等地新矿仍在爬坡，窗口内观测不足以判定表列终点值。  
  来源：<https://www.iea.org/reports/lithium-2>；<https://www.miningnews.net/miners/news-analysis/4517988/lithium-tune-changing-diggers-dealers-2025>
- **#99** 「Nickel demand Stated Policies Announced Pledges Net Zero by 2050 Unit: kt Ni 2021 2023 2030 2040 2050 2030 204…」  
  判断：**暂无法判断**。附录表中镍需求（STEPS/APS/NZE）的未来值终点为2030、2040、2050年，均未到达。IEA《全球关键矿产展望2025》（镍章节）对同一指标给出了更新后的情景/基准预测，属新的预测而非实现结果；诺镍2025年报给出的是2025年当年需求，窗口内观测不足以判定表列终点值。  
  来源：<https://www.iea.org/reports/nickel-2>；<https://ar2025.nornickel.com/strategic-report/commodity-markets/>
- **#100** 「Nickel supply Mining Historical Refining Base case Historical Unit: kt Ni 2021 2023 2030 2040 Indonesia 1 005 …」  
  判断：**暂无法判断**。附录表中镍基准情形供应及前三国份额的未来值终点为2030、2040、2050年，均未到达。IEA《全球关键矿产展望2025》（镍章节）对同一指标给出了更新后的情景/基准预测，属新的预测而非实现结果；国际镍研究组2026年仍在修订短期平衡，窗口内观测不足以判定表列终点值。  
  来源：<https://www.iea.org/reports/nickel-2>；<https://insg.org/index.php/about-nickel/the-market-2026-7/>
- **#101** 「Cobalt demand Stated Policies Announced Pledges Net Zero by 2050 Unit: kt Co 2021 2023 2030 2040 2050 2030 204…」  
  判断：**暂无法判断**。附录表中钴需求（STEPS/APS/NZE）的未来值终点为2030、2040、2050年，均未到达。IEA《全球关键矿产展望2025》（钴章节）对同一指标给出了更新后的情景/基准预测，属新的预测而非实现结果；钴协会给出的是2025年当年需求，窗口内观测不足以判定表列终点值。  
  来源：<https://www.iea.org/reports/cobalt-2>；<https://www.cobaltinstitute.org/cobalt-market-report-2025/>
- **#102** 「Cobalt supply Mining Base case Unit: kt Co 2021 2023 2030 2040 DRC 121 157 215 135 Indonesia 3 20 50 Russia 6 …」  
  判断：**暂无法判断**。附录表中钴基准情形供应及前三国份额的未来值终点为2030、2040、2050年，均未到达。IEA《全球关键矿产展望2025》（钴章节）对同一指标给出了更新后的情景/基准预测，属新的预测而非实现结果；刚果（金）2025年出口禁令只影响当期供应，窗口内观测不足以判定表列终点值。  
  来源：<https://www.iea.org/reports/cobalt-2>；<https://www.cobaltinstitute.org/wp-content/uploads/2025/08/Quarterly-Market-Report-Q2-2025-Public.pdf>
- **#103** 「Graphite demand Historical Stated Policies Announced Pledges Net Zero by 2050 Unit: kt 2021 2023 2030 2040 205…」  
  判断：**暂无法判断**。附录表中石墨清洁能源与电动车需求（STEPS/APS/NZE）的未来值终点为2030、2040、2050年，均未到达。IEA《全球关键矿产展望2025》（石墨章节）对同一指标给出了更新后的情景/基准预测，属新的预测而非实现结果；窗口内观测不足以判定表列终点值。  
  来源：<https://www.iea.org/reports/graphite-2>；<https://www.hkexnews.hk/listedco/listconews/sehk/2026/0326/2026032603354.pdf>
- **#104** 「Battery storage 37 145 508 904 1 133 638 1 210 1 459 815 1 555 1 867 Other uses 3 388 3 340 4 430 6 047 7 648 …」  
  判断：**暂无法判断**。附录表中石墨储能、其他用途与总需求（STEPS/APS/NZE）的未来值终点为2030、2040、2050年，均未到达。IEA《全球关键矿产展望2025》（石墨章节）对同一指标给出了更新后的情景/基准预测，属新的预测而非实现结果；窗口内观测不足以判定表列终点值。  
  来源：<https://www.iea.org/reports/graphite-2>；<https://www.hkexnews.hk/listedco/listconews/sehk/2026/0326/2026032603354.pdf>
- **#105** 「Graphite supply Mining (natural graphite) Historical Refined battery-grade supply Base case Historical Unit: k…」  
  判断：**暂无法判断**。附录表中石墨基准情形供应及前三国份额的未来值终点为2030、2040、2050年，均未到达。IEA《全球关键矿产展望2025》（石墨章节）对同一指标给出了更新后的情景/基准预测，属新的预测而非实现结果；中国以外新矿仍在建设，窗口内观测不足以判定表列终点值。  
  来源：<https://www.iea.org/reports/graphite-2>；<https://mining.com.au/structural-shift-australias-graphite-grab/>
- **#106** 「Rare earth elements demand Historical Stated Policies Announced Pledges Net Zero by 2050 Unit: kt REE 2021 202…」  
  判断：**暂无法判断**。附录表中磁体稀土需求（STEPS/APS/NZE）的未来值终点为2030、2040、2050年，均未到达。IEA《全球关键矿产展望2025》（稀土章节）对同一指标给出了更新后的情景/基准预测，属新的预测而非实现结果；窗口内观测不足以判定表列终点值。  
  来源：<https://www.iea.org/reports/rare-earth-elements-2025>；<https://global-reia.org/wp-content/uploads/2026/09/2025_Annual_REE-Market-Report-REIA-Public.pdf>
- **#107** 「Rare earth elements supply Mining Historical Refining Base case Unit: kt REE 2021 2023 2030 2040 China 32 47 5…」  
  判断：**暂无法判断**。附录表中磁体稀土基准情形供应及前三国份额的未来值终点为2030、2040、2050年，均未到达。IEA《全球关键矿产展望2025》（稀土章节）对同一指标给出了更新后的情景/基准预测，属新的预测而非实现结果；中国以外的分离与磁体产能仍在建设，窗口内观测不足以判定表列终点值。  
  来源：<https://www.iea.org/reports/rare-earth-elements-2025>；<https://www.reuters.com/sustainability/climate-energy/west-scrambles-fill-heavy-rare-earth-gap-china-rivalry-deepens-2025-11-19/>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| 19 | India is anticipated to reduce subsidy l… | 出版前已发生 | 2024年4月1日起EMPS 2024将电动两轮车补贴由每kWh 1万卢比减半至5000卢比（Livemint 2024-04-02），事件发生在出版日（2024-05-17）之前，出版时已成定局，不作为出版后预测计分。 |
| 22 | The novel fast charging LFP battery will… | 出版前已发生 | 宁德时代神行快充LFP电池已于2024年2月在奇瑞星纪元ET首发装车（盖世汽车2024-02-21），出版日前已成事实；出版后哪吒L（2024-05-26预售）等只是延续。不作为出版后预测计分。 |

## 文件

- 本文：`cases/iea-global-critical-minerals-outlook-2024-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/iea-global-critical-minerals-outlook-2024-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/iea-global-critical-minerals-outlook-2024-v5/audit/manual_review_2026-11-15.py`
