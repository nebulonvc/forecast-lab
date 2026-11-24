# 洛佩斯-克拉罗斯、达尔、格罗夫《全球治理与21世纪全球机构的兴起》：出版后预测人工核查

- 案例目录：`cases/lopez-claros-global-governance-21st-century-v5/`
- 出版日期：2020年（Cambridge University Press；队列只给年份，观察窗口2020→2026-11-15）。PDF sha256 `240418a8d4d6e634b5f6029e2fc36eba926a777b4b806f640a030f2c16e36bb2`；TXT sha256 `090efd4b9b5b0dbecdff1f4fd2a4e528aff272e270ac6f794ba88da931a0302d`。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

严格使用85e6da1版prepare_book：3500字符/600上下文，共486块；未跳过matter_spans。续跑实际起点为379块（此前1–378已答），不重新领书，379–486逐块完整通读，包括附录国家投票表、参考文献、索引；全486块逐块写JSON，并非关键词抽样。原始53项，扩完整指代句并清空context后，确定性代码排除2条historical，导入51候选，其中36条resolvable、15条unclear。没有人工按摘要/正文重复批量降级，没有人工额外duplicate，代码去重0条。每条首轮各support/counter一次，共76次查询（包括扩句前另2条）；第二轮18个主题共36次；自适应16个主题各2条新查询，共32次。均使用Exa，仅选搜索返回URL，最多8个URL/条。最终68个公开来源归档及68条证据记录，均含sha256。逐项读取归档中有关段落，明确区分观测、模型、永久/临时迁移、存量/流量及条件；选择决定性原句写入evidence_notes，人工完成六项语义复核，再apply assess→check→report。未定项evidence_support为unknown，避免假装已获充分结果证据。先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 36 条，剔除非预测 0 条，计入 **36 条预测**，其中 **22 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 9 |
| 趋势符合 | 0 |
| 部分符合 | 9 |
| 错误 | 4 |
| 暂无法判断 | 14 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **40.9%**（9/22） |
| 加权胜率 | **61.4%** |
| 错误率 | **18.2%**（4/22） |
| 未定占比（暂无法判断/预测） | 38.9%（14/36） |

## 总体评价

较短的2020—2026观察窗中，人口收缩、塔利班回归、军费达到2万亿、否决权与安理会改革阻力等方向已出现。粮食价格、公众不满及迁移等多为部分成立或统计口径不完全对应；“只会增长”的流离失所判断遇到2025年下降，财政起源危机、财政工具消失及IMF放贷能力减半也不符证据。长期人口、核灭绝政治吸引力、永久迁移历史纪录、辅助语言和国际公民合作的强断言有定义或实测缺口，不把未来模型当作命中，趋势符合0条。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（9 条）

- **#3** 「in the Middle East and North Africa, high fertility rates and the highest rates of population growth in the wo…」  
  判断：**正确**。ILO2024年资料显示中东北非2023年青年失业率24.4%，仍为全球最高、近全球均值两倍，劳动力市场压力这一无明确终点判断在观察窗内出现。  
  来源：<https://www.ilo.org/sites/default/files/2024-08/MENA%20GET%20Youth%20Brief%202024.pdf>
- **#4** 「the populations of countries such as Italy, Japan, Russia and others in the industrial world will continue to …」  
  判断：**正确**。意大利2024年人口继续下降，日本2024年总人口同比减少55万；俄罗斯资料也显示2025年初人口低于2021年普查值。三个点名国家在观察窗内均出现人口收缩。  
  来源：<https://www.istat.it/wp-content/uploads/2025/03/DEMOGRAPHIC-INDICATORS_YEAR-2024.pdf>；<https://www.stat.go.jp/english/data/jinsui/2024np/>；<https://en.wikipedia.org/wiki/Demography_of_Russia>
- **#10** 「with increased intra-EU migratory ﬂows, there will be shifts in the composition of national populations over t…」  
  判断：**正确**。Eurostat记载2023年有150万人在欧盟国家间迁移、2024年1400万欧盟公民居于另一成员国；此前资料也显示不同国籍群体人数增减不一。人口流动改变成员国人口组成这一无明确终点方向在窗内得到支持。  
  来源：<https://ec.europa.eu/eurostat/web/interactive-publications/migration-2025>；<https://ec.europa.eu/eurostat/cache/digpub/demography_2022/bloc-3b.html?lang=en>
- **#12** 「with these countries again beginning to use their veto more frequently, to advance individual agendas or to co…」  
  判断：**正确**。安理会报告记载2024年七份草案因否决失败，为1986年以来最高；中俄美共投出八次否决。三国继续频繁动用否决权的近期方向已出现。  
  来源：<https://www.securitycouncilreport.org/monthly-forecast/2025-01/in-hindsight-the-security-council-in-2024-and-looking-ahead-to-2025.php>
- **#13** 「The resistance to change by permanent members of the Security Council with a veto will likely continue to be a…」  
  判断：**正确**。2025年研究直述常任理事国抵制削弱其影响力的结构改革；2026年11月材料仍记载改革谈判僵局，俄罗斯等抵制文本谈判。常任国阻力继续阻碍改革这一无明确终点判断成立。  
  来源：<https://www.accord.org.za/conflict-trends/un-security-council-reform-africas-quest-for-permanent-representation-and-veto-power/>；<https://www.stimson.org/2026/is-reforming-the-unsc-realistic-article-273-of-the-un-charter-offers-a-starting-point/>
- **#15** 「there is no certainty that, in the absence of further deployment of ﬁnancial resources to maintain a military …」  
  判断：**正确**。CRS记载塔利班2021年8月15日进入喀布尔、美国撤军8月30日完成，塔利班推进发生在撤军完成过程中。维持军事存在的投入停止后塔利班可能回归这一条件风险已经兑现。  
  来源：<https://www.congress.gov/crs_external_products/R/PDF/R46879/R46879.8.pdf>
- **#16** 「a ﬁgure quickly approaching US$ 2 trillion」  
  判断：**正确**。SIPRI统计2021年全球军费达到2.113万亿美元，首次超过2万亿。“迅速接近2万亿”的方向及规模在出版后不久兑现。  
  来源：<https://www.sipri.org/media/press-release/2022/world-military-expenditure-passes-2-trillion-first-time>
- **#18** 「However, political opposition could be strong, given powerful anti-tax sentiments in many countries such as th…」  
  判断：**正确**。C2ES对第119届国会的2026年资料明确指出联邦碳定价政策尚未通过，虽然部分州已有制度、国会有提案。美国联邦碳税近期仍遥远这一方向在已观察窗口内成立。  
  来源：<https://www.c2es.org/wp-content/uploads/2026/02/carbon-pricing-proposals-in-the-119th-Congress-FINAL.pdf>
- **#29** 「Staple crops may no longer grow where they had previously been mainstays of local populations.」  
  判断：**正确**。Crop Trust2025年的实地报道明确说津巴布韦Chimukoko许多农户已不能继续种稻，原因是气候变化使雨季过短。原文“原有地区主粮可能不再能生长”的无明确终点、局地可能性结果已出现。  
  来源：<https://www.croptrust.org/news-events/news/article/zimbabwes-crop-diversity-secured-in-svalbard/>

### 部分符合（9 条）

- **#1** 「Climate change, soil erosion, and overﬁshing are expected to reduce food production and are likely to put upwa…」  
  判断：**部分符合**。2022—24年多个极端天气事件伴随食品涨价，支持价格上行压力这一分项；但FAO2025年报告预计产量广泛回升、并记载谷物价格下压，不能将局地减产外推为全球粮食产量减少。  
  来源：<https://www.carbonbrief.org/mapped-16-times-extreme-weather-drove-higher-food-prices-since-2022>；<https://www.fao.org/newsroom/detail/fao-food-outlook-points-to-broad-based-increase-in-global-food-commodity-production/en>
- **#7** 「publics everywhere are showing growing dissatisfaction with the inability of national politics and politicians…」  
  判断：**部分符合**。OECD同组调查显示2021—23年政府信任小幅下降，支持部分不满上升；Pew2026年却显示多数调查国家无显著变化，日韩满意度明显提高。全球普遍继续加剧的强表述不能全部成立。  
  来源：<https://www.oecd.org/en/publications/oecd-survey-on-drivers-of-trust-in-public-institutions-2024-results_9a20554b-en/full-report/overview-new-trends-persistent-patterns-and-necessary-changes_f3abe0c7.html>；<https://www.pewresearch.org/short-reads/2026/06/10/americans-are-more-dissatisfied-with-how-their-democracy-is-working-than-people-in-other-high-income-countries/>
- **#11** 「migrants and displaced persons whose numbers will increase dramatically if climate change and resource destruc…」  
  判断：**部分符合**。IDMC资料显示内部流离失所总人数由2019年4910万升至2025年8220万，灾害类存量2024—25年也增加，结果方向部分出现；但“气候变化和资源破坏未被迅速控制”的前提没有统一可判定阈值，不能给条件命中。  
  来源：<https://www.iom.int/news/idmc-report-record-83-million-people-living-internal-displacement-worldwide>；<https://api.internal-displacement.org/sites/default/files/publications/documents/2026-idmc-global-report-on-internal-displacement-2026-summary-en.pdf>
- **#20** 「it is very probably an irreversible process.32 Policy-makers are not likely to be any more successful at stopp…」  
  判断：**部分符合**。WTO记载2025年货物和服务贸易量仍增长，显示跨境整合韧性；IMF同年却指出贸易开放度停滞和关税逆转。全球联系仍存在这一部分成立，但政策不能阻断、整体不可逆的强推断没有完全兑现。  
  来源：<https://www.wto.org/english/news%5Fe/news26%5Fe/anrp%5F09sep26%5F482%5Fe.htm>；<https://www.imf.org/en/publications/fandd/issues/2025/06/picture-this-trade-reckoning>
- **#25** 「There is no doubt in our minds that the IMF will be forced to play a central role in crisis management during …」  
  判断：**部分符合**。IMF2020年为80国提供约910亿美元融资，独立评估称反应有效而敏捷，确有重要危机管理参与；但G20财政支持超过10万亿美元，不能仅以参与和贷款国数证明IMF已在全球金融危机管理中居于“核心”。  
  来源：<https://www.imf.org/external/pubs/ft/ar/2020/eng/what-we-do/lending/>；<https://ieo.imf.org/en/-/media/ieo/files/evaluations/completed/03-20-2023-emergency-response-to-the-covid-19-pandemic/erp-chapeau-web-v2.pdf>；<https://www.imf.org/external/np/g20/pdf/2020/071620a.pdf>
- **#28** 「their increasing frequency and severity will push countries beyond their capacity to recover, requiring intern…」  
  判断：**部分符合**。世界银行对巴基斯坦2022年洪灾评估要求至少163亿美元恢复重建，并称国际支持对气候冲击恢复至关重要；OCHA2023年仍报告援助需求。灾害恢复依靠国际支持这一后果出现，但单一国家案例不足以确认全球频率和严重程度上升导致多国无力恢复的完整链条。  
  来源：<https://www.worldbank.org/en/news/press-release/2022/10/28/pakistan-flood-damages-and-economic-losses-over-usd-30-billion-and-reconstruction-needs-over-usd-16-billion-new-assessme>；<https://www.unocha.org/publications/report/pakistan/one-year-after-pakistan-monsoon-floods-2022-31-august-2023>
- **#30** 「This acidiﬁcation is already occurring and will impact all marine life that depends on calciﬁed shells or skel…」  
  判断：**部分符合**。IPCC报告酸化等压力影响海洋生态；2022年覆盖985项研究的综述却显示多类钙化生物对近期酸化耐受、反应差异明显。部分生物受影响有支持，但“所有”钙化生物这一全称范围没有被证明。  
  来源：<https://www.ipcc.ch/report/ar6/wg2/chapter/chapter-3/>；<https://pubmed.ncbi.nlm.nih.gov/35934837/>
- **#31** 「A new category of environmentally displaced persons includes those who migrate because rising sea levels, drou…」  
  判断：**部分符合**。灾害类内部流离失所存量从2023年770万到2024年980万、2025年约1360万，支持环境流离失所人数增加；但统计覆盖灾害而非全部环境迁移，且2025年移动次数下降。  
  来源：<https://www.migrationdataportal.org/climate-mobility-spotlight>；<https://api.internal-displacement.org/sites/default/files/publications/documents/250506_IDMC_Global_Report_Internal_Displacement_2025_Summary_ENG.pdf>；<https://api.internal-displacement.org/sites/default/files/publications/documents/2026-idmc-global-report-on-internal-displacement-2026-summary-en.pdf>
- **#33** 「We must anticipate greatly increased ﬂows of migrants.」  
  判断：**部分符合**。OECD永久迁移2024年比2019年高15%，2025年仍高12.5%，有增加分项；但2024、2025连续下降，且OECD不等于全球所有流量。全球迁移流大幅增加只能部分支持。  
  来源：<https://www.oecd.org/content/dam/oecd/en/publications/support-materials/2025/11/international-migration-outlook-2025_355ae9fd/Migration%20Outlook%20-%20infographic.pdf>；<https://www.oecd.org/en/about/news/press-releases/2026/11/migration-to-oecd-countries-declines-for-second-consecutive-year-but-remains-high-by-historical-standards.html?status=none>

### 错误（4 条）

- **#17** 「Given the sheer volume of persons currently displaced for a variety of reasons (which will only grow in the fo…」  
  判断：**错误**。UNHCR记录2024年底全球被迫流离失所人数1.232亿，而2025年底为1.178亿，出现明确年度下降。原文“只会增长”的单向强断言因此遇到反例。  
  来源：<https://www.unhcr.org/publications/global-trends-2024>；<https://www.unhcr.org/sites/default/files/2026-06/global-trends-report-2025.pdf>
- **#22** 「we think there is a high likelihood that the next ﬁnancial crisis will be ﬁscal in nature」  
  判断：**错误**。按2020年出版年窗口，随后2020年市场危机的研究将冲击根源归为疫情而非财政问题；2022年英国迷你预算虽引起国债压力，却不能倒置为“下一次”全球危机。财政起源这一主要判断不符。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC7665755/>；<https://www.chicagofed.org/publications/chicago-fed-letter/2023/480>
- **#23** 「in the absence of additional progress in currently frozen negotiations on a quota increase, it is expected tha…」  
  判断：**错误**。IMF第十五次份额审议于2020年以不增资结束，但2021年通过扩大NAB和新的双边借款将放贷能力维持约1万亿美元。未获份额增资而能力仍未减半，是该条件预测的反例。  
  来源：<https://www.imf.org/en/news/articles/2020/02/13/pr2050-imf-board-of-governors-approves-a-resolution-on-quota-reviews>；<https://www.imf.org/en/news/articles/2021/01/08/pr214-imf-concludes-steps-to-maintain-its-lending-capacity>
- **#24** 「Dealing with the next global ﬁnancial crisis in the context of sharply reduced ﬁscal space, when the tradition…」  
  判断：**错误**。2020年全球冲击中，IMF记载截至9月宣布的财政措施达11.7万亿美元，G20同时实施大规模货币宽松。传统工具仍被大规模使用，不符合“基本不再可用”。  
  来源：<https://www.imf.org/-/media/files/publications/fiscal-monitor/2020/october/english/ch1.pdf>；<https://www.imf.org/external/np/g20/pdf/2020/071620a.pdf>

### 暂无法判断（14 条）

- **#2** 「grow by more than 25 percent by 2040,19 reﬂecting the addition of some 1.7 billion people to the world’s popul…」  
  判断：**暂无法判断**。上下文将约17亿新增人口放在2040年；现有联合国材料给出2024/2025年约82亿人口，2040年尚未到来。未取得同口径的持续实绩及原基数来确认该增量的兑现程度，故不把新人口预测当成实绩。  
  来源：<https://www.un.org/en/UN-projects-world-population-to-peak-within-this-century>；<https://www.un.org/en/desa/WUP-2025>
- **#5** 「Migration has become a new issue of planetary scale and is anticipated to accelerate as climate change displac…」  
  判断：**暂无法判断**。IOM确认气候压力影响迁移，但同时强调多因交互和全球数据不足；IDMC灾害移动量2025年反而下降。尚缺可把天气灾害、冲突及重复撤离分开的气候归因迁移加速度序列。  
  来源：<https://worldmigrationreport.iom.int/what-we-do/world-migration-report-2026/chapter-6/climate-change-and-migration-understanding-context>；<https://api.internal-displacement.org/sites/default/files/publications/documents/2026-idmc-global-report-on-internal-displacement-2026-summary-en.pdf>；<https://www.frontiersin.org/journals/climate/articles/10.3389/fclim.2025.1570995/full>
- **#6** 「Military conscription is on its way out in most countries」  
  判断：**暂无法判断**。2024年跨国快照显示大量国家仍征兵，欧盟2025年资料则记录征兵重新受到重视；这些都不能回答2020年以后全球“多数国家”是否正在退出。已改查跨国面板，但公开页面未给出所需的近年完整序列。  
  来源：<https://www.europarl.europa.eu/RegData/etudes/BRIE/2025/769541/EPRS_BRI(2025)769541_EN.pdf>；<https://gnv.news/archives/24690>；<https://www.uptoninstitute.org/data/military-recruitment>
- **#8** 「the two countries will never again be at war with each other」  
  判断：**暂无法判断**。德国外交部2026年描述法德安全合作密切并在2022年后加强，支持当前和平合作状态；但截至截止日的一段和平无法证明“永不再战”。  
  来源：<https://www.auswaertiges-amt.de/en/aussenpolitik/europe/cooperation-in-europe/german-french-cooperation-228748>
- **#9** 「creation of a United Nations Parliamentary Assembly” and that the UN “must address the democratic deﬁcit withi…」  
  判断：**暂无法判断**。2025年联合国/IPU报告记载与各国议会合作扩大，UNPA倡议材料也有支持及民调；但这些不是部分大国实际反对另设UNPA的证据。经机构材料定向补查仍缺观察窗内可归属的直接反对表态。  
  来源：<https://www.ipu.org/file/21575/download>；<https://www.unpacampaign.org/proposal/milestones/>
- **#14** 「Nuclear mass extermination was never and is hardly ever likely to be an attractive political option.」  
  判断：**暂无法判断**。原文说的是核“大规模灭绝”作为政治选项的吸引力，不是简单预测核武器不被使用。SIPRI的未使用记录及RAND关于有限核使用情景的分析均不能直接测量前者，缺少其可操作的结果指标。  
  来源：<https://www.sipri.org/sites/default/files/SIPRIYB25c01.pdf>；<https://www.rand.org/pubs/research_reports/RRA3859-1.html>
- **#19** 「Sooner or later, it is very likely that the global population crisis will emerge」  
  判断：**暂无法判断**。联合国/FAO仍记录严重饥饿，但英国粮食安全报告指出全球总食物量足够，FAO2026年又记录饥饿率下降。作者没有给出“全球人口危机爆发”的阈值或有限时间，现有资料不能将地区饥饿等同于该事件。  
  来源：<https://www.gov.uk/government/statistics/united-kingdom-food-security-report-2024/united-kingdom-food-security-report-2024-theme-1-global-food-availability>；<https://www.fao.org/newsroom/detail/sofi-2026--hunger-not-inevitable--fao-says-as-global-hunger-report-shows-progress/en>
- **#21** 「Climate-induced migration will accelerate」  
  判断：**暂无法判断**。天气灾害移动2024年大幅上升，但归因综述明确指出长期气候变化对已观察全球迁移的贡献尚未量化。不能从灾害次数推导出气候引致迁移已经加速。  
  来源：<https://news.un.org/en/story/2025/05/1163176>；<https://www.frontiersin.org/journals/climate/articles/10.3389/fclim.2025.1570995/full>；<https://api.internal-displacement.org/sites/default/files/publications/documents/2026-idmc-global-report-on-internal-displacement-2026-summary-en.pdf>
- **#26** 「Parts of the planet will become less able to support a human population, or even uninhabitable, due to excessi…」  
  判断：**暂无法判断**。热风险综述确认极端热可致命，IPCC也报告健康风险，但所选材料没有给出出版后具体区域因过高气温而持续丧失居住承载力的可比观察。后续搬迁检索多为冻土融化等不同机制，不能移作生理热不宜居的命中。  
  来源：<https://www.nature.com/articles/s43017-024-00635-w>；<https://www.ipcc.ch/report/ar6/wg2/chapter/chapter-7/?utm=>
- **#27** 「Since about 100 million people currently live less than 1 meter above sea level, and many others will be threa…」  
  判断：**暂无法判断**。IPCC给出未来沿海风险暴露，联合国2025年说太平洋至少37个社区被列为拟搬迁；这不是全球已经发生的永久迁移数量。缺少可与过去同等时长比较的去重永久迁移序列，无法证明“超过以往任何规模”。  
  来源：<https://www.ipcc.ch/report/ar6/wg2/downloads/outreach/IPCC_AR6_WGII_FactSheet_SLR.pdf>；<https://www.undrr.org/resource/case-study/understanding-disaster-displacement-and-assessing-future-risk>；<https://pacific.un.org/en/299779-rc-remarks-iom-development-partner-roundtable-%E2%80%93-climate-mobility-pacific-%E2%80%93-series-1-planned>
- **#32** 「accelerating climate change, are going to displace hundreds of millions of people in the decades ahead」  
  判断：**暂无法判断**。世界银行的2.16亿为2050年情景上限，RAND提醒估计可在4400万到2.16亿间、旧模型永久离开的假设有问题。未有数亿人离家的实测统计，几十年后的预测不能由另一预测替代验收。  
  来源：<https://www.worldbank.org/en/news/press-release/2021/09/13/climate-change-could-force-216-million-people-to-migrate-within-their-own-countries-by-2050>；<https://www.rand.org/pubs/commentary/2024/11/understanding-climate-migration.html>
- **#34** 「The time may well come in the future when governments will see the need for an ofﬁcial international auxiliary…」  
  判断：**暂无法判断**。联合国目前列出六种官方语言，2024年大会决议继续强调其平等和多语制。两者都不证明各国政府未来不会认识到单一辅助语的需要，也未提供其已正式认可的事实；原文没有期限。  
  来源：<https://www.un.org/en/our-work/official-languages>；<https://treaties.un.org/doc/source/a_res_78_330-English.pdf>
- **#35** 「Einstein was right when he wrote that “the destiny of civilized humanity depends more than ever on the moral f…」  
  判断：**暂无法判断**。2024年俄罗斯反对《未来契约》、安理会改革争执可见，但它们并不等同于针对重启宪章修订讨论的特别强烈反应。2025—26年Article109资料仍以倡议及程序设计为主，缺少与原对象直接对应的常任国反应证据。  
  来源：<https://www.dw.com/en/un-reform-plan-adopted-despite-russian-opposition/a-70295441>；<https://article109.org/2025/10/02/let-it-roll-article-109-at-unga80/>；<https://www.stimson.org/2026/negotiation-process-design-is-key-for-article-109-un-charter-review/>
- **#36** 「Civil society organizations are active in public discourses and have built mature international coalitions in …」  
  判断：**暂无法判断**。2024年联合国会议有逾2150名代表，显示合作活动存在；OHCHR同年却报告跨境团结网络面临审查、限制数字平台等压力。没有统一可比的国际公民社会合作量序列及ICT贡献指标，不能据单次盛会判持续只增。  
  来源：<https://www.un.org/sites/un2.un.org/files/final_2024uncsc_report_part_i.pdf>；<https://www.ohchr.org/en/documents/thematic-reports/ahrc5657-participation-civil-society-organizations-seeking-express>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/lopez-claros-global-governance-21st-century-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/lopez-claros-global-governance-21st-century-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/lopez-claros-global-governance-21st-century-v5/audit/manual_review_2026-11-15.py`
## 口径与执行说明

- 此报告canonical表中的“候选36/非预测0”仅指resolvable集合；完整导入候选为51，其中流水线unclear 15，不进入评分，全部仍保留于claims.jsonl，pipeline报告有完整计数。最终预测36，可判定22，正确9/趋势0/部分9/错误4/未定14。
- 为满足context清空后的reference_support规则，6条指代句扩展至包含先行句，均为原TXT连续片段。贫困率上升及巴黎承诺两个真实向前判断因含2015等历史年份被未改动的英文筛选规则排除historical（2），不是人工改unclear；此为原确定性规则的英文局限，保留policy_report与proposals审计。不修改工具以绕过。
- 少数必要引文超过300字符（人口、UNPA、宪章讨论），这是连续引文，不是全文或chunk body；所有context为空，所有batch plan和模型request等含全书的中间件移出case和bundle。
- 第三轮换策略主题（按扩句前38项编号）：3巴黎长期温度阈值、4人口实绩/2040终点、7及23气候迁移归因加速度、8全球征兵面板、10法德永不战争、11机构对UNPA直接反对、16核灭绝政治效用定义、21人口危机阈值、28高温居住性实测、29永久搬迁历史可比规模、31主粮原产区实地停种、34数亿去重气候移民、36政府辅助语正式立场、37宪章审议讨论反应、38NGO登记与实际合作量。原因是首轮/定向第二轮多为模型、错口径或间接指标；各仅2条新query，≤5。31补查获得津巴布韦稻作实地证据后判正确。
- 三项2020年全球危机判断按出版年代理窗口核验，无法精确到原出版日，已在相关limitation声明同年时序敏感。
- 继承的本地check_answers.py使用config的publication_year_proxy而非1919；fix_answer.py从w8复制。本次仅调整本地research.py、verify_apply.py读取用户指定新Exa密钥路径优先、旧池第4行备用；只内部按路径读取，未输出或打包密钥。repo/toolkit未修改，canonical manual_report.py md5=682248fa9f6c63e3492a559ccac12761。
- 未调用DeepSeek、未开子任务、未commit/push/PR、未改其他worker的锁或已接受case。评分是回溯父记录统计，不是独立预测技能估计。

