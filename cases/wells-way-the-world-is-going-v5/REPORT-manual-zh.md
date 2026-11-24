# H. G. 威尔斯《世界的走向：对未来岁月的猜测与预测》（The Way the World Is Going: Guesses & Forecasts of the Years Ahead，1928）：出版后预测人工核查

- 案例目录：`cases/wells-way-the-world-is-going-v5/`
- 出版日期：各篇于 1927 年在《纽约时报杂志》等报刊连载，1928 年由 Ernest Benn（伦敦）结集出版。正文取自 Project Gutenberg #77242 纯文本（据 1929 年 Doubleday 版；与队列记录 sha256 `6249a53f…` 逐字节一致，499,470 字节；按工具包读取为 497,376 字符），原样使用，不做转换。观察窗口为 1928 至 2026-11-15（以 1928 为出版年代理；文中各篇写于 1927 年）。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

按 METHOD.md 执行。抽取：用仓库 prepare_book v5 流水线（85e6da1 工具包）把全文（497,376 字符）切成 144 块（每块 3500 字符，带 600 字符上下文；第 139—144 块为全书结尾与 Gutenberg 许可文本）。助手逐块通读，没有用关键词筛选，按 DISCOVER_PROMPT_V5 写出模型本应返回的 JSON（未调用 DeepSeek），再由仓库代码完成引文对齐、归属降级、去重和导入：共 69 条候选，其中 43 条为可核验预测，26 条为 unclear（格言、价值判断、同一主题的重复表述等），另有 3 条格言、2 条琐碎陈述被排除。同一主题（民主衰落、有组织团体、广播、航空、劳工等）只保留一条，避免拆分放大胜率。核验：每条先写 scope，各做一次 support 与 counter 的 Exa 检索，第 5 条追加一轮检索，共 88 次检索；只从检索返回的 URL 中选源。原文用 Exa contents 抓取（失败时 curl 兜底）存档于 data/sources（91 份，sha256），写入 data/evidence.jsonl（91 条）；理由中的数字均已在存档文本中核对。助手阅读后按“正确／趋势符合／部分符合／错误／暂无法判断”规则逐条评断，再经 pipeline.py apply assess → check → report。本稿由助手逐条对照书中原文与存档证据人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 43 条，剔除非预测 0 条，计入 **43 条预测**，其中 **42 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 12 |
| 趋势符合 | 4 |
| 部分符合 | 14 |
| 错误 | 12 |
| 暂无法判断 | 1 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **28.6%**（12/42） |
| 加权胜率 | **52.4%** |
| 错误率 | **28.6%**（12/42） |
| 未定占比（暂无法判断/预测） | 2.3%（1/43） |

## 总体评价

威尔斯对社会与人口长期走向的判断较准：几乎所有孩子都能活到成年、人口老龄化、婚姻制度现代化、美国大力扩张教育、德国在联合的欧洲中占据重要地位、大英帝国瓦解、法西斯党继续统治意大利直到 1943 年、不太遥远的将来爆发大战、“赤色分子”成为猎巫对象、发达工业国没有发生劳工革命，都已应验。小家庭、体力劳动阶层萎缩、工业心理学兴起、街头扩音器受立法限制只确认了方向。部分符合的多是前半对、后半错，或时间与机制不对：结婚推迟和寿命延长都晚于“不久的将来”，二战后共产主义扩展靠的是占领而非世界革命，世界气象组织建成了但没能提前多年预报收成。判错的集中在政治与技术的近期判断：大国强人独裁并未终结，意大利没有沦为欧洲贫民窟、此后十年也未被边缘化，STV 成为爱尔兰、马耳他的选举制度，议会政治没有消失，工党 1929 年再次以少数党执政，苏联没有在几十年内被摧毁，航空业和广播业都在高速发展，伦敦也没有在开战几小时内遭毒气攻击。鲍德温“再执政五年”的条件没有触发，该条未判定。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（12 条）

- **#1** 「It points forward to a time when nearly every child born into a civilized community will live to maturity.」  
  判断：**正确**。发达社会几乎每个孩子都能活到成年已成现实：Our World in Data指出历史上约1/2的新生儿活不到15岁，此后大幅下降；2024年G10国家5岁以下儿童死亡率平均为每1000名活产4例，最高的美国也只有7例  
  来源：<https://ourworldindata.org/child-mortality>；<https://www.theglobaleconomy.com/rankings/child_mortality/G10/>
- **#5** 「a state of society, in fact, in which the average man and woman will be of riper years」  
  判断：**正确**。人口老龄化已发生：2020年欧盟65岁及以上人口占20.6%，比十年前高3.0个百分点；2020年欧洲人口中位年龄为42.5岁  
  来源：<https://ec.europa.eu/eurostat/web/products-eurostat-news/-/ddn-20210316-1>；<https://www.populationpyramid.net/europe/2020/>
- **#10** 「this romantic, magnificent, patriotic Fascist Party, so exalted and devoted in its professions, will continue …」  
  判断：**正确**。法西斯党此后继续牢牢控制意大利：法西斯政权从1922年10月延续到1943年7月25日墨索里尼被法西斯大委员会投票罢黜，书出版后又统治了十多年  
  来源：<https://en.wikipedia.org/wiki/Fascist_Italy>；<https://encyclopedia.ushmm.org/content/en/article/italy>
- **#13** 「She may blunder into a disastrous war, or she may develop sufficient social misery to produce a chaotic social…」  
  判断：**正确**。意大利确实卷入灾难性战争：其武装力量“带着惶恐进入二战，以屈辱告终”，在地中海、东线等多条战线接连失利，1943年墨索里尼倒台  
  来源：<https://doi.org/10.1017/cbo9780511762970.006>；<https://en.wikipedia.org/wiki/Military_history_of_Italy_during_World_War_II>
- **#18** 「Everybody in Parliament knows that Coalition waits at the end of the passage even if a second election interve…」  
  判断：**正确**。联合政府最终出现：1929年工党少数派政府在1931年财政危机中垮台，麦克唐纳组成有保守党、自由党参加的国民政府（联合政府）  
  来源：<https://www.encyclopedia.com/history/encyclopedias-almanacs-transcripts-and-maps/national-government>；<https://en.wikipedia.org/wiki/National_Government_(1931)>
- **#19** 「To-day there are many signs that the “Red” has a good chance of playing the part of the witch of older times i…」  
  判断：**正确**。“赤色分子”确实成了新的“女巫”：二战后美国第二次红色恐慌（麦卡锡主义）被普遍称为猎巫；1950年2月麦卡锡声称掌握205名国务院共产党员名单  
  来源：<https://www.gilderlehrman.org/history-resources/essays/anti-communism-1950s>；<https://www.eisenhowerlibrary.gov/research/online-documents/mccarthyism-red-scare>
- **#21** 「I do not believe that under modern conditions, in a modern mechanicalized State, common low-grade labour is ca…」  
  判断：**正确**。发达工业国没有发生劳工革命：研究者指出几十年来社会主义者一直在解释为何先进资本主义国家没有发生革命；共产主义革命发生在俄国、中国等以农业为主的国家  
  来源：<https://doi.org/10.4324/9781003408048-1>；<https://newleftreview.org/issues/ii61/articles/perry-anderson-two-revolutions>
- **#25** 「a British Empire which does not seem to me to be realizing the wide and generous dreams of the liberal imperia…」  
  判断：**正确**。大英帝国没有延续：1947年印度独立、英属印度分治，BBC称英国的帝国权力到20世纪60年代中期已基本瓦解  
  来源：<https://www.bbc.co.uk/history/british/modern/endofempire_overview_01.shtml>；<https://www.iwm.org.uk/history/second-world-war/india/partition>
- **#29** 「Germany to-day is much more likely to take a great place in a united Europe than she ever was before」  
  判断：**正确**。德国在联合的欧洲中占据重要地位：1951年德国是欧洲煤钢共同体创始成员；2025年德国是欧盟最大经济体，GDP达4.5万亿欧元，占欧盟总量的23.8%  
  来源：<https://www.deutschland.de/en/topic/politics/germanys-role-in-the-eu-ten-facts-and-figures>；<https://ec.europa.eu/eurostat/web/products-eurostat-news/w/wdn-20260806-1>
- **#30** 「the processes that will inevitably develop into warfare in the not very remote future」  
  判断：**正确**。不太遥远的将来果然爆发战争：1939年9月1日德国入侵波兰，引发第二次世界大战，距写作约12年  
  来源：<https://encyclopedia.ushmm.org/content/en/article/invasion-of-poland-fall-1939>；<https://www.iwm.org.uk/history/second-world-war/causes>
- **#39** 「This dispute at Denver is certainly only one of the opening incidents in a very wide and far-reaching movement…」  
  判断：**正确**。婚姻制度确实迎来广泛的修订和现代化：1969年加州通过美国首部无过错离婚法，随后迅速推广到除纽约以外的各州，纽约后来也跟进；西方家族法在半个多世纪里大幅改革  
  来源：<https://www.abajournal.com/magazine/article/and_then_there_was_none>；<https://research.vu.nl/en/publications/50-years-of-developments-in-family-law-in-the-westernised-world-t/>
- **#40** 「the growing volume of self-criticism in America, of which the books I have cited are only samples, is a very h…」  
  判断：**正确**。美国确实大力补上教育短板：1910—1940年美国青年中学在读比例从18%升到71%，毕业比例从9%升到51%，1920—1935年尤其迅速；20世纪高等教育随之大规模扩张  
  来源：<https://doi.org/10.3386/w10075>；<https://scholar.harvard.edu/files/goldin/files/americas_graduation.pdf>

### 趋势符合（4 条）

- **#3** 「he will have a small, successful family」  
  判断：**趋势符合**。小家庭方向得到确认：OECD平均总和生育率从1960年的每名妇女3.3个孩子降到2022年的1.5个；但中途有战后婴儿潮，美国总和生育率1957年达到3.77的峰值，并非一路走向小家庭  
  来源：<https://www.oecd.org/en/publications/society-at-a-glance-2024_918d8db3-en/full-report/fertility-trends-across-the-oecd-underlying-drivers-and-the-role-for-policy_770679b8.html>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC6973346/>
- **#23** 「There is a growing science of industrial psychology and industrial efficiency. It is, I believe, likely to dev…」  
  判断：**趋势符合**。工业心理学确实成长为有影响力的学科：《牛津手册》综述其从19世纪末发展为复杂、广泛的学科；20世纪20年代起的霍桑研究催生人际关系运动，改变了以科学管理为主导的管理范式。“非常强大”难以量化，只认定方向  
  来源：<https://doi.org/10.1093/oxfordhb/9780199928309.013.0002>；<https://www.library.hbs.edu/hc/hawthorne/anewvision.html>
- **#24** 「In the long run it seems probable that the sort of thing we understand by “Labour” now will dwindle to a small…」  
  判断：**趋势符合**。体力劳动阶层在萎缩：美国蓝领岗位占非农就业的比例从1970年的31.2%降到2016年的13.6%；1950年近31%的非农就业在制造业，此后持续下降。但尚未缩成“很小、不重要”的阶层  
  来源：<https://cepr.net/publications/the-decline-of-blue-collar-jobs-in-graphs/>；<https://www.chicagofed.org/publications/blogs/midwest-economy/2010/isusmanufacturing>
- **#33** 「The bawling of loud speakers, as I have heard it in the streets of some French towns, is so obviously disconce…」  
  判断：**趋势符合**。街头高音喇叭确被立法限制：英国1974年《污染控制法》规定晚9点至早8点不得在街头使用扩音器，任何时间不得用于广告；美国路易斯维尔1931年也通过规制广告用扩音器的条例。但仍是限制而非全面禁止  
  来源：<https://www.york.gov.uk/noise-pollution/loudspeakers-causing-noise>；<https://www.courtlistener.com/opinion/3446488/brachey-judge-v-maupin/>

### 部分符合（14 条）

- **#2** 「In the near future, on the contrary, man will not work until he is adult; he will marry much later」  
  判断：**部分符合**。“结婚大大推迟”只在长期上应验：美国女性初婚年龄1890年为22.0岁，1956年降到20.1岁的最低点，之后才持续上升到2025年的28.4岁；“不久的将来”反而先出现提早结婚，“成年后才工作”一项未单独核实  
  来源：<https://www.khoury.northeastern.edu/home/rachlin/somai/stories/when-america-married-youngest/Karina_Advani_Data-Website_Page1.html>；<https://www.pbs.org/fmc/book/4family1.htm>
- **#4** 「The average active human life, we may conclude, in the quite near future, will be not only unencumbered but pr…」  
  判断：**部分符合**。活跃寿命确实延长：OECD称自20世纪中叶以来多数OECD国家预期寿命持续上升，斯坦福研究显示活过65岁者的寿命每代约增加3年；但书中寄望的施泰纳赫式“返老还童”手术被证明无效，且延长主要发生在“相当近的将来”之后  
  来源：<https://www.oecd.org/en/publications/mortality-and-the-provision-of-retirement-income_a10a6c09-en/full-report/component-3.html>；<https://news.stanford.edu/stories/2018/11/lifespan-increasing-people-live-65>；<https://www.auajournals.org/doi/10.1016/j.juro.2011.10.134>
- **#7** 「one in Russia, and now another over the larger half of China, which bid fair to spread over the entire breadth…」  
  判断：**部分符合**。党治国家在亚洲确有扩展：中国1949年建立人民共和国，亚洲还出现蒙古、朝鲜、越南等共产党执政国家，与苏联连成一片；但书中寄望的国民党与苏联合流在1927年4月的上海清党中破裂，且党治政府并未覆盖整个亚洲  
  来源：<https://history.state.gov/milestones/1945-1952/chinese-rev>；<https://www.cmcarchive.org/events/shanghai-massacre-1927>；<https://scholarlycommons.law.case.edu/cgi/viewcontent.cgi?article=1870&context=jil>
- **#8** 「What is now drilled and disciplined as Fascism existed before him and will go on after him.」  
  判断：**部分符合**。法西斯主义在墨索里尼之后以新法西斯形式延续：曾在意大利社会共和国效力的法西斯分子于1946年创立意大利社会运动（MSI），兄弟党即源于此；但1948年宪法第十二条禁止以任何形式重建法西斯党，MSI于1995年解散，有组织的法西斯运动只以边缘或转型形态存续  
  来源：<https://www.treccani.it/enciclopedia/movimento-sociale-italiano/>；<https://www.senato.it/istituzione/la-costituzione/disposizioni-transitorie-e-finali/xii>；<https://www.upi.com/Archives/1995/01/28/Italys-hard-right-dissolves-fascist-past/1080791269200/>
- **#9** 「organized brotherhoods, maintaining a certain uniformity of thought and action over large areas and exacting a…」  
  判断：**部分符合**。前段应验：《Annual Review》指出20世纪下半叶一党专制空前扩张，成为最常见的威权统治类型；但20世纪80年代末起，非洲等地一党制纷纷让位于多党政治，“日益重要”并未持续到截止日  
  来源：<https://www.annualreviews.org/content/journals/10.1146/annurev.polisci.031908.220529>；<https://www.cambridge.org/core/books/abs/democracy-in-africa/second-liberation-economic-decline-the-end-of-the-cold-war-and-the-struggle-for-democracy/C916D53037634308580EF71E563823AF>
- **#22** 「Something like a world revolution may occur in the smash that may follow another great war, a greater Soviet e…」  
  判断：**部分符合**。条件（又一场大战）已出现，后果部分应验：二战后苏联在中东欧扶植共产党政权，中国1949年建立人民共和国，苏维埃式体制大幅扩展；但这主要靠苏军占领和内战，而非类似“世界革命”的普遍崩溃  
  来源：<https://www.encyclopedia.com/history/encyclopedias-almanacs-transcripts-and-maps/eastern-bloc>；<https://history.state.gov/milestones/1945-1952/chinese-rev>；<https://academic.oup.com/book/40007/chapter/340343478>
- **#31** 「wars in the future, even at the outset, will not be undertaken with the gusto with which we all set about the …」  
  判断：**部分符合**。对二战成立：1939年开战时德国民众是“勉强的忠诚”，没有1914年那样的欢呼人群（SOPADE报告称没有战争热情）；但原文泛指“未来的战争”，证据只覆盖二战，且“1914年狂热”本身被史学界指为部分神话  
  来源：<https://germanhistorydocs.org/en/nazi-germany-1933-1945/sopade-report-no-war-enthusiasm-september-october-1939>；<https://www.bbc.co.uk/bitesize/guides/z3h7bk7/revision/1>；<https://journals.sagepub.com/doi/10.1177/0968344516650476>
- **#35** 「There is a future for the wireless news ticker」  
  判断：**部分符合**。无线新闻接收打印设备有一定发展：赫尔无线电传打字机1929—1930年获专利，挪威通讯社1934年起用它接收国外新闻；但面向家庭的“无线电传真报纸”在20世纪30、40年代试验后未能普及  
  来源：<https://www.hellschreiber.com/pdf-hell/hell-presse-NTB-12b.pdf>；<https://doi.org/10.1080/08838151.2011.597471>
- **#36** 「That vertical city of the future we know now is, to put it mildly, highly improbable.」  
  判断：**部分符合**。人口和产业向外疏散得到确认：美国都市区居民住在中心城市的比例从1950年的56%持续下降，20世纪郊区增长远快于城市；但高层“垂直城市”在香港等地大量出现，“极不可能”不完全成立  
  来源：<https://www.nber.org/system/files/working_papers/w16435/revisions/w16435.rev0.pdf>；<https://caf.ctbuh.org/wp-content/uploads/2024/12/2024-Vertical-Urbanism-Index-Report-1.pdf>
- **#37** 「we shall probably find that there also the conditions of machine production have evoked a new town population …」  
  判断：**部分符合**。识字和城市化部分应验：1939年苏联人口普查显示城市人口比1926年翻了一番多，从26.3 million增至55.9 million，识字率也上升；但1932年起实行国内护照和城市户籍，1938—1940年收紧劳动纪律，工人的自由与西方工人不可同日而语  
  来源：<https://en.wikipedia.org/wiki/1939_Soviet_census>；<https://shs.cairn.info/journal-cahiers-du-monde-russe-2001-2-page-477?lang=en>；<http://cyberussr.com/rus/labor-discip.html>
- **#38** 「The common man in quite a little space of years may be better off than are even the fortunate few to-day.」  
  判断：**部分符合**。短期不成立，长期部分成立：大萧条期间33个城市家庭平均收入下降24%至51%；长期看，发达国家普通人的生活水平大幅提高，但现有证据比较的是19世纪王室，不是写作当时的少数幸运者  
  来源：<https://www.nber.org/system/files/chapters/c5307/c5307.pdf>；<https://www.adamsmith.org/blog/the-average-today-is-higher-than-the-living-standard-of-19th-century-royalty>
- **#41** 「In quite a few years we shall know within quite small limits the population of the world and its rate of incre…」  
  判断：**部分符合**。后来确实能较准确地掌握世界人口：联合国1946年开始收集各国人口数据，得出1950年全球人口约2.47 billion，1951年发布首版人口展望；但这是写作约二十年后，而且人口普查仍有漏报误差，需要估算修正  
  来源：<https://en.wikipedia.org/wiki/World_Population_Prospects>；<https://www.un.org/development/desa/pd/sites/www.un.org.development.desa.pd/files/files/documents/2020/Oct/undesa_pd_tp_2020_tp_population_estimates.pdf>
- **#42** 「the little scattered band of meteorologists who now observe and guess about the weather will have been reinfor…」  
  判断：**部分符合**。世界性气象组织已建成：国际气象组织于1950年3月23日改组为世界气象组织（WMO），1963年建立世界天气监视网；但书中设想的提前多年预测收成与短缺并未实现  
  来源：<https://wmo.int/about-us/history-of-imo-and-wmo>；<https://wmo.int/site/world-meteorological-day-2026/how-does-observing-system-work>
- **#43** 「unless Britain can rouse itself--within a very brief term of years--to meet the irksome demand for more knowle…」  
  判断：**部分符合**。“英国是否振作”这一前提无法客观判定；后果部分出现：英国人均GDP相对法、德、美长期下降，但1997—2010年英国人均GDP年增1.42%，好于其他G6国家，“永久”落后不完全成立  
  来源：<https://cepr.org/voxeu/columns/mrs-thatchers-economic-legacy>；<https://cep.lse.ac.uk/pubs/download/cp366.pdf>

### 错误（12 条）

- **#6** 「The days of great adventurers seem to be past in any country larger than Italy」  
  判断：**错误**。比意大利大的国家并未告别强人独裁：本书写成后希特勒、斯大林、毛泽东等在大国建立个人崇拜式统治，History Today称希特勒、墨索里尼、毛、斯大林等人的画像遍布各地  
  来源：<https://www.historytoday.com/archive/feature/great-dictators>；<https://www.encyclopedia.com/history/modern-europe/russian-soviet-and-cis-history/cult-personality>
- **#11** 「until at last the peninsula will be plainly the industrial slum of Europe」  
  判断：**错误**。意大利没有沦为欧洲的工业贫民窟：研究指出1950年后意大利经济显著发展，起点人均GDP比同类国家低约40%，随后的“经济奇迹”使其跻身发达工业国  
  来源：<https://iris.uniupo.it/handle/11579/122773>；<https://en.wikipedia.org/wiki/Italian_economic_miracle>
- **#12** 「In the attempts to consolidate European affairs that will be going on in the next decade, Italy will be watche…」  
  判断：**错误**。此后十年意大利并未被边缘化：1933年英、法、意、德四国公约由墨索里尼提议并在罗马签署；1935年4月英法意首脑在意大利斯特雷萨会晤，组成斯特雷萨阵线  
  来源：<https://en.wikipedia.org/wiki/Four-Power_Pact>；<https://en.wikipedia.org/wiki/Stresa_Front>
- **#14** 「there is not the slightest chance of its ever becoming, except perhaps in name and with essential mutilations,…」  
  判断：**错误**。单记可让渡投票（STV）成为现代国家的立法选举方式：ACE项目指出爱尔兰自1921年、马耳他自1947年起用STV选举议会，澳大利亚参议院也采用  
  来源：<https://aceproject.org/ace-en/topics/es/esd/esd02/esd02d/>；<https://electoral-reform.org.uk/does-ireland-use-proportional-representation/>
- **#15** 「Parliaments and parliamentary bodies and political life as we know it to-day are destined to disappear.」  
  判断：**错误**。议会政治并未消失：两战之间确有民主崩溃（1920年欧洲二十八国中二十六国为议会民主，到1938年其中十三国变为独裁），但Our World in Data据Regimes of the World数据显示过去两百年民主国家大幅增加  
  来源：<https://ourworldindata.org/democracy>；<https://escholarship.org/uc/item/8xf4t3t0>
- **#17** 「The Labour Party is surely not so foolish as to take office in a minority again」  
  判断：**错误**。工党再次以少数党身份执政：1929年大选形成悬浮议会，工党获287席成为最大党，组成少数派政府  
  来源：<https://liberalhistory.org.uk/history/the-1929-general-election/>；<https://researchbriefings.files.parliament.uk/documents/SN04951/SN04951.pdf>
- **#20** 「there is a very considerable probability that that ailing State will be, as a potential modern State, ruined a…」  
  判断：**错误**。苏联在随后几十年内没有被摧毁，反而迅速工业化：1928年起推行五年计划，到20世纪30年代末已由农业社会变成主要工业强国；苏联到1991年才解体，距写作已超过60年，原因也不是书中设想的英美围剿  
  来源：<https://en.wikipedia.org/wiki/Economy_of_the_Soviet_Union>；<https://www.investopedia.com/articles/investing/021716/why-ussr-collapsed-economically.asp>
- **#26** 「It seems highly probable that twenty years hence we shall be muckering about with air travel very much as we a…」  
  判断：**错误**。二十年后的航空并未依旧时断时续：20世纪30年代中期起DC-3等客机推动美国航空业高速增长；1946年美国定期航班运送14,000,000名旅客、7,000,000,000英里，创纪录；同年在美国境内死亡旅客75人也创新高，但航空已成为定期、大规模的运输方式，不再是“时断时续”的试验  
  来源：<https://time.com/archive/6793048/transport-fatal-statistics/>；<https://www.faa.gov/sites/faa.gov/files/about/history/milestones/Celebrating_75_Years_of_Federal_Air_Traffic_Control.pdf>
- **#27** 「the real professional soldiers will torture and kill scores of thousands of conscripts before they learn, horr…」  
  判断：**错误**。书中设想下一场大战里毒气会杀死成千上万的征召兵，但二战欧洲主战场基本没有使用化学武器；日本在中国使用化学武器2000多次是例外，受害者主要是中国军民而非本国征召兵  
  来源：<https://scholarship.richmond.edu/polisci-faculty-publications/222/>；<https://link.springer.com/chapter/10.1007/978-3-319-51664-6_14>
- **#28** 「It is the country that has the courage to scrap its army most completely which may come nearest winning in the…」  
  判断：**错误**。二战并非由裁撤传统军队的国家赢得：苏联在战争中动员了29,574,900人，全世界约127.2 million人被动员；雷达、原子弹等科技很重要，但没有哪个大国靠裁军接近胜利  
  来源：<https://www.cuttersguide.com/pdf/ww2/Hitlers%20Versus%20Stalin%20-%20The%20Eastern%20Front%20in%20Photographs.pdf>；<https://www.statista.com/statistics/1342260/wwii-mobilization-by-country/>；<https://www.nationalww2museum.org/war/articles/scientific-and-technological-advances-world-war-ii>
- **#32** 「it will be almost impossible to prevent the copious gassing of that great warren within a few hours of the ope…」  
  判断：**错误**。前提成立（1939年爆发一流欧洲大战），但伦敦没有在开战几小时内遭毒气攻击：1939年9月3日宣战当天虽响起防空警报，英格兰直到次年才被德国空军轰炸，且始终未遭毒气袭击  
  来源：<https://historicengland.org.uk/whats-new/features/blitz-stories/england-under-attack/>；<https://www.museum-newtonabbot.org.uk/news/article/world-war-two-gas-protection-equipment>
- **#34** 「When they have flowed past, then I suggest that the whole broadcasting industry will begin to dry up.」  
  判断：**错误**。广播业没有枯竭：英国无线电执照从1937年底的8,479,600张增加到1938年底的8,908,900张；美国家庭拥有收音机的比例从1930年的40%多升到1940年的83%  
  来源：<https://www.worldradiohistory.com/UK/BBC/BBC-Annual/BBC-Year-Book-1939.pdf>；<https://www.apmreports.org/episode/2014/11/10/radio-the-internet-of-the-1930s>

### 暂无法判断（1 条）

- **#16** 「If the present British Government remains in office for another five years that smash, I believe, will come.」  
  判断：**暂无法判断**。条件未触发：鲍德温政府在1929年5月大选中失败，1929年6月卸任，没有“再执政五年”，无法据此判断“大祸”预测  
  来源：<https://www.ark.ac.uk/elections/fw29.htm>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/wells-way-the-world-is-going-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/wells-way-the-world-is-going-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/wells-way-the-world-is-going-v5/audit/manual_review_2026-11-15.py`
