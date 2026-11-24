# 托马斯·罗伯特·马尔萨斯《人口原理》（An Essay on the Principle of Population，1798 年第一版）：出版后预测人工核查

- 案例目录：`cases/malthus-essay-on-population-v5/`
- 出版日期：1798 年 6 月 7 日匿名出版（J. Johnson，伦敦）。正文取自 Project Gutenberg #4239 纯文本（与队列记录 sha256 `e277e7d2…` 逐字节一致，344,419 字节；按工具包读取为 344,315 字符，含 CRLF），原样使用，不做转换。观察窗口为 1798-06 至 2026-11-15。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

按 METHOD.md 执行。抽取：用仓库 prepare_book v5 流水线（85e6da1 工具包）把全文（344,315 字符）切成 100 块（每块 3500 字符，带 600 字符上下文；第 94—100 块主要是 Gutenberg 许可文本）。助手逐块通读，没有用关键词筛选，按 DISCOVER_PROMPT_V5 写出模型本应返回的 JSON，再由仓库代码完成引文对齐、归属降级、去重和导入：共 42 条候选，其中 22 条为可核验预测，20 条为 unclear（一般规律、对戈德温/孔多塞设想的反驳、同一论点的重复表述等），另有 3 条假设推演被排除。核验：每条先写 scope，各做一次 support 与 counter 的 Exa 检索，其中 5 条（第 3、4、15、19、21 条）追加一轮自适应检索；只从检索返回的 URL 中选源。原文用 Exa contents 抓取（失败时 curl 兜底）存档于 data/sources（62 份，sha256），写入 data/evidence.jsonl（62 条）；理由中的数字均已在存档文本中核对。助手阅读后按“正确／趋势符合／部分符合／错误／暂无法判断”规则逐条评断，再经 pipeline.py apply assess → check → report。本稿由助手逐条对照书中原文与存档证据人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 22 条，剔除非预测 0 条，计入 **22 条预测**，其中 **22 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 6 |
| 趋势符合 | 0 |
| 部分符合 | 3 |
| 错误 | 13 |
| 暂无法判断 | 0 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **27.3%**（6/22） |
| 加权胜率 | **34.1%** |
| 错误率 | **59.1%**（13/22） |
| 未定占比（暂无法判断/预测） | 0.0%（0/22） |

## 总体评价

马尔萨斯对“近期”和局部的判断多数应验：两性情欲没有消失，1800—1850 年不列颠农业产出远未翻两番，中国此后一个半世纪反复发生大饥荒，美国从未发生饥荒，物理学出现了一系列重大发现，欧洲下层民众受教育程度大幅提高。部分应验的有三条：19 世纪大部分人类确实长期处于极端贫困，但今天饥饿人口已降到 8% 左右；“按育种改良人类”从未普遍推行，但 20 世纪上半叶强制绝育法曾大规模实施；美国人口增速终究放缓，但 1798 年后 60 多年仍保持约 25 年翻番的速度。判错的集中在全书核心命题上：食物产出没有按算术级数增长，耕地扩张停止后食物年增量没有递减；下层阶级的实际工资、识字率和闲暇都大幅改善；转移支付和社会保险能持续减贫；中国开放贸易后既大量进口粮食，又让约 8 亿人脱贫；全球生育率降到 2.2，人口“超过生活资料”的倾向已明显改变。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（6 条）

- **#1** 「the passion between the sexes is necessary and will remain nearly in its present state」  
  判断：**正确**。两性情欲并未如戈德温设想的那样趋于消失：进化人类学综述指出性动机是自然选择的产物、在各人类社会普遍存在；近年美国调查虽显示年轻人性活动频率有所下降（“性衰退”），但属幅度变化，不构成“情欲消失”  
  来源：<https://onlinelibrary.wiley.com/doi/full/10.1002/ajpa.22394>；<https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/abs/precis-of-the-evolution-of-human-sexuality/F1406141BA424362B1F506E8A912B359>；<https://pubmed.ncbi.nlm.nih.gov/28265779/>
- **#4** 「In the next twenty-five years, it is impossible to suppose that the produce could be quadrupled.」  
  判断：**正确**。英格兰农业产出在1800—1850年远未翻两番：经济史估算显示英格兰农业产出1700—1850年合计只增长2.5—3倍（Overton估计约170%—180%），1750年后一个世纪才翻一番多；Clark还认为工业革命时期新增人口主要靠进口粮食养活  
  来源：<https://www.edgepedia.org/british-agricultural-revolution>；<https://www.bahs.org.uk/AGHR/PDFS/ARTICLES/44n1a1.pdf>；<https://www.bbc.co.uk/history/british/empire_seapower/agricultural_revolution_01.shtml>
- **#8** 「A nation in this state must necessarily be subject to famines.」  
  判断：**正确**。此后中国反复发生大饥荒：1876—79年“丁戊奇荒”约900万—1300万人死亡，1920—21年、1928—30年、1942—43年等华北饥荒，以及1959—61年大饥荒；1961年后未再发生饥荒，但在1798年后的一个半世纪里预测结果明确出现  
  来源：<https://en.wikipedia.org/wiki/List_of_famines_in_China>；<https://scispace.com/pdf/changing-disaster-relief-regimes-in-china-an-analysis-using-44awu666w1.pdf>；<https://worldpeacefoundation.org/wp-content/uploads/2025/01/Historic-Famines-synthesis-table-191224.pdf>
- **#9** 「In America, where the reward of labour is at present so liberal, the lower classes might retrench very conside…」  
  判断：**正确**。1798年以来美国从未发生全国或区域性饥荒：世界和平基金会1870年以来“大饥荒”（死亡10万以上）统计和Our World in Data的饥荒数据均无美国；大萧条时期有饥饿与粮食援助问题，个别被强制迁徙的原住民群体出现饥饿死亡，但不构成饥荒  
  来源：<https://ourworldindata.org/famines>；<https://worldpeacefoundation.org/wp-content/uploads/2025/01/Historic-Famines-synthesis-table-191224.pdf>；<https://foodsystemprimer.org/food-nutrition/hunger-and-food-insecurity>；<https://www.mnhs.org/mnopedia/search/index/event/sandy-lake-tragedy>
- **#14** 「I expect that great discoveries are yet to take place in all the branches of human science, particularly in ph…」  
  判断：**正确**。1798年后科学尤其物理学出现大量重大发现：1820年奥斯特发现电流磁效应、1831年法拉第电磁感应、1870年代麦克斯韦电动力学，20世纪的狭义/广义相对论（1905、1915）与量子力学（1900—1927）  
  来源：<https://physicstribune.com/physicists/physics-timeline/>；<https://www.ias.ac.in/article/fulltext/reso/023/10/1077-1100>；<https://www.mpg.de/19252737/physics-in-upheaval>
- **#16** 「The lower classes of people in Europe may at some future period be much better instructed than they are at pre…」  
  判断：**正确**。19世纪起欧洲普遍推行初等义务教育，下层识字率大幅上升，多数国家在1871—1880年前后已越过75%识字门槛；英格兰政府逐步介入大众初等教育，欧洲下层民众受教育程度远高于1798年  
  来源：<https://doi.org/10.1017/9781009242585.005>；<https://www.degruyterbrill.com/document/doi/10.9783/9781512807189/html>；<https://doi.org/10.37830/sjs.2024.1.04>

### 部分符合（3 条）

- **#3** 「This difficulty must fall somewhere and must necessarily be severely felt by a large portion of mankind.」  
  判断：**部分符合**。前半段应验：OECD《How Was Life? II》按基本需求成本法估算，1820年后135年间全球一半以上人口处于极端贫困，此后又用了46年才把这一比例减半；但当前比例已大幅下降，2024年全球饥饿人口约6.73亿、占8.2%，“很大一部分人类必然严重受苦”已不再是常态  
  来源：<https://www.oecd.org/en/publications/how-was-life-volume-ii_3d96efc5-en/full-report/component-14.html>；<https://www.fao.org/newsroom/detail/global-hunger-declines--but-rises-in-africa-and-western-asia--un-report/en>；<https://ourworldindata.org/poverty>
- **#12** 「it is not probable that an attention to breed should ever become general」  
  判断：**部分符合**。“按育种改良人类”从未成为普遍做法，二战后优生学被广泛否定，这一点与预测相符；但20世纪上半叶优生学曾成为跨国主流运动，美国32个州和加拿大两省通过强制绝育法，正是作者认为不可行的“让劣质个体不育”的手段被大规模推行，故只部分符合  
  来源：<https://thecanadianencyclopedia.ca/en/article/eugenics>；<https://www.annualreviews.org/content/journals/10.1146/annurev-genom-090314-024930>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC2757926/>
- **#21** 「we may be perfectly sure that population will not long continue to increase with the same rapidity as it did t…」  
  判断：**部分符合**。方向最终应验但“不会长期保持”未兑现：美国人口普查局指出1790—1860年每十年增长始终在32.7%以上（约25年翻番的速度又维持了60多年），1860年人口过3000万后才降到22.6%，此后持续放缓  
  来源：<https://www.census.gov/newsroom/blogs/random-samplings/2021/04/comparisons-to-benchmarks-as-a-measure-of-quality.html>；<https://en.wikipedia.org/wiki/Demographic_history_of_the_United_States>

### 错误（13 条）

- **#2** 「Subsistence increases only in an arithmetical ratio.」  
  判断：**错误**。食物产出并非按算术级数增长：基于FAOSTAT 157种作物的研究显示，1961—2023年全球作物总产量增长3.9倍，主要来自单产提高2.54倍；Our World in Data显示各大洲食物供应增长都快于人口（如非洲食物供应增长6.2倍、人口增长2.6倍），与“人口几何增长、食物只能算术增长”相反  
  来源：<https://www.cabidigitallibrary.org/doi/pdf/10.31220/agriRxiv.2025.00382?download=true>；<https://ourworldindata.org/data-insights/food-supplies-have-grown-even-faster-than-the-population-on-every-continent>；<https://www.nature.com/articles/ncomms2296>
- **#5** 「This constant effort as constantly tends to subject the lower classes of the society to distress and to preven…」  
  判断：**错误**。主结果相反：Clark对1209—2003年英格兰工匠和劳工实际工资的估算显示，工业革命后实际工资持续大幅上升，下层阶级境况出现重大而持久的改善；1770—1850年间实际收入增长缓慢（Feinstein的“悲观”结论）只在窗口前段部分符合  
  来源：<https://faculty.econ.ucdavis.edu/faculty/gclark/papers/wage%20-%20jpe%20-2004.pdf>；<https://doi.org/10.1093/ooec/odad033>；<http://www.piketty.pse.ens.fr/files/Feinstein1998.pdf>
- **#6** 「no possible contributions or sacrifices of the rich, particularly in money, could for any time prevent the rec…」  
  判断：**错误**。转移支付能够持续降低贫困：OECD《政府概览2025》称再分配在每个有数据的OECD国家都降低了相对贫困，税前转移前平均27%的人处于相对贫困；美国老年贫困率在社会保障扩张后由1959年约35%降到2006年约9%。贫困并未消失，但与“任何时期都无法阻止困苦”的判断相反  
  来源：<https://www.oecd.org/en/publications/government-at-a-glance-2025_0efd0bcd-en/full-report/poverty-and-inequality_5f7b56a0.html>；<https://www.everycrsreport.com/files/20080404_RL34433_56abba6edca766b0483af00c7991d314e29be0ff.pdf>；<https://www.nytimes.com/2023/03/09/magazine/poverty-by-america-matthew-desmond.html>
- **#7** 「When acre has been added to acre, till all the fertile land is occupied, the yearly increase of food will depe…」  
  判断：**错误**。耕地扩张基本停止后，食物年增量没有逐渐减少：Our World in Data显示1961年以来谷物产量大幅增长而谷物用地面积基本稳定，增产主要来自单产提高；全球作物总产量1961—2023年增长3.9倍。部分地区单产增速放缓或停滞（Ray等2012），但全球年增量未见递减  
  来源：<https://ourworldindata.org/yields-vs-land-use-how-has-the-world-produced-enough-food-for-a-growing-population>；<https://www.cabidigitallibrary.org/doi/pdf/10.31220/agriRxiv.2025.00382?download=true>；<https://www.nature.com/articles/ncomms2296>
- **#10** 「It may be expected that in the progress of the population of America, the labourers will in time be much less …」  
  判断：**错误**。美国劳动者实际工资长期大幅上升而非下降：IZA研究指出美国制造业工人实际（消费）工资自19世纪以来持续上涨；NBER估计1860—1890年制造业日工资上升约50%、建筑业约60%。19世纪中叶个别时期实际工资有过下滑，但长期方向相反  
  来源：<https://docs.iza.org/dp17326.pdf>；<https://www.nber.org/system/files/chapters/c2496/c2496.pdf>；<https://www.nber.org/system/files/chapters/c11510/c11510.pdf>
- **#11** 「Such establishments and calculations may appear very promising upon paper, but when applied to real life they …」  
  判断：**错误**。精算式社会保险在实践中大有成效：美国老年官方贫困率1966—2006年由28.5%降至9.4%，社会保障被普遍认为是主要原因；2000财年社会保障向4500万人支付4150亿美元。部分国家养老金制度存在可持续性问题，但不等于“完全无效”  
  来源：<https://www.ssa.gov/policy/docs/ssb/v69n1/v69n1p45.html>；<https://www.federalreserve.gov/boarddocs/speeches/2001/200104192/default.htm>；<https://documents1.worldbank.org/curated/en/973571468174557899/pdf/multi-page.pdf>
- **#13** 「the improbability that the lower classes of people in any country should ever be sufficiently free from want a…」  
  判断：**错误**。主结果相反：1820年全球只有约十分之一的成年人识字，如今识字率约87%；普及初等、中等乃至高等教育使下层民众大规模获得智识提升。高等教育中的阶层差距仍存在，但不改变方向  
  来源：<https://ourworldindata.org/data-insights/two-centuries-ago-only-1-in-10-adults-could-read-today-its-almost-9-in-10>；<https://ourworldindata.org/literacy>；<https://link.springer.com/rwe/10.1007/978-3-319-74078-2_9-1>
- **#15** 「no possible sacrifices or exertions of the rich, in a country which had been long inhabited, could for any tim…」  
  判断：**错误**。以殖民地末期北美普通人为基准，久已开发国家的下层民众早已超过：Lindert与Williamson估算1774年殖民地居民平均收入远高于英国人；而英格兰银行千年数据显示英国人均实际GDP从1700年约1600英镑增至2016年约29600英镑（2016年价格），增长约17倍，今天英国低收入阶层的物质条件远高于18世纪北美普通人。改善主要来自经济增长与再分配的结合，并非单靠富人的牺牲  
  来源：<https://www.degruyterbrill.com/document/doi/10.1515/9781400880348-005/html>；<https://www.mountvernon.org/george-washington/colonial-life-today/early-american-economics-facts>；<https://longseries.com/en/d/boe-real-gdp-per-capita/>
- **#17** 「I even conceive it possible, though not probable that they may have more leisure」  
  判断：**错误**。劳动者闲暇大幅增加：Our World in Data据Huberman与Minns数据显示，富裕国家平均工人年工作小时比19世纪后期减少约一半，工作日、每周天数与年工作周数均下降。工业革命初期工时曾延长，只是窗口前段的情况  
  来源：<https://ourworldindata.org/data-insights/working-hours-in-wealthy-countries-have-been-reduced-by-half-over-the-last-150-years>；<https://ourworldindata.org/working-more-than-ever>；<https://fred.stlouisfed.org/blog/2021/10/a-short-history-of-working-hours>
- **#18** 「if the lower classes of society could agree among themselves never to work more than six or seven hours in the…」  
  判断：**错误**。限制工时的约定能够被遵守并制度化：八小时工作制是一战前国际工会运动的主要诉求；国际劳工组织称1918—19年八小时工作日已通过集体协议或法律在多数工业国家成为现实，1922年48小时工作周在欧洲等地工业中已成普遍做法；此后富裕国家实际工时持续下降。部分国家仍有违规加班，但不改变主结果  
  来源：<https://www.ilo.org/resource/article/convention-no-1-landmark-workers%E2%80%99-rights>；<https://ourworldindata.org/data-insights/working-hours-in-wealthy-countries-have-been-reduced-by-half-over-the-last-150-years>；<https://www.respicio.ph/commentaries/unpaid-overtime-in-the-philippines-employee-rights-and-legal-remedies>
- **#19** 「she could not in return import such a quantity as would be any sensible addition to the annual stock of subsis…」  
  判断：**错误**。条件已触发（改革开放后中国大力发展对外贸易），而进口已成为食物供给的重要补充：中国每年进口约1亿吨大豆，用于满足国内饲料需求；杜鹰测算净进口农产品虚拟播种面积占国内总播面比重2020年达23.2%，食物自给率由约100%降到约76%  
  来源：<https://farmdocdaily.illinois.edu/2025/12/can-china-reduce-soybean-import-demand-evaluating-soybean-meal-reduction-efforts.html>；<https://m.thepaper.cn/kuaibao_detail.jsp?contid=16255265&from=kuaibao>；<https://chinapower.csis.org/china-food-security/>
- **#20** 「the increasing wealth of the nation would rather tend to depress than to raise the condition of the poor」  
  判断：**错误**。条件已触发（1978年后对外开放、出口制造业迅速扩张），但穷人境况大幅改善：世界银行称过去40年按每天1.9美元标准中国贫困人口减少约8亿，占同期全球减贫的75%。农民工待遇与不平等问题存在，但与“压低穷人境况”相反  
  来源：<https://www.worldbank.org/en/news/press-release/2022/04/01/lifting-800-million-people-out-of-poverty-new-report-looks-at-lessons-from-china-s-experience>；<https://thedocs.worldbank.org/en/doc/f692402b5b3b21154f103ee64c0c551d-0070012022/original/Poverty-Synthesis-Report-cn.pdf>；<https://www.ilo.org/media/330291/download>
- **#22** 「The perpetual tendency in the race of man to increase beyond the means of subsistence is one of the general la…」  
  判断：**错误**。人口超过生活资料增长的倾向已明显改变：联合国称全球生育率已降至约2.2，越来越多国家低于更替水平；同时各大洲食物供应增长都快于人口。人口在食物充足条件下并未继续扩张，与“该规律不会改变”相反；撒哈拉以南非洲人口增长仍快，是局部例外  
  来源：<https://desapublications.un.org/policy-briefs/un-desa-policy-brief-no-172-new-landscape-fertility-and-family-planning-30-years>；<https://www.un.org/development/desa/pd/sites/www.un.org.development.desa.pd/files/undesa_pd_2025_wfr_2024_final.pdf>；<https://ourworldindata.org/data-insights/food-supplies-have-grown-even-faster-than-the-population-on-every-continent>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC9628488/>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/malthus-essay-on-population-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/malthus-essay-on-population-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/malthus-essay-on-population-v5/audit/manual_review_2026-11-15.py`
