# J. B. S. 霍尔丹（J. B. S. Haldane）《代达罗斯，或科学的未来》（Daedalus; or, Science and the Future）：出版后预测人工核查

- 案例目录：`cases/haldane-daedalus-science-and-the-future-v5/`
- 出版日期：**1924 年**（纽约 E. P. Dutton，“To-day and To-morrow”丛书）。正文取自队列登记的 Project Gutenberg 纯文本 `reading-library/2026-11-15-未来判断扩展100本/05-技术与科学/095-daedalus-or-science-and-the-future.txt`（sha256 `8d90da9e271b54ebc158018415a3ea6d9695b7a82dca224d7958b89ac166afe9`，92,140 字符，与队列登记一致）。观察窗口为 1924→2026-11-15；书中明示的终点（如“1940 年”“1951 年”“1957 年”“1968 年”“五十年内”“下一个世纪内”“约 120 年”“四百年后”等）分别适用。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

本稿按 METHOD.md 执行。抽取：用仓库 prepare_book v5 流水线（toolkit 85e6da1）把全文切成 27 块（3500 字符、600 字符上下文）。助手按 DISCOVER_PROMPT_V5 逐块写出模型本应返回的 JSON，再由仓库代码完成引文对齐、归属降级、去重和导入，得到 79 条候选，其中 42 条可核验预测；仓库代码未划出任何 matter_spans（excluded_matter_spans 与 skipped_matter_chunks 均为空），27 块全部逐块完整通读；其中第 22–27 块为 Project Gutenberg 许可声明（正文于第 21 块内结束），逐块完整通读后 predictions 均为空；第 1–2、11–12 块通读后亦无作者预测。书中“一百五十年后剑桥本科生论文”所写的生物学史设想（含具体年份）按作者以虚构文体作出的预测抽取；明示的假设情景（3 条）、机制说明（1 条）、被作者反驳的观点（1 条）与格言（1 条）排除；37 条为 unclear（无可检验的作者断言或引述他人）。核验：每条预测先写 scope，第 1 轮各做一次 support 和一次 counter 的 Exa 检索（84 次），第 2 轮仅对 3 条证据不足者（#6 照明成本历史序列、#13 水电与工业区位、#16 风电制氢储能）再各做一次 support/counter（6 次），未启用第 3 轮或自适应轮；只使用检索返回的 URL。所选来源经 Exa 内容接口抓取并存档于 data/sources（122 份，sha256），写入 data/evidence.jsonl（122 条），由助手逐条阅读存档文本后按四分类规则评断，再经 pipeline.py apply assess → check → report。本稿以 v5 抽取的候选句（`data/claims.jsonl` 中可判定的条目）为起点，由助手逐条对照书中原文与存档证据人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 42 条，剔除非预测 0 条，计入 **42 条预测**，其中 **35 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 15 |
| 趋势符合 | 1 |
| 部分符合 | 9 |
| 错误 | 10 |
| 暂无法判断 | 7 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **42.9%**（15/35） |
| 加权胜率 | **57.9%** |
| 错误率 | **28.6%**（10/35） |
| 未定占比（暂无法判断/预测） | 16.7%（7/42） |

## 总体评价

霍尔丹对科学将持续扩张并深刻改变生活、相对论终被接受、照明成本大幅下降与城市夜晚普遍被照亮、产业相互依存加深、风与太阳能终被利用、铝成为第二大金属而不取代钢、星际通信、孟德尔遗传学融入思想与政治、国联和共产国际不会成为世界国家、下一场战争后方不再安全等判断成立；英国风电成为第一大电源按趋势符合计。部分符合集中在社会与医学：传染病大幅减少但未消灭、人类开始有能力做可遗传改造但未系统应用、阿片危机、激素疗法、化学阉割等。主要误判有：工人完全接管关键产业、水电带动工业重心迁往喜马拉雅山麓等地、核反应不可商用、Recresal 成为日常饮品、糖比锯末便宜，以及“论文”中给出具体年份的设想（1940 年固氮生物、1957 年固沙地衣、1951 年体外发育婴儿与出生率低于死亡率、1968 年法国每年 6 万体外婴儿）。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（15 条）

- **#1** 「so long as our present economic and national systems continue, scientific research has little to fear」  
  判断：**正确**。AAAS 2024 全球研发报告显示，经通胀与购买力调整后全球研发投入从 1992 年的 6720 亿美元增至 2021 年逾 2.2 万亿美元，三十年翻了三倍；在资本主义与民族国家体制延续下科研持续扩张，“科研无须担忧”的判断成立。近年个别国家削减经费不改变总体方向。  
  来源：<https://www.aaas.org/sites/default/files/2024-04/AAAS%20Global%20RD%20Update%202024.pdf>；<https://steps-centre.org/wp-content/uploads/rd-data.pdf>；<https://www.theatlantic.com/science/archive/2018/11/diminishing-returns-science/575665/>
- **#2** 「competitive nationalism, even if war is wholly or largely prevented, will hardly forego the national advantage…」  
  判断：**正确**。美国国会研究服务处资料显示，二战科研动员后联邦研发经费从 1947 年约 55 亿美元增至 1998 财年约 714 亿美元（1998 年美元）；NSF 回顾称布什《科学：无尽的前沿》以国防与国家利益为由推动大规模政府资助。国家未放弃科研带来的国家利益；阿根廷等近年削减属局部反例。  
  来源：<https://www.everycrsreport.com/files/19980814_95-1209_5099a81054a63d58f79d6d18b4572fe7270f5a2e.pdf>；<https://www.nsf.gov/science-matters/75-years-endless-frontier-vision-future-rooted-past>；<https://www.science.org/content/article/scienticide-argentina-s-science-workforce-shrinks-government-pursues-austerity>
- **#4** 「I do not doubt that he will be believed」  
  判断：**正确**。1920 年代反相对论小册子虽多，但研究指出反对者被逐步边缘化；2015 年 LIGO 首次直接探测引力波，信号与广义相对论预测无偏差，相对论已成为物理学公认理论，“他将被相信”成立。  
  来源：<https://physics.aps.org/articles/v9/52>；<https://www.ligo.caltech.edu/news/ligo20160211>；<https://journals.sagepub.com/doi/10.1177/0306312712469855>
- **#5** 「a better knowledge of the properties of radiation will permit us to produce it in a more satisfactory manner t…」  
  判断：**正确**。白炽灯整体效率仅约 2%（IEA），此后荧光灯、CFL 和白光 LED 相继商业化，美国 EIA 记录 LED 灯泡光效持续提高，人类以远比 1920 年代高效的方式产生光，方向成立。  
  来源：<https://www.eia.gov/tODAyinenergy/detail.php?id=18671>；<https://www.esource.com/sites/default/files/2025-01/esource-history-of-lighting-infographic.pdf>；<https://iea.blob.core.windows.net/assets/imports/events/12/Waide.pdf>
- **#6** 「in 50 years light will cost about a fiftieth of its present price」  
  判断：**正确**。Fouquet 序列（Exponential Tracker 数据）显示英国每百万流明小时照明成本（2000 年英镑）1920 年为 156.5 英镑、1970 年为 3.51 英镑，五十年降至约 1/45；按 1924→1974 插值约降至 1/34，量级与“约五十分之一”相符。  
  来源：<https://exponentialtracker.com/data/lighting_cost_lumen_hour.csv>；<https://exponentialtracker.com/curve/lighting_cost_lumen_hour>；<https://ourworldindata.org/light-at-night>
- **#7** 「there will be no more night in our cities」  
  判断：**正确**。《自然综述》2024 年指出全球 80% 人口生活在光污染天空下；2016 年全球夜空亮度图谱显示美欧 99% 人口受光污染，作者所指的（欧美）城市夜晚已普遍被人工照亮；拉各斯等发展中城市部分街区仍缺路灯，属作者语境之外的局部例外。  
  来源：<https://www.nature.com/articles/s43017-024-00555-9>；<https://darksky.org/news/80-of-world-population-lives-under-skyglow-new-study-finds/>；<https://www.african-cities.org/left-in-the-dark-understanding-streetlighting-provision-challenges-in-lagos-and-its-informal-settlements/>
- **#10** 「as industrial progress continues an ever larger number--perhaps the majority--of industries will become key in…」  
  判断：**正确**。CIGI 指出互联网使关键基础设施更复杂、更相互依存因而更脆弱，一处失效会连锁波及多个部门；BIS 2026 年公报显示咽喉点中断的宏观冲击扩散至能源、化肥、食品等行业，产业互相牵连、关键产业范围扩大的方向成立。  
  来源：<https://www.cigionline.org/articles/danger-critical-infrastructure-interdependency/>；<https://www.bis.org/publications/bulletin-138-chokepoint-disruptions-and-their-macroeconomic-consequences.pdf>；<https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/06/oecd-supply-chain-resilience-review_9930d256/94e3a8ea-en.pdf>
- **#12** 「Water-power is not, I think, a probable substitute」  
  判断：**正确**。2025 年水电仅占全球一次能源消费约 2.68%（statbase 汇总能源统计），IEA 称水电约占全球发电量 14%；化石燃料仍是主体，水电未成为煤和石油的替代品，判断成立。  
  来源：<https://statbase.org/datasets/energy/primary-energy-consumption-hydro/>；<https://www.iea.org/commentaries/hydropower-is-still-the-forgotten-giant-of-electricity-and-that-needs-to-change>；<https://www.columbia.edu/~jeh1/Data/EnergyConsump/WorldPrimaryEnergy2023_pies.pdf>
- **#14** 「Ultimately we shall have to tap those intermittent but inexhaustible sources of power, the wind and the sunlig…」  
  判断：**正确**。Ember 报告显示 2024 年可再生能源发电创纪录增长、低碳电力占全球发电 40.9%，太阳能领涨；风能和太阳能已被大规模利用，尽管化石燃料仍占一次能源大头，“终将利用风和阳光”的方向成立。  
  来源：<https://ember-energy.org/latest-insights/global-electricity-review-2025/2024-in-review/>；<https://ember-energy.org/latest-updates/world-surpasses-40-clean-power-as-renewables-see-record-rise/>；<https://www.carbonbrief.org/six-charts-show-how-clean-power-was-worlds-largest-source-of-new-energy-in-2025>
- **#18** 「I do not think that even when this is accomplished aluminium will oust iron and steel as they ousted bronze an…」  
  判断：**正确**。铝已是仅次于钢的第二大用量金属；2025 年全球原铝产量约 7400 万吨，远高于铜（2320 万吨），但 2024 年全球粗钢产量达 16.76 亿吨，铝未取代钢铁。“第二位、不取代钢铁”的判断成立。  
  来源：<https://www.cleanenergytransition.org/cmm/aluminum>；<https://igmnir.org/en/knowledge/compare/>；<https://worldsteel.org/wp-content/uploads/WSIF-2025-infographic.pdf>
- **#25** 「that it will be attempted I have no doubt whatever」  
  判断：**正确**。NASA 深空网络支持星际探测器通信，火星中继网络由多颗轨道器转发地表数据；1974 年阿雷西博射电望远镜还向 M13 星团发送了星际信息。星际通信早已被尝试并实现，预测成立。  
  来源：<https://www.nasa.gov/communicating-with-missions/dsn/>；<https://science.nasa.gov/mars/mars-relay-network/>；<https://archive.seti.org/seti-institute/project/details/arecibo-message>
- **#26** 「those of Weismann and Mendel will be digested in the course of the present century, and are going to affect po…」  
  判断：**正确**。孟德尔遗传学在 20 世纪与达尔文理论融合为“现代综合论”；剑桥大学出版社《Social Mendelism》等研究显示孟德尔遗传学深刻塑造了 20 世纪上半叶的优生政治与社会思想，被消化并影响政治理论的判断成立。  
  来源：<https://lareviewofbooks.org/article/eugenics-genetics-evolution-modern-synthesis-darwin-riskin-1/>；<https://www.cambridge.org/core/books/social-mendelism/9D75B07C66371E2A30653650DDB8444B>；<https://onlinelibrary.wiley.com/doi/full/10.1111/j.1469-1809.2011.00649.x>
- **#40** 「I believe that it will continue to do so, and even more profoundly than I have suggested」  
  判断：**正确**。CDC 称 20 世纪美国人均寿命延长 30 余年，其中 25 年归功于公共卫生进步；维基百科 20 世纪科学条目列举电力、汽车、计算机等技术的完善与普及。科学继续深刻改变人类生活，尽管有研究认为新想法越来越难找。  
  来源：<https://www.cdc.gov/mmwr/preview/mmwrhtmL/00056796.htm>；<https://en.wikipedia.org/wiki/20th_century_in_science>；<https://web.stanford.edu/~chadj/IdeaPF.pdf>
- **#41** 「I do not suggest that a world-state will arise from the present league--or for the matter of that from the thi…」  
  判断：**正确**。国际联盟未能阻止二战，于 1946 年 4 月解散，由联合国取代；共产国际于 1943 年 5 月解散。两者都没有发展成世界国家，作者的否定判断成立。  
  来源：<https://www.nationalww2museum.org/war/articles/league-of-nations>；<https://www.un.org/en/about-us/history-of-the-un/predecessor>；<https://www.nationalww2museum.org/war/articles/joseph-stalin-and-dissolution-comintern>
- **#42** 「In the next war no one will be behind the front line」  
  判断：**正确**。二战中德国对英国的“闪电战”连续轰炸伦敦等城市，造成 4 万多名平民死亡；二战平民死亡约 4500 万，远超约 1500 万战斗死亡，后方不再安全，预测成立。  
  来源：<https://encyclopedia.ushmm.org/content/en/timeline-event/holocaust/1939-1941/the-blitz-begins>；<https://www.nationalww2museum.org/students-teachers/student-resources/research-starters/research-starters-worldwide-deaths-world-war>；<https://blogs.lse.ac.uk/europpblog/2025/01/30/dark-figures-innocent-bystanders-the-civilian-victims-of-the-two-world-wars/>

### 趋势符合（1 条）

- **#15** 「four hundred years hence the power question in England may be solved somewhat as follows: The country will be …」  
  判断：**趋势符合**。情景终点为四百年后；但英国官方统计显示 2024 年风电发电量占比创纪录达 29.5%（84.1 TWh），风电成为英国第一大电源，并经高压电网输送，方向明确朝预测发展；2015–2024 年英格兰陆上风电曾被事实禁止，进程有波折。  
  来源：<https://www.renewableuk.com/news-and-resources/press-releases/official-stats-show-renewables-generated-over-half-uk-s-electricity-for-the-first-time-in-2024/>；<https://www.reuters.com/world/uk/wind-britains-top-electricity-source-2024-2025-01-07/>；<https://eciu.net/analysis/reports/2022/ban-on-onshore-wind-could-cost-800-million-this-winter>

### 部分符合（9 条）

- **#3** 「I have no doubt that Einstein’s name will still be remembered and revered when Lloyd George, Foch, and William…」  
  判断：**部分符合**。爱因斯坦至今仍被广泛尊崇（英国皇家学会 2005 年民调专门把他与牛顿比较谁对科学和人类影响更大），这一半成立；但作者预言将陷入“遗忘”的卓别林百年后仍是文化偶像（AV Club、NPR 2025 年报道《大独裁者》85 周年），对照组判断明显不成立，故部分符合。  
  来源：<https://royalsociety.org/news/2012/newton-einstein/>；<https://www.avclub.com/a-century-later-why-does-chaplin-still-matter-1798269769>；<https://www.npr.org/2025/10/15/nx-s1-5554555/the-great-dictator-charlie-chaplin-anniversary-hitler>
- **#8** 「the ideal of the leaders of industry, under no matter what economic system, will be directed less and less to …」  
  判断：**部分符合**。BCG 与贝恩报告显示，近年企业把供应链韧性和稳定性提升为与降本并列的优先事项；但 BCG 同时指出此前数十年企业优先降本增效，股东价值最大化自 1980 年代以来仍是主流管理原则，“越来越不追求产量扩张”只部分出现。  
  来源：<https://www.bcg.com/publications/2023/united-states-breaking-the-reactionary-cycle-by-investing-in-supply-chain-resilience>；<https://www.bain.com/globalassets/noindex/2024/bain_brief_how_ceos_can_balance_the_new_supply_chain_equation.pdf>；<https://en.wikipedia.org/wiki/Shareholder_value>
- **#24** 「disappearance of the agricultural labourer in favour of the factory worker」  
  判断：**部分符合**。农业劳动者大幅减少：FAO 称全球农业就业由 2000 年 10 亿人降至 2021 年 8.73 亿人，但规模仍巨大；但转移去向主要是服务业（服务业就业占比 1991–2019 年由 34% 升至 51%），撒哈拉以南非洲甚至“跳过工厂”，并非被工厂工人取代，仅部分符合。  
  来源：<https://openknowledge.fao.org/server/api/core/bitstreams/afd796fe-01c6-4edc-bd5d-9cc1457d068c/content>；<https://ourworldindata.org/data-insights/the-service-sector-now-represents-about-half-of-employment-across-the-world>；<https://cepr.org/voxeu/columns/skipping-factory-service-led-growth-sub-saharan-africa>
- **#27** 「Far more important was the progress in medicine which practically abolished infectious diseases in those count…」  
  判断：**部分符合**。天花于 1980 年被宣布在全球根除，传染病死亡率长期下降；但 WHO 2023 年十大死因中仍有下呼吸道感染，低收入国家十大死因中 7 项为传染病等可传播疾病，“全世界基本消灭传染病”未实现，仅部分符合。  
  来源：<https://www.who.int/news/item/08-05-2020-commemorating-smallpox-eradication-a-legacy-of-hope-for-covid-19-and-other-diseases>；<https://www.who.int/news-room/fact-sheets/detail/the-top-10-causes-of-death>；<https://ourworldindata.org/grapher/infectious-disease-death-rates-gbd?tab=line>
- **#34** 「it seems only a question of time before we shall be able to apply the same principles to our own」  
  判断：**部分符合**。2018 年贺建奎用 CRISPR 编辑胚胎并诞生双胞胎，表明人类已有能力对自身做可遗传改造；但这是未获许可的个案，此后科学界呼吁暂停并多国禁止，人类尚未像改造动物那样系统应用，仅部分符合。  
  来源：<https://www.nih.gov/about-nih/who-we-are/nih-director/statements/statement-claim-first-gene-edited-babies-chinese-researcher>；<https://www.nature.com/articles/d41586-018-07607-3>；<https://www.nature.com/articles/d41586-019-00726-5>
- **#35** 「As our knowledge of this subject increases we may be able, for example, to control our passions by some more d…」  
  判断：**部分符合**。以抗雄激素药物抑制性欲的“化学阉割”已被法国、美国加州等纳入对性犯罪者的处置，属以生理手段处理“变态本能”；但其通常作为假释或附加措施而非替代监禁，有效性证据不足且争议大，其余设想（控制情欲、刺激想象的试剂）未见证据，仅部分符合。  
  来源：<https://www.service-public.gouv.fr/particuliers/vosdroits/F35709?lang=en>；<https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PEN&sectionNum=645>；<https://www.dw.com/en/combating-sexual-violence-is-chemical-castration-a-valid-method/a-56839505>
- **#36** 「Conversely there will inevitably arise possibilities of new vices similar to but even more profound than those…」  
  判断：**部分符合**。新型合成阿片（芬太尼）带来更致命的成瘾危机：CDC 称 2023 年美国约 10.5 万人死于药物过量、其中约 76% 涉阿片；但 UNODC 称 1906 年全球阿片使用者占人口 1.5%，今天约 0.25%，按普及度并非“更深重”，仅部分符合。  
  来源：<https://www.cdc.gov/overdose-prevention/about/understanding-the-opioid-overdose-epidemic.html>；<https://www.unodc.org/documents/data-and-analysis/Studies/100_Years_of_Drug_Control.pdf>；<https://www.smithsonianmag.com/history/inside-story-americas-19th-century-opiate-addiction-180967673/>
- **#37** 「We are not likely to deal with them effectually on Pasteur’s lines」  
  判断：**部分符合**。肺结核恰恰是按针对病原体的路线被攻克：1943 年分离出链霉素，此后抗生素疗法有效治疗结核，与作者判断相反；癌症多数并非由特定病原体引起，治疗主要不走这条路，但 HPV 疫苗通过预防感染预防几乎全部宫颈癌，故仅部分符合。  
  来源：<https://www.nejm.org/doi/full/10.1056/NEJMra1205429>；<https://globaltb.njms.rutgers.edu/abouttb/historyoftb.php>；<https://www.cancer.gov/about-cancer/causes-prevention/risk/infectious-agents/hpv-vaccine-fact-sheet>
- **#38** 「When we can isolate and synthesize this body we shall be able to prolong a woman’s youth, and allow her to age…」  
  判断：**部分符合**。前提已满足：20 世纪上半叶研究者经数年研究提纯了多种雌激素，随即发展出治疗潮热、骨质疏松的疗法；WHI 等研究显示其能有效缓解血管舒缩症状，JAMA 2024 研究显示用过激素疗法者生物衰老差值较小，但并未使女性“像男性一样缓慢衰老”，且有血栓等风险，仅部分符合。  
  来源：<https://academic.oup.com/endo/article/160/3/605/5250672>；<https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2822953>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC3547645/>

### 错误（10 条）

- **#9** 「It is quite possible that capitalism itself may demand that the control of certain key industries be handed ov…」  
  判断：**错误**。最接近的是德国 1951 年煤钢产业对等共决制，工人只获得与资方对等的监事会席位而非完全控制；英国走的是国有化，矿工 1947 年后仍罢工。资本主义并未把关键产业控制权“完全”交给工人，主结果未出现。  
  来源：<https://strathprints.strath.ac.uk/54060/1/Zahn_HSIR_2015_German_codetermination_without_nationalization_and_British_nationalization.pdf>；<https://germanhistorydocs.org/en/occupation-and-the-emergence-of-two-states-1945-1961/co-determination-law-mitbestimmungsgesetz-may-21-1951>；<https://socialistworker.co.uk/in-depth/what-is-workers-control/>
- **#13** 「It may perhaps, however, shift the centre of industrial gravity to well-watered mountainous tracts such as the…」  
  判断：**错误**。水电确实吸引了个别高耗能产业（如不列颠哥伦比亚基蒂马特铝冶炼、冰岛铝厂），但全球工业重心转向的是中国：2023 年中国占全球制造业产出 29%，喜马拉雅山麓、不列颠哥伦比亚、亚美尼亚并未成为工业中心，主结果未出现。  
  来源：<https://www.statista.com/chart/20858/top-10-countries-by-share-of-global-manufacturing-output/>；<https://heritagebc.ca/industrial-heritage-location/kitimat-smelter-kemano-power-project/>；<https://www.nytimes.com/2017/07/01/us/politics/american-companies-still-make-aluminum-in-iceland.html>
- **#17** 「I do not much believe in the commercial possibility of induced radio-activity」  
  判断：**错误**。世界核协会称首批商用核电站 1950 年代投运，如今约 440 座反应堆提供全球约 9% 电力；2024 年核电发电量创 2667 TWh 新高。人工诱发核反应的商业利用早已实现，与作者判断相反。  
  来源：<https://world-nuclear.org/information-library/current-and-future-generation/nuclear-power-in-the-world-today>；<https://www.iaea.org/PRIS/WorldStatistics/NuclearShareofElectricityGeneration.aspx>；<https://world-nuclear.org/our-association/publications/world-nuclear-outlook-report/chapter-1-review-of-nuclear-energy>
- **#19** 「It is possible that it may become as normal a beverage as coffee or tea」  
  判断：**错误**。1932 年药理学文献已质疑 Recresal（酸性磷酸钠）的“所谓增效作用”；今天磷酸钠仅作为运动员赛前短期“磷酸盐负荷”的小众补剂，研究结果不一致，从未成为像咖啡或茶那样的日常饮品。  
  来源：<https://doi.org/10.1007/bf01925359>；<https://supp.science/supplements/sodium-phosphate/>；<https://journals.lww.com/nsca-scj/fulltext/2010/10000/phosphate_supplementation__an_update.5.aspx>
- **#20** 「in any case within the next century sugar and starch will be about as cheap as sawdust」  
  判断：**错误**。国际糖业组织 2024 年 11 月底 ISA 日价约 20 美分/磅（约 547 美元/吨），而锯末批发报价约 9.7 美元/吨至 120–150 美元/吨；一个世纪后糖仍比锯末贵数倍至数十倍，纤维素制糖也未商业化取代甘蔗甜菜糖，预测不成立。  
  来源：<https://www.isosugar.org/prices.php?pricerange=2024-11-01>；<https://www.lesprom.com/en/trade/Wood_sawdust_337/>；<https://www.tradewheel.com/p/mixed-wood-sawdust-1546020/>
- **#28** 「it was not until 1940 that Selkovski invented the purple alga _Porphyrococcus fixator_ which was to have so gr…」  
  判断：**错误**。1940 年并未出现人工培育的高效固氮生物；2024 年综述称 50 多年研究后仍无可靠证据显示谷物接种固氮菌能固定具农艺意义的氮量，2023 年综述也称谷物生物固氮工程仍面临重大挑战；基因编辑固氮微生物（Pivot Bio）至 2020 年代才商用，且未使小麦增产一倍。  
  来源：<https://link.springer.com/article/10.1007/s11104-024-07001-1>；<https://www.cell.com/plant-communications/fulltext/S2590-3462(22)00346-7>；<https://news.mit.edu/2025/pivot-bio-uses-microbial-nitrogen-sustainable-agriculture-0213>
- **#29** 「in 1957 produced the lichen which has bound the drifting sand of the world’s deserts」  
  判断：**错误**。1957 年并未出现固定全球流沙的地衣；生物结皮接种直到“近些年”才被视为有前景的旱地治理技术，2025 年沙丘固定综述与全球荒漠化治理综述仍在讨论固沙挑战，沙漠流沙并未被生物手段普遍固定。  
  来源：<https://onlinelibrary.wiley.com/doi/10.1002/ldr.3423>；<https://doi.org/10.1016/j.catena.2025.108786>；<https://onlinelibrary.wiley.com/doi/full/10.1111/sum.13154>
- **#30** 「It was in 1951 that Dupont and Schwarz produced the first ectogenetic child」  
  判断：**错误**。剑桥 2025 年《Artificial Womb on Trial》明言完全体外发育至今尚未实现；1978 年才诞生首例体外受精婴儿路易丝·布朗，且仍在母体妊娠。1951 年诞生体外发育婴儿的设想不成立。  
  来源：<https://www.cambridge.org/core/elements/artificial-womb-on-trial/F74D45F1B5AE2C2ACD8A51FDEDE482EA>；<https://www.lancaster.ac.uk/future-of-human-reproduction/major-themes/ectogenesis/>；<https://www.sciencenews.org/blog/growth-curve/40-years-ivf-baby-louise-brown>
- **#31** 「for the birth-rate was already less than the death-rate in most civilised countries」  
  判断：**错误**。该设想把“多数文明国家出生率低于死亡率”放在约 1951 年；实际欧洲 1951 年出生率 21.8‰、死亡率 11.9‰，正值战后婴儿潮。自然减少直到近年才在部分欧洲国家出现，设定时点的判断不成立。  
  来源：<https://commons.wikimedia.org/wiki/Data:Europe_Natural_population_growth.tab>；<https://www.ined.fr/sites/default/files/imported_images/pesa431.en.pdf>；<https://ourworldindata.org/data-insights/where-are-more-people-dying-than-being-born>
- **#32** 「France was the first country to adopt ectogenesis officially, and by 1968 was producing 60,000 children annual…」  
  判断：**错误**。法国首例试管婴儿 1982 年才出生，INED 称此后累计 40 余万例 IVF 活产，仍全部经母体妊娠；人工子宫至 2023 年仍只在讨论早产儿人体试验。1968 年法国每年 6 万体外发育婴儿的设想不成立。  
  来源：<https://www.ined.fr/en/all-about-population/issue-today/how-many-children-have-been-conceived-ivf-vitro-fertilization>；<https://www.cambridge.org/core/elements/artificial-womb-on-trial/F74D45F1B5AE2C2ACD8A51FDEDE482EA>；<https://www.cnn.com/2023/09/19/health/artificial-womb-human-trial-fda>

### 暂无法判断（7 条）

- **#11** 「the exhaustion of our coal and oil-fields is a matter of centuries only」  
  判断：**暂无法判断**。按 BP 2020 年数据，石油储采比约 54 年、煤炭约 139 年，但探明储量在过去 40 年反而翻倍（Gapminder）；“几个世纪内耗尽”的终点远在 2026 年之后，现有证据无法检验。  
  来源：<https://www.thenationalnews.com/business/energy/2024/06/24/oil-reserves-future-outlook/>；<https://www.gapminder.org/facts/fossil-fuel-reserves-arent-running-out/>；<https://ourworldindata.org/grapher/years-of-fossil-fuel-reserves-left>
- **#16** 「during windy weather the surplus power will be used for the electrolytic decomposition of water into oxygen an…」  
  判断：**暂无法判断**。利用富余风电电解制氢储能已有试点（如西班牙 IDOM 风电富余制氢项目），但 IEA 称 2023 年全球 97 Mt 氢气中低排放氢不足 1%，路透社报道大量绿氢项目被取消或推迟；该情景终点在四百年后，目前趋势尚不足以判定。  
  来源：<https://www.iea.org/reports/global-hydrogen-review-2024/hydrogen-production>；<https://www.idom.com/en/project/h2-verde-almacenamiento-de-excedente-de-energia-eolica-2/>；<https://www.reuters.com/sustainability/climate-energy/cancelled-postponed-green-hydrogen-projects-2025-07-23/>
- **#21** 「Many of our foodstuffs, including the proteins, we shall probably build up from simpler sources such as coal a…」  
  判断：**暂无法判断**。终点为约 120 年后（约 2044 年）。由空气/CO2 发酵合成蛋白已起步：Solar Foods 首座商业工厂 2024 年投产、年设计产能 160 吨 Solein，2026 年获 EFSA 安全评价；但规模极小，远非“完全令人满意的合成膳食”，终点未到，暂无法判断。  
  来源：<https://solarfoods.com/solar-foods-factory-01-has-reached-its-productivity-targets/>；<https://www.foodingredientsfirst.com/news/solar-foods-efsa-solein-fazer.html>；<https://www.the-innovation.org/article/doi/10.59717/j.xinn-life.2026.100200>
- **#22** 「This will mean that agriculture will become a luxury」  
  判断：**暂无法判断**。该预测以合成食品普及为前提；FAO 数据显示农业增加值占全球 GDP 比重恢复下降趋势、2022 年为 4.3%，但近半可居住土地仍用于农业，合成膳食并未普及，前提未满足，无法判定农业是否“变成奢侈品”。  
  来源：<https://www.fao.org/statistics/highlights-archive/highlights-detail/gross-domestic-product-and-agriculture-value-added-2013-2022.-global-and-regional-trends/en>；<https://ourworldindata.org/agricultural-productivity-crucial>
- **#23** 「mankind will be completely urbanized」  
  判断：**暂无法判断**。该预测以合成食品普及为前提，前提未满足；联合国《世界城市化展望 2025》按统一口径称城市居住人口占全球 45%，世界银行称 2008 年后城市人口才过半，“完全城市化”远未出现，但因前提未成立不作对错判定。  
  来源：<https://www.un.org/en/desa/WUP-2025>；<https://datatopics.worldbank.org/world-development-indicators/stories/from-water-to-electricity.html>
- **#33** 「As we know ectogenesis is now universal, and in this country less than 30 per cent of children are now born of…」  
  判断：**暂无法判断**。设想时点为约 150 年后（约 2073 年）。截至 2026 年尚无人类在人工子宫中妊娠，技术仅在动物模型（2017 年早产羔羊“生物袋”）阶段，完全体外发育可能还需数十年；终点未到且无可确认的趋势，暂无法判断。  
  来源：<https://familyfound.io/guides/artificial-wombs-ectogenesis>；<https://theconversation.com/artificial-wombs-could-someday-be-a-reality-heres-how-they-may-change-our-notions-of-parenthood-217490>；<https://www.nature.com/articles/ncomms15112>
- **#39** 「the face of the world and the possibilities of existence will be totally altered when we can control their eff…」  
  判断：**暂无法判断**。预测以“控制并标准化催眠与暗示的效果”为前提；荟萃分析显示催眠在医疗操作与疼痛中有一定疗效，但综述称其至今仍未被充分使用、技术不统一，前提未满足，无法判定世界是否因此被彻底改变。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC10807512/>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC4175906/>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/haldane-daedalus-science-and-the-future-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/haldane-daedalus-science-and-the-future-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/haldane-daedalus-science-and-the-future-v5/audit/manual_review_2026-11-15.py`

## 说明

- 第 22、23、39 条以合成食品普及、催眠与暗示被控制和标准化为前提，截至截止日前提未满足，记暂无法判断；第 1、38 条前提已满足，按结果判断。
- 第 11、16、21、33 条终点（几个世纪内、四百年后、约 2044 年、约 2073 年）未到且窗口内无可确认证据，记暂无法判断；第 15 条终点同为四百年后，但英国风电已成第一大电源，方向明确，按趋势符合计。
- 第 6 条“五十年内光价降至约五十分之一”：Fouquet 序列显示英国照明成本 1920→1970 年降至约 1/45，按 1924→1974 插值约 1/34，量级相符，计正确。
- 第 10 块“within the next century”跨行，horizon 字段留空，期限写入 claim 文本与 observation_end。
- 密度约 45 条可核验预测/10 万字符（扣除书末约 2 万字符许可声明后约 58 条），显著高于英文目标 8–10 条：本书是 1924 年的未来学小册子，几乎每段都是对未来的断言，且含带具体年份的虚构“论文”。
- 统计以 pipeline.py report 的 summary.json 为准；本表的加权胜率按 manual_report.py 的权重计算。

