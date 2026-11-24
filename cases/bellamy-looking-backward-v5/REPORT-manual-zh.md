# 爱德华·贝拉米《回顾：公元2000—1887年》（Looking Backward）：出版后预测人工核查

- 案例目录：`cases/bellamy-looking-backward-v5/`
- 出版日期：**1888 年 1 月**（Ticknor and Company，波士顿；按 1888 年起算）。正文为 Project Gutenberg #624 英文本（`reading-library/2026-11-15-未来判断书单/06-古典预言文本/40-回顾.txt`，sha256 `ddaf515e…`）。小说虚构的“当下”是 **2000 年**（主人公 1887 年 5 月 30 日入睡，2000 年 9 月 10 日醒来），因此书中对 2000 年社会的描写视为**写明终点为 2000 年**的预言；观察窗口为 1888 年至 2026-11-15，以 2000 年为主要判断时点，并注明此后的发展。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

本稿是按 METHOD.md 的重做版（替代此前助手手工挑选 37 条的旧稿）。抽取：用仓库 prepare_book v5 流水线把全文切成 135 块（3500 字符、600 字符上下文），助手逐块通读、按 DISCOVER_PROMPT_V5 写出模型本应返回的 JSON，再由仓库代码完成引文对齐、归属降级、去重和导入，得到 51 条可核验预测（0.38 条/块）。核验：每条先写 scope，各做一次 support 与 counter 的 Exa 检索，只从检索返回的 URL 中选源，原文存档于 data/sources（sha256），写入 data/evidence.jsonl（107 条），由助手阅读后按四分类规则评断，经 pipeline.py apply assess → check → report。书中人物（Leete 医生、Barton 牧师等）以 2000 年“现状”口吻讲述的内容按“作者借人物之口”计为作者预测。本稿由助手逐条对照书中原文与存档证据人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 51 条，剔除非预测 0 条，计入 **51 条预测**，其中 **50 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 3 |
| 趋势符合 | 6 |
| 部分符合 | 11 |
| 错误 | 30 |
| 暂无法判断 | 1 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **6.0%**（3/50） |
| 加权胜率 | **26.0%** |
| 错误率 | **60.0%**（30/50） |
| 未定占比（暂无法判断/预测） | 2.0%（1/51） |

## 总体评价

技术与生活方式方面贝拉米有几处命中：“信用卡”一词与刷卡消费、经电线/广播在家收听音乐、医师执照制度、女性法官，以及女性大规模就业、高等教育普及、家仆减少、工伤死亡大幅下降等趋势。但书的核心是社会制度预言——全国唯一托拉斯、取消货币和买卖、人人做国家雇员 45 岁退休、没有战争/政党/税收/军队/监狱/律师/广告/经济周期——几乎全部落空，所以错误占可判定预测的六成。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（3 条）

- **#20** 「These halls are connected by telephone with all the houses of the city whose people care to pay the small fee,…」  
  判断：**正确**。1890年代欧洲已有通过电话线收听歌剧的Théâtrophone，1920年代起有经电线传送音乐的Muzak和无线电广播；到2000年家家都能随时收听各类音乐，虽然载体主要是无线电而不是电话线  
  来源：<https://en.wikipedia.org/wiki/Th%C3%A9%C3%A2trophone>；<https://earlyradiohistory.us/sec003.htm>；<https://www.history.com/articles/muzak-invention-army-general>
- **#24** 「None but students who have passed the severe tests of the schools, and clearly proved their vocation, are perm…」  
  判断：**正确**。到1910年美国几乎所有州都设立了医师执照委员会，1910年Flexner报告后医学教育和执照考试日益严格，无证行医成为违法行为  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC7011294/>；<https://www.jmronline.org/content/98/1/20>
- **#49** 「we have women on the bench, appointed by the general of the women, as well as men.」  
  判断：**正确**。女性法官早已出现：Florence Allen成为首位当选司法职务的女性，此后女性陆续进入联邦法院；到2001年联邦法官中约22%是女性  
  来源：<https://www.supremecourt.ohio.gov/courts/judicial-system/supreme-court-of-ohio/justices-1803-to-present/florence-allen/>；<https://teachingamericanhistory.org/document/a-latina-judges-voice-2/>；<https://www.uscourts.gov/data-news/judiciary-news/2015/02/26/women-way-pavers-federal-judiciary>

### 趋势符合（6 条）

- **#4** 「The railroads had gone on combining till a few great syndicates controlled every rail in the land.」  
  判断：**趋势符合**。1893年恐慌后摩根等投资银行主导铁路重组，以“利益共同体”消除竞争，全国干线铁路落入少数几个集团之手；但1904年北方证券案依《谢尔曼法》阻止了进一步合并，并未形成书中那样的完全垄断  
  来源：<https://digfir-published.macmillanusa.com/roark7e/roark7e_ch18_11.html>；<https://www.annenbergclassroom.org/timeline_event/northern-securities-co-v-united-states/>
- **#10** 「The nation does not maim and slaughter its workmen by thousands, as did the private capitalists and corporatio…」  
  判断：**趋势符合**。工伤死亡率在20世纪大幅下降（CDC：1933—1997年下降约90%；OSHA成立后死亡人数又减少六成以上），方向应验；但2000年美国仍有5,915人死于工伤，“不再以千计伤亡”并未实现  
  来源：<https://www.cdc.gov/mmwr/preview/mmwrhtml/mm4822a1.htm>；<https://www.bls.gov/iif/fatal-injuries-tables/archive/census-of-fatal-occupational-injuries-news-release-2000.pdf>
- **#11** 「The schools of technology, of medicine, of art, of music, of histrionics, and of higher liberal learning are a…」  
  判断：**趋势符合**。高等教育大幅普及：NCES数据显示2000年应届高中毕业生的升学率为63%，2016年升至70%；但并非“无条件向所有人开放”，高收入家庭子女升学率（83%）明显高于低收入家庭，学费负担仍是障碍  
  来源：<https://nces.ed.gov/programs/coe/pdf/Indicator_CPA/coe_cpa_2018_05.pdf>；<https://www.americanprogress.org/article/affordability-of-postsecondary-education-equity-and-adequacy-across-the-50-states/>
- **#14** 「a credit card issued him with which he procures at the public storehouses」  
  判断：**趋势符合**。贝拉米首创“credit card”一词；1950年Diners Club推出首张通用信用卡，到2000年刷卡已是主流支付方式。但卡不是国家发放的额度凭证，也没有取代现金  
  来源：<https://www.historyofinformation.com/detail.php?entryid=2044>；<https://www.history.com/articles/when-were-credit-cards-invented>；<https://americanhistory.si.edu/explore/exhibitions/value-money/online/innovations-money/plastic-payments>
- **#23** 「We have no use for domestic servants.」  
  判断：**趋势符合**。20世纪初中产家庭普遍雇佣佣人，此后家电普及、佣人大幅减少，到2000年普通家庭基本不再雇用住家佣人；但家政服务并未消失，富裕家庭和部分城市仍有雇佣  
  来源：<https://daily.jstor.org/how-america-tried-and-failed-to-solve-its-servant-problem/>；<https://journals.sagepub.com/doi/10.1177/0891243207300764>
- **#48** 「Our women, as well as our men, are members of the industrial army, and leave it only when maternal duties clai…」  
  判断：**趋势符合**。女性劳动参与率从1950年的33.9%升到1998年接近60%，女性大规模进入职场、婚后继续工作成为常态；但并非和男性一样全员参加，带婴儿的母亲中工作的比例2000年只有51.0%  
  来源：<https://www.bls.gov/opub/ted/2000/feb/wk3/art03.htm>；<https://www.bls.gov/opub/ted/2001/apr/wk5/art04.htm>

### 部分符合（11 条）

- **#3** 「During the last decade of the century, such small businesses as still remained were fast-failing survivals of …」  
  判断：**部分符合**。1895—1904年的“大兼并浪潮”中，大批原本相互竞争的企业合并为占据主导份额的巨型公司，集中趋势应验；但小企业没有“迅速消亡”，自营业主和小企业主在20世纪仍大量存在  
  来源：<http://naomi-lamoreaux.squarespace.com/the-great-merger-movement>；<https://ciaotest.cc.columbia.edu/olj/ep/ep_jan06/ep_jan06c.pdf>
- **#15** 「the nation guarantees the nurture, education, and comfortable maintenance of every citizen from the cradle to …」  
  判断：**部分符合**。美国建立了社会保障、医疗保险等覆盖失业、贫困、疾病和养老的福利国家制度；但远非“从摇篮到坟墓”的全面保障：2000年仍有14.0%的人全年没有医疗保险  
  来源：<https://archives.history.ac.uk/history-in-focus/welfare/articles/katzm.html>；<https://www.census.gov/library/publications/2001/demo/p60-215.html>
- **#18** 「All our stores are sample stores, except as to a few classes of articles. The goods, with these exceptions, ar…」  
  判断：**部分符合**。“看样下单、仓库发货”的模式在目录展厅零售中出现（Service Merchandise鼎盛时有近350家展厅），后来又有亚马逊式仓配电商；但到2000年普通商店并未普遍改成样品店，Service Merchandise本身也在1999年破产后大批关店  
  来源：<https://www.encyclopedia.com/social-sciences-and-law/economics-business-and-labor/businesses-and-occupations/service-merchandise-company-inc>；<https://jasonmiller15.substack.com/p/why-some-of-this-retailers-leases>；<https://www.aboutamazon.com/news/operations/amazon-fulfillment-center-photo-tour>
- **#21** 「Our washing is all done at public laundries at excessively cheap rates, and our cooking at public kitchens.」  
  判断：**部分符合**。外出就餐确实大幅增加，到21世纪初已占美国食品支出的一半左右，并在2023年达到峰值；但洗衣主要靠家用洗衣机（人口普查局统计绝大多数家庭有洗衣机），做饭也没有普遍交给公共厨房  
  来源：<https://www.ers.usda.gov/media/18720/a-brief-history-of-food-away-from-home-in-the-united-states.pdf?v=41438>；<http://www.ers.usda.gov/data-products/chart-gallery/110112>；<https://www2.census.gov/programs-surveys/well-being/tables/1998/tab01a.pdf>
- **#22** 「Electricity, of course, takes the place of all fires and lighting.」  
  判断：**部分符合**。照明方面基本应验：通电家庭比例由1907年的8%升到1956年的98.8%；但取暖没有“全部改用电力”，2000年用电取暖的家庭只占约30%，燃气占一半以上  
  来源：<https://henryutd2021.github.io/learn/x03-transitions-history.html>；<https://www.census.gov/data/tables/time-series/dec/coh-fuels.html>
- **#26** 「The peaceful relations of these nations are assured by a loose form of federal union of world-wide extent.」  
  判断：**部分符合**。国际联盟（1920）和联合国（1945）先后成立，宗旨正是促进国际合作、维护和平；但它们没有“保障”和平，联合国未能阻止卢旺达、斯雷布雷尼察等惨剧  
  来源：<https://www.un.org/en/about-us/history-of-the-un/predecessor>；<https://digitalcommons.usf.edu/cgi/viewcontent.cgi?article=1141&context=gsp>
- **#29** 「The two minor meals of the day are usually taken at home, as not worth the trouble of going out; but it is gen…」  
  判断：**部分符合**。到20世纪末美国人的饮食重心确已大幅转向外出就餐和外卖；但吃饭的地方是商业餐馆和快餐店，而不是书中设想的社区公共餐厅  
  来源：<https://www.ers.usda.gov/media/18720/a-brief-history-of-food-away-from-home-in-the-united-states.pdf?v=41438>；<https://ers.usda.gov/sites/default/files/_laserfiche/publications/44117/29269_eib19.pdf?v=83611>
- **#32** 「There ensued an era of mechanical invention, scientific discovery, art, musical and literary productiveness to…」  
  判断：**部分符合**。20世纪确实出现了前所未有的发明与科学突破（汽车、电话、相对论、量子力学等迅速改变日常生活）；但这并非书中设想的社会制度变革所激发，文艺“空前繁荣”也难以客观衡量  
  来源：<https://www.sciencenews.org/article/century-scientific-innovation-invention-technology>；<https://en.wikipedia.org/wiki/20th_century_in_science>
- **#34** 「The prices of the staples grow less year by year, but rarely, if ever, rise.」  
  判断：**部分符合**。按实际价格计，1900—2000年消费者支付的食品价格确有下降，食品支出占收入的比重也持续下降；但名义物价并非“逐年下降、几乎从不上涨”，美国CPI在20世纪大幅上升  
  来源：<https://eh.net/encyclopedia/u-s-agriculture-in-the-twentieth-century/>；<https://www2.census.gov/library/publications/2004/compendia/statab/123ed/hist/hs-36.pdf>
- **#35** 「Persons of average constitution usually live to eighty-five or ninety」  
  判断：**部分符合**。寿命显著延长，但“通常活到85—90岁”没有实现：2000年美国出生时预期寿命为76.6岁（女性79.3岁），65岁老人的余寿约18年  
  来源：<https://countryeconomy.com/demography/life-expectancy/usa?year=2000>；<https://www.cdc.gov/nchs/data/nvsr/nvsr51/nvsr51_03.pdf>
- **#50** 「he preaches only by telephone, and to audiences often reaching 150,000.」  
  判断：**部分符合**。远程布道确实出现并拥有巨大听众：1920年代起有广播布道，Billy Graham等人通过电台、电视面向数以百万计的听众；但大多数布道仍在教堂现场进行，约七成美国人仍是教会成员  
  来源：<https://billygrahamlibrary.org/blog-billy-grahams-radio-ministry/>；<https://www.encyclopedia.com/environment/encyclopedias-almanacs-transcripts-and-maps/religious-broadcasting>；<https://news.gallup.com/poll/2974/america-remains-predominantly-christian.aspx>

### 错误（30 条）

- **#1** 「It is nearly a century since the crude method of combustion on which you depended for heat became obsolete.」  
  判断：**错误**。2000年人口普查：美国家庭主要取暖燃料中燃气占51.2%、燃油/煤油9.0%、木柴1.7%，用电取暖只有30.3%；室内燃烧取暖远未“过时”  
  来源：<https://www2.census.gov/programs-surveys/decennial/tables/time-series/coh-fuels/fuels2000.txt>；<https://www.census.gov/data/tables/time-series/dec/coh-fuels.html>
- **#2** 「As no such thing as the labor question is known nowadays」  
  判断：**错误**。劳资冲突并未消失：BLS统计1947—2025年共有11,685起千人以上的大型停工；2000年波音1.7万名工程师罢工，是美国史上最大的白领罢工之一  
  来源：<https://www.bls.gov/wsp/factsheets/summary-of-work-stoppages-in-the-united-states.htm>；<https://www.latimes.com/archives/la-xpm-2000-feb-10-fi-62793-story.html>
- **#5** 「Early in the last century the evolution was completed by the final consolidation of the entire capital of the …」  
  判断：**错误**。受本书启发的“民族主义俱乐部”曾在1880年代末兴起（至少165个），但很快衰落；美国20世纪始终是以私营企业为主的市场经济，全部资本从未收归国家  
  来源：<https://en.wikipedia.org/wiki/Nationalist_Clubs>；<https://usa.usembassy.de/etexts/oecon/chap2.htm>
- **#6** 「We have no wars now, and our governments no war powers」  
  判断：**错误**。1945年后大国之间确有“长期和平”，但战争并未消失：1990年代美国参与了海湾战争、索马里、科索沃等冲突，各国政府仍保有战争权力  
  来源：<https://en.wikipedia.org/wiki/List_of_wars_involving_the_United_States_in_the_20th_century>；<https://2001-2009.state.gov/r/pa/ho/time/pcw/index.htm>；<https://en.wikipedia.org/wiki/Long_Peace>
- **#7** 「We have no parties or politicians, and as for demagoguery and corruption, they are words having only an histor…」  
  判断：**错误**。2000年美国大选仍是共和党布什与民主党戈尔对决，政党和职业政客照旧主导政治  
  来源：<https://www.archives.gov/electoral-college/2000>；<https://www.presidency.ucsb.edu/statistics/elections/2000>
- **#8** 「When the nation became the sole employer, all the citizens, by virtue of their citizenship, became employees」  
  判断：**错误**。2000年人口普查补充调查：只有约14%的就业者是联邦、州或地方政府雇员（约1800万人），绝大多数人受雇于私营部门  
  来源：<https://www.prb.org/resources/the-size-and-shape-of-americas-government/>；<https://www.bls.gov/opub/mlr/2004/10/art3full.pdf>
- **#9** 「The period of industrial service is twenty-four years, beginning at the close of the course of education at tw…」  
  判断：**错误**。美国并没有45岁退休的制度：1990—1995年男性平均退休年龄约62.2岁，社会保障的全额退休年龄为65岁并逐步提高到67岁  
  来源：<http://www.bls.gov/opub/mlr/2000/07/art2full.pdf>；<https://www.ssa.gov/benefits/retirement/planner/ageincrease.html>
- **#12** 「There is neither selling nor buying nowadays; the distribution of goods is effected in another way.」  
  判断：**错误**。到2000年买卖和商店照旧存在：人口普查局的年度零售报告统计了数以百万计的零售企业和数万亿美元的零售额  
  来源：<https://www2.census.gov/retail/releases/benchmark/annpub00.pdf>；<https://www2.census.gov/library/publications/2008/compendia/statab/128ed/tables/09s1017.pdf>
- **#13** 「As to the bankers, having no money we have no use for those gentry.」  
  判断：**错误**。货币和银行没有消失：美联储统计的流通中现金在20世纪持续增长；直到2026年仍有约58%的美国人每周用现金付款，只是用现金的人在减少  
  来源：<https://www.federalreserve.gov/newsevents/testimony/roseman20100720a_accessible.htm>；<https://www.pewresearch.org/short-reads/2026/08/26/fewer-americans-use-cash-today-than-a-decade-ago-but-many-still-carry-it/>
- **#16** 「we have nothing at all answering to your idea of wages.」  
  判断：**错误**。工资制度依旧，收入差距很大：2000年美国家庭收入基尼系数为0.460，显著高于此前多数年份；1990年代高收入者与中间层差距继续拉大  
  来源：<https://www2.census.gov/library/publications/2001/demographics/p60-213.pdf>；<https://www.epi.org/publication/books_swa2000_swa2000intro/>
- **#17** 「though we have abolished poverty and the fear of it, and inordinate luxury with the hope of it」  
  判断：**错误**。贫困没有被消灭：2000年美国有3,110万人（11.3%）生活在官方贫困线以下  
  来源：<https://www.bls.gov/cps/cpswp2000.htm>；<https://www.census.gov/library/publications/2001/demo/p60-214.html>
- **#19** 「The packages are then delivered by larger tubes to the city districts, and thence distributed to the houses.」  
  判断：**错误**。1890年代起费城、纽约等城市确曾用地下气动管道传送信件，但只限邮局之间的信件，后来被停用；到2000年商品从未通过管道网络送到各家各户  
  来源：<https://postalmuseum.si.edu/exhibition/customers-and-communities-serving-the-cities-city-free-delivery/pneumatic-tube-mail>；<https://www.smithsonianmag.com/history/when-a-labyrinth-of-pneumatic-tubes-shuttled-mail-beneath-the-streets-of-new-york-city-180983472/>
- **#25** 「the great nations of Europe as well as Australia, Mexico, and parts of South America, are now organized indust…」  
  判断：**错误**。欧洲各国战后实行的是“混合经济+福利国家”，并非国家统一经营全部产业；1980—1990年代西欧还普遍推行私有化  
  来源：<https://www.cambridge.org/core/books/abs/an-economic-history-of-twentiethcentury-europe/mixed-economy-and-welfare-state-in-an-integrated-postworld-war-ii-western-europe/E>；<https://feem-media.s3.eu-central-1.amazonaws.com/wp-content/uploads/NDL2006-124.pdf>
- **#28** 「Subject to these regulations, the right of any man to emigrate at any time is unrestricted.」  
  判断：**错误**。1948年《世界人权宣言》第13条承认“离开任何国家”的权利，但入境移民普遍受限：美国1924年起实行国别配额，各国至今仍严格管控移民  
  来源：<https://www.ohchr.org/en/human-rights/universal-declaration/translations/english>；<https://history.state.gov/milestones/1921-1936/immigration-act>
- **#30** 「She said to me that at the present time all the streets were provided against inclement weather in the manner …」  
  判断：**错误**。城市街道没有普遍加装可收放的防雨顶棚；只有少数城市建有局部连廊，例如明尼阿波利斯1962年起建的空中走廊系统（约80个街区）  
  来源：<https://www.mnhs.org/mnopedia/search/index/structure/minneapolis-skyways>；<https://www.minneapolis.org/map-transportation/minneapolis-skyway-guide/>
- **#31** 「The equal wealth and equal opportunities of culture which all persons now enjoy have simply made us all member…」  
  判断：**错误**。财富与阶层差距没有消失：美联储数据显示1989—2016年最富1%家庭的财富份额持续上升；教育虽大幅普及，但教育不平等依然存在  
  来源：<https://www.federalreserve.gov/econres/notes/feds-notes/wealth-concentration-levels-and-growth-1989-2016-accessible-20200220.htm>；<https://www.pnas.org/doi/full/10.1073/pnas.1907258117>
- **#33** 「The people who take the paper pay the expense of its publication, choose its editor, and remove him when unsat…」  
  判断：**错误**。到2000年美国报纸仍是私人商业经营、主要依靠广告：当年报纸广告支出达487亿美元，报业还在不断集中；订户出资并选举编辑的合作社报纸只是2010年代才出现的零星个案  
  来源：<https://www.mediapost.com/publications/article/11138/ad-spending-in-newspapers-hit-487-billion-in-200.html>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC12714153/>
- **#36** 「The professional sportsmen, which were such a curious feature of your day, we have nothing answering to」  
  判断：**错误**。职业体育反而高度商业化：2000年美国职棒大联盟球员平均年薪升至约190万美元；奥运会也在1980年代后逐步向职业运动员开放并设奖金  
  来源：<http://cgi.usatoday.com/sports/baseball/salary/00final.htm>；<https://www.reuters.com/sports/key-moments-path-amateurism-professionalism-2024-04-10/>
- **#37** 「We have no jails nowadays. All cases of atavism are treated in the hospitals.」  
  判断：**错误**。监狱没有消失，反而急剧扩张：2000年底美国州和联邦监狱关押138万人，监禁率从1980年的每10万人139人升到2000年的478人  
  来源：<https://bjs.ojp.gov/content/pub/pdf/p00.pdf>；<https://www.justice.gov/archive/mps/strategic2001-2006/d_incrt.htm>
- **#38** 「We do without the lawyers, certainly」  
  判断：**错误**。律师职业大幅扩张：1900—2000年美国律师人数从114,460人增至100多万，增长793%  
  来源：<https://www.americanbar.org/news/profile-legal-profession/demographics/>；<https://www.americanbarfoundation.org/wp-content/uploads/2023/05/2005_lawyer_statistical_report.pdf>
- **#39** 「We have no army or navy, and no military organization.」  
  判断：**错误**。美国2000财年现役士兵约115万人（仅士兵），国防拨款数千亿美元，陆海军依然庞大  
  来源：<https://www.cna.org/pop-rep/2000/html/chapter3/chapter3.htm>；<https://www.everycrsreport.com/files/19991027_RL30205_2175ae2e3789a83c62acbcdffb6cc4d241ccc85a.html>
- **#40** 「We have no departments of state or treasury, no excise or revenue services, no taxes or tax collectors.」  
  判断：**错误**。财政部和国务院依然存在，国税局2000财年征收了上万亿美元税款，税收和税务人员并未消失  
  来源：<https://www.irs.gov/pub/irs-soi/00databk.pdf>；<https://home.treasury.gov/about/history/history-overview/history-of-the-treasury>
- **#41** 「We have no legislation," replied Dr. Leete, "that is, next to none.」  
  判断：**错误**。立法没有消失：第106届国会（1999—2000年）制定了580项法律；各州议会也一直存在并持续运作  
  来源：<https://en.wikisource.org/wiki/Portal:Acts_of_the_United_States_Congresses/Acts_of_the_106th_United_States_Congress>；<https://www.governing.com/politics/the-evolution-of-state-legislatures-throughout-u-s-history>
- **#42** 「We have simply added to the common school system of compulsory education, in vogue in Massachusetts a hundred …」  
  判断：**错误**。2000年各州义务教育上限一般为16—18岁，并未延长到21岁；2000年人口普查时25岁以上人口中80%有高中及以上学历，但远非人人接受高等教育  
  来源：<https://nces.ed.gov/programs/digest/d02/tables/PDF/table150.pdf>；<https://www2.census.gov/library/publications/decennial/2000/briefs/c2kbr-24.pdf>
- **#43** 「Insanity, for instance, which in the nineteenth century was so terribly common a product of your insane mode o…」  
  判断：**错误**。精神疾病和自杀没有绝迹：美国1990—2003年精神障碍患病率稳定在约30%；CDC统计2000年起年龄调整自杀率每年仍有数万人死亡并在此后上升  
  来源：<https://www.nejm.org/doi/full/10.1056/NEJMsa043266>；<https://www.cdc.gov/nchs/data/databriefs/db309%5Ftable.pdf>
- **#44** 「We have no national, state, county, or municipal debts, or payments on their account.」  
  判断：**错误**。各级政府都背负公共债务：2000年联邦债务达数万亿美元，人口普查局另有州和地方政府债务统计  
  来源：<https://www.govinfo.gov/content/pkg/BUDGET-2002-TAB/pdf/BUDGET-2002-TAB-9-1.pdf>；<https://www.census.gov/data/datasets/2000/econ/local/public-use-datasets.html>
- **#45** 「Our statisticians calculate that one eightieth part of our workers suffices for all the processes of distribut…」  
  判断：**错误**。流通环节的就业比重不降反升：零售业占美国民用就业的比例从1958年的12.6%升到2000年的16.4%，加上批发业约5%，远高于“八十分之一”  
  来源：<https://www2.census.gov/ces/wp/2005/CES-WP-05-30.pdf>；<https://www.bls.gov/careeroutlook/2001/Winter/art04.pdf>
- **#46** 「Except for slight occasional effects of such natural causes, there are no fluctuations of business」  
  判断：**错误**。商业周期没有消失：NBER持续记录20世纪的历次经济衰退，2001年3月美国又进入一轮衰退  
  来源：<https://www.nber.org/research/data/us-business-cycle-expansions-and-contractions>；<https://www.nber.org/news/business-cycle-dating-committee-announcement-november-26-2001>
- **#47** 「Then the national party arose to carry it out by political methods.」  
  判断：**错误**。受本书影响的民族主义运动与1890年代人民党有所交集，社会党在1912年也曾在一些城市获胜；但没有任何以国有化全部生产为目标的政党赢得全国多数，书中设想的变革从未实现  
  来源：<https://edwardbellamyhouse.org/2022/10/31/talking-politics-edward-bellamy-populism-and-the-election-of-1892/>；<https://en.wikipedia.org/wiki/Socialist_Party_of_America>
- **#51** 「There had been no personal advertising in the Boston of the twentieth century, because there was no need of an…」  
  判断：**错误**。商业广告非但没有消失，反而长期维持在GDP的约2%，2026年美国广告总支出估计约3,610亿美元  
  来源：<https://www.econlib.org/library/Enc/Advertising.html>；<https://content.ibisworld.com/media/twpnf2mv/total-advertising-expenditure-total-advertising-expenditure-business-environment-profile-by-ibisworld.pdf>

### 暂无法判断（1 条）

- **#27** 「we all look forward to an eventual unification of the world as one nation.」  
  判断：**暂无法判断**。书中把世界统一为一国说成即便到2000年也仍是“最终”的远景，没有给出时间；至今联合国有193个成员国，世界联邦运动在1950年代后衰落，远景仍未到期，无法判断  
  来源：<https://research.un.org/en/unmembers/intro>；<https://www.thefederalist.eu/site/index.php/en/essays/1892-the-world-federalist-movements-from-1945-to-1954-and-european-integration>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/bellamy-looking-backward-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/bellamy-looking-backward-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/bellamy-looking-backward-v5/audit/manual_review_2026-11-15.py`

## 说明

- 第 27 条（世界最终统一为一国）在书中即便到 2000 年也仍是远景，没有给出时间，记为暂无法判断。
- 第 32 条（20 世纪发明高潮）结果出现，但书中把它归因于社会变革，这个原因并未出现，所以记部分符合。
- 统计以 pipeline.py report 的 summary.json 为准；本表的加权胜率按 manual_report.py 的权重计算。

