# 联合国粮农组织（FAO）《全球森林部门展望2050：评估可持续经济的未来木材需求与来源》（Global Forest Sector Outlook 2050）：出版后预测人工核查

- 案例目录：`cases/fao-global-forest-sector-outlook-2050-v5/`
- 出版日期：**2022 年 12 月**，FAO 林业工作文件第 31 号（cc2265en）。所用正文为 FAO 开放知识库 PDF（openknowledge.fao.org/3/cc2265en/cc2265en.pdf），重新下载后 sha256 为 `8da09b0a…`，与书单记录逐字节一致；pdftotext 抽出 TXT 的 sha256 为 `e4e34360…`（286,680 字符）。书中 2020 年及以前的数据视为已知历史。观察窗口为 2022-12 至 2026-11-15。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

按 METHOD.md 执行。抽取：用仓库 prepare_book v5 流水线把全文（286,680 字符）切成 83 块（每块 3500 字符，带 600 字符上下文）。助手逐块通读，按 DISCOVER_PROMPT_V5 写出模型本应返回的 JSON，再由仓库代码完成引文对齐、归属降级、去重和导入：共 50 条候选，其中 34 条为可核验预测；16 条降为 unclear（12 条为书中转述、未获作者认可的第三方观点），另有 8 条（3 条历史陈述、1 条规范建议、4 条假设推演）被排除。核验：每条先写 scope，各做一次 support 与 counter 的 Exa 检索（68 次），其中 3 条追加一轮自适应检索（6 次）；只从检索返回的 URL 中选源。原文存档于 data/sources（sha256），写入 data/evidence.jsonl（45 条）。助手阅读后按“正确／趋势符合／部分符合／错误／暂无法判断”规则逐条评断，再经 pipeline.py apply assess → check → report。本稿由助手逐条对照书中原文与存档证据人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 34 条，剔除非预测 0 条，计入 **34 条预测**，其中 **21 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 10 |
| 趋势符合 | 4 |
| 部分符合 | 6 |
| 错误 | 1 |
| 暂无法判断 | 13 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **47.6%**（10/21） |
| 加权胜率 | **76.2%** |
| 错误率 | **4.8%**（1/21） |
| 未定占比（暂无法判断/预测） | 38.2%（13/34） |

## 总体评价

这是一份以全球森林产品模型（GFPM）为核心的情景展望，绝大多数量化结论以 2050 年为终点，截止日前无法检验，所以未定占比偏高（13/34）。可检验的部分主要是结构性、方向性判断，大多应验：林产工业投资流向巴西等新兴产区、热带天然林继续损失、热带人工林扩张、人造板增速领先、纸浆需求增长集中在亚洲、包装和生活用纸取代文化用纸成为主要驱动、中国继续依赖进口木材、天然林木材产量不再大幅增长。偏差在两处：一是“亚洲短缺将带动工业原木和初级产品贸易增长”，出版后全球工业原木贸易在 2023 年跌到 2009 年以来最低，中国进口也持续下降，判为错误；二是对增长速度普遍偏乐观，2020—2024 年全球初级加工木材产品消费基本持平，CLT、回收纸、欧美纸浆消费等判断只部分成立。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（10 条）

- **#8** 「it seems likely that forest industry investments will be made in these regions.」  
  判断：**正确**。出版后新兴/热带地区大型林产工业投资确实出现：Suzano在巴西塞拉多投资约43亿美元的纸浆线2024年投产；Arauco 2024年9月批准在巴西南马托格罗索州投资46亿美元建Sucuriú纸浆厂  
  来源：<https://www.suzano.com.br/en/news-post/suzano-starts-operation-of-the-worlds-largest-pulp-production-line>；<https://www.reuters.com/markets/commodities/copecs-arauco-approves-construction-46-bln-pulp-mill-brazil-2024-09-25/>；<https://www.fastmarkets.com/insights/suzano-cerrado-project-brazil-pulp-capacity-h2-24/>
- **#9** 「Wood fuel will remain the main energy source for many households in emerging economies.」  
  判断：**正确**。SDG7 2025年报告显示全球仍约21亿人依赖污染性炊事燃料（以薪柴、木炭等为主），撒哈拉以南非洲清洁炊事普及率很低；FAO数据中薪材产量2024年为19.49亿m³，较2020年仍增1%  
  来源：<https://unstats.un.org/sdgs/report/2025/goal-07/>；<https://trackingsdg7.esmap.org/sites/default/files/download-documents/Chapter2-SDG7-Report2025-0804-V11.pdf>；<https://www.fao.org/forestry/statistics/data/en/>
- **#12** 「Wood-based panels may see the strongest increase in future consumption (+102 percent for veneer/plywood and +7…」  
  判断：**正确**。该判断未给年份，按窗口检验相对增速。FAO数据：2024年人造板产量3.93亿m³，较2020年增8%，2023、2024年连续增长；同期锯材降8%、木浆增3%、纸和纸板增5%，人造板增幅最大  
  来源：<https://www.fao.org/forestry/statistics/data/en/>；<https://www.fao.org/newsroom/detail/global-forest-products-trade-and-production-show-signs-of-recovery-in-2024/en>；<https://www.fao.org/newsroom/detail/global-forest-products-facts-and-figures-2023-shows-fall-in-global-trade-in-wood-and-paper-products/en>
- **#13** 「The reliance on imported wood products is likely to continue due to the continued logging bans and poor produc…」  
  判断：**正确**。中国对进口木材的依赖延续：国家林草局刊文称2024年中国木材产量约1.37亿m³、消费量约2亿m³、进口约6284万m³，对外依存度约37%，“长期处于高位”；FAO数据显示2024年中国占全球工业原木进口37%、锯材进口23%  
  来源：<https://www.forestry.gov.cn/c/www/lcdt/670716.jhtml>；<https://www.fao.org/forestry/statistics/data/en/>
- **#20** 「The most important mid-term consumption drivers will be packaging materials and hygienic tissue in Asian, Euro…」  
  判断：**正确**。出版后纸浆需求结构与判断一致：Cepi称2023年欧洲文化用纸与包装、生活用纸的结构性分化仍在继续；FAO数据显示2023年全球文化用纸降9%至1987年以来最低，其他纸种只降3%；业内认为包装纸板和生活用纸市场将继续增长  
  来源：<https://www.cepi.org/wp-content/uploads/2024/02/Cepi-Preliminary-Statistics-report-2023.pdf>；<https://www.fao.org/newsroom/detail/global-forest-products-facts-and-figures-2023-shows-fall-in-global-trade-in-wood-and-paper-products/en>；<https://resource-recycling.com/recycling/2024/01/29/rising-packaging-and-tissue-markets-lift-fiber-prices/>
- **#21** 「The most significant market growth is expected to occur in the Asian sub-regions.」  
  判断：**正确**。纸浆市场增长集中在亚洲：Hawkins Wright指出中国占全球漂白化学浆需求的比重升至2023年的43%，其他地区需求下降；FAO数据显示2024年中国占全球纸浆进口41%、纸张消费34%  
  来源：<https://www.europulp.eu/wp-content/uploads/2024/09/Chinas-growing-impact-on-global-pulp-paper-markets-Hawkins-Wright.pdf>；<https://www.fao.org/forestry/statistics/data/en/>
- **#22** 「Forest area losses in naturally regenerated tropical and sub-tropical regions have been substantial and are ex…」  
  判断：**正确**。热带天然林损失持续：WRI/马里兰大学数据显示2023年热带原始林损失约370万公顷，2024年创纪录达约670万公顷  
  来源：<https://gfr.wri.org/global-tree-cover-loss-data-2024>；<https://www.wri.org/news/release-global-forest-loss-shatters-records-2024-fueled-massive-fires>；<https://gfr.wri.org/global-tree-cover-loss-data-2023>
- **#23** 「Small- and large-scale private sector interest and 200 million ha of FLR pledges suggest that this trend will …」  
  判断：**正确**。热带人工林扩张和工业原木供应增加的趋势延续：巴西人工林面积2024年首次超过1000万公顷（IBÁ）；FAO指出2024年新增纸浆供应主要来自巴西、智利、乌拉圭；FRA 2025显示全球人工林面积继续增加（增速放缓）  
  来源：<https://www.iba.org/wp-content/uploads/2025/05/relatorio2024.pdf>；<https://malinovski.com.br/relatorio-iba-aponta-para-mais-de-10-milhoes-de-ha-com-florestas-plantadas-no-brasil/>；<https://www.fao.org/newsroom/detail/global-forest-products-trade-and-production-show-signs-of-recovery-in-2024/en>；<https://openknowledge.fao.org/server/api/core/bitstreams/2dee6e93-1988-4659-aa89-30dd20b43b15/content/FRA-2025/key-findings.html>
- **#24** 「However, most IRW will be processed in the regions of production.」  
  判断：**正确**。FAO数据：2024年全球工业原木产量19.56亿m³，出口只有9300万m³（约5%），绝大部分在产地加工  
  来源：<https://www.fao.org/forestry/statistics/data/en/>；<https://www.fao.org/newsroom/detail/global-forest-products-trade-and-production-show-signs-of-recovery-in-2024/en>
- **#28** 「Given the actual trend towards conserving natural forests and the increasing market preference for plantation …」  
  判断：**正确**。ITTO《2023—2024年双年度评估》：ITTO生产国热带工业原木产量2023年为2.893亿m³，比上年略增，2024年预计持平；人工林采伐比重上升，天然林原木供应下降；2024年全球热带原木进口降至34年来最低。天然林木材生产没有大幅增长  
  来源：<https://www.itto.int/direct/topics/topics_pdf_download/topics_id=8063&no=1&disp=inline>；<https://www.itto.int/news/2025/10/20/itto_biennial_review_global_tropical_log_imports_hit_new_low_furniture_exports_lag/>

### 趋势符合（4 条）

- **#10** 「Economic development and population growth will further drive global material consumption.」  
  判断：**趋势符合**。UNEP国际资源委员会《全球资源展望2024》（2024年3月）指出，全球自然资源开采量在过去五十年翻了三倍，目前仍在上升，预计到2060年再增约60%；方向相符，但出版后年度消费增量没有单独数据  
  来源：<https://www.resourcepanel.org/news-events/global-resources-outlook-2024-press-release>；<https://www.unep.org/en/publications/report/global-resources-outlook-2024>
- **#15** 「Eastern Asia will expand its leading role, consuming 41 percent of the world´s primary processed wood products…」  
  判断：**趋势符合**。亚洲在全球消费中的份额继续上升：锯材从2023年的37%升至2024年的39%，人造板从58%升至59%，纸和纸板维持55%；统计口径为整个亚洲而非东亚，时间也短，只能算方向相符  
  来源：<https://cdn.forestresearch.gov.uk/2026/10/FS2026_Ch9.pdf>；<https://cdn.forestresearch.gov.uk/2025/09/FS2025_Ch9.pdf>
- **#16** 「Europe and Northern America will lose shares in global consumption」  
  判断：**趋势符合**。欧洲份额下降：锯材从2023年的26%降至2024年的25%，人造板从22%降至20%；北美及中美洲纸和纸板从19%降至18%，锯材和人造板持平。方向相符，但序列只有两年  
  来源：<https://cdn.forestresearch.gov.uk/2026/10/FS2026_Ch9.pdf>；<https://cdn.forestresearch.gov.uk/2025/09/FS2025_Ch9.pdf>
- **#29** 「The area of planted forests for timber production is expected to increase until 2050.」  
  判断：**趋势符合**。终点为2050年。FAO《全球森林资源评估2025》显示人工林面积继续增加（2025年约3.12亿公顷），但增速放缓，方向相符  
  来源：<https://openknowledge.fao.org/server/api/core/bitstreams/2dee6e93-1988-4659-aa89-30dd20b43b15/content/FRA-2025/key-findings.html>；<https://openknowledge.fao.org/server/api/core/bitstreams/2dee6e93-1988-4659-aa89-30dd20b43b15/content/FRA-2025/forest-characteristics.html>

### 部分符合（6 条）

- **#11** 「The products that are most likely to increase in market size are cross laminated timber and wood-based textile…」  
  判断：**部分符合**。木基纺织纤维（人造纤维素纤维）产量由2022年的740万吨增至2023年的790万吨，方向相符；但Graphfolio数据显示，2025年全球CLT表观消费量为181万m³，仍低于2021年205万m³的高点，CLT市场出版后没有扩大，只对一半  
  来源：<https://textileexchange.org/app/uploads/2024/09/Materials-Market-Report-2024.pdf>；<https://graphfolio.com/global/industrial-materials/wood-products/global-cross-laminated-timber-clt-and-x-lam-market>
- **#17** 「consumption looks different with substantially decreasing consumption volumes in Europe and Northern America」  
  判断：**部分符合**。欧洲大幅下降的方向相符：Cepi称2023年欧洲纸和纸板产量降13%，表观消费量降15.3%；但北美木浆消费2024年回升约13%（IndexBox，商业数据源），“持续大幅下降”只部分成立  
  来源：<https://www.cepi.org/wp-content/uploads/2024/07/Cepi-press-release_Final-2023-statistics_09072024-FINAL.pdf>；<https://www.cepi.org/wp-content/uploads/2024/02/Cepi-Preliminary-Statistics-report-2023.pdf>；<https://www.indexbox.io/blog/wood-pulp-northern-america-market-overview-2024-4/>
- **#18** 「Across all world regions, GFPM simulates the growing consumption of recycled paper」  
  判断：**部分符合**。全球回收纸产量2024年为2.41亿吨，较2020年增4%；但并非“所有地区”都在增长：欧洲2023年回收纸回收量下降逾100万吨，消费同步走弱  
  来源：<https://www.fao.org/forestry/statistics/data/en/>；<https://www.fao.org/newsroom/detail/global-forest-products-trade-and-production-show-signs-of-recovery-in-2024/en>；<https://www.euwid-recycling.com/news/business/european-recovered-paper-arisings-fall-by-more-than-one-million-tonnes-in-2023-170724/>
- **#27** 「the intensification of forest management in temperate and boreal forests is likely to be restricted by environ…」  
  判断：**部分符合**。欧盟《自然恢复条例》2024年生效，限制温带森林经营强化的方向成立；但欧盟《毁林条例》推迟，美国2025年3月行政令要求扩大木材生产，政策走向并不一致  
  来源：<https://eur-lex.europa.eu/eli/reg/2024/1991/oj/eng>；<https://www.reuters.com/business/environment/eu-finalises-12-month-delay-deforestation-law-2024-12-18/>；<https://www.whitehouse.gov/presidential-actions/2025/03/immediate-expansion-of-american-timber-production/>
- **#33** 「Publicly owned naturally regenerated forests, which are important sources of timber, will increasingly be mana…」  
  判断：**部分符合**。部分公有林转向碳汇和生物多样性管理：俄勒冈州2024年批准把Elliott州有林纳入碳市场，马萨诸塞州推行“森林作为气候方案”；但美国2025年行政令要求扩大联邦林地木材生产，方向不一致  
  来源：<https://www.salemreporter.com/2024/10/16/land-board-approves-precedent-setting-plan-to-put-elliott-state-forest-in-a-carbon-market/>；<https://www.mass.gov/news/healey-driscoll-administration-outlines-implementation-for-forests-as-climate-solutions-initiative>；<https://www.whitehouse.gov/presidential-actions/2025/03/immediate-expansion-of-american-timber-production/>
- **#34** 「the traditional use of fuelwood is expected to increase in sub-Saharan Africa and Southern Asia」  
  判断：**部分符合**。撒哈拉以南非洲缺乏清洁炊事的人口持续增加，2023年约9.6亿人，传统薪柴使用量上升，方向相符；但南亚的印度靠液化气推广，2022年清洁炊事普及率已达70%，预计无清洁炊事人口从2023年的4.3亿降至2030年的2.85亿，南亚部分不成立  
  来源：<https://www.iea.org/reports/sdg7-data-and-projections/access-to-clean-cooking>；<https://www.iea.org/reports/universal-access-to-clean-cooking-in-africa/executive-summary>；<https://trackingsdg7.esmap.org/sites/default/files/download-documents/Chapter2-SDG7-Report2025-0804-V11.pdf>

### 错误（1 条）

- **#4** 「IRW shortage in Asian sub-regions will induce increasing trade flows of industrial roundwood and primary proce…」  
  判断：**错误**。该判断未给年份，按出版至截止日窗口检验。亚洲短缺带动工业原木及初级产品贸易增长的方向未出现：2023年全球工业原木贸易降13%至1亿m³（2009年以来最低），2024年再降1%，出口比2020年低32%；中国占全球工业原木进口37%，其锯材进口2024年同比降4%；全球热带原木进口2024年降至34年来最低  
  来源：<https://www.fao.org/newsroom/detail/global-forest-products-facts-and-figures-2023-shows-fall-in-global-trade-in-wood-and-paper-products/en>；<https://www.fao.org/newsroom/detail/global-forest-products-trade-and-production-show-signs-of-recovery-in-2024/en>；<https://www.fao.org/forestry/statistics/data/en/>；<https://www.globalwoodmarketsinfo.com/chinas-lumber-market-in-2024-falling-softwood-imports-rising-hardwood-demand/>；<https://www.itto.int/news/2025/10/20/itto_biennial_review_global_tropical_log_imports_hit_new_low_furniture_exports_lag/>

### 暂无法判断（13 条）

- **#1** 「The GFPM outlook for a primary processed wood products consumption of 3.1 billion m³ roundwood equivalents (RW…」  
  判断：**暂无法判断**。终点为2050年。FAO数据显示2024年锯材产量较2020年降8%、人造板升8%、木浆升3%，2023年多数产品下滑、2024年回升，2020—2024年初级加工木材产品消费总体持平，看不出朝+37%增长的明确趋势  
  来源：<https://www.fao.org/forestry/statistics/data/en/>；<https://www.fao.org/newsroom/detail/global-forest-products-facts-and-figures-2023-shows-fall-in-global-trade-in-wood-and-paper-products/en>；<https://www.fao.org/newsroom/detail/global-forest-products-trade-and-production-show-signs-of-recovery-in-2024/en>
- **#2** 「the resulting industrial roundwood (IRW) demand may grow between 0.5 billion to 0.9 billion m³ by 2050 compare…」  
  判断：**暂无法判断**。终点为2050年。全球工业原木采伐量2023年降4%至19.2亿m³，2024年回升2%至19.56亿m³，比2020年仍低1%，截至截止日看不出增量趋势  
  来源：<https://www.fao.org/forestry/statistics/data/en/>；<https://www.fao.org/newsroom/detail/global-forest-products-facts-and-figures-2023-shows-fall-in-global-trade-in-wood-and-paper-products/en>；<https://www.fao.org/newsroom/detail/global-forest-products-trade-and-production-show-signs-of-recovery-in-2024/en>
- **#3** 「This study does not identify a global IRW supply gap to meet basic outlook demand in 2050.」  
  判断：**暂无法判断**。“2050年无全球工业原木供应缺口”是2050年的情景判断，截止日前无法检验  
  来源：<https://www.fao.org/forestry/statistics/data/en/>
- **#5** 「More restrictive policies for extractive forest use in the EU-27 would lead to a decrease of IRW production in…」  
  判断：**暂无法判断**。条件句。欧盟《自然恢复条例》（2024/1991）于2024年8月生效，但成员国恢复计划尚未落地，《毁林条例》还被推迟一年，“更严格的采伐限制”这一条件在截止日前没有明确触发，不判正确或错误  
  来源：<https://eur-lex.europa.eu/eli/reg/2024/1991/oj/eng>；<https://environment.ec.europa.eu/news/nature-restoration-law-enters-force-2024-08-15_en>；<https://www.reuters.com/business/environment/eu-finalises-12-month-delay-deforestation-law-2024-12-18/>
- **#6** 「Wood fuel sourcing in industrialized world regions that are predominately located in temperate and boreal zone…」  
  判断：**暂无法判断**。未找到工业化地区薪材来源向人工林和残余物转移的系统统计，无法判断  
  来源：<https://www.fao.org/forestry/statistics/data/en/>
- **#7** 「The medium estimate suggests 2050 employment being in the range of 2019 figures.」  
  判断：**暂无法判断**。终点为2050年。FAO 2024年按新方法估计森林部门就业约4200万人，口径与2019年不同，无法判断趋势  
  来源：<https://www.fao.org/newsroom/detail/new-research-provides-updated-estimates-on-global-forest-sector-employment/en>
- **#14** 「The GFPM simulations for 2050 indicate a strong increase in the consumption of primary processed wood products…」  
  判断：**暂无法判断**。预测期为2020—2040年。2020—2024年全球锯材降8%、人造板增8%、木浆增3%，合计大致持平，尚未出现“强劲增长”，但终点尚远，暂不判定  
  来源：<https://www.fao.org/forestry/statistics/data/en/>；<https://www.fao.org/newsroom/detail/global-forest-products-facts-and-figures-2023-shows-fall-in-global-trade-in-wood-and-paper-products/en>；<https://www.fao.org/newsroom/detail/global-forest-products-trade-and-production-show-signs-of-recovery-in-2024/en>
- **#19** 「The most substantial increase in urban housing requirements up to 2050 will occur in Southern Asia and sub-Sah…」  
  判断：**暂无法判断**。终点为2050年的城市住房需求，截止日前无法检验  
  来源：<https://www.un.org/en/desa/68-world-population-projected-live-urban-areas-2050-says-un>
- **#25** 「The growing number of large-scale wood industries and the ongoing modernization of forest industries in emergi…」  
  判断：**暂无法判断**。未找到新兴经济体木材加工残余物利用量的系统统计，无法判断  
  来源：<https://www.fao.org/forestry/statistics/data/en/>
- **#26** 「The forest area and growing stock trends in these regions suggest that IRW supply in Europe, Northern America …」  
  判断：**暂无法判断**。预测期为“未来几十年”。2024年欧洲占全球工业原木采伐30%，全球采伐增2%；但北美2023—2024年大量锯木厂因原料和价格问题关闭，各地区走势不一，时间太短，无法判断  
  来源：<https://cdn.forestresearch.gov.uk/2026/10/FS2026_Ch9.pdf>；<https://www.canfor.com/newsroom/2024-09-04/canfor-announces-closure-of-plateau-and-fort-st-john-sawmills-in-northern-bc>；<https://www.timberindustrynews.com/n-american-sawmill-capacity-dragged-down-by-low-demand-closures-and-shift-reductions/>
- **#30** 「Assuming that African countries comply with their stated policy commitments, the IEA simulation of 2019 (IEA, …」  
  判断：**暂无法判断**。条件句且终点为2050年（以非洲国家兑现政策承诺为条件），截止日前无法检验  
  来源：<https://www.iea.org/reports/africa-energy-outlook-2022/key-findings>
- **#31** 「In the sub-Saharan African context, the expansion of agricultural land driven by population growth will severe…」  
  判断：**暂无法判断**。未找到农业扩张导致撒哈拉以南非洲薪材供应严重受限的系统数据，无法判断  
  来源：<https://www.fao.org/in-action/dryland-sustainable-landscapes/news-and-events/news-detail/woodfuel-at-crossroads---sustainable-solutions-for-southern-africa/en>
- **#32** 「In combination with a population driven demand growth of around 83 million m³ ** by 2050, there will be a futu…」  
  判断：**暂无法判断**。终点为2050年的薪材供应缺口，截止日前无法检验  
  来源：<https://www.iea.org/reports/africa-energy-outlook-2022/key-findings>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/fao-global-forest-sector-outlook-2050-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/fao-global-forest-sector-outlook-2050-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/fao-global-forest-sector-outlook-2050-v5/audit/manual_review_2026-11-15.py`

## 说明

- 第 5、30 条是条件句：欧盟《自然恢复条例》2024 年已生效，但尚未转化为具体采伐限制，第 30 条以非洲各国兑现政策承诺为前提且终点为 2050 年，均记“暂无法判断”。
- 第 6、25、31 条没有找到可用的系统统计，按“证据不足”记“暂无法判断”。
- 第 15、16 条的区域份额只有 2023、2024 两年对比（Forestry Statistics 2025/2026 第 9 章），且统计口径是整个亚洲而非东亚，只记“趋势符合”。
- 第 17 条北美纸浆消费数据来自商业数据源 IndexBox，可信度低于官方统计。

