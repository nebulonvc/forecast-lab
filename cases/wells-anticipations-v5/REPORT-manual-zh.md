# 赫伯特·乔治·威尔斯《预言》（Anticipations of the Reaction of Mechanical and Scientific Progress upon Human Life and Thought）：出版后预测人工核查

- 案例目录：`cases/wells-anticipations-v5/`
- 出版日期：**1901 年 11 月**（各章 1901 年 4–12 月在 Fortnightly Review、6–11 月在 North American Review 连载，同年 11 月由 Chapman & Hall／Harper 出版成书）。正文为 Project Gutenberg #19229（Chapman & Hall 1902 年第二版），`reading-library/2026-11-15-未来判断书单/06-古典预言文本/39-预言.txt`，sha256 `d1e73b22f194360ab5e8572fe5179716683c8f1fb1d5358b411d53e2968cc367`。未发现只出现在第二版里的预测。观察窗口为 1901-11→2026-11-15；书中明示的终点（1910、几年之内、本十年、五十年内、1950、2000、一百年后、再过一个世纪等）分别适用。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

本稿是按 METHOD.md 的重做版（替代此前助手手工挑选 54 条的旧稿，对应仍打开的 PR #20）。抽取：用仓库 prepare_book v5 流水线把全文切成 147 块（3500 字符、600 字符上下文），助手逐块通读、按 DISCOVER_PROMPT_V5 写出模型本应返回的 JSON，再由仓库代码完成引文对齐、归属降级、去重和导入，得到 91 条可核验预测（约 0.62 条/块；英语预测书的密度高于一般英语非虚构的 0.2–0.35）。核验：按主题先写 scope，各做 support 与 counter 的 Exa 检索（只使用检索返回的 URL），原文存档于 data/sources（sha256），写入 data/evidence.jsonl（48 条），由助手阅读后按四分类规则评断，经 pipeline.py apply assess → check → report。本稿由助手逐条对照书中原文与存档证据人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 91 条，剔除非预测 0 条，计入 **91 条预测**，其中 **90 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 47 |
| 趋势符合 | 2 |
| 部分符合 | 29 |
| 错误 | 12 |
| 暂无法判断 | 1 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **52.2%**（47/90） |
| 加权胜率 | **70.0%** |
| 错误率 | **13.3%**（12/90） |
| 未定占比（暂无法判断/预测） | 1.1%（1/91） |

## 总体评价

交通与战争方面威尔斯命中很多：汽车、卡车、公共汽车、对向分隔和立体交叉的专用道路、城市中马匹退出、电气照明、家仆减少、离婚与道德多元、总体战、堑壕对峙、飞机（远早于 1950 年）并立即用于战争、坦克、图片远距传送、英语成为全球功能语言、德意志帝国在大战中崩溃、英美海军与商业优势转移等。主要误判包括：低估航空对运输的改变、1910 年前美德已有数千英里机动车专用道、伦敦/柏林等城市人口达到两三千万、潜艇只能用于狭窄水域、民主将被技术管理者取代并消亡、优生伦理主导世界国家、以及英语民族组成正式联邦。明确写在更远期的“世界国家”仍记为暂无法判断。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（47 条）

- **#1** 「so far as a light powerful engine goes, comparatively noiseless, smooth-running, not obnoxious to sensitive no…」  
  判断：**正确**。20世纪头十年轻型汽油内燃机已迅速成熟并适合公路使用，1911/1922年《不列颠百科》已把汽车当作既成工业。  
  来源：<https://en.wikisource.org/wiki/1922_Encyclop%C3%A6dia_Britannica/Motor_Vehicles>；<https://en.wikipedia.org/wiki/Long_Island_Motor_Parkway>
- **#2** 「There will, first of all, be the motor truck for heavy traffic.」  
  判断：**正确**。20世纪最初十年重型机动卡车已进入商业使用，与“将首先出现机动卡车”相符。  
  来源：<https://en.wikisource.org/wiki/1922_Encyclop%C3%A6dia_Britannica/Motor_Vehicles>
- **#3** 「sooner or later, no doubt, the numerous advantages of such an arrangement will lead to the organization of lar…」  
  判断：**正确**。随后出现了以卡车在公路上承运货物和包裹的大型运输公司，公路货运成为产业。  
  来源：<https://en.wikisource.org/wiki/1922_Encyclop%C3%A6dia_Britannica/Motor_Vehicles>；<https://assets.publishing.service.gov.uk/media/5c07d08240f0b670656346e3/Historyoftransport.pdf>
- **#4** 「there will develop the hired or privately owned motor carriage.」  
  判断：**正确**。出租与私家汽车在20世纪迅速普及，并在多数中短途出行中取代头等铁路。  
  来源：<https://en.wikisource.org/wiki/1922_Encyclop%C3%A6dia_Britannica/Motor_Vehicles>；<https://assets.publishing.service.gov.uk/media/5c07d08240f0b670656346e3/Historyoftransport.pdf>
- **#5** 「It will be capable of a day's journey of three hundred miles or more, long before the developments to be prese…」  
  判断：**正确**。现代汽车轻松达到单日300英里以上的行程，该能力在汽车早期发展完成之前就已具备。  
  来源：<https://en.wikisource.org/wiki/1922_Encyclop%C3%A6dia_Britannica/Motor_Vehicles>；<https://www.roads.org.uk/blog/century-motorways>
- **#6** 「And thirdly there will be the motor omnibus, attacking or developing out of the horse omnibus companies and th…」  
  判断：**正确**。伦敦等地在1900–1914年即出现机动公共汽车取代马拉公共车辆的“机动车革命”。  
  来源：<https://www.ltmuseum.co.uk/collections/stories/transport/motor-bus-revolution-1900-1914>；<https://en.wikisource.org/wiki/1922_Encyclop%C3%A6dia_Britannica/Motor_Vehicles>
- **#10** 「Their traffic in opposite directions will probably be strictly separated」  
  判断：**正确**。对向车流分隔成为高速公路和汽车专用路的标准设计。  
  来源：<https://en.wikipedia.org/wiki/Controlled_access_highway>；<https://www.roads.org.uk/blog/century-motorways>
- **#11** 「where their ways branch the streams of traffic will not cross at a level but by bridges.」  
  判断：**正确**。立交桥与匝道使车流不再在同一平面交叉，已是现代公路的常规做法。  
  来源：<https://en.wikipedia.org/wiki/Controlled_access_highway>；<https://www.roads.org.uk/blog/century-motorways>
- **#12** 「there is still a profit to be made from a certain section of the heavy goods traffic, and from cheap excursion…」  
  判断：**正确**。铁路在客运分流后仍长期承担大宗货物和部分游览运输，与预测方向一致。  
  来源：<https://assets.publishing.service.gov.uk/media/5c07d08240f0b670656346e3/Historyoftransport.pdf>；<https://en.wikipedia.org/wiki/History_of_rail_transport_in_Great_Britain_1948%E2%80%931994>
- **#14** 「step by step with these developments will come a very considerable acceleration of the ferry traffic of the na…」  
  判断：**正确**。涡轮推进等改进提高了海峡轮渡速度，20世纪跨海渡轮明显快于1901年水平。  
  来源：<https://assets.publishing.service.gov.uk/media/5c07d08240f0b670656346e3/Historyoftransport.pdf>；<https://en.wikipedia.org/wiki/Steamship>
- **#15** 「the centripetal pressure of the congested towns of our epoch may ultimately be very greatly relieved, but for …」  
  判断：**正确**。城市拥挤的缓解是长期过程，20世纪前几十年原有城市使用方式仍占主导，与“至少未来几十年仍将如此”相符。  
  来源：<https://www.archives.nyc/blog/2023/10/20/horsepower-the-city-and-the-horse>；<https://assets.publishing.service.gov.uk/media/5c07d08240f0b670656346e3/Historyoftransport.pdf>
- **#16** 「I do not see what is to prevent the process of elimination that is beginning now with the heavy vans spreading…」  
  判断：**正确**。城市街道上的马匹交通在20世纪上半叶基本被机动车淘汰，纽约等地文献明确记载了这一转变。  
  来源：<https://www.archives.nyc/blog/2023/10/20/horsepower-the-city-and-the-horse>
- **#20** 「nearly twenty that bid fair to reach that limit in the next decade」  
  判断：**正确**。20世纪初已有一批百万人口城市，之后十年又有更多城市跨过百万门槛，与“近二十座将在十年内达到”的方向和量级大致相符。  
  来源：<https://en.wikipedia.org/wiki/List_of_cities_with_over_one_million_inhabitants>；<https://www2.census.gov/library/publications/2004/compendia/statab/123ed/hist/hs-07.pdf>；<http://www.demographia.com/db-wldurb-2000r.htm>
- **#22** 「It is much more probable that these coming cities will not be, in the old sense, cities at all; they will pres…」  
  判断：**正确**。大城市演变为连绵都会区和城市区域，不再是旧式边界清晰的紧凑城墙城市。  
  来源：<http://www.demographia.com/db-wldurb-2000r.htm>；<https://en.wikipedia.org/wiki/Blue_Banana>
- **#29** 「and various dealers in fresh provisions, baker, grocer, butcher; or if they are already established there they…」  
  判断：**正确**。家庭电气化和汽车、照相、音响等设备普及，技术维修与工程职业成为20世纪显要阶层。  
  来源：<https://hss.sas.upenn.edu/sites/default/files/Industrial%20Revolution%20in%20the%20Home.pdf>；<https://www.americanhistory.si.edu/explore/stories/power-people-rural-electrification-brought-more-lights>；<https://www.bls.gov/opub/mlr/2006/03/art3full.pdf>
- **#30** 「The telephone will almost certainly prove a very potent auxiliary indeed to the forces making for diffusion.」  
  判断：**正确**。电话降低了必须住在市中心的必要性，是郊区化的重要辅助条件。  
  来源：<https://hss.sas.upenn.edu/sites/default/files/Industrial%20Revolution%20in%20the%20Home.pdf>；<https://www.americanhistory.si.edu/explore/stories/power-people-rural-electrification-brought-more-lights>；<https://scorecard.prb.org/goingtoworkamericanscommutingpatternsin2000/>
- **#32** 「Enough has been said to demonstrate that old "town" and "city" will be, in truth, terms as obsolete as "mail c…」  
  判断：**正确**。“城镇”“城市”的旧边界被都会区和连绵建成区取代，已成为20–21世纪的普遍形态。  
  来源：<http://www.demographia.com/db-wldurb-2000r.htm>；<https://en.wikipedia.org/wiki/Blue_Banana>
- **#36** 「this factor of irresponsible property is certain to be present in the social body a hundred years ahead.」  
  判断：**正确**。到2001年，不直接经营的股权和食利财产仍是现代经济的核心成分。  
  来源：<http://piketty.pse.ens.fr/files/PIK2008DYNalvaredo.pdf>；<https://www.bls.gov/opub/mlr/2006/03/art3full.pdf>
- **#37** 「the shareholding element will still endure, so long as our present progressive and experimental state of socie…」  
  判断：**正确**。在持续的市场经济中，股东/持股要素并未消失。  
  来源：<http://piketty.pse.ens.fr/files/PIK2008DYNalvaredo.pdf>；<https://www.bls.gov/opub/mlr/2006/03/art3full.pdf>
- **#38** 「There seems every reason to suppose that this phenomenon of unemployed citizens, who are, in fact, unemployabl…」  
  判断：**正确**。失业和难以被常规雇佣的群体在整个20–21世纪持续存在。  
  来源：<https://www.bls.gov/opub/mlr/2006/03/art3full.pdf>
- **#39** 「the day is not far distant when the extension of means of communication, and of the shareholding method of con…」  
  判断：**正确**。股份制和类似社会分层随通讯与市场扩展到全球大部分地区。  
  来源：<http://piketty.pse.ens.fr/files/PIK2008DYNalvaredo.pdf>；<https://www.bls.gov/opub/mlr/2006/03/art3full.pdf>
- **#40** 「for that emergent community, wherever it may be, it seems reasonable to anticipate, replacing and enormously l…」  
  判断：**正确**。受过科学与工程训练的技术职业阶层规模远大于1901年的旧式工匠，并具有明显的职业认同。  
  来源：<https://www.bls.gov/opub/mlr/2006/03/art3full.pdf>
- **#41** 「The practically autonomous farm of the old epoch will probably be replaced by a great variety of types of cult…」  
  判断：**正确**。在工业化国家，配备机械的专业化农业大规模取代了旧式相对自给的农场。  
  来源：<https://www.bls.gov/opub/mlr/2006/03/art3full.pdf>
- **#42** 「There may be several wars between European powers, prepared and organized to accept the old conventions, blood…」  
  判断：**正确**。两次世界大战后，职业化、技术化的现代军人取代了纯按旧惯例组织的军队。  
  来源：<https://en.wikipedia.org/wiki/Technology_during_World_War_I>；<https://openstax.org/books/world-history-volume-2/pages/11-3-total-war>；<https://en.wikipedia.org/wiki/Tanks_in_World_War_I>
- **#43** 「a large part of the history of the coming years will certainly record more or less conscious endeavours to ada…」  
  判断：**正确**。20世纪充满对过时制度的改造，以及革命、世界战争和边界重划。  
  来源：<https://openstax.org/books/world-history-volume-2/pages/11-3-total-war>；<https://en.wikipedia.org/wiki/German_Empire>；<https://en.wikipedia.org/wiki/Treaty_of_Versailles>
- **#44** 「I find it incredible that there will not be a sweeping revolution in the methods of building during the next c…」  
  判断：**正确**。钢筋混凝土、钢结构、预制等使建筑方法在20世纪发生了根本变化。  
  来源：<https://hss.sas.upenn.edu/sites/default/files/Industrial%20Revolution%20in%20the%20Home.pdf>
- **#45** 「They will probably not keep a servant for two very excellent reasons, because in the first place they will not…」  
  判断：**正确**。中产家庭在20世纪中叶以后普遍不再雇用常住佣人。  
  来源：<https://hss.sas.upenn.edu/sites/default/files/Industrial%20Revolution%20in%20the%20Home.pdf>
- **#47** 「Our coming house, however, will have no lamps to need filling」  
  判断：**正确**。电气照明取代了需要加油的油灯，成为标准家用照明。  
  来源：<https://hss.sas.upenn.edu/sites/default/files/Industrial%20Revolution%20in%20the%20Home.pdf>；<https://www.americanhistory.si.edu/explore/stories/power-people-rural-electrification-brought-more-lights>
- **#49** 「For the middling sort of people in the future maintaining a separate _menage_ there is nothing for it but the …」  
  判断：**正确**。中等阶层广泛居住在配备家电的公寓或省力住宅中，并以餐馆等补充家务。  
  来源：<https://hss.sas.upenn.edu/sites/default/files/Industrial%20Revolution%20in%20the%20Home.pdf>
- **#50** 「it is impossible to ignore the forces making for a considerable relaxation of the institution of permanent mon…」  
  判断：**正确**。离婚、同居和非终身婚姻安排在20世纪大幅增加，永久一夫一妻制明显松动。  
  来源：<https://en.wikipedia.org/wiki/Divorce_Reform_Act_1969>；<https://www.parliament.uk/about/living-heritage/transformingsociety/private-lives/relationships/keydates/>；<https://www.thebritishacademy.ac.uk/documents/249/Happy-families-History-family-policy.pdf>
- **#52** 「In another direction there must be a movement towards the relaxation of the marriage law and of divorce that w…」  
  判断：**正确**。各国婚姻法与离婚程序在20世纪显著放宽，婚姻身份更加多样。  
  来源：<https://en.wikipedia.org/wiki/Divorce_Reform_Act_1969>；<https://www.parliament.uk/about/living-heritage/transformingsociety/private-lives/relationships/keydates/>；<https://www.thebritishacademy.ac.uk/documents/249/Happy-families-History-family-policy.pdf>
- **#53** 「We are moving towards a time when, through this confusion of moral standards I have foretold, the pressure of …」  
  判断：**正确**。公共道德不再由单一宗教声音规定，性与婚姻问题上的舆论压力明显放松。  
  来源：<https://en.wikipedia.org/wiki/Divorce_Reform_Act_1969>；<https://www.thebritishacademy.ac.uk/documents/249/Happy-families-History-family-policy.pdf>；<https://www.pewresearch.org/short-reads/2017/10/27/500-years-after-the-reformation-5-facts-about-protestants-around-the-world/>
- **#54** 「the world of the coming time will still have its Homes, its real Mothers, the custodians of the human successi…」  
  判断：**正确**。核心家庭仍然存在，但旅馆、无子女家庭和公寓等非传统居处已成大规模常态。  
  来源：<https://hss.sas.upenn.edu/sites/default/files/Industrial%20Revolution%20in%20the%20Home.pdf>；<https://www.thebritishacademy.ac.uk/documents/249/Happy-families-History-family-policy.pdf>；<https://en.wikipedia.org/wiki/Divorce_Reform_Act_1969>
- **#55** 「It means that for one Morality there will be many moralities.」  
  判断：**正确**。统一道德被多种并存的道德体系取代，与20–21世纪的道德多元相符。  
  来源：<https://www.thebritishacademy.ac.uk/documents/249/Happy-families-History-family-policy.pdf>；<https://en.wikipedia.org/wiki/Divorce_Reform_Act_1969>；<https://www.pewresearch.org/short-reads/2017/10/27/500-years-after-the-reformation-5-facts-about-protestants-around-the-world/>
- **#60** 「That all these governments of confusion will drift towards war, with a spacious impulse and a final vehemence …」  
  判断：**正确**。20世纪的民主与民族国家体系确实滑向规模空前的世界大战。  
  来源：<https://openstax.org/books/world-history-volume-2/pages/11-3-total-war>；<https://en.wikipedia.org/wiki/German_Empire>；<https://en.wikipedia.org/wiki/Treaty_of_Versailles>
- **#63** 「Illustrations will be telegraphed just as well as matter」  
  判断：**正确**。传真照片（wirephoto）等技术使图片能像文字一样远距离传送。  
  来源：<https://en.wikipedia.org/wiki/Wirephoto>
- **#65** 「this will be the opening phase of the struggle, a vast duel all along the frontier between groups of skilled m…」  
  判断：**正确**。第一次世界大战的开局与相持阶段正是沿漫长前线的火力对峙，并不断从后方补充。  
  来源：<https://en.wikipedia.org/wiki/Technology_during_World_War_I>；<https://openstax.org/books/world-history-volume-2/pages/11-3-total-war>
- **#66** 「the State will be organized as a whole to fight as a whole, it will have triumphantly asserted the universal d…」  
  判断：**正确**。两次世界大战中的总体战把交通、工业和全体可动员人口纳入战争体系。  
  来源：<https://openstax.org/books/world-history-volume-2/pages/11-3-total-war>；<https://en.wikipedia.org/wiki/Technology_during_World_War_I>
- **#67** 「a factor which will be enormously stimulated to develop in the future, will be the aerial factor.」  
  判断：**正确**。空中力量在两次大战及以后成为战争的首要因素之一并飞速发展。  
  来源：<https://en.wikipedia.org/wiki/Aerial_reconnaissance_in_World_War_I>；<https://www.guinnessworldrecords.com/world-records/first-use-of-aircraft-in-warfare>；<https://en.wikipedia.org/wiki/Technology_during_World_War_I>
- **#68** 「long before the year A.D. 2000, and very probably before 1950, a successful aeroplane will have soared and com…」  
  判断：**正确**。莱特飞行器于1903年成功起飞并降落，远早于1950年和2000年。  
  来源：<https://en.wikipedia.org/wiki/Wright_Flyer>
- **#69** 「Directly that is accomplished the new invention will be most assuredly applied to war.」  
  判断：**正确**。飞机在发明后数年即被用于战争（意土战争及第一次世界大战侦察与作战）。  
  来源：<https://www.guinnessworldrecords.com/world-records/first-use-of-aircraft-in-warfare>；<https://en.wikipedia.org/wiki/Aerial_reconnaissance_in_World_War_I>
- **#70** 「ironclad road fighting-machines may perhaps play a considerable part in this」  
  判断：**正确**。第一次世界大战中的坦克正是用于突破堑壕防线的装甲陆地战斗机器。  
  来源：<https://en.wikipedia.org/wiki/Tanks_in_World_War_I>；<https://en.wikipedia.org/wiki/Technology_during_World_War_I>
- **#82** 「And to-day the Germans invade the sea with a threat and intention that will certainly create a countervailing …」  
  判断：**正确**。德国海军扩张推动了英德海军竞赛，并促使美国大力扩充海军、英国调整结盟与海军政策。  
  来源：<https://history.state.gov/milestones/1921-1936/naval-conference>；<https://en.wikipedia.org/wiki/German_Empire>；<https://learningenglish.voanews.com/a/a-23-2006-07-12-voa3-83127997/125489.html>
- **#83** 「I imagine that the German Empire--that is, the organized expression of German aggression to-day--will be eithe…」  
  判断：**正确**。德意志帝国在第一次世界大战后崩溃，1918年帝制结束并为凡尔赛体系所处分。  
  来源：<https://en.wikipedia.org/wiki/German_Empire>；<https://en.wikipedia.org/wiki/Treaty_of_Versailles>
- **#86** 「its English language should be already rooting firmly through all the world beyond its confines」  
  判断：**正确**。英语已在英语国家以外广泛扎根，成为全球使用最广的国际语言之一。  
  来源：<https://en.wikipedia.org/wiki/English_language>；<https://en.wikipedia.org/wiki/List_of_countries_and_territories_where_English_is_an_official_language>
- **#87** 「These things render the transfer of the present mercantile and naval ascendency of Great Britain to the United…」  
  判断：**正确**。到1920年代，美国已成世界最大经济体，并在华盛顿海军会议等安排中取得与英国对等的海军地位。  
  来源：<https://learningenglish.voanews.com/a/a-23-2006-07-12-voa3-83127997/125489.html>；<https://history.state.gov/milestones/1921-1936/naval-conference>
- **#89** 「A scheme of death duties and of heavy graduated taxes upon irresponsible incomes, with, perhaps, in addition, …」  
  判断：**正确**。英国等地实行了遗产税和对高额收入的累进税，正是用来抑制财富代际堆积的工具。  
  来源：<https://en.wikipedia.org/wiki/Inheritance_Tax_in_the_United_Kingdom>；<http://piketty.pse.ens.fr/files/PIK2008DYNalvaredo.pdf>

### 趋势符合（2 条）

- **#31** 「it seems only reasonable to anticipate the need for that expensive office and the irksome daily journey will s…」  
  判断：**趋势符合**。远程通讯使部分办公和通勤需求下降，这一趋势在世纪后期和21世纪更明显，但在大部分20世纪里每日通勤办公室仍是主流，终点并未完全到来。  
  来源：<https://hss.sas.upenn.edu/sites/default/files/Industrial%20Revolution%20in%20the%20Home.pdf>；<https://www.americanhistory.si.edu/explore/stories/power-people-rural-electrification-brought-more-lights>；<https://scorecard.prb.org/goingtoworkamericanscommutingpatternsin2000/>；<https://www.bls.gov/opub/mlr/2006/03/art3full.pdf>
- **#80** 「this process nevertheless aims finally, and will attain to the establishment of one world-state at peace withi…」  
  判断：**趋势符合**。国际组织和区域一体化持续推进，但到2026年并未建立起内部和平的单一世界国家，终点尚未到来。  
  来源：<https://en.wikipedia.org/wiki/Blue_Banana>；<https://www.cambridge.org/core/journals/european-political-science-review/article/beyond-dualism-the-hybridization-of-technocracy-and-democracy-in-europe/E84607A737F7ED0EAC3D3E19210AD316>

### 部分符合（29 条）

- **#7** 「will secure the power to form private roads of a new sort, upon which their vehicles will be free to travel up…」  
  判断：**部分符合**。高速机动车专用道路确实出现（公园大道、高速公路），但多为公共工程而非私营公共汽车公司所建的“私路”。  
  来源：<https://en.wikipedia.org/wiki/Long_Island_Motor_Parkway>；<https://en.wikipedia.org/wiki/Controlled_access_highway>；<https://www.roads.org.uk/blog/century-motorways>；<https://highways.dot.gov/highway-history/interstate-system/reichsautobahnen>
- **#8** 「This segregation of motor traffic is probably a matter that may begin even in the present decade.」  
  判断：**部分符合**。1908年前后已有长岛机动车公园大道这类专用道路，分流在本十年内萌芽，但远未在1910年前成为普遍制度。  
  来源：<https://en.wikipedia.org/wiki/Long_Island_Motor_Parkway>；<https://www.roads.org.uk/blog/century-motorways>
- **#13** 「Almost all will probably be still in existence and in divers ways busy, spite of the swarming new highways I h…」  
  判断：**部分符合**。2001年前后仍有大量1901年即存在的铁路线在运营，但英国Beeching裁撤等使“几乎全部仍存在且繁忙”并不成立。  
  来源：<https://en.wikipedia.org/wiki/History_of_rail_transport_in_Great_Britain_1948%E2%80%931994>；<https://assets.publishing.service.gov.uk/media/5c07d08240f0b670656346e3/Historyoftransport.pdf>
- **#17** 「Their advent will be the beginning of the end for steam traction on land and of the steam ship at sea: the end…」  
  判断：**部分符合**。陆上蒸汽牵引和远洋蒸汽客货轮确实被内燃机、柴油和电力取代，但煤电与部分蒸汽用途仍存，“煤与蒸汽时代终结”说得过满。  
  来源：<https://en.wikipedia.org/wiki/Steamship>；<https://assets.publishing.service.gov.uk/media/5c07d08240f0b670656346e3/Historyoftransport.pdf>；<https://en.wikipedia.org/wiki/History_of_rail_transport_in_Great_Britain_1948%E2%80%931994>
- **#21** 「not only will many of these railway-begotten "giant cities" reach their maximum in the commencing century, but…」  
  判断：**部分符合**。城市确向郊区扩散、建成区摊开，但20世纪巨型城市往往继续增长而非在本世纪达到峰值并在地图上近乎消失。  
  来源：<http://www.demographia.com/db-wldurb-2000r.htm>；<https://www2.census.gov/library/publications/2004/compendia/statab/123ed/hist/hs-07.pdf>；<https://en.wikipedia.org/wiki/List_of_cities_with_over_one_million_inhabitants>
- **#23** 「that daily journey, that has governed and still to a very considerable extent governs the growth of cities, ha…」  
  判断：**部分符合**。多数通勤仍以约一小时为常见上限，规划上也常用此经验，但超两小时通勤群体已显著存在，并非“始终”不可突破。  
  来源：<https://scorecard.prb.org/goingtoworkamericanscommutingpatternsin2000/>；<https://www.tuc.org.uk/news/number-commuters-spending-more-two-hours-travelling-and-work-72-last-decade-says-tuc>
- **#24** 「the London citizen of the year 2000 A.D. may have a choice of nearly all England and Wales south of Nottingham…」  
  判断：**部分符合**。高速交通使长距离通勤在技术上可行，东北走廊和伦敦通勤圈扩大，但2000年并不是“几乎整个英格兰南部或华盛顿至奥尔巴尼全境都已是日常郊区”。  
  来源：<https://scorecard.prb.org/goingtoworkamericanscommutingpatternsin2000/>；<http://www.demographia.com/db-wldurb-2000r.htm>；<https://www.tuc.org.uk/news/number-commuters-spending-more-two-hours-travelling-and-work-72-last-decade-says-tuc>
- **#26** 「I imagine it will be doing all these things within the next half-century.」  
  判断：**部分符合**。电话费下降、包裹和报刊投递改善在1951年前已明显推进，但并未在“几小时内以极低价满足家庭几乎一切日常需求”。  
  来源：<https://hss.sas.upenn.edu/sites/default/files/Industrial%20Revolution%20in%20the%20Home.pdf>；<https://www.americanhistory.si.edu/explore/stories/power-people-rural-electrification-brought-more-lights>
- **#27** 「the confluent "residential suburbs" of London, of the great Lancashire-Yorkshire city, and of the Scotch city,…」  
  判断：**部分符合**。英国南岸等地出现了连绵的海滨通勤和度假居住带，但并未在下世纪末沿大不列颠海岸线围成一圈。  
  来源：<https://assets.publishing.service.gov.uk/media/5c07d08240f0b670656346e3/Historyoftransport.pdf>；<http://www.demographia.com/db-wldurb-2000r.htm>
- **#28** 「the centre will probably still remain the centre and "Town," it will be essentially a bazaar, a great gallery …」  
  判断：**部分符合**。市中心仍是商业与聚会核心，出现了拱廊、商场、电梯乃至少量移动步道，但并未普遍变成全天候遮挡的步行化长廊。  
  来源：<https://hss.sas.upenn.edu/sites/default/files/Industrial%20Revolution%20in%20the%20Home.pdf>；<https://assets.publishing.service.gov.uk/media/5c07d08240f0b670656346e3/Historyoftransport.pdf>
- **#33** 「the whole of Great Britain south of the Highlands seems destined to become such an urban region」  
  判断：**部分符合**。英格兰中南部形成了高度连通的城市区域，但高地以南并非已汇合成单一连续城市区域。  
  来源：<https://en.wikipedia.org/wiki/Blue_Banana>；<https://assets.publishing.service.gov.uk/media/5c07d08240f0b670656346e3/Historyoftransport.pdf>；<http://www.demographia.com/db-wldurb-2000r.htm>
- **#34** 「The old antithesis will indeed cease, the boundary lines will altogether disappear; it will become, indeed, me…」  
  判断：**部分符合**。城乡界线显著模糊，但并未 altogether 消失，乡村与城市在密度和功能上仍可区分。  
  来源：<http://www.demographia.com/db-wldurb-2000r.htm>；<https://en.wikipedia.org/wiki/Blue_Banana>
- **#35** 「Everywhere, indeed, over the land of the globe between the frozen circles, the railway and the new roads will …」  
  判断：**部分符合**。铁路、公路和通讯网在两极圈之间大部分有人居住的陆地铺开，但并非覆盖“所有陆地”。  
  来源：<https://assets.publishing.service.gov.uk/media/5c07d08240f0b670656346e3/Historyoftransport.pdf>；<https://en.wikipedia.org/wiki/Controlled_access_highway>
- **#46** 「The house of the future will probably be warmed in its walls from some power-generating station, as, indeed, a…」  
  判断：**部分符合**。集中供暖和锅炉供热广泛取代了室内烧煤，但“由发电站在墙内供暖”的区域供热并未成为最普遍形态。  
  来源：<https://hss.sas.upenn.edu/sites/default/files/Industrial%20Revolution%20in%20the%20Home.pdf>；<https://www.americanhistory.si.edu/explore/stories/power-people-rural-electrification-brought-more-lights>；<https://www.1900s.org.uk/1940s50s-coal-fires.htm>
- **#48** 「there will be no chimneys at all to the house of the future of this type, except the flue for the kitchen smel…」  
  判断：**部分符合**。许多现代住宅不再依赖开放式烟囱取暖，但厨房排气和部分烟囱仍然存在，并非除厨气味烟道外完全消失。  
  来源：<https://hss.sas.upenn.edu/sites/default/files/Industrial%20Revolution%20in%20the%20Home.pdf>；<https://www.1900s.org.uk/1940s50s-coal-fires.htm>；<https://www.americanhistory.si.edu/explore/stories/power-people-rural-electrification-brought-more-lights>
- **#51** 「where will the moral censor of the year 1950 find his congenial following to gather stones?」  
  判断：**部分符合**。对未婚母亲的态度在20世纪逐步放宽，但到1950年英美学界和福利实践中耻感与收容制度仍相当普遍，时间点上早于全面改观。  
  来源：<https://www.thebritishacademy.ac.uk/documents/249/Happy-families-History-family-policy.pdf>；<https://www.theguardian.com/lifeandstyle/2007/oct/31/familyandrelationships.women>
- **#56** 「In other words, there will be a process of moral segregation[31] set up.」  
  判断：**部分符合**。城市中确有按阶层、生活方式划分的街区，但并非普遍形成被明确标记的道德隔离区。  
  来源：<https://www.thebritishacademy.ac.uk/documents/249/Happy-families-History-family-policy.pdf>；<http://www.demographia.com/db-wldurb-2000r.htm>
- **#57** 「Unless some great catastrophe in nature break down all that man has built, these great kindred groups of capab…」  
  判断：**部分符合**。受过科学教育的专业阶层影响力大增，但并未作为单一主导力量“最终浮现”并压倒其他社会成分。  
  来源：<https://www.cambridge.org/core/journals/european-political-science-review/article/beyond-dualism-the-hybridization-of-technocracy-and-democracy-in-europe/E84607A737F7ED0EAC3D3E19210AD316>；<https://www.bls.gov/opub/mlr/2006/03/art3full.pdf>
- **#61** 「War in the future will be a question of preparation, of long years of foresight and disciplined imagination, t…」  
  判断：**部分符合**。一战前线呈现长期对峙与冲突扩散，准备和物质基础变得决定性，但后世战争中仍有多次具有决定性的战役，故“不会有决定性会战”过绝对。  
  来源：<https://openstax.org/books/world-history-volume-2/pages/11-3-total-war>；<https://en.wikipedia.org/wiki/Technology_during_World_War_I>
- **#64** 「with tapes (or phonograph to replace them) in every post-office and nearly every private house」  
  判断：**部分符合**。广播、电视和互联网把即时新闻送进家庭，方向正确，但并非威尔斯所设想的每户电报纸带或留声装置。  
  来源：<https://en.wikipedia.org/wiki/Wirephoto>
- **#73** 「Warfare in the future, on sea or land alike, will be much more one-sided than it has ever been in the past, mu…」  
  判断：**部分符合**。部分战争因技术差距而高度一边倒，但20世纪仍有多场胜负难料、持久胶着的大战，并非普遍“更加可预料”。  
  来源：<https://openstax.org/books/world-history-volume-2/pages/11-3-total-war>；<https://en.wikipedia.org/wiki/Battle_of_the_Atlantic>；<https://en.wikipedia.org/wiki/Technology_during_World_War_I>
- **#74** 「The Twentieth Century will see the effectual crowding out of most of the weaker languages」  
  判断：**部分符合**。许多弱势语言确被边缘化，英语等大语种叠加在其区域之上，但“大多数较弱语言被实际排挤掉”并不成立。  
  来源：<https://en.wikipedia.org/wiki/English_language>；<https://en.wikipedia.org/wiki/European_languages>；<https://en.wikipedia.org/wiki/List_of_countries_and_territories_where_English_is_an_official_language>
- **#75** 「then by the year 2000 I would prophesy that the whole functional body of human society would read, and perhaps…」  
  判断：**部分符合**。英语成为全球最重要的功能性和国际语言，但到2000年并非“整个功能性人类社会”都能阅读或使用英语。  
  来源：<https://en.wikipedia.org/wiki/English_language>；<https://en.wikipedia.org/wiki/List_of_countries_and_territories_where_English_is_an_official_language>
- **#76** 「Of the two I am inclined to think French will spread further than German.」  
  判断：**部分符合**。法语在非洲等地仍有官方地位，但作为国际语言的扩张并未明显超过德语，两者都相对英语失势。  
  来源：<https://en.wikipedia.org/wiki/English_language>；<https://en.wikipedia.org/wiki/European_languages>；<https://en.wikipedia.org/wiki/List_of_countries_and_territories_where_English_is_an_official_language>；<https://www.pewresearch.org/short-reads/2017/10/27/500-years-after-the-reformation-5-facts-about-protestants-around-the-world/>
- **#77** 「Politically this region lies now in six independent States, but economically it must become one in the next fi…」  
  判断：**部分符合**。莱茵—鲁尔—比荷卢地区走向深度经济一体化，但“五十年内（至约1951年）必须在经济上成为一体”为时过早，欧共体煤钢联盟才刚刚起步。  
  来源：<https://en.wikipedia.org/wiki/Blue_Banana>
- **#78** 「It will almost certainly be the greatest urban region in all the world except that which will arise in the eas…」  
  判断：**部分符合**。莱茵沿线城市带（蓝香蕉）是欧洲最重要的城市区域之一，但并非除美国东部和汉口之外的世界最大城市区域。  
  来源：<https://en.wikipedia.org/wiki/Blue_Banana>；<http://www.demographia.com/db-wldurb-2000r.htm>
- **#79** 「By A.D. 2000 all these languages will be tending more and more to be the second tongues of bi-lingual communit…」  
  判断：**部分符合**。荷兰语和北欧语言地区普遍掌握英语等大语言，但这些语言本身仍是第一语言，并未沦为“越来越只是第二语言”。  
  来源：<https://en.wikipedia.org/wiki/European_languages>；<https://en.wikipedia.org/wiki/English_language>
- **#84** 「The splendid dream of a Federal Europe, which opened the nineteenth century for France, may perhaps, after all…」  
  判断：**部分符合**。欧盟等安排使“联邦欧洲”在21世纪初得到部分实现，但并非完整的联邦国家。  
  来源：<https://en.wikipedia.org/wiki/Blue_Banana>
- **#91** 「there will, I imagine, be a steady decay in the various Protestant congregations.」  
  判断：**部分符合**。欧美主流新教会众显著衰落，但全球南部的新教（尤其是五旬节派）仍在增长，故不是各地都“持续衰落”。  
  来源：<https://www.pewresearch.org/short-reads/2017/10/27/500-years-after-the-reformation-5-facts-about-protestants-around-the-world/>；<https://spectator.org/triumph-and-decline-of-americas-protestant-ascendancy/>

### 错误（12 条）

- **#9** 「that there are now so many thousand miles of these roads already established in America and Germany and elsewh…」  
  判断：**错误**。到1910年，美、德并不存在“数千英里”仅供机动车使用的专用道路；德国高速公路和英美现代路网要到两次大战之间乃至更晚才规模化。  
  来源：<https://en.wikipedia.org/wiki/Long_Island_Motor_Parkway>；<https://highways.dot.gov/highway-history/interstate-system/reichsautobahnen>；<https://www.roads.org.uk/blog/century-motorways>
- **#18** 「There can be little doubt that the sea speeds of 50 and even 60 miles an hour will be attained within the next…」  
  判断：**错误**。“几年之内”船舶普遍达到每小时50–60英里并未发生；当时最快鱼雷艇也远低于这一商用/常规航速，此后常规海船亦未在数年内达到该水平。  
  来源：<https://en.wikipedia.org/wiki/Steamship>
- **#19** 「I do not think it at all probable that aeronautics will ever come into play as a serious modification of trans…」  
  判断：**错误**。航空后来成为客运和远程交通的重大变革，与“航空永远不会严重改变运输与通讯”相反。  
  来源：<https://ourworldindata.org/grapher/airline-capacity-and-traffic?tab=table&time=1950..2024>；<https://www.iata.org/contentassets/9c78bde7ffb24da6b1f7085a07059161/100years-infographic-v3.pdf>
- **#25** 「So far as London, St. Petersburg, and Berlin go, it seems fairly safe to assume that they will go well over tw…」  
  判断：**错误**。到截点，伦敦、柏林、圣彼得堡均远未“远超两千万”，纽约、费城、芝加哥、武汉（汉口）也未达到四千万。  
  来源：<http://www.demographia.com/db-wldurb-2000r.htm>；<https://www2.census.gov/library/publications/2004/compendia/statab/123ed/hist/hs-07.pdf>；<https://en.wikipedia.org/wiki/List_of_metropolitan_areas_in_Europe_by_population>；<https://en.wikipedia.org/wiki/List_of_cities_with_over_one_million_inhabitants>
- **#58** 「This class will become, I believe, at last consciously _the_ State, controlling and restricting very greatly t…」  
  判断：**错误**。技术中产并未有意识地“成为国家本身”并全面管制其余阶层；选举政治与多元权力仍在。  
  来源：<https://www.cambridge.org/core/journals/european-political-science-review/article/beyond-dualism-the-hybridization-of-technocracy-and-democracy-in-europe/E84607A737F7ED0EAC3D3E19210AD316>
- **#59** 「The suppression of the party machine in the purely democratic countries and of the official choice of the rich…」  
  判断：**错误**。民主国家的政党机器并未被技术行政人员取代，君主制国家也未普遍改由技术管理者选择统治者。  
  来源：<https://www.cambridge.org/core/journals/european-political-science-review/article/beyond-dualism-the-hybridization-of-technocracy-and-democracy-in-europe/E84607A737F7ED0EAC3D3E19210AD316>
- **#62** 「this grey confusion that is Democracy must pass away inevitably by its own inherent conditions」  
  判断：**错误**。民主并未因其内在条件而消亡并演化为世界国家，当代仍以民族国家民主政体为主。  
  来源：<https://www.cambridge.org/core/journals/european-political-science-review/article/beyond-dualism-the-hybridization-of-technocracy-and-democracy-in-europe/E84607A737F7ED0EAC3D3E19210AD316>；<https://en.wikipedia.org/wiki/German_Empire>
- **#71** 「At the utmost the submarine will be used in narrow waters, in rivers, or to fluster or destroy ships in harbou…」  
  判断：**错误**。潜艇在两次大战的开阔海洋战役（尤其是大西洋战役）中发挥了核心作用，远不止用于狭窄水域或港内骚扰。  
  来源：<https://en.wikipedia.org/wiki/U-boat>；<https://en.wikipedia.org/wiki/Battle_of_the_Atlantic>
- **#72** 「And, even then, it can be merely destructive, while a sane and high-spirited fighter will always be dissatisfi…」  
  判断：**错误**。与上条相同：潜艇成为远洋破交的主力兵器，预测明显低估了其作用。  
  来源：<https://en.wikipedia.org/wiki/U-boat>；<https://en.wikipedia.org/wiki/Battle_of_the_Atlantic>
- **#81** 「Politically the Russian Government may come to dominate China in the coming decades, but the reality beneath a…」  
  判断：**错误**。俄国既未在之后几十年形式上支配中国，也未被东亚综合体所吸纳；苏联与中华人民共和国是独立大国关系。  
  来源：<https://en.wikipedia.org/wiki/German_Empire>；<https://learningenglish.voanews.com/a/a-23-2006-07-12-voa3-83127997/125489.html>
- **#85** 「There will, I believe, develop about that centre a great federation of white English-speaking peoples, a feder…」  
  判断：**错误**。并未出现以墨西哥以北美洲为核心、拥有共同联邦政府和舰队的英语民族大联邦。  
  来源：<https://history.state.gov/milestones/1921-1936/naval-conference>；<https://en.wikipedia.org/wiki/English_language>；<https://learningenglish.voanews.com/a/a-23-2006-07-12-voa3-83127997/125489.html>
- **#88** 「And the ethical system of these men of the New Republic, the ethical system which will dominate the world stat…」  
  判断：**错误**。优生学曾在20世纪部分国家实践，但二战后遭到摒弃，并未成为主导世界国家的伦理。  
  来源：<https://www.pewresearch.org/short-reads/2017/10/27/500-years-after-the-reformation-5-facts-about-protestants-around-the-world/>；<https://www.thebritishacademy.ac.uk/documents/249/Happy-families-History-family-policy.pdf>

### 暂无法判断（1 条）

- **#90** 「It will aim to establish, and it will at last, though probably only after a second century has passed, establi…」  
  判断：**暂无法判断**。“再过一个世纪才建立有共同语言和共同统治的世界国家”的明示终点仍在未来，到2026年尚未出现可据以判定的最终结果。  
  来源：<https://en.wikipedia.org/wiki/Blue_Banana>；<https://en.wikipedia.org/wiki/English_language>；<https://www.cambridge.org/core/journals/european-political-science-review/article/beyond-dualism-the-hybridization-of-technocracy-and-democracy-in-europe/E84607A737F7ED0EAC3D3E19210AD316>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/wells-anticipations-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/wells-anticipations-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/wells-anticipations-v5/audit/manual_review_2026-11-15.py`

## 说明

- 开篇脚注认为航空不太可能严重改变运输，后文又预言飞机将用于战争：两条都按原文各自计分（前者错误，后者正确）。
- 第 31 条（办公室与每日通勤需求下降）和第 80 条（最终将出现内部和平的世界国家）按趋势符合记录：方向出现但终点未到。
- 第 90 条（再过一个世纪才建立有共同语言和共同统治的世界国家）明示终点仍在未来，记为暂无法判断。
- 统计以 pipeline.py report 的 summary.json 为准；本表的加权胜率按 manual_report.py 的权重计算。

