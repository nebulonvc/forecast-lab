# 哈尔福德·麦金德《民主的理想与现实》（Democratic Ideals and Reality）：出版后预测人工核查

- 案例目录：`cases/mackinder-democratic-ideals-and-reality-v5/`
- 出版日期：Henry Holt and Company（纽约）**1919 年**出版（序言写于 1919 年 2 月；英国 Constable 版同年），按 1919 年起算。书单正文为 `reading-library/2026-11-15-未来判断扩展100本/02-政治与治理/023-democratic-ideals-and-reality-a-study-in-the-politics-of-reconstruction.pdf`（美国国会图书馆扫描本，sha256 `e8fb817a…`，298 页）；因本地检出缺该 PDF、loc.gov 被拦截，抽取改用 Internet Archive 上同一 Holt 1919 扫描本 `democraticideals00mack`（298 页，sha256 `1c230d20…`，自带 OCR 文字层），经 `pdftotext -enc UTF-8` 得到 TXT（340,159 字符，sha256 `95d85690…`）。观察窗口 1919 至 2026-11-15；书中写明的终点（“不久”“几年内”“一两代”等）按各自终点判断。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

按 METHOD.md 复刻仓库 DeepSeek 流水线，仅以人工阅读替代模型调用。抽取：仓库 prepare_book v5 把全文切成 99 块（3500 字符、600 字符上下文），助手逐块通读、按 DISCOVER_PROMPT_V5 写出模型本应返回的 JSON（非关键词筛选），再由仓库代码完成引文对齐、归属降级、去重和导入：候选 49 条，其中可核验预测 38 条、非预测/不可判 11 条（机制 4、假设 4、被作者否定 1、琐碎 1、不可判 1）。OCR 文本换行错乱，英文 changes 均取原文同一行片段。核验：每条先写 scope，各做 support 与 counter 的 Exa 检索（两轮共 86 次），只从检索返回的 URL 中选源，原文存档于 data/sources（sha256），写入 data/evidence.jsonl（88 条），由助手阅读存档全文后按四分类规则评断，经 pipeline.py apply assess → check → report。本稿由助手逐条对照书中原文与存档证据人工复核：判断理由中的事实与数字均取自 data/sources 中实际抓取的网页存档。先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 38 条，剔除非预测 0 条，计入 **38 条预测**，其中 **38 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 22 |
| 趋势符合 | 0 |
| 部分符合 | 8 |
| 错误 | 8 |
| 暂无法判断 | 0 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **57.9%**（22/38） |
| 加权胜率 | **68.4%** |
| 错误率 | **21.1%**（8/38） |
| 未定占比（暂无法判断/预测） | 0.0%（0/38） |

## 总体评价

《民主的理想与现实》写于一战停战后、巴黎和会之际，核心论断是“心脏地带—东欧”的地缘政治逻辑：若和约不彻底解决东欧问题，德俄之争终将再起战端。这一主线大体应验：国际紧张在 1920 年代缓慢重积、1930 年代激化，纳粹从魏玛乱局中崛起，东线成为二战最大战场，西欧先后联合对抗纳粹德国与苏联；普鲁士在 1947 年被正式废除，俄国经历了长期专制；地理上的“封闭世界”、喀拉海夏季航运、土西铁路、巴勒斯坦铁路南北贯通、犹太民族家园也都实现。失误集中在他寄予厚望的战后安排上：德俄之间的“中间层”小国未能抵御德苏、国联未能维持和平，保加利亚并未欣然接受讷伊条约，罗马尼亚没有富起来，加澳实力远未赶上英国，英国也没有走向联邦制，英国战债负担远比他预想的沉重。俄国“分成若干国家、组成某种松散联邦”只部分应验：1991 年苏联解体、成立独联体，但此前近 70 年是高度集权的联盟，独联体也不是联邦。38 条可判定预测中正确 22 条、错误 8 条。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（22 条）

- **#1** 「But interna- tension will accumulate again, though」  
  判断：**正确**。1919年后国际紧张确实重新积累：起初较缓（1920年代被视为相对乐观的阶段），1930年代经大萧条、法西斯意大利与纳粹德国扩张而激化，1939年9月德国入侵波兰引发第二次世界大战。方向与结果均与预测一致。  
  来源：<https://www.iwm.org.uk/history/second-world-war/causes>；<https://www.ungeneva.org/en/about/league-of-nations/at-work>
- **#2** 「No considerable fertile new land, no important mountainrange, and no first-class river can any more be the rew…」  
  判断：**正确**。1919年后人类对地表的探索转向高峰、深海与极地细节，已无重要的新肥沃陆地、大山脉或一级大河被发现；近年的“发现”只是对已知河流源头等细节的厘清（如阿姆河源头的考证），不构成反例。  
  来源：<https://www.encyclopedia.com/science/encyclopedias-almanacs-transcripts-and-maps/history-exploration-iii-modern-era>；<https://en.wikipedia.org/wiki/List_of_explorations>；<https://www.uwa.edu.au/news/article/2026/march/explorers-solve-3000-year-mystery-of-source-of-central-asias-greatest-river>
- **#3** 「Every deed of humanity will henceforth be echoed and reechoed in like manner round the world.」  
  判断：**正确**。出版后世界经济与政治的互联显著加深：OWID 记录上世纪各国经济被整合入全球体系、贸易大幅增长；即便1914–1939年贸易全球化一度“死亡”，大萧条等冲击本身也在全球传导，二战后又进入新的整合与“超全球化”阶段，符合“每一行动都将在全球回响”的方向。  
  来源：<https://ourworldindata.org/trade-and-globalization>；<https://www.piie.com/blogs/realtime-economic-issues-watch/twenty-first-century-trade-integration-eight-figures>；<https://academic.oup.com/qje/article/118/2/359/1899569>
- **#4** 「In the days of air navigation which are coming, sea-power will use the water way of the Mediterranean and Red …」  
  判断：**正确**。英国官方战史记载：1941年1月德国空军进入地中海带来新挑战，缺乏合适机场时只能部分应对，此后敌方夺回昔兰尼加、攻占克里特，空军在当地大批进驻，英国须付出重大代价并依靠夺取北非、西西里沿岸重新控制航道；2023–2024年也门胡塞武装从陆上袭击商船，2024年头两个月苏伊士运河贸易同比下降约50%，红海港口挂靠下降85%。海权使用该航道受制于陆基力量得到反复印证。  
  来源：<https://www.ibiblio.org/hyperwar/UN/UK/UK-Med-II/UK-Med-2-14.html>；<https://www.gtreview.com/news/mena/red-sea-attacks-causing-steep-drop-in-port-calls-canal-traffic-data-shows/>；<https://navymuseum.co.nz/explore/by-themes/world-war-two-by-themes/malta-convoys/>；<https://www.imf.org/en/blogs/articles/2024/03/07/red-sea-attacks-disrupt-global-trade>
- **#7** 「to open a direct route to the mouths of the Obi and Yenisei may perhaps result in the establishment of a sea-b…」  
  判断：**正确**。1920年起苏俄组织“喀拉海远征”，借破冰船护航经喀拉海向鄂毕河、叶尼塞河口运送货物，1920–1930年代形成定期的夏季海运，与预测一致。  
  来源：<https://bsk.nios.ru/enciklodediya/karskie-ekspedicii>；<https://vestnikgum.ru/en/archive/?ELEMENT_ID=43369541>
- **#8** 「aeroplane routes in the near future, constitutes a revolution in the relations of men to the larger geographic…」  
  判断：**正确**。出版后十余年内，土西铁路（Turksib）于1930年建成通车，把中亚与西伯利亚连接起来；心脏地带的交通开放在“不久的将来”实现。  
  来源：<https://en.wikipedia.org/wiki/Turkestan%E2%80%93Siberia_Railway>；<https://docs.historyrussia.org/ru/nodes/382051-ob-otkrytii-turkestano-sibirskoy-zheleznoy-dorogi-turksiba-1-maya-1930-g-post-vtsik-i-snk-ot-19-aprelya-1930-g>
- **#9** 「already the trunk railway is being built through the coastal plain by Jaffa, which will connect the Southern w…」  
  判断：**正确**。巴勒斯坦铁路在一战后经营沿海干线；澳大利亚战争纪念馆1942年7月档案称，海法至的黎波里的新连接线即将完工，“使利比亚、巴勒斯坦、叙利亚与土耳其之间形成不间断的铁路连接”，南北贯通得以实现；1948年后该线中断，但连接本身已经出现。  
  来源：<https://en.wikipedia.org/wiki/Palestine_Railways>；<https://www.awm.gov.au/collection/150255>；<https://en.wikipedia.org/wiki/Cairo%E2%80%93Haifa_train_bombings_1948>
- **#12** 「No mere scraps of paper, even though they be the written constitution of a League of Nations, are under the co…」  
  判断：**正确**。国际联盟未能阻止新的世界大战，东线（德苏战争）成为二战规模最大、伤亡最惨重的战场，心脏地带及东欧再次成为世界大战的中心。  
  来源：<https://encyclopedia.ushmm.org/content/en/article/the-soviet-union-and-the-eastern-front>；<https://www.ibiblio.org/hyperwar/USA/USA-EF-Defeat/USA-EF-Defeat-22.html>
- **#13** 「As far as the two chief nations, Britain and France, are concerned, there is and can be in modern times no que…」  
  判断：**正确**。出版后英法始终未出现一方征服另一方；两国在两次世界大战中为盟友，冷战与当代防务合作延续。1940年英国在米尔斯克比尔袭击法国舰队是严重冲突，但不是征服，不改变结论。  
  来源：<https://en.wikipedia.org/wiki/Entente_Cordiale>；<https://en.wikipedia.org/wiki/Attack_on_Mers-el-K%C3%A9bir>
- **#14** 「West Europe, both insular and peninsular, must necessarily be opposed to whatever Power attempts to organize t…」  
  判断：**正确**。西欧先后与试图组织东欧及心脏地带资源的纳粹德国作战，战后又与美加组建北约以对抗苏联扩张；1938年慕尼黑绥靖是阶段性例外，但总体走向符合预测。  
  来源：<https://history.state.gov/milestones/1945-1952/nato>；<https://1997-2001.state.gov/regions/eur/nato_fsnato.html>；<https://encyclopedia.ushmm.org/content/en/timeline-event/holocaust/1933-1938/munich-agreement>
- **#15** 「If we accept anything less than a complete solution of the Eastern Question in its largest sense we shall mere…」  
  判断：**正确**。条件成立：凡尔赛体系未能最终解决德国与东欧斯拉夫民族问题，1939年德国吞并捷克斯洛伐克，凡尔赛和平结构瓦解；结果出现：胜利只换来约二十年的喘息，下一代不得不再次集结力量对抗控制东欧的强国。  
  来源：<https://www.cambridge.org/core/books/abs/versailles-treaty-and-its-legacy/coming-of-war-1939/583E546DAB060CD7F82DB8D70CF87D4D>；<https://wwnorton.com/college/history/western-civilization17-brief/ch/26/summary.aspx>
- **#16** 「The end of the present disorder may only be a new ruthless organization, and ruthless organizers do not stop w…」  
  判断：**正确**。魏玛共和国1924–1929年一度稳定，但最终于1933年由纳粹夺权，德国由民主转为独裁，并持续扩张而未止步于最初目标，与“混乱的结局可能只是新的冷酷组织”相符。  
  来源：<https://encyclopedia.ushmm.org/content/en/article/the-nazi-rise-to-power>；<https://alphahistory.com/weimarrepublic/golden-age-of-weimar/>
- **#18** 「The Russians are, and for one, if not two, generations must remain, hopelessly incapable of resisting German p…」  
  判断：**正确**。出版后俄国（苏联）长期处于专制统治：斯大林自1920年代末至1953年实行极权统治，此后苏共一党专政延续至1980年代末，覆盖作者所说的一到两代人。  
  来源：<https://en.wikipedia.org/wiki/stalinism>；<https://www.history.com/articles/joseph-stalin>
- **#19** 「rate, will not lack the will to order and to indethe creating pendence.」  
  判断：**正确**。捷克斯洛伐克在1918–1938年逐步建立起运转中的（虽有缺陷）议会民主，是中东欧少有维持秩序与独立的国家；1938年慕尼黑协定是大国强加的割让，不能说明其缺乏维持独立的意志。  
  来源：<https://experts.illinois.edu/en/publications/interwar-czechoslovakia-a-national-state-for-a-multiethnic-popula>；<https://www.vhu.cz/en/exhibit/01-mnichovska-dohoda/>
- **#20** 「But the Magyars and Bulgarians are engirt by the other five peoples, and neither of them will be powerful for …」  
  判断：**正确**。两次世界大战之间，匈牙利（以及加入轴心国的保加利亚）只有依靠德意支持才获得领土（第一、二次维也纳仲裁），并作为轴心国一员为害；1919年匈牙利苏维埃共和国短暂进攻斯洛伐克后即被罗马尼亚击败，进一步说明其单独为害能力有限。  
  来源：<https://encyclopedia.ushmm.org/content/en/article/axis-powers-in-world-war-ii>；<https://en.wikipedia.org/wiki/Second_Vienna_Award>；<https://en.wikipedia.org/wiki/Hungarian_Soviet_Republic>
- **#22** 「a democratic Hungary will sooner or later adapt herself to the new environment.」  
  判断：**正确**。两次大战之间的匈牙利并非民主政体，奉行收复失地主义，前提未成立；1989年后民主匈牙利与斯洛伐克、罗马尼亚签订基础条约，至1990年代末已与八个邻国无边界争议，迟早适应新环境的结果在条件满足后出现。  
  来源：<https://1997-2001.state.gov/regions/eur/fs_hungary.html>；<https://www.rferl.org/a/1081535.html>；<https://www.osw.waw.pl/sites/default/files/PV_EN_Trianon.pdf>
- **#25** 「we not now the certainty that the United Kingdom, Canada, and Australia will each have its own fleet and army」  
  判断：**正确**。英国本土、加拿大与澳大利亚此后一直各自保有本国海军与陆军（皇家澳大利亚海军1911年定名、加拿大海军1910年建立并延续至今），与预测一致；此事在出版前已有端倪，属于延续性判断。  
  来源：<https://www.navy.gov.au/about-navy/history/history-milestones/king-george-v-grants-title-royal-australian-navy>；<https://thecanadianencyclopedia.ca/en/article/royal-canadian-navy>
- **#27** 「Is it not probable that occasions will occur when the Prime Ministers of Canada and Australia may be called in…」  
  判断：**正确**。巴黎和会期间，澳大利亚总理休斯、加拿大总理博登作为全权代表与英、法、意首脑一同与会并签署和约；此后帝国会议等场合亦多次出现。该会议在出版时已开始，属于近期即兑现的判断。  
  来源：<https://en.wikipedia.org/wiki/List_of_participants_in_the_Paris_Peace_Conference_(1919%E2%80%931920)>；<https://anzacportal.dva.gov.au/wars-and-missions/ww1/politics/peace-negotations>
- **#29** 「France, is a purely artificial structure, will broken into several Federal States.」  
  判断：**正确**。1947年2月25日盟国管制委员会第46号法令正式废除普鲁士，其领土分属新的联邦州及他国，普鲁士作为单一结构被分解。  
  来源：<https://en.wikipedia.org/wiki/Abolition_of_Prussia>；<https://en.wikisource.org/wiki/Control_Council_Law_No_46_(25_February_1947)_Abolition_of_Prussia>
- **#33** 「The Jewish National seat in Palestine will be one of the most important outcomes of the War.」  
  判断：**正确**。一战中的贝尔福宣言与战后英国委任统治为犹太民族家园奠基，1948年5月14日以色列建国，成为一战后中东格局最深远的结果之一。  
  来源：<https://history.state.gov/milestones/1945-1952/creation-israel>；<https://www.un.org/unispal/history2/origins-and-evolution-of-the-palestine-problem/part-i-1917-1947/>
- **#34** 「even among those large Jewish communities which will remain as Going Concerns outside Palestine.」  
  判断：**正确**。至2023年全球犹太人约1570万，以色列约占45%（约700万），巴勒斯坦以外（尤其美国）仍有庞大犹太社群。  
  来源：<https://www.jewishdatabank.org/databank/search-results/study/1249>；<https://www.jewishagency.org/jewish-population-rises-to-15-7-million-worldwide-in-2023/>
- **#35** 「No important country, after this War, upset. is going to allow itself to be deprived either of that it any "ke…」  
  判断：**正确**。连奉行自由贸易的英国也在1921年通过《工业保护法》，对光学玻璃等关键工业征收保护性关税，1930年代各国普遍转向保护主义，与预测方向一致。  
  来源：<https://en.wikipedia.org/wiki/Safeguarding_of_Industries_Act_1921>；<https://www.legislation.gov.uk/ukpga/Geo5/11-12/47/enacted>

### 部分符合（8 条）

- **#5** 「a circumstance which may some day have importance for the traveler by railway or air」  
  判断：**部分符合**。纽约—北京最短的大圆航线确实穿越北极地区，跨极地商业航班已运营，北方路线对航空旅行具有实际意义；但预测中经白令海峡的铁路通道至今仍只是设想，未曾建成。航空部分符合，铁路部分不符。  
  来源：<https://thatsmaths.com/2017/10/05/from-sailing-on-a-rhumb-to-flying-on-a-geodesic/>；<https://www.airwaysmag.com/new-post/transpolar-commercial-flights>；<https://en.wikipedia.org/wiki/Bering_Strait_crossing>
- **#6** 「Nor is time likely to the lesser continents. change these proportions materially.」  
  判断：**部分符合**。据《不列颠百科全书》1926年增补卷估计，1920年世界人口约18.19亿，其中北美1.44亿、南美0.67亿，美洲约占11.6%；2020年拉丁美洲8.3%、北美4.7%，合计约13%。“较小大陆”所占比例确实没有实质变化，世界岛占比也大体稳定；但作者给出的基准比例（美洲与澳洲约1/16）本身与当时数据不符，英日份额的变化未取得存档证据，故只记部分符合。  
  来源：<https://en.wikisource.org/wiki/Page:EB1926_-_Supplement_Volume_3.pdf/223>；<https://demographystatisticsand.health.blog/2020/11/30/distribution-of-world-population-by-continent-2020/>
- **#10** 「it is probable that Tibet, the " roof of the world, and widely separate the overland routes into China and wil…」  
  判断：**部分符合**。西藏高原至今仍是巨大屏障：跨喜马拉雅的中尼铁路仍处计划阶段，中巴喀喇昆仑公路是“极少数”穿越该山系的路线之一，主要陆路仍绕行高原侧翼；但青藏铁路和公路已深入高原，高原并非完全被绕开，且预测的前提（撒哈拉被日常交通穿越）只部分出现。  
  来源：<https://en.wikipedia.org/wiki/China%E2%80%93Nepal_railway>；<https://en.wikivoyage.org/wiki/Karakoram_Highway>
- **#11** 「The World-Island united, as it soon will be, by part parallel with railways, and by aeroplane routes」  
  判断：**部分符合**。航空线路很快把欧亚连接起来：帝国航空1929年开通伦敦—卡拉奇定期航线；但铁路方面，泛亚铁路网至今仍存在多处缺失路段，世界岛被铁路“联结”只部分实现。  
  来源：<https://www.nzsgb.org.uk/bobs/air-external-eastern-kar/>；<https://www.unescap.org/sites/default/d8files/event-documents/ESCAPTARN%289%29_5_E.pdf>
- **#30** 「number of States in some sort of loose federation?」  
  判断：**部分符合**。按 WORKER_BRIEF 规则 10 严格复核（2026-11-16），由正确改为部分符合。“分成若干国家”在 1991 年出现：苏联解体为 15 个独立国家，俄罗斯、白俄罗斯、乌克兰以《别洛韦日协议》宣告苏联不复存在，并成立独联体作为替代的“共同体”，前自治区的分离运动大多失败。但此前近 70 年走的是相反方向：1922 年成立的苏联名义上是民族共和国的联盟，政府和经济却高度集权、多数方面是单一制国家；独联体是独立国家之间的共同体而不是联邦，而且结果出现在出版七十多年后。“某种松散联邦”只算部分实现。  
  来源：<https://en.wikipedia.org/wiki/Dissolution_of_the_Soviet_Union>；<https://courses.lumenlearning.com/suny-worldhistory/chapter/30-2-6-formation-of-the-soviet-union/>
- **#32** 「When the network of railways has covered the World-Island, Constantinople will be one of the most accessible p…」  
  判断：**部分符合**。伊斯坦布尔在航空与海运上已是全球枢纽：Eurocontrol 显示伊斯坦布尔机场2024年连续第三年为欧洲最繁忙机场；但其铁路联系长期薄弱，国际列车班次稀少，“铁路、轮船、飞机三者皆最便捷”只部分实现。  
  来源：<https://www.aa.com.tr/en/turkiye/istanbul-airport-keeps-crown-of-europe-s-busiest-air-hub-in-2024/3460499>；<https://railturkey.org/2018/02/28/trainless-istanbul/>
- **#37** 「No doubt a new Germany and a new Russia will some day increase them to seven.」  
  判断：**部分符合**。新德国与新俄国确实先后作为大国加入国联并获常任理事国席位（德国1926年9月8日、苏联1934年9月18日），但德国已于1933年10月退出，美国从未加入，国联中的大国数目从未同时达到七个。方向部分实现，具体数目不符。  
  来源：<https://www.usni.org/magazines/proceedings/1934/november/notes-international-affairs>；<https://www.loc.gov/item/2021667903/>；<https://digital.nls.uk/league-of-nations/archive/194789813?mode=transcription>
- **#38** 「Perhaps the Smaller Powers, taking note of the naked fact which was exposed by this incident, will set about f…」  
  判断：**部分符合**。小国确实结成过区域组合：捷克斯洛伐克、罗马尼亚和南斯拉夫在1920–1921年组成“小协约国”，北欧国家1952年成立北欧理事会；但这些都是松散同盟或合作机制而非联邦，北欧联邦至今仅为提议，西语南美集团也未形成。  
  来源：<https://www.encyclopedia.com/reference/encyclopedias-almanacs-transcripts-and-maps/little-entente>；<https://www.norden.org/en/information/history-nordic-co-operation>；<http://ssoar.info/ssoar/handle/document/10366>

### 错误（8 条）

- **#17** 「her increased productive power, — — owing to reorganization and new methods compelled by the War, should far e…」  
  判断：**错误**。与“生产能力增长将远超战债利息与偿债基金”相反：战后英国债务占GDP比重在1923年升至约180%，1920年代末仅降至约160%；IMF 指出英国经历强烈通缩、增长乏力和高失业，尽管保持大额基本盈余，债务比率仍在上升。  
  来源：<https://www.economicshelp.org/blog/11709/debt/attempting-to-reduce-debt-after-first-world-war/>；<https://www.imf.org/-/media/websites/imf/imported-flagship-issues/external/pubs/ft/weo/2012/02/c3/_fig37pdf.pdf>
- **#21** 「the twelve million Rumanians will be a rich people.」  
  判断：**错误**。罗马尼亚并未成为富裕民族：IMF 指出尽管有显著追赶，罗马尼亚人均GDP在欧盟中仍排倒数第二，贫困与不平等相对较高；媒体至2026年仍称其为欧盟最穷国家之一。  
  来源：<https://www.elibrary.imf.org/view/journals/002/2022/311/article-A002-en.xml>；<https://www.theguardian.com/world/2026/jun/29/romanian-families-torn-apart-by-migration-children>
- **#23** 「both nations, the Bulgarians and the Serbs, deeply war-weary, For twenty will probably accept it joyfully.」  
  判断：**错误**。协约国在1919年《讷伊条约》中强加了解决方案，但保加利亚并未欣然接受：割地、限制军队并支付赔款，在保加利亚被称为“第二次民族灾难”，对战后安排的不满最终使其在二战中与纳粹德国结盟、暂时重占所失领土。塞尔维亚一方作为受益者接受了和约，但对保加利亚的判断与事实相反。  
  来源：<https://www.thesecondworldwar.org/interbellum-1918-1936/1919/paris-peace-conference/treaty-of-neuilly-sur-seine>；<https://www.novinite.com/articles/134306/Bulgaria+Marks+92+Years+of+Gruesome+Neuilly+Treaty+after+WW+I>
- **#24** 「the governing units of will the British Empire can only grow by gradual process into their place as units of y…」  
  判断：**错误**。加拿大、澳大利亚等自治领并非渐进地成为国联成员：它们作为凡尔赛和约签字国名列国联创始会员国名单，1920年1月10日即成为会员（美国史学会文章亦称其“成为国联创始会员国”）；完全主权地位后来才经1926年贝尔福宣言等确认，但这不同于“成为国联单位”的具体判断。  
  来源：<https://history.state.gov/historicaldocuments/frus1919Parisv13/ch10subsubch1>；<https://history.state.gov/historicaldocuments/frus1919Parisv13/ch22subsubch1>；<https://www.historians.org/resource/are-the-dominions-really-independent/>
- **#26** 「is it not now a question of only a few years before Canada and Australia will equal the Motherland in power?」  
  判断：**错误**。“几年内”加澳实力并未与英国相当：1931年加拿大人口约1037.7万、澳大利亚约645.6万（1930年9月估计），两者合计约1680万；而英国在1914年人口已约4600万（含爱尔兰430万），即便扣除爱尔兰，加澳合计仍远不及英国的一半。  
  来源：<https://www66.statcan.gc.ca/eng/1939/193901490083_p.%2083.pdf>；<https://trove.nla.gov.au/newspaper/article/203347641?browse=ndp%3Abrowse%2Ftitle%2FA%2Ftitle%2F809%2F1931%2F02%2F10%2Fpage%2F18964949%2Farticle%2F203347641>；<https://nzhistory.govt.nz/war/united-kingdom-facts>
- **#28** 「With a Middle Tier of really independent States between Germany and Russia they will achieve their end, and wi…」  
  判断：**错误**。一战后确实在德俄之间建立起波兰、捷克斯洛伐克、罗马尼亚、南斯拉夫等独立的中间层国家，但国际联盟仍未能维持和平，二十年后这些国家全部卷入并遭吞并或沦为附庸，与“有中间层即可实现目标”的预测相反。  
  来源：<https://journals.unibuc.ro/index.php/index/article/view/4002>；<https://www.nationalww2museum.org/war/articles/league-of-nations>
- **#31** 「they may be trusted — any new organization of either great neighbor making towards the Empire of East to resis…」  
  判断：**错误**。中间层国家未能抵抗德俄重建东欧帝国：二战中匈牙利、罗马尼亚、保加利亚加入轴心国，捷克斯洛伐克和波兰被德国吞并或占领；1945年后苏联在中东欧建立东方集团，扶植受其控制的政府。  
  来源：<https://en.wikipedia.org/wiki/Formation_of_the_Eastern_Bloc>；<https://encyclopedia.ushmm.org/content/en/article/axis-powers-in-world-war-ii>
- **#36** 「in Britain we seem to be not very far from becoming so.」  
  判断：**错误**。英国并未走向联邦制：直到1999年才实行向苏格兰、威尔士和北爱尔兰的权力下放，议会资料明确指出这与联邦制不同，英国在二十世纪后半期仍是最中央集权的发达国家之一。  
  来源：<https://commonslibrary.parliament.uk/research-briefings/cbp-8599/>；<https://personal.lse.ac.uk/hopkin/regno%20unito%20hopkin%202007.pdf>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/mackinder-democratic-ideals-and-reality-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/mackinder-democratic-ideals-and-reality-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/mackinder-democratic-ideals-and-reality-v5/audit/manual_review_2026-11-15.py`
## 说明

- 第 15、22、23、28 条是条件句：15、23、28 条前提按已发生的历史安排视为成立；第 22 条“民主匈牙利”的前提在两次大战之间不成立，按 1989 年后条件满足的阶段核验。
- 第 6 条作者给出的人口比例基准本身与 1920 年数据不符，按“比例是否实质变化”核验，只记部分符合。
- 2026-11-16 按 WORKER_BRIEF 规则 10 严格复核：第 30 条（俄国分成若干国家、组成松散联邦）由正确改为部分符合；第 19 条（捷克人不缺乏维持秩序与独立的意志）维持正确（存档证据：两次大战间建成运转中的议会民主、1938 年全军动员且“决心作战”，是中欧最后的民主国家，慕尼黑割让系大国强加）。两条均只依据已存档证据，未新增检索。
- 正文所用 PDF 为 Internet Archive 上同一 LOC 扫描本，未与书单 PDF 做字节比对（文件大小相差约 46KB）。
- 统计以 pipeline.py report 的 summary.json 为准；加权胜率按 manual_report.py 的权重计算（正确×1 + 趋势符合×0.75 + 部分符合×0.5）。

