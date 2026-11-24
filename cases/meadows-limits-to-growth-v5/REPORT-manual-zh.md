# 增长的极限（The Limits to Growth，1972）：出版后预测人工核查

- 案例目录：`cases/meadows-limits-to-growth-v5/`
- 出版日期：1972-03
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

按仓库原 DeepSeek 管线逐步操作（pdftotext 转 TXT、3500 字切块、逐块按 DISCOVER_PROMPT_V5 通读抽取、确定性筛选、取证、判分），只把模型调用改成助手通读，不用 DeepSeek API。先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 35 条，剔除非预测 0 条，计入 **35 条预测**，其中 **17 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 5 |
| 趋势符合 | 3 |
| 部分符合 | 7 |
| 错误 | 2 |
| 暂无法判断 | 18 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **29.4%**（5/17） |
| 加权胜率 | **63.2%** |
| 错误率 | **11.8%**（2/17） |
| 未定占比（暂无法判断/预测） | 51.4%（18/35） |

## 总体评价

本书是罗马俱乐部委托的 World3 模型报告，核心判断是：若当时的增长趋势不变，地球的增长极限将在未来一百年内到来，并可能出现人口与工业的突然下降。按通读新方法抽出 35 条可核验预测（旧的关键词法只有 13 条计入预测）。其中 18 条因终点仍在未来（约 2072/2100 年）或模型情景的前提并未按设定出现，记为暂无法判断，可判定样本只有 17 条。说中的主要是中短期、可观察的判断：2000 年前人口不会趋平、各国增长率不会原样持续、欠发达地区城市化更快、部分地区缺水先于全球耕地耗尽、资源政治冲突会早于经济枯竭。明显说错的是建立在 1970 年代核电高增长情景上的判断：2000 年美国核电装机只有约 9.8 万兆瓦，远不是 90 万兆瓦，相应核废料存量也低一个数量级。2000 年世界人口约 61 亿而非 70 亿、大气 CO2 约 370 ppm 而非 380 ppm，都属于方向对、时点或幅度有偏差的部分符合。标准运行的“过冲与崩溃”本身要等到二十一世纪中后期才能下结论，现在既没有全球崩溃，也还不能宣布已经被证伪。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（5 条）

- **#2** 「Total urban population is expected to increase exponentially in the less developed regions of the world, but a…」  
  判断：**正确**。联合国《世界城市化展望》和后续综述显示，1970年以来欠发达地区城市人口持续快速（近指数）增长，而较发达地区城市人口增速已下降近半个世纪、更接近线性甚至趋缓，与图3说明的方向一致。  
  来源：<https://population.un.org/wup/assets/Publications/WUP2018-PopFacts_2018-1.pdf>；<https://www.rics.org/news-insights/wbef/the-history-and-future-of-places-part-14-urban-growth-and-decline-over-the-coming-century>；<http://ourworldindata.org/urbanization>
- **#3** 「there is no possibility of leveling off the population growth curve before the year 2000, even with the most o…」  
  判断：**正确**。联合国在2001年发布的《世界人口展望》说明：2000年年中世界人口为61亿，仍以每年约1.2%、7700万人的速度增长，增长曲线在2000年前并未趋平。  
  来源：<https://press.un.org/en/2001/chamiebriefing.doc.htm>；<https://usinfo.org/wf-archive/2001/010302/epf506.htm>
- **#6** 「It is unlikely that the rates of growth listed in table 2 will continue unchanged even until the end of this c…」  
  判断：**正确**。表2所列主要国家的人均经济与人口增长率到2000年已明显改变：中国人均GDP增速远高于书中所列水平，日本高速增长结束，苏联解体，尼日利亚、巴基斯坦等也经历冲击与恢复。作者关于“不太可能原封不动持续到本世纪末”的判断成立。  
  来源：<https://data.worldbank.org/indicator/NY.GDP.PCAP.KD.ZG?locations=CN>；<https://cepr.net/documents/publications/econ_growth_2005_11_27_table_1.htm>
- **#9** 「In some areas of the world, this limit will be reached long before the land limit becomes apparent.」  
  判断：**正确**。全球可耕地并未在2000年前耗尽，但近东和北非等地区已处于极高水资源压力：世界资源研究所指出17个国家（约占世界人口四分之一）面临极度缺水，粮农组织称该地区多个国家位列全球水资源压力最高之列。淡水约束在部分地区确实早于全球土地极限出现。  
  来源：<https://www.fao.org/neareast/news/details/FAO-launches-a-new-report-informing-on-the-status-of-land-and-water-resources-in-the-Near-East-and-North-Africa-region/en>；<https://bdd.pseau.org/outils/ouvrages/wri_17_countries_home_to_one_quarter_of_the_world_s_population_face_extremely_high_water_stress_2019.pdf>
- **#12** 「the political question may arise long before the ultimate · economic one.」  
  判断：**正确**。1973年和1979年石油危机、欧佩克提价、南美矿山国有化以及此后的稀土地缘政治，都表明生产国与消费国之间的政治较量远早于资源的最终经济枯竭出现，与作者的方向判断一致。  
  来源：<https://carnegieendowment.org/posts/2025/11/todays-rare-earths-conflict-echoes-the-1973-oil-crisis-but-its-not-the-same>

### 趋势符合（3 条）

- **#19** 「if society continues to strive for that goal, it will eventually reach one of many earthly limitations.」  
  判断：**趋势符合**。在持续追求物质增长的窗口内，斯德哥尔摩韧性中心2023年评估显示九项行星边界中已有六项被突破（气候变化、生物圈完整性、氮磷循环等），表明人类已在逼近并越过若干地球限制；但全球物质产出仍在增长，尚未出现书中那种全面的硬停止，故记为趋势符合。  
  来源：<https://www.stockholmresilience.org/research/research-news/2023-09-13-all-planetary-boundaries-mapped-out-for-the-first-time-six-of-nine-crossed.html>；<https://www.science.org/doi/10.1126/sciadv.adh2458>
- **#23** 「under the assumption of no major change in the present system, population and industrial growth will certainly…」  
  判断：**趋势符合**。在“系统无重大变化则至迟在下一世纪内（约2072年前）停止”的窗口中，联合国2024年展望已将世界人口峰值放到2080年代中期，人口增长率已大幅下降；但全球工业产出和GDP在2026年仍在增长，工业增长停止尚未出现，终点也未到，记为趋势符合。  
  来源：<https://www.un.org/en/UN-projects-world-population-to-peak-within-this-century>；<https://ourworldindata.org/un-population-2024-revision/>
- **#34** 「the growth phase cannot continue for another one hundred years.」  
  判断：**趋势符合**。作者怀疑增长阶段不可能再持续一百年（至约2072年）。联合国2024年展望将世界人口峰值放在2080年代中期，增长率已大幅放缓，方向朝向增长阶段结束；但全球经济在2026年仍在增长，2072年终点未到，记为趋势符合。  
  来源：<https://www.un.org/en/UN-projects-world-population-to-peak-within-this-century>；<https://ourworldindata.org/un-population-2024-revision/>

### 部分符合（7 条）

- **#4** 「we can look forward to a world population of around 7 billion persons in .30 more years.」  
  判断：**部分符合**。作者估计约30年后（2000年）世界人口约为70亿。联合国及人口咨询局数据为2000年约60.67–61亿；70亿在2011年10月31日才达到。方向正确，但到达时间晚了约11年、2000年时点偏低约13%。  
  来源：<https://www.prb.org/news/9-billion-world-population-by-2050/>；<https://www.unfpa.org/press/world-population-reach-7-billion-31-october>；<https://press.un.org/en/2001/chamiebriefing.doc.htm>
- **#7** 「economzc growth, as it is occurring today, is inexorably widening the absolute gap between the rich and the po…」  
  判断：**部分符合**。按当时增长方式，绝对差距在美国与许多低收入国家之间确实扩大；但中国、印度等人口大国的追赶显著改变了全球图景，穷国集团并未整体被“无情地”拉远。绝对差距扩大与部分收敛并存，故为部分符合。  
  来源：<https://www.stlouisfed.org/on-the-economy/2024/aug/convergence-divergence-gdp-growth-richer-poorer-countries>；<https://fred.stlouisfed.org/blog/2016/06/income-difference-across-countries-is-the-gap-closing/>
- **#13** 「the CO, concentration will reach 380 ppm by the year 2000, an Increase of nearly 30 percent of the probable va…」  
  判断：**部分符合**。作者（转述并采纳 Machta）预计2000年大气CO2为380 ppm。NOAA毛纳罗亚年均值2000年为369.71 ppm，2005年379.98 ppm、2006年382.09 ppm，380 ppm大约在2005–2006年才达到。量级接近，时点偏晚约五六年。  
  来源：<https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_annmean_mlo.txt>
- **#20** 「will bring us close to the limits to growth of those activities surprisingly soon.」  
  判断：**部分符合**。1972年之后世界经济与人口又持续增长了半个多世纪，并未在“出人意料的很快”的短窗口内全面撞上增长极限；但气候、部分渔业和行星边界等问题已显示出逼近限制的迹象。时间判断偏早，方向部分应验。  
  来源：<https://www.mdpi.com/1996-1073/15/14/4953>；<https://www.stockholmresilience.org/research/research-news/2023-09-13-all-planetary-boundaries-mapped-out-for-the-first-time-six-of-nine-crossed.html>
- **#21** 「as the rest of the world develops economically, it will follow basically the US pattern of consumption」  
  判断：**部分符合**。许多工业化国家在经济起飞阶段的能源与物质消费确实随人均产出上升而陡增，接近作者假定的美国模式；但欧、中等经济体后来出现能效提高与部分脱钩，并非简单复制美国人均消费路径。  
  来源：<https://doi.org/10.1016/j.worlddev.2018.06.008>；<https://doi.org/10.55845/jos-2025-1251>
- **#28** 「Where these conditions of economic inequality already exist, the Green Revolution tends to cause widening ineq…」  
  判断：**部分符合**。绿色革命在亚洲显著提高单产并减少贫困和饥饿；同时在土地分配本已不平等的地区（如印度旁遮普等地）也出现大农户先获益、土地与收益集中的记录。加剧不平等的倾向在部分地区存在，但并非普遍的唯一结果。  
  来源：<https://ncbi.nlm.nih.gov/pmc/articles/PMC3411969/>；<https://archive.foodfirst.org/wp-content/uploads/2013/12/DR15-A-Bitter-Harvest.pdf>；<https://geosci.uchicago.edu/~moyer/GEOS24705/2014a/Notes/Hazell_IFPRI_2003.pdf>
- **#29** 「The fifth, sixth, and perhaps even seventh billions may arrive before the year 2000, less than 30 years from n…」  
  判断：**部分符合**。世界人口第五个十亿在1987年、第六个十亿在1999年10月12日到来，均在2000年之前；第七个十亿在2011年10月31日才到达。作者对第七个十亿用了“perhaps”，前两个节点正确，第三个未在2000年前出现，记为部分符合。  
  来源：<https://press.un.org/en/1998/19981028.pop685.html>；<https://www.census.gov/newsroom/blogs/random-samplings/2011/10/the-world-population-at-7-billion.html>；<https://www.prb.org/app/uploads/2020/11/population-bulletin-2011-66-2-world-at-7-billion.pdf>

### 错误（2 条）

- **#15** 「Installed nuclear generating capacity In the United States Is expected ro grow from 11 thousand megawatts In 1…」  
  判断：**错误**。美国能源信息署核电运行表显示，2000年美国核电净夏季装机容量为97.9百万千瓦（约9.79万兆瓦），2011年也仅约101百万千瓦，远低于所预测的90万兆瓦以上，主结果相反。  
  来源：<https://www.eia.gov/totalenergy/data/annual/txt/ptb0902.html>
- **#16** 「Total amount of stored nuclear wastes, radioactive by-products of the energy production, will probably exceed …」  
  判断：**错误**。该核废料存量预测建立在核电装机增至90万兆瓦以上的情景上。实际2000年装机仅约9.8万兆瓦；美国国家科学院资料记载，至2001年12月美国商用乏燃料库存约4.5万吨重金属、装机约88吉瓦。规模比预测低一个数量级，主结果未出现。公开库存多以吨计而非居里，居里口径存在局限。  
  来源：<https://www.eia.gov/totalenergy/data/annual/txt/ptb0902.html>；<https://www.nationalacademies.org/read/11320/chapter/4>

### 暂无法判断（18 条）

- **#1** 「If the present growth trends in world population, industrialization, pollution, food production, and resource …」  
  判断：**暂无法判断**。作者把“现有趋势不变则在未来一百年内（约至2072年）达到极限并出现人口与工业突然下降”作为最可能结果。观察窗口截止2026年11月，全球人口仍在增长、工业产出仍在扩张，尚未出现全球性突然崩溃；该期限尚未到期，也还没有足以判定崩溃即将在剩余窗口内发生的决定性趋势。  
  来源：—
- **#5** 「if we continue to succeed in lowering mortality with no better success in lowering fertility than we have acco…」  
  判断：**暂无法判断**。该判断的前提是“生育率下降不比过去更成功”。联合国《World Fertility 2024》显示全球总和生育率已由1960年代的约5降到2024年的约2.2，下降幅度远大于1972年以前的经验，前提未满足，不能按正误计分。实际2030年前后世界人口约80–90亿，远低于当时人口的四倍。  
  来源：<https://www.un.org/development/desa/pd/sites/www.un.org.development.desa.pd/files/undesa_pd_2025_wfr_2024_final.pdf>
- **#8** 「there will still be a desperate land shortage before the year 2000 if per capita land requirements and populat…」  
  判断：**暂无法判断**。该判断明确以“人均用地需求和人口增长率保持当时水平”为条件。此后生育率下降、单产提高，人均耕地需求下降，前提未满足；全球也未在2000年前出现作者所说的全面“严重土地短缺”。按未触发的真实条件，不按正误计分。  
  来源：<https://www.fao.org/4/y4252e/y4252e06a.htm>
- **#10** 「This more realistic dynamic assumption about the future use of chromium yields a probable lifetime of 125 year…」  
  判断：**暂无法判断**。动态模型给出铬的可能可用年限约125年（自1970年起约至2095年）。该终点尚未到来；美国地质调查局2024–2025年矿产摘要仍列有可观铬铁矿储量和产量，但尚不能据此判定2095年前是否会按该寿命耗尽。  
  来源：<https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-chromium.pdf>
- **#11** 「th~ gr~at majority of th~ curr~ntly important nonren~wabl~ resources will b~ ~xtrem~ly costly roo y~ars from n…」  
  判断：**暂无法判断**。“一百年后（约2072年）绝大多数重要不可再生资源将极其昂贵”是带明确远期终点的判断。截止2026年，实际金属与能源价格经历周期但并不是全面、持续的“极其昂贵”，终点尚未到达，暂不按正误判定。  
  来源：<https://ourworldindata.org/grapher/real-commodity-price-index-metals>
- **#14** 「At the present rate of growth, thermal release will reach 18 percent of incoming solar energy by the year 2000…」  
  判断：**暂无法判断**。检索未找到可核验的、关于2000年洛杉矶盆地废热释放占入射太阳能比例的存档数据，无法判断是否达到18%。缺一项决定性观测。  
  来源：—
- **#17** 「Annual release of nuclear wastes, mostly In the form of krypton gas and tritium In cooling water, will reach 2…」  
  判断：**暂无法判断**。判断附有“若当时排放标准仍然有效”的前提。美国核管会在1991年大幅修订、1994年生效的10 CFR Part 20提高了辐射防护标准，前提未保持，故不按正误计分。  
  来源：<https://www.nrc.gov/about-nrc/radiation/related-info/opt-revise/faqs>
- **#18** 「if the 7 billion people of the year 2000 have a GNP per capita as high as that of present-day Americans, the t…」  
  判断：**暂无法判断**。该估算的前提是2000年世界人口达70亿且人均GNP达到当时美国水平。2000年世界人口实为约61亿，且全球人均收入远低于1970年美国水平，前提未满足。  
  来源：<https://www.prb.org/news/9-billion-world-population-by-2050/>
- **#22** 「The behavior mode of the system shown in figure 35 is clearly that of overshoot and collapse. In this run the …」  
  判断：**暂无法判断**。标准运行的过冲与崩溃被放在21世纪内、确切年份作者认为无意义。截止2026年全球工业与人口尚未因不可再生资源耗竭而崩溃；部分对照研究认为轨迹仍接近标准运行，但崩溃终点尚未出现，暂无法判断。  
  来源：<https://ethz.ch/content/dam/ethz/special-interest/usys/ites/ecosystem-management-dam/documents/EducationDOC/Readings_DOC/Turner_2012_GAIA_LimitsToGrowth.pdf>；<https://www.imf.org/en/publications/weo/issues/2026/10/13/world-economic-outlook-october-2026>
- **#24** 「The overall behavior mode in · figure 36--growth and collapse-is very similar to that in the standard run.」  
  判断：**暂无法判断**。“资源翻倍后行为模式仍是增长而后崩溃”是模型情景，前提是其他系统结构不变、仅经济可采资源加倍。1972年后储量、技术、效率和生育率同时变化，该单独前提并未在现实中按设定出现，条件未满足。  
  来源：—
- **#25** 「The result is still an end to growth before the year 2100.」  
  判断：**暂无法判断**。同时引入“无限”资源、污染控制、提高农业产量和完美节育四项技术政策，是模型中的组合假设，并未作为一套政策在1975年前后被世界一并实施；且“2100年前增长结束”的终点仍在未来。  
  来源：—
- **#26** 「we have not been able to find a set of policies that avoids the collapse mode of behavior.」  
  判断：**暂无法判断**。“在不有意限制增长的前提下找不到能避免崩溃的技术政策组合”是对模型试验的概括，无法在单一现实路径上直接证伪或证实；现实同时出现了生育率下降等社会变化，并非纯粹的“只靠技术”路径。  
  来源：—
- **#27** 「did not in any case postpone the collapse beyond the year 2100.」  
  判断：**暂无法判断**。“即使最乐观的技术估计也无法把崩溃推迟到2100年之后”的终点为2100年，尚未到达，且所设技术组合并未按原设定实施。  
  来源：—
- **#30** 「Population and Industrial capital reach levels high enough to create food and resource shortages before the ye…」  
  判断：**暂无法判断**。“到2000年才引入稳定化政策，则2100年前会出现粮食和资源短缺”以该套稳定政策在2000年被引入为前提。世界并未在2000年按书中设定同时稳定人口与资本，前提未满足；2100年终点也未到。  
  来源：—
- **#31** 「if Mexico's birth rate gradually declined fiom its present value to an exact replacement value the year 2000, …」  
  判断：**暂无法判断**。前提是墨西哥出生率到2000年降到精确更替水平。世界银行数据中墨西哥2000年人口约9863万，2021年约1.2765亿；生育率大幅下降但2000年仍高于更替水平，前提未精确满足，不能按“至2060年达1.30亿”的条件推演计分。  
  来源：<https://databank.worldbank.org/views/reports/reportwidget.aspx?Id=b450fd57&Report_Name=CountryProfile&country=MEX&dd=y&inf=n&tbar=y&zm=n>；<https://mexiconewsdaily.com/news/mexicos-population-growth-130-million-fertility-rate-falls/>
- **#32** 「If the United States population had two children per family starting now and if there were no net immigration,…」  
  判断：**暂无法判断**。前提是美国从当时起保持每家两个孩子且没有净移民。美国总和生育率随后降至更替水平以下，同时净移民持续存在；沃顿预算模型估计2026年美国居民人口约3.435亿。前提未满足，不按正误计分。  
  来源：<https://budgetmodel.wharton.upenn.edu/p/2026-05-29-the-demographic-economic-and-conventional-budget-outlook-2026-2056/>；<https://www.macrotrends.net/global-metrics/countries/usa/united-states/fertility-rate>
- **#33** 「If world population as a whole reached a replacement-size family by the year 2000 (at which time the populatio…」  
  判断：**暂无法判断**。前提是世界在2000年达到更替水平生育率且人口为58亿。实际2000年世界人口约61亿，全球生育率仍明显高于更替水平；2024年人口约82亿且联合国中方案仍预计增至2080年代的约103亿。前提未满足。  
  来源：<https://press.un.org/en/2001/chamiebriefing.doc.htm>；<https://population.un.org/wpp/assets/Files/WPP2024_Summary-of-Results.pdf>
- **#35** 「if the global society waits until those constraints are unmistakably apparent, it will have waited too long.」  
  判断：**暂无法判断**。“若等到约束已经明白无误才行动，那就已经太迟”取决于社会是否等到那一步、以及“太迟”的判定标准。气候治理中1.5°C是否不可逆回就仍有争议，缺少一项可在本窗口内一锤定音的事实。  
  来源：—

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/meadows-limits-to-growth-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/meadows-limits-to-growth-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/meadows-limits-to-growth-v5/audit/manual_review_2026-11-15.py`
