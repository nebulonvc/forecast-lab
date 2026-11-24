# 罗伯特·D·卡普兰《地理的复仇》（The Revenge of Geography）：出版后预测人工核查

- 案例目录：`cases/kaplan-revenge-of-geography-v5/`
- 出版日期：**2012 年 9 月 11 日**（Random House 初版；电子版 ISBN 978-0-679-60483-9）。正文为 reading-library 书单中的 PDF（sha256 `64e13003…`）经 pdftotext 得到的全书 TXT（sha256 `ff5b7f15…`）。观察窗口为 2012-09-11 至 2026-11-15（Asia/Shanghai）。书中写明的终点（如 2018—2020 年、1995—2025 年、2050 年）按各自时点判断。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

本稿是按 METHOD.md 的重做版（替代此前助手用关键词筛句后只保留 33 条预测的旧稿）。抽取：用仓库 prepare_book v5 流水线把全文切成 221 块（3500 字符、600 字符上下文），助手通读正文各块、按 DISCOVER_PROMPT_V5 写出模型本应返回的 JSON，再由仓库代码完成引文对齐、归属降级、去重和导入，得到 137 条可核验预测。前言与致谢不录入预测。核验：每条先写 scope，各做一次 support 与 counter 的 Exa 检索，只从检索返回的 URL 中选源，原文存档于 data/sources（sha256），写入 data/evidence.jsonl（210 条），由助手阅读后按四分类规则评断，经 pipeline.py apply assess → check → report。本稿由助手逐条对照书中原文与存档证据人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 137 条，剔除非预测 0 条，计入 **137 条预测**，其中 **131 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 57 |
| 趋势符合 | 34 |
| 部分符合 | 32 |
| 错误 | 8 |
| 暂无法判断 | 6 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **43.5%**（57/131） |
| 加权胜率 | **75.2%** |
| 错误率 | **6.1%**（8/131） |
| 未定占比（暂无法判断/预测） | 4.4%（6/137） |

## 总体评价

卡普兰对2012年后大国竞争回归、印太海权和边缘地带制衡、欧洲因俄乌战争再次被对俄关系决定、南海成为亚洲政治地理核心、伊朗在伊拉克遭反感、叙利亚成为阿拉伯动荡中心等判断，多数已经应验。人口、互联互通和海军投射等方向性预测也大体同向。主要失准集中在定量或时机过满的句子：全球城市人口并未在2025年达到三分之二，俄罗斯穆斯林人口没有在约十年内升至20%，朝鲜半岛政治边界并未移动，两岸经济联系没有降低军事统一压力，阿萨德政权也没有在本书出版前倒下。条件未出现或终点仍在“最终”的条目（朝鲜统一、美国放弃台湾、伊朗政权更迭、阿富汗被稳定等）记为暂无法判断。与旧稿 33 条相比，通读后预测数量明显增加，严格胜率有所下降，但加权胜率仍高，说明书的大方向比若干具体时点和数字更经得起检验。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（57 条）

- **#2** 「For such struggles in the heart of Europe there will be.」  
  判断：**正确**。2022年俄罗斯全面入侵乌克兰后，欧洲腹地再次成为大国军事对抗的现场，后冷战“欧洲和平”被打破，判断已经应验。  
  来源：<https://ies.lublin.pl/en/yearbook/riesw/2022/4/1/>
- **#3** 「And because world government will forever remain elusive, since there will never be fundamental agreement on t…」  
  判断：**正确**。截至核验截止日，并不存在世界政府。联合国仍是主权国家组成的政府间组织，世界仍由不同政体分别统治。  
  来源：<https://openstax.org/books/introduction-political-science/pages/15-3-the-united-nations-and-global-intergovernmental-organizations-igos>
- **#4** 「even as the spatial arrangement of Libyan tribes and of the mountain ranges in Yemen will continue to play cru…」  
  判断：**正确**。利比亚内战与也门冲突表明，部落空间分布与山地地貌仍是两国政治和战争的关键约束，并未被后革命制度消解。  
  来源：<https://academic.oup.com/yale-scholarship-online/book/13064/chapter/166289073>
- **#8** 「The Arctic, especially if it warms, will give new meaning to sea power and especially air power in future deca…」  
  判断：**正确**。北极变暖条件已经满足，俄中在北极的长期目标和美国对北极防务的重视表明，海权与空权在该地区获得了新的战略意义。  
  来源：<https://www.gmfus.org/sites/default/files/2026-01/20260121-Hybrid-CoE-Paper-28-Bracing-for-a-cold-front-Assessing-Russian-and-Chinese-strategic-objectives-and-hybrid-threat-capabilities-in-the-Arctic-WEB.pdf>
- **#12** 「the Greater Indian Ocean will form the maritime interstate of the World-Island’s commercial and military traff…」  
  判断：**正确**。印度洋作为连接非洲、中东与东亚的能源和商业海上干道，已成为美、中、印海军战略的核心水域。  
  来源：<https://www.uscc.gov/sites/default/files/2022-05/Darshana_Baruah_Testimony.pdf>
- **#13** 「Still, the Eurasian Rimland will not be united in any strictly political sense.」  
  判断：**正确**。欧亚边缘地带仍分裂为欧盟、东盟、南亚和中东等互不统属的政治单位，并不存在政治意义上的边缘地带统一。  
  来源：<https://www.foreignaffairs.com/china/heartland-vs-rimland-beckley-brands>
- **#14** 「Not even the Chinese, with their rising sea power, appear capable of this achievement, checked as they will be…」  
  判断：**正确**。美印日澳通过四边机制和AUKUS加强海军协作，中国海权上升但未能统一边缘地带，制衡格局已经出现。  
  来源：<https://seapower.navy.gov.au/sites/default/files/2023-04/AUKUS%20and%20the%20Indo-Pacific%20An%20Emerging%20Debate.pdf>
- **#17** 「the Western Pacific and Indian oceans will be the first among equals in strategic importance.」  
  判断：**正确**。美国对华竞争使西太平洋与印度洋成为战略文献中的首要海域，印太成为美国大战略重心。  
  来源：<https://www.nbr.org/wp-content/uploads/pdfs/publications/asiapolicy16-3_indianocean_rt_july2021.pdf>
- **#18** 「On the other hand, there will be the assertion of rising power by China primarily, and India secondarily, each…」  
  判断：**正确**。中国和印度都在扩建航母与远海海军，两国在印太的海权伸张已被广泛记录。  
  来源：<https://asia.nikkei.com/politics/defense/china-and-india-race-to-expand-aircraft-carrier-fleets>
- **#19** 「worldwide hegemonic struggles may only quicken in speed and intensity.」  
  判断：**正确**。2010年代后期至2020年代中期，美中俄大国竞争明显加速，中期战略评估已将其作为当代主轴。  
  来源：<https://inss.ndu.edu/Research-and-Commentary/View-Publications/Article/4414682/strategic-assessment-2025-evolving-great-power-competition-at-mid-decade/>
- **#23** 「There will not be the accumulation of masses of thermonuclear warheads that we saw during the Cold War, so tha…」  
  判断：**正确**。SIPRI 2026年全球库存约1.2万枚，远低于冷战高峰的数万枚规模，新核国家也未复制美苏式大规模堆积；相互确保摧毁的两极稳定并未简单再现。  
  来源：<https://www.sipri.org/media/press-release/2026/increasing-focus-nuclear-weapons-amid-heightened-escalation-risks-new-sipri-yearbook-out-now>
- **#24** 「increasingly the Chinese and Indian navies will be projecting power from the Gulf of Aden all the way to the S…」  
  判断：**正确**。中国海军已在亚丁湾、印度洋和南海常态存在，印度海军亦向东向西投送，符合沿整个可航行边缘地带投射力量的判断。  
  来源：<https://www.iiss.org/globalassets/media-library---content--migration/files/charting/china/2025/05/cc_chinese_influence_print.pdf>
- **#29** 「Almost all urban growth in the future will be in developing countries, specifically in Asia and Africa.」  
  判断：**正确**。几乎全部新增城市人口都出现在发展中地区、尤其亚洲和非洲，联合国贸发会议和城市研究都支持这一判断。  
  来源：<https://unctad.org/system/files/official-document/tdstat48_FS011_en.pdf/>
- **#34** 「Internal disorders could quickly spill over into whole regions, inflamed by mass media that reach across borde…」  
  判断：**正确**。叙利亚、利比亚、也门等内乱确实迅速外溢到邻国，并被跨境媒体和对外寻找敌人的逻辑放大。  
  来源：<https://edoc.ku.de/id/eprint/36812/1/farag-et-al-2026-media-systems-and-violent-conflicts-a-theoretical-framework-and-patterns-of-transformation.pdf>
- **#37** 「we will have new roads and ports and energy pipelines connecting the Middle East and Central Asia with the res…」  
  判断：**正确**。中亚、中东与中国、俄罗斯、印度洋之间的公路、港口和管道在“一带一路”和欧亚互联项目中大量新增，预测的互联方向已经发生。  
  来源：<https://eabr.org/upload/iblock/3c1/blacf9p2xjhoow8pe2nxq72ip6r8iusu/EDB_2026_ETN_Observatory_Executive_Summary_EN.pdf>
- **#41** 「But before the dullness completely sets in, there will upheavals and power shifts and natural」  
  判断：**正确**。乌克兰战争、新冠疫情和大国关系重组构成了明确的动荡与权力转移，发生在任何“沉闷均衡”之前。  
  来源：<https://www.foreignaffairs.com/world/out-alignment-war-in-ukraine-non-western-powers-shivshankar-menon>
- **#42** 「And indeed, in the twenty-first century, Europe will continue to be pivotally influenced by its relations with…」  
  判断：**正确**。2022年俄乌战争彻底改写欧洲安全秩序，欧洲命运再次被对俄关系决定，判断完全应验。  
  来源：<https://carnegieendowment.org/europe/research/2022/11/a-paradigm-shift-eu-russia-relations-after-the-war-in-ukraine>
- **#43** 「Yet Europe, precisely because of its quest for a wider and deeper unity, will also continue to be bedeviled by…」  
  判断：**正确**。欧债危机余波、英国脱欧和后续内部极化表明，欧盟在追求统一的同时持续受裂痕困扰。  
  来源：<https://securityconference.org/en/publications/munich-security-report-2025/chapter-4-european-union-a-perfect-polar-storm/>
- **#44** 「Europe, largely because of how technology facilitates the movement of peoples, will certainly see its history …」  
  判断：**正确**。欧盟统计局显示，近年首次庇护申请中亚洲和非洲籍占绝大多数，欧洲与非洲、亚洲的人口和历史交织明显加深。  
  来源：<https://ec.europa.eu/eurostat/web/interactive-publications/migration-2025>
- **#45** 「which will continue to contribute to political and economic disunity in the years to come, despite pan-Europea…」  
  判断：**正确**。英国脱欧及其他多重危机表明，泛欧机构并未消除政治与经济不统一。  
  来源：<https://academic.oup.com/book/31844/chapter/267484801>
- **#48** 「This will likely lead to increased immigration of young people from the Third World to support Europe’s aging …」  
  判断：**正确**。2015年难民危机及此后数年，欧盟接收大量来自欧盟以外的移民，老龄化与外来劳动力需求并行，判断已经应验。  
  来源：<https://ec.europa.eu/eurostat/web/interactive-publications/migration-2025>
- **#54** 「the European Union, albeit beset by divisions, anxieties, and massive growing pains, will remain one of the wo…」  
  判断：**正确**。欧盟虽经历分裂、增长之痛和多重危机，按购买力平价仍占全球产出可观份额，并保持为世界主要后工业经济中心之一。  
  来源：<https://www.statista.com/statistics/253512/share-of-the-eu-in-the-inflation-adjusted-global-gross-domestic-product/>
- **#56** 「To be sure, the Russians will not deploy land forces to reoccupy Eastern Europe for the sake of a new cordon s…」  
  判断：**正确**。俄罗斯出动陆军入侵了乌克兰，但并未出动陆军重新占领已加入北约的东欧国家以重建隔离地带。就该书针对北约东翼/原华约已入约成员的含义而言，这一判断成立。  
  来源：<https://quincyinst.org/research/right-sizing-the-russian-threat-to-europe/>
- **#58** 「Of course, the Soviet Union would never be reconstituted.」  
  判断：**正确**。苏联没有被重建。欧亚经济联盟等一体化方案存在，但并非恢复苏联，俄官方也公开表示在现有条件下恢复苏联不可能。  
  来源：<https://tass.com/politics/1372635>
- **#60** 「that doesn’t mean that Georgians, Armenians, or Uzbeks, with all the historical and emotional baggage that goe…」  
  判断：**正确**。格鲁吉亚、亚美尼亚、乌兹别克斯坦等国的主体认同仍是民族国家认同，并未因为欧亚一体化方案而改称或自视为“欧亚人”。  
  来源：<http://www.journals.uchicago.edu/doi/full/10.1086/708183>
- **#63** 「will probably not allow for the rebirth of a Russian empire to compete with Kievan Rus, medieval Muscovy, the …」  
  判断：**正确**。仅凭地理诉求并不足以让俄罗斯重生为可与基辅罗斯、罗曼诺夫或苏联比肩的帝国。2014年后的扩张尝试代价高昂，并未建成同等量级的新帝国。  
  来源：<https://www.dw.com/en/putins-russia-is-not-an-empire-despite-crimea-annexation/a-49166052>
- **#69** 「Thus, Russia will discipline its behavior in Central Asia and likely forswear any attempt to reclaim parts of …」  
  判断：**正确**。俄罗斯2012年后并未以武力收复中亚心脏地带。2022年集安组织进入哈萨克斯坦是应邀短期行动，随后撤离，与武力再征服不是一回事。  
  来源：<https://jamestown.org/russian-led-mission-in-kazakhstan-unveils-new-peacekeeping-model-part-one/>
- **#70** 「its annual GDP growth rates of over 10 percent for the past thirty years simply cannot continue—China, even in…」  
  判断：**正确**。中国已多年不再保持10%以上的GDP增速，同时仍是欧亚和全球地缘政治的中枢，判断的两部分都已应验。  
  来源：<https://chinapower.csis.org/tracker/china-gdp/>
- **#73** 「Again, no troops will be necessary as Greater China extends into Mackinder’s Eurasian Heartland, the upshot of…」  
  判断：**正确**。中国主要通过“一带一路”投资和互联互通向中亚心脏地带延伸，并未动用军队征服，与“不必动用军队”的判断一致。  
  来源：<https://theasanforum.org/chinas-strategic-thinking-toward-central-asia-2013-2024/>
- **#75** 「China and India will play a Great Game not only here, but in Bangladesh and Sri Lanka, too.」  
  判断：**正确**。中印在孟加拉国、斯里兰卡以及缅甸周边的港口、投资和外交竞争已被广泛记载，孟加拉湾成为双方博弈舞台，判断已经应验。  
  来源：<https://www.orfonline.org/research/ports-and-geopolitics-the-case-of-sino-indian-rivalry-in-the-bay-of-bengal>
- **#76** 「Mongolia, the Russian Far East, Central Asia, and Southeast Asia are all natural zones of Chinese influence an…」  
  判断：**正确**。中国在蒙古、中亚、东南亚和与俄远东经济联系中的影响明显上升，而中国正式政治边界没有相应改变，判断的两部分都成立。  
  来源：<https://thediplomat.com/2025/04/russias-complicated-strategic-frontiers-in-southeast-asia/>
- **#78** 「China will never annex any part of Korea, yet it remains frustrated by Korean sovereignty.」  
  判断：**正确**。中国没有吞并朝鲜半岛的任何部分；与此同时，朝核、萨德和半岛同盟问题持续使北京感到受挫，判断成立。  
  来源：<https://www.internationalaffairs.org.au/australianoutlook/korea-part-china/>
- **#82** 「China, which in the twenty-first century will project hard power primarily through its navy」  
  判断：**正确**。中国在二十一世纪投射硬实力的主要工具是海军及配套的海空导弹体系，航母、远海护航和南海岛礁部署都印证了这一点。  
  来源：<https://digital-commons.usnwc.edu/cgi/viewcontent.cgi?article=1054&context=cmsi-maritime-reports>
- **#83** 「China will field a fifth-generation fighter between 2018 and 2020, even as the United States slows or stops pr…」  
  判断：**正确**。歼-20约在2017年前后列装，与2018至2020年的时间窗口基本吻合；美国F-22生产已在该书出版前后停止，判断的核心内容成立。  
  来源：<https://www.businessinsider.com/how-china-j20-stealth-jet-compares-to-us-f22-fighter-2020-11>
- **#85** 「The U.S.-China relationship, I believe, will not only be determined by such bilateral and global issues as tra…」  
  判断：**正确**。美中关系的焦点正是台湾、南海和第一岛链等海洋亚洲的具体地理，而不是抽象的全球议程，判断已经应验。  
  来源：<https://www.lawfaremedia.org/article/the-geography-of-a-u.s.-china-war>
- **#89** 「we can call the South China Sea the Asian Mediterranean, since it will be at the heart of political geography …」  
  判断：**正确**。南海在2012年后成为印太政治地理的核心议题之一，岛礁军事化、仲裁和航行自由行动都印证了“亚洲地中海”式的中心地位。  
  来源：<https://www.rand.org/content/dam/rand/pubs/perspectives/PEA2000/PEA2021-1/RAND_PEA2021-1.pdf>
- **#90** 「China may seek to dominate the South China Sea in a similar way that the Americans dominated the Caribbean, wh…」  
  判断：**正确**。中国通过岛礁建设和灰色地带手段扩大在南海的控制；美国则与菲律宾、越南等加强合作，试图维持其作为国际水道，双方行为都符合预测。  
  来源：<https://www.armyupress.army.mil/Journals/Military-Review/English-Edition-Archives/Nov-Dec-2024/IW-South-China-Sea/>
- **#91** 「the risks of incidents at sea and fatal miscalculations about the balance of power—which everyone is seeking t…」  
  判断：**正确**。南海和周边海域的近距离接触、对峙和险些相撞事件在2012年后明显增多，误判风险随军事对峙复杂化而上升。  
  来源：<https://www.philstar.com/headlines/2026/03/28/2517342/philippines-vessel-avoids-crash-china-warship>
- **#93** 「the very fact of Chinese economic power—increasingly accompanied by military power—will lead to a pivotal degr…」  
  判断：**正确**。中国经济实力日益伴随军事实力，2018年后美中关系转入地缘政治竞争，紧张程度达到该书所说的关键水平。  
  来源：<https://www.nbr.org/publication/the-changing-character-of-u-s-china-economic-relations-from-competition-to-geopolitical-rivalry-2018-23/>
- **#96** 「The United States will draw down its troops in Afghanistan, but India will still have to live with the results…」  
  判断：**正确**。美国先是缩减、最终于2021年撤出阿富汗；印度仍须面对塔利班回归和地区后果，并保持外交与安全上的持续关注，判断应验。  
  来源：<https://foreignpolicy.com/2021/08/18/afghanistan-withdrawal-india-china-russia-pakistan-geopolitics-indo-pacific/>
- **#97** 「Its great power status in the new century will be enhanced by its very political and military competition with…」  
  判断：**正确**。印中政治军事竞争（包括边境对峙）提升了印度的大国能见度，同时巴基斯坦、阿富汗、尼泊尔等邻国问题继续构成牵制，两部分都成立。  
  来源：<https://www.brookings.edu/articles/indias-competitive-turn-toward-china/>
- **#105** 「pipelines radiate and will radiate from the Caspian region to the Mediterranean, the Black Sea, China, and the…」  
  判断：**正确**。里海油气管道继续向地中海、黑海和中国等方向延伸，南部天然气走廊等项目在2012年后建成或扩展，辐射格局已经出现。  
  来源：<https://www.energypolicy.columbia.edu/qa-the-geopolitics-of-caspian-gas/>
- **#108** 「Kazakhstan and Iran will also be linked by rail, providing Kazakhstan with direct access to the Gulf.」  
  判断：**正确**。哈萨克斯坦—土库曼斯坦—伊朗铁路已于2010年代开通，使哈萨克斯坦获得通往海湾方向的铁路线，判断应验。  
  来源：<https://tass.com/world/764933>
- **#110** 「And as the Iranian economic crisis continues to unfold, ordinary Iranians could well up in anger over hundreds…」  
  判断：**正确**。伊朗经济困境加深后，2018年以来抗议中多次出现“不要加沙、不要黎巴嫩，我们的命给伊朗”等口号，民众对海外撒钱的愤怒已经出现。  
  来源：<https://www.thecairoreview.com/tahrir-forum/questioning-irans-regional-ambitions/>
- **#111** 「This is to say nothing of how Iranians will become increasingly hated inside Iraq as the equivalent of “Ugly A…」  
  判断：**正确**。2019年伊拉克抗议者烧毁伊朗驻纳杰夫领事馆，民调也显示伊朗在伊拉克什叶派中的支持度下降，书中“越来越遭人憎恨”的判断应验。  
  来源：<https://www.reuters.com/article/us-iraq-protests/iraq-protesters-torch-iran-consulate-in-najaf-curfew-imposed-idUSKBN1Y11JI/>
- **#114** 「both Turkey and Iran will have their geographies further unleashed in order to play intensified roles in the A…」  
  判断：**正确**。2012年后土耳其和伊朗都在阿拉伯中东扮演了比此前更强的角色，地理邻近和历史通道被进一步激活，判断成立。  
  来源：<https://link.springer.com/article/10.1057/s41311-024-00625-1?code=e5ff86d7-079f-484c-abec-35a79bf9332c&error=cookies_not_supported>
- **#117** 「But as time passes, the geographies of Tunisia, Libya, Egypt, Yemen, Syria, and other countries will reassert …」  
  判断：**正确**。2011年后的希望消退后，利比亚的部落与东西分裂、也门的破碎化、埃及的核心地带治理和叙利亚的族群教派地理重新主导了政治结果，地理约束明显回潮。  
  来源：<https://www.iiss.org/online-analysis/online-analysis/2022/11/acs-2022-middle-east-and-north-africa/>
- **#118** 「Still, any Iraqi democracy that emerges in the second decade of the twenty-first century is going to be uncert…」  
  判断：**正确**。2011至2020年代的伊拉克选举政治伴随严重腐败、低效、派系冲突和多次政治暗杀，符合“不确定、腐败、低效且相当混乱”的判断。  
  来源：<https://freedomhouse.org/country/iraq/freedom-world/2020>
- **#119** 「a democratic Iraq, despite prodigious petroleum wealth and an American-trained military, will be a weak state …」  
  判断：**正确**。尽管有石油收入和美训部队，伊拉克在2014年伊斯兰国冲击中几乎崩溃，此后仍长期表现为弱国家，近判断完全应验。  
  来源：<https://www.bbc.com/news/world-middle-east-27883157>
- **#120** 「And its feuding politicians will reach out for financial and political support to contiguous powers—principall…」  
  判断：**正确**。伊拉克各派政客持续向伊朗和沙特等邻国寻求财政与政治支持，外部影响深刻嵌入国内权力斗争，成为其“玩物”的判断成立。  
  来源：<https://doi.org/10.7765/9781526150844.00010>
- **#121** 「The post-Mubarak era in Egypt, which has the Arab world’s largest population, will feature governments whose e…」  
  判断：**正确**。后穆巴拉克时代，无论穆尔西还是塞西政府，首要精力都用于对内巩固控制，塞西时期更明确重建警察国家，判断应验。  
  来源：<https://carnegieendowment.org/posts/2013/08/reconstructing-the-police-state-in-egypt>
- **#122** 「Struggles over water use will increasingly burden all these governments in the twenty-first century.」  
  判断：**正确**。尼罗河复兴大坝等争端使埃及等国在二十一世纪持续承受用水政治的压力，水资源斗争已成为外交和国内治理负担。  
  来源：<https://monitoring.bbc.co.uk/product/b0004ase>
- **#123** 「Geography and history tell us that Syria, with a population of twenty million, will continue to be the epicent…」  
  判断：**正确**。2011年后的叙利亚内战、难民潮和2024年政权更迭，使叙利亚长期处于阿拉伯世界动荡的中心，判断应验。  
  来源：<https://www.cfr.org/articles/syrias-civil-war>
- **#124** 「the next target of Sunni jihadists could be Syria itself」  
  判断：**正确**。2011年后，努斯拉阵线、伊斯兰国等逊尼派圣战组织把叙利亚作为主要战场和目标，预测已经应验。  
  来源：<https://www.tandfonline.com/doi/full/10.1080/13530194.2024.2373079>
- **#125** 「Syria appears destined to become a less centralized, and, therefore, a weaker state.」  
  判断：**正确**。战争使叙利亚出现多个实际控制区和并行治理结构，中央集权明显下降，国家能力变弱，即便2024年后仍高度碎片化。  
  来源：<http://hdl.handle.net/10419/197622>
- **#127** 「The crowd baying at real and perceived injustices is the new postmodern tiger that the next generation of Arab…」  
  判断：**正确**。2019年前后伊拉克、黎巴嫩、苏丹、阿尔及利亚等地的抗议潮表明，新一代领导人难以控制因不公而动员起来的人群，判断应验。  
  来源：<https://gsdrc.org/publications/responding-to-popular-protests-in-the-mena-region/>
- **#135** 「Mexico will assume more importance as time goes on.」  
  判断：**正确**。美墨加协定、近岸外包、边境安全和芬太尼问题都使墨西哥对美国的重要性在2012年后明显上升，判断应验。  
  来源：<https://www.everycrsreport.com/reports/IF11175.html>

### 趋势符合（34 条）

- **#1** 「This is something which Germans may yet recover, allowing them to move beyond the quasi-pacifism of the moment…」  
  判断：**趋势符合**。2022年朔尔茨“时代转折”演说后，德国显著提高防务开支并加强对东欧盟友的支持，走出准和平主义的方向已经出现；但2026年的民意研究显示，德国民众在防务问题上的转变并不彻底。  
  来源：<https://germanhistorydocs.org/en/a-new-germany-1990-2023/zeitenwende-policy-statement-by-chancellor-olaf-scholz-february-27-2022>；<https://link.springer.com/article/10.1007/s11615-026-00687-1>
- **#5** 「Eurasia and Africa together form the “World-Island,” something that as the decades march on will be increasing…」  
  判断：**趋势符合**。“一带一路”等互联项目使欧亚—非洲的铁路、港口和贸易联系明显加密，世界岛更具连通性；但远未成为一个政治上的整体单元。  
  来源：<https://doi.org/10.1007/978-981-16-8086-1_19>；<https://www.sociostudies.org/journal/files/jogs/2014_1/065-081.pdf>
- **#6** 「means that there will be a crisis of “room” on the map of the world.」  
  判断：**趋势符合**。全球城市化与远程导弹、防空体系压缩了地理距离，安全文献普遍把拥挤城市与远程打击视为新的空间压力，方向符合“空间危机”，但尚未形成该书所暗示的全面危机。  
  来源：<https://globalinitiative.net/wp-content/uploads/2024/10/v8-Urbanization-Peace-and-Security.pdf>；<https://www.weforum.org/agenda/2021/10/parag-khanna-move-book-excerpt/>
- **#10** 「The increased use of polar routes will lock the United States, Russia, and China in an ever tighter embrace.」  
  判断：**趋势符合**。北极航线、破冰船竞赛和防务部署使美俄中在北极的互动显著加密，方向是更紧密缠绕；但这种缠绕主要表现为竞争而非合作。  
  来源：<https://www.cnbc.com/2026/03/28/china-russia-arctic-polar-icebreaker-ships.html>；<https://quincyinst.org/research/restraint-and-diplomacy-in-arctic-policy-cooperation-amid-u-s-russia-china-tensions/>
- **#11** 「Geography, because it will be more accessible, will, counterintuitively, become more crucial.」  
  判断：**趋势符合**。全球化并未使地理过时，2012年后的战略讨论仍强调地理与地缘政治的关键性，与卡普兰的方向判断一致。  
  来源：<https://dergipark.org.tr/en/download/article-file/4480664>；<https://thestrategybridge.org/the-bridge/2019/6/4/the-revenge-of-geography-in-cyberspace>
- **#20** 「the very “finite size of the earth” would increasingly be a force for instability, as military hardware and so…」  
  判断：**趋势符合**。远程导弹与反介入体系压缩了战场距离，欧亚安全讨论把地缘与技术互动视为威胁上升的来源，方向符合有限地球带来的不稳定。  
  来源：<https://hcss.nl/wp-content/uploads/2021/12/Integrated-Air-and-Missile-Defense-HCSS-Dec-2021.pdf>；<https://www.nature.com/articles/ngeo2556?code=de9b8b7b-3eac-4d7d-8032-c948aa2018e4&error=cookies_not_supported>
- **#21** 「large forward bases like the kind the U.S. military maintained in Saudi Arabia and Kuwait prior to the two Gul…」  
  判断：**趋势符合**。海湾美军大型基地靠近伊朗、易受导弹与无人机打击的弱点已被广泛承认，基地区位脆弱性按预测方向显现。  
  来源：<https://www.cfr.org/articles/rising-u-s-casualties-in-the-iran-war-should-force-a-rethink-of-middle-east-bases>
- **#22** 「The geography of Eurasia will become as intimate as the geography of Europe, where a myriad of powerful states…」  
  判断：**趋势符合**。俄罗斯全面侵乌后，欧亚战略空间更局促，均势调整更频繁，方向接近“欧洲式挤迫”；但并非全大陆都进入持续热战。  
  来源：<https://www.csis.org/analysis/eurasias-shifting-balance-influence-opening-united-states>；<https://ponarseurasia.org/wp-content/uploads/attachments/Pepm366_Laruelle_July2015.pdf>
- **#25** 「while the population of the Greater Middle East grows from 854 million to over 1.2 billion over the next twent…」  
  判断：**趋势符合**。联合国世界人口展望显示，大中东及北非人口在2012年后继续大幅增长，方向指向十亿以上规模；是否在约2032年前达到12亿尚取决于分国汇总，但趋势明确。  
  来源：<https://population.un.org/wpp>；<https://data.worldbank.org/indicator/SP.POP.TOTL?locations=XQ>
- **#26** 「Crowded megacities, beset by poor living conditions, periodic rises in the price of commodities, water shortag…」  
  判断：**趋势符合**。特大城市确是抗议与激进动员的重要场所，同时导弹与现代军队也强化了若干政权；“民主与激进同时蔓延”只部分兑现，并非所有巨型城市都成为双重温床。  
  来源：<https://doi.org/10.1016/j.polgeo.2022.102693>
- **#30** 「A Eurasia and North Africa of vast, urban concentrations, overlapping missile ranges, and sensational global m…」  
  判断：**趋势符合**。2011年后中东、欧亚多次出现跨境传染的城市抗议浪潮，媒体放大了愤怒；但并非欧亚北非所有巨型城市都处于持续暴怒状态。  
  来源：<https://www.belfercenter.org/publication/contagious-protests>；<https://theconversation.com/we-live-in-a-global-age-of-rage-and-its-entering-a-new-phase-80173>
- **#32** 「politics in the mass media age will be more intense than anything we have experienced, because the past and fu…」  
  判断：**趋势符合**。极化、即时媒体和社交媒体使政治对抗明显更激烈，方向正确；“过去与未来被抹去”是修辞，难以单独核验。  
  来源：<https://doi.org/10.1177/20570473261455070>；<https://newrepublic.com/article/101797/occupy-movement-tea-party-polarization>
- **#35** 「Meanwhile, some states will slowly, inexorably lose the battle against globalization, as their bureaucratic ca…」  
  判断：**趋势符合**。脆弱国家指数显示多国在长期战争、难民和治理失败中能力持续受损，方向符合“输掉与全球化的较量”，但并非所有弱国都不可逆衰落。  
  来源：<https://fragilestatesindex.org/2025/02/18/a-world-adrift-the-failures-of-the-global-order-and-what-comes-next/>；<https://www.brookings.edu/articles/the-new-geopolitics-of-state-fragility/>
- **#39** 「smaller regions will emerge in bolder lines, as they did during the Middle Ages following the breakup of the R…」  
  判断：**趋势符合**。加泰罗尼亚、库尔德地区、顿巴斯等次国家区域认同明显上升，国家弱化处更小区域更鲜明，但并非全球普遍的“中世纪式”裂解。  
  来源：<https://www.cambridge.org/core/journals/european-political-science-review/article/lost-autonomy-triggers-and-the-rise-of-secessionism/33C784B42B3DB6CCE96007B76DFCA4A0>；<https://doi.org/10.34079/2226-2822-2021-11-21-41-52>
- **#46** 「the balance of power within Europe may shift slightly eastward to the confluence of Prussia and Mitteleuropa, …」  
  判断：**趋势符合**。德国对波兰和中东欧的投资持续领先，经济影响向东辐射的方向符合预测；但“均势东移至普鲁士与中欧交汇”只是部分实现。  
  来源：<https://www.ost-ausschuss.de/sites/default/files/pm_pdf/Studie%20KPMG-OA_2026.pdf>；<https://old.aspeninstitutece.org/article/2017/the-consequences-of-german-unification-for-europe/>
- **#47** 「Europe will lose 24 percent of its prime, working-age population by 2050, and its population of those over six…」  
  判断：**趋势符合**。欧盟人口预测确认劳动年龄人口下降、老龄人口大幅上升的方向，与书中24%和47%的定量描述同向；精确百分比以2050年终点为准，目前按官方基线情景趋势符合。  
  来源：<https://ec.europa.eu/eurostat/statistics-explained/index.php?+title=Population_projections_in_the_EU>；<https://www.ecb.europa.eu/press/economic-bulletin/focus/2026/html/ecb.ebbox202606_03~93f1f1d53c.en.html>
- **#49** 「the percentage of Muslims in major European countries will, in fact, more than triple by mid-century, from the…」  
  判断：**趋势符合**。皮尤研究中心对2050年欧洲穆斯林比例的预测大体落在该数量级，主要国家由低个位数升至接近或超过10%的情景存在；趋势符合，但“超过三倍、约10%”取决于移民情景。  
  来源：<https://www.pewresearch.org/religion/2015/04/02/europe/>；<https://www.pewresearch.org/religion/2025/06/09/religion-in-europe/>
- **#50** 「by 2050 the combined populations of Europe, the United States, and Canada will comprise just 12 percent of the…」  
  判断：**趋势符合**。联合国长期预测显示欧美加占世界人口的比重持续下降，朝向十几个百分点的量级，与约12%的方向一致；2050年确切数字以最新世界人口展望为准。  
  来源：<https://ourworldindata.org/grapher/population-regions-with-projections>；<https://www.foreignaffairs.com/articles/2010-01-01/new-population-bomb>
- **#55** 「the ongoing power shift within it, eastward from Brussels-Strasbourg to Berlin—from the European Union to Germ…」  
  判断：**趋势符合**。德国在欧盟中的相对权重上升，尤其在2022年后防务和财政讨论中更为突出，权势向柏林倾斜的方向出现；但布鲁塞尔机构仍是决策中心，所谓“从欧盟转向德国”并未完成。  
  来源：<https://www.ifri.org/sites/default/files/2026-01/ifri_suess_merz_european_policy_making_2026.pdf>；<https://www.taylorfrancis.com/chapters/edit/10.4324/9781003491224-18/hegemony-germany-odd-couple-joachim-schild>
- **#61** 「Indeed, because of low birth rates, high death rates, a high rate of abortion, and low immigration, Russia’s p…」  
  判断：**趋势符合**。俄罗斯生育率低、人口自然增长为负，官方和独立预测均指向2050年前继续下降；但2023年前后人口仍约1.45亿，降至1.11亿的终点尚未到来，目前只能判断趋势同向。  
  来源：<https://codexpopuli.org/country/russia/projections>；<https://www.ined.fr/en/all-about-population/data-graphs/projections-countries>
- **#66** 「Thus, a Russian sphere of influence will be challenging to preserve, and will be held hostage in some degree t…」  
  判断：**趋势符合**。俄罗斯在中亚的安全角色仍在，但相对地位因侵乌和中国影响上升而受损，能源价格波动也削弱了其杠杆，势力范围“难以维持”的方向符合事实。  
  来源：<https://fiia.fi/wp-content/uploads/2026/11/BP442_Russia-as-a-security-actor-in-Central-Asia.pdf>；<https://www.sipri.org/sites/default/files/files/books/SIPRI99Chu/SIPRI99Chu06.pdf>
- **#67** 「Russia’s new empire, if it does emerge, will likely be a weak reincarnation of previous ones, limited not just…」  
  判断：**趋势符合**。若把对乌战争视为新帝国尝试，其表现更接近受资源、后勤和外部制衡约束的弱小翻版，中亚则受中、印、伊影响上升所制约，条件性判断的方向成立。  
  来源：<https://www.asiamaior.org/the-journal/asia-maior-vol-xxxvi-2025/from-monopoly-to-dual-patronage-the-evolution-of-russian-and-chinese-influence-in-central-asia-1991-2025.html>；<https://en.wikipedia.org/wiki/Russian_conquest_of_Central_Asia>
- **#68** 「Reasonably good Russian-Chinese relations will provide momentum to the Shanghai Cooperation Organization」  
  判断：**趋势符合**。中俄关系总体保持稳定，上海合作组织从6个正式成员扩大到10个，为组织提供了发展动力；但扩员后的实质性成就仍然有限。  
  来源：<https://www.tandfonline.com/doi/full/10.1080/24761028.2026.2658324>；<https://carnegieendowment.org/russia-eurasia/politika/2024/07/sco-summit-china-russia>
- **#72** 「Given that China has absorbed Tibet, Macau, and Hong Kong on the mainland, Mongolia will be a trip wire for ju…」  
  判断：**趋势符合**。蒙古确实常被用作观察中国对外意图的风向标，其主权运作和第三邻国政策持续受到关注；但这是分析角色的延续，而非一条已被清晰触发的“红线”。  
  来源：<https://asiacentre.eu/wp-content/uploads/2025/12/10.Mikan_MGL.pdf>；<https://moderndiplomacy.eu/2026/08/04/the-only-way-south/>
- **#74** 「as the United States moves to defeat al Qaeda and irreconcilable elements of the Taliban, it is China’s geopol…」  
  判断：**趋势符合**。美国深陷阿富汗战争的年代，中国相对提升了在欧亚的经济与外交地位；2021年美军撤离后，中国的实际收获低于一些预期，增强是相对而非全面的。  
  来源：<https://jamestown.org/chinas-interests-in-afghanistan-one-year-after-the-u-s-withdrawal/>；<https://foreignpolicy.com/2021/08/20/china-russia-afghanistan-victory/>
- **#84** 「China likely has no intention of ever attacking a U.S. aircraft carrier.」  
  判断：**趋势符合**。截至截止日，中国并未攻击美国航空母舰，可观察结果与“无意攻击”一致；但反舰弹道导弹等能力建设表明存在作战准备，意图不能被完全证实。  
  来源：<https://www.navytimes.com/news/pentagon-congress/2015/01/16/navy-china-has-not-attacked-u-s-aircraft-carrier/>；<https://thediplomat.com/2017/01/no-china-did-not-target-a-us-carrier-with-ballistic-missiles-last-summer/>
- **#92** 「Oceania will grow in importance because it is sufficiently proximate to East Asia, while lying just outside th…」  
  判断：**趋势符合**。澳英美联盟、太平洋岛国竞争和美军基地讨论表明大洋洲的战略重要性上升，且多被置于中国反介入气泡之外；这一提升仍在进行中，尚未完全定型。  
  来源：<https://www.brookings.edu/wp-content/uploads/2023/02/FP_20230207_pacific_basing_jones.pdf>；<https://www.abc.net.au/pacific/programs/pacificbeat/australias-influence-declining-in-the-region/8724586>
- **#94** 「As the United States and China become great power rivals, the direction in which India tilts could determine t…」  
  判断：**趋势符合**。随着美中成为大国对手，印度在四边机制和印太战略中的分量显著上升；但“可能决定二十一世纪欧亚走向”的终点仍在百年尺度上，目前只能确认方向。  
  来源：<https://www.brookings.edu/articles/indias-competitive-turn-toward-china/>；<https://indianexpress.com/article/opinion/columns/with-russias-declining-influence-india-needs-a-new-strategy-in-eurasia-8160821/>
- **#95** 「if Americans do not come to grasp India’s highly unstable geopolitics, especially as it concerns Pakistan, Afg…」  
  判断：**趋势符合**。美国若忽视印巴阿中的复杂地缘，确实更容易处理失当；2012年后美印关系总体靠近，但也多次因俄罗斯、巴基斯坦和关税等问题出现摩擦，警告的方向成立。  
  来源：<https://doi.org/10.1080/14736489.2023.2180921>；<https://globalaffairs.org/commentary/analysis/india-united-states-relationship-trump-changed-things>
- **#99** 「Kashmir, like Palestine, because of the effect of cyberspace and new media, could still fire hatred among mill…」  
  判断：**趋势符合**。社交媒体和新媒体确使克什米尔议题在更大范围被动员；2019年废除370条后矛盾并未解决，问题更难缓解的方向成立，但并非简单复制巴勒斯坦式的全球动员强度。  
  来源：<https://www.orfonline.org/expert-speak/the-aftermath-of-article-370>；<https://www.csmonitor.com/World/Asia-South-Central/2013/0102/After-peaceful-2012-Kashmiris-urge-end-to-war-time-measures>
- **#106** 「whose navies may at some point in the twenty-first century share dominance with that of the United States in t…」  
  判断：**趋势符合**。中印海军在印度洋和欧亚海上通道的存在显著上升，美国不再是唯一主导者；但至2026年仍谈不上中印与美国“分享主导权”，只是多极化趋势已经出现。  
  来源：<https://www.tandfonline.com/doi/full/10.1080/10220461.2025.2509560>；<https://yalebooks.yale.edu/book/9780300234848/to-rule-eurasias-waves/>
- **#107** 「it seems likely that the Greater Middle East, and by extension Eurasia, will be critically affected by Iran’s …」  
  判断：**趋势符合**。伊朗的地区政策和内部政治持续影响大中东，并波及更广的欧亚平衡；但伊朗政治并未出现决定性转型，影响是重要的，未必已经“决定”整个地区走向。  
  来源：<https://bti-project.org/en/reports/country-report/IRN>；<https://mei.edu/publication/irans-playbook-arab-world-ideology-or-domestic-politics/>
- **#112** 「will make Turkey a greater power in the Arab Middle East in the twenty-first century than it was in the twenti…」  
  判断：**趋势符合**。土耳其在叙利亚、伊拉克和更广阿拉伯世界的军事与外交角色明显强于二十世纪大部分时期，幼发拉底河水利是其杠杆之一；但更强角色还有多重原因，并非主要由大坝系统单独造就。  
  来源：<https://carnegieendowment.org/research/2026/02/the-evolving-middle-eastern-regional-order-turkiye-iraq-relations-in-context>；<https://ciaotest.cc.columbia.edu/wps/usak/0030221/index.html>
- **#132** 「By 2050, one-third the population of the United States could be Spanish-speaking.」  
  判断：**趋势符合**。美国西班牙语人口持续增长，长期预测认为美国将成为全球最大西班牙语国家之一；但西班牙语使用者占比达到三分之一取决于2050年终点，且后代语言转用可能使该比例低于三分之一，目前只能判断趋势同向。  
  来源：<https://www.cnn.com/2015/07/01/us/spanish-speakers-united-states-spain>；<https://www.forbes.com/sites/soniathompson/2021/05/27/the-us-has-the-second-largest-population-of-spanish-speakers-how-to-equip-your-brand-to-serve-them/>

### 部分符合（32 条）

- **#7** 「there is no guarantee that the United States will remain the dominant outside power in a region in which under…」  
  判断：**部分符合**。中国对拉美贸易和投资在二十年内大幅上升，美国不再享有无可挑战的外部经济主导；但美国依地理邻近、市场和安全存在，仍是西半球最关键的域外行为体。  
  来源：<https://www.wilsoncenter.org/article/chinas-influence-latin-america-implications-united-states>；<https://carnegieendowment.org/research/2026/09/recasting-american-power-in-latin-america>
- **#15** 「where trade and economics will erode sheer military might, will still be one of geopolitics governed by geogra…」  
  判断：**部分符合**。全球海运仍高度繁忙，地理继续约束战略；但贸易与经济并未简单侵蚀军力，乌克兰战争后的制裁与军备扩张说明军力权重回升，原判断只对了一半。  
  来源：<https://unctad.org/system/files/official-document/rmt2025_en.pdf>；<https://unctad.org/press-material/review-maritime-transport-notes-drop-liner-competition-stresses-environmental>
- **#27** 「and that number will rise to forty by 2015, with all but two in the former Third World.」  
  判断：**部分符合**。2015年前后千万人口城市数量接近该书所说的四十量级，且绝大多数在发展中世界；但不同口径（市区或都会区）下，数字并不完全吻合“恰好40、除两座外都在前第三世界”。  
  来源：<http://docs.wbcsd.org/2018/01/Urban_Trends_Narrative.pdf>；<https://www.newgeography.com/content/004841-largest-1000-cities-earth-world-urban-areas-2015-edition>
- **#31** 「Conversely, the crowd, empowered by social media like Twitter and Facebook, will also be fed by the very truth…」  
  判断：**部分符合**。社交媒体在阿拉伯之春等事件中确曾传播被隐瞒的信息，但随后威权国家也用同一工具加强监控，真相扩散与压制并存。  
  来源：<https://www.eff.org/deeplinks/2026/04/digital-hopes-real-power-how-arab-spring-fueled-global-surveillance-boom>；<https://www.cambridge.org/core/journals/british-journal-of-political-science/article/online-social-media-and-political-awareness-in-authoritarian-regimes/DC37CC0F454D8E2FA74775D04FD97CEA>
- **#33** 「Mass education, because it produces hosts of badly educated people liberated from fatalism, will contribute to…」  
  判断：**部分符合**。部分发展中国家教育扩张与政治不稳定同时出现，但教育研究也常显示教育有助于民主态度，并非单向加剧动荡。  
  来源：<https://journals.library.ualberta.ca/jcie/index.php/JCIE/article/download/29709/21537/78949>；<https://www.epdc.org/sites/default/files/documents/Impact%20of%20Education%20Across%20Sectors%20-%20Democracy.pdf>
- **#36** 「as the map of Eurasia gets smaller thanks to technology and population growth, artificial frontiers will begin…」  
  判断：**部分符合**。后苏联空间和叙利亚等地出现边界争议与事实分裂，人造边界有所弱化；与此同时欧洲等地又在加筑边境设施，弱化并非单向。  
  来源：<https://www.ispionline.it/en/publication/borders-in-the-post-soviet-region-unfinished-business-190265>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC4917236/>
- **#38** 「The airplane, the Internet, the concentration of politics in vast cities that more and more look like one anot…」  
  判断：**部分符合**。互联网和城市化改变了部分地理约束，但地形、海峡和边境在战略上仍然关键，侵蚀并不彻底。  
  来源：<https://www.sciencedirect.com/science/article/abs/pii/S0264275122004280>；<https://www.usgs.gov/programs/national-geospatial-program/topographic-maps>
- **#40** 「the world will be both duller and more dangerous than ever before.」  
  判断：**部分符合**。大国竞争和战争使世界更危险，符合“更危险”的判断；“更沉闷”与持续危机并不吻合，2012年后冲突先降后升。  
  来源：<https://www.foreignaffairs.com/united-states/dangerous-decade-foreign-policy-world-crisis-richard-haass>；<https://reliefweb.int/report/world/human-security-report-2013-decline-global-violence-evidence-explanation-and>
- **#51** 「The Mediterranean will become a connector, rather than the divider it has been during most of the postcolonial…」  
  判断：**部分符合**。地中海两岸的人员流动、贸易和伙伴关系确实加深，具有连接者的一面；但欧盟南部边境管控、海上拦截和外部化政策同时把地中海重新变成硬隔离线。  
  来源：<https://www.iemed.org/wp-content/uploads/2021/03/Human-Mobility-in-the-Mediterranean-Basin-An-Integral-Element-of-the-Euro-Mediterranean-Partnership.pdf>；<https://www.eu-values.eu/blog/lost-at-sea-eu-values-and-the-southern-neighbourhood>
- **#52** 「Europe will now expand to the south to encompass the Arab revolutions.」  
  判断：**部分符合**。欧盟继续通过地中海伙伴关系与北非交往，但并未把阿拉伯革命“纳入其范围”：多数革命失败或被逆转，欧洲向南的政治扩展没有实现。  
  来源：<https://www.eeas.europa.eu/eeas/eu-and-north-africa_en>；<https://www.epsteinscan.org/pdf/1448948>
- **#53** 「Tunisia and Egypt are not about to join the EU, but they are about to become shadow zones of deepening EU invo…」  
  判断：**部分符合**。突尼斯和埃及确实没有即将加入欧盟；欧盟保持接触，但2013年后对埃及的介入并未稳定加深为书中所说的“阴影地带”，对突尼斯的深化也随政治回潮起伏。  
  来源：<https://www.eeas.europa.eu/eeas/eu-and-north-africa_en>
- **#57** 「Russia’s investment activities as well as its critical role as an energy supplier will loom larger in a weaken…」  
  判断：**部分符合**。2012年至2021年，俄罗斯作为欧洲能源供应方的角色确实更加突出；2022年全面侵乌后，欧洲大幅削减俄气依赖，投资与供应方地位转而急剧下降。  
  来源：<https://ciep.energy/media/pdf/uploads/THE%20POLITICAL-ECONOMIC%20DIMENSION%20OF%20TRANSFORMATIONS%20IN%20EU-RUSSIA%20GAS%20TRADE%20MECHANISMS%20secured.pdf>；<https://www.files.ethz.ch/isn/192240/Brief_22_energy_security.pdf>
- **#59** 「However, a looser form of union reaching to the borders of the Middle East and the Indian Subcontinent might s…」  
  判断：**部分符合**。欧亚经济联盟确实构成一种更松散的联合，但成员仅限俄、白、亚美尼亚和部分中亚国家，并未延伸到中东或印度次大陆边界。  
  来源：<https://www.crisisgroup.org/rpt/europe-central-asia/central-asia/240-eurasian-economic-union-power-politics-and-trade>；<https://afpc.org/publications/articles/slouching-toward-eurasia>
- **#64** 「Europe—especially Eastern Europe and the Balkans—will still be dependent on Russia to a significant degree.」  
  判断：**部分符合**。东欧和巴尔干在2010年代确实在相当程度上依赖俄罗斯天然气；2022年后多数国家大幅降低对俄依赖，原判断只在战争前成立。  
  来源：<https://www.tandfonline.com/doi/full/10.1080/14782804.2024.2385978>；<https://real.mtak.hu/33784/1/WP_221_Weiner.pdf>
- **#65** 「history will likely not repeat itself in the sense of another Russian empire emerging in the early twenty-firs…」  
  判断：**部分符合**。完整的新俄罗斯帝国并未在二十一世纪初成功再现；但2014年和2022年的吞并与全面战争表明，帝国工程已被重新付诸实施，历史并非简单“不会重演”。  
  来源：<https://carnegie.ru/2012/05/07/russian-empire-is-gone-for-good-pub-48098>；<https://www.atlanticcouncil.org/blogs/ukrainealert/putins-plan-for-a-new-russian-empire-includes-both-ukraine-and-belarus/>
- **#71** 「Having once conquered Outer Mongolia by moving the line of cultivation northward, China may be poised to conqu…」  
  判断：**部分符合**。中国在蒙古矿业和贸易中占据主导地位，经济渗透很深；但蒙古仍是主权国家，并推行“第三邻国”政策，所谓通过全球化“征服”并未发生。  
  来源：<https://www.nbr.org/publication/mongolias-development-of-critical-minerals-opportunities-and-challenges/>；<https://www.congress.gov/crs_external_products/R/PDF/R41867/R41867.12.pdf>
- **#81** 「the PLA ground force will not have an expeditionary capability for years to come.」  
  判断：**部分符合**。2012年后解放军的投送、海外基地和撤离能力明显提升，已具备有限远征手段；但对照美军仍不具备大规模、持续的远征陆军能力，原判断只对了一半。  
  来源：<https://www.uscc.gov/sites/default/files/2020-12/Chapter_3_Section_2--Chinas_Growing_Power_Projection_and_Expeditionary_Capabilities.pdf>；<https://www.nbr.org/publication/the-dawn-of-a-pla-expeditionary-force/>
- **#86** 「According to a 2009 RAND study, the United States will not be able to defend Taiwan from Chinese attack by 202…」  
  判断：**部分符合**。2020年并未发生对台进攻，因而“美国无法保卫台湾”没有被实战检验；此后多份兵棋推演显示美军防卫难度显著上升，力量对比恶化的方向与兰德判断相近，但“无法保卫”并未被证实。  
  来源：<https://www.rand.org/pubs/monographs/MG888.html>；<https://www.reuters.com/article/us-usa-china-taiwan-idUSKBN26T01W/>
- **#100** 「Between 1995 and 2025, the populations of Iraq, Jordan, Kuwait, Oman, Syria, the West Bank, Gaza Strip, and Ye…」  
  判断：**部分符合**。联合国人口数据表明，1995至2025年间伊拉克、约旦、科威特、阿曼、也门和巴勒斯坦人口大体翻倍或接近翻倍；叙利亚因战争人口明显少于翻一番，清单并非全部应验。  
  来源：<https://population.un.org/wpp/>；<https://www.worlddata.info/populationgrowth.php>
- **#101** 「The next generation of Middle Eastern rulers, whether in Iran or in the Arab states, will not have the luxury …」  
  判断：**部分符合**。社交媒体、青年结构和外部压力使一些统治者不能完全沿用旧式封闭专制；但埃及、海湾和伊朗等地的继任者在许多方面同样或更加威权，“无法像前任那样专制”并未普遍成立。  
  来源：<https://kalam.chathamhouse.org/containment-and-adaptation-governance-in-the-arab-world-after-2011/>；<https://carnegieendowment.org/middle-east/diwan/2018/11/how-will-the-new-generation-of-arab-leaders-compare-to-their-predecessors?center=middle-east&lang=en>
- **#102** 「the Middle East of the next few decades will make the recent era of Arab-Israeli state conflict seem almost li…」  
  判断：**部分符合**。2010年代中东冲突的主轴一度转向内战、代理人战争和海湾对立，阿以国家间战争显得相对遥远；2023年10月7日后的加沙战争和伊朗—以色列直接交火，又使国家间冲突回到前台。  
  来源：<https://www.csis.org/analysis/changing-military-dynamics-mena-region>；<https://api.pageplace.de/preview/DT0400.9781438419398_A43264305/preview-9781438419398_A43264305.pdf>
- **#103** 「if that high rate continues, its population will double in a few decades, putting enormous strain on resources」  
  判断：**部分符合**。沙特人口在2012年后继续增长并对资源构成压力；但接近2%的高增长率并未持续，联合国预测到2050年增速将明显放缓，按原假设“几十年内翻倍”的路径已经偏离。  
  来源：<https://data.worldbank.org/indicator/SP.POP.GROW?locations=SA>；<https://www.arabnews.com/business/saudi-arabia-faces-demographic-shift-as-birth-rates-decline-sectors-rethink-strategies-2626340>
- **#104** 「The future of teeming, tribalized Yemen will go a long way to determining the future of Saudi Arabia」  
  判断：**部分符合**。也门战争、胡塞武装袭击和边境安全确实深刻影响了沙特的安全与财政，但沙特未来仍更多取决于石油、国内改革和与美伊关系，也门并不是“在很大程度上决定”其未来的单一因素。  
  来源：<https://www.csis.org/analysis/iranian-and-houthi-war-against-saudi-arabia>；<https://themedialine.org/in-context/yemens-long-war-saudi-arabias-security-dilemma-and-the-shifting-middle-east/>
- **#113** 「some Arab states will go through en route to freer systems.」  
  判断：**部分符合**。埃及、突尼斯、苏丹等地在转型期确实出现过军方与文人政客分权的混合阶段；但其中多数并未走向更自由的制度，而是重新巩固军人或强人统治。  
  来源：<https://ddd.uab.cat/pub/tfg/2024/tfg_7687243/TFG_FINAL.pdf>；<https://www.iemed.org/wp-content/uploads/2021/02/The-Role-of-the-Military-in-Arab-Transitions.pdf>
- **#116** 「Western-style democracy may not exactly follow, but some form of liberalization eventually must」  
  判断：**部分符合**。西式民主确实没有紧随阿拉伯之春而来；但“某种形式的自由化最终必然出现”在多数国家并未兑现， Tunis 一度例外后也出现回潮，总体是局部、可逆的变化。  
  来源：<https://www.washingtoninstitute.org/policy-analysis/political-rights-and-civil-liberties-middle-east-trends-freedom-house-data-2010>；<https://www.foreignaffairs.com/articles/syria/2012-12-03/mirage-arab-spring>
- **#126** 「A weakened Syria could mean the emergence of Beirut as the cultural and economic capital of Greater Syria, wit…」  
  判断：**部分符合**。大马士革确实因战争和孤立付出了长期代价；但贝鲁特自身在2019年后陷入金融崩溃和政治失灵，并未成为“大叙利亚的文化和经济首都”。  
  来源：<https://arabcenterdc.org/resource/lifting-us-sanctions-on-syria-a-new-chapter-for-damascus-and-beirut/>；<https://www.persee.fr/doc/remmm_0997-1327_1990_num_55_1_2344>
- **#129** 「The destiny of the United States will be north–south, rather than the east–west, sea-to-shining-sea of contine…」  
  判断：**部分符合**。美国与墨西哥、中美洲的人口、贸易和安全联系确实使南北向变得更加重要；但美国战略重心同时明显转向印太，东西向的“两洋国家”定位并未被南北向取代。  
  来源：<https://www.migrationpolicy.org/publication/investing-neighborhood-changing-mexico-us-migration-patterns-and-opportunities>；<http://njbrepository.blogspot.com/2013/07/east-west-expansion-made-united-states.html>
- **#130** 「This will be amplified by the scheduled 2014 widening of the Panama Canal, which will open the Caribbean Basin…」  
  判断：**部分符合**。巴拿马运河扩建实际于2016年通航，晚于计划中的2014年；扩建后东亚至美国墨西哥湾的超大型船舶通道打开，海湾港口确有扩张，实质方向正确但时间推迟。  
  来源：<https://www.freightwaves.com/news/gulf-ports-expanding-their-way-to-bigger-profits>；<https://rosap.ntl.bts.gov/view/dot/34899/dot_34899_DS1.pdf>
- **#131** 「Yet Mexico could affect America’s destiny more than any of those countries.」  
  判断：**部分符合**。墨西哥通过贸易、移民、芬太尼和近岸外包深刻影响美国日常安全与繁荣，重要性高于许多中东议题；但并未清楚超过中国在美国大战略中的位置。  
  来源：<https://www.csis.org/analysis/why-us-mexico-security-cooperation-still-falling-short-washington>；<https://www.cfr.org/articles/greater-north-america-rethinking-the-geography-of-u-s-security-and-prosperity>
- **#133** 「America, I believe, will actually emerge in the course of the twenty-first century as a Polynesian-cum-mestizo…」  
  判断：**部分符合**。美国人口的拉丁裔和混血比重上升，与加拿大、墨西哥的经济社会联系加深；但把二十一世纪的美国定义为“玻利尼西亚兼混血文明”并完成南北取向转型，仍明显过满。  
  来源：<https://www.oupress.com/9780806157191/mestizos-come-home/>；<https://forum.slowtwitch.com/t/mexico-is-the-reason-why-us-standards-are-falling/605641>
- **#134** 「it will continue to use its immigration laws to asset-strip the world of its best and brightest, and to furthe…」  
  判断：**部分符合**。2012年后相当长时间内，美国继续通过职业移民吸纳全球人才，亚洲移民上升也使来源比亨廷顿所担忧的更加多元；2025至2026年对H-1B等高技能签证的限制，又削弱了“将继续吸纳最优秀人才”的后半段。  
  来源：<https://www.migrationpolicy.org/sites/default/files/publications/mpi_central-america-mexico-us-pathways-2024-final.pdf>；<https://www.cbsnews.com/news/trump-administration-100000-dollar-h-1b-visa-fee-impacting-u-s-ability-to-attract-global-talent/>
- **#136** 「future decades will see rail, road, and pipelines connecting all of Eurasia through a Central Asian and partic…」  
  判断：**部分符合**。欧亚大陆的铁路、公路和管道互联在中亚方向确有推进；但以阿富汗为枢纽打通整个欧亚的设想，因战争和政权更迭基本没有实现。  
  来源：<https://www.nbr.org/publication/afghanistan-a-junction-of-asias-connectivity/>；<https://www.iss.europa.eu/publications/briefs/unlocking-afghanistans-connectivity-potential-opportunities-eu>

### 错误（8 条）

- **#9** 「Supersonic transport may cut the distance between the west coast of the United States and cities in Asia by tw…」  
  判断：**错误**。截至2026年11月15日，美西海岸至亚洲的商业超音速航班并未开通，书中所说把航程缩短三分之二的效果没有出现。Boom等公司仍在研制超音速客机，但该书未写明更远终点，按出版日至截止日的隐含窗口，该能力预测未兑现。  
  来源：<https://boomsupersonic.com/wp-content/uploads/2025/07/Boom-Fact-Sheet-1.pdf>；<https://www.militaryaerospace.com/commercial-aerospace/article/55417548/what-was-the-fastest-commercial-passenger-plane>
- **#16** 「and with the possibility—because of budget cuts and cost overruns—of going down to 250 in the coming years and…」  
  判断：**错误**。2012年后美国海军舰艇数量并未降至250艘。海军历史统计与国会研究处报告显示舰队在约280至300艘上下波动，并讨论扩军目标，预测的下降并未兑现。  
  来源：<https://www.everycrsreport.com/files/2024-09-24_RL32665_30bb7761c5fb7be8feabaabff79ce083922a4b30.html>；<https://www.history.navy.mil/research/histories/ship-histories/us-ship-force-levels.html>
- **#28** 「over half of humanity now lives in urban conditions, a statistic that will rise to two-thirds by 2025.」  
  判断：**错误**。联合国《世界城市化展望》2025版显示，按该修订口径全球居住在城市的比例远未在2025年达到三分之二；即便按较早“城镇人口”口径，2025年也大约刚过六成，未到三分之二。  
  来源：<https://www.un.org/development/desa/pd/world-urbanization-prospects-2025>；<https://www.un.org/en/desa/WUP-2025>
- **#62** 「Russia’s nominal Muslim community is increasing and may make up as much as 20 percent of the country’s populat…」  
  判断：**错误**。“十年内占全国人口20%”对应约2022年。公开数据在2013年约为11%，此后十年未见达到20%的可靠统计，预测显著偏高。  
  来源：<https://www.ifri.org/sites/default/files/migrated_files/documents/atoms/files/laruelle_russia_islam_2021.pdf>；<https://www.theglobaleconomy.com/Russia/muslim/>
- **#77** 「But China is most incomplete on the Korean Peninsula, where political borders could well shift」  
  判断：**错误**。朝鲜半岛的政治边界（三八线/非军事区）在2012至2026年间并未发生实质变动。2026年朝方修宪调整统一表述，并不是书中所说的政治边界移动。  
  来源：<https://en.wikipedia.org/wiki/Geography_of_South_Korea>；<https://www.reuters.com/world/china/north-korea-revises-constitution-drop-references-unification-korean-peninsula-2026-05-06/>
- **#87** 「There will be less and less of a need for an invasion when subtle economic warfare will achieve the same resul…」  
  判断：**错误**。两岸经济联系并未降低军事统一的压力。2016年后台湾认同上升，解放军围岛军演和施压明显增强，经济战并未使“入侵必要性越来越小”。  
  来源：<https://www.uscc.gov/sites/default/files/031810%20Testimony_Kastner.pdf>；<https://nex.stimson.org/2025/rethinking-the-threat-why-china-is-unlikely-to-invade-taiwan/>
- **#98** 「If the Nepalese government cannot increase state capacity, the state itself could gradually dissolve.」  
  判断：**错误**。尼泊尔国家能力仍然薄弱，并反复出现政治动荡，但国家本身并未逐渐解体，预测的结果没有出现。  
  来源：<https://farsightnepal.com/news/political-change-without-institutionalisation-nepals-persistent-challenge-with-democratisation-and-state-capacity/>；<https://www.adb.org/sites/default/files/publication/1189836/governance-public-sector-management-nepal.pdf>
- **#115** 「The one in Syria is tyrannical but under intense siege from its own masses (and may not last to the time this …」  
  判断：**错误**。书于2012年出版，阿萨德政权并未在出版前倒下，而是一直维持到2024年12月；约旦也未变成君主立宪，仍大体维持国王主导的君主制并延续至今。两条核心判断都不成立。  
  来源：<https://www.congress.gov/crs-product/RL33546>；<https://www.crisisgroup.org/cmt/middle-east-north-africa/east-mediterranean-mena/syria/regional-perspectives-house-assads-fall>

### 暂无法判断（6 条）

- **#79** 「it is more likely than not that China, even though it fears reunification, will eventually benefit from it.」  
  判断：**暂无法判断**。朝鲜半岛统一尚未发生，中国是否“最终从中获益”无法在现有窗口内检验。  
  来源：<https://questia.com/library/journal/1P3-2969147901/china-s-cost-benefit-analysis-of-a-unified-korea>；<https://www.theatlantic.com/international/archive/2013/01/china-wouldnt-mind-a-unified-korea-just-not-yet/272492/>
- **#80** 「A reunified Korea tilting slightly toward China and away from Japan would be one with little or no basis for a…」  
  判断：**暂无法判断**。前提是统一后的朝鲜半岛向中国倾斜并疏远日本，这一条件至截止日并未出现，后续关于美军驻扎依据和日本再武装的推论无法检验。  
  来源：<https://english.hani.co.kr/arti/english_edition/e_northkorea/628913.html>
- **#88** 「Were the United States simply to abandon Taiwan, that could undermine America’s bilateral relationships with J…」  
  判断：**暂无法判断**。美国并未放弃台湾，条件未出现，因此对日韩菲澳等同盟关系受损的推论无法检验。  
  来源：<https://www.foreignaffairs.com/articles/china/2022-06-16/consequences-conquest-taiwan-indo-pacific>；<https://www.thinkchina.sg/politics/will-us-abandon-taiwan>
- **#109** 「I don’t believe we will see the true appeal of Iran, in all its cultural glory, until the regime liberalizes o…」  
  判断：**暂无法判断**。伊朗政权至截止日既未自由化也未被推翻，书中所说“文化魅力的真正展现”取决于这一前提，现有窗口无法检验。  
  来源：<https://monitoring.bbc.co.uk/product/b0005h81>；<https://www.theatlantic.com/international/2026/01/iran-revolution-protests-collapse/685578/>
- **#128** 「even if we do stabilize Afghanistan and Pakistan, China will be the main beneficiary, able to build roads and …」  
  判断：**暂无法判断**。前提是“即便美国稳定了阿富汗和巴基斯坦”，美国并未稳定这两国，中国也未能顺利在阿富汗建成规模化的公路与管道网络，条件未满足，结果无法按原表述检验。  
  来源：<https://chellaney.net/2021/07/30/china-moves-swiftly-to-exploit-the-void-in-afghanistan/>；<https://www.orfonline.org/expert-speak/afghanistan-pakistan-quagmire-reveals-the-limits-of-china-s-leverage>
- **#137** 「An organic and united Eurasia will demand as a balancer an organic and united North America, from the Canadian…」  
  判断：**暂无法判断**。这是一条条件性战略命题：有机联合的欧亚需要同样有机联合的北美作为平衡者。欧亚并未形成有机联合，北美一体化也未延伸到中美洲丛林，前提和结果都尚未出现。  
  来源：<https://www.brookings.edu/articles/the-usmca-can-help-make-north-america-the-economic-core-of-the-western-hemisphere/>；<https://carnegieendowment.org/posts/2016/10/transatlantic-relations-in-a-eurasian-world>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/kaplan-revenge-of-geography-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/kaplan-revenge-of-geography-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/kaplan-revenge-of-geography-v5/audit/manual_review_2026-11-15.py`

## 说明

- 本稿取代此前关键词筛选的人工稿（32 条可判定，严格胜率 60%）。新稿按原 DeepSeek 管线通读全书，每条预测都有存档证据。
- 第 9 条（超音速运输缩短美亚航程）书中未写明年份，按出版日至截止日的隐含窗口判断为错误；相关项目仍在研制，但不把未到期的远期能力记为暂无法判断。
- 第 56 条（俄罗斯不会出兵重新占领东欧）按上下文理解为已加入北约的东欧国家；俄罗斯入侵了乌克兰，但并未占领波兰、波罗的海等北约东翼。
- 第 115 条是复合判断：阿萨德“可能撑不到本书出版”与约旦绝对君主制的前景均不成立，整体记为错误。
- 统计以 pipeline.py report 的 summary.json 为准；本表的加权胜率按 manual_report.py 的权重计算。

