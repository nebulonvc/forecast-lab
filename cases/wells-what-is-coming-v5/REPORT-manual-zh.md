# 赫伯特·乔治·威尔斯《即将到来的事物：对战后的预测》（What Is Coming? A Forecast of Things after the War）：出版后预测人工核查

- 案例目录：`cases/wells-what-is-coming-v5/`
- 出版日期：**1916 年**（写于一战进行中，同年由 Cassell（伦敦）／Macmillan（纽约）出版）。正文为 Project Gutenberg #11289，`reading-library/2026-11-15-未来判断扩展100本/02-政治与治理/025-what-is-coming-a-forecast-of-things-after-the-war.txt`，sha256 `c5f23e1fcfe1f5c325220f1daf6c489cb18807e100c0b275a0e9041df6950191`。观察窗口为 1916→2026-11-15；书中明示的终点（1916 年底、1917 年前、至迟 1918、1924、1926、二十五年内、五十年内、1950、1960、一百年后、两百年后、2100、2200 等）分别适用。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

本稿按 METHOD.md 执行。抽取：用仓库 prepare_book v5 流水线（toolkit 85e6da1）把全文切成 113 块（3500 字符、600 字符上下文；第 108 块后半至第 113 块为 Project Gutenberg 许可文本，无预测）。助手逐块通读，按 DISCOVER_PROMPT_V5 写出模型本应返回的 JSON，再由仓库代码完成引文对齐、归属降级、去重和导入，得到 139 条候选，其中 133 条可核验预测（约 1.18 条/块，约 34 条/10 万字符）。本书是一部专门预测战后局势的书，所以密度明显高于一般非虚构。核验：按 58 个主题先写 scope，各做一次 support 和一次 counter 的 Exa 检索，共两轮 118 次请求，只使用检索返回的 URL。原文存档于 data/sources（169 份，sha256），写入 data/evidence.jsonl（169 条）。由助手阅读后按四分类规则评断，再经 pipeline.py apply assess → check → report。本稿由助手逐条对照书中原文与存档证据人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 133 条，剔除非预测 0 条，计入 **133 条预测**，其中 **124 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 53 |
| 趋势符合 | 14 |
| 部分符合 | 35 |
| 错误 | 22 |
| 暂无法判断 | 9 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **42.7%**（53/124） |
| 加权胜率 | **65.3%** |
| 错误率 | **17.7%**（22/124） |
| 未定占比（暂无法判断/预测） | 6.8%（9/133） |

## 总体评价

威尔斯对一战本身走向的判断多数命中：战争是持续多年的消耗战，于 1918 年结束；德国战败但未被彻底粉碎；德国率先提出和平试探；保加利亚、土耳其先于德国退出；德国失去全部殖民地和占领区；和约带有惩罚性；霍亨索伦及德意志各邦君主全部倒台，魏玛联合政府式的共和国建立；协约国在 1916 年即讨论战后经济协调；交战国普遍停止黄金兑付；国际联盟成立；波兰在 25 年内再次成为战场；南斯拉夫建国；英国妇女获得选举权、离婚放宽、非婚生子女去污名、生育率下降、私人巨额财富集中下降，以及此后更具破坏性的大战等。主要误判集中在战后制度上：他预期战时国家管制会延续为“国家企业”并扩展到欧洲的集体所有，但英国在 1921 年前后就撤销管制、交还私营；他预期协约国同盟长期存续、出现三大集团并由战时双轨和会议和，但俄国退出、美国回归孤立，和会只在战后于巴黎召开；他预期 1926 年前出现国营汽车、英国学生普遍学俄语、法英双语、殖民扩张停止、霍亨索伦帝制再存续几代人等，均未发生。远期判断（2100 年前不再有从属民族、2200 年的民族格局、两百年后的人口格局）尚未到期，记为暂无法判断。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（53 条）

- **#1** 「men will probably be making aeroplanes of an improved pattern in 1950」  
  判断：**正确**。1950年前后喷气战斗机与轰炸机正在研制和量产（如美国陆军航空队的喷气机项目、加拿大CF-100），人们确实在制造改进型飞机。  
  来源：<https://generalatomic.com/jetmakers/chapter2.html>；<https://thecanadianencyclopedia.ca/en/article/avro-cf-100-canuck>
- **#6** 「And that current will flow, sluggishly or rapidly, towards war.」  
  判断：**正确**。帝国属地与列强对抗依旧存在，尽管有洛迦诺公约等努力，世界仍走向了第二次世界大战。  
  来源：<https://www.history.com/articles/world-war-ii-deadliest-war>；<https://en.wikipedia.org/wiki/Locarno_Treaties>
- **#7** 「There is every reason to believe that it will continue to intensify these characteristics.」  
  判断：**正确**。第二次世界大战成为史上最致命的战争，战略轰炸以摧毁敌方城市与平民为目标，比一战更具破坏性、更不顾非战斗人员。  
  来源：<https://www.history.com/articles/world-war-ii-deadliest-war>；<https://www.sciencespo.fr/mass-violence-war-massacre-resistance/en/content/perspectives-bombing-civilians-world-war-ii-present-introduction.html>
- **#8** 「there lies ahead a period of extreme economic and political dislocation」  
  判断：**正确**。战后欧洲出现1917–1923年革命浪潮和德国1921–1923年恶性通胀，经济政治极度混乱。  
  来源：<https://en.wikipedia.org/wiki/Revolutions_of_1917%E2%80%931923>；<https://en.wikipedia.org/wiki/Hyperinflation_in_the_Weimar_Republic>
- **#9** 「The credit system has been strained, and will be strained, and will need unprecedented readjustments.」  
  判断：**正确**。战后信用体系经历剧烈调整：德国通胀把债务“通胀掉”，英国自1914年停止的金本位到1925年才恢复。  
  来源：<https://libertystreeteconomics.newyorkfed.org/2023/07/inflating-away-the-debt-the-debt-inflation-channel-of-german-hyperinflation/>；<https://www.bankofengland.co.uk/quarterly-bulletin/1968/q4/the-exchange-equalisation-account---its-origins-and-development>
- **#10** 「Germany, I believe, is going to be beaten, but not completely crushed, by this war」  
  判断：**正确**。德国1918年11月战败并签署停战协定，但本土未被入侵、未遭彻底粉碎。  
  来源：<https://www.iwm.org.uk/history/first-world-war/armistice>；<https://explaininghistory.org/2012/12/11/germany-s-defeat-in-1918/>
- **#12** 「it is impossible to imagine that they will not set up some permanent organ for the direction and co-ordination…」  
  判断：**正确**。国际联盟盟约并入凡尔赛条约，联盟于1920年成立，成为协调国际关系的常设机构。  
  来源：<https://www.ungeneva.org/en/about/league-of-nations/overview>；<https://www.ungeneva.org/en/about/league-of-nations/covenant>
- **#13** 「it seems to me incredible that the two great Central European Powers should ever fall into sustained conflict …」  
  判断：**正确**。战后德奥之间未再爆发战争，1938年反而以合并方式结合。  
  来源：<https://encyclopedia.ushmm.org/content/en/article/german-foreign-policy-1933-1945>；<https://shs.cairn.info/journal-revue-de-l-ofce-2021-1-page-37?lang=en>
- **#18** 「the deadlock, if no sudden peace occurs, can end now in only one thing, the exhaustion in various degrees of a…」  
  判断：**正确**。战争最终以德国耗竭、在战场上失利后请求停战告终。  
  来源：<https://www.historytoday.com/archive/stabbed-front>；<https://www.iwm.org.uk/history/first-world-war/armistice>
- **#22** 「Nor is there anything on or under the sea that seems likely now to produce decisive results.」  
  判断：**正确**。日德兰海战未能取得决定性结果；潜艇战几乎拖垮英国，但被护航制度遏制，海上作战没有直接决定战局。  
  来源：<https://www.usni.org/magazines/naval-history-magazine/2016/june/jutlands-place-history>；<https://www.iwm.org.uk/history/first-world-war/germany/u-boat-campaign>
- **#23** 「Exhaustion is likely to be a very long and very thorough process, extending over years.」  
  判断：**正确**。耗竭过程持续两年多，直到1918年11月停战才结束。  
  来源：<https://en.wikipedia.org/wiki/Hundred_Days_Offensive>；<https://www.iwm.org.uk/history/first-world-war/armistice>
- **#24** 「A "war of attrition" may last into 1918 or 1919」  
  判断：**正确**。消耗战持续到1918年，于1918年11月11日停战结束，落在“1918或1919年”之内。  
  来源：<https://en.wikipedia.org/wiki/Hundred_Days_Offensive>；<https://www.iwm.org.uk/history/first-world-war/armistice>
- **#27** 「The Eastern and Western Allies will probably begin quite soon to discuss an anti-German Zollverein and the co-…」  
  判断：**正确**。1916年6月协约国巴黎经济会议即讨论战后对德经济战与协调措施。  
  来源：<https://thegreatwar.pl/en/allied-economic-conference-in-paris>；<https://history.state.gov/historicaldocuments/frus1916Supp/d1310>
- **#30** 「The broad conditions of a possible peace will begin to get stated towards the end of 1916, and a certain lassi…」  
  判断：**正确**。1916年12月12日德国及其盟国发出和平照会，随后威尔逊也发出和平照会，各方开始提出和平条件。  
  来源：<https://wwi.lib.byu.edu/index.php/Peace_Note_of_Germany_and_Her_Allies,_December_12,_1916>；<https://worldhistoryproject.org/1916/12/12/germany-makes-first-peace-proposal-to-allied-nations/>
- **#33** 「That is not going to stop the war」  
  判断：**正确**。财政困难没有让战争停下，战争一直打到1918年德国军事失败。  
  来源：<https://www.historytoday.com/archive/stabbed-front>；<https://www.iwm.org.uk/history/first-world-war/armistice>
- **#35** 「Great Britain will not get through the war on those terms.」  
  判断：**正确**。1914年英国以财政部纸币（Bradbury pound）替代金币流通，银行停止兑付黄金，实际上脱离了金本位。  
  来源：<https://assets.publishing.service.gov.uk/media/5a8feacaed915d1ddaadb643/FOI2018-00037_Bradbury_Pound.pdf>；<https://www.westernfrontassociation.com/world-war-i-articles/2020/december/the-first-world-war-paid-off/>
- **#36** 「Sooner or later, and probably in all cases before 1917, all the belligerents will be forced to adopt inconvert…」  
  判断：**正确**。德、奥匈、俄、法中央银行在战争初期即停止硬币兑付，英国也以不兑换纸币替代金币，均早于1917年。  
  来源：<https://www.nber.org/system/files/chapters/c5938/c5938.pdf>；<https://assets.publishing.service.gov.uk/media/5a8feacaed915d1ddaadb643/FOI2018-00037_Bradbury_Pound.pdf>
- **#39** 「The war will not end the conflict of anti-Germany and Germany」  
  判断：**正确**。此战没有终结德国与反德阵营的冲突，1939年德国再次挑起世界大战。  
  来源：<https://www.nationalww2museum.org/war/articles/invasion-poland-september-1939>；<https://www.history.com/articles/world-war-ii-deadliest-war>
- **#41** 「All these classes, by instinct and the baser kinds of reason also, will be doing their best to check the rise …」  
  判断：**正确**。战后英国推行通缩，并在1925年按战前平价恢复金本位，与预测的利益集团方向一致。  
  来源：<https://api.parliament.uk/historic-hansard/commons/1925/apr/28/return-to-gold-standard>；<https://cepr.org/voxeu/columns/walking-wounded-british-economy-aftermath-world-war-i>
- **#43** 「but I do not think there is going to be a chaotic and merely destructive phase in Great Britain or any Western…」  
  判断：**正确**。战后英国有罢工和激进运动，但没有发生革命，走的是改良而非叛乱之路。  
  来源：<https://www.bbc.co.uk/bitesize/guides/zc9887h/revision/4>；<https://books.openbookpublishers.com/10.11647/obp.0323/ch39.xhtml>
- **#45** 「she will have to give up every scrap of territorial advantage she has gained」  
  判断：**正确**。停战协定迫使德军撤出占领区，凡尔赛条约要求德国放弃布列斯特—立托夫斯克和约所得。  
  来源：<https://www.iwm.org.uk/history/first-world-war/armistice>；<https://en.wikipedia.org/wiki/Treaty_of_Versailles>
- **#46** 「she may lose most of her Colonial Empire」  
  判断：**正确**。凡尔赛条约第119条规定德国放弃全部海外属地。  
  来源：<https://history.state.gov/historicaldocuments/frus1919Parisv13/ch13subch1>；<https://encyclopedia.ushmm.org/content/en/article/treaty-of-versailles>
- **#48** 「I believe that the end of the war will see, not only transit, but shipping, collieries, and large portions of …」  
  判断：**正确**。战争结束时英国已设航运管制官（1916）、煤炭管制官（1917），铁路由国家控制，食品实行管理与配给。  
  来源：<https://thegreatwar.pl/en/new-ministries-in-britain>；<https://www.uvic.ca/humanities/history/assets/docs/davenport-daniel.pdf>；<https://api.parliament.uk/historic-hansard/lords/1921/aug/11/railways-bill>
- **#54** 「there will probably be far less evidence of great concentrations of private wealth in the European social land…」  
  判断：**正确**。西欧最富10%人群的财富占比在1900–1910年约90%，此后大幅下降，私人财富集中远低于战前。  
  来源：<http://www.piketty.pse.ens.fr/files/ideology/pdf/F10.4.pdf>；<https://www.history.com/articles/wwi-decline-british-aristocracy>
- **#55** 「there will be an enormously increased _rentier_ class drawing the interest of the war loans from the community」  
  判断：**正确**。战争借款使英国国债由战前约6.45亿英镑升至1920年约78亿英镑，大量持有战争公债者靠利息生活。  
  来源：<https://api.parliament.uk/historic-hansard/commons/1919/aug/18/national-indebtedness>；<https://www.natwestgroupremembers.com/banking-in-wartime/banking-business/supporting-government-borrowing-1914-18.html>；<https://www.telegraph.co.uk/news/election-2010/7640349/Geddes-Axe-a-brief-explanation.html>
- **#66** 「it seems incredible that it can ever again be reconstituted in its old seats upon the old lines」  
  判断：**正确**。剑桥1919年、牛津1920年取消入学必考希腊语，旧式古典教育未能照原样恢复。  
  来源：<https://archive.spectator.co.uk/article/6th-march-1920/3/greek-has-at-last-ceased-to-be-a-compulsory-subjec>；<https://bmcr.brynmawr.edu/2000/2000.05.04/>
- **#67** 「this war involves, in this as in so many matters, no fundamental set-back, no reversals nor restorations」  
  判断：**正确**。战后英国妇女获得选举权，1919年法律禁止以性别取消任职资格，妇女解放没有倒退。  
  来源：<https://www.parliament.uk/about/living-heritage/transformingsociety/electionsvoting/womenvote/overview/thevote/>；<https://www.gov.uk/government/news/the-sex-disqualification-removal-act-1919>
- **#68** 「Not the most frantic outbursts of militancy after this war can prevent them getting it.」  
  判断：**正确**。1918年人民代表法给予30岁以上、符合财产条件的妇女选举权。  
  来源：<https://www.parliament.uk/about/living-heritage/transformingsociety/electionsvoting/womenvote/overview/thevote/>
- **#71** 「The women of the next decades will not only be able to get along economically without marriage, but they will …」  
  判断：**正确**。一战造成男性短缺，受影响世代女性终身未婚比例上升；英国二战前大量人口未婚，部分因为女性占多数。  
  来源：<https://www.stlouisfed.org/on-the-economy/2015/march/how-world-war-i-changed-marriage-patterns-in-europe>；<https://www.thebritishacademy.ac.uk/documents/249/Happy-families-History-family-policy.pdf>
- **#74** 「The family, already light, will grow lighter.」  
  判断：**正确**。20世纪前期欧洲生育率持续急降，到1920年代半数以上欧洲人口生活在低于更替水平生育率的国家。  
  来源：<https://brispo.research.vub.be/sites/default/files/2024-02/IDWP2008-1.pdf>；<https://germanhistorydocs.org/en/nazi-germany-1933-1945/births-and-marriages-1900-1905-1910-and-1913-1941>
- **#76** 「the harsh lines once drawn between them will dissolve」  
  判断：**正确**。1926年合法化法、1969年和1987年家庭法改革逐步消除非婚生子女的法律区别，英国非婚生育比例也大幅上升。  
  来源：<https://www.parliament.uk/about/living-heritage/transformingsociety/private-lives/relationships/overview/legitimacyadoption/>；<https://www.legislation.gov.uk/ukpga/1987/42>；<https://static.ons.gov.uk/visual/2017/10/bornoutmarriage.csv>
- **#77** 「Marriage will not only be lighter, but more dissoluble.」  
  判断：**正确**。1923年婚姻诉讼法放宽离婚条件，此后英国离婚大幅增加。  
  来源：<https://www.parliament.uk/business/publications/research/olympic-britain/housing-and-home-life/split-pairs/>
- **#78** 「She will make the first advances towards peace」  
  判断：**正确**。1916年12月12日德国率先向协约国提出和平建议。  
  来源：<https://worldhistoryproject.org/1916/12/12/germany-makes-first-peace-proposal-to-allied-nations/>；<https://wwi.lib.byu.edu/index.php/Peace_Note_of_Germany_and_Her_Allies,_December_12,_1916>
- **#79** 「she will ultimately admit defeat.」  
  判断：**正确**。1918年德国请求停战并接受停战条件，实际承认失败（尽管后来出现“背后一刀”神话）。  
  来源：<https://explaininghistory.org/2012/12/11/germany-s-defeat-in-1918/>；<https://www.historytoday.com/archive/stabbed-front>
- **#82** 「It is my impression that she will be deserted by Bulgaria」  
  判断：**正确**。1918年9月29日保加利亚签订萨洛尼卡停战协定，先于德国退出战争。  
  来源：<https://en.wikipedia.org/wiki/Armistice_of_Salonica>
- **#83** 「Turkey will be out of the fighting before the end」  
  判断：**正确**。1918年10月30日奥斯曼帝国签订穆德洛斯停战协定，早于11月11日的德国停战。  
  来源：<https://anzacportal.dva.gov.au/wars-and-missions/ww1/politics/armistice>
- **#85** 「almost certainly Japan will be with them」  
  判断：**正确**。日本作为协约国一方出席巴黎和会。  
  来源：<https://en.wikipedia.org/wiki/List_of_participants_in_the_Paris_Peace_Conference_(1919%E2%80%931920)>；<https://history.state.gov/milestones/1914-1920/paris-peace>
- **#88** 「An entirely independent Poland will be a feverish field of international intrigue--intrigue to which the fatal…」  
  判断：**正确**。波兰1918年独立，1920年与苏俄交战，1939年德国入侵，确实在25年内再次成为战场。  
  来源：<https://guides.loc.gov/poland-manuscripts/timeline>；<https://en.wikipedia.org/wiki/Polish%E2%80%93Soviet_War>；<https://www.nationalww2museum.org/war/articles/invasion-poland-september-1939>
- **#94** 「sooner or later the south Slav state will insist upon itself」  
  判断：**正确**。1918年12月1日塞尔维亚—克罗地亚—斯洛文尼亚王国（南斯拉夫）成立。  
  来源：<https://en.wikipedia.org/wiki/Creation_of_Yugoslavia>
- **#95** 「Her gravitation to the Central Powers seems inevitable.」  
  判断：**正确**。战后匈牙利在霍尔蒂治下与纳粹德国结盟，最终加入轴心国。  
  来源：<https://www.history.com/articles/hungary-axis-powers-hitler>
- **#104** 「certain things are so inevitable--the integration of a modernised Bengal, of China, and of Egypt」  
  判断：**正确**。埃及1922年独立，印度（含孟加拉）1947年独立，这些地区相继摆脱从属地位。  
  来源：<https://en.wikipedia.org/wiki/Timeline_of_national_independence>；<https://en.wikipedia.org/wiki/Republic_in_the_Commonwealth_of_Nations>
- **#105** 「These Dominions seem rather to tend to become independent and distinct sovereign states in close and affection…」  
  判断：**正确**。1926年贝尔福宣言、1931年威斯敏斯特法令确认各自治领为与英国平等的自治共同体，而非建立帝国议会。  
  来源：<https://thecanadianencyclopedia.ca/en/article/statute-of-westminster>；<https://teara.govt.nz/en/self-government-and-independence/page-6>
- **#112** 「There is practically always going to be an Egypt, a Poland, an Armenia.」  
  判断：**正确**。埃及（1922）、波兰（1918）、亚美尼亚（1991）均已独立存在。  
  来源：<https://en.wikipedia.org/wiki/Timeline_of_national_independence>；<https://www.indexmundi.com/factbook/fields/independence>；<https://guides.loc.gov/poland-manuscripts/timeline>
- **#114** 「That body must come into human affairs.」  
  判断：**正确**。1920年成立国际联盟，作为维护和平的常设国际机构。  
  来源：<https://www.ungeneva.org/en/about/league-of-nations/overview>；<https://www.ungeneva.org/en/about/league-of-nations/covenant>
- **#115** 「if Germany by some swift convulsion expelled her dynasty and turned herself into a republic, it would be impos…」  
  判断：**正确**。1918年11月9日德国宣布君主退位、成立共和国，两天后英国等即与德国停战，没有继续战争。  
  来源：<https://en.wikipedia.org/wiki/Abdication_of_Wilhelm_II>；<https://www.iwm.org.uk/history/first-world-war/armistice>
- **#118** 「when the soldiers come home the hate will come home as well」  
  判断：**正确**。1918年后德国并未安宁，自由军团与左右翼政治暴力几乎引发内战。  
  来源：<https://doi.org/10.11575/prism/27638>；<https://www.theholocaustexplained.org/the-nazi-rise-to-power/the-effects-of-the-first-world-war-on-germany/>
- **#120** 「The time when Britain will again have a Queen of British race may not be very remote.」  
  判断：**正确**。出身英国贵族的伊丽莎白·鲍斯-莱昂1936年成为王后，1952年伊丽莎白二世即位。  
  来源：<https://www.royal.uk/encyclopedia/queen-elizabeth-the-queen-mother>；<https://www.royal.uk/queen-elizabeth-iis-accession-and-coronation>
- **#123** 「This, we suppose, will be a restrictive peace so far as Germany is concerned, humiliating her and hampering he…」  
  判断：**正确**。凡尔赛条约对德国施加严厉惩罚：割地约10%、限制军备、承担战争责任与赔款，德国视为屈辱。  
  来源：<https://encyclopedia.ushmm.org/content/en/article/treaty-of-versailles>；<https://history.state.gov/milestones/1914-1920/paris-peace>
- **#124** 「The German Press will talk freely of a _revanche_ and the renewal of the struggle」  
  判断：**正确**。战后“背后一刀”神话在德国广泛流传，助长极端民族主义与复仇情绪。  
  来源：<https://www.theholocaustexplained.org/the-nazi-rise-to-power/the-effects-of-the-first-world-war-on-germany/>；<https://www.historytoday.com/archive/stabbed-front>
- **#125** 「The mercantile and professional classes will join hands with the social democrats to remove the decaying incub…」  
  判断：**正确**。帝制倒台后社民党与德国民主党、中央党组成魏玛联合政府，建立议会共和国。  
  来源：<https://en.wikipedia.org/wiki/Weimar_Coalition>；<https://en.wikipedia.org/wiki/Abdication_of_Wilhelm_II>
- **#126** 「This collapse of the Germanic monarchical system may spread considerably beyond the limits of the German empir…」  
  判断：**正确**。德意志各邦君主全部退位，奥匈哈布斯堡王朝也随之终结，崩溃超出德意志帝国范围。  
  来源：<https://en.wikipedia.org/wiki/List_of_German_monarchs_in_1918>；<https://en.wikipedia.org/wiki/Dissolution_of_Austria-Hungary>
- **#128** 「the inevitable fall in the German birth-rate」  
  判断：**正确**。德国生育率在20世纪持续下降，小家庭化趋势延续。  
  来源：<https://germanhistorydocs.org/en/nazi-germany-1933-1945/births-and-marriages-1900-1905-1910-and-1913-1941>；<https://www.statista.com/statistics/1033102/fertility-rate-germany-1800-2020/>
- **#131** 「The German population is and will remain the central and largest mass of people in Europe.」  
  判断：**正确**。德国至今仍是欧盟人口最多的国家，位于欧洲中部。  
  来源：<https://www.bbc.com/news/world-europe-17299607>；<https://en.wikipedia.org/wiki/Germany>

### 趋势符合（14 条）

- **#25** 「she will completely socialise herself, completely reorganise her whole social and economic structure sooner th…」  
  判断：**趋势符合**。英国没有输掉战争，战时设立航运管制官、对煤矿实行国家控制并实行食品配给，社会经济大幅国家化，方向一致，但并非“彻底社会化”。  
  来源：<https://thegreatwar.pl/en/new-ministries-in-britain>；<https://api.parliament.uk/historic-hansard/commons/1917/mar/27/coal-mines-state-control>
- **#37** 「The pound British will come out of this war like a company out of a well-shelled trench--attenuated.」  
  判断：**趋势符合**。英国自1914年起停止金本位，直到1925年才按战前平价恢复，说明战后英镑并不在战前平价上，方向一致；来源未给出具体贬值幅度。  
  来源：<https://www.bankofengland.co.uk/speech/2025/june/andrew-bailey-opening-remarks-at-britains-return-to-the-gold-standard-in-1925-conference>；<https://api.parliament.uk/historic-hansard/commons/1925/apr/28/return-to-gold-standard>
- **#40** 「This Court and land-holding class cannot go on being rich and living rich during the strains of the coming yea…」  
  判断：**趋势符合**。战后重税和遗产税迫使大批英国土地贵族出售庄园，财富与奢华生活明显衰落；但王室并未因此失去富裕地位。  
  来源：<https://www.history.com/articles/wwi-decline-british-aristocracy>；<https://www.theatlantic.com/magazine/archive/1922/04/changes-in-landownership-in-england/647625/>
- **#63** 「The widely prevalent discontent with the part played by the lawyer in the affairs of all the Western Allies is…」  
  判断：**趋势符合**。英国法律职业改革要到20世纪中后期（1979年本森皇家委员会、1990年改革）才真正推进，方向一致但远非战后不久。  
  来源：<https://scholar.smu.edu/til/vol24/iss3/12>；<https://www.cambridge.org/core/journals/cambridge-law-journal/article/liberalisation-and-the-legal-profession-in-england-and-wales/4D9AAC9607C7948B893097867978310B>
- **#73** 「this increase in the class of economically independent bachelor women that is now taking place is a permanent …」  
  判断：**趋势符合**。女性就业壁垒在法律上被拆除，结婚比例此后长期下降，独立单身女性群体扩大，方向一致。  
  来源：<https://www.gov.uk/government/news/the-sex-disqualification-removal-act-1919>；<https://www.parliament.uk/business/publications/research/olympic-britain/housing-and-home-life/all-you-need-is-love-and-a-marriage-certificate/>
- **#75** 「There is an increasing disposition to group solitary children and to delegate their care to specially qualifie…」  
  判断：**趋势符合**。一战期间为让已婚妇女工作而开设托儿所，二战时又设立大量战时托儿所，但托育供给增长时断时续，方向一致而进展有限。  
  来源：<https://historyandpolicy.org/wp-content/uploads/original/docs/pat_thane_early_years.pdf>；<https://doi.org/10.1080/00071005.2020.1804525>
- **#91** 「The German kings would vanish like a wisp of smoke.」  
  判断：**趋势符合**。1918年德国全部君主退位，奥匈、奥斯曼王朝亦相继终结；但保加利亚、南斯拉夫等王冠仍存，“几乎全部”略有夸大。  
  来源：<https://en.wikipedia.org/wiki/List_of_German_monarchs_in_1918>；<https://en.wikipedia.org/wiki/Dissolution_of_Austria-Hungary>
- **#99** 「I believe it will turn first to the idea of keeping the seas with Britain and France, and then to this still w…」  
  判断：**趋势符合**。1920年代英美签订华盛顿海军条约但仍有海军竞争，1941年大西洋宪章、1949年北约才形成合作维和格局，方向一致但过程更曲折。  
  来源：<https://history.state.gov/milestones/1921-1936/naval-conference>；<https://history.state.gov/milestones/1921-1936/geneva>；<https://www.gchq.gov.uk/information/brief-history-of-ukusa>；<https://usnhistory.navylive.dodlive.mil/Wars-Conflicts-and-Operations/Article-View/Article/3734783/the-navy-and-the-formation-of-nato/>
- **#101** 「The age of "expansion," the age of European "empires" is near its end.」  
  判断：**趋势符合**。战后委任统治使殖民帝国在1920年达到面积顶峰，此后扩张基本停止，并于1947–1980年解体，方向一致但并非立即终结。  
  来源：<https://thewheeleratlas.com/moments/british-empire-1920>；<https://examexplained.com.au/vce/modern-history/syllabus/unit-2/decolonisation-africa-asia-1947-1980>
- **#102** 「it will end last in Africa, and even in Africa the end draws near」  
  判断：**趋势符合**。亚洲殖民地先于非洲独立，1960年“非洲年”有17国独立，帝国时代最后在非洲结束，但距1916年仍有四十多年。  
  来源：<https://en.wikipedia.org/wiki/Year_of_Africa>；<https://examexplained.com.au/vce/modern-history/syllabus/unit-2/decolonisation-africa-asia-1947-1980>
- **#108** 「Through all Africa and Western Asia there is a great to-morrow for a renascent Islam under Arab auspices.」  
  判断：**趋势符合**。20世纪伊斯兰复兴运动兴起（1928年埃及穆斯林兄弟会），伊斯兰教在非洲与西亚影响巨大，方向一致，但并非统一由阿拉伯人主导的复兴。  
  来源：<https://www.foreignaffairs.com/middle-east/moderate-muslim-brotherhood>；<https://www.pewresearch.org/religion/2025/06/09/religion-in-sub-saharan-africa/>
- **#109** 「The whole trend of events in Asia Minor, the breaking up and decapitation of the Ottoman Empire and the Euphra…」  
  判断：**趋势符合**。英国行政当局1920年代起推行现代化，加上1927年发现石油，伊拉克人口迅速增长，1958年接近700万，方向一致；但称不上“大复兴”。  
  来源：<https://www.statista.com/statistics/1066952/population-iraq-historical/>；<https://www.nature.com/articles/143018c0.pdf>
- **#113** 「India might be a confederation of sovereign states in close alliance with the British Empire and its allies wi…」  
  判断：**趋势符合**。印度1947年独立，1950年成为共和国并留在英联邦，方向一致；但形成的是印巴分治而非主权国家联邦。  
  来源：<https://en.wikipedia.org/wiki/Republic_in_the_Commonwealth_of_Nations>
- **#127** 「It will probably be effected without much violence」  
  判断：**趋势符合**。革命初期大体和平，皇帝退位与各邦君主退位没有大流血；但1919年斯巴达克斯起义等带来流血冲突。  
  来源：<https://origins.osu.edu/review/victorious-weimar-reframing-german-revolution>；<https://en.wikipedia.org/wiki/German_Revolution_of_1918%E2%80%9319>

### 部分符合（35 条）

- **#3** 「Mechanical novelties will probably play a very small part in that coming history.」  
  判断：**部分符合**。1920年代无线电、汽车、电网与电影迅速普及、深刻改变生活，但多为既有发明的扩散而非新发明；“机械发明作用很小”只部分成立。  
  来源：<https://www.countryreports.org/lessons/ap-us-history/unit-7/7-1920s-innovations>；<https://www.nist.gov/pao/nist-100-foundations-progress/roaring-twenties-overview>
- **#4** 「if there is much difference in the roads and railways and shipping it will be for the worse」  
  判断：**部分符合**。战后英国铁路收入受损、航运业走向衰退，但公路运输在1920年代迅速发展，“若有变化也是变差”只部分成立。  
  来源：<https://en.wikipedia.org/wiki/History_of_rail_transport_in_Great_Britain_1923%E2%80%931947>；<https://www.thefreelibrary.com/Managing+decline%3A+the+political+economy+of+British+shipping+in+the...-a0415444522>
- **#5** 「architecture, domestic equipment, and so on, will be fortunate if in 1924 they stand where they did in the spr…」  
  判断：**部分符合**。战后英国住房严重短缺，但1919年住房法、1924年住房法推动了政府补贴的新住房建设，不完全是停滞于1914年水平。  
  来源：<https://www.parliament.uk/about/living-heritage/transformingsociety/towncountry/towns/overview/councilhousing/>；<https://www.bbc.co.uk/programmes/p011mt9s>
- **#11** 「she is going to be left militarist and united with Austria and Hungary, and unchanged in her essential nature」  
  判断：**部分符合**。战后奥匈帝国解体，和约禁止德奥合并，德国与奥、匈并未立即联合；军国主义情绪延续，直到1938年德奥合并、匈牙利后来与纳粹德国结盟才部分应验。  
  来源：<https://en.wikipedia.org/wiki/Dissolution_of_Austria-Hungary>；<https://shs.cairn.info/journal-revue-de-l-ofce-2021-1-page-37?lang=en>；<https://www.history.com/articles/hungary-axis-powers-hitler>
- **#16** 「none of them is likely to be a monarchy」  
  判断：**部分符合**。德国确实变为共和国，但三大集团本身没有出现，英国等协约国仍是君主制；只部分符合。  
  来源：<https://en.wikipedia.org/wiki/Abdication_of_Wilhelm_II>；<https://encyclopedia.ushmm.org/content/en/article/the-united-states-isolation-intervention>
- **#17** 「But it will be a Roman world peace, made in Germany, and there will have to be several more great wars before …」  
  判断：**部分符合**。协约国合作未能维持（美国拒绝凡尔赛条约），此后又爆发大战；但德国主导的和平只是短暂的，德国在二战中战败。  
  来源：<https://www.senate.gov/about/powers-procedures/treaties/senate-rejects-treaty-of-versailles.htm>；<https://www.history.com/articles/world-war-ii-deadliest-war>
- **#19** 「The end of this war will be a matter of negotiation between practically immobilised and extremely shattered an…」  
  判断：**部分符合**。战争以谈判停战结束，协约国未攻入柏林，这一点应验；但1918年并非双方“几乎动弹不得”，百日攻势是大规模运动战，德国是被迫接受条件。  
  来源：<https://explaininghistory.org/2012/12/11/germany-s-defeat-in-1918/>；<https://www.iwm.org.uk/history/first-world-war/armistice>
- **#20** 「it is highly probable that they will be repeated on a much larger scale before the war is over」  
  判断：**部分符合**。对英空袭持续到战争结束，但1916年后齐柏林飞艇损失惨重，空袭主力改由哥达轰炸机承担；齐柏林空袭本身并未以更大规模重演。  
  来源：<https://history.blog.gov.uk/2015/01/19/air-raid-casualties-in-the-first-world-war/>；<https://en.wikipedia.org/wiki/German_bombing_of_Britain,_1914%E2%80%931918>
- **#26** 「The German group, I reckon, therefore, will become exhausted first.」  
  判断：**部分符合**。同盟国最终先后崩溃，但最先耗竭退出战争的是俄国（1918年布列斯特—立托夫斯克和约）。  
  来源：<https://en.wikipedia.org/wiki/Treaty_of_Brest-Litovsk>；<https://en.wikipedia.org/wiki/Armistice_of_Salonica>
- **#28** 「some neutral power, Denmark or Spain or the United States or Holland, will invite representatives to an inform…」  
  判断：**部分符合**。1916年有私人发起的中立国调停会议，1917年社会党人计划在中立国召开斯德哥尔摩会议，但并非由中立国政府邀请各方讨论战后安排。  
  来源：<https://digital.janeaddams.ramapo.edu/items/show/8385>；<https://www.socialhistoryportal.org/stockholm1917>
- **#32** 「The belligerent Powers are approaching a phase when they will no longer be paying anything like twenty shillin…」  
  判断：**部分符合**。德国借恶性通胀实际赖掉了国内债务，但英国并未违约，1926年仍在逐年减债，1925年按战前平价恢复金本位；只部分应验。  
  来源：<https://libertystreeteconomics.newyorkfed.org/2023/07/inflating-away-the-debt-the-debt-inflation-channel-of-german-hyperinflation/>；<https://api.parliament.uk/historic-hansard/commons/1926/apr/26/dept-redemption>；<https://api.parliament.uk/historic-hansard/commons/1925/apr/28/return-to-gold-standard>
- **#38** 「It will emerge from this war much more so than it went in」  
  判断：**部分符合**。战时国家管制在1921年前后被撤销，煤矿和铁路交还私营；国家企业化要到1945年后的国有化才部分实现。  
  来源：<https://en.wikipedia.org/wiki/Black_Friday_(1921)>；<https://researchbriefings.files.parliament.uk/documents/CBP-8325/CBP-8325.pdf>
- **#44** 「Out of this war, whatever else emerges, there will emerge a more highly organised State than existed before」  
  判断：**部分符合**。战后英国很快撤销管制并削减公共开支（格迪斯斧），组织化、社会主义化的国家要到1945年后才部分出现。  
  来源：<https://en.wikipedia.org/wiki/Black_Friday_(1921)>；<http://www.christopherhood.net/pdfs/public-spending-in-hard-times.pdf>；<https://researchbriefings.files.parliament.uk/documents/CBP-8325/CBP-8325.pdf>
- **#47** 「she may be obliged to complete her modernisation by abandoning her militant Imperialism」  
  判断：**部分符合**。1919年凡尔赛条约迫使德国裁军、放弃殖民地，但1930年代纳粹德国重拾扩张性帝国主义。  
  来源：<https://encyclopedia.ushmm.org/content/en/article/treaty-of-versailles>；<https://encyclopedia.ushmm.org/content/en/article/german-foreign-policy-1933-1945>
- **#50** 「America will be the continent with the long purse, prepared to buy rather than sell.」  
  判断：**部分符合**。战后美国确实成为财力雄厚的债权国，但其经常账户自1890年代至1970年代长期顺差，是卖方而非买方。  
  来源：<https://doi.org/10.5287/ora-ga99pxbqy>；<https://hsus.cambridge.org/HSUSWeb/essay/pdf/Ee.ESS.01.pdf>
- **#51** 「The Allies will become State firms, as Germany was, indeed, already becoming before the war」  
  判断：**部分符合**。战后英国很快撤销管制；煤炭、铁路等要到1945年后才国有化（法国1937年铁路国有化），农业从未成为国家事业。  
  来源：<https://en.wikipedia.org/wiki/Black_Friday_(1921)>；<https://researchbriefings.files.parliament.uk/documents/CBP-8325/CBP-8325.pdf>；<https://industrie-uoh.univ-tlse2.fr/04_mutations-industrielles/112_nationalisations.html>
- **#56** 「By 1926 we shall be going about a world that will have recovered very largely from the impoverishment of the s…」  
  判断：**部分符合**。1925–1929年欧洲制造业增长较快，但英国1920年代通缩、高失业，1926年还发生大罢工，到1926年只是部分恢复。  
  来源：<https://doi.org/10.1007/978-1-349-03036-1_3>；<https://www.economicshelp.org/blog/5948/economics/uk-economy-in-the-1920s/>；<https://www.nationalarchives.gov.uk/explore-the-collection/stories/the-general-strike/>
- **#58** 「and paying off the National Debt simultaneously」  
  判断：**部分符合**。1926年英国国债仍有约76.16亿英镑，当年只减少3000万英镑，偿还极其有限。  
  来源：<https://api.parliament.uk/historic-hansard/commons/1926/apr/26/dept-redemption>；<https://www.telegraph.co.uk/news/election-2010/7640349/Geddes-Axe-a-brief-explanation.html>
- **#64** 「will break down at last even the conservatism of the most rigidly organised and powerful and out-of-date of al…」  
  判断：**部分符合**。法律职业确实在20世纪中期以后快速变化、走向自由化，但与战争示范的关系缺乏证据。  
  来源：<https://www.cambridge.org/core/journals/cambridge-law-journal/article/liberalisation-and-the-legal-profession-in-england-and-wales/4D9AAC9607C7948B893097867978310B>；<https://scholar.smu.edu/til/vol24/iss3/12>
- **#70** 「I do not believe that this invasion by women of a hundred employments hitherto closed to them is a temporary a…」  
  判断：**部分符合**。1919年性别取消资格法开放了许多职业，但同年恢复战前惯例法把岗位还给复员男性，战后婚姻限制也迫使已婚女性离职，部分逆转。  
  来源：<https://www.gov.uk/government/news/the-sex-disqualification-removal-act-1919>；<https://en.wikipedia.org/wiki/Restoration_of_Pre-War_Practices_Act_1919>；<https://womenwhomeantbusiness.com/2020/12/27/the-marriage-bar/>
- **#72** 「it is quite possible that this process will be presently resumed and, as a new generation grows up to restore …」  
  判断：**部分符合**。战后几十年英国结婚率上升、结婚年龄下降（二战后至1970年代初），与预测相反；1970年代后才转为晚婚、少婚。  
  来源：<https://www.actuaries.org.uk/system/files/documents/pdf/0125-0134.pdf>；<https://www.thebritishacademy.ac.uk/documents/249/Happy-families-History-family-policy.pdf>；<https://blog.ons.gov.uk/2019/04/01/married-by-30-youre-now-in-the-minority/>
- **#80** 「In the end, America may have the power to insist upon almost vital conditions in the settlement」  
  判断：**部分符合**。美国参战后，德国被迫以十四点为谈判基础，但巴黎和会上英法迫使威尔逊在许多点上妥协。  
  来源：<https://www.gresham.ac.uk/sites/default/files/2018-11-07_DavidStevenson_TheEndingOfWWI-T.pdf>；<https://www.worldhistory.org/article/2801/woodrow-wilsons-fourteen-points/>
- **#86** 「it is doubtful if the United States will count for all that they might in the decision」  
  判断：**部分符合**。威尔逊在巴黎和会是“四巨头”之一，推动建立国联，但十四点被大幅妥协，美国参议院最终拒绝条约。  
  来源：<https://www.worldhistory.org/article/2801/woodrow-wilsons-fourteen-points/>；<https://www.senate.gov/about/powers-procedures/treaties/senate-rejects-treaty-of-versailles.htm>
- **#87** 「This war of exhaustion may be going on for a year or so more, but the end will be the thrusting in of the too …」  
  判断：**部分符合**。协约国最终把德军战线压回，但战争又持续了两年多，到1918年11月才结束，而非一年左右。  
  来源：<https://en.wikipedia.org/wiki/Hundred_Days_Offensive>；<https://www.iwm.org.uk/history/first-world-war/armistice>
- **#90** 「They will, I fear, do nothing of the sort.」  
  判断：**部分符合**。威尔逊的十四点和国联对和约有重大影响，但多处被英法压低，美国最终未批准条约；部分符合。  
  来源：<https://www.worldhistory.org/article/2801/woodrow-wilsons-fourteen-points/>；<https://www.senate.gov/about/powers-procedures/treaties/senate-rejects-treaty-of-versailles.htm>
- **#97** 「I believe that the stars in their courses tend to draw these States together into a dominant peace alliance」  
  判断：**部分符合**。二战中美、英、苏等结成反轴心同盟，但两次大战之间美国奉行孤立，战后也未形成包括俄国在内的持久主导性和平同盟。  
  来源：<https://encyclopedia.ushmm.org/content/en/article/axis-powers-in-world-war-ii>；<https://encyclopedia.ushmm.org/content/en/article/the-united-states-isolation-intervention>
- **#106** 「In a hundred years' time black Africa, west of Tripoli, from Oran to Rhodesia, will, I believe, talk French.」  
  判断：**部分符合**。非洲约有1.63亿法语使用者，占全球一半以上，但北非独立后推行阿拉伯化，法语并非“整个”黑非洲的通用语。  
  来源：<https://rvf.ca/en/news/la-francophonie-by-the-numbers/>；<https://doi.org/10.1515/ijsl.1999.137.115>
- **#107** 「I guess, however, that it will be an Islamic and not a Christian cult that will be talking Italian and French.」  
  判断：**部分符合**。萨赫勒的法语国家多数信仰伊斯兰教，但中非等法语国家以基督教为主，且撒哈拉以南非洲62%为基督徒。  
  来源：<https://www.pewresearch.org/religion/2009/10/07/mapping-the-global-muslim-population-sub-saharan-africa-overview/>；<https://www.visualcapitalist.com/africas-north-south-religious-divide/>；<https://www.pewresearch.org/religion/2025/06/09/religion-in-sub-saharan-africa/>
- **#110** 「The vast system of irrigation that was destroyed by the Mongol armies of Hulugu in the thirteenth century will…」  
  判断：**部分符合**。1938年库特拦河坝等灌溉工程建成，1950年成立发展委员会，人口大增；但盐碱化和沙漠化又严重侵蚀农地，沙漠并未普遍重新稠密。  
  来源：<https://www.nature.com/articles/143018c0.pdf>；<https://doi.org/10.4236/jwarp.2014.65042>；<https://reliefweb.int/report/iraq/iraq-death-knell-agriculture>
- **#111** 「A new intellectual movement in Islam, a renascent Bagdad, is as inevitable as is 1950.」  
  判断：**部分符合**。20世纪出现了伊斯兰新思潮，巴格达1950年人口约57.9万并持续扩大，但“复兴的巴格达”成为伊斯兰中心并不明确。  
  来源：<https://www.foreignaffairs.com/middle-east/moderate-muslim-brotherhood>；<https://books.mongabay.com/population_estimates/1950/Baghdad-Iraq.html>
- **#117** 「I do not think that all the schoolmasters of Germany, teaching in unison at the tops of their voices, will sus…」  
  判断：**部分符合**。皇帝退位、帝制终结，但“背后一刀”神话和军国主义、民族主义情绪延续，并最终被纳粹利用。  
  来源：<https://en.wikipedia.org/wiki/Abdication_of_Wilhelm_II>；<https://www.theholocaustexplained.org/the-nazi-rise-to-power/the-effects-of-the-first-world-war-on-germany/>
- **#119** 「print, paper and the spoken word have bound Germany now into one people for all time」  
  判断：**部分符合**。德国在1949–1990年分裂为两国，但1990年又统一，民族统一意识延续；“永久”一点并未完全应验。  
  来源：<https://en.wikipedia.org/wiki/Germany>；<https://www.bbc.com/news/world-europe-17299607>
- **#122** 「liberal forces in Germany may nevertheless be strong enough to force a peace upon the Hohenzollern empire so s…」  
  判断：**部分符合**。和平在1918年内到来，在“至迟1918年”之内；但主要原因是军事崩溃，并非自由派力量迫使帝国求和。  
  来源：<https://www.gresham.ac.uk/sites/default/files/2018-11-07_DavidStevenson_TheEndingOfWWI-T.pdf>；<https://en.wikipedia.org/wiki/Abdication_of_Wilhelm_II>
- **#129** 「By 1960 or so the alteration of perspectives will have gone so far that historians will be a little perplexed …」  
  判断：**部分符合**。1960年代初的费舍尔争论是最激烈的史学论战之一，说明史学界对战争起因高度争议，而不是难以理解；只部分符合。  
  来源：<https://research.aber.ac.uk/en/studentTheses/fritz-fischer-and-the-rise-of-critical-historiography-in-west-ger/>；<https://journals.sagepub.com/doi/10.1177/0022009412472712>
- **#133** 「it will take sixty or seventy years for the two sides in this present war to grow kindly again」  
  判断：**部分符合**。二战后德国迅速成为西方盟友，1963年法德签订爱丽舍条约实现和解，距1918年约45年，比预测的六七十年更快。  
  来源：<https://www.diplomatie.gouv.fr/en/the-ministry-in-action/ensuring-the-presence-of-french-culture/franco-german-cooperation/the-elysee-treaty-in-six-questions>；<https://www.open.edu/openlearn/mod/oucontent/view.php?id=142569&section=5>

### 错误（22 条）

- **#2** 「there will be a through railway connection between Constantinople and Bombay and between Baku and Bombay in th…」  
  判断：**错误**。到1966年并无君士坦丁堡或巴库直通孟买的铁路；伊朗与南亚路网的缺口（巴姆—扎黑丹段）直到2009年前后才接通，且印巴之间多数线路已废弃。  
  来源：<https://www.andrewgrantham.co.uk/afghanistan/gap-in-britain-to-india-rail-route-closed/>；<https://www.railwaygazette.com/news/2009/08/28/a-long-way-to-go/>；<https://irfca.org/faq/faq-inter.html>
- **#14** 「Probably the hundred millions of Latin America may achieve a method of unity, and then deal on equal terms wit…」  
  判断：**错误**。美洲国家组织1948年成立，但拉美区域一体化总体失败，各国不愿让渡主权，并未形成可与美国平起平坐的统一体。  
  来源：<https://www.oas.org/key_issues/eng/GAhistory.htm>；<https://www.scielo.br/j/cint/a/4P4f6PmP4LdPpgCmcDP3Ydt/?lang=en>
- **#15** 「there will be only three great World Powers left--the anti-German allies, the allied Central Europeans, the Pa…」  
  判断：**错误**。战后没有形成三大集团：奥匈解体，中欧同盟不复存在；美国两次大战之间奉行孤立主义，并未出现“泛美”力量集团。  
  来源：<https://en.wikipedia.org/wiki/Dissolution_of_Austria-Hungary>；<https://encyclopedia.ushmm.org/content/en/article/the-united-states-isolation-intervention>
- **#29** 「Probably, therefore, the peace negotiations will take the extraordinary form of two simultaneous conferences」  
  判断：**错误**。和会只有一个：1919年巴黎和会在停战后召开，战败国被排除在外，并非战争进行中同时召开的两个会议。  
  来源：<https://www.historisches-lexikon-bayerns.de/Lexikon/EN:Treaty_of_Versailles,_1919/20>；<https://germanhistorydocs.org/en/weimar-germany-1918-1933/the-paris-peace-conference-january-18-1919-january-21-1920>
- **#31** 「neither the Germans nor their antagonists will be able for many years to go on with those projects for world e…」  
  判断：**错误**。战后英国通过委任统治扩张，大英帝国约在1920年达到面积顶峰，殖民扩张并未停止。  
  来源：<https://thewheeleratlas.com/moments/british-empire-1920>；<https://en.wikipedia.org/wiki/Territorial_evolution_of_the_British_Empire>
- **#42** 「the association of the Pledged Allies will not break up after the war」  
  判断：**错误**。战后协约国同盟实际瓦解：俄国1918年单独媾和，美国参议院拒绝凡尔赛条约，英法在鲁尔问题上严重分歧。  
  来源：<https://en.wikipedia.org/wiki/Treaty_of_Brest-Litovsk>；<https://www.senate.gov/about/powers-procedures/treaties/senate-rejects-treaty-of-versailles.htm>；<https://doi.org/10.1057/9780230510999_4>
- **#49** 「It will be as impossible to put back British industrialism into the factories and forms of the pre-war era as …」  
  判断：**错误**。1921年前后煤矿和铁路交还私人经营，两次大战之间英国工业仍以众多小型私营企业为主。  
  来源：<https://en.wikipedia.org/wiki/Black_Friday_(1921)>；<https://researchbriefings.files.parliament.uk/documents/CBP-8325/CBP-8325.pdf>
- **#52** 「the Allies will be forced also to link their various State firms together into a great allied trust」  
  判断：**错误**。战后各国国家管制随即撤销，协约国并未把各自的国家企业联合成统一托拉斯；美国甚至拒绝加入国联。  
  来源：<https://en.wikipedia.org/wiki/Black_Friday_(1921)>；<https://www.senate.gov/about/powers-procedures/treaties/senate-rejects-treaty-of-versailles.htm>
- **#53** 「the ships, the railways, the coal and metal supply, the great metal industries, much engineering, and most agr…」  
  判断：**错误**。1930年代中期英国工业与公用事业仍以众多私营小企业为主，大规模国有化要到1945年后；农业更未集体化。  
  来源：<https://researchbriefings.files.parliament.uk/documents/CBP-8325/CBP-8325.pdf>；<https://www.econstor.eu/bitstream/10419/139470/1/v12-i05-a10-BF02928713.pdf>
- **#57** 「we shall tour in State-manufactured automobiles upon excellent roads」  
  判断：**错误**。到1926年并无国营工厂造车；德国劳工阵线主导的“国民汽车”项目直到1937年才开始。  
  来源：<https://www.volkswagen-group.com/en/volkswagen-chronicle-17351/1937-to-1945-founding-of-the-company-and-integration-into-the-war-economy-17354>；<https://researchbriefings.files.parliament.uk/documents/CBP-8325/CBP-8325.pdf>
- **#59** 「they will in many cases be learning Russian instead of Greek or German」  
  判断：**错误**。俄语在英国学校始终是小语种，法语长期占主导，并未在大量情况下取代希腊语或德语。  
  来源：<https://api.parliament.uk/historic-hansard/written-answers/1958/dec/11/russian-language>；<https://education-uk.org/documents/minofed/pamphlet-29.html>；<https://questions-statements.parliament.uk/written-questions/detail/2024-04-30/HL4240>
- **#60** 「More of our boys will be going into the public service, and fewer thinking of private business」  
  判断：**错误**。1920年代英国大幅削减公务员；近年公务员占全部就业不到2%，青年并未主要流向公共服务。  
  来源：<http://www.christopherhood.net/pdfs/public-spending-in-hard-times.pdf>；<https://civilservant.org.uk/library/2012_Civil-Service-Reform-Context.pdf>
- **#61** 「The ties that bind France and Great Britain at the present moment will have been drawn very much closer.」  
  判断：**错误**。战后英法关系并没有更紧密，鲁尔危机凸显英法之间缺乏信任，双方在对德问题上严重分歧。  
  来源：<https://doi.org/10.1057/9780230510999_4>
- **#62** 「France, Belgium and England will be drifting towards a French-English bi-lingualism」  
  判断：**错误**。英国学校仍以法语为主要外语来教，但英、法、比三国从未走向法英双语社会。  
  来源：<https://education-uk.org/documents/minofed/pamphlet-29.html>；<https://journals.openedition.org/dhfles/4089>
- **#65** 「not a tithe of the war class of undergraduates will ever return」  
  判断：**错误**。战后复员使英国大学学生人数激增，学业中断者大量返校，并非不到十分之一回来。  
  来源：<http://soc-for-ed-studies.org.uk/wp-content/uploads/2022/09/Educational-Access-and-Student-Life-in-the-Aftermath-of-the-Great-War.pdf>；<https://discovery.ucl.ac.uk/id/eprint/10138116/1/Students%20in%20England%20and%20the%20Legacy%20of%20the%20First%20World%20War.pdf>
- **#69** 「There is likely to be something like a truce in the fashions throughout Europe for some years.」  
  判断：**错误**。1919年巴黎时装季就恢复繁华，1920年代时尚发生剧变（短发、短裙、宽松廓形），并未停滞。  
  来源：<https://www.nytimes.com/1919/10/05/archives/reasserting-leadership-as-fashions-capital-paris-elects-the-short.html>；<https://fashionhistory.fitnyc.edu/1920-1929/>
- **#84** 「Against Germany there will certainly be the three great allies, France, Russia and Britain」  
  判断：**错误**。苏俄未受邀参加巴黎和会，坐在谈判桌前的并非法、俄、英三大盟国。  
  来源：<https://en.wikipedia.org/wiki/List_of_participants_in_the_Paris_Peace_Conference_(1919%E2%80%931920)>
- **#89** 「there is a probability that the end of this war may find Poland still divided」  
  判断：**错误**。战争结束时波兰于1918年11月独立建国，并未仍被瓜分。  
  来源：<https://guides.loc.gov/poland-manuscripts/timeline>
- **#92** 「I think that if she does not get it now her gravitation towards it in the future will be so great as to cause …」  
  判断：**错误**。俄国没有得到君士坦丁堡，1946年苏联就海峡问题施压引发危机，但并未因此爆发新战争。  
  来源：<https://moneyweek.com/332694/7-august-1946-turkish-straits-crisis-reaches-its-climax>；<https://en.wikipedia.org/wiki/Treaty_of_Brest-Litovsk>
- **#93** 「I believe she will fight on along the Black Sea coast until she gets there.」  
  判断：**错误**。俄国1918年单独媾和退出战争，从未打下君士坦丁堡。  
  来源：<https://en.wikipedia.org/wiki/Treaty_of_Brest-Litovsk>
- **#96** 「I have, as a balancing prophet, to face the high probability of its outliving me for some generations」  
  判断：**错误**。霍亨索伦帝制1918年11月即告终结，远早于作者去世，更谈不上存续几代人。  
  来源：<https://en.wikipedia.org/wiki/Abdication_of_Wilhelm_II>
- **#121** 「It is improbable that there will be any such revolution as overthrew French Imperialism」  
  判断：**错误**。1918年德国革命推翻了霍亨索伦帝制，类似推翻法兰西第二帝国。  
  来源：<https://en.wikipedia.org/wiki/German_Revolution_of_1918%E2%80%9319>；<https://en.wikipedia.org/wiki/Abdication_of_Wilhelm_II>

### 暂无法判断（9 条）

- **#21** 「the moral effect of these raids has been, and will be, to stiffen the British resolution」  
  判断：**暂无法判断**。检索到的来源只记录了空袭次数和伤亡，没有可靠说明空袭对英国民众意志的总体心理效应，暂无法判断。  
  来源：<https://historicengland.org.uk/research/current/discover-and-understand/military/first-world-war-home-front/air/first-blitz/>；<https://history.blog.gov.uk/2015/01/19/air-raid-casualties-in-the-first-world-war/>
- **#34** 「At the end of the war Great Britain will probably find herself with a national debt so great that she will be …」  
  判断：**暂无法判断**。来源给出英国战前国债约6.45亿英镑、1920年约78亿英镑，但没有给出战后国债年利息与战前全部国家支出的直接对比数字，暂无法判断。  
  来源：<https://api.parliament.uk/historic-hansard/commons/1919/aug/18/national-indebtedness>；<https://www.telegraph.co.uk/news/election-2010/7640349/Geddes-Axe-a-brief-explanation.html>
- **#81** 「in A.D. 2200 there will still be a France, an Ireland, a Germany, a Jugo-Slav region, a Constantinople, a Rajp…」  
  判断：**暂无法判断**。预测终点是公元2200年，截至2026-11-15尚未到期，暂无法判断。  
  来源：<https://en.wikipedia.org/wiki/Timeline_of_national_independence>
- **#98** 「two centuries ahead Russia and the United States will be two of the greatest masses of fairly homogeneous popu…」  
  判断：**暂无法判断**。预测指向两百年后（约2116年），截至2026-11-15尚未到期，暂无法判断。  
  来源：<https://georank.org/population/russia/united-states>
- **#100** 「then the Belgians, French, Americans and English will be doing business in Russia after the war in the German …」  
  判断：**暂无法判断**。这是以西方是否解决俄语教学为条件的预测，俄国革命后条件与情境都已改变，来源无法核对“通过德语经商”，暂无法判断。  
  来源：<https://kingspast.kcl.ac.uk/moments/09/slavonic-school>
- **#103** 「Long before A.D. 2100 there will be no such thing as a "subject race" in all the world.」  
  判断：**暂无法判断**。截至2026年仍有17个非自治领土、不足200万人处于殖民统治之下，期限是2100年前，尚未到期，暂无法判断。  
  来源：<https://www.un.org/en/global-issues/decolonization>
- **#116** 「it will certainly not survive this war.」  
  判断：**暂无法判断**。检索到的来源没有直接衡量战后德国“善战名声”的变化，暂无法判断。  
  来源：<https://www.historytoday.com/archive/stabbed-front>
- **#130** 「I doubt if there will be nearly so much writing and reading about the Great War in the latter half of the twen…」  
  判断：**暂无法判断**。有关一战与拿破仑在不同时期出版量的可比统计不足（仅知拿破仑相关书籍约8万种、比利时一战研究每天超过一本），暂无法判断。  
  来源：<https://en.wikipedia.org/wiki/Bibliography_of_Napoleon>；<https://www.cegesoma.be/en/publication/cent-ans-%E2%80%93-et-plus-%E2%80%93-d%E2%80%99ouvrages-historiques-sur-la-premi%C3%A8re-guerre-mondiale-en-belgique>
- **#132** 「The world will still, in 1950 or so, be throwing much passion into the rights and wrongs of the sinking of the…」  
  判断：**暂无法判断**。没有找到1950年前后有关卢西塔尼亚号争论热度的证据，暂无法判断。  
  来源：<https://www.lrb.co.uk/the-paper/v39/n03/isabel-hull/the-innocence-campaign>；<https://www.theatlantic.com/politics/archive/2015/03/over-there-and-overlooked/387367/>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/wells-what-is-coming-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/wells-what-is-coming-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/wells-what-is-coming-v5/audit/manual_review_2026-11-15.py`

## 说明

- 第 6、17、80、88、91、92、115 条是条件句，前提已经出现，按条件满足计分；第 100 条（若西方不解决俄语教学）的前提无法确认，记为暂无法判断。
- 第 21、34、116、130、132 条在检索证据中找不到能直接核对结果的材料（如空袭对民心的效果、战后国债利息与战前全部支出的对比、卢西塔尼亚号争论在 1950 年的热度），按规则记为暂无法判断，没有勉强判定。
- 抽取时删去了 3 条过于空泛、无法核验的候选（txt-00009“狂热性格增多”、txt-00016“现金付清”、txt-00023“普遍储蓄习惯”），候选中另有 6 条因归属或措辞含糊被流水线降为 unclear，不进入核验。
- 统计以 pipeline.py report 的 summary.json 为准；本表的加权胜率按 manual_report.py 的权重计算。

