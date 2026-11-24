# 英国制造业的未来（GO-Science 2013，返工版）：出版后预测人工核查

- 案例目录：`cases/uk-goscience-future-of-manufacturing-v5/`
- 出版日期：2013-10
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

按METHOD.md人工替代模型调用，其余使用toolkit 85e6da1原代码。219块全部通读；本次逐条恢复60项原始forecast字段，未按跨段重复或密度人工降unclear。Box7.1按PDF203页左右栏顺序实际阅读，新增17条手写答案（10预测、7非预测）；原有价格波动预测另保留。重新validate/claims_from_results/import，300候选、234可核验。只允许原claims_from_results自动重叠规则去重（本案0项）；ASSESS不作额外语义去重。原9项均恢复forecast，没有据非预测规则继续排除的项目。先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 234 条，剔除非预测 0 条，计入 **234 条预测**，其中 **188 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 81 |
| 趋势符合 | 13 |
| 部分符合 | 74 |
| 错误 | 20 |
| 暂无法判断 | 46 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **43.1%**（81/188） |
| 加权胜率 | **68.0%** |
| 错误率 | **10.6%**（20/188） |
| 未定占比（暂无法判断/预测） | 19.7%（46/234） |

## 总体评价

技术数字化与服务化方向多有进展，循环制造、空间布局及技能结构变化并不均衡；长期终点与缺少直接指标的命题仍保留暂无法判断。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（81 条）

- **#5** 「manufacturers make use of the increasing pervasiveness of ‘Big Data’」  
  判断：**正确**。大数据/数据分析已成为制造商核心技术用例：Gartner调查显示81%的制造业领导者把数据与分析用于流程改进列为最重要技术用例；ABI 2024调查76%制造商使用云平台做实时协作与供应链。  
  来源：<https://fonsecaadvisers.com/wp-content/uploads/2024/09/Gartner-manufacturing-emerging-technology-priorities-and-progress-by-use-case.pdf>；<https://www.abiresearch.com/press/study-shows-76-of-discrete-and-process-manufacturers-use-cloud-platforms-for-real-time-collaboration-and-supply-chain-efficiency>
- **#7** 「New sources of revenue and of value creation will transform manufacturing business models over time.」  
  判断：**正确**。制造服务已实质改变收入模式：Bain对51家工业企业2020年调查显示服务平均占收入35%、利润60%；2024年服务化综述确认企业从产品中心转向服务中心的模式。  
  来源：<https://www.bain.com/insights/services-build-value-for-the-industrial-sector-snap-chart/>；<https://www.techtarget.com/news/Manufacturers-turn-to-servitization-for-competitive-advantage/852858/>；<https://www.pwc.com/hu/en/kiadvanyok/assets/pdf/sharing-economy-en.pdf>；<https://www.brookings.edu/articles/the-current-and-future-state-of-the-sharing-economy/>；<https://doi.org/10.31893/multirev.2024201>
- **#8** 「Future sources of revenue for manufacturers will include26:  Increasingly extensive packaging of services w…」  
  判断：**正确**。服务化收入上升已被证实：Bain 2020年对51家工业企业调查显示服务平均占收入35%、利润60%；IDC服务化晴雨表调查421家生产型企业向服务化模式转型的成熟度。  
  来源：<https://www.bain.com/insights/services-build-value-for-the-industrial-sector-snap-chart/>；<https://www.techtarget.com/news/Manufacturers-turn-to-servitization-for-competitive-advantage/852858/>
- **#16** 「The range of biotechnology products is likely to increase, with greater use of fields of biology by industry.」  
  判断：**正确**。工业对生物学利用扩大：个性化药物连续四年超过FDA新药批准的三分之一，合成生物学被用于生物燃料与化学品（NREL-LanzaTech项目），生物技术产品范围持续扩大。  
  来源：<https://www.personalizedmedicinecoalition.org/in-2023-personalized-medicines-topped-one-third-of-new-drug-approvals-for-fourth-year-in-a-row/>；<https://www.nlr.gov/news/detail/program/2023/nrel-launches-synthetic-biology-project-to-advance-biofuel-discovery-technologies-with-lanzatech-northwestern-and-yale>
- **#17** 「the volume and detail of information captured by businesses and the rise of multimedia, social medial and the …」  
  判断：**正确**。数据量持续增长：IDC估计2025年全球数据圈约173.4ZB，预计2029年达527.5ZB；IoT Analytics统计2024年联网IoT设备188亿台、年增13%。  
  来源：<https://www.qualstar.com/archive/how-hyperscale-data-growth-is-changing-the-future-of-cold-storage>；<https://iot-analytics.com/number-of-connected-iot-devices-2024/>
- **#24** 「Pervasive computing, advanced software and sensor technologies have much further to go in transforming value c…」  
  判断：**正确**。ABI 2024年调查中76%的制造业受访者已部署云方案促进供应商等实时协作；Deloitte记录智能制造的实际产出改善，技术进一步改变价值链的方向得到证实。  
  来源：<https://www.deloitte.com/us/en/about/press-room/deloitte-2025-smart-manufacturing-survey.html>；<https://www.bcg.com/publications/2024/shaking-up-the-factory-floor-with-digital-and-ai>；<https://www.abiresearch.com/press/study-shows-76-of-discrete-and-process-manufacturers-use-cloud-platforms-for-real-time-collaboration-and-supply-chain-efficiency>；<https://www.bain.com/insights/services-build-value-for-the-industrial-sector-snap-chart/>；<https://www.techtarget.com/news/Manufacturers-turn-to-servitization-for-competitive-advantage/852858/>
- **#27** 「High-tech likely to remain an area of UK advantage」  
  判断：**正确**。高技术仍是英国优势：LSE研究指出英国在航空航天、制药等高技术品类出口占比高于平均；剑桥CIIP显示制药、运输设备仍是关键产业。  
  来源：<http://eprints.lse.ac.uk/117344/1/Oliveira_Cunha_enduring_strengths_published.pdf>；<https://www.ciip.group.cam.ac.uk/innovation/structure-and-performance-of-the-uk-economy-25/>
- **#31** 「FDI flows into Europe, as a proportion of total available FDI, are likely to reduce due to competition from BR…」  
  判断：**正确**。UNCTAD《世界投资报告2024》显示欧洲FDI流入大幅波动并在2022年为负(-1060亿美元)、2023年仅160亿美元；EY称2024年欧洲FDI项目降至九年最低，欧洲占全球FDI比重下降。  
  来源：<https://unctad.org/publication/world-investment-report-2024>；<https://trendsgroup.org/insight/the-world-investment-trends-and-sdgs-funding-challenges/>；<https://www.ey.com/en_gl/newsroom/2025/05/fdi-in-europe-slows-but-confidence-remains-for-long-term-rebound>
- **#37** 「UK manufacturers will be affected by challenges such as the disruption of their international supply chains.」  
  判断：**正确**。极端天气对供应链的扰动增多：2021年德州冰冻导致石化供应链中断至年底，NC State分析指天气相关供应链中断呈上升趋势。  
  来源：<https://www.dallasfed.org/research/swe/2021/swe2102/swe2102c>；<https://scm.ncsu.edu/scm-articles/article/the-increasing-role-of-climate-change-in-supply-chain-disruptions>
- **#39** 「Regulation is likely to focus increasingly on promoting resource productivity.」  
  判断：**正确**。监管日益侧重资源生产率：欧盟2024年通过《可持续产品生态设计法规》(ESPR)，把耐用、可修复、可回收等资源效率要求扩展到几乎所有产品。  
  来源：<https://eur-lex.europa.eu/eli/reg/2024/1781/2024-06-28/eng>；<https://www.consilium.europa.eu/en/press/press-releases/2024/05/27/green-transition-council-gives-its-final-approval-to-the-ecodesign-regulation/>
- **#45** 「the UK will have an ageing population, with the number of people aged 65 years and over (i.e. of ‘traditional’…」  
  判断：**正确**。ONS 2022年基期人口预测显示65岁及以上人口持续增加，英国人口老龄化。  
  来源：<https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationprojections/bulletins/nationalpopulationprojections/2022based>
- **#48** 「Future demand is currently likely to exceed supply」  
  判断：**正确**。EngineeringUK 2023报告与Make UK均指出工程/STEM技能需求未被供给满足，2026年制造业仍有约4.8万个空缺。  
  来源：<https://www.engineeringuk.com/research-and-insights/our-research-and-evaluation-reports/engineering-skills-needs-now-and-into-the-future/>；<https://www.makeuk.org/insights/publications/make-uk-calls-immigration-reform-tackle-manufacturing-skills-shortages>
- **#49** 「These blends of high quality skills will allow developed economies such as the UK to increasingly compete in t…」  
  判断：**正确**。Make UK研究指出制造商所需技术层次日益提高，领导管理与技术岗位技能同时重要；工程人才短缺材料也证实劳动力素质成为竞争约束。  
  来源：<https://www.makeuk.org/docs/skills-2030-closing-gap-report-web/download>；<https://www.imeche.org/news/news-article/new-recruits-%27lack-skills-for-digital-transformation%27-large-manufacturing-companies-complain>；<https://www.engineeringuk.com/research-and-insights/our-research-and-evaluation-reports/engineering-skills-needs-now-and-into-the-future/>
- **#53** 「Manufacturers are increasingly using a wider value chain26 to embrace new sources of revenue, which will trans…」  
  判断：**正确**。Bain对2020年51家工业企业的调查显示服务平均占收入35%、利润60%；IDC的421家生产企业调查亦观察到从售产品向售服务和结果转型。无日期方向判断在出版后窗口已有实绩，商业模式变化判正确。  
  来源：<https://www.bain.com/insights/services-build-value-for-the-industrial-sector-snap-chart/>；<https://www.techtarget.com/news/Manufacturers-turn-to-servitization-for-competitive-advantage/852858/>
- **#59** 「the UK and other developed economies will increasingly need to compete using the quality of their workforces.」  
  判断：**正确**。Make UK调查发现企业所需技能层级不断提高、正在增加现有员工的技能升级；2024年数字化技能短缺已构成制造商现实约束。这里预测的是竞争对劳动力质量的需求增加，并非要求政府采取某政策，因此保留forecast，按已观察方向判正确。  
  来源：<https://www.makeuk.org/docs/skills-2030-closing-gap-report-web/download>；<https://www.imeche.org/news/news-article/new-recruits-%27lack-skills-for-digital-transformation%27-large-manufacturing-companies-complain>
- **#60** 「extreme weather events fuelled by climate change may disrupt vulnerable global supply chains」  
  判断：**正确**。极端天气扰乱全球供应链已多次出现：2021年德州冰冻扰乱石化供应，NC State指出天气导致的供应链中断上升。  
  来源：<https://www.dallasfed.org/research/swe/2021/swe2102/swe2102c>；<https://scm.ncsu.edu/scm-articles/article/the-increasing-role-of-climate-change-in-supply-chain-disruptions>
- **#61** 「future advanced and information-rich products may be particularly vulnerable to cyber-attack.」  
  判断：**正确**。IBM X-Force报告制造业第三次被列为遭受网络攻击最多的行业（占安全事件逾25%），信息密集产品/系统易受攻击得到证实。  
  来源：<https://cybermagazine.com/articles/why-does-manufacturing-see-the-most-cyber-attacks>
- **#62** 「diverse changes will play out in a world that will be increasingly wealthy, urban and interconnected.」  
  判断：**正确**。UBS记录世界财富在2022年下滑后恢复长期增长，ITU记录2024年联网人口55亿、占68%，联合国记录城市化继续推进；三项总体方向得到支持。  
  来源：<https://thehometrust.com/wp-content/uploads/2024/09/UBS-global-wealth-report-2024-1.pdf>；<https://www.itu.int/itu-d/reports/statistics/2024/11/10/ff24-internet-use/>；<https://thedocs.worldbank.org/en/doc/ec3d46c25a822d6d248e86d17179ea4e-0090012024/original/Poverty-and-Inequality-Quarterly-Update-3PR-Edition.pdf>；<https://www.un.org/en/desa/68-world-population-projected-live-urban-areas-2050-says-un>
- **#64** 「Future sources of new and additional revenue for manufacturers are likely to include the following3:  Sellin…」  
  判断：**正确**。服务与产品捆绑销售扩大：Bain 2020年调查与IDC服务化晴雨表均显示工业企业加大服务业务。  
  来源：<https://www.bain.com/insights/services-build-value-for-the-industrial-sector-snap-chart/>；<https://www.techtarget.com/news/Manufacturers-turn-to-servitization-for-competitive-advantage/852858/>
- **#68** 「This is likely to be an important trend for manufacturers to embrace」  
  判断：**正确**。服务化已成为制造商重要趋势：IDC对421家生产型企业调查与Bain工业服务调查均证实。  
  来源：<https://www.techtarget.com/news/Manufacturers-turn-to-servitization-for-competitive-advantage/852858/>；<https://www.bain.com/insights/services-build-value-for-the-industrial-sector-snap-chart/>
- **#69** 「A number of other business models are likely to become more common in the decades ahead」  
  判断：**正确**。Bain工业服务调查与2024年服务化综述均记录制造商采用新的服务收入方式，共享租赁平台也扩展；多种新模式更普遍的方向符合。  
  来源：<https://www.bain.com/insights/services-build-value-for-the-industrial-sector-snap-chart/>；<https://www.techtarget.com/news/Manufacturers-turn-to-servitization-for-competitive-advantage/852858/>；<https://www.pwc.com/hu/en/kiadvanyok/assets/pdf/sharing-economy-en.pdf>；<https://www.brookings.edu/articles/the-current-and-future-state-of-the-sharing-economy/>；<https://doi.org/10.31893/multirev.2024201>
- **#72** 「Personalised medicine aimed at individuals or segments of the population become established as prognostic and …」  
  判断：**正确**。个性化医疗已确立：个性化药物连续四年（至2023年）超过FDA新药批准的三分之一。  
  来源：<https://www.personalizedmedicinecoalition.org/in-2023-personalized-medicines-topped-one-third-of-new-drug-approvals-for-fourth-year-in-a-row/>
- **#75** 「In the US, Walmart are developing a sustainability metric which may become widely used across retailing in the…」  
  判断：**正确**。沃尔玛可持续性指数演化为THESIS系统，被沃尔玛、Target、亚马逊、Sam’s Club、Walgreens、Kroger等零售商用于评估供应商。  
  来源：<https://sustainablebrands.com/read/thesis-tsc-s-newest-way-for-retailers-to-track-supplier-sustainability-performance>；<https://sustainabilityconsortium.org/tsc-report-shows-companies-with-science-based-targets-more-likely-to-improve-sustainability-of-consumer-product-supply-chains/>
- **#76** 「Advances in IT are expected to have profound implications for manufacturing business models」  
  判断：**正确**。云协作、产品数据与服务化已改变制造商服务交付方式；ABI调查的实际云部署与Bain记录的服务收入说明IT对商业模式的影响已经发生。  
  来源：<https://www.deloitte.com/us/en/about/press-room/deloitte-2025-smart-manufacturing-survey.html>；<https://www.bcg.com/publications/2024/shaking-up-the-factory-floor-with-digital-and-ai>；<https://www.abiresearch.com/press/study-shows-76-of-discrete-and-process-manufacturers-use-cloud-platforms-for-real-time-collaboration-and-supply-chain-efficiency>；<https://www.bain.com/insights/services-build-value-for-the-industrial-sector-snap-chart/>；<https://www.techtarget.com/news/Manufacturers-turn-to-servitization-for-competitive-advantage/852858/>
- **#79** 「The ability of firms to coordinate activity through collaborative, inter-organisational connections is likely …」  
  判断：**正确**。ABI调查中76%的受访制造商已用云方案提高跨供应商、分销商和伙伴的数据可获得性与协调效率，支持跨组织协调能力增强。  
  来源：<https://www.abiresearch.com/press/study-shows-76-of-discrete-and-process-manufacturers-use-cloud-platforms-for-real-time-collaboration-and-supply-chain-efficiency>；<https://journals.sagepub.com/doi/full/10.1177/0308518X231202390>
- **#81** 「The manufacturing sector is likely to continue evolving, with value created in increasingly diverse ways.」  
  判断：**正确**。Bain记录工业服务占收入和利润的重要份额，2024年服务化综述确认产品升级、安装、维护等多种服务方式被采用，价值创造多样化的方向成立。  
  来源：<https://www.bain.com/insights/services-build-value-for-the-industrial-sector-snap-chart/>；<https://www.techtarget.com/news/Manufacturers-turn-to-servitization-for-competitive-advantage/852858/>；<https://www.pwc.com/hu/en/kiadvanyok/assets/pdf/sharing-economy-en.pdf>；<https://www.brookings.edu/articles/the-current-and-future-state-of-the-sharing-economy/>；<https://doi.org/10.31893/multirev.2024201>
- **#82** 「Changes in business models and other areas will result in a more interconnected manufacturing system, with pro…」  
  判断：**正确**。ABI的76%云平台部署及制造商跨伙伴实时协作，连同智能制造调查记录的数据连接，支持制造体系互联程度上升。  
  来源：<https://www.deloitte.com/us/en/about/press-room/deloitte-2025-smart-manufacturing-survey.html>；<https://www.bcg.com/publications/2024/shaking-up-the-factory-floor-with-digital-and-ai>；<https://www.abiresearch.com/press/study-shows-76-of-discrete-and-process-manufacturers-use-cloud-platforms-for-real-time-collaboration-and-supply-chain-efficiency>；<https://www.bain.com/insights/services-build-value-for-the-industrial-sector-snap-chart/>；<https://www.techtarget.com/news/Manufacturers-turn-to-servitization-for-competitive-advantage/852858/>
- **#91** 「other drivers, including global resource scarcity and environmental concerns18 will promote the use of sustain…」  
  判断：**正确**。欧洲塑料工业2026年报告记录2022至2024年循环塑料产出仍年均增长1.2%、需求增长4%，全球循环塑料产出年均增7.7%；可持续材料使用增加的方向成立。  
  来源：<https://plasticseurope.org/media/circular-economy-report-2026-dramatic-slowdown-in-plastics-circularity/>；<https://green-alliance.org.uk/wp-content/uploads/2024/08/Policy-barriers-to-greening-the-chemical-industry.pdf>
- **#93** 「The maturation of additive technologies will significantly expand the ability to create hybrid, tailored and g…」  
  判断：**正确**。2024年功能梯度材料综述记录增材技术已能合成具有定制属性和功能的结构，并讨论多材料与分层制造，所预测制造能力扩展已经出现。  
  来源：<https://www.mdpi.com/2504-4494/8/1/23>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC11432905/>
- **#96** 「are connected to the internet, will become commonplace.」  
  判断：**正确**。联网产品已普遍：2024年联网IoT设备188亿台，2025年约211亿台。  
  来源：<https://iot-analytics.com/number-of-connected-iot-devices-2024/>；<https://iot-analytics.com/number-connected-iot-devices/>
- **#97** 「Likely developments include autonomous vehicle navigation in city centres」  
  判断：**正确**。城市中心自动驾驶已出现：Waymo 2024年向旧金山全体用户开放无人驾驶网约车，付费行程数三个月翻倍。  
  来源：<https://www.cnbc.com/2024/06/25/waymo-opens-robotaxi-service-to-all-san-francisco-users.html>；<https://www.reuters.com/business/autos-transportation/alphabets-waymo-robotaxi-unit-doubles-its-paid-rides-three-months-2024-08-20/>
- **#103** 「Over the next two decades, the range of biotechnology products is set to expand, with revenues expected to gro…」  
  判断：**正确**。市场研究估计2020年全球生物技术市场约6276亿美元（ResearchAndMarkets）至7529亿美元（Grand View），达到或超过6000亿美元。  
  来源：<https://www.businesswire.com/news/home/20210824005591/en/Insights-on-the-%24627-Billion-Biotechnology-Global-Market-to-2026---Key-Drivers-and-Challenges---ResearchAndMarkets.com>；<https://doi.org/10.1051/e3sconf/202129501037>
- **#104** 「Firms will increasingly favour resilient supply chains, with built-in redundancy which allows adaptation to di…」  
  判断：**正确**。McKinsey 2023供应链调查显示企业普遍采用双重采购、增加库存与区域化以提高韧性；Axios报道近岸化企业比例当年近三倍。  
  来源：<https://www.mckinsey.com/capabilities/operations/our-insights/tech-and-regionalization-bolster-supply-chains-but-complacency-looms>；<https://www.axios.com/2023/08/15/share-of-companies-nearshoring-their-supply-chains-tripled-this-year-survey>
- **#105** 「More resilient supply chains are likely to be shorter with fewer links, and include more local suppliers with …」  
  判断：**正确**。近岸化/区域化供应链增多：McKinsey 2023调查近岸化比例约三倍；英国工厂转向本地供应商（Reuters 2023）。  
  来源：<https://www.mckinsey.com/capabilities/operations/our-insights/tech-and-regionalization-bolster-supply-chains-but-complacency-looms>；<https://www.axios.com/2023/08/15/share-of-companies-nearshoring-their-supply-chains-tripled-this-year-survey>；<https://www.reuters.com/world/uk/more-uk-factories-turn-away-foreign-suppliers-survey-shows-2023-03-07/>
- **#109** 「An integration of artificial intelligence (AI), natural user interfaces (NUI), more intuitive computing and ne…」  
  判断：**正确**。AI与大数据持续推动任务自动化：生成式AI出现后，KPMG、McKinsey等估计大量任务可被自动化，自动化扩展到更多知识型任务。  
  来源：<https://assets.kpmg.com/content/dam/kpmgsites/uk/pdf/2023/06/generative-ai-and-the-uk-labour-market.pdf>；<https://www.mckinsey.com/%7E/media/mckinsey/mckinsey%20global%20institute/our%20research/generative%20ai%20and%20the%20future%20of%20work%20in%20america/generative-ai-and-the-future-of-work-in-america-vf1.pdf>
- **#110** 「The expanding volume and detail of information captured by businesses and the rise of multimedia, social media…」  
  判断：**正确**。数据量持续大幅增长：IDC估计全球数据圈2025年约173ZB、2029年达527.5ZB。  
  来源：<https://www.qualstar.com/archive/how-hyperscale-data-growth-is-changing-the-future-of-cold-storage>
- **#111** 「communications, are likely to be able to ‘talk to’ intranets and the rest of the internet within the next coup…」  
  判断：**正确**。物联网已成现实：2024年联网IoT设备188亿台、蜂窝IoT连接超40亿，早于“约20年”的时间框架实现。  
  来源：<https://iot-analytics.com/number-of-connected-iot-devices-2024/>；<https://iot-analytics.com/number-connected-iot-devices/>
- **#113** 「Manufacturing execution systems (MES) are likely to become more important.」  
  判断：**正确**。2024年MES指南引用LNS称MES采用率2019至2023年翻倍；ARC亦将MES/MOM列为制造数字转型核心，重要性上升方向符合。  
  来源：<https://www.criticalmanufacturing.com/wp-content/uploads/2024/05/Tech-Clarity-MES-Buyers-Guide-2024.pdf>；<https://www.arcweb.com/press/manufacturing-execution-systems-mesmom-vital-digital-transformation>
- **#116** 「On the human front, 3D vision will be able to track gestures, body motion, gaze and recognise faces」  
  判断：**正确**。3D视觉追踪人脸已普及：苹果2017年推出Face ID深度感知人脸识别，此后TrueDepth传感器进入每款新iPhone。  
  来源：<https://en.wikipedia.org/wiki/Face_ID>；<https://arstechnica.com/gadgets/2018/09/video-a-quick-explainer-on-truedepth-the-tech-thats-in-every-new-iphone/>
- **#117** 「manufacturers will rely increasingly on energy intelligence to monitor and control energy consumption」  
  判断：**正确**。Omdia对制造商能源管理调查记录31%已跨多个设施完整部署数字用能优化工具，43%在单厂部署，能源智能成为实际生产管理方式。  
  来源：<https://get.spacewell.com/hubfs/%5BDEXMA%5D/%5BDEXMA%5D%20Surveys%20and%20Reports/%5BDEXMA%5D%20Surveys%20and%20Reports%20Materials/EN%20-%20Energy%20Survey%202024%20Spacewell%20Energy%20-%20Report.pdf>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC10806267/>；<https://literature.rockwellautomation.com/idc/groups/literature/documents/sp/rok-sp001_-en-p.pdf>
- **#118** 「The growing trends in industry to improve corporate sustainability and implement energy and carbon reduction t…」  
  判断：**正确**。SBTi到2024年已有超过6000家企业通过科学减排目标验证，其中电子设备机械475家、食品饮料加工341家，目标扩展趋势持续。  
  来源：<https://sciencebasedtargets.org/blog/climate-action-milestone-6-000-companies-adopt-science-based-targets>；<https://www.bloomberg.com/news/features/2025-06-12/climate-pledges-dropped-by-coca-cola-bp-hsbc-as-planet-heats-up>
- **#119** 「New techniques such as hydraulic fracturing of shale rocks or ‘fracking’, horizontal drilling and microseismic…」  
  判断：**正确**。水力压裂与水平钻井推动页岩油气：美国原油产量2024年达1330万桶/日创纪录，主要来自二叠纪致密油。  
  来源：<https://oilprice.com/Latest-Energy-News/World-News/Annual-US-Crude-Production-Sets-New-Record-in-2024-But-Growth-Pace-Slows-EIA.html>；<https://www.eia.gov/todayinenergy/detail.php?id=65404>
- **#125** 「Simulation technologies will play a greater role in training the work force before they set foot on the shop f…」  
  判断：**正确**。Permco在疫情后用CAD建立VR装配培训并衍生新技术企业，ABI 2024调查也记录32%制造业受访者处于XR实际实施阶段，上岗培训仿真作用增大已经出现。  
  来源：<https://www.digitalengineering247.com/article/vr-models-streamline-training-for-manufacturer>；<https://www.abiresearch.com/press/survey-finds-32-of-discrete-and-process-manufacturers-are-implementing-xr-technologies-into-their-operations>
- **#132** 「In the decades ahead, it is likely that leaders such as RollsRoyce plc will be joined by other manufacturers u…」  
  判断：**正确**。更多制造商在全球销售服务：Bain与IDC调查均显示工业企业服务收入与服务化战略扩大。  
  来源：<https://www.bain.com/insights/services-build-value-for-the-industrial-sector-snap-chart/>；<https://www.techtarget.com/news/Manufacturers-turn-to-servitization-for-competitive-advantage/852858/>
- **#142** 「it is likely that this industry will be challenged in the future by growth in the ICT sector」  
  判断：**正确**。英国印刷业受数字替代冲击：IBISWorld指出数字替代品流行削弱印刷需求，BPIF显示2020年营收下降19%。  
  来源：<https://www.ibisworld.com/united-kingdom/industry/printing/985/>；<https://printbusiness.co.uk/industry-is-bouncing-back-says-bpif/>
- **#143** 「Demand for new products will increase from emerging economies, creating strong market opportunities.」  
  判断：**正确**。Bain记录2023年新兴市场贡献全球消费品销量增长的绝大部分，产品需求增加的总体方向成立。  
  来源：<https://www.bain.com/globalassets/noindex/2024/bain_report_consumer_products_report-2024.pdf>；<https://research.jgu.edu.in/how-consumption-slowdown-meets-persistent-inequality/>
- **#146** 「As the global economy changes and future markets emerge, EU and US markets will continue to be important for t…」  
  判断：**正确**。欧盟与美国仍是英国最重要市场：2024年欧盟占英国进口50.2%，美国是最大单一出口国（货物出口593亿英镑，占16.2%）。  
  来源：<https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/articles/uktradewiththeunitedstates/2024>；<https://www.tradeandbusiness.uk/news/ons-trade-figures>
- **#149** 「as competition from BRIC and emerging economies increases, future FDI into Europe is likely to be a smaller sh…」  
  判断：**正确**。同#31：欧洲FDI流入2022年为负、2023年仅160亿美元，2024年项目数降至九年最低，占全球比重下降。  
  来源：<https://unctad.org/publication/world-investment-report-2024>；<https://trendsgroup.org/insight/the-world-investment-trends-and-sdgs-funding-challenges/>；<https://www.ey.com/en_gl/newsroom/2025/05/fdi-in-europe-slows-but-confidence-remains-for-long-term-rebound>
- **#153** 「China will continue to be a global force in manufacturing.」  
  判断：**正确**。中国仍是全球制造业力量：制造业增加值占全球约30%，连续15年居首（UNIDO数据）。  
  来源：<https://www.guancha.cn/chenjing/2025_10_20_793928.shtml>；<https://www.visualcapitalist.com/charted-chinas-rise-to-manufacturing-dominance-over-30-years/>
- **#160** 「While BRIC growth rates will slow down, emerging economies as a group, consisting of BRIC, N-11, and other ‘la…」  
  判断：**正确**。金砖增速放缓（新兴市场增速从2010年7.6%降至2015年3.7%），但新兴经济体仍是全球增长主要来源（IMF 2024）。  
  来源：<https://www.worldbank.org/content/dam/Worldbank/GEP/GEP2016a/Global-Economic-Prospects-January-2016-Spillovers-from-major-emerging-markets.pdf>；<https://www.imf.org/-/media/files/publications/fandd/article/2024/09/aslam.pdf>
- **#162** 「Both scenarios envisage that emerging economies will grow faster than today’s mature economies and that compet…」  
  判断：**正确**。IMF 2024年附表记录2016至2023年新兴发展经济体各年的实际增速均高于发达经济体，英国制造出口亦面临中国份额上升的竞争，情景共同方向符合。  
  来源：<https://www.imf.org/-/media/files/publications/weo/2024/october/english/tablea.pdf>；<https://www.mckinsey.com/mgi/our-research/investing-in-productivity-growth>；<https://www.ciip.group.cam.ac.uk/reports-and-articles/uk-manufacturing-at-a-crossroads-building-on-strengths-to-meet-the-china-challenge/>
- **#163** 「the current account shown in Figure 4.1448 is in deficit throughout the projection period.」  
  判断：**正确**。ONS序列AA6H显示2012–2022年英国经常账户每年均为赤字（-0.8%至-5.1% GDP）。  
  来源：<https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/timeseries/aa6h/ukea>；<https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/bulletins/unitedkingdombalanceofpaymentsthepinkbook/2023>
- **#166** 「There is a continued decline in the performance of oil and gas relative to GDP and a continued deficit on food…」  
  判断：**正确**。2022年燃料进口激增：ONS显示燃料进口增加636亿英镑(+119%)，油气贸易表现恶化；英国货物贸易持续逆差，食品与原材料继续逆差。  
  来源：<https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/articles/uktradeingoodsyearinreview/2022/pdf>；<https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/bulletins/unitedkingdombalanceofpaymentsthepinkbook/2024>
- **#167** 「But FDI in Europe is likely to be a dwindling share of global FDI flows, and the UK will face growing competit…」  
  判断：**正确**。同#31：欧洲FDI占比缩小，英国2024年FDI项目减少13%，面临激烈竞争。  
  来源：<https://unctad.org/publication/world-investment-report-2024>；<https://www.ey.com/en_gl/newsroom/2025/05/fdi-in-europe-slows-but-confidence-remains-for-long-term-rebound>
- **#171** 「First, demographics will become much less favourable with labour force growth turning negative from the 2020s」  
  判断：**正确**。中国劳动年龄人口（15–64岁）2015年达峰后以每年约0.7%下降；16–59岁人口占比2023年降至61.3%。  
  来源：<https://wol.iza.org/articles/the-chinese-labor-market/long>；<https://www.cnbc.com/2024/01/19/chinas-working-age-population-is-shrinking.html>
- **#172** 「In addition, the structure of the economy will become less industrial, which will tend anyway to reduce produc…」  
  判断：**正确**。中国经济服务化：2024年服务业占GDP约56.7%、工业约36.5%，较2013年前后工业占比明显下降。  
  来源：<https://ecoindica.com/countries/china-gdp/>；<https://www.stats.gov.cn/english/PressRelease/202502/t20250228_1958822.html>
- **#173** 「Economic history suggests that the OECD projections may well be too optimistic.」  
  判断：**正确**。OECD预测2012–17年中国年均增长8.9%，实际十八大以来年均约7.1%，预测确属过于乐观。  
  来源：<http://www.da.gov.cn/da/gnyw/201712/ed6cbc5efa774c598c1a0b1b98c59808.shtml>；<https://kdijep.org/v.46/1/1/China%E2%80%99s+Slowdown>
- **#175** 「Global fragmentation of value chains will continue to be the dominant force in the spatial distribution of man…」  
  判断：**正确**。GVC仍主导制造业空间分布，回流只带回部分生产：McKinsey调查显示近岸化增加，但WTO显示GVC仍是主导生产范式，仅增速放缓。  
  来源：<https://www.wto.org/english/res_e/booksp_e/04_gvc23_ch1_dev_report_e.pdf>；<https://www.mckinsey.com/capabilities/operations/our-insights/tech-and-regionalization-bolster-supply-chains-but-complacency-looms>
- **#177** 「The prospect of future ‘reindustrialisation’ looks weak (based on current metrics)」  
  判断：**正确**。再工业化疲弱：制造业增加值占比由2000年14.8%降至2023年9.1%（剑桥CIIP），2025年约7.7%为历史最低。  
  来源：<https://www.ciip.group.cam.ac.uk/innovation/structure-and-performance-of-the-uk-economy-25/>；<https://www.theglobaleconomy.com/United-Kingdom/Share_of_manufacturing/>
- **#181** 「the various authors are agreed that, under almost any scenario, there is unlikely to be a significant increase…」  
  判断：**正确**。制造业就业占比未回升：下议院图书馆称2022年4–6月制造业岗位约260万、仅占全部岗位7%，制造业增加值约占10%；JWR7显示制造业岗位2010–2023年在约256万–272万间徘徊而总就业增长，与“难以显著上升”一致。  
  来源：<https://commonslibrary.parliament.uk/research-briefings/cdp-2022-0205/>；<https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/employmentandemployeetypes/timeseries/jwr7/lms/previous/v36>
- **#186** 「As demand increases for natural resources there is likely to be greater volatility in their prices with potent…」  
  判断：**正确**。资源价格波动加大并出现供应中断：2022年能源价格创1973年以来最大23个月涨幅；中国2023–2025年对镓、锗、稀土实施出口管制。  
  来源：<https://thedocs.worldbank.org/en/doc/24e8d315b8229b791ea61e0fa09b28d0-0350012022/related/CMO-April-2022-Executive-Summary.pdf>；<https://www.ui.se/globalassets/ui.se-eng/publications/other-publications/chinas-mineral-export-restrictions_market-impacts-and-implications_nkk_2025.pdf>
- **#188** 「Governments around the world are likely to set increasingly stringent environmental regulations due to environ…」  
  判断：**正确**。各国环境法规趋严：英国2019年立法净零目标，欧盟ESPR等法规出台。  
  来源：<https://www.gov.uk/government/news/uk-becomes-first-major-economy-to-pass-net-zero-emissions-law>；<https://eur-lex.europa.eu/eli/reg/2024/1781/2024-06-28/eng>
- **#189** 「An important future trend is likely to be ‘pricing of the environment’, which involves attaching an economic v…」  
  判断：**正确**。环境定价成为重要趋势：碳定价覆盖全球约28%排放，2024年收入超过1000亿美元。  
  来源：<https://www.worldbank.org/en/news/press-release/2025/06/10/global-carbon-pricing-mobilizes-over-100-billion-for-public-budgets>；<https://documents1.worldbank.org/curated/en/099052726140533053/pdf/P502283-3c932762-c975-44ed-856e-95d37c1e347d.pdf>
- **#190** 「Regulatory pressure to reduce emissions in manufacturing is likely to increase.」  
  判断：**正确**。制造业减排监管压力增加：EU ETS碳价从2010年代约5欧元升至2023年80欧元以上；英国净零立法。  
  来源：<https://carbonprice.co.uk/eu-carbon-price/history>；<https://www.gov.uk/government/news/uk-becomes-first-major-economy-to-pass-net-zero-emissions-law>
- **#191** 「the fact that the availability of mined materials is subject to marked geo-political risk is the critical issu…」  
  判断：**正确**。矿产地缘政治风险加剧：中国2023–2025年对镓、锗、锑、稀土实施出口管制（CSIS 2025）。  
  来源：<https://www.ui.se/globalassets/ui.se-eng/publications/other-publications/chinas-mineral-export-restrictions_market-impacts-and-implications_nkk_2025.pdf>；<https://www.csis.org/analysis/consequences-chinas-new-rare-earths-export-restrictions>
- **#192** 「As emerging economies develop, it seems likely that competition for resources will be fierce and protectionism…」  
  判断：**正确**。资源保护主义出现：中国对稀有金属实施出口管制，印尼禁止镍矿出口。  
  来源：<https://www.csis.org/analysis/consequences-chinas-new-rare-earths-export-restrictions>；<https://www.iea.org/policies/16084>
- **#195** 「However, in the longer term, research and development is likely to reduce the costs of renewable energy33.」  
  判断：**正确**。可再生能源成本大幅下降：IRENA显示公用事业级光伏LCOE 2010–2023年下降90%至0.044美元/kWh。  
  来源：<https://www.pv-tech.org/irena-solar-lcoe-falls-12-year-on-year-90-since-2010/>
- **#198** 「To make the most efficient use of the various renewable resources in Europe, it is likely that much more elect…」  
  判断：**正确**。欧洲远距离输电增加：英国互联容量2021–2024年增至10.5GW（Viking Link等），Ofgem 2024年批准新互联项目。  
  来源：<https://www.regen.co.uk/insights/the-growth-of-gbs-interconnector-capacity>；<https://www.ofgem.gov.uk/press-release/empowering-great-britain-clean-and-flexible-energy-future-next-generation-interconnectors>
- **#199** 「The need for such demand-side management, the options for providing it, and the price paid are all likely to i…」  
  判断：**正确**。需求侧管理需求与支付增加：英国电网2022年起推出需求灵活性服务(DFS)，向减少用电的用户支付费用。  
  来源：<https://www.energy-uk.org.uk/publications/energy-uk-explainer-demand-flexibility-service-dfs/>；<https://www.neso.energy/news/world-first-demand-flexibility-service-exceeds-expectations-businesses-saving-thousands-pounds-while-reducing-carbon-emissions>
- **#203** 「Firms which use significant amounts of energy are likely to face higher energy costs in the future resulting f…」  
  判断：**正确**。碳价上升推高高耗能企业成本：EU ETS碳价升至80欧元以上，英国高耗能用户协会指工业电价欧洲最高损害竞争力。  
  来源：<https://carbonprice.co.uk/eu-carbon-price/history>；<https://www.eiug.co.uk/high-uk-industrial-electricity-prices-continue-to-damage-competitiveness-of-energy-intensive-industries/>
- **#205** 「For example, desalinisation technologies will become more important」  
  判断：**正确**。海水淡化重要性上升：反渗透占全球淡化产能约70%并持续扩张（EU蓝色经济观察），Oliver Wyman称淡化已从小众变为核心供水。  
  来源：<https://blue-economy-observatory.ec.europa.eu/eu-blue-economy-sectors/desalination_en>；<https://www.oliverwyman.com/our-expertise/insights/2025/dec/mena-global-water-sector-8-transformations.html>
- **#207** 「‘Collaborative consumption’109, a type of rental model, may become more prevalent in the face of environmental…」  
  判断：**正确**。共享/租赁模式普及：Airbnb、Uber等共享经济平台在2015年后大规模扩张（PwC、Brookings）。  
  来源：<https://www.pwc.com/hu/en/kiadvanyok/assets/pdf/sharing-economy-en.pdf>；<https://www.brookings.edu/articles/the-current-and-future-state-of-the-sharing-economy/>
- **#212** 「Manufacturing output is likely to continue increasing without associated increases in direct employment.」  
  判断：**正确**。制造业产出指数（2008=100，ONS K22A）由2010年90.9升至2023年104.5、2024年106.0；同期制造业工作岗位2010年约257.2万、2023年约258.3万（JWR7），产出增长而直接就业未增加。  
  来源：<https://reindustrialiseuk.org/wp-content/uploads/riu-charts/BR-433-manufacturing-growth.csv>；<https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/employmentandemployeetypes/timeseries/jwr7/lms/previous/v36>
- **#219** 「It seems likely that manufacturing will continue to face strong competition from other sectors for STEM gradua…」  
  判断：**正确**。制造业争夺STEM人才竞争激烈：EngineeringUK指出约25%的招聘与工程相关、需求跨行业，供给不足。  
  来源：<https://www.engineeringuk.com/research-and-insights/our-research-and-evaluation-reports/engineering-skills-needs-now-and-into-the-future/>
- **#220** 「Changing immigration rules may mean that some employers will face greater challenges in sourcing some of their…」  
  判断：**正确**。脱欧后移民规则使海外招聘更难：2025年移民规则收紧使制造业更难填补短缺（Myerson），Make UK呼吁改革。  
  来源：<https://www.myerson.co.uk/news-insights-and-events/navigating-uk-immigration-changes-what-manufacturers-need-to-know>；<https://www.makeuk.org/insights/publications/make-uk-calls-immigration-reform-tackle-manufacturing-skills-shortages>
- **#222** 「It seems likely that most of the future workforce will be drawn from the UK.」  
  判断：**正确**。ReindustrialiseUK分析指出制造业对外国出生工人的依赖与整体经济相当，劳动力大多数仍为英国本土出生。  
  来源：<https://reindustrialiseuk.org/knowledgebase/migration-labour-mobility-and-industrial-skills/>
- **#223** 「At the same time, foreign direct investment (FDI) into Europe as a proportion of worldwide FDI is set to decre…」  
  判断：**正确**。同#31：欧洲FDI流入占全球比重下降（UNCTAD 2024；EY 2025）。  
  来源：<https://unctad.org/publication/world-investment-report-2024>；<https://www.ey.com/en_gl/newsroom/2025/05/fdi-in-europe-slows-but-confidence-remains-for-long-term-rebound>
- **#224** 「Advances in technologies including sensors, additive manufacturing and ICT will ‘digitise’ manufacturing.」  
  判断：**正确**。Deloitte 2025智能制造调查记录传感器、云及分析技术已经用于制造并带来产出改善，ABI记录实际云协作部署，制造数字化的方向符合。  
  来源：<https://www.deloitte.com/us/en/about/press-room/deloitte-2025-smart-manufacturing-survey.html>；<https://www.bcg.com/publications/2024/shaking-up-the-factory-floor-with-digital-and-ai>；<https://www.abiresearch.com/press/study-shows-76-of-discrete-and-process-manufacturers-use-cloud-platforms-for-real-time-collaboration-and-supply-chain-efficiency>
- **#227** 「Increasing competition for resources is likely to result in greater price volatility in commodities.」  
  判断：**正确**。大宗商品价格波动加大：2014年油价暴跌、2022年能源价格创纪录涨幅（世界银行）。  
  来源：<https://thedocs.worldbank.org/en/doc/24e8d315b8229b791ea61e0fa09b28d0-0350012022/related/CMO-April-2022-Executive-Summary.pdf>；<https://www.imf.org/external/pubs/ft/fandd/2015/12/baffes.htm>
- **#230** 「Manufacturers in developed economies will increasingly use the quality of their workforces to compete in high …」  
  判断：**正确**。Make UK记录制造商日益重视现有员工技能升级及再培训以适应技术并留住人才，2024年数字技能缺口亦成为现实竞争约束。无终点方向性预测在出版后窗口已有企业行为与约束证据，判正确。  
  来源：<https://www.makeuk.org/docs/skills-2030-closing-gap-report-web/download>；<https://www.imeche.org/news/news-article/new-recruits-%27lack-skills-for-digital-transformation%27-large-manufacturing-companies-complain>
- **#232** 「markets for UK manufacturers, including the US and and utlilisation of future manufacturing workers Europe, wi…」  
  判断：**正确**。ONS显示2024年英国对美商品出口593亿英镑，占商品出口16.2%；欧盟仍占英国总出口41%。美国和欧洲仍是重要市场这一无日期方向已观察到，判正确。  
  来源：<https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/articles/uktradewiththeunitedstates/2024>；<https://www.tradeandbusiness.uk/news/ons-trade-figures>

### 趋势符合（13 条）

- **#14** 「New data streams from products will become available to support new services, enable self-checking inventories…」  
  判断：**趋势符合**。产品与设备数据流支撑的预测性维护快速扩散：Siemens报告7年间预测性维护咨询增加275%，PwC比利时调查显示预测性维护实施率约17%；方向符合，但自检库存/故障前自诊断尚未普遍。  
  来源：<https://assets.new.siemens.com/siemens/assets/api/uuid:8ee59c19-1c37-4516-a290-2844096f1cff/Readiness-Report-2023_original.pdf>；<https://press.pwc.be/digital-technology-on-the-rise-in-companies-maintenance-on-mobile-devices-is-growing>
- **#40** 「Over the period to 2050, national and international responses are likely to include tougher environmental stan…」  
  判断：**趋势符合**。更严格的产品环境标准与资源定价正在推进：ESPR于2024年生效；碳定价覆盖全球约28%排放（2005年约5%）。终点为2050年，方向符合。  
  来源：<https://eur-lex.europa.eu/eli/reg/2024/1781/2024-06-28/eng>；<https://documents1.worldbank.org/curated/en/099052726140533053/pdf/P502283-3c932762-c975-44ed-856e-95d37c1e347d.pdf>
- **#98** 「In the manufacturing sector, information will be increasingly machinegenerated」  
  判断：**趋势符合**。机器生成的数据（IoT、预测性维护）快速增长：联网设备188亿台、预测性维护兴趣大增；方向符合但“越来越多由机器生成”的比例缺少直接度量。  
  来源：<https://iot-analytics.com/number-of-connected-iot-devices-2024/>；<https://assets.new.siemens.com/siemens/assets/api/uuid:8ee59c19-1c37-4516-a290-2844096f1cff/Readiness-Report-2023_original.pdf>
- **#114** 「Over the next decade, cloud-based software will move from specialist applications towards the shop floor.」  
  判断：**趋势符合**。云软件已进入车间：ABI 2024调查76%制造商使用云平台做实时协作与供应链；但Forrester指出制造业上云慢于其他行业，方向符合。  
  来源：<https://www.abiresearch.com/press/study-shows-76-of-discrete-and-process-manufacturers-use-cloud-platforms-for-real-time-collaboration-and-supply-chain-efficiency>；<https://www.forrester.com/report/the-state-of-cloud-in-manufacturing-2024/RES180386>
- **#138** 「in cell-based therapies, particularly those exploiting the patient’s own or autologous cells, treatments are l…」  
  判断：**趋势符合**。自体CAR-T等细胞疗法的院内/床旁（point-of-care）生产已在学术医院开展并被研究推广，方向符合但尚非主流。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC11707413/>；<https://ashpublications.org/bloodict/article/2/2/100053/567760/Decentralized-CAR-T-manufacturing-highlighting>
- **#141** 「The emergence of technologies that will help manufacturers use less resource to deliver value, for example lig…」  
  判断：**趋势符合**。原文终点是未来二十年（约2033年）；2024年综述记录轻量复合材料近年跨行业应用扩展，全球复合材料量2023年1300万吨、2024年1350万吨，方向符合。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC11550074/>；<https://www.composites-united.com/en/avk-market-report-2024/>
- **#145** 「On current trends, manufacturing exports would not double before 2032.」  
  判断：**趋势符合**。出口翻番目标落空：2017年政府放弃“2020年出口达1万亿英镑”目标；ONS制造业出口2013年约1385亿英镑、2024年约1975亿英镑，未翻番。2032年终点未到，方向符合。  
  来源：<https://www.independent.co.uk/news/uk/politics/liam-fox-brexit-government-abandons-export-target-trade-talks-a7556866.html>；<https://www.nao.org.uk/wp-content/uploads/2017/10/Short-Guide-to-the-Department-for-International-Trade.pdf>；<https://www.ons.gov.uk/economy/economicoutputandproductivity/output/timeseries/csyb/diop>
- **#193** 「Out to 2050, there will be a drive towards decarbonising the energy system; however fossil fuels are still pre…」  
  判断：**趋势符合**。化石燃料仍主导：2024年油气煤占全球能源消费约86.6%，且总量仍在增长；终点为2050年，方向符合。  
  来源：<https://justthenews.com/politics-policy/energy/annual-benchmark-global-energy-report-shows-fossil-fuels-continued-dominate>；<https://energyinst.org/exploring-energy/resources/news-centre/media-releases/renewables-soar,-but-fossil-fuels-continue-to-rise-as-global-electricity-demand-hits-record-levels>
- **#200** 「This is expected to place increasing demand for provenance information and we can expect future products to pr…」  
  判断：**趋势符合**。欧盟数字产品护照(ESPR)要求产品呈现价值链可持续性数据，正在实施准备中，方向符合。  
  来源：<https://single-market-economy.ec.europa.eu/single-market/goods/european-standards/harmonised-standards/digital-product-passport-dpp_en>；<https://eur-lex.europa.eu/eli/reg/2024/1781/2024-06-28/eng>
- **#201** 「In 2011, re-manufacturing only represented approximately 1% of the total UK manufacturing sector turnover76. T…」  
  判断：**趋势符合**。CRR估计英国再制造业规模近50亿英镑；MTA报告2022年制造业GVA约1840亿英镑（营业额远大于GVA），据此再制造约占制造业营业额1%量级，仍属有限水平；ReindustrialiseUK指出官方统计无法单独计量，故只判方向符合。  
  来源：<https://www.remanufacturing.org.uk/market-intelligence>；<https://www.mta.org.uk/wp-content/uploads/2024/04/Manufacturing-Technologies-Association-The-true-impact-of-British-Manufacturing.pdf>
- **#206** 「These trends, combined with a greater demand for food and bio-fuels, will place pressure on land use around th…」  
  判断：**趋势符合**。英国农地价格上升：Savills 2023显示优质耕地价格超过2015年高点；但2015–2020年基本持平，方向符合。  
  来源：<https://www.savills.co.uk/insight-and-opinion/savills-news/349733/farmland-values-break-new-ground-and-supply-returns-to-near-10-year-average-levels>
- **#208** 「However, in recent years supply chains have become more vulnerable as a consequence of globalisation and this …」  
  判断：**趋势符合**。环境与地缘冲击使供应链脆弱性受到更多关注（德州冰冻、2022年能源危机），企业加大韧性投资，方向符合。  
  来源：<https://scm.ncsu.edu/scm-articles/article/the-increasing-role-of-climate-change-in-supply-chain-disruptions>；<https://www.mckinsey.com/capabilities/operations/our-insights/tech-and-regionalization-bolster-supply-chains-but-complacency-looms>
- **#209** 「Strong future demand for workers is likely, however within a context of small further reductions in the total …」  
  判断：**趋势符合**。制造业劳动力需求强劲（Make UK称2026年约4.8万空缺）；JWR7显示工作岗位从2018年约271.5万降至2023年约258.3万，小幅下降，但2010–2018年曾上升，方向大体符合。  
  来源：<https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/employmentandemployeetypes/timeseries/jwr7/lms/previous/v36>；<https://www.makeuk.org/insights/publications/make-uk-calls-immigration-reform-tackle-manufacturing-skills-shortages>

### 部分符合（74 条）

- **#6** 「many are not positioned to succeed in a future world where greater opportunities will be balanced by greater c…」  
  判断：**部分符合**。剑桥研究记录中国制造力量上升与英国全球份额下降，而Make UK仍记录高价值制造优势；竞争加剧与新机会并存，但“机会与竞争相平衡”没有同一可比量尺。  
  来源：<https://www.ciip.group.cam.ac.uk/reports-and-articles/uk-manufacturing-at-a-crossroads-building-on-strengths-to-meet-the-china-challenge/>；<https://www.makeuk.org/insights/reports/uk-manufacturing-facts-2025>
- **#9** 「many of the technologies that will transform manufacturing, such as additive manufacturing , are already estab…」  
  判断：**部分符合**。增材制造已产生约128亿美元的2020年行业规模并扩展部分生产方式，但没有证实对制造业整体的全面改造，技术影响只部分实现。  
  来源：<https://wohlersassociates.com/press-releases/new-wohlers-report-2021-finds-7-5-growth-in-additive/>；<https://think.ing.com/uploads/reports/3D_printing_report_final_050821_RL_OT_FINAL.pdf>
- **#10** 「The historic split between cheap massproduced products creating value from economies of scale and more expensi…」  
  判断：**部分符合**。个性化/定制被Euromonitor列为消费“大趋势”，企业借直销与数据提供定制产品；但大规模低成本定制主要见于部分品类，廉价大规模产品与定制产品的分野仅在部分产品类型缩小。  
  来源：<https://www.euromonitor.com/article/introducing-the-personalisation-megatrend>；<https://www.prescouter.com/inquiry/the-future-of-consumer-goods-harnessing-hyper-personalization-and-mass-customization/>
- **#11** 「Direct customer input to design will increasingly enable companies to produce customised products with the sho…」  
  判断：**部分符合**。客户参与设计的定制产品增多（Euromonitor个性化大趋势、PreScouter报告企业借直销收集客户数据做定制），但“低成本、快速”定制在多数品类尚未普及，只部分实现。  
  来源：<https://www.euromonitor.com/article/introducing-the-personalisation-megatrend>；<https://www.prescouter.com/inquiry/the-future-of-consumer-goods-harnessing-hyper-personalization-and-mass-customization/>
- **#12** 「The factories of the future will be more varied, and more distributed than those of today」  
  判断：**部分符合**。Bain 2024年调查显示64%的企业高管报告已投资近岸或分岸布局，生产地理布局确在变化；但AM成本研究显示分布式配置仍有规模经济障碍，不能确认工厂全面多样化和分散化。  
  来源：<https://www.bain.com/about/media-center/press-releases/2024/businesses-accelerate-reshoring-and-near-shoring-amid-heightened-geopolitical-uncertainties-and-rising-costs-bain--company-finds/>；<https://researchportal.ulisboa.pt/en/publications/technology-cost-drivers-for-a-potential-transition-to-decentraliz/>
- **#13** 「The integration of sensors into networks of technology, such as products connected to the internet, will revol…」  
  判断：**部分符合**。Deloitte 2025年调查记录传感器、云和分析支撑的产出与生产率改善；BCG则发现多数制造商尚未实现数字化全部潜力，“革命性改造”只在部分企业实现。  
  来源：<https://www.deloitte.com/us/en/about/press-room/deloitte-2025-smart-manufacturing-survey.html>；<https://www.bcg.com/publications/2024/shaking-up-the-factory-floor-with-digital-and-ai>
- **#15** 「New materials, in which the UK has strong capabilities, will penetrate the mass market and will include reacti…」  
  判断：**部分符合**。轻质复合材料等已进入大众市场，但石墨烯/碳纳米管等仍处早期：Nature Reviews Physics 2024指出石墨烯最大应用仍在复合材料与涂料等，IDTechEx称仍在寻找杀手级应用；自愈材料未见大众化。  
  来源：<https://www.nature.com/articles/s42254-024-00754-9>；<https://www.idtechex.com/en/research-article/prosumer-applications-lead-early-adoption-of-graphene/34187>
- **#18** 「In factory and process environments, virtually everything is expected to be connected via central networks.」  
  判断：**部分符合**。工厂联网程度提高：2023年调查62%的制造商在生产/装配中使用IoT；但“几乎一切联网”尚未实现，多数仍在部分部署。  
  来源：<https://ubisense.com/wp-content/uploads/2023/05/Berkeley-Ubisense-IoT-In-Manufacturing-2023-V3.pdf>；<https://iot-analytics.com/number-of-connected-iot-devices-2024/>
- **#19** 「Increasingly, new products will have embedded sensors and become autonomous.」  
  判断：**部分符合**。内置传感器的联网产品大量增加（2024年联网IoT设备188亿台），但“自主化”产品仍限于部分领域。  
  来源：<https://iot-analytics.com/number-of-connected-iot-devices-2024/>；<https://iot-analytics.com/number-connected-iot-devices/>
- **#20** 「Advances are likely to make many routine manufacturing operations obsolete」  
  判断：**部分符合**。工业机器人存量2023年达约428万台创纪录，自动化持续推进；但“许多常规制造操作过时”仅部分实现，人工岗位仍大量存在。  
  来源：<https://ifr.org/ifr-press-releases/news/record-of-4-million-robots-working-in-factories-worldwide>
- **#21** 「This is expected to have a profound impact on the way manufacturers make almost any product.」  
  判断：**部分符合**。增材制造持续增长但规模有限：Wohlers 2021报告2020年全行业约128亿美元、增速降至7.5%；尚未“深刻影响几乎所有产品的制造方式”，属部分实现（终点为未来数十年）。  
  来源：<https://wohlersassociates.com/press-releases/new-wohlers-report-2021-finds-7-5-growth-in-additive/>；<https://think.ing.com/uploads/reports/3D_printing_report_final_050821_RL_OT_FINAL.pdf>
- **#23** 「Smart phones and similar devices are positioned to become ubiquitous, general purpose tools for managing suppl…」  
  判断：**部分符合**。智能手机/平板在工厂管理中的使用增长但不普遍：2021年调查仅47%一线制造工人获配移动设备；Automation World调查约三分之一受访者在车间使用移动应用。  
  来源：<https://parsable.com/wp-content/uploads/2021/06/CM-FrontlineWorkersSurveyReport-R1-RegUD.pdf>；<https://www.automationworld.com/products/control/article/13318550/hey-operators-theres-an-app-for-that>
- **#32** 「Many manufacturing value chains are likely to continue to fragment」  
  判断：**部分符合**。WTO《全球价值链发展报告》指出2010–2019年GVC扩张明显放缓，并在金融危机、中美贸易争端和疫情后参与率下降；碎片化未逆转但未“继续”明显推进，只部分符合。  
  来源：<https://www.wto.org/english/res_e/booksp_e/03_gvc_executive-summary_dev_report_2021_e.pdf>；<https://www.wto.org/english/res%5Fe/booksp%5Fe/gvcreport2025-01%5Fe.pdf>
- **#34** 「some underlying trends suggest it will become increasingly possible for the UK to compete with lower cost loca…」  
  判断：**部分符合**。2022–2023年英国部分制造商因供应链冲击把生产迁回（Reuters报道伯明翰订单回流、英国工厂转向本地供应商）；但大规模回流未见，只部分符合。  
  来源：<https://www.reuters.com/world/uk/made-britain-broken-supply-lines-drive-manufacturing-back-home-2022-07-28/>；<https://www.reuters.com/world/uk/more-uk-factories-turn-away-foreign-suppliers-survey-shows-2023-03-07/>
- **#35** 「As manufacturing value chains continue to fragment globally, and new business models such as manufacturing ser…」  
  判断：**部分符合**。制造服务收入增加与云平台跨企业协作扩大支持价值链运营的重要性；但WTO材料显示全球价值链碎片化的扩张放缓，并非原句所暗示的持续强劲推进。  
  来源：<https://www.wto.org/english/res_e/booksp_e/03_gvc_executive-summary_dev_report_2021_e.pdf>；<https://www.wto.org/english/res%5Fe/booksp%5Fe/gvcreport2025-01%5Fe.pdf>；<https://www.bain.com/insights/services-build-value-for-the-industrial-sector-snap-chart/>；<https://www.techtarget.com/news/Manufacturers-turn-to-servitization-for-competitive-advantage/852858/>；<https://www.abiresearch.com/press/study-shows-76-of-discrete-and-process-manufacturers-use-cloud-platforms-for-real-time-collaboration-and-supply-chain-efficiency>
- **#36** 「In most cases, prices will rise and they may also become more volatile.」  
  判断：**部分符合**。资源价格高度波动：2014–2016年大宗商品超级周期结束、油价暴跌，2022年能源价格创1973年以来最大涨幅；“多数情况下上涨”与2014–2020年的下跌不符，只部分符合。  
  来源：<https://thedocs.worldbank.org/en/doc/24e8d315b8229b791ea61e0fa09b28d0-0350012022/related/CMO-April-2022-Executive-Summary.pdf>；<https://www.imf.org/external/pubs/ft/fandd/2015/12/baffes.htm>；<https://en.lavajato.org/data/series/brent_anual.csv>
- **#42** 「Resource scarcity and higher costs for energy and waste disposal will shift manufacturing value creation to ne…」  
  判断：**部分符合**。循环经济政策与讨论增加，但Circularity Gap Report 2024显示全球循环率从2018年9.1%降至2023年7.2%；价值创造向再利用/再制造转移只部分符合。  
  来源：<https://www.renewablematter.eu/en/Circularity-Gap-Report-2024-a-roadmap-to-lead-the-world-towards-the-circular-economy>；<https://vjol.info.vn/index/article/view/103633>
- **#52** 「These changes will present major opportunities for the UK to develop competitive strengths in new and existing…」  
  判断：**部分符合**。剑桥报告记录英国面临中国崛起的竞争压力且仍在航空航天和生命科学领域有优势，机会与威胁并存的方向部分得到证实。  
  来源：<https://www.ciip.group.cam.ac.uk/reports-and-articles/uk-manufacturing-at-a-crossroads-building-on-strengths-to-meet-the-china-challenge/>；<https://www.makeuk.org/insights/reports/uk-manufacturing-facts-2025>
- **#54** 「The factories of the future will be more varied, and less spatially concentrated than those of today.」  
  判断：**部分符合**。2024年Bain调查中64%企业已投资或执行分岸、近岸等布局，支持工厂区位趋于多样。成本模型亦显示分布式生产面临规模经济门槛，不能由部分企业重布局推定全球工厂空间集中度普遍下降，判部分符合。  
  来源：<https://www.bain.com/about/media-center/press-releases/2024/businesses-accelerate-reshoring-and-near-shoring-amid-heightened-geopolitical-uncertainties-and-rising-costs-bain--company-finds/>；<https://researchportal.ulisboa.pt/en/publications/technology-cost-drivers-for-a-potential-transition-to-decentraliz/>
- **#58** 「Resource scarcity and higher costs for energy and waste disposal will shift manufacturing value creation to ne…」  
  判断：**部分符合**。同#42：循环政策增加，但全球循环率2018–2023年由9.1%降至7.2%，向再利用/再制造转型只部分实现。  
  来源：<https://www.renewablematter.eu/en/Circularity-Gap-Report-2024-a-roadmap-to-lead-the-world-towards-the-circular-economy>；<https://vjol.info.vn/index/article/view/103633>
- **#65** 「Becoming ‘factoryless goods producers’, capturing value by selling technological knowledge and leaving product…」  
  判断：**部分符合**。美国研究显示“无工厂制造”商业模式被越来越多企业采用（Bayard等2014），Cato 2024亦提到其兴起；英国缺少统计，只部分证实。  
  来源：<https://david-m-byrne.github.io/david-m-byrne/factoryless-manufacturing_bayard-byrne-smith_2014.pdf>；<https://www.cato.org/blog/concerns-over-us-manufacturing-trade-deficit-are-misplaced>
- **#66** 「These will become important in most sub-sectors in future decades as technological, economic, environmental an…」  
  判断：**部分符合**。服务化与租赁等收入模式已扩展，但全球循环率2018至2023年由9.1%降至7.2%，服务化、个性化、循环与租赁四项并未在多数子行业一致成为重要模式。  
  来源：<https://circulareconomy.europa.eu/platform/en/knowledge/circularity-gap-report-2024>；<https://www.deloitte.com/be/en/issues/working-together-towards-a-sustainable-future/circularity-gap-report.html>；<https://www.bain.com/insights/services-build-value-for-the-industrial-sector-snap-chart/>；<https://www.techtarget.com/news/Manufacturers-turn-to-servitization-for-competitive-advantage/852858/>；<https://doi.org/10.31893/multirev.2024201>
- **#67** 「technological developments such as the integration of sensors into products, and advances in information commu…」  
  判断：**部分符合**。个性化产品增多（Euromonitor个性化大趋势），但传感器与IT驱动的产品个性化仅见于部分品类。  
  来源：<https://www.euromonitor.com/article/introducing-the-personalisation-megatrend>；<https://www.prescouter.com/inquiry/the-future-of-consumer-goods-harnessing-hyper-personalization-and-mass-customization/>
- **#70** 「As the pace of change in manufacturing accelerates, these metrics are increasingly likely to misrepresent the …」  
  判断：**部分符合**。剑桥2019年研究确认制造品价值日益依赖划作其他行业的活动，旧统计覆盖缺陷加深的方向有支持；但2026年英国SIC已作大幅修订，原句隐含持续恶化只部分符合。  
  来源：<https://www.ifm.eng.cam.ac.uk/uploads/Research/CSTI/Inside_the_Black_Box_of_Manufacturing_report_FINAL_120619.pdf>；<https://www.ons.gov.uk/file?uri=%2Fmethodology%2Fclassificationsandstandards%2Fukstandardindustrialclassificationofeconomicactivities%2Fuksic2026%2Fuksic2026introductoryguidelines31july2026.pdf>
- **#71** 「Re-manufacturing institutionalised through standards, with more products designed from the outset with remanuf…」  
  判断：**部分符合**。再制造标准化有进展（ISO 8887-1:2017、BS 8887-220），欧盟ESPR纳入可再制造设计要求；但“更多产品从设计起考虑再制造”缺乏量化证据，只部分符合。  
  来源：<https://www.iso.org/standard/62047.html>；<https://knowledge.bsigroup.com/products/design-for-manufacture-assembly-disassembly-and-end-of-life-processing-made-the-process-of-remanufacture-specification>
- **#73** 「Environmental sustainability will become an increasingly important component of product differentiation and va…」  
  判断：**部分符合**。可持续性日益进入零售与法规（THESIS指标被多家零售商使用、欧盟ESPR与数字产品护照），但作为产品差异化与价值创造的主要来源证据有限。  
  来源：<https://sustainablebrands.com/read/thesis-tsc-s-newest-way-for-retailers-to-track-supplier-sustainability-performance>；<https://single-market-economy.ec.europa.eu/single-market/goods/european-standards/harmonised-standards/digital-product-passport-dpp_en>
- **#74** 「Environmental sustainability is likely to come to be measured and managed in order to provide clear informatio…」  
  判断：**部分符合**。可持续性测量与信息披露增强（欧盟数字产品护照立法），但面向消费者的碳足迹标签并未普及，只部分符合。  
  来源：<https://single-market-economy.ec.europa.eu/single-market/goods/european-standards/harmonised-standards/digital-product-passport-dpp_en>；<https://eur-lex.europa.eu/eli/reg/2024/1781/2024-06-28/eng>
- **#77** 「Telepresence will affect development and production processes of manufacturing, as well as create opportunitie…」  
  判断：**部分符合**。PMMI调查记录2023年55.1%的终端用户使用远程支持，虚拟验厂和远程调试也已使用；但后两者仅26.5%和5.2%，Bath研究亦指出AR部署缓慢，生产研发全面变化只部分实现。  
  来源：<https://www.webbersmith.com/wp-content/uploads/2024/01/2024-Trends-in-Remote-Services-and-Monitoring_FINAL.pdf>；<https://researchportal.bath.ac.uk/en/publications/challenges-to-deploy-augmented-reality-in-manufacturing>
- **#80** 「‘Co-production’ between firms is likely to occur as collaborative communities of firms emerge」  
  判断：**部分符合**。Catena-X于2021年由28家企业支持成立，2024年Ford、Flex、T-Systems与IBM已开展跨组织数据链试点，协作社区确已出现；但档案主要证明数据与碳足迹协同，而非大规模共同生产，结果只部分实现。  
  来源：<https://www.automotivelogistics.media/digitalisation/frank-goeller-explains-how-catenax-is-making-manufacturing-logistics-processes-more-efficient-and-resilient/181037>；<https://research.cgu.edu/drucker-customer-lab/auto-6-sustainability-with-catena-x-case-study/>
- **#83** 「many of the technologies that will transform manufacturing, such as additive manufacturing, are already establ…」  
  判断：**部分符合**。增材制造到2020年规模接近128亿美元、当年增长7.5%，出版后已有实际扩张。同期增长较此前显著放缓，仅一项技术扩张不能证明多种既有技术已全面变革制造业，判部分符合。  
  来源：<https://wohlersassociates.com/press-releases/new-wohlers-report-2021-finds-7-5-growth-in-additive/>；<https://think.ing.com/uploads/reports/3D_printing_report_final_050821_RL_OT_FINAL.pdf>
- **#84** 「Primary or underpinning technologies such as information and communications technology (ICT), sensors, advance…」  
  判断：**部分符合**。ICT与传感器已广泛用于制造流程，但石墨烯和部分先进材料商业化仍受限制；原句列举的全部底层技术普及程度不一致。  
  来源：<https://www.deloitte.com/us/en/about/press-room/deloitte-2025-smart-manufacturing-survey.html>；<https://www.bcg.com/publications/2024/shaking-up-the-factory-floor-with-digital-and-ai>；<https://www.isi.fraunhofer.de/en/presse/2024/presseinfo-04-graphen-weltmarkt-anwendungsfelder.html>；<https://www.nature.com/articles/s42254-024-00754-9>
- **#85** 「A much more distributed local and global production base, with manufacturing done much closer to the customer」  
  判断：**部分符合**。Bain记录近岸与分岸投资已经实施，制造更贴近市场的部分出现；但分布式制造的规模经济研究说明并非所有组件适合分散生产。  
  来源：<https://www.bain.com/about/media-center/press-releases/2024/businesses-accelerate-reshoring-and-near-shoring-amid-heightened-geopolitical-uncertainties-and-rising-costs-bain--company-finds/>；<https://researchportal.ulisboa.pt/en/publications/technology-cost-drivers-for-a-potential-transition-to-decentraliz/>
- **#86** 「This is likely, eventually, to level, or even invert, differences in technological development between differe…」  
  判断：**部分符合**。WIPO 2024记录中国等中等收入经济体自2013年以来创新排名上升，中国达第11位；但前列仍以高收入经济体为主，地区技术差距并未全面拉平或逆转。  
  来源：<https://www.wipo.int/web-publications/global-innovation-index-2024/en/gii-2024-at-a-glance.html>；<https://www.wipo.int/edocs/pubdocs/en/wipo-pub-944-2024-en-world-intellectual-property-report-2024.pdf>
- **#89** 「simulation capabilities will become embedded within processes to provide intelligent, adaptive, real time cont…」  
  判断：**部分符合**。McKinsey记录工厂数字孪生实时连接传感器并优化良率、能耗和吞吐，仿真进入生产已出现；NIST仍称其为早期采用阶段，普遍的智能自适应实时控制尚未确立。  
  来源：<https://www.mckinsey.com/capabilities/operations/our-insights/digital-twins-the-next-frontier-of-factory-optimization>；<https://www.nist.gov/publications/digital-twins-advanced-manufacturing-standardized-approach>
- **#90** 「The added value of materials will expand as new materials such as graphene, carbon nanotubes, diamond-like car…」  
  判断：**部分符合**。Fraunhofer记录石墨烯市场近年持续增长、2022年平均估计收入3.8亿美元；Nature指出最大应用仍集中于储能与聚合物，原句列举材料的全面附加值扩展只部分得到证实。  
  来源：<https://www.isi.fraunhofer.de/en/presse/2024/presseinfo-04-graphen-weltmarkt-anwendungsfelder.html>；<https://www.nature.com/articles/s42254-024-00754-9>
- **#92** 「A number of new materials, in which the UK has strong capabilities, are currently in development and are expec…」  
  判断：**部分符合**。石墨烯等英国优势新材料已有消费品与复合材料应用，但Nature 2023指出主流商业化仍受市场成熟度限制，进入大众市场有限。  
  来源：<https://www.nature.com/articles/s42254-024-00754-9>；<https://www.idtechex.com/en/research-article/prosumer-applications-lead-early-adoption-of-graphene/34187>
- **#94** 「Biomaterials, or substances which interact with biological systems (discussed in a following section), will co…」  
  判断：**部分符合**。生物基材料进入消费品（如Sorona纤维、蘑菇皮革）有进展，但BoF 2023指出新一代材料规模化困难，渗透有限。  
  来源：<https://www.businessoffashion.com/opinions/sustainability/next-generation-materials-innovation-mylo-bolt-threads-mushroom-leather/>；<https://sustainablebrands.com/read/q-a-dupont-sorona-and-the-evolution-and-revolution-of-biomaterials>
- **#95** 「it is the integration of sensors into networks of technology that is expected to revolutionise manufacturing」  
  判断：**部分符合**。Deloitte智能制造调查报告受访企业产出及生产率最高提升20%，支持联网数字技术已改变部分生产实践。BCG调查仅16%企业达到AI目标，且整体智能制造效益不能全归于传感器联网，故“革命性”全行业程度只判部分符合。  
  来源：<https://www.deloitte.com/us/en/about/press-room/deloitte-2025-smart-manufacturing-survey.html>；<https://www.bcg.com/publications/2024/shaking-up-the-factory-floor-with-digital-and-ai>
- **#99** 「The global market for biotechnology products was valued at US$216.5 billion in 2011 and is expected to reach $…」  
  判断：**部分符合**。2017年全球生物技术市场估计约3800亿–4040亿美元（韩国生物产业信息3797亿美元；Pragma 4038亿美元），接近但低于4145亿美元预测，部分符合。  
  来源：<https://www.bioin.or.kr/metaInfoView.do?meta_info_sn=11558>；<https://www.pragmamarketresearch.com/reports/119278/global-biotechnology-market>
- **#101** 「These approaches are being applied to the industrial production of amino acids and polyketides and are expecte…」  
  判断：**部分符合**。合成生物学用于生物燃料已有项目（NREL与LanzaTech合作），但仍以研发与小规模为主，商业化有限，部分符合。  
  来源：<https://www.nlr.gov/news/detail/program/2023/nrel-launches-synthetic-biology-project-to-advance-biofuel-discovery-technologies-with-lanzatech-northwestern-and-yale>
- **#106** 「in the UK chemical sector, research and engineering practices are likely to change fundamentally, as ‘green ch…」  
  判断：**部分符合**。英国UKRI在2024年支持21项跨行业可持续生物制造合作，绿色研发方向已变化；Green Alliance指出英国化工仍高度依赖化石原料且政策存在缺口，“广泛采用并根本改变”只部分实现。  
  来源：<https://www.ukri.org/news/11-5m-bioinnovation-boost-set-to-transform-uk-manufacturing/>；<https://green-alliance.org.uk/wp-content/uploads/2024/08/Policy-barriers-to-greening-the-chemical-industry.pdf>
- **#107** 「in industrial biotechnology, biological catalysts are increasingly likely to replace chemical catalysts.」  
  判断：**部分符合**。行业报告称工业酶正越来越多替代化学催化剂，但工业酶市场2023年仅约61亿美元、年增4.4%，替代程度有限，部分符合。  
  来源：<https://www.fortunebusinessinsights.com/industrial-enzymes-market-106036>；<https://www.businesswire.com/news/home/20240603891134/en/Global-Industrial-Enzymes-Strategic-Industry-Report-2024-Market-to-Reach-%248.2-Billion-by-2030-Driven-by-Growing-Need-to-Replace-Harsh-Chemical-Processes-with-Eco-Friendly-Enzymatic-Processes---ResearchAndMarkets.com>
- **#108** 「will mean that smartphones are positioned to become ubiquitous, general purpose tools for the management of su…」  
  判断：**部分符合**。同#23：移动设备在工厂中的使用增加但不普遍（2021年仅47%一线工人获配移动设备）。  
  来源：<https://parsable.com/wp-content/uploads/2021/06/CM-FrontlineWorkersSurveyReport-R1-RegUD.pdf>；<https://www.automationworld.com/products/control/article/13318550/hey-operators-theres-an-app-for-that>
- **#112** 「Industrial products will become more autonomous in functionality, with systems which may incorporate millions …」  
  判断：**部分符合**。工业调查记录自主移动机器人、协作机器人与AI成为实际投资和应用领域，但没有证实工业产品普遍达到系统级高度自主及数百万传感器规模。  
  来源：<https://www.industryweek.com/technology-and-iiot/article/55017723/rockwell-automation-chronicles-the-rise-of-ai>；<https://www.universal-robots.com/blog/this-is-what-they-told-us-how-manufacturers-are-embracing-technology-in-2024/>
- **#120** 「It is expected to lead to profound changes in the way businesses make almost any product over the coming decad…」  
  判断：**部分符合**。同#21：增材制造增长但2020年行业仅约128亿美元，对“几乎所有产品”的深刻影响尚未出现（终点为未来数十年）。  
  来源：<https://wohlersassociates.com/press-releases/new-wohlers-report-2021-finds-7-5-growth-in-additive/>；<https://think.ing.com/uploads/reports/3D_printing_report_final_050821_RL_OT_FINAL.pdf>
- **#122** 「A key driver of future manufacturing is likely to be a shift to more sustainable manufacturing」  
  判断：**部分符合**。可持续制造进入工业研发、减排目标及循环设计政策，但2024年全球循环率报告显示实际循环性下降，整体转型尚不充分。  
  来源：<https://circulareconomy.europa.eu/platform/en/knowledge/circularity-gap-report-2024>；<https://www.deloitte.com/be/en/issues/working-together-towards-a-sustainable-future/circularity-gap-report.html>；<https://www.ukri.org/news/11-5m-bioinnovation-boost-set-to-transform-uk-manufacturing/>；<https://green-alliance.org.uk/wp-content/uploads/2024/08/Policy-barriers-to-greening-the-chemical-industry.pdf>
- **#123** 「’Circular’ business models will be promoted further by resource scarcity and tighter environmental standards」  
  判断：**部分符合**。循环商业模式受到ESPR等环境要求推动，但Deloitte记录逾70%的组织尚无循环经济举措，全球循环率下降，推广只部分落地。  
  来源：<https://circulareconomy.europa.eu/platform/en/knowledge/circularity-gap-report-2024>；<https://www.deloitte.com/be/en/issues/working-together-towards-a-sustainable-future/circularity-gap-report.html>；<https://eur-lex.europa.eu/eli/reg/2024/1781/2024-06-28/eng>；<https://www.consilium.europa.eu/en/press/press-releases/2024/05/27/green-transition-council-gives-its-final-approval-to-the-ecodesign-regulation/>
- **#127** 「It is likely that the factories of the future will be increasingly diverse」  
  判断：**部分符合**。近岸、分岸与不同配置的制造布局出现，但成本研究显示分布式技术只适合部分组件，工厂多样化没有在所有行业普遍实现。  
  来源：<https://www.bain.com/about/media-center/press-releases/2024/businesses-accelerate-reshoring-and-near-shoring-amid-heightened-geopolitical-uncertainties-and-rising-costs-bain--company-finds/>；<https://researchportal.ulisboa.pt/en/publications/technology-cost-drivers-for-a-potential-transition-to-decentraliz/>
- **#128** 「Factory locations are likely to become increasingly diverse and nearer to the customer’s home.」  
  判断：**部分符合**。Bain记录企业已开展近岸与分岸布局，支持工厂位置更靠近市场；分布式制造成本研究仍显示配置多样化受规模经济约束，选址变化只部分实现。  
  来源：<https://www.bain.com/about/media-center/press-releases/2024/businesses-accelerate-reshoring-and-near-shoring-amid-heightened-geopolitical-uncertainties-and-rising-costs-bain--company-finds/>；<https://researchportal.ulisboa.pt/en/publications/technology-cost-drivers-for-a-potential-transition-to-decentraliz/>
- **#129** 「Advances in additive manufacturing and other technologies will allow factories on a micro scale to become much…」  
  判断：**部分符合**。增材制造推动部分分布式/微型生产，但家用3D打印未达预期（Vox 2016、SMH 2022），只部分符合。  
  来源：<https://www.vox.com/2016/6/6/11693388/makerbot-home-3d-printers>；<https://www.smh.com.au/technology/the-3d-printer-was-supposed-to-be-everywhere-by-now-so-where-is-it-20220804-p5b7ai.html>
- **#134** 「Products are also likely to become increasingly ‘information-dense’ or ‘informated’」  
  判断：**部分符合**。欧盟数字产品护照将要求产品携带来源与可持续性信息，但截至2026年仍在实施准备中，产品普遍显示来源与绿色属性尚未实现。  
  来源：<https://single-market-economy.ec.europa.eu/single-market/goods/european-standards/harmonised-standards/digital-product-passport-dpp_en>；<https://eur-lex.europa.eu/eli/reg/2024/1781/2024-06-28/eng>
- **#135** 「This likely trend implies that the scale of many factories will get smaller over the next decades for many sec…」  
  判断：**部分符合**。圣路易斯联储记录美国平均制造厂就业规模长期下降、2024年约32人，印度研究也记录单厂常规工人规模下降；按就业规模有支持，但并不等于全球多数行业的产能和物理工厂规模都减小。  
  来源：<https://www.policyedge.in/p/bigger-firms-smaller-factories-the-declining-productive-scale-in-indian-manufacturing>；<https://www.stlouisfed.org/on-the-economy/2025/aug/sluggish-renaissance-us-manufacturing>
- **#137** 「Factories are therefore likely to move closer to customers, build more localised products, and use more local …」  
  判断：**部分符合**。Bain记录企业实际开展近岸和分岸布局，支持工厂贴近市场；但全部使用本地材料、制造本地化产品与工厂普遍移近客户未获一致证实。  
  来源：<https://www.bain.com/about/media-center/press-releases/2024/businesses-accelerate-reshoring-and-near-shoring-amid-heightened-geopolitical-uncertainties-and-rising-costs-bain--company-finds/>；<https://researchportal.ulisboa.pt/en/publications/technology-cost-drivers-for-a-potential-transition-to-decentraliz/>
- **#139** 「Resources such as energy, materials, land and water are likely to become scarcer, with availability increasing…」  
  判断：**部分符合**。2021–2022年能源供应紧张、价格飙升，但2014–2020年多数资源价格下跌；“更稀缺、供应更不稳定”只部分符合。  
  来源：<https://thedocs.worldbank.org/en/doc/24e8d315b8229b791ea61e0fa09b28d0-0350012022/related/CMO-April-2022-Executive-Summary.pdf>；<https://www.imf.org/external/pubs/ft/fandd/2015/12/baffes.htm>
- **#140** 「The market for technologies and knowledge that enable resource-efficient production will grow quickly」  
  判断：**部分符合**。工业能源管理系统2014年收入123亿美元、同比增9%，但IEA指出工业能效投资自2015年相对稳定；资源效率技术知识市场的快速持续增长只部分成立。  
  来源：<https://www.iea.org/reports/energy-efficiency-2024/executive-summary>；<https://www.iea.org/reports/tracking-energy-efficiency-investment-progress>；<https://www.iea.org/reports/world-energy-investment-2019/energy-end-use-and-efficiency>；<https://blog.advancedenergyunited.org/advanced-energy-now-connectivity-analytics-drive-energy-management>
- **#144** 「International ‘fragmentation’ of manufacturing value chains will continue to be driven by advances in ICT and …」  
  判断：**部分符合**。ICT推动的价值链碎片化在2010年代明显放缓，GVC参与率在多次冲击后下降（WTO），只部分符合。  
  来源：<https://www.wto.org/english/res_e/booksp_e/03_gvc_executive-summary_dev_report_2021_e.pdf>；<https://www.wto.org/english/res%5Fe/booksp%5Fe/gvcreport2025-01%5Fe.pdf>
- **#148** 「A baseline scenario for 2022 indicates if trends continue, with sustained economic recovery, a current account…」  
  判断：**部分符合**。ONS《粉皮书2023》初值为2022年经常账户赤字占GDP 3.1%，接近3%；但最新修订序列(AA6H)为2.0%，部分符合。  
  来源：<https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/bulletins/unitedkingdombalanceofpaymentsthepinkbook/2023>；<https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/timeseries/aa6h/ukea>
- **#156** 「UK exports are likely to increase at a similar rate of 3-4% over the next decade.」  
  判断：**部分符合**。ONS显示2010年以来英国出口增长主要靠服务、货物出口增长很弱；按名义计十年年均约5%，按实际计明显低于3–4%，口径不明，只部分符合。  
  来源：<https://www.ons.gov.uk/businessindustryandtrade/internationaltrade/articles/recenttrendsinuktradevolumesandbalances/2010to2024>；<https://www.theglobaleconomy.com/United-Kingdom/Growth_of_exports/>
- **#157** 「the UK’s comparative advantage in high-technology sectors will be a source of export growth in the future.」  
  判断：**部分符合**。ADS记录航空航天、国防、安全与航天产业出口2013至2023年增32%至387亿英镑；Make UK则记录2024年航空航天等出口增6.6%、电子电气增2.4%，化工制药降14%，高技术出口拉动在不同部门表现不一。  
  来源：<https://www.adsgroup.org.uk/knowledge/value-of-aerospace-defence-security-and-space-sectors-to-uk-economy-increased-50-in-last-10-years-new-data-finds/>；<https://www.makeuk.org/docs/manufacturing-facts-2025pdf/download?attachment=>
- **#180** 「Additive manufacturing (see Chapter 3) is likely to play an increasingly important role by allowing customised…」  
  判断：**部分符合**。增材制造在就近生产备件/定制零件中应用增长，但行业规模仍小（2020年约128亿美元），只部分符合。  
  来源：<https://wohlersassociates.com/press-releases/new-wohlers-report-2021-finds-7-5-growth-in-additive/>；<https://think.ing.com/uploads/reports/3D_printing_report_final_050821_RL_OT_FINAL.pdf>
- **#182** 「Rapid improvements in coordination and communication technology, for example advances in telepresence technolo…」  
  判断：**部分符合**。技术进步使供应链更复杂，但碎片化在2010年代放缓、疫情后区域化增加（WTO、McKinsey），只部分符合。  
  来源：<https://www.wto.org/english/res_e/booksp_e/03_gvc_executive-summary_dev_report_2021_e.pdf>；<https://www.mckinsey.com/capabilities/operations/our-insights/tech-and-regionalization-bolster-supply-chains-but-complacency-looms>
- **#184** 「Falling export shares are almost inevitable, given developments in emerging economies」  
  判断：**部分符合**。英国货物出口占全球份额降至约2.1%（Make UK 2024），但货物与服务合计份额2012年3.73%、2024年3.71%基本持平，只部分符合。  
  来源：<https://www.theglobaleconomy.com/United-Kingdom/share_world_exports/>；<https://www.makeuk.org/docs/uk-manufacturing-facts-2024-report/download?attachment=>
- **#187** 「As a result, these resources will be subject to greater competition and therefore increasing prices.」  
  判断：**部分符合**。资源竞争与2021–2022年价格飙升出现，但2014–2016年和2020年大宗商品价格大跌，长期上涨只部分符合。  
  来源：<https://www.worldbank.org/en/news/press-release/2022/04/26/food-and-energy-price-shocks-from-ukraine-war>；<https://www.imf.org/external/pubs/ft/fandd/2015/12/baffes.htm>
- **#194** 「In the short and medium term, the move towards a decarbonised energy system is likely to involve higher energy…」  
  判断：**部分符合**。英国工业电价为欧洲和G7最高，部分源于政策成本，但2021–2022年飙升主要因天然气价格，脱碳导致更高能源价格只部分证实。  
  来源：<https://fullfact.org/economy/uk-world-electricity-prices/>；<https://www.eiug.co.uk/high-uk-industrial-electricity-prices-continue-to-damage-competitiveness-of-energy-intensive-industries/>
- **#196** 「Prices of fossil fuels, on the other hand, are likely to rise.」  
  判断：**部分符合**。化石燃料价格2022年大涨，但布伦特油价从2013年108.6美元降至2024年80.5美元，长期上涨只部分符合。  
  来源：<https://en.lavajato.org/data/series/brent_anual.csv>；<https://www.worldbank.org/en/news/press-release/2022/04/26/food-and-energy-price-shocks-from-ukraine-war>
- **#197** 「In the future, there is likely to be an increased risk of UK electricity system failure.」  
  判断：**部分符合**。英国电力系统风险曾上升：2016年备用容量降至创纪录低位需应急措施，2019年8月9日停电影响逾100万用户；但NESO近年预测供应充足，只部分符合。  
  来源：<https://www.telegraph.co.uk/business/2016/07/08/uk-relies-on-emergency-measures-to-avert-winter-blackouts/>；<https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/855767/e3c-gb-power-disruption-9-august-2019-final-report.pdf>；<https://assets.publishing.service.gov.uk/media/6763f85acdb5e64b69e3084c/statutory-security-of-supply-report-2024.pdf>
- **#202** 「In the decades ahead, the world is likely to experience rising energy costs, greater demand for energy from ma…」  
  判断：**部分符合**。2021–2022年能源成本上升、供应安全下降（俄乌冲突），但此前2014–2020年能源价格偏低，只部分符合。  
  来源：<https://thedocs.worldbank.org/en/doc/24e8d315b8229b791ea61e0fa09b28d0-0350012022/related/CMO-April-2022-Executive-Summary.pdf>；<https://fullfact.org/economy/uk-world-electricity-prices/>
- **#204** 「The security of supply of the future UK energy system is likely to worsen, even in the short term.」  
  判断：**部分符合**。2016年英国备用容量降至创纪录低位，供应安全短期恶化；此后保持充足，只部分符合。  
  来源：<https://www.telegraph.co.uk/business/2016/07/08/uk-relies-on-emergency-measures-to-avert-winter-blackouts/>；<https://assets.publishing.service.gov.uk/media/6763f85acdb5e64b69e3084c/statutory-security-of-supply-report-2024.pdf>
- **#225** 「It will take place closer to the customer, with a much greater range of products becoming more ‘personalised’ …」  
  判断：**部分符合**。近岸/分岸布局已实施，个性化产品趋势也出现；但面向全部客户的就近制造和大范围个性化仍只部分实现。  
  来源：<https://www.bain.com/about/media-center/press-releases/2024/businesses-accelerate-reshoring-and-near-shoring-amid-heightened-geopolitical-uncertainties-and-rising-costs-bain--company-finds/>；<https://researchportal.ulisboa.pt/en/publications/technology-cost-drivers-for-a-potential-transition-to-decentraliz/>；<https://www.euromonitor.com/article/introducing-the-personalisation-megatrend>；<https://www.prescouter.com/inquiry/the-future-of-consumer-goods-harnessing-hyper-personalization-and-mass-customization/>
- **#226** 「Factories of the future will be more diverse in their scale, with potential for mobile and home manufacturing.」  
  判断：**部分符合**。制造布局更多样且出现移动/院内等小规模生产，但家用3D打印未普及，多样工厂与家庭制造的组合只部分实现。  
  来源：<https://www.bain.com/about/media-center/press-releases/2024/businesses-accelerate-reshoring-and-near-shoring-amid-heightened-geopolitical-uncertainties-and-rising-costs-bain--company-finds/>；<https://researchportal.ulisboa.pt/en/publications/technology-cost-drivers-for-a-potential-transition-to-decentraliz/>；<https://www.vox.com/2016/6/6/11693388/makerbot-home-3d-printers>；<https://www.smh.com.au/technology/the-3d-printer-was-supposed-to-be-everywhere-by-now-so-where-is-it-20220804-p5b7ai.html>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC11707413/>；<https://ashpublications.org/bloodict/article/2/2/100053/567760/Decentralized-CAR-T-manufacturing-highlighting>
- **#228** 「Successful manufacturers will significantly reduce inputs (for example materials and energy) while increasing …」  
  判断：**部分符合**。工业能效管理工具已实际部署，制造投入效率有进展；但世界物质投入仍庞大且循环率下降，减少投入同时增加客户价值未普遍确立。  
  来源：<https://literature.rockwellautomation.com/idc/groups/literature/documents/sp/rok-sp001_-en-p.pdf>；<https://circulareconomy.europa.eu/platform/en/knowledge/circularity-gap-report-2024>；<https://www.deloitte.com/be/en/issues/working-together-towards-a-sustainable-future/circularity-gap-report.html>
- **#229** 「They will also place much greater emphasis on new ways of doing business, such as moving to a ‘circular econom…」  
  判断：**部分符合**。循环模式政策与实践增加，但逾70%的组织尚未开展循环举措，2018至2023年全球循环率下降，未来更重视再制造只部分实现。  
  来源：<https://circulareconomy.europa.eu/platform/en/knowledge/circularity-gap-report-2024>；<https://www.deloitte.com/be/en/issues/working-together-towards-a-sustainable-future/circularity-gap-report.html>；<https://eur-lex.europa.eu/eli/reg/2024/1781/2024-06-28/eng>；<https://www.consilium.europa.eu/en/press/press-releases/2024/05/27/green-transition-council-gives-its-final-approval-to-the-ecodesign-regulation/>
- **#233** 「products will change in response to ageing populations (see Chapter 6). and changing levels of personal wealth…」  
  判断：**部分符合**。CPRAM记录美国65岁以上人群消费地位由十年前落后转为领先，NIQ也记录50岁以上消费偏好差异；老龄化改变需求已出现，但发达和新兴经济体财富变化引起的全部产品结构变化未完整覆盖。  
  来源：<https://cpram.com/sgp/en/individual/publications/megatrends/the-consumption-by-the-silver-population>；<https://nielseniq.com/global/en/insights/report/2024/the-multi-trillion-dollar-market/>
- **#234** 「new foreign investments in manufacturing are likely manufacturers make use of a wider ‘value chain’ to be draw…」  
  判断：**部分符合**。EY记录2024年欧洲制造业外资项目下降9%、新建项目下降20%，支持欧洲吸引新增制造业投资的部分走弱。欧洲总体FDI在2023年又由负转正，且全球FDI亦下降，尚不能把欧洲项目减少全部解释为投资转投别区，故判部分符合而非正确。  
  来源：<https://www.ey.com/en_gl/newsroom/2025/05/fdi-in-europe-slows-but-confidence-remains-for-long-term-rebound>；<https://unctad.org/publication/world-investment-report-2024>；<https://trendsgroup.org/insight/the-world-investment-trends-and-sdgs-funding-challenges/>

### 错误（20 条）

- **#25** 「BRIC economies (Brazil, Russia, India and China) are likely to become larger than the US by 2015 and the G7 by…」  
  判断：**错误**。Livemint报道2014年金砖五国（含南非）GDP合计约17万亿美元，仍仅“几乎追平”美国；世界银行数据显示2015年巴西、俄罗斯GDP分别萎缩3.55%、1.97%，金砖四国合计约16.55万亿美元（中国11.28、印度2.10、巴西1.80、俄罗斯1.36万亿），按名义美元未能在2015年超过美国；2032年超过G7部分尚未到期。  
  来源：<https://nationdata.org/downloads/gdp/brics-gdp-ranking-2015.csv>；<https://www.livemint.com/Politics/JpR16R0Ijx06sJRY7fdMLP/Size-matters-Brics-leaders-have-17-trillion-ways-to-rival-U.html>
- **#43** 「Any future declines will be much smaller, with around 170,000 fewer people in the sector projected by 2020 com…」  
  判断：**错误**。ONS工作岗位系列(JWR7，2024年8月版)显示制造业岗位2010年约257.2万、2020年约262.1万，不降反增，未出现“比2010年少约17万”的下降（GMB按另一口径称2010–2022年减少近20万，但终点为2022年且非预测所用口径）。  
  来源：<https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/employmentandemployeetypes/timeseries/jwr7/lms/previous/v36>；<https://www.gmb.org.uk/news/almost-200000-manufacturing-jobs-lost-2010>
- **#100** 「Sorona, an ‘eco-fibre for carpet, apparel and automotive’ developed by DuPont is a bioderived brand of poly-tr…」  
  判断：**错误**。杜邦2020年以2.4亿美元出售包括Sorona在内的生物材料业务（2022年交割给华峰），未见Sorona成为十亿美元级产品。  
  来源：<https://doi.org/10.1021/cen-10020-buscon1>；<https://sustainablebrands.com/read/q-a-dupont-sorona-and-the-evolution-and-revolution-of-biomaterials>
- **#102** 「stem cell therapies, exceeded US$3 billion in 2010 and is expected to reach $4.5 billion by 2014 and over $35 …」  
  判断：**错误**。再生医学市场2019年约125亿–133亿美元（CCRM 133亿美元），远低于预测的“超过350亿美元”。  
  来源：<https://www.ccrm.ca/wp-content/uploads/2021/01/Quick-Facts-CCRM-Media-Kit-Oct.-2020-FINAL.pdf>；<https://nextmsc.gonevis.com/regenerative-medicine-market-size-witness-highest-growth-in-near-future-by-2030-allergan-integra-lifesciences-medtronic/>
- **#121** 「between 20102012, the global market for AM products rose from US$1.3 billion to $1.9 billion72, with estimates…」  
  判断：**错误**。Wohlers Report 2021显示2020年全球增材制造行业约128亿美元，远低于预测的1000亿美元。  
  来源：<https://wohlersassociates.com/press-releases/new-wohlers-report-2021-finds-7-5-growth-in-additive/>；<https://think.ing.com/uploads/reports/3D_printing_report_final_050821_RL_OT_FINAL.pdf>
- **#124** 「worldwide litigation over IP infringement has increased in proportion to the rise in patent filings and this t…」  
  判断：**错误**。美国专利侵权诉讼自2013年以来呈下降趋势（Marcum 2024研究；Lex Machina显示2023年案件数较前降约20%），与“诉讼持续增加”相反。  
  来源：<https://info.marcumllp.com/hubfs/pdf/2024-Marcum-Patent-Litigation-Study.pdf?hsLang=en>；<https://abovethelaw.com/2024/02/3-takeaways-from-the-lex-machina-2024-patent-report/>
- **#136** 「For some product categories, distributed or even home manufacturing will be undertaken by consumers sharing da…」  
  判断：**错误**。消费者在家制造产品未成现实：Vox 2016与SMH 2022报道家用3D打印革命未兑现，3D打印机未进入普通家庭。  
  来源：<https://www.vox.com/2016/6/6/11693388/makerbot-home-3d-printers>；<https://www.smh.com.au/technology/the-3d-printer-was-supposed-to-be-everywhere-by-now-so-where-is-it-20220804-p5b7ai.html>
- **#147** 「The BRIC economies are likely to become larger than the US by 2015, and the G7 by 2032.」  
  判断：**错误**。同#25：2014年金砖五国合计仍略低于美国，2015年金砖四国名义GDP合计约16.55万亿美元且巴西、俄罗斯负增长，未在2015年超过美国。  
  来源：<https://nationdata.org/downloads/gdp/brics-gdp-ranking-2015.csv>；<https://www.livemint.com/Politics/JpR16R0Ijx06sJRY7fdMLP/Size-matters-Brics-leaders-have-17-trillion-ways-to-rival-U.html>
- **#154** 「Chinese GDP forecast to overtake the US between 2017 and 2026.」  
  判断：**错误**。按市场汇率，中国GDP至2025年仍远低于美国（2025年差距达11.3万亿美元创纪录），2026年内不可能超越；按PPP计中国早在2014年已超过美国，也不在2017–2026年窗口内。  
  来源：<https://kitegraph.com/insights/us-gdp-29-trillion>；<https://www.piie.com/blogs/realtime-economics/2025/china-vs-us-which-gdp-bigger>；<https://www.independent.co.uk/news/business/news/move-over-america-china-overtakes-us-as-world-s-biggest-economy-kind-of-9783050.html>
- **#158** 「Projecting this forward would imply an export to output ratio of 54% by 2020 and an export value of £310 billi…」  
  判断：**错误**。ONS制造业出口（CSYB）2020年约1505亿英镑，远低于预测的3100亿英镑；出口/产出比54%亦无法达到。  
  来源：<https://www.ons.gov.uk/economy/economicoutputandproductivity/output/timeseries/csyb/diop>；<https://www.makeuk.org/docs/uk-manufacturing-facts-2020-21-make-uk-santander/download?attachment=>
- **#159** 「China may overtake the US by 2026 or 201728.」  
  判断：**错误**。同#154：按市场汇率中国至2025年未超越美国且差距扩大；PPP口径在2014年已超越，均不符合“2017或2026年超越”。  
  来源：<https://kitegraph.com/insights/us-gdp-29-trillion>；<https://www.piie.com/blogs/realtime-economics/2025/china-vs-us-which-gdp-bigger>
- **#170** 「China’s growth in the recent past has been close to 10% per year with Chinese GDP forecast to overtake the Uni…」  
  判断：**错误**。同#154：中国GDP（市场汇率）在2017–2026年间未超过美国，2025年差距创纪录。  
  来源：<https://kitegraph.com/insights/us-gdp-29-trillion>；<https://www.piie.com/blogs/realtime-economics/2025/china-vs-us-which-gdp-bigger>
- **#174** 「Replacing the RDA regime entails a difficult institutional transformation but pressures to embrace democracy a…」  
  判断：**错误**。自由之家指出中国威权体制在近年更加压制，过去十年自由得分下降，未出现走向民主的压力增强迹象。  
  来源：<https://freedomhouse.org/country/china/freedom-world/2023>；<https://freedomhouse.org/article/chinese-communist-partys-ride-or-die-moment>
- **#176** 「’Business-as-usual’ projections of the structure of the UK economy show a continuing tendency to de-industrial…」  
  判断：**错误**。2010–2020年制造业就业并未下降：JWR7工作岗位由约257.2万增至约262.1万，不在“减少14万–55万”范围。  
  来源：<https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/employmentandemployeetypes/timeseries/jwr7/lms/previous/v36>
- **#179** 「It appears likely, therefore, is that globalisation and the ‘second unbundling’ may still develop much further…」  
  判断：**错误**。WTO显示GVC扩张在2010年代显著放缓，参与率在2018年中美争端与2020年疫情后下降，“第二次分拆进一步大幅发展”未出现。  
  来源：<https://www.wto.org/english/res_e/booksp_e/03_gvc_executive-summary_dev_report_2021_e.pdf>；<https://www.wto.org/english/res%5Fe/booksp%5Fe/gvcreport2025-01%5Fe.pdf>
- **#183** 「The weight of the evidence and analysis suggests a continued, likely and significant growth in the internation…」  
  判断：**错误**。WTO报告显示2010–2019年间接出口与总出口增速大幅放缓、GVC参与率在冲击后下降，供应链国际化未“持续显著增长”。  
  来源：<https://www.wto.org/english/res_e/booksp_e/03_gvc_executive-summary_dev_report_2021_e.pdf>；<https://www.wto.org/english/res%5Fe/booksp%5Fe/gvcreport2025-01%5Fe.pdf>
- **#210** 「Any future declines will be much smaller, with around 170,000 fewer people in the sector expected by 2020 comp…」  
  判断：**错误**。同#43：2020年制造业岗位（约262.1万）高于2010年（约257.2万），未减少17万。  
  来源：<https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/employmentandemployeetypes/timeseries/jwr7/lms/previous/v36>
- **#217** 「It is likely that future increases in output in manufacturing will be associated with some further reductions …」  
  判断：**错误**。同#43：2010–2020年制造业岗位未减少（JWR7约257.2万→262.1万）。  
  来源：<https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/employmentandemployeetypes/timeseries/jwr7/lms/previous/v36>
- **#218** 「which would result in these roles comprising around 40% of the total projected manufacturing employment of aro…」  
  判断：**错误**。2020年英国制造业工作岗位约262.1万（ONS JWR7），高于预测的约240万。  
  来源：<https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/employmentandemployeetypes/timeseries/jwr7/lms/previous/v36>
- **#231** 「BRIC economies are likely to become larger than to increase the scale and ambition of its current the US by 20…」  
  判断：**错误**。World Bank同一历史版2015年名义GDP表中，中印巴俄合计16.323024万亿美元，低于美国18.036648万亿美元，2015年超过美国的终点未实现。按该已到期明确子终点判错误；2032年超过G7的另一子终点尚未到，不预判其真假。  
  来源：<https://www.pacificresearch.org/wp-content/uploads/2017/06/GDP.pdf>；<https://databank.worldbank.org/embed/US-2016/id/c34167a7>；<https://www.eea.europa.eu/en/analysis/maps-and-charts/historic-and-projected-gdp-in>

### 暂无法判断（46 条）

- **#1** 「Manufacturing in 2050 will look very different from today」  
  判断：**暂无法判断**。这是以2050年为终点的制造业总体愿景，截止日尚未到2050年；没有把“与今天不同”误判为非预测。  
  来源：<https://www.deloitte.com/us/en/about/press-room/deloitte-2025-smart-manufacturing-survey.html>；<https://www.bcg.com/publications/2024/shaking-up-the-factory-floor-with-digital-and-ai>
- **#2** 「manufacturing becomes faster, more responsive to changing global markets and closer to customers.」  
  判断：**暂无法判断**。上下文属于2050年制造业愿景；制造业响应性已有数字化改善，但2050年“更快、更近客户”的综合结果尚未到期。  
  来源：<https://www.deloitte.com/us/en/about/press-room/deloitte-2025-smart-manufacturing-survey.html>；<https://www.bcg.com/publications/2024/shaking-up-the-factory-floor-with-digital-and-ai>
- **#3** 「Products and processes will be sustainable, with built-in reuse, remanufacturing and recycling for products re…」  
  判断：**暂无法判断**。产品生命周期内置再利用、再制造与回收属于2050年愿景，终点未到；目前全球循环率反而下降，不能先给趋势分。  
  来源：<https://circulareconomy.europa.eu/platform/en/knowledge/circularity-gap-report-2024>；<https://www.deloitte.com/be/en/issues/working-together-towards-a-sustainable-future/circularity-gap-report.html>
- **#4** 「Closed loop systems will be used to eliminate energy and water waste and to recycle physical waste.」  
  判断：**暂无法判断**。本节把闭环系统置于2050年制造愿景中，截止日尚未到期，不能以现有循环项目宣布能源和水浪费已消除。  
  来源：<https://circulareconomy.europa.eu/platform/en/knowledge/circularity-gap-report-2024>；<https://www.deloitte.com/be/en/issues/working-together-towards-a-sustainable-future/circularity-gap-report.html>
- **#22** 「Computerised manufacturing execution systems (MES) will work increasingly in real time」  
  判断：**暂无法判断**。未检索到可直接说明制造执行系统（MES）实时运行普及程度的统计，无法判断。  
  来源：<https://www.forrester.com/report/the-state-of-cloud-in-manufacturing-2024/RES180386>
- **#26** 「the ‘N-11’ economiesii are likely to become larger than the US and almost twice the size of the Euro area by 2…」  
  判断：**暂无法判断**。终点为2050年，尚未到期。  
  来源：<https://www.pwc.com/gx/en/world-2050/assets/pwc-the-world-in-2050-full-report-feb-2017.pdf>
- **#28** 「population with annual per capita expenditure between US$3,650 and US$36,500 (2005 prices), is estimated to mo…」  
  判断：**暂无法判断**。终点为2030年，尚未到期（Brookings估计2023年全球消费阶层约40亿人，2031年或达50亿，口径不同）。  
  来源：<https://www.brookings.edu/articles/how-the-world-consumer-class-will-grow-from-4-billion-to-5-billion-people-by-2031/>
- **#29** 「Asia’s share of the group will rise from 30% to 64%.」  
  判断：**暂无法判断**。亚洲中产占比的终点为2030年，尚未到期。  
  来源：<https://www.brookings.edu/articles/how-the-world-consumer-class-will-grow-from-4-billion-to-5-billion-people-by-2031/>
- **#30** 「There will be 3 billion more people in the world by 205034 with 97% of population growth taking place in devel…」  
  判断：**暂无法判断**。终点为2050年，尚未到期。  
  来源：<https://www.un.org/en/UN-projects-world-population-to-peak-within-this-century>
- **#33** 「If current trends continue, the foreign-owned manufacturing sector within the UK will account for a larger sha…」  
  判断：**暂无法判断**。未检索到可直接比较外资与本国所有制造业产出、增加值、就业份额的统计（ONS仅有全经济外资企业数据），无法判断。  
  来源：<https://www.ons.gov.uk/businessindustryandtrade/business/businessservices/articles/annualbusinesssurvey/2021>
- **#38** 「A growing global population and increased urbanisation (70% of the global population will live in urban areas …」  
  判断：**暂无法判断**。城市化与资源需求的终点为2050年（UN预计2050年68%人口居住城市），尚未到期。  
  来源：<https://www.un.org/en/desa/68-world-population-projected-live-urban-areas-2050-says-un>
- **#41** 「2050 & beyond: A resource constrained world」  
  判断：**暂无法判断**。情景图明确指向2050年及以后，尚未到达这一观察终点；资源消耗与循环率数据不能提前裁决该世界状态。  
  来源：<https://circulareconomy.europa.eu/platform/en/knowledge/circularity-gap-report-2024>；<https://www.deloitte.com/be/en/issues/working-together-towards-a-sustainable-future/circularity-gap-report.html>
- **#44** 「However, there will be around 800,000 jobs to fill in the years up to 2020, as people retire or leave manufact…」  
  判断：**暂无法判断**。“约80万个岗位需填补”是退休/离职替代需求的模型测算，无官方实际统计可核对。  
  来源：<https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/303434/evidence-report-41-working-futures-2010-2020.pdf>
- **#46** 「By 2030, 17% of the UK population will be aged between 60-74.」  
  判断：**暂无法判断**。终点为2030年，尚未到期。  
  来源：<https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationprojections/bulletins/nationalpopulationprojections/2022based>
- **#47** 「By 2020 there are expected to be an additional 80,000 managerial, professional and associate professional and …」  
  判断：**暂无法判断**。未检索到可直接核对2010–2020年制造业管理/专业/技术岗位净增数的统计，无法判断。  
  来源：<https://www.nfer.ac.uk/media/gctlixoe/long-run-employment-prospects-for-the-uk_revised-tables-and-figures.pdf>
- **#50** 「By 2050 patterns of employment will be influenced by new forms of human enhancement and augmented capabilities…」  
  判断：**暂无法判断**。2050年人类增强改变就业模式的终点未到；虽已有外骨骼部署，但没有就业模式整体改变的证据，暂不计趋势分。  
  来源：<https://corporate.ottobock.com/en/media/newsroom/ikea-exoskeletons>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC10884500/>
- **#51** 「Higher level skills, vocational training, apprenticeships and STEM qualifications will be critical as the manu…」  
  判断：**暂无法判断**。未检索到制造业内部管理/专业/技术岗位占比时间序列，无法判断。  
  来源：<https://www.nfer.ac.uk/media/gctlixoe/long-run-employment-prospects-for-the-uk_revised-tables-and-figures.pdf>
- **#55** 「Urban sites will become common as factories reduce their environmental impacts27.」  
  判断：**暂无法判断**。未检索到可核对“城市厂址普遍化”的证据，无法判断。  
  来源：—
- **#56** 「The ‘global middle-class’ with annual per capita expenditure between US$3,650 and US$36,500, is estimated to m…」  
  判断：**暂无法判断**。终点为2030年，尚未到期。  
  来源：<https://www.brookings.edu/articles/how-the-world-consumer-class-will-grow-from-4-billion-to-5-billion-people-by-2031/>
- **#57** 「There will be 3 billion more people in the world by 205029 with 97% of population growth by 2050 taking place …」  
  判断：**暂无法判断**。终点为2050年，尚未到期。  
  来源：<https://www.un.org/en/UN-projects-world-population-to-peak-within-this-century>
- **#63** 「Forming strategic alliances with manufacturers across sub-sectors, resulting in collaborative communities whic…」  
  判断：**暂无法判断**。ABI证实跨企业协作工具广泛使用，但两轮检索的网络治理研究没有给出“协作社区在制造活动中超过龙头主导网络”的可比规模或份额。  
  来源：<https://www.abiresearch.com/press/study-shows-76-of-discrete-and-process-manufacturers-use-cloud-platforms-for-real-time-collaboration-and-supply-chain-efficiency>；<https://journals.sagepub.com/doi/full/10.1177/0308518X231202390>；<https://link.springer.com/article/10.1007/s43253-024-00121-5>
- **#78** 「The most valuable future economic activity in biotechnology and nanotechnology is likely to not be in the manu…」  
  判断：**暂无法判断**。两轮资料说明生物与纳米技术有广泛应用价值及商业化成本障碍，但未提供应用环节相对投入材料制造的可比增加值或利润排序。  
  来源：<https://www3.weforum.org/docs/WEF_Accelerating_the_Tech_Driven_Bioeconomy_2024.pdf>；<https://www.researchandmarkets.com/reports/5950113/lipid-nanoparticle-raw-materials-market-size>；<https://www.bcg.com/publications/2024/breaking-the-cost-barrier-on-biomanufacturing>
- **#87** 「with investments in automation alone expected to comprise some 8% of global ICT expenditure by 20206.」  
  判断：**暂无法判断**。未检索到“自动化投资占全球ICT支出比例”的2020年统计，无法核对8%。  
  来源：<https://resources.flexera.com/web/pdf/Report-SLO-State-of-Tech-Spend-2020.pdf>
- **#88** 「Over the next 20 years, modelling and simulation is expected to become integrated into all design processes as…」  
  判断：**暂无法判断**。终点为“未来20年”（约2033年），尚未到期。  
  来源：—
- **#115** 「In the next three decades, the development of powered exoskeletons (a wearable robotics suit), artificial and …」  
  判断：**暂无法判断**。终点为“未来三十年”（约2043年），尚未到期。  
  来源：—
- **#126** 「Working practices and environments will change, the workforce will age and the requirement for mental rather t…」  
  判断：**暂无法判断**。上下文明确“未来四十年”（约2053年），老龄化与脑力需求的长期复合结果未到终点；不凭几个辅助外骨骼案例提前判对。  
  来源：<https://corporate.ottobock.com/en/media/newsroom/ikea-exoskeletons>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC10884500/>
- **#130** 「2050, second-by-second data on usage will allow manufacturers to alter products while in use」  
  判断：**暂无法判断**。2050年终点未到；2024年已有电池OTA远程修改，但未能证明“秒级使用数据”驱动所有所述在用产品调整的综合结果。  
  来源：<https://ugowork.com/resources/new-over-the-air-ota-updates-with-ugowork-batteries/>；<https://link.springer.com/article/10.1007/s10462-024-10968-z>
- **#131** 「is likely to be well positioned, for example, in the market for human enhancement technologies which is set to…」  
  判断：**暂无法判断**。英国康复机器人2024年有市场收入且本土神经植入研发活跃，但两轮资料没有给出全口径人类增强市场实际增长及英国相对竞争优势的可比序列。  
  来源：<https://corporate.ottobock.com/en/media/newsroom/ikea-exoskeletons>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC10884500/>；<https://www.grandviewresearch.com/horizon/outlook/rehabilitation-robots-market/uk>；<https://www.imperial.ac.uk/news/255319/mint-amber-gold-spinouts-colour-future/>
- **#133** 「The new manufacturing services business models that will become mainstream out to 2050 will involve customers …」  
  判断：**暂无法判断**。到2050年按功能或全生命周期付费成为主流的终点未到；服务收入占比增加不能等同于这种特定付费模式已成主流。  
  来源：<https://www.bain.com/insights/services-build-value-for-the-industrial-sector-snap-chart/>；<https://www.techtarget.com/news/Manufacturers-turn-to-servitization-for-competitive-advantage/852858/>；<https://www.pwc.com/hu/en/kiadvanyok/assets/pdf/sharing-economy-en.pdf>；<https://www.brookings.edu/articles/the-current-and-future-state-of-the-sharing-economy/>；<https://doi.org/10.31893/multirev.2024201>
- **#150** 「A decline in the share of manufacturing as a proportion of total inward FDI is likely.」  
  判断：**暂无法判断**。未检索到英国内向FDI存量按行业（制造业占比）的可读时间序列，无法判断。  
  来源：<https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/bulletins/foreigndirectinvestmentinvolvingukcompanies/2023>
- **#151** 「Foreign-owned manufacturers in the UK will continue to increase.」  
  判断：**暂无法判断**。ONS显示2015–2021年全经济外资企业数增长52.2%，但缺少制造业单列数据，无法判断。  
  来源：<https://www.ons.gov.uk/businessindustryandtrade/business/businessservices/articles/annualbusinesssurvey/2021>
- **#152** 「manufacturing sector within the UK will account for a larger share of output (by 2020), gross value added (GVA…」  
  判断：**暂无法判断**。同#33：缺少外资与本国制造业份额的可比统计。  
  来源：<https://www.ons.gov.uk/businessindustryandtrade/business/businessservices/articles/annualbusinesssurvey/2021>
- **#155** 「history suggests that Chinese catch-up may stall before 2050.」  
  判断：**暂无法判断**。终点为2050年前，尚未到期。  
  来源：—
- **#161** 「By 2050, the G7 countries will still be the wealthiest (Figure 4.10)31: At about US$78,00032 the UK will enjoy…」  
  判断：**暂无法判断**。终点为2050年，尚未到期。  
  来源：<https://www.pwc.com/gx/en/world-2050/assets/pwc-the-world-in-2050-full-report-feb-2017.pdf>
- **#164** 「the deficit on manufacturing trade increases in monetary terms from an estimated £67 billion in 2012 to £85 bi…」  
  判断：**暂无法判断**。未检索到可直接核对的2022年制造品贸易差额数值，无法判断850亿英镑。  
  来源：<https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/articles/uktradeingoodsyearinreview/2022/pdf>
- **#165** 「However, relative to the economy as a whole it declines from 4.4% of GDP in 2012 to 3.3% in 2022」  
  判断：**暂无法判断**。同#164：缺少2022年制造品贸易逆差占GDP比重数据。  
  来源：<https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/articles/uktradeingoodsyearinreview/2022/pdf>
- **#168** 「it is difficult to envisage anything other than a continuing decline in the share of manufacturing as a propor…」  
  判断：**暂无法判断**。同#150：缺少制造业在英国内向FDI中占比的时间序列。  
  来源：<https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/bulletins/foreigndirectinvestmentinvolvingukcompanies/2023>
- **#169** 「It is likely that the foreign-owned manufacturing sector within the UK will soon account for a larger share of…」  
  判断：**暂无法判断**。同#33：缺少外资与本国制造业份额的可比统计。  
  来源：<https://www.ons.gov.uk/businessindustryandtrade/business/businessservices/articles/annualbusinesssurvey/2021>
- **#178** 「with the most plausible scenarios producing a manufacturing share of GDP of either 7.3% or 9.7% in 2035.」  
  判断：**暂无法判断**。终点为2035年，尚未到期。  
  来源：<https://www.theglobaleconomy.com/United-Kingdom/Share_of_manufacturing/>
- **#185** 「Recent levels of public investment imply these ratios will continue to fall.」  
  判断：**暂无法判断**。检索结果未给出公共资本存量/GDP比率的时间序列，无法核对“继续下降”。  
  来源：<https://obr.uk/docs/dlm_uploads/Public-investment-and-potential-output_August-2024.pdf>；<https://ifs.org.uk/articles/public-investment-what-you-need-know>
- **#211** 「However, there will still be strong demand for workers, with around 800,000 roles to be filled up to 2020 as p…」  
  判断：**暂无法判断**。同#44：替代需求测算无实际统计可核对。  
  来源：<https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/303434/evidence-report-41-working-futures-2010-2020.pdf>
- **#213** 「By 2030, 17% of the population will be aged between 60-74.」  
  判断：**暂无法判断**。终点为2030年，尚未到期。  
  来源：<https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationprojections/bulletins/nationalpopulationprojections/2022based>
- **#214** 「With regard to future demand for skills, by 2020 an additional 80,000 people in the UK are expected to be empl…」  
  判断：**暂无法判断**。同#47：缺少管理/专业/技术岗位净增统计。  
  来源：<https://www.nfer.ac.uk/media/gctlixoe/long-run-employment-prospects-for-the-uk_revised-tables-and-figures.pdf>
- **#215** 「Despite this overall decline, projections indicate that there will still be about 800,000 manufacturing roles …」  
  判断：**暂无法判断**。同#44：替代需求测算无实际统计可核对。  
  来源：<https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/303434/evidence-report-41-working-futures-2010-2020.pdf>
- **#216** 「Looking to the decades ahead, it seems likely that few ‘low value and high employment’ manufacturing activitie…」  
  判断：**暂无法判断**。“低价值高就业”活动保留程度缺乏统一度量，且为未来数十年的判断，无法判断。  
  来源：—
- **#221** 「By 2030, 17% of the population will be aged between 60-74, with the proportion of the population over 75 overt…」  
  判断：**暂无法判断**。终点为2050年，尚未到期。  
  来源：<https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationprojections/bulletins/nationalpopulationprojections/2022based>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/uk-goscience-future-of-manufacturing-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/uk-goscience-future-of-manufacturing-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/uk-goscience-future-of-manufacturing-v5/audit/manual_review_2026-11-15.py`
## 返工审计

- 60项逐字段恢复，全部60项进入预测分母；不因摘要/正文重复降unclear或核验剔除。
- Box7.1新增10个可核验候选全部保留；另7个非预测答案由原抽取代码排除，不属于234→225的9项差额。
- 234个resolvable全部独立判定：原5项与Box另4项的ASSESS语义去重全部撤销。详见audit/assessment_exclusion_rework_9.jsonl及中文表。
- 保留此前原164项结论；本轮只修改上述9项，其余291个ASSESS实质字段不变。语义近似的预测不代表统计独立性。
- 原阶段5条第三轮自适应主题为外资份额、制造品逆差、岗位、2015金砖GDP、FDI行业占比，原因是两轮缺数字；本轮仅为独立Box231补第二轮2条查询，无新增第三轮。
- 使用指定exa-new-3.key路径读取，未输出密钥。
