# 诺曼·安吉尔《大幻觉》（The Great Illusion）：出版后预测人工核查

- 案例目录：`cases/angell-great-illusion-v5/`
- 出版日期：本书最早是 1909 年的小册子《欧洲的视觉幻象》，1910 年扩充为《大幻觉》初版，**1913 年**出修订第四版。所用正文为 Project Gutenberg #38535 的 1913 年修订版（G. P. Putnam's Sons，纽约／伦敦），TXT 的 sha256 为 `d389c7dc…`，与队列记录一致。按 1913 年起算，书中提到的 1911—1912 年事件（阿加迪尔危机、意土战争、巴尔干战争）视为已知历史。观察窗口为 1913 年至 2026-11-15。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

按 METHOD.md 执行。抽取：用仓库 prepare_book v5 流水线把全文（728,826 字符）切成 211 块（每块 3500 字符，带 600 字符上下文）。助手逐块通读，按 DISCOVER_PROMPT_V5 写出模型本应返回的 JSON，再由仓库代码完成引文对齐、归属降级、去重和导入：共 36 条候选，其中 30 条为可核验预测；另有 5 条被降为 unclear（3 条不可核验、2 条为未获作者认可的第三方观点），1 条历史陈述被排除。前言、索引和 Gutenberg 许可文本不产生预测。核验：每条先写 scope，各做一次 support 与 counter 的 Exa 检索，有 3 条追加一轮自适应检索，第 3 条在 2026-11-16 按规则 10 复核时又补做一轮 support/counter 检索；只从检索返回的 URL 中选源。原文存档于 data/sources（sha256），写入 data/evidence.jsonl（88 条）。助手阅读后按“正确／趋势符合／部分符合／错误／暂无法判断”规则逐条评断，再经 pipeline.py apply assess → check → report。本稿由助手逐条对照书中原文与存档证据人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 30 条，剔除非预测 0 条，计入 **30 条预测**，其中 **30 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 7 |
| 趋势符合 | 2 |
| 部分符合 | 13 |
| 错误 | 8 |
| 暂无法判断 | 0 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **23.3%**（7/30） |
| 加权胜率 | **50.0%** |
| 错误率 | **26.7%**（8/30） |
| 未定占比（暂无法判断/预测） | 0.0%（0/30） |

## 总体评价

《大幻觉》的核心论点是：在金融相互依存的现代世界，征服与战争在经济上徒劳。作者明确说过，正因为各国不明白这一点，战争“极有可能”发生。这一判断和“单靠军备竞赛只会走向战争，而战争解决不了问题，必须从头再来”都被 1914 年和 1939 年证实。普鲁士专制的终结、王室殖民地走向自治、奥斯曼帝国灭亡、国际合作超越国界等判断也都应验；“美国终将效仿英国银行体系”只部分成立（联储效仿了伦敦的承兑贴现机制，但英式稳健银行带来的公众信心直到 1933 年存款保险后才建立）。失误集中在近期乐观判断上：各国民主派“很快”联合反对军备、阶级凝聚力压倒民族性、德国军国主义被工商业吸收、德国人“永远不会见到战斗”、英国在海军竞赛中地位恶化、德国占领荷比时会对其财富秋毫无犯，均被事实否定。至于“战争越来越不划算”“人类远离冲突”“征服观念最终被抛弃”等长期判断，1945 年后的长和平与领土完整规范给出了部分支持，但途径是两次世界大战，而不是作者期待的观念改革。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（7 条）

- **#5** 「Not only is there an irresistible tendency for Crown Colonies to acquire the practical rights of self-governin…」  
  判断：**正确**。二战后英国王室殖民地纷纷取得自治乃至独立（如牙买加1962年独立），到1960年代中期英国的主要属地大多已经独立，“不可阻挡”的趋势得到印证  
  来源：<https://www.iwm.org.uk/history/cold-war/end-of-empire>；<https://link.springer.com/book/10.1007/978-1-349-26922-8>；<https://www.jamaicaglobalonline.com/history/>
- **#6** 「the one certain result of the whole thing is that immense burdens will be added in the shape of further taxati…」  
  判断：**正确**。1912—1913年欧洲军备急剧扩张：德国1913年通过新军事法和配套财政法（含国防特别税），法国1913年8月通过三年兵役法并筹措专项税收，相关国家确实在原有负担上再加军备税负  
  来源：<https://fr.wikisource.org/wiki/Les_Armemens_financiers_de_la_France_et_de_l%E2%80%99Allemagne>；<https://en.wikipedia.org/wiki/Law_of_Three_Years>；<https://archive.spectator.co.uk/article/22nd-february-1913/2/in-paris-on-monday-some-very-important-details-bec>
- **#20** 「Does anyone really believe that the situation will remain there, that the Democratic parties will continue to …」  
  判断：**正确**。1918年11月革命推翻德意志帝国，德皇退位；普鲁士三级选举制随之废除，1919年普鲁士按普选举行选举，1920年通过民主宪法，“现状不会维持下去”的判断得到印证  
  来源：<https://en.wikipedia.org/wiki/German_Revolution_of_1918%E2%80%931919>；<https://en.wikipedia.org/wiki/Prussian_three-class_franchise>；<https://en.wikipedia.org/wiki/1919_Prussian_state_election>
- **#23** 「What justification have we, therefore, for saying dogmatically that a tendency to co-operation, which has swep…」  
  判断：**正确**。跨越国界的合作持续扩展：国际组织从1909年的37个增至1980年的逾1000个，2017年约7653个；欧洲还形成了超国家的一体化，合作没有止步于国家边界  
  来源：<https://uia.org/sites/uia.org/files/misc_pdfs/stats/Historical_overview_of_number_of_international_organizations_by_type_1909-2013.pdf>；<https://assets.cambridge.org/97811070/77218/excerpt/9781107077218_excerpt.pdf>；<https://www.europarl.europa.eu/factsheets/en/sheet/1/the-european-union-a-brief-history>
- **#26** 「In attempting to find the solution of this question in terms of one party, you are attempting the impossible. …」  
  判断：**正确**。条件基本成立：英德陷入以军备为主的海军竞赛，这场竞赛是一战的诱因之一；1914年战争爆发，而战争没有解决德国问题，1939年再次爆发大战，“一切重新开始”  
  来源：<https://www.iwm.org.uk/history/first-world-war/outbreak/naval-arms-race>；<https://en.wikipedia.org/wiki/Anglo-German_naval_arms_race>；<https://www.iwm.org.uk/history/second-world-war/causes>
- **#28** 「I have always urged with emphasis that our ignorance on this matter makes war not only possible, but extremely…」  
  判断：**正确**。1914年7月危机后欧洲大战爆发；世界和平基金会等也指出，安吉尔从未说战争不可能，而是认为在普遍误解下战争很可能发生  
  来源：<https://www.iwm.org.uk/history/first-world-war/outbreak>；<https://worldpeacefoundation.org/blog/the-great-illusion-114-years-on/>；<https://nzhistory.govt.nz/war/first-world-war-overview/origins>
- **#30** 「His nation has lived by the sword and to-day he is dying by the sword, because the sword, the mere exercise of…」  
  判断：**正确**。1912—1913年巴尔干战争后奥斯曼帝国在欧洲几乎丧失全部领土，1922年11月1日苏丹制度被废除，奥斯曼帝国终结  
  来源：<https://en.wikipedia.org/wiki/Dissolution_of_the_Ottoman_Empire>；<https://en.wikipedia.org/wiki/Abolition_of_the_Ottoman_sultanate>；<https://en.wikipedia.org/wiki/First_Balkan_War>

### 趋势符合（2 条）

- **#10** 「rivals, including Germany, will be quietly walking off with the trade that _does_ matter, will be increasing t…」  
  判断：**趋势符合**。1914年以前德国在拉美等市场确实持续扩张，对英国贸易和银行业形成侵蚀，这一方向得到印证；但一战爆发后英国对德国在南美的商业展开打击，这一趋势随即中断  
  来源：<https://www.cambridge.org/core/journals/albion/article/abs/british-overseas-banking-in-latin-america-and-the-encroachment-of-german-competition-18871914/FE133351AB416AF9901F8EEAD84E69A3>；<https://ora.ox.ac.uk/objects/uuid:78f8ab7c-76ae-40f8-9d33-490927ea9273/files/s0r967467k>；<https://surface.syr.edu/hst_etd/3>
- **#22** 「More and more in international relationship is the purely economic motive--and the economic motive is only one…」  
  判断：**趋势符合**。一战后经济制裁被写入国联盟约第16条，成为和平时期的工具；1990年代以后制裁使用量激增，在全球生效的制裁从2020年的320项增至2025年的828项，经济手段替代或补充武力的趋势得到印证，但武力并没有被取代  
  来源：<https://yalebooks.yale.edu/2022/02/24/the-history-of-economic-sanctions-as-a-tool-of-war/>；<https://origins.osu.edu/article/economic-sanctions-history-trump-global>；<https://www.lebow.drexel.edu/news/economics-sanctions-spread-lebow-experts-chart-their-growth-assess-their-impact>

### 部分符合（13 条）

- **#2** 「It is facts of the nature of those I have instanced which constitute the real protection of the small State, a…」  
  判断：**部分符合**。1914年和1940年比利时、荷兰等小国照样遭到入侵，金融相互依存没有成为“真正的保护”；1945年后贸易与相互依存降低国家间冲突的实证证据较多，所说的机制有部分成立  
  来源：<https://warontherocks.com/disillusioned-by-the-great-illusion-the-outbreak-of-great-war/>；<https://www.nber.org/papers/w35078>；<https://journals.sagepub.com/doi/10.1177/0022343310385995>
- **#3** 「In the end the Americans will imitate it, or they will suffer from a hopeless disadvantage in their financial …」  
  判断：**部分符合**。按 WORKER_BRIEF 规则 10 严格复核（2026-11-16），由正确改为部分符合。效仿的一面成立：1907 年危机后美国认识到需要类似英格兰银行的中央银行，1913 年建立联储，沃伯格明确提出效仿伦敦城的承兑与贴现机制。但作者所说要效仿的是英国银行业靠稳健经营建立的公众信心（“心理储备”），这一点在窗口内长期没有实现：1920 年代美国银行仍把在途支票计作“虚构准备金”，1930 年秋起接连爆发银行恐慌，1920 年代至 1930 年代初数千家银行倒闭；1933 年设立联邦存款保险才恢复公众信心，靠的是政府担保而不是效仿英式银行经营。因此只算部分符合  
  来源：<https://cepr.org/voxeu/columns/lessons-financial-preparations-lead-first-world-war>；<https://www.federalreservehistory.org/essays/banking-panics-1930-31>；<https://guides.loc.gov/this-month-in-business-history/june/fdic-established>
- **#4** 「to show that less and less can war be made to pay; that all those forces of our world which daily gain in stre…」  
  判断：**部分符合**。两次世界大战给主要交战国都带来巨大的经济损失，战争总体上越来越不划算，这一方向基本成立；但Liberman等研究表明，纳粹德国对被占工业化经济的榨取在短期内确实能让征服“有利可图”，说战争越来越不可能有利可图并不完全成立  
  来源：<https://warwick.ac.uk/fac/soc/economics/staff/mharrison/public/ww1overview2005.pdf>；<https://www.timeshighereducation.com/books/vassals-can-be-good-for-you/162218.article>；<https://cepr.org/voxeu/columns/exploitation-and-destruction-nazi-occupied-europe>
- **#8** 「And Italy, whose statesmen have been faithful to all the old "axioms" (Heaven save the mark!) will discover it…」  
  判断：**部分符合**。利比亚殖民地长期是意大利的财政和军事负担，经济上没有带来真正的收益，这一点与预测一致；但意大利并没有“很快发现”并放弃，法西斯时期反而加大移民和投资，直到1943年才失去利比亚  
  来源：<https://aehnetwork.org/wp-content/uploads/2021/11/AEHN-WP-66.pdf>；<https://www.worldhistory.org/article/2722/italian-colonialism-in-libya/>；<https://unitesi.unive.it/retrieve/1f183485-f859-4748-b74a-22963479bd9b/D%27ANDREA_MICHELLEANNA_885595.pdf>
- **#9** 「It is not the result of any inherent necessity of either people; it is the result merely of that woeful confus…」  
  判断：**部分符合**。英德对抗最终确实结束，1945年后两国同在北约、成为盟友；但结束的路径是两次世界大战和德国战败，并不是作者设想的“治国思想上的混乱被澄清”  
  来源：<https://www.ghil.ac.uk/fileadmin/redaktion/dokumente/House_Publications/Birke_Britain_and_Germany_Historical_Patterns_of_a_Relationship.pdf>；<https://www.nato.int/en/about-us/nato-history/history-by-theme/my-country-and-nato/germany-and-nato>；<https://en.wikipedia.org/wiki/Germany%E2%80%93United_Kingdom_relations>
- **#11** 「the final result of the administrative work of Europe in the Near and Far East will be to make populations lik…」  
  判断：**部分符合**。小亚细亚最终由当地人自治（1923年土耳其共和国成立，《洛桑条约》承认其主权），这个结果实现了；但途径是击退欧洲的瓜分，而非欧洲“行政工作”的成果，近东其他地区还经历了英法委任统治  
  来源：<https://origins.osu.edu/watch/treaty-lausanne-and-end-ottoman-empire>；<https://pressbooks.palomar.edu/historyofthemiddleeast/chapter/chapter-twelve-the-middle-east-under-european-control-1923-1948/>；<https://www.open.edu/openlearn/society-politics-law/international-relations-exploring-territorial-divisions/content-section-4.1>
- **#12** 「Those struggles of ideas will be carried out, not between States, but between different groups in the same Sta…」  
  判断：**部分符合**。1945年后内战和跨国意识形态冲突确实成为武装冲突的主要形式；但20世纪上半叶最大的意识形态斗争（两次世界大战、冷战对峙）主要还是在国家之间展开，不完全符合  
  来源：<https://oxfordre.com/politics/display/10.1093/acrefore/9780190228637.001.0001/acrefore-9780190228637-e-312>；<https://www.columbia.edu/~aw2951/WavesIntro.pdf>；<https://assets.cambridge.org/97810092/24857/excerpt/9781009224857_excerpt.pdf>
- **#13** 「he is drifting away from conflict, from the use of physical force, and towards co-operation.」  
  判断：**部分符合**。1945年后大国之间长期没有战争，战争死亡率呈下降趋势；但20世纪是有记录以来最血腥的世纪（战争相关死亡约1.87亿），“远离冲突、走向合作”只在长期、部分意义上成立  
  来源：<https://ourworldindata.org/war-and-peace-long-run>；<https://www.lrb.co.uk/the-paper/v24/n04/eric-hobsbawm/war-and-peace-in-the-20th-century>；<https://www.foreignaffairs.com/united-states/end-longest-peace>
- **#14** 「In the same way, as they become more familiar with the facts, the English will attenuate their hostility to "G…」  
  判断：**部分符合**。一战期间英国的反德情绪急剧恶化；直到二战后才逐步缓和，近年的民调显示多数英国人对德国持正面看法。最终方向与预测一致，但中间有数十年的反向发展  
  来源：<https://www.ourmigrationstory.org.uk/oms/germanophobia-and-germans-in-britain-in-the-early-twentieth-century>；<https://www.debrige.de/wp-content/uploads/2023/12/GermanySummaryReport.pdf>；<https://yougov.com/en-gb/articles/50803-who-do-britons-see-as-the-uks-allies-and-enemies>
- **#18** 「Spanish America seems at last in a fair way to throwing off the domination of the soldier and awakening from t…」  
  判断：**部分符合**。1930—1980年代拉美军事政变和军政府频繁出现，与“正在摆脱军人统治”的判断相反；不过到1993年中南美洲和西语加勒比地区已经没有军政府，长期看最终实现  
  来源：<https://faculty.chass.ncsu.edu/slatta/hi216/documents/dictatorships.pdf>；<https://journals.sagepub.com/doi/10.1177/0095327X9402000307>；<https://doi.org/10.2307/166175>
- **#21** 「especially as the charges in battle are getting very out of date, and are shortly to disappear from our warfar…」  
  判断：**部分符合**。一战西线的火力与堑壕使骑兵冲锋失去决定性作用，这一方向是对的；但步兵冲锋在一战中普遍存在，较大规模的骑兵冲锋一直持续到1942年，并没有“很快”消失  
  来源：<https://www.nam.ac.uk/explore/cavalry-western-front>；<https://www.history.com/articles/the-last-major-cavalry-charge-70-years-ago>；<https://www.warhistoryonline.com/world-war-i/cavalry-world-war-one.html>
- **#24** 「a tendency which has broken down profound national divisions, like those which separated the Celt and the Saxo…」  
  判断：**部分符合**。法德和解与欧洲一体化表明部分国家间的隔阂确实被打破；但民族主义在全球范围内持续存在，21世纪还出现了新的高涨，国家间心理隔阂并没有“必将”消解  
  来源：<https://www.tandfonline.com/doi/full/10.1080/17449057.2018.1532633>；<https://kclpure.kcl.ac.uk/portal/en/publications/global-nationalism-ideas-movements-and-dynamics-in-the-twenty-fir/>；<https://www.europarl.europa.eu/RegData/etudes/BRIE/2015/568359/EPRS_BRI%282015%29568359_EN.pdf>
- **#29** 「In like manner will the patriot come finally to see that better than _Dreadnoughts_ will be the recognition on…」  
  判断：**部分符合**。1945年后《联合国宪章》确立领土完整规范，武力兼并领土明显减少；但征服并未绝迹，2014年俄罗斯吞并克里米亚、2022年起占领乌克兰约20%领土，“最终认识到征服无利”只部分实现  
  来源：<https://library.fes.de/libalt/journals/swetsfulltext/10676368.pdf>；<https://dan-altman.weebly.com/uploads/3/2/3/1/32312379/evolution_of_conquest.pdf>；<https://www.foreignaffairs.com/ukraine/russias-costly-conquest-ukraine>

### 错误（8 条）

- **#1** 「if Germany conquered Holland or Belgium to-morrow, she would have to leave their wealth untouched; there could…」  
  判断：**错误**。条件已成立：德国1914—1918年占领比利时、1940—1945年占领荷比。占领期间德国征收战争税、征用物资，二战中被占欧洲向德国战争经济贡献约936亿帝国马克（含无偿掠夺和强迫劳动则约1182亿），远非“让其财富原封不动”  
  来源：<https://cepr.org/voxeu/columns/exploitation-and-destruction-nazi-occupied-europe>；<https://en.wikipedia.org/wiki/German_occupation_of_Belgium_during_World_War_I>；<https://api.parliament.uk/historic-hansard/commons/1944/feb/22/german-occupied-countries-money-payments>
- **#7** 「In a few years, as history goes, unless there is some complete change in tendencies, which at present seem as …」  
  判断：**错误**。两次大战之间法国低生育率趋势基本延续（1911—1938年人口只从约3960万增至约4190万），1931年外国人约270万、占人口7%，远谈不上被移民“淹没”、法兰西民族不复存在；二战后法国人口还大幅增长  
  来源：<https://www.histoire-immigration.fr/sites/default/files/2023-11/Textes_Parcours-permanent_MNHI_EN.pdf>；<https://www.persee.fr/doc/rhmc_0048-8003_1985_num_32_2_1318>；<https://shs.cairn.info/la-france-des-annees-30--9782200248895-page-5>；<https://www.ined.fr/en/all-about-population/data-graphs/fertility-france-total-fertility-rate-completed-fertility-and-age>
- **#15** 「From the realization of these things to the realization on the part of the British democrat that what stands i…」  
  判断：**错误**。这一步并没有“很快迈出”：1914年8月4日德法社会民主党议员一致投票支持战争拨款，第二国际的反战合作随之瓦解  
  来源：<https://isj.org.uk/the-great-schism-socialism-and-war-in-1914/>；<https://www.wsws.org/en/special/library/foundations-ger/04.html>；<https://onlinelibrary.wiley.com/doi/10.1111/j.1468-0130.2004.00287.x>
- **#16** 「so in like manner will the progress of political rationalism mark the evolution of the relationship of politic…」  
  判断：**错误**。争夺支配权的斗争并未停止：20世纪经历了两次世界大战和冷战，1945年后大国虽未直接交战，但大国竞争一直延续，近年还在加剧  
  来源：<https://ndupress.ndu.edu/Portals/68/Documents/Books/SA2020/SA-2020_Ch2.pdf?ver=8Vwnw6ygWN0NN9jzFtfY1g%3D%3D>；<https://en.wikipedia.org/wiki/Long_Peace>；<https://www.foreignaffairs.com/united-states/end-longest-peace>
- **#17** 「The immense majority of adult Germans--practically, all who make up what we know as Germany--have never seen a…」  
  判断：**错误**。一战中德国动员约1100万至1300万人，阵亡约200万；二战中约1800万人在国防军服役，战火也烧到德国本土。作者那一代德国成年男子大多亲历战场，“绝大多数永远不会见到战斗”的判断落空  
  来源：<https://www.loc.gov/collections/world-war-i-rotogravures/articles-and-essays/events-and-statistics/mobilized-strength-and-casualty-losses/>；<https://en.wikipedia.org/wiki/Wehrmacht>；<https://web.archive.org/web/20210418075408/https:/encyclopedia.1914-1918-online.net/article/war_losses_germany>
- **#19** 「far from allowing her military activities to absorb her industrial, it is precisely the military activities wh…」  
  判断：**错误**。德国军国主义并没有被工商业“吸收”：军方在帝国宪政中地位特殊、几乎不受国会约束，随后德国发动一战，纳粹时期又大规模重整军备；直到1945年战败后才出现根本转变  
  来源：<https://www.bpb.de/shop/zeitschriften/izpb/das-deutsche-kaiserreich-1871-1918-329/224753/autoritaerer-staat-und-demokratisierung-1890-1914/>；<https://www.cambridge.org/core/journals/central-european-history/article/world-of-enemies-new-perspectives-on-german-military-culture-and-the-origins-of-the-first-world-war/F46578E48DDC824833D6CDD375CADBAB>；<https://www.nsdoku.de/en/lexikon/artikel/aufruestung-der-reichswehrwehrmacht-46>
- **#25** 「We are, therefore, confronted with a coming condition of affairs in which the force of nationality will be dis…」  
  判断：**错误**。1914年战争爆发时，各国社会党纷纷支持本国政府，第二国际瓦解，民族性压倒阶级凝聚力，与预测相反  
  来源：<https://doi.org/10.1017/s0018246x14000454>；<https://isj.org.uk/the-great-schism-socialism-and-war-in-1914/>；<https://www.marxists.org/history/international/social-democracy/second-international-resolutions-book/ch10.htm>
- **#27** 「The longer it goes on, the worse will be England's relative position, because she has imposed on herself a pro…」  
  判断：**错误**。英国的相对地位并没有恶化：1912年后英国保持海上优势的决心使德国大海军派受挫，英国赢得了战前造舰竞赛，1914年8月英国大舰队有20艘无畏舰和超无畏舰，明显多于德国  
  来源：<https://www.bbc.co.uk/history/worldwars/wwone/war_sea_gallery_01.shtml>；<https://doi.org/10.1017/9781315248295.007>；<https://api.parliament.uk/historic-hansard/commons/1914/apr/22/british-and-german-fleets>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/angell-great-illusion-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/angell-great-illusion-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/angell-great-illusion-v5/audit/manual_review_2026-11-15.py`

## 说明

- 第 1、7、26 条是条件句，前提已成立（德国确实占领荷比、两次大战之间法国低生育率趋势延续、英德确实以军备竞赛为主），按结果判定。第 2、9、14 条的前提（相关事实被普遍认识、混乱被澄清）只部分出现，记为条件未知，结果按部分符合处理。
- 只有在存档证据明确证实方向时才给“趋势符合”（第 10、22 条）。
- 2026-11-16 按 WORKER_BRIEF 规则 10 严格复核：第 3 条（美国效仿英国银行体系）由正确改为部分符合，补检索并存档联储历史（1930—31 年银行恐慌）与国会图书馆（FDIC 设立）两份来源，替换原先只说明联储创设与美元崛起的两份来源；其余判定不变。
- 书中大量篇幅是论证和对他人观点的反驳，被反驳的观点和引述的第三方预测都不计入；这本书的预测密度（约 4.1 条／10 万字符）低于预测型著作。
- 统计以 pipeline.py report 的 summary.json 为准；本表的加权胜率按 manual_report.py 的权重计算（正确×1 + 趋势符合×0.75 + 部分符合×0.5）。

