# 威廉·斯坦利·杰文斯《煤炭问题：关于国家进步与煤矿可能耗尽的探究》（The Coal Question; An Inquiry Concerning the Progress of the Nation, and the Probable Exhaustion of Our Coal-Mines）：出版后预测人工核查

- 案例目录：`cases/jevons-coal-question-v5/`
- 出版日期：初版1865年，本稿依据1866年修订第二版。正文取自自由基金会在线自由图书馆（Online Library of Liberty）PDF（sha256 `0f64ed7a…`，与队列记录一致），用 pdftotext 转为 TXT（sha256 `5076828c…`，504,056 字符）。观察窗口为1866年至2026-11-15。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

按 METHOD.md 执行。抽取：用仓库 prepare_book v5 流水线把全文（504,056 字符）切成146块（每块3500字符，带600字符上下文）。助手逐块通读，没有用关键词筛选，按 DISCOVER_PROMPT_V5 写出模型本应返回的 JSON，再由仓库代码完成引文对齐、归属降级、去重和导入：共80条候选，其中76条为可核验预测；4条转述他人（赫尔、珀西、波特）且作者未表态的观点被降为 unclear。序言（对全书结论的概述）、尾注和参考文献不另行计入预测。核验：每条先写 scope，各做一次 support 与 counter 的 Exa 检索，其中17条追加一轮自适应检索；只从检索返回的 URL 中选源。原文存档于 data/sources（124份，sha256），写入 data/evidence.jsonl（124条）。助手阅读后按“正确／趋势符合／部分符合／错误／暂无法判断”规则逐条评断，再经 pipeline.py apply assess → check → report。本稿由助手逐条对照书中原文与存档证据人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 76 条，剔除非预测 0 条，计入 **76 条预测**，其中 **72 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 38 |
| 趋势符合 | 5 |
| 部分符合 | 14 |
| 错误 | 15 |
| 暂无法判断 | 4 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **52.8%**（38/72） |
| 加权胜率 | **67.7%** |
| 错误率 | **20.8%**（15/72） |
| 未定占比（暂无法判断/预测） | 5.3%（4/76） |

## 总体评价

杰文斯对英国煤业本身的判断大多应验：产量增速放缓，1913年在2.87亿吨见顶，远低于按3.5%外推的数量；英国在煤远未采尽时就停止大规模产煤，2015年最后一座深井关闭；南斯塔福德郡铁业衰落，钢铁业重心移往美国，匹兹堡和俄亥俄河谷成为钢铁中心；1870—1913年出现大规模外移潮。判错的主要是能源替代和技术：他认为不会出现比煤更强的替代能源、石油只会加剧煤耗、空中运输永远不可行、英国永远不会进口煤，这些都被后来的历史否定；他还低估了美国工业化和德国出口的速度，误判贝塞麦钢价会保持高位、美国人口会在1900年前达到1亿、殖民地会放弃保护主义。部分符合的集中在“程度”上：煤价上涨主要源于劳动成本而非深井开采，增长率并非近乎不变，1913年产量约为成书时的3.1倍、刚到“三到四倍”的下限，自由贸易先倒退后才在欧共体内部实现。另有4条因条件或证据不足暂无法判断。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（38 条）

- **#4** 「It is thence simply inferred that we cannot long continue our present rate of progress.」  
  判断：**正确**。英国煤产量增速放缓，1913年在约2.9亿吨见顶，此后长期下降，指数增长确未能长期维持  
  来源：<https://ourworldindata.org/death-uk-coal>；<https://www.resilience.org/stories/2011-08-15/jevons-coal-question-why-uk-coal-peak-wasnt-bad-expected/>
- **#5** 「after a time we must either sink down into poverty, adopting wholly new habits, or else witness a constant ann…」  
  判断：**正确**。1870—1913年英国累计外移约1000万人、净外移近600万，年轻人持续大规模外移这一结果确实出现  
  来源：<https://ideas.repec.org/p/auu/hpaper/079.html>；<https://docs.iza.org/dp830.pdf>
- **#6** 「the ultimate results will be to render labour so abundant in the United States that our iron manufactures will…」  
  判断：**正确**。美国生铁产量于1890年超过英国；1870—1913年英国由钢铁业公认领先者跌为次于美德的生产国  
  来源：<https://doi.org/10.1016/s0016-0032(15)90629-4>；<https://www.cambridge.org/core/journals/comparative-studies-in-society-and-history/article/abs/progress-in-iron-and-steel-18701913/61F2F5DF5A59207B5E051A4EB94442BD>
- **#10** 「how mistaken is Mr. Hull, in supposing our production of coal to be limited to 100 millions」  
  判断：**正确**。英国煤产量约1870年超过1亿吨，1913年达2.87亿吨，远超赫尔设想的上限  
  来源：<https://thundersaidenergy.com/downloads/uk-coal-productivity-and-production-statistics-1700-to-2025/>；<https://www.historytoday.com/archive/british-miners-and-coal-industry-between-wars>
- **#11** 「the time is not remote when we shall have to encounter the disadvantages of increased cost of working and dimi…」  
  判断：**正确**。1914年前英国采煤劳动生产率呈下降趋势；研究指出两战之间英国矿井加深、成本相对新产区上升，正如杰文斯所料  
  来源：<https://www.cambridge.org/core/journals/journal-of-economic-history/article/abs/fifty-years-of-coalmining-productivity-the-record-of-the-british-coal-industry-before-1939/7F6684EEDF962B37660B7AE226D26763>；<https://seec.surrey.ac.uk/wp-content/uploads/2020/06/SEEDS83.pdf>
- **#12** 「long before complete exhaustion takes place, England will have ceased to be a coal-producing country on an ext…」  
  判断：**正确**。英国在煤远未采尽时就停止了大规模产煤：2015年产量降至900万吨的历史低点，最后一座深井凯林利同年关闭  
  来源：<https://assets.publishing.service.gov.uk/media/5a75bd5de5274a545822dda9/Coal_in_2015.pdf>；<http://www.theguardian.com/environment/2015/dec/18/kellingley-colliery-shabby-end-for-an-industry>
- **#17** 「when this time comes, the States of North America will still be working coal in the light of day」  
  判断：**正确**。美国长期以露天和浅层开采为主：2022年露天矿占美国煤产量63%，露天开采自1970年代起超过井工  
  来源：<https://www.eia.gov/energyexplained/coal/where-our-coal-comes-from.php>；<https://en.wikipedia.org/wiki/Coal_mining_in_the_United_States>
- **#19** 「that migration of the iron trade to the newer coal-fields which must soon take place」  
  判断：**正确**。1875—1886年南斯塔福德郡铁业衰落尤为严重，成为永久衰退的开端；克利夫兰等新产区则迅速扩张  
  来源：<https://doi.org/10.1201/9781351251341-15>；<https://www.gracesguide.co.uk/The_Basic_Industries_of_Great_Britain_by_Aberconway:_Chapter_XX>
- **#21** 「the use of steel, could Mr. Bessemer produce it sufficiently cheap, would occasion a third, and as far as we c…」  
  判断：**正确**。贝塞麦法等让钢变便宜后，低碳钢在1870年代以后迅速取代熟铁，用于钢轨、船舶、机器和建筑  
  来源：<https://hmsjournal.org/index.php/home/article/view/55>；<https://www.iom3.org/resource/industry-evolution-in-steel.html>
- **#22** 「half a century hence our chief ocean conveyances will be wholly by steam」  
  判断：**正确**。到1910年代，蒸汽船已主导远洋运输；1890—1950年蒸汽不定期货船最终把帆船逐出远程航线  
  来源：<https://doi.org/10.3828/liverpool/9781802078596.003.0006>；<https://www.rmg.co.uk/stories/ocean/sailing-ships-steam-power-how-industrial-revolution-changed-life-sea-forever>
- **#23** 「Sailing vessels will not be entirely discarded, but will occupy a subordinate rank, similar to that of canal b…」  
  判断：**正确**。20世纪初帆船仍承运木材、硝石等少数大宗货物，但已退居次要地位，与预测一致  
  来源：<https://quivis.uk/linklater/dum/sailvsteam/sailvsteam2.html>；<https://ttu-ir.tdl.org/collections/06bff410-d866-4790-b87c-fc2878a61a3e>
- **#24** 「Our world-wide communications will be improved in a degree now perhaps unthought of」  
  判断：**正确**。1866年起跨大西洋电缆投入使用，19世纪末全球电报网已连通各大洲，此后又有电话、无线电等，世界通讯得到巨大改进  
  来源：<https://www.cambridge.org/core/books/connecting-the-nineteenthcentury-world/12743072DEB4F98C126DF5E81895FA2F>；<https://cup.columbia.edu/book/wiring-the-world/9780231540261/>
- **#28** 「now our mechanical skill in construction is sufficiently advanced, it must come more and more into use」  
  判断：**正确**。液压动力随后被大量采用：伦敦液压动力公司1882—83年起建成覆盖全市的管网，曼彻斯特等城市也建了管网，多数一直运行到1960—70年代  
  来源：<https://en.wikipedia.org/wiki/Hydraulic_power_network>；<https://collection.sciencemuseumgroup.org.uk/people/ap28550/london-hydraulic-power-company>
- **#31** 「there is little doubt, too, that a century hence the steam-engine will be two or three-fold as efficient as at…」  
  判断：**正确**。1869年的估计是蒸汽机只利用燃料约10%的能量；1950—60年代超临界蒸汽发电机组热效率接近40%，一百年内效率至少提高两三倍  
  来源：<https://www.scientificamerican.com/article/andldquowasteandrdquo-and-andldquoe-1869-03-13/>；<https://visualizingenergy.org/maximum-efficiencies-of-engines-and-turbines-1700-2000/>
- **#37** 「such changes must be expected to continue with the growth of our population and consumption, until only the ri…」  
  判断：**正确**。1871—1901年英国谷物种植面积下降29%，永久牧场增加35%；1875—1905年谷物缩减、草地扩张  
  来源：<https://www.nber.org/system/files/working_papers/w32958/w32958.pdf>；<https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Agriculture/Acreage_and_Yields_of_British_Crops>
- **#38** 「as steam-power is more and more used upon a farm, the number of labourers will continue to decrease」  
  判断：**正确**。农业劳动者人数在1851年后持续下降，历次人口普查都有记录  
  来源：<https://doi.org/10.2307/2339663>；<https://www.nber.org/system/files/working_papers/w32958/w32958.pdf>
- **#43** 「we cannot long maintain our present rate of increase of consumption; that we can never advance to the higher」  
  判断：**正确**。英国煤产量1913年在2.87亿吨见顶，远低于按3.5%外推的数十亿吨，此后再未接近  
  来源：<https://www.historytoday.com/archive/british-miners-and-coal-industry-between-wars>；<https://www.resilience.org/stories/2011-08-15/jevons-coal-question-why-uk-coal-peak-wasnt-bad-expected/>
- **#44** 「the check to our progress must become perceptible within a century from the present time」  
  判断：**正确**。不到五十年煤业于1913年见顶，两战之间陷入衰退，英国工业相对优势明显受阻，在一百年内显现  
  来源：<https://seec.surrey.ac.uk/wp-content/uploads/2020/06/SEEDS83.pdf>；<https://www.historytoday.com/archive/british-miners-and-coal-industry-between-wars>
- **#49** 「no one can doubt that the extension of our commerce and the growth of continental industry will demand a conti…」  
  判断：**正确**。英国煤出口在19世纪末增速快于产量，1913年出口（含船用燃煤）达9400万吨的峰值  
  来源：<https://dspace.lboro.ac.uk/2134/13782>；<https://www.historytoday.com/archive/british-miners-and-coal-industry-between-wars>
- **#50** 「as long as Britain maintains her present commercial and maritime position, not only the continental and other …」  
  判断：**正确**。一战前英国（尤其南威尔士）蒸汽煤通过遍布全球的加煤站供应世界大部分蒸汽船和海军，前提“保持海上地位”在当时成立  
  来源：<https://pure.port.ac.uk/ws/files/3055929/Boyns_Gray_Welsh_coalMB_2015_09_25_cleaned_up_version_.pdf>；<https://ijnh.seahistory.org/when-dreams-confront-reality-replenishment-at-sea-in-the-era-of-coal/>
- **#51** 「it cannot be supposed the competition of their coal industry can proceed far, or prove permanent and formidabl…」  
  判断：**正确**。法国煤产量1913年约4000万吨，不到英国2.92亿吨的七分之一，以煤为基础的工业始终没有构成持久而可怕的竞争  
  来源：<https://fraser.stlouisfed.org/files/docs/publications/FRB/pages/1920-1924/25077_1920-1924.pdf>；<https://api.parliament.uk/historic-hansard/commons/1933/jun/20/production-international-comparison>
- **#52** 「it would be absurd to suppose that they can support any industry capable of seriously competing with ours」  
  判断：**正确**。比利时虽是早期工业国，但煤炭和工业规模有限，从未与英国构成严重竞争  
  来源：<https://researchportal.vub.be/nl/publications/belgian-ironworks-in-the-19th-century/>；<https://fraser.stlouisfed.org/files/docs/publications/FRB/pages/1920-1924/25077_1920-1924.pdf>
- **#57** 「Of the greatly increased supplies of iron required in the future general progress of nations, we shall continu…」  
  判断：**正确**。19世纪中叶起英国是世界钢铁主要供应者，此后数十年出口持续增长，直到1913年才被德国超过  
  来源：<https://www.cambridge.org/core/journals/journal-of-economic-history/article/abs/international-competition-in-iron-and-steel-18501913/42E54B8BF3859143369F316381F4DE92>；<https://en.wikipedia.org/wiki/History_of_the_steel_industry_(1850%E2%80%931970)>
- **#58** 「And the result must be a new migration of our great trade.」  
  判断：**正确**。钢铁业的世界重心随后移出英国：英国在世界生铁产量中的份额1875年为47%，1913年降至约13%  
  来源：<https://en.wikipedia.org/wiki/History_of_the_steel_industry_(1850%E2%80%931970)>；<https://www.cambridge.org/core/journals/comparative-studies-in-society-and-history/article/abs/progress-in-iron-and-steel-18701913/61F2F5DF5A59207B5E051A4EB94442BD>
- **#59** 「It is impossible there should be two opinions as to the future seat of the iron trade.」  
  判断：**正确**。美国成为世界钢铁中心：1890年生铁产量超过英国，1901年组建的美国钢铁公司是当时世界最大的企业  
  来源：<https://doi.org/10.1016/s0016-0032(15)90629-4>；<https://billofrightsinstitute.org/essays/andrew-carnegie-and-the-creation-of-us-steel/>
- **#60** 「The first obstacle will disappear.」  
  判断：**正确**。煤矿与铁矿不在一处的障碍被克服：苏必利尔湖铁矿经五大湖和铁路大量运往克利夫兰、扬斯敦、匹兹堡  
  来源：<https://doi.org/10.1680/imotp.1899.18970>；<https://www.mikegravel.org/where-did-pittsburgh-get-its-iron-ore/>
- **#61** 「The high rate of wages in a new country like the States is a true and natural obstacle to the progress of a ma…」  
  判断：**正确**。美国虽然工资高，仍凭较高劳动生产率成为世界领先的制造国，高工资障碍被克服  
  来源：<https://www.nber.org/system/files/working_papers/w10364/w10364.pdf>；<https://khd.vse.cz/wp-content/uploads/page/351/04_Wright_Origins_of_American_Industrial_Success_1876-1940.pdf>
- **#62** 「and its development is a question only of time」  
  判断：**正确**。匹兹堡成为“钢城”：约1900年全美近一半的钢产自该地区  
  来源：<https://clui.org/projects/old-steel>；<https://www.pbs.org/wgbh/americanexperience/features/foster-pittsburgh-becomes-city-steel/>
- **#63** 「For many years to come our relations will remain of the same kind as at present. Europe will receive more and …」  
  判断：**正确**。此后数十年英国对欧洲出口的煤、铁持续增长，1913年英国煤出口的主要去向是法国、意大利、德国等欧洲国家  
  来源：<https://api.parliament.uk/historic-hansard/written-answers/1925/mar/11/british-coal-exports>；<https://dspace.lboro.ac.uk/2134/13782>
- **#64** 「Instead of extending across the seas an agricultural system in harmonious union, with our own manufacturing sy…」  
  判断：**正确**。英国（尤其威尔士）矿工把技术带到美国、加拿大、澳大利亚等地，当地煤铁工业兴起并与英国竞争  
  来源：<https://www.peoplescollection.wales/content/working-abroad-welsh-emigration>；<https://www.cambridge.org/core/journals/international-review-of-social-history/article/migration-and-ethnicity-in-coalfield-history-global-perspectives/12A2FB55688F2AE2C81BF6D324AE6C6D>
- **#65** 「nothing is more probable in political matters than that their population will grow both by internal multiplica…」  
  判断：**正确**。美国人口靠自然增长和移民持续增长：1880年代移民520多万，1900年代820多万  
  来源：<https://spartacus-educational.com/USAE1900.htm>；<https://www.census.gov/library/publications/2002/dec/censr-4.html>
- **#67** 「Within a century the choicest lands will have been taken up」  
  判断：**正确**。1890年人口普查宣布边疆已不复存在，在一个世纪内美国最好的土地已被占据  
  来源：<https://www.census.gov/dataviz/visualizations/001/>；<https://www.historians.org/resource/the-significance-of-the-frontier-in-american-history/>
- **#68** 「at last a sound system of metallurgical industry will grow up on the banks of the Ohio, capable of almost inde…」  
  判断：**正确**。俄亥俄河上游—莫农加希拉河谷形成了世界最大的钢铁产区之一，包括匹兹堡、惠灵、扬斯敦等地  
  来源：<https://en.wikipedia.org/wiki/Steel_Valley_(Pittsburgh)>；<https://www.phmc.state.pa.us/portal/communities/pa-suburbs/files/minesmillsmalls_dietrich.pdf>
- **#70** 「America will tend to supplant us in the European market for iron and other crude materials, and in all parts o…」  
  判断：**正确**。美国在1910年前后成为制成品净出口国，1890年代中期起钢铁出口激增，逐步在世界市场上取代英国  
  来源：<https://www.nber.org/papers/w7638>；<https://www.nytimes.com/1904/05/21/archives/america-will-be-in-lead-is-passing-great-britain-as-exporter-of.html>
- **#73** 「the Americans will hardly succeed in their apparent object of rendering their continent a self-contained Chine…」  
  判断：**正确**。美国虽有麦金利关税等高关税，却没有与欧洲贸易隔绝：1900年美国进出口规模巨大，对欧洲出口尤多  
  来源：<https://en.wikisource.org/wiki/Popular_Science_Monthly/Volume_58/April_1901/Foreign_Trade_of_the_United_States>；<https://history.house.gov/Historical-Highlights/1851-1900/The-McKinley-Tariff-of-1890/>
- **#74** 「in other parts of the world—Africa, Asia, and South America—there is sure to be a general and perhaps a very g…」  
  判断：**正确**。1870年代后铁路、轮船和电报把非洲、亚洲、南美纳入世界经济，英国对这些地区的贸易和投资大幅扩张  
  来源：<https://arrighinetwork.org/wp-content/uploads/2022/01/1999_arrighi_the-global-market.pdf>；<https://www.library.hbs.edu/working-knowledge/merchants-to-multinationals-british-trading-companies-in-the-nineteenth-and-twentieth-centuries>
- **#75** 「Our new industry and civilization had an obscure and unregarded commencement; it is great already, and will be…」  
  判断：**正确**。1870—1913年英国制造业年均增长约2.2%，衰退前确实变得更加强大  
  来源：<https://michaelkitson.org/wp-content/uploads/2013/03/kitson-and-michie-the-deindustrial-revolution-web.pdf>；<https://ideas.repec.org/p/wrk/warwec/423.html>
- **#76** 「But our name and race, our language, history, and literature, our love of freedom and our instincts of self-go…」  
  判断：**正确**。英语成为事实上的全球通用语，在贸易、学术、航空、科技等领域普遍使用  
  来源：<https://www.ucl.ac.uk/engage/case-studies/2022/mar/english-often-considered-de-facto-global-language>；<https://futureofenglish.britishcouncil.org/hubfs/Global%20-%20Future%20of%20English/eBook%20and%20Summary/FoE%20Summaries/FoE_Research%20Summary_revisedv4.pdf>

### 趋势符合（5 条）

- **#1** 「the high price demanded for coals drawn from some of the deepest pits indicates the high price that must in ti…」  
  判断：**趋势符合**。英国煤价确实走高：1856年坑口总值1666万英镑、产量6665万吨，折合每吨约5先令；1913年坑口均价约10先令10便士；一战后再未回到旧水平。但上涨主要来自劳动成本与工资，而非书中所说的深井开采，因此只算方向相符  
  来源：<https://archive.spectator.co.uk/article/19th-july-1919/2/the-price-of-coal-raised-at-the-pithead-was-sir>；<http://www.dmm.org.uk/books/ccci-026.htm>
- **#7** 「the crude iron manufacture will, in all probability, be our first loss」  
  判断：**趋势符合**。钢铁业是英国最早失去世界领先地位的大产业之一：1890年代被美德超越，1913年德国钢铁出口超过英国；但“最先失去的是生铁”这一排序难以严格证实  
  来源：<https://www.cambridge.org/core/journals/journal-of-economic-history/article/abs/international-competition-in-iron-and-steel-18501913/42E54B8BF3859143369F316381F4DE92>；<https://www.deirdremccloskey.com/docs/pdf/Article_11.pdf>
- **#13** 「Other nations, and especially the United States of America, which possess coal-fields thirty-seven times more …」  
  判断：**趋势符合**。战后英国煤出口萎缩，原因是航运改用石油、海外煤业兴起；美国自19世纪末起持续出口煤。方向相符，但美国把英国煤挤出“所有”市场没有直接证据  
  来源：<https://www.bbc.com/wales/history/sites/themes/society/industry_coal03.shtml>；<https://www.everycrsreport.com/reports/R43198.html>
- **#33** 「In a future age power may become the staple commodity of the Icelanders.」  
  判断：**趋势符合**。冰岛利用廉价的地热和水电大规模冶炼铝，铝锭实质上是“出口能源”；但渔业仍是主要出口，能源是否已是“主要商品”只能算方向相符  
  来源：<https://www.bloomberg.com/news/articles/2016-02-15/aluminum-island-offers-cheap-power-oasis-amid-commodities-tumble>；<https://www.statice.is/publications/news-archive/fisheries/export-value-of-icelandic-fisheries-in-2023/>
- **#35** 「So far then as our wealth and progress depend upon the superior command of coal we must not only stop—we must …」  
  判断：**趋势符合**。以煤为基础的英国优势确实停滞并倒退：煤产量1913年见顶后持续下降至几乎为零，英国在世界制造业中的份额由1870年的31.8%降至1913年的14%；但整体国民财富仍在增长  
  来源：<https://alanhoward.info/the-fall-of-british-coal>；<https://sourcebooks.fordham.edu/mod/indrevtabs1.asp>

### 部分符合（14 条）

- **#3** 「Nor will the economical use of coal reduce its consumption.」  
  判断：**部分符合**。19世纪英国蒸汽机效率提高的同时煤耗持续上升，“杰文斯悖论”由此得名；但现代研究认为反弹效应通常不足以完全抵消节约，英国后期也在效率提高与燃料替代下大幅减少用煤，普遍性存疑  
  来源：<https://en.wikipedia.org/wiki/Jevons_paradox>；<https://www.aceee.org/news/rebound-effect-real-not-very-large/>
- **#8** 「It must rise by degrees into the position of a great national and perhaps a party question, antithetical to th…」  
  判断：**部分符合**。全国性问题一侧应验：格莱斯顿受此书影响，1866年议会辩论并设皇家煤炭委员会；但煤炭问题没有成为与自由贸易对立的主要党派分界  
  来源：<https://api.parliament.uk/historic-hansard/commons/1866/jun/12/coal-motion-for-a-royal-commission>；<https://mathshistory.st-andrews.ac.uk/DSB/Jevons.pdf>
- **#9** 「it may proceed until the whole country is mainly dependent on one or two of the greatest coal basins」  
  判断：**部分符合**。1913年前产量分散于达勒姆/诺森伯兰、南威尔士、约克郡和中部、苏格兰等多个煤田；直到行业晚期才集中于约克—诺丁汉—德比煤田，1993—94年塞尔比一地约占英国深井产量的45%  
  来源：<https://lib-dh-app1.swan.ac.uk/getfile.php%3Ftype=site_documents&id=14%20Annual%20coal%20production%201882%20to%201948.pdf>；<https://en.wikipedia.org/wiki/Selby_Coalfield>
- **#15** 「Nor will the use of the coal-cutting machine much affect this question.」  
  判断：**部分符合**。截割机确实普及（机械截煤比例1913年8%、1937年57%），但没能扭转1914年前生产率下降和成本相对上升的趋势；“不会实质改变问题”大体成立，只是机械化对后期生产率有一定作用  
  来源：<http://www.dmm.org.uk/news19/9381217m.htm>；<https://www.cambridge.org/core/journals/journal-of-economic-history/article/abs/fifty-years-of-coalmining-productivity-the-record-of-the-british-coal-industry-before-1939/7F6684EEDF962B37660B7AE226D26763>
- **#16** 「Our industry will certainly last and grow until our mines are commonly sunk 2,000 or 3,000, or even 4,000 feet…」  
  判断：**部分符合**。英国工业与煤产量增长到1913年；1911年《不列颠百科全书》称曾被视为极限的4000英尺已被突破。但增长停止主要由于竞争和石油替代，并非普遍矿深达到2000—4000英尺  
  来源：<https://en.wikisource.org/wiki/Page:EB1911_-_Volume_06.djvu/611>；<https://ourworldindata.org/death-uk-coal>
- **#18** 「Yet it is certain that coal has been cheaper in the past than it can again be」  
  判断：**部分符合**。英国坑口煤价由1856年的每吨约5先令（总值÷产量）升至1913年的约10先令10便士，一战后更高，再未回到旧时低价；但能源长期价格研究显示，按实际价格计算煤价有起伏，后期大量廉价进口煤也让“永远更贵”难以全面成立  
  来源：<https://archive.spectator.co.uk/article/19th-july-1919/2/the-price-of-coal-raised-at-the-pithead-was-sir>；<http://www.dmm.org.uk/books/ccci-026.htm>；<https://www.lse.ac.uk/granthaminstitute/wp-content/uploads/2014/06/LREnergyPricesREEP2011.pdf>
- **#25** 「improvement of the air-engine will probably reduce the consumption to less than onethird of the present consum…」  
  判断：**部分符合**。现代斯特林热气机效率可达约40%，远高于1860年代蒸汽机，节能潜力在技术上成立；但热气机始终没有成为燃煤动力的主流，1920年代后被内燃机和电动机取代  
  来源：<https://www.nasa.gov/glenn/research/dynamic-thermal-energy-conversion/>；<https://www.steamengine.com.au/stirling/stirling-history>
- **#32** 「The progress of science, and the improvement in the arts, will tend to increase the supremacy of steam and coa…」  
  判断：**部分符合**。到20世纪中叶煤和蒸汽的地位确实更强，1860—1960年代煤提供了欧洲一半以上的能源；此后内燃机和油气取代了其霸主地位，只有蒸汽轮机在发电中仍占重要位置  
  来源：<https://stm.cairn.info/journal-journal-of-energy-history-2025-1-page-4?lang=en>；<https://technicshistory.com/2024/03/21/twilight-of-the-steam-age-part-1-internal-combustion/>
- **#34** 「the consumption of coal will increase at a nearly constant rate until some check, some natural but perhaps ela…」  
  判断：**部分符合**。煤产量持续增长到1913年后才遇阻，但增长率并非“近乎不变”：从成书时约9300万吨增至1913年的2.87亿吨，年均约2.4%，低于书中3.5%的速度并逐渐放慢  
  来源：<https://www.resilience.org/stories/2011-08-15/jevons-coal-question-why-uk-coal-peak-wasnt-bad-expected/>；<https://www.historytoday.com/archive/british-miners-and-coal-industry-between-wars>
- **#39** 「we observe a fall in the rate, probably temporary」  
  判断：**部分符合**。1864年后生铁产量增速回升，1872年达674万吨的高峰；但此后长期增长缓慢，1913年约1040万吨，增速放缓并非只是暂时  
  来源：<https://academic.oup.com/jrsssa/article-pdf/43/2/380/49666566/jrsssa_43_2_380.pdf>；<https://citizendium.org/wiki/Steel_industry,_history>
- **#45** 「the cost of fuel must rise, perhaps within a lifetime, to a rate injurious to our commercial and manufacturing…」  
  判断：**部分符合**。1900年前后英国出现煤价高涨的“煤荒”（1900年出口煤均价15.87先令），一战前生产率下降、成本上升削弱了竞争力；但到1913年英国煤仍主导世界海运煤贸易，燃料成本尚未直接摧毁其商业霸权  
  来源：<https://api.parliament.uk/historic-hansard/commons/1900/jul/27/national-coal-reserve>；<https://journals.sagepub.com/doi/10.1177/08438714231181754>
- **#46** 「Suppose our progress to be checked within half a century, yet by that time our consumption will probably be th…」  
  判断：**部分符合**。1913年产量2.87亿吨，约为成书时约9300万吨的3.1倍，刚到“三到四倍”的下限；但其中9400万吨用于出口，国内消费只有约2倍  
  来源：<https://www.historytoday.com/archive/british-miners-and-coal-industry-between-wars>；<https://www.resilience.org/stories/2011-08-15/jevons-coal-question-why-uk-coal-peak-wasnt-bad-expected/>
- **#48** 「Runcorn, supplied by direct lines from the South Lancashire field, will ship great amounts of coal ballast」  
  判断：**部分符合**。加斯顿码头确实把南兰开夏煤运往爱尔兰等地，但利物浦/朗科恩从未成为大规模压舱煤出口港，英国煤出口集中在加的夫和东北部  
  来源：<https://ariadne-portal.d4science.org/resource/6a5e264a72e99808b7f735eb35affdef8222ae5607fa9335d29687b5af3620c9>；<https://www.cardiffharbour.com/history/>
- **#71** 「But on the whole Free Trade is likely to extend itself on the Continent.」  
  判断：**部分符合**。短期内方向相反：1879年德国、1892年法国（梅利纳关税）先后回到保护主义；长期看，1957年后欧共体关税同盟让欧洲大陆内部实现自由贸易  
  来源：<https://siepr.stanford.edu/publications/working-paper/rise-german-protectionism-1870s-macroeconomic-perspective>；<https://european-union.europa.eu/principles-countries-history/history-eu/1960-69_en>

### 错误（15 条）

- **#2** 「there is no probability that when our coal is used up any more powerful substitute will be forthcoming」  
  判断：**错误**。后来出现了更强的替代能源：石油在1950年超过煤成为美国第一大能源，1940至1970年代工业国普遍由煤转向油气，英国煤在远未采尽时即被替代  
  来源：<https://www.eia.gov/TODAYINENERGY/detail.php?id=62444>；<https://utppublishing.com/doi/full/10.3138/cjh.ach.53.3.03>
- **#14** 「it must still be held very unlikely that coal will ever be got in this tract」  
  判断：**错误**。1890年利用英吉利海峡隧道旧钻孔在多佛附近发现煤，肯特煤田后来建成提尔曼斯通、斯诺当、贝特尚格等煤矿，开采至1980年代  
  来源：<https://en.wikipedia.org/wiki/Kent_Coalfield>；<https://www.kentminingmuseum.co.uk/kent-coalfields>
- **#26** 「an improvement in the engine, reducing the cost of fuel, will turn the balance in favour of coal-power, and it…」  
  判断：**错误**。蒸汽犁最盛时的1870年代末英格兰也只有约700套，从未普及；农业动力化后来靠内燃拖拉机实现  
  来源：<https://blog.scottishagriculturalimplementmakers.co.uk/mistress-and-master-ploughing-new-furrows-in-scottish-steam-ploughing-history/>；<https://www.bahs.org.uk/AGHR/REVIEWS/REVIEW_2245.html>
- **#27** 「Uncertainty will for ever render aërial conveyance a commercial impossibility.」  
  判断：**错误**。20世纪商业航空客货运规模巨大：1945年至1973年国际航空运输保持两位数增长  
  来源：<https://www.iata.org/en/about/history/history-growth-and-development/>；<https://www.airandspace.si.edu/explore/stories/early-commercial-aviation>
- **#29** 「To extend the use of petroleum, then, is only a new way of pushing the consumption of coal. It is more likely …」  
  判断：**错误**。石油最终成为煤的主要替代品：20世纪船舶、铁路、交通改用石油，1940至1970年代油气取代煤，减轻而非加剧了对煤的依赖  
  来源：<https://utppublishing.com/doi/full/10.3138/cjh.ach.53.3.03>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC7471716/>
- **#30** 「the power of coal will ever be superseded by anything better」  
  判断：**错误**。煤作为动力来源已被石油、天然气、核能和可再生能源大规模取代，英国燃煤发电已基本退出  
  来源：<https://www.eia.gov/TODAYINENERGY/detail.php?id=62444>；<https://ourworldindata.org/data-insights/coal-power-has-effectively-died-in-the-united-kingdom>
- **#41** 「Liverpool, which soon will be the greatest of all emporiums of trade」  
  判断：**错误**。利物浦始终没有成为世界最大港口：19世纪伦敦是世界最大港口，1899年伦敦港外贸货物逾900万吨，纽约后来居上  
  来源：<https://en.wikipedia.org/wiki/19th-century_London>；<https://erenow.org/common/history-of-the-port-of-london/6.php>
- **#47** 「While the export of coal is a vast and growing branch of our trade, a reversal of the trade, and a future retu…」  
  判断：**错误**。英国后来大量进口煤：2001年起进口量超过国内产量，2006年达峰  
  来源：<https://ourworldindata.org/death-uk-coal>；<https://assets.publishing.service.gov.uk/media/5a7eaff5e5274a2e87db144e/Annex_G.pdf>
- **#53** 「Prussia, by its somewhat inland position, as well as for other reasons, is also incapable of taking any consid…」  
  判断：**错误**。以普鲁士为核心的德国在世界贸易中占据可观份额：1913年德国钢铁出口超过英国，鲁尔煤大量出口  
  来源：<https://www.cambridge.org/core/journals/journal-of-economic-history/article/abs/international-competition-in-iron-and-steel-18501913/42E54B8BF3859143369F316381F4DE92>；<https://www.dhm.de/lemo/kapitel/kaiserreich/industrie>
- **#54** 「America has not and cannot for a long period reach that state of industrial development in which a great syste…」  
  判断：**错误**。美国1880年代中期即超过英国成为世界最大制造国，1900年拥有世界约一半制造能力，用时并不长  
  来源：<https://www.cfr.org/education/learn/reading/how-did-united-states-become-global-power>；<https://www.gilderlehrman.org/history-resources/essays/rise-industrial-america-1877-1900>
- **#55** 「It is, therefore, necessary to use, in the making of Bessemer steel, ores which are free from impurities, and …」  
  判断：**错误**。1879年吉尔克里斯特—托马斯碱性法解决了脱磷问题，贝塞麦钢价从每吨约40英镑跌到6—7英镑  
  来源：<http://ctlhs.co.uk/golden-jubilee/fifty-interesting-events/the-introduction-of-the-gilchrist-thomas-process-1879/>；<https://en.wikipedia.org/wiki/Bessemer_process>
- **#56** 「It is even possible that recourse will some day be had to the Wealden ores」  
  判断：**错误**。威尔德铁业约1760年后消亡，后来没有恢复开采当地铁矿石  
  来源：<https://en.wikipedia.org/wiki/Wealden_iron_industry>；<https://www.wealdeniron.org.uk/>
- **#66** 「the population of the States will number 100 millions of persons before the year 1900」  
  判断：**错误**。1900年人口普查美国人口为7621万，远未达到1亿（1915年前后才达到）  
  来源：<https://www.census.gov/programs-surveys/decennial-census/decade/decennial-facts.1900.html>；<https://en.wikipedia.org/wiki/1900_United_States_census>
- **#69** 「We shall neither buy corn from them, nor sell iron articles to them.」  
  判断：**错误**。1846年后英国成为国际小麦市场中心，美国是其主要的小麦来源之一；英国对美国的铁和钢轨出口一直持续到1880年代中期  
  来源：<https://doi.org/10.1163/2468-1733_shafr_sim040140361>；<https://economics.yale.edu/sites/default/files/iron_www.pdf>
- **#72** 「Our colonies after a brief experience may see through their mistaken and highly prejudicial views」  
  判断：**错误**。殖民地没有放弃保护主义：加拿大1879年推行“国家政策”关税，此后一直维持到二战；维多利亚州及联邦后的澳大利亚长期实行保护  
  来源：<https://thecanadianencyclopedia.ca/en/article/national-policy>；<https://en.wikipedia.org/wiki/History_of_tariffs_in_Australia>

### 暂无法判断（4 条）

- **#20** 「When the general depth of coal workings has increased to 2,000 feet, little or no coal will be sold for less t…」  
  判断：**暂无法判断**。条件是“矿井普遍深达2000英尺”，但存档资料无法证实这一条件何时成立；1913年坑口均价约10先令10便士只是旁证，无法判定条件句  
  来源：<https://archive.spectator.co.uk/article/19th-july-1919/2/the-price-of-coal-raised-at-the-pithead-was-sir>
- **#36** 「the rates of increase will probably not continue falling」  
  判断：**暂无法判断**。两轮检索和存档资料都没有提供可比的制造业城镇十年增长率序列，无法判定增长率是否停止下降  
  来源：<https://doc.ukdataservice.ac.uk/doc/7154/mrdoc/pdf/guide.pdf>
- **#40** 「it is possible that there are those now living who will see the end of the export of crude iron」  
  判断：**暂无法判断**。存档资料只说明英国商品生铁业后来衰亡，没有给出1866年在世者有生之年英国生铁出口终结的确切时间，无法判定  
  来源：<https://hmsjournal.org/index.php/home/article/view/448>
- **#42** 「before long this deplorable waste of coal must come to a natural end」  
  判断：**暂无法判断**。只找到副产炼焦炉利用碎煤、矸石山自燃延续等间接资料，无法确认矿口焚烧碎煤的浪费何时终止  
  来源：<https://www.maryporttowncouncil.gov.uk/local-attractions/maryport-coke-ovens-unique-listed-monument/>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/jevons-coal-question-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/jevons-coal-question-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/jevons-coal-question-v5/audit/manual_review_2026-11-15.py`
