# 埃比尼泽·霍华德《明日的田园城市》（Ebenezer Howard, Garden Cities of To-Morrow）：出版后预测人工核查

- 案例目录：`cases/howard-garden-cities-of-to-morrow-v5/`
- 出版日期：**1902** 年由伦敦 Swan Sonnenschein & Co., Ltd. 出版，是 1898 年 *To-Morrow: A Peaceful Path to Real Reform* 的修订第二版。正文用 `reading-library/2026-11-15-未来判断扩展100本/01-社会/009-garden-cities-of-to-morrow.txt`，与 Project Gutenberg #46134 的 `ebooks/46134.txt.utf-8` 及 `cache/epub/46134/pg46134.txt` 逐字节一致（292,092 字节，sha256 `f1104aedd82d3f27a363a1ac98cbb68169826b1a2c98f16d7f7097eacd67248b`），与队列记录完全吻合；CRLF 原样使用，未转换。TXT 不入库。书中对 1902 年及以前的陈述按史实处理，预测窗口按 1902→2026-11-15 计。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

本稿按 METHOD.md 复刻 DeepSeek 流水线，只把模型调用换成助手人工阅读。抽取：用仓库 prepare_book v5（toolkit 来自 main `85e6da1`，prepare_book.py md5 `01fc49ad64795a345ca1cb32bb2e4366`）把全文切成 84 块（3500 字符、600 字符上下文），助手逐块通读（含前后附文块），按 DISCOVER_PROMPT_V5 写出模型本应返回的 JSON（可为空），再由仓库代码完成引文对齐、非预测筛除、归属降级和去重，得到 21 条候选、全部为可核验预测（resolvable）。英文 `changes` 均为 quote 的逐字子串（必要时保留原文 CRLF，避免跨行空格导致降级）。核验：每条可核验候选先定 scope，用 Exa 各做一次 support/counter 检索，只从检索返回的 URL 中选源，优先独立第三方（Historic England、英国议会、ONS/GLA、TCPA、学术论文与官方统计），存档到 `data/sources/`（sha256），写入 `data/evidence.jsonl`（44 条），再经 `pipeline.py apply assess → check → report`。本稿由助手逐条对照书中原文与存档证据人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 21 条，剔除非预测 0 条，计入 **21 条预测**，其中 **20 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 5 |
| 趋势符合 | 0 |
| 部分符合 | 10 |
| 错误 | 5 |
| 暂无法判断 | 1 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **25.0%**（5/20） |
| 加权胜率 | **50.0%** |
| 错误率 | **25.0%**（5/20） |
| 未定占比（暂无法判断/预测） | 4.8%（1/21） |

## 总体评价

这是一本 1902 年的城市规划宣言（1898 年《明日》的修订第二版），主体大量是田园城市方案的规范设计与财务估算，真正针对出版后世界的可核验预测集中在导论的磁体命题与第十一至十三章（社会城市、伦敦的未来）。21 条可核验预测中 20 条可判定、1 条暂无法判断：5 条正确，0 条趋势符合，10 条部分符合，5 条错误。正确项是第一座田园城市之后确有许多座花园郊区与英国新镇（32 座）继起；20 世纪市政与公共行动范围大幅扩大；1902–1962 年技术与发明变化同样显著；首个实验后出现推广该方法的广泛国际与国内需求；英格兰农地长期趋于上涨。部分符合主要是方向出现但强度、形态或机制不足：人口外迁与伦敦中期减少并非持久扭转；社区地权只在新镇/信托中局部采用；卫星城项链并非原书几何簇群；议会授权迟到数十年；贫民窟被清除但原址多为市政住宅而非公园，住房拥挤缓解但并未普遍达到五六间；伦敦有大规模重建但并非比奥斯曼巴黎更彻底的整体重建，既得利益也未被几乎消除。错误集中在“解决问题/回到土地”、城市与伦敦地价和房租将大幅度下跌、以及贫民窟清除将无需立法而由地主自愿完成。对趋势符合从严：仅在存档证据确认方向持续且终点未到时才使用，本卷未使用该标签。严格胜率 25.0%，加权胜率 50.0%，错误率 25.0%。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（5 条）

- **#2** 「The construction of such a magnet, could it be effected, followed, as it would be, by the construction of many…」  
  判断：**正确**。条件已触发：莱奇沃思于1903年开工。此后韦林（1920）及大量花园郊区相继出现，1946年《新镇法》又启动英国历史上最庞大的新城计划之一，50年间建成32座新镇；国际上也出现多座田园城市。‘许多座将随之建造’这一主结果成立。  
  来源：<https://www.tcpa.org.uk/resources/explore-the-uks-new-towns/>；<https://en.wikipedia.org/wiki/New_towns_in_the_United_Kingdom>；<https://en.wikipedia.org/wiki/List_of_garden_cities>
- **#4** 「The area of municipal and corporate action is probably destined to become greatly enlarged」  
  判断：**正确**。英国公共开支占经济的比重由1900年前后约12–14%升至1960年代中期约40%，并在此后大体维持在这一量级；20世纪上半叶福利国家、市政事业与社会服务大幅扩张。即使1980年代私有化收回部分职能，公共行动范围仍远大于1902年。无时点的方向性判断在观察窗口内成立。  
  来源：<https://www.ukpublicspending.co.uk/past_spending>；<http://eprints.lse.ac.uk/108537/1/Piachaud_social_security_past_present_and_future.pdf>
- **#7** 「doubt that the next sixty years will reveal changes fully as remarkable?」  
  判断：**正确**。1902–1962年间出现了与此前六十年同等量级的变革：汽车普及、航空、无线电与电视、抗生素、原子能与核技术等，科学与技术史将其视为20世纪的重大技术转折。反方关于专利速率在1873年后下降的讨论，并不能否定该六十年内变化‘同样显著’。明示时窗内主结果成立。  
  来源：<https://en.wikipedia.org/wiki/20th_century_in_science>；<https://www.pbs.org/wgbh/aso/thenandnow/tech.html>
- **#8** 「Granted the success of the initial experiment, and there must inevitably arise a widespread demand for an exte…」  
  判断：**正确**。莱奇沃思虽在财务上起步艰难，但仍被看作有力示范。花园城市协会发展为全国性组织，1913–1926年国际花园城市与规划协会举办大会并向世界传播该理念，最终推动1946年《新镇法》。最初实验之后，推广该方法的广泛需求确实出现。  
  来源：<https://historicengland.org.uk/images-books/publications/english-garden-cities-introduction/english-garden-cities/>；<https://research.vu.nl/ws/files/42215264/chapter%202%20Garden%20cities%20to%20the%20world%201913-1920.pdf>
- **#13** 「the other a less marked tendency for agricultural land to rise.[29]」  
  判断：**正确**。尽管两次大战前后和1990年代初等时期农地价格有过回落，但长期序列显示英格兰农地价值在过去约一百年年均回报约5.7%，实际复合增长率接近2%。无时点的方向性判断（农地趋于上涨，且相对城市更弱）在窗口内成立。  
  来源：<https://www.savills.co.uk/landing-pages/rural-land-values.aspx>；<https://www.savills.co.uk/research_articles/229130/202022-0>

### 部分符合（10 条）

- **#1** 「the certainty of being able to live this life will be the magnet which will produce the effect for which we ar…」  
  判断：**部分符合**。第一座田园城市（莱奇沃思，1903）与韦林（1920）以及后来的英国新镇确从伦敦等地吸引了居民，Historic England也认为它们有力示范了开明开发。但20世纪英格兰城市化率仍从约77%升至89%，伦敦人口在1901–1939年继续增长，因此“人民从拥挤城市自发迁往城乡结合之地”并未成为主导流向，主结果只部分实现。  
  来源：<https://historicengland.org.uk/images-books/publications/english-garden-cities-introduction/english-garden-cities/>；<https://researchbriefings.files.parliament.uk/documents/RP99-111/RP99-111.pdf>；<https://en.wikipedia.org/wiki/History_of_London_(1900%E2%80%931939)>
- **#5** 「as men hasten to build up this and the other towns which must inevitably follow its construction, the migratio…」  
  判断：**部分符合**。新镇与‘伦敦外溢’政策确曾把部分人口从首都迁出：大伦敦人口由1939年约860万降至1991年约680万。但这并非出版后即被‘有效遏制’，1901–1939年伦敦仍在增长；1990年代以后人口回升，2015年已超过1939年峰值。流向并未被持久地‘正好扭转’到新城镇。子项与持续性均有实质差距。  
  来源：<https://trustforlondon.org.uk/data/topics/population/?tab=population-over-time>；<https://en.wikipedia.org/wiki/Demographics_of_London>；<https://en.wikipedia.org/wiki/London_overspill>
- **#6** 「it is proposed to purchase the necessary land with which to establish the system on a small scale, and to trus…」  
  判断：**部分符合**。莱奇沃思土地信托、新镇开发公司及土地增值回收等，确实局部沿用了社区持有土地、共享增值的做法；当代社区土地信托也仍在倡导这一原则。但英格兰土地治理至今仍以私有、个人化产权为主，该制度并未被逐渐采纳为普遍地权。示范有影响，普遍化未实现。  
  来源：<https://online.ucpress.edu/elementa/article/12/1/00085/202564/Land-commoning-in-deagrarianized-contexts>；<https://researchbriefings.files.parliament.uk/documents/SN06867/SN06867.pdf>；<https://www.tcpa.org.uk/wp-content/uploads/2021/11/NTGC-P2_LR.pdf>
- **#9** 「prepared the reader for the later development which must inevitably follow--the planning and building of town …」  
  判断：**部分符合**。阿伯克隆比《大伦敦规划》按环状绿带与卫星城‘项链’布置了多座新城，1946年后伦敦周围一批新镇落成，部分实现了以绿带分隔、围绕中心城的城镇簇群设想。但这并非霍华德图示中那种有市际铁路、统一大计划的几何‘社会城市’簇群，也未形成一座新的中心城。方向出现，形态与完整度有实质差距。  
  来源：<https://etheses.bham.ac.uk/id/eprint/12336/7/Goode2022PhD_Redacted.pdf>；<https://www.english-heritage.org.uk/visit/blue-plaques/sir-patrick-abercrombie/>；<https://oro.open.ac.uk/96228/1/OVERVIEW%20OF%20ENGLISH%20NEW%20TOWNS.pdf>
- **#10** 「when our first experiment has been brought to a successful issue, there will be no great difficulty in acquiri…」  
  判断：**部分符合**。1946年《新镇法》确实赋予政府划定新镇用地并由开发公司推进的法定权力，议会辩论也追溯至霍华德与花园城市实验。但距离莱奇沃思开工已四十余年，且中间经历两次世界大战与巴洛委员会等，早期花园城市公司本身长期缺乏强制购地权。权力最终获得，但‘不会有很大困难’明显过早、过易。  
  来源：<https://www.parliament.uk/about/living-heritage/transformingsociety/towncountry/towns/overview/newtowns/>；<https://hansard.parliament.uk/commons/1946-05-08/debates/c58019de-db33-4580-a8cb-053a44c80825/NewTownsBill>
- **#16** 「Slum property will sink to zero,」  
  判断：**部分符合**。1930年代至1970年代英格兰大规模清除贫民窟，维多利亚式贫民窟房东经济大体消失，贫民窟作为可高额榨取的房产类型不再是城市住房的主体。但这主要靠住房立法与公共住房，而非人口外逃使贫民窟租金‘降至零’；部分过度拥挤和劣质住房仍存。结果部分出现，机制与彻底程度有差距。  
  来源：<https://www.nuff.ox.ac.uk/Economics/History/Paper98/carter98.pdf>；<https://ueaeprints.uea.ac.uk/id/eprint/40440/1/Slum_clearance_20th_Century_British_History_Vol_21_no_4.pdf>
- **#17** 「Families which are now compelled to huddle together in one room will be able to rent five or six」  
  判断：**部分符合**。伦敦人均房间数在至少约一个世纪里总体上升，早年‘一间房挤一户’的普遍情形已大幅缓解，多数家庭住进多室住宅。但‘租得起五六间’并未普遍实现，2001–2011年人均房间数还一度下降，21世纪仍有家庭挤在单间或严重过挤住房中。拥挤缓解是事实，具体规模与普遍性未达到原文。  
  来源：<https://data.london.gov.uk/download/24rpx/27e10d40-bb04-4028-95a6-606bd13d7777/Housing-in-London-2017-report.pdf>；<https://www.independent.co.uk/news/uk/home-news/housing-flat-rent-overcrowding-family-b2641122.html>
- **#18** 「These wretched slums will be pulled down, and their sites occupied by parks, recreation grounds, and allotment…」  
  判断：**部分符合**。贫民窟确实被大量拆除，个别清除地块或周边被辟为花园、游憩场地（如Tabard Gardens、战后扩建的公园）。但主导再利用方式是兴建市政住宅与街区重建，而非把原址主要改为公园、游憩场地和分配菜园。拆除发生，用途与原文有实质差别。  
  来源：<https://www.thelondonarchives.org/your-research/boundary-estate>；<https://londongardenstrust.org/conservation/inventory/site-record/?ID=SOU094>；<https://www.thelondonarchives.org/your-research/lcc-housing-records>
- **#20** 「The time for the complete reconstruction of London--which will eventually take place on a far more comprehensi…」  
  判断：**部分符合**。伦敦在Blitz之后经历了阿伯克隆比规划、大规模重建、码头区改造等重大更新，尺度不可谓不大。但史料与评论均指出，伦敦从未像奥斯曼巴黎或维也纳环形大道那样按统一秩序被‘彻底’重建，建筑遗产是多时期拼贴，战后规划本身也常被描述为碎片化。重建发生，但‘彻底’且‘远大于巴黎等地’的比较尺度未达到。  
  来源：<https://www.economist.com/interactive/britain/2023/08/24/how-the-blitz-changed-london-for-the-better>；<https://www.tandfonline.com/doi/full/10.1080/02665433.2023.2200400>；<https://en.wikipedia.org/wiki/Architecture_of_London>
- **#21** 「These tasks done, and done well, the reconstruction of London must inevitably follow, and the power of vested …」  
  判断：**部分符合**。田园城市与伦敦外围新镇建成后，伦敦确实出现了战后重建规划；巴洛委员会、张伯伦与阿伯克隆比路线也借助花园城市/卫星城思想推动了政策转变。但既得开发利益并未‘几乎或完全’失去阻挡力：地方政府仍依赖私人开发商供房，规划常被描述为向私人产权转移价值的机制。顺序上有重建，利益消除这一支不成立。  
  来源：<https://eprints.bbk.ac.uk/id/eprint/28411/3/28411.pdf>；<https://www.tandfonline.com/doi/full/10.1080/02665433.2023.2200400>；<https://doi.org/10.14324/111.9781800087088>

### 错误（5 条）

- **#3** 「would certainly afford a solution of the burning question set before us by Sir John Gorst, “how to back the ti…」  
  判断：**错误**。议会研究显示，20世纪英格兰城镇人口比重由约77%升至89%，农村人口外流在出版后很长时期仍在继续。1970年代以后虽出现有限的逆城市化，但并未构成对‘阻止人口涌入城镇、使人民回到土地’这一紧迫问题的解决。主结果相反。  
  来源：<https://researchbriefings.files.parliament.uk/documents/RP99-111/RP99-111.pdf>；<https://www.gov.uk/government/statistics/population-statistics-for-rural-england>
- **#12** 「The first will be a strong tendency for city ground values to fall,」  
  判断：**错误**。在1902–2026年的观察窗口内，英国与伦敦城市地价的长期趋势是大幅上涨而非强烈下跌。伦敦住宅用地价值居于英国和全球城市前列；即便利特周期和下跌，也不能把主结果说成‘强烈下跌趋势’。主结果相反。  
  来源：<https://www.london.gov.uk/sites/default/files/chapter4-economic-evidence-base-2016.pdf>；<http://news.bbc.co.uk/1/hi/business/2787695.stm>；<https://www.ons.gov.uk/aboutus/transparencyandgovernance/freedomofinformationfoi/houseandlandpricesfortheukfrom1900to2022>
- **#14** 「First, notice that ground values will fall enormously!」  
  判断：**错误**。伦敦地价并未因田园城市或新镇而‘大幅度下跌’。大伦敦经济证据显示，对土地的激烈竞争使伦敦地价和房价处于英国及全球城市最高之列；20世纪末至21世纪住宅用地价格还出现过成倍上涨。主结果相反。  
  来源：<https://www.london.gov.uk/sites/default/files/chapter4-economic-evidence-base-2016.pdf>；<http://news.bbc.co.uk/1/hi/business/2787695.stm>
- **#15** 「Obviously, house-property in London will fall in rental value, and fall enormously.」  
  判断：**错误**。即使伦敦人口曾在1939–1980年代下降，房屋财产的租金与售价在1902–2026年的长期趋势仍是大幅上升而非‘大幅度下跌’。2023年伦敦住房平均成交价约59万英镑，私人市场一居室平均租金远高于英格兰其他地区，负担危机持续。主结果相反。  
  来源：<https://trustforlondon.org.uk/data/rent-affordability/>；<https://www.london.gov.uk/sites/default/files/2024-11/London's%20Housing%20Stock%20-%20Research%20Unit%20-%20November%202024.pdf>；<https://centreforlondon.org/wp-content/uploads/2023/08/Centre-for-London-Homes-fit-for-Londoners-Londons-homes-today.pdf>
- **#19** 「Nor will, I think, the compulsion of any Act of Parliament be necessary to effect this result: it will probabl…」  
  判断：**错误**。贫民窟清除的主渠道是1875年以后一系列住房法、强制征购与规划立法（直至《住房法》《土地补偿法》中的清除程序），而非‘无需任何议会法案、由地主自愿完成’。虽有少数私人修缮案例，但不能代表主结果。机制预测不成立。  
  来源：<https://www.gov.uk/guidance/land-compensation-manual-section-9-slum-clearance-and-associated-procedures/slum-clearance-and-associated-procedures>；<https://ueaeprints.uea.ac.uk/id/eprint/40440/1/Slum_clearance_20th_Century_British_History_Vol_21_no_4.pdf>

### 暂无法判断（1 条）

- **#11** 「First, I say vested-property interests will be broken in twain, and will range themselves in opposite camps.」  
  判断：**暂无法判断**。检索可见花园城市运动内部围绕郊区化路线的分歧，以及后来绿带、新镇与开发利益之间的冲突，但未能找到足以判定‘既得财产利益被劈成农业地主与城市地主等对立阵营’这一具体政治分裂是否因该实验而出现的直接证据。缺一项关键事实，暂无法判断。  
  来源：—

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/howard-garden-cities-of-to-morrow-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/howard-garden-cities-of-to-morrow-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/howard-garden-cities-of-to-morrow-v5/audit/manual_review_2026-11-15.py`

## 说明

- 抽取密度（21 条可核验 / 84 块 ≈ 0.25）落在 METHOD 英文书参考区间（约 0.2–0.35）。本书大部分章节是田园城市的方案设计、财政估算与行政结构，不把方案内部的“将”当作对现实世界的预测；只收录作者对出版后可观察结果的断言（含有条件预测）。未为凑密度放宽标准。
- 前后附文人工排除记录：仓库 `matter_spans` 只识别中文“序/目录/参考文献”等标题，对英文 CONTENTS、INDEX、POSTSCRIPT 与 Gutenberg 许可无匹配，故 `excluded_matter_spans=[]`，须人工排除。
  - 前附文：字符偏移 0–3745（Gutenberg 头部与许可、START 标记、卷首 Transcriber's Note、签名摹本、1902 年扉页、CONTENTS、LIST OF ILLUSTRATIONS、半标题），主要落在 txt-00001 及 txt-00002 前部，未抽预测。
  - 正文自 INTRODUCTION 标题（offset 3746）起。导论是全书开篇论证（目录第 9 页），不是致谢性序言，纳入正文。正文含导论与第一至十三章，并包括 THE END 之后、INDEX 之前的第十三章脚注。
  - 后附文自 INDEX（offset 236437）起：索引；POSTSCRIPT（1898–1902 年本书接受情况与花园城市协会成立的事后叙述，按方法视为跋，不抽预测）；卷末 Transcriber's Note；Gutenberg 许可。主要落在 txt-00069 后部至 txt-00084。
  - txt-00002 为前附文与正文交界块，只对 INTRODUCTION 起的正文抽取（该段无预测）。txt-00069 为正文脚注与 INDEX 交界块，只对脚注抽取（无预测）。全部 21 条引文偏移均在正文区间内。
- 第 7 条“sixty years / the next sixty years”按 1902–1962 明示时窗判断。第 20 条 “eventually” 在截至 2026-11-15 的窗口内判断，不以仍可能发生的未来重建推迟结论。
- 第 11 条（既得财产利益将被劈成对立阵营）因缺少可直接判定该分裂是否因该实验而出现的存档证据，记暂无法判断。
- 第 2、3、5、8、10、12–18、21 条等以第一座田园城市/新镇建成或人口外迁为条件；条件已在不同程度上触发（莱奇沃思、韦林、32 座新镇、伦敦外溢），按条件已满足后的可观察结果判断。
- 出版前史实（1898 年《明日》出版、1891 年前后他人关于城市膨胀的评论等）未计入可判定预测。方案内部的财政估算与“设想中的田园城市将如何运转”不作为对现实世界的预测。
- 检索摘录均取自第三方存档页面；已扫描 `data/sources/` 与 `data/evidence.jsonl`，未见与原书连续 300 字符重合而需截断的情形。检索结果中出现的原书转载页（sacred-texts.com 等）未用作证据。
- 案例的 `context` 字段按协调者口径清空（`data/claims.jsonl` 与 `output/txt_import/claims_proposals.jsonl`）。
- 源文本 sha256 与队列完全一致：`f1104aedd82d3f27a363a1ac98cbb68169826b1a2c98f16d7f7097eacd67248b`（292,092 字节），取自 Project Gutenberg #46134 的 `ebooks/46134.txt.utf-8`（与 `cache/epub/46134/pg46134.txt` 逐字节相同），CRLF 原样使用，未转换。

