# 英国政府科学办公室 Foresight《智能基础设施的未来：通向2055的情景》（Intelligent Infrastructure Futures: The Scenarios – Towards 2055）：出版后预测人工核查

- 案例目录：`cases/curry-intelligent-infrastructure-futures-2055-v5/`
- 出版日期：**2006 年 1 月**，英国贸工部科学技术办公室 Foresight 项目（文件号 DTI/Pub 8159，作者 Andrew Curry、Tony Hodgson、Rachel Kelnar、Alister Wilson）。所用正文为 GOV.UK 公开 PDF（assets.publishing.service.gov.uk/…/06-521-intelligent-infrastructure-scenarios.pdf），重新下载后 sha256 为 `73b51cc2…`，与书单记录逐字节一致；pdftotext 抽出 TXT 的 sha256 为 `9dcfbd23…`（215,883 字符）。观察窗口为 2006-01 至 2026-11-15。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

按 METHOD.md 执行。抽取：用仓库 prepare_book v5 流水线把全文（215,883 字符）切成 63 块（每块 3500 字符，带 600 字符上下文）。助手逐块通读，按 DISCOVER_PROMPT_V5 写出模型本应返回的 JSON（87 条原始条目），再由仓库代码完成引文对齐、归属降级、去重和导入：共 47 条候选，其中 27 条为可核验预测；20 条降为 unclear（14 条为书中转述、未获作者认可的第三方观点，即工作坊参与者和脚注引述，5 条无法核验）；另有 40 条（34 条情景假设推演、4 条历史陈述、1 条机制、1 条规范建议）被排除。核验：每条先写 scope，各做一次 support 与 counter 的 Exa 检索（54 次），其中 3 条追加一轮自适应检索（7 次）；只从检索返回的 URL 中选源。原文存档于 data/sources（sha256），写入 data/evidence.jsonl（67 条）。助手阅读后按“正确／趋势符合／部分符合／错误／暂无法判断”规则逐条评断，再经 pipeline.py apply assess → check → report。本稿由助手逐条对照书中原文与存档证据人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 27 条，剔除非预测 0 条，计入 **27 条预测**，其中 **27 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 20 |
| 趋势符合 | 0 |
| 部分符合 | 6 |
| 错误 | 1 |
| 暂无法判断 | 0 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **74.1%**（20/27） |
| 加权胜率 | **85.2%** |
| 错误率 | **3.7%**（1/27） |
| 未定占比（暂无法判断/预测） | 0.0%（0/27） |

## 总体评价

这份报告的主体是四个 2055 年情景（Perpetual Motion、Urban Colonies、Tribal Trading、Good Intentions），作者明言情景不是预测，因此情景叙事全部按假设推演排除。计入的 27 条来自执行摘要、Urban Colonies 后的反思、生物乙醇信息框，以及附录“变化驱动因素”清单（项目自身口吻）。清单条目多为简短的方向性标题（移动需求增长、亚洲经济增长、移民增加、电子商务、监控社会、嵌入式技术、ICT 成本下降等），20 年后大多已成趋势，所以正确率偏高（20/27），这反映的是条目本身的低难度，而不是对具体数量或时点的命中。偏差在三类：一是对“全球能源缺口”“老龄而更活跃”“贫富差距扩大”“自动驾驶更安全高效”的判断只部分成立；二是“地方交通改造方案将陷入迷雾”被牛津、剑桥等地的推进与受挫并存所部分证实；三是“税收将越来越基于资源消耗”与事实相反，欧盟环境税占税收比重下降，判为错误。生物乙醇将来自炎热国家只部分应验：增量多来自巴西、印度，但温带美国仍占全球一半以上。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（20 条）

- **#1** 「transport, with its need for convenient and portable fuels, will find it harder than other uses of energy to s…」  
  判断：**正确**。按出版至截止日窗口检验。英国国内交通排放自1990年仅降15%，同期全国国内排放降48%；2023年交通占国内排放29%，仍是最大排放部门；欧盟资料也指出交通排放与其他部门相反，过去几十年未能显著下降。交通比其他用能部门更难脱碳的判断成立  
  来源：<https://www.gov.uk/government/statistics/transport-and-environment-statistics-2023/transport-and-environment-statistics-2023>；<https://www.gov.uk/government/statistics/transport-and-environment-statistics-2023--2/greenhouse-gas-emissions-from-transport-in-2023>；<https://www.jttri.or.jp/topic_europe_2024Dec-01.pdf>
- **#2** 「if current trends continue, transport could be responsible for a steadily increasing percentage of all emissio…」  
  判断：**正确**。以英国为口径（报告对象）。交通排放自1990年降15%而全国排放降48%，交通占比随之上升，2023年占29%、2024年占30%，Carbon Brief称已接近总量的三分之一；全球层面2010—2019年交通是燃烧排放中增长最快的部门。占比持续上升的方向成立  
  来源：<https://www.gov.uk/government/statistics/transport-and-environment-statistics-2023/transport-and-environment-statistics-2023>；<https://www.gov.uk/government/statistics/transport-and-environment-statistics-2023--2/greenhouse-gas-emissions-from-transport-in-2023>；<https://www.gov.uk/government/statistics/transport-and-environment-statistics-2024--2/greenhouse-gas-emissions-from-transport-in-2024>；<https://www.carbonbrief.org/analysis-uk-emissions-in-2023-fell-to-lowest-level-since-1879>；<https://tcc-gsr.com/wp-content/uploads/2023/06/1-Transport-Pathways-to-Reach-Global-Climate-and-Sustainability-Goals.pdf>
- **#3** 「The particular politics of London at the moment of the inception of the Congestion Charge are unlikely to be r…」  
  判断：**正确**。伦敦开征拥堵费时的政治条件此后未在英国其他城市重现：大曼彻斯特2008年公投否决拥堵费，剑桥2023年放弃拥堵费方案；到2025年10月牛津才在六条街道试行临时性的5英镑收费点，规模远不及伦敦全域收费  
  来源：<http://news.bbc.co.uk/2/hi/uk_news/england/manchester/7778110.stm>；<https://www.theguardian.com/politics/2008/dec/13/congestion-charging-transport>；<https://www.bbc.co.uk/news/uk-england-cambridgeshire-66961894>；<https://www.bbc.co.uk/news/articles/c3epz1lpx9yo>
- **#6** 「Growing demand for mobility – passengers and goods」  
  判断：**正确**。按出版至截止日窗口检验。英国机动车行驶里程由2005年的3058亿车英里增至截至2025年3月一年的3359亿车英里，2025年交通量已高于疫情前2019年水平  
  来源：<https://www.data.gov.uk/collections/transport/road-traffic/download/>；<https://www.gov.uk/government/statistics/provisional-road-traffic-estimates-great-britain-april-2024-to-march-2025>；<https://roadtraffic.dft.gov.uk/>
- **#7** 「Growth of Asian economies」  
  判断：**正确**。亚洲经济持续增长：亚洲在全球GDP中的比重由2000年不到30%升至近50%（CFR）；1990—2022年亚洲名义GDP增长近16倍，全球为9倍；2024年亚洲发展中经济体增速仍约4.9%  
  来源：<https://www.cfr.org/education/learn/reading/economics-asia>；<https://www.eastspring.com/insights/deep-dives/30-years-of-asian-growth-a-story-of-resilience-and-untapped-potential>；<https://www.adb.org/sites/default/files/publication/1017791/ado-december-2024.pdf>
- **#8** 「Increasing migration (and emigration)」  
  判断：**正确**。全球国际移民存量2024年达3.04亿，较1990年几乎翻倍，2020年为2.75亿；英国2024年净移民43.1万，虽较2023年减半但仍处高位。移民增加的方向成立  
  来源：<https://www.destatis.de/EN/Themes/Countries-Regions/International-Statistics/Data-Topic/Population-Labour-Social-Issues/DemographyMigration/Migrants.html>；<https://www.migrationdataportal.org/themes/international-migrant-stocks-overview>；<https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/longterminternationalmigrationprovisional/yearendingdecember2024>
- **#10** 「Declining trust in institutions」  
  判断：**正确**。以英国为口径。英国社会态度调查（BSA）2024年显示对政府体制的信任与信心降至纪录低点，45%受访者“几乎从不”相信政府会把国家置于党派之上，为历史最高比例  
  来源：<https://natcen.ac.uk/news/trust-and-confidence-britains-system-government-record-low>；<https://www.bbc.co.uk/news/articles/cv223kzq6r9o>
- **#12** 「Growth in ‘cyberfraud’」  
  判断：**正确**。网络欺诈增长：英格兰和威尔士犯罪调查显示截至2025年3月一年约420万起欺诈，较上年增31%；截至2026年6月一年达450万起，为2017年有可比记录以来最高；欺诈占个人所受犯罪的约41%  
  来源：<https://www.ons.gov.uk/peoplepopulationandcommunity/crimeandjustice/articles/natureoffraudandcomputermisuseinenglandandwales/yearendingmarch2025>；<https://www.which.co.uk/news/article/fraud-levels-hit-record-high-how-to-stay-safe-from-scams-alwjH5m0kSpi>；<https://www.nationalcrimeagency.gov.uk/what-we-do/crime-threats/fraud-and-economic-crime/>
- **#13** 「Increasing world trade」  
  判断：**正确**。世界贸易继续增加：2024年全球贸易创纪录达33万亿美元，增长3.7%（约1.2万亿美元），世界贸易增加的方向成立  
  来源：<https://unctad.org/news/global-trade-hits-record-33-trillion-2024-driven-services-and-developing-economies>；<https://unctad.org/publication/key-statistics-and-trends-international-trade-2024>
- **#14** 「Increasing use of ‘telepresence’ technology」  
  判断：**正确**。远程临场/视频会议使用大幅增加：Zoom日会议参与者2020年4月达3亿；德国电信全球在线会议分钟数由2019年约8.8亿增至2023年约17.3亿，疫情后虽回落仍远高于疫情前  
  来源：<https://www.reuters.com/article/us-zoom-video-commn-encryption/zoom-says-it-has-300-million-daily-meeting-participants-not-users-idUSKBN22C1T4/>；<https://report.telekom.com/hr-factbook/2023/organizational-culture/working-in-the-digital-age.html>
- **#15** 「Growing (impact of) climate change」  
  判断：**正确**。气候变化及其影响加剧：WMO确认2024年为有记录以来最暖年份，全球平均近地面气温比1850—1900年高1.55℃，冰量损失与海平面上升加速  
  来源：<https://wmo.int/news/media-centre/wmo-confirms-2024-warmest-year-record-about-155degc-above-pre-industrial-level>；<https://www.reuters.com/business/environment/record-2024-temperatures-accelerate-ice-loss-rise-sea-levels-un-weather-body-2025-03-19/>
- **#16** 「E-commerce continues to grow」  
  判断：**正确**。电子商务持续增长：英国网络销售占零售额比重由2010年的7.3%升至2025年的27.5%，2021年曾达30.7%的年度高点  
  来源：<https://www.anthonymcgrath.co/data/uk-online-share-of-retail/uk-online-share-of-retail.pdf>；<https://www.ons.gov.uk/businessindustryandtrade/retailindustry/timeseries/j4mc>
- **#17** 「Increasingly localised/decentralised energy production」  
  判断：**正确**。分布式能源生产增加：英国自2008年有记录以来MCS认证的小型光伏装置已超过150万套，政府称逾150万户家庭装有太阳能板  
  来源：<https://solarenergyuk.org/news/uk-reaches-1-5m-small-scale-solar-installations/>；<https://www.gov.uk/government/publications/solar-roadmap/solar-roadmap-united-kingdom-powered-by-solar-accessible-webpage>
- **#18** 「Growth of the surveillance society」  
  判断：**正确**。以英国为口径。监控社会扩张：警方实时人脸识别2025年扩展到更多警队，政府拟设立专门机构监管；伦敦部分行政区升级CCTV并加装人脸识别  
  来源：<https://www.gov.uk/government/news/live-facial-recognition-technology-to-catch-high-harm-offenders>；<https://www.reuters.com/world/uk/british-police-ramp-up-facial-recognition-catch-criminals-2025-12-04/>；<https://www.biometricupdate.com/202509/as-london-expands-cctv-network-critics-express-concerns-of-overreach>
- **#19** 「Emergence of megacities」  
  判断：**正确**。特大城市持续涌现：人口千万以上城市2005年为20个，2025年增至33个，其中19个在亚洲  
  来源：<https://www.jkgeography.com/uploads/1/0/8/4/108433405/un_mega_cities_fact_sheet.pdf>；<https://www.un.org/en/desa/WUP-2025>
- **#20** 「Growing utilisation of ‘embedded’ technology」  
  判断：**正确**。嵌入式（物联网）技术使用增加：2024年全球联网物联网设备达185亿台，比2023年增长12%  
  来源：<https://iot-analytics.com/number-connected-iot-devices/>
- **#21** 「Changing data storage: from desktop to network」  
  判断：**正确**。数据存储由桌面转向网络：Forrester报告称一半以上企业数据已存于云端；Wasabi调查称2024年平均43%的数据存于公有云  
  来源：<https://www.forrester.com/report/more-than-half-of-enterprise-data-is-in-the-cloud/RES185482>；<https://wasabi.com/company/newsroom/press-releases/public-cloud-spend-shows-no-fear-of-recession-according-to-wasabi-2023-global-cloud-storage-index>
- **#22** 「Continued growth of an ‘always on’ culture」  
  判断：**正确**。以英国为口径。“永远在线”继续扩张：英国成年人日均上网四个半小时，比上年多10分钟，95%的16岁以上人口家中可上网  
  来源：<https://www.ofcom.org.uk/siteassets/resources/documents/research-and-data/online-research/online-nation/2025/online-nations-report-2025.pdf?v=409837>；<https://www.ofcom.org.uk/media-use-and-attitudes/online-habits/from-apps-to-ai-search-how-the-uk-goes-online-in-2025>
- **#23** 「Movement away from office-based working」  
  判断：**正确**。以英国为口径。工作脱离办公室：疫情前约八分之一在职成年人居家工作，2024年秋28%的在职成年人采用混合办公；2007年春居家或以家为基地的工作者约320万  
  来源：<https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/employmentandemployeetypes/articles/whoarethehybridworkers/latest>；<https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/employmentandemployeetypes/articles/characteristicsofhomeworkersgreatbritain/september2022tojanuary2023>；<https://www.eurofound.europa.eu/en/publications/all/telework-united-kingdom>
- **#26** 「Reducing cost of ICT and enhanced data processing」  
  判断：**正确**。信息通信技术成本下降、算力增强：硬件每美元性能每年约提升30%；2006—2021年GPU每美元浮点运算能力约每2.5年翻倍  
  来源：<https://epoch.ai/data-insights/price-performance-hardware>；<https://epoch.ai/publications/trends-in-gpu-price-performance>

### 部分符合（6 条）

- **#4** 「both in London and elsewhere other proposals for significant reconfiguration of local transport management reg…」  
  判断：**部分符合**。部分应验：剑桥拥堵费方案2023年在反对声中被放弃；但颇具争议的伦敦超低排放区（ULEZ）仍于2023年8月扩展到全市，牛津也在2025年开始收费，重大地方交通管理改革并非一概搁浅  
  来源：<https://www.bbc.co.uk/news/uk-england-cambridgeshire-66961894>；<https://www.reuters.com/world/uk/londons-contentious-clean-air-zone-extends-entire-city-2023-08-28/>；<https://www.bbc.co.uk/news/articles/c3epz1lpx9yo>
- **#5** 「Future supply of bioethanol will come from countries with hot climates.」  
  判断：**部分符合**。部分应验：2021—2025年全球燃料乙醇增量多来自巴西、印度等炎热国家（印度由8.3亿加仑增至26亿加仑，巴西由72.4亿增至86.5亿）；但温带的美国以玉米为原料仍是最大产地，2025年占全球52%，巴西占27%、印度占8%，供应并未主要转向炎热国家  
  来源：<https://ethanolrfa.org/markets-and-statistics/annual-ethanol-production>；<https://ethanolrfa.org/file/2919/branch_global_brief.pdf>；<https://css.umich.edu/publications/factsheets/energy/biofuels-factsheet>
- **#9** 「Growing global energy deficit – increased demand and consumption」  
  判断：**部分符合**。需求与消费增长部分成立：2024年全球能源需求增长2.2%，快于过去十年平均；但“能源缺口扩大”不成立，2025年石油市场供过于求，1—9月平均过剩约190万桶/日，油价下跌  
  来源：<https://www.iea.org/news/growth-in-global-energy-demand-surged-in-2024-to-almost-twice-its-recent-average>；<https://www.iea.org/commentaries/as-oil-market-surplus-keeps-rising-something-s-got-to-give>；<https://www.eia.gov/todayinenergy/detail.php?id=66944&utm=>
- **#11** 「Ageing, yet more active, population」  
  判断：**部分符合**。老龄化成立：英格兰和威尔士65岁及以上人口由2011年的920万增至2021年的逾1100万；但“更活跃”未得到证实，英国健康预期寿命在2022—2024年较此前下降（男性降1.8年、女性降2.5年），议会报告也指出太多老年人缺乏身体活动  
  来源：<https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/ageing/articles/profileoftheolderpopulationlivinginenglandandwalesin2021andchangessince2011/2023-04-03>；<https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/healthandlifeexpectancies/bulletins/healthstatelifeexpectanciesuk/between2011to2013and2022to2024>；<https://committees.parliament.uk/publications/53187/documents/297506/default/>
- **#24** 「Semi-autonomous/autonomous vehicles becoming safer and more efficient」  
  判断：**部分符合**。安全性部分成立：IIHS研究显示Waymo无人车每英里事故比人类驾驶少68%；但驾驶辅助系统存在明显安全缺口，NHTSA认定特斯拉Autopilot与至少467起碰撞相关、其中13起致命；“更高效”缺少系统证据  
  来源：<https://www.iihs.org/news/detail/waymos-driverless-cars-crash-less-often-than-people>；<https://www.cnbc.com/2024/04/26/tesla-autopilot-linked-to-hundreds-of-collisions-has-critical-safety-gap-nhtsa.html>
- **#27** 「Growing gap between rich and poor」  
  判断：**部分符合**。以英国为口径。财富差距扩大：2011—2019年最贫困10%家庭与富裕家庭的财富差距扩大约50%；但收入不平等基本未扩大，2017—18年基尼系数0.34，与1980年代末相同，前1%家庭财富占比自1980年以来仅升1个百分点  
  来源：<https://blogs.lse.ac.uk/inequalities/2024/10/29/the-uks-wealth-gap-has-grown-by-50-in-eight-years/>；<https://ifs.org.uk/publications/living-standards-poverty-and-inequality-uk-2019>；<https://www.resolutionfoundation.org/comment/wealth-inequality/>

### 错误（1 条）

- **#25** 「Taxation increasingly based on resource consumption rather than income」  
  判断：**错误**。以欧盟为口径（英国无存档数据）。税收并未日益转向资源消耗：欧盟环境税占税收和社会缴款的比重持续下降，2019年为6.44%，2023年为5.19%，2024年为5.1%  
  来源：<https://www.eea.europa.eu/en/analysis/indicators/share-of-environmental-taxes-in>；<https://www.statista.com/statistics/1387416/share-environmental-taxes-total-tax-revenues-eu/>；<https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Environmental_tax_statistics>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/curry-intelligent-infrastructure-futures-2055-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/curry-intelligent-infrastructure-futures-2055-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/curry-intelligent-infrastructure-futures-2055-v5/audit/manual_review_2026-11-15.py`

## 说明

- 第 6—27 条来自附录“变化驱动因素”清单，原文只有一句标题，按出版日→2026-11-15 的隐含窗口判断方向。
- 第 2、10、18、22、23、27 条按英国口径核对，第 25 条按欧盟口径核对；口径限制写在 assessment 的 scope／limitations 字段。
- 部分来源为商业或第三方整理（IoT Analytics、Statista 式整理 PDF 等），已尽量用 ONS、DfT、IEA、UN 等官方来源对照。

