# 勒庞《乌合之众》：出版后预测人工核查

- 案例目录：`cases/le-bon-the-crowd-v5/`
- 出版日期：1895
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

以85e6da1工具将Gutenberg445公开原文358860字符切为104块，逐块全部全文通读（matter_spans=[]）。手写104份答卷56条原始条目，确定性排除1机制→55候选、49resolvable、6unclear（其中5reported）；拒绝0、自动重叠去重0，无人工语义去重。工具下文候选49指可核验子集而非全部55候选。本稿以 v5 抽取的候选句（`data/claims.jsonl` 中可判定的条目）为起点，由助手逐条对照书中原文人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 49 条，剔除非预测 0 条，计入 **49 条预测**，其中 **34 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 9 |
| 趋势符合 | 0 |
| 部分符合 | 16 |
| 错误 | 9 |
| 暂无法判断 | 15 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **26.5%**（9/34） |
| 加权胜率 | **50.0%** |
| 错误率 | **26.5%**（9/34） |
| 未定占比（暂无法判断/预测） | 30.6%（15/49） |

## 总体评价

逐项区分群众影响与完全取代权威、社会主义兴起与实施后威望、法国分权与彻底摧毁中央集权。遥远世纪端点、未触发政策条件及无可操作文明指标保留未定；不以没有搜到反例自动判对。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（9 条）

- **#1** 「Still it is already clear that on whatever lines the societies of the future are organised, they will have to …」  
  判断：**正确**。存档学术摘要记载，十九世纪末至二十世纪初普选扩展改变欧美政治，现代群众社会中的权力需要群众支持；独裁研究亦把民众合法性列为生存条件。主要结果符合。  
  来源：<https://www.cambridge.org/core/books/abs/cambridge-history-of-twentiethcentury-political-thought/advent-of-the-masses-and-the-making-of-the-modern-theory-of-democracy/B5B8B77756023E5516F25F53502ECEDD>；<https://www.cambridge.org/core/books/two-logics-of-autocratic-rule/9C61972920FEE9E850313E54936A9D1E>
- **#3** 「Little adapted to reasoning, crowds, on the contrary, are quick to act. As the result of their present organis…」  
  判断：**正确**。关于二十世纪极权政治宗教的存档明确记述不容置疑的文本、无谬领袖和绝对服从，列明列宁主义、斯大林主义、法西斯主义和纳粹主义。新群众教条取得宗教式专断力量的结果出现。  
  来源：<https://www.degruyterbrill.com/document/doi/10.1515/9780804783682/html>；<https://yalebooks.yale.edu/book/9780300194128/contesting-democracy/>
- **#5** 「Universal symptoms, visible in all nations, show us the rapid growth of the power of crowds, and do not admit …」  
  判断：**正确**。1920年欧洲28国有26国是议会民主，群众力量在作者写作后并未迅速终止；但1938年前半数转为独裁，提示不能延伸为永远单向增长。  
  来源：<https://escholarship.org/content/qt8xf4t3t0/qt8xf4t3t0_noSplash_8f7474814cd22dec8d0f23599f84dc46.pdf>；<https://link.springer.com/chapter/10.1057/9781137333001_4?code=9b6721af-519a-4533-97ee-77102b9792d1&error=cookies_not_supported>
- **#8** 「The Christian ideas of the Middle Ages, the democratic ideas of the last century, or the social ideas of to-da…」  
  判断：**正确**。存档记载基督教民主以宗教观念与自由经济结合，1948—1949年已在多个欧洲国家成为突出或主导力量；2014年虽有衰退，相关政党集团仍赢得欧洲议会最多议席。观念长期影响国家行动的方向兑现。  
  来源：<https://academic.oup.com/policy-press-scholarship-online/book/42362/chapter/356580959>；<https://www.foreignaffairs.com/articles/western-europe/2014-07-15/end-christian-democracy>
- **#14** 「No doubt sanguinary wars and violent revolutions have been undertaken, and will continue to be undertaken, to …」  
  判断：**正确**。关于十月革命与伊拉克的存档均明确讨论以武力推行政治制度；1917革命此后深刻重画意识形态版图，伊拉克案例直接涉及外部强加民主，主要结果出现。  
  来源：<https://www.cambridge.org/core/books/cambridge-history-of-twentiethcentury-political-thought/russian-revolution-an-ideology-in-power/981B4AB8C3E68ED85476F5DCDD44B0F8>；<https://www.tandfonline.com/doi/full/10.1080/13510340902914338>
- **#19** 「To prove to us experimentally that dictators cost the nations who acclaim them dear, two ruinous experiences h…」  
  判断：**正确**。存档记载1940年议会给予贝当全面非常权力，随后集行政、立法等权力于一身。法国再次尝试独裁的主要结果出现。  
  来源：<https://www.smithsonianmag.com/history/vichy-government-france-world-war-ii-willingly-collaborated-nazis-180967160/>；<https://www.universalis.fr/encyclopedie/regime-de-vichy/2-l-instauration-d-un-nouveau-regime/>
- **#23** 「One of the most striking ones that posterity will recall from age to age will be supplied by the history of th…」  
  判断：**正确**。2020新闻争议和2021学术记忆研究仍围绕德雷赛普雕像，1895之后跨代记忆可观测；记忆性质由赞颂转为殖民争议，不等于被遗忘。  
  来源：<https://doi.org/10.4000/ema.14779>；<https://apnews.com/general-news-d7128f71fc990e8f9d9447dd1316facc>
- **#27** 「In consequence, the evident weakness of the socialist beliefs of to-day will not prevent them triumphing among…」  
  判断：**正确**。存档记载1912年德国社会民主党成为帝国议会第一大党，1919年取得近40%选票，主要结果即群众政治胜利确有发生。  
  来源：<https://encyclopedia.ushmm.org/content/en/article/communism-1>；<https://www.cambridge.org/core/journals/american-political-science-review/article/abs/redefining-the-political-system-of-the-ussr-mass-support-for-political-change/4126A645F4EA8766396B959AEADEB3D3>
- **#43** 「Moreover, wars, socialism, and economic conflicts hold in store for us a profusion of other catastrophes in th…」  
  判断：**正确**。马里兰大学存档汇总二十世纪战争冲突及政治决定相关死亡约2.31亿；MIT出版材料亦述世界大战及斯大林、毛泽东时期严重人为灾难。战争、社会主义和经济冲突继续带来众多灾难的主要结果出现。  
  来源：<https://gpi.umd.edu/research-impact/publications/deaths-wars-and-conflicts-20th-century>；<https://thereader.mitpress.mit.edu/the-mega-wars-that-shaped-world-history/>

### 部分符合（16 条）

- **#2** 「On the ruins of so many ideas formerly considered beyond discussion, and to-day decayed or decaying, of so man…」  
  判断：**部分符合**。君主制此后衰退，群众协调政治影响确有增强；但战后美国权力精英研究仍记录军方、大企业和政府领袖的权力集中，不能称群众力量吸收了其他一切权威。  
  来源：<https://journals.sagepub.com/doi/10.1177/0010414020938090>；<https://www.encyclopedia.com/social-sciences-and-law/sociology-and-social-reform/sociology-general-terms-and-concepts/power-elite>
- **#4** 「The divine right of the masses is about to replace the divine right of kings.」  
  判断：**部分符合**。德国1918—1919年转向对人民而非君主负责的政府，说明群众主权替代君权的核心方向出现；沙特仍有宗教合法化的绝对君主制，故非无例外替代。  
  来源：<https://www.facinghistory.org/resource-library/creating-constitutional-government>；<https://www.wilsoncenter.org/article/iran-v-saudi-arabia-four-part-series>
- **#9** 「Were it possible to induce the masses to adopt atheism, this belief would exhibit all the intolerant ardour of…」  
  判断：**部分符合**。苏联推行战斗无神论并迫害宗教领袖，另有学术存档把苏联无神论描述为含自身信念、实践与精神承诺的替代宇宙观，后果与预言相合；但学术资料也明确说苏共从未建立无神论社会，群众完全采纳的前提不能确认。  
  来源：<https://www.history.com/articles/joseph-stalin-religion-atheism-ussr>；<https://www.wilsoncenter.org/book/sacred-space-never-empty-history-soviet-atheism>
- **#15** 「Experience alone, that supreme educator of peoples, will be at pains to show us our mistake. It alone will be …」  
  判断：**部分符合**。1919年Astier法把技术教育组织化，并要求工商业18岁以下青少年每周接受职业课程，方向符合加强工业训练；但这并非全面取代课本和考试。  
  来源：<https://journals.ub.umu.se/index.php/njedh/article/download/293/211>；<https://eduscol.education.gouv.fr/4857/table-school-system-structure>
- **#17** 「Not truth, but error has always been the chief factor in the evolution of nations, and the reason why socialis…」  
  判断：**部分符合**。共产主义在1917年后通过战争革命扩展，证明社会主义确实成为重大未来力量；但1991年苏联意识形态和计划经济崩溃，不能说未来长期独属于它。  
  来源：<https://www.encyclopedia.com/social-sciences/encyclopedias-almanacs-transcripts-and-maps/communism-population-aspects>；<https://origins.osu.edu/article/soviet-collapse-yeltsin-putin-gorbachev-russia>
- **#18** 「Our century and that which preceded it will doubtless be alluded to by historians as an era of curious experim…」  
  判断：**部分符合**。后世牛津历史学者确把十九世纪拉美称为大型政治实验室，普林斯顿出版史著亦称其共和实验规模空前，支持后世以社会政治试验描述时代；尚不足覆盖两个世纪并验证所有时代中数量最多。  
  来源：<https://intellectualhistory.site.ox.ac.uk/article/revolution-republicanism-and-the-end-of-empire-latin-america-in-victorian-intellectual-histo>；<https://press.princeton.edu/books/hardcover/9780691161440/republics-of-the-new-world>
- **#21** 「The leader serves them as guide. It is just possible that he may be replaced, though very inefficiently, by th…」  
  判断：**部分符合**。大战报刊确能调动并维持公众支持，说明传播组织部分接过领袖功能；两级传播研究仍强调意见领袖的中介作用，不支持报刊完全替代。  
  来源：<https://www.bloomsbury.com/us/call-to-arms-9780275973834/>；<https://doi.org/10.1002/9781405186407.wbiect063>
- **#25** 「It is in defence, too, of such beliefs that the world has been so often the scene of the direst disorder, and …」  
  判断：**部分符合**。第一次世界大战史存档明确记载数百万人死亡；报刊史表明多国报纸以共同理想动员并维持战争支持，二战史亦确认政治信念的战争作用。可是战士动机研究同时强调求生与战友纽带，不能把所有战场死亡都明确归于保卫信仰。  
  来源：<https://doi.org/10.1093/oxfordhb/9780199341795.013.22>；<https://mlpp.pressbooks.pub/modernworldhistory/chapter/world-war-ii/>；<https://www.bloomsbury.com/us/call-to-arms-9780275973834/>；<https://digitalcommons.providence.edu/history_undergrad_theses/11>
- **#32** 「given the power possessed at present by crowds, were a single opinion to acquire sufficient prestige to enforc…」  
  判断：**部分符合**。纳粹利用宣传和审查压制异见，苏联科学独立直至开放时代仍受侵蚀，结果部分相符；但资料不足证明某意见已普遍被接受才触发压制的因果条件。  
  来源：<https://encyclopedia.ushmm.org/content/en/article/nazi-propaganda-and-censorship>；<https://doi.org/10.1080/13523279808415389>
- **#33** 「Given the growing influence of crowds and the successive capitulations before them of those in authority, we a…」  
  判断：**部分符合**。法国档案馆明确记录1944年权威瓦解、群众正义及报复蔓延，包括民兵被法外处决；因此类似群众暴行确曾重现。但是这些资料不能单独证明由群众力量持续增长、当局屡次向群众让步这一组合前提触发。  
  来源：<https://shs.hal.science/halshs-02142376>；<https://francearchives.gouv.fr/fr/article/877558609>
- **#41** 「It is evident that the continued growth of expenditure of this kind must end in bankruptcy.」  
  判断：**部分符合**。法国公债与公共开支在1960—2024明显增加，专项存档又记录1932年停止偿还对美战争债务，财政偿债困难确实出现。可是该外债违约并未证明由选举性养老金和地方支出必然导致国家整体破产；IMF记载的国内债融资延续构成边界。  
  来源：<https://www.parisschoolofeconomics.eu/app/uploads/2026/02/the-evolution-of-public-spending-in-france-by-francois-langot-fabien-tripier.pdf>；<https://www.robert-schuman.eu/en/european-issues/850-out-of-debt>；<https://gripe.polisci.ucla.edu/wp-content/uploads/sites/121/2022/09/GRIPE_S06E02_GILL.pdf>；<https://www.elibrary.imf.org/display/book/9781513511795/ch004.xml>
- **#42** 「Many European countries--Portugal, Greece, Spain, Turkey--have reached this stage, and others, such as Italy, …」  
  判断：**部分符合**。IMF存档描述1920年代强制债务转换为部分违约，说明偿债危机部分出现；但距1895已三十余年，不能等同不久即破产，且部分违约不是国家全面破产。  
  来源：<https://www.elibrary.imf.org/display/book/9781513511795/ch005.xml>；<https://doi.org/10.1017/cbo9780511628528.018>
- **#44** 「This progressive restriction of liberties shows itself in every country in a special shape which Herbert Spenc…」  
  判断：**部分符合**。法国官方确认2011—2022公务人员增6.1%，长时段研究估1980—2019增长约三分之一；人数扩张符合，但存档并未分别识别新增限制法与官员权力影响增长的因果。  
  来源：<https://www.fonction-publique.gouv.fr/toutes-les-publications/rapport-annuel-sur-letat-de-la-fonction-publique-edition-2024>；<https://www.ifrap.org/fonction-publique-et-administration/1980-2019-quelle-evolution-des-effectifs-de-la-fonction-publique-et-de-la-masse-salariale>
- **#45** 「These functionaries tend in this way to become the veritable masters of civilised countries.」  
  判断：**部分符合**。2022法国行政精英研究描述高级公务员与政治人物合成强有力国家精英；2024独立治理评估同时确认民主制度和权利讨论依然稳固。官僚势力确大，成为所有文明国家真正主人的强断言未全实现。  
  来源：<https://doi.org/10.4337/9781839109447.00034>；<https://www.sgi-network.org/2024/France/Executive_Summary>；<https://www.sgi-network.org/2024/France/Horizontal_Accountability>
- **#46** 「This incessant creation of restrictive laws and regulations, surrounding the pettiest actions of existence wit…」  
  判断：**部分符合**。行政法规和国家作用有扩张，但剑桥法律研究强调宪法、欧盟法和人权公约制约；Sciences Po年表列1944妇女普选、1960废强迫劳动和1981废死刑，非所有自由持续单向收窄。  
  来源：<https://www.cambridge.org/core/books/contemporary-french-administrative-law/introduction/EEC35F3F6A1137BB1AA3B9177AEE9B2B>；<https://espace-mondial-atlas.sciencespo.fr/en/topic-contrasts-and-inequalities/map-1C25-EN-democracy-building-in-france-1789-2018andnbsp.html>
- **#48** 「The functions of governments necessarily increase in proportion as the indifference and helplessness of the ci…」  
  判断：**部分符合**。IMF存档指出二十世纪政府税收占比由不足10%增至30%—50%，政府社会职能扩张明确；英国历史研究却称公民参与并未衰退、福利国家促进志愿组织，不能确认增长的冷漠无能这一前提。  
  来源：<https://www.imf.org/-/media/files/publications/fandd/article/2022/march/saez.pdf>；<https://historyandpolicy.org/policy-papers/papers/the-big-society-civic-participation-and-the-state-in-modern-britain/>

### 错误（9 条）

- **#13** 「Were it possible to bring about the decentralisation which is to-day preoccupying minds lacking in foresight, …」  
  判断：**错误**。宪法委员会的40年回顾描述1982年权力转移、持续的机构改革和宪法审查；参议院记录改革依正常立法推进。法国实现分权却未迅速滑入原文所称极其血腥动乱。  
  来源：<https://www.conseil-constitutionnel.fr/publications/titre-vii/1982-2022-quarante-ans-de-decentralisation-en-france>；<https://archives.senat.fr/en-2025-le-senat-fete-ses-150-ans/la-loi-du-2-mars-1982-socle-de-la-decentralisation.html>；<http://repub.eur.nl/pub/758>
- **#26** 「In practice they have created an entirely new civilisation, and for fifteen centuries have given mankind a gli…」  
  判断：**错误**。剑桥存档记录1906年兴起的五旬节复兴，现有约五亿人，核心包括日常预言、信仰疗愈和异象；贝勒学者也明确否定宗教必然崩溃的简单世俗化论。基督教梦想和希望并未再不可体验。  
  来源：<https://doi.org/10.1017/ccol9780521886536.016>；<https://ifl.web.baylor.edu/conferences-and-symposiums/baylor-symposium-faith-and-culture/2009-secularization-and-revival>
- **#28** 「The socialist ideal of happiness being intended to be realised on earth, the vanity of its promises will at on…」  
  判断：**错误**。剑桥史述记载苏联威望在1939年前低落、二战结束后却反转并得到远超共产主义阵营的承认。实施社会主义多年后仍能获得显著威望，与一经实行便完全失去威望不符。  
  来源：<https://doi.org/10.1017/cho9781139524377.006>；<https://www.encyclopedia.com/history/encyclopedias-almanacs-transcripts-and-maps/new-economic-policy-nep>
- **#29** 「Its strength, in consequence, will only increase until the day when, having triumphed, its practical realisati…」  
  判断：**错误**。1917年俄国已开始建立苏维埃政权；剑桥共产主义史明确记录二战后共产主义国家和运动继续崛起并向亚非拉扩展，增长没有停在首次胜利实施日。  
  来源：<https://www.encyclopedia.com/history/modern-europe/russian-soviet-and-cis-history/october-revolution>；<https://arxiujosepserradell.cat/wp-content/uploads/2025/10/The_Cambridge_History_of_Communism_Volume_2_the_Socialist_Norman.pdf>
- **#30** 「For this reason, while the new religion exerts to begin with, like all those that have preceded it, a destruct…」  
  判断：**错误**。世界银行存档确认苏联教育在严重社会经济动荡下获得发展，百科存档也说明1928年后建立重工业与集体化制度。无创造任何东西的绝对断言与这些制度及生产建设不符。  
  来源：<https://documents1.worldbank.org/curated/en/363441468768731106/pdf/multi0page.pdf>；<https://www.encyclopedia.com/history/encyclopedias-almanacs-transcripts-and-maps/industrialization-soviet>
- **#31** 「they have reached the point of suppressing literary criticism, confining themselves to citing the title of a b…」  
  判断：**错误**。预测截止约1915年；2014学术活动简介明确记载Comœdia剧场艺术文学日报1907—1937年持续出版，并在1920—1930年代继续生涯，故戏剧评论未在二十年期限内消失。  
  来源：<https://www.fabula.org/actualites/63556/comoedia-1907-1937-un-continent-inexplore-dans-l-histoire-du-the-tre.html>；<https://fr.wikisource.org/wiki/Revue_dramatique_-_14_octobre_1913>
- **#35** 「It should thus be clear that were the accused to be definitely judged by magistrates instead of by jurymen, he…」  
  判断：**错误**。法国五名职业法官组成的省级刑事法院实际替代部分陪审案件；评估记录428人被定罪、25人获无罪，无罪率5.5%。职业法官裁判并未消灭被告获无罪的机会，主结果与预测相反。  
  来源：<https://www.assemblee-nationale.fr/dyn/opendata/PIONANR5L16B1205.html>；<https://www.france-victimes.fr/index.php/informations-pratiques/1245-rapport-du-comite-d-evaluation-et-de-suivi-de-la-cour-criminelle-departementale>
- **#40** 「In each country the average opinions of those elected represent the genius of the race, and they will be found…」  
  判断：**错误**。法国政党研究在1978—2002四次选举间发现政治分歧结构深刻变化、欧洲整合及新文化冲突重组左右派并产生新主要政党，不支持当选者平均意见代际基本不变。  
  来源：<https://www.tandfonline.com/doi/full/10.1080/01402380802670677>
- **#47** 「Accustomed to put up with every yoke, they soon end by desiring servitude, and lose all spontaneousness and en…」  
  判断：**错误**。法国社会史直接记录工会、社团即使在法律宽容之前也富有活力；1968年群众广泛动员和抗议反证国民已不久必失自发活力而只求服从。  
  来源：<https://sciencespo.hal.science/hal-01312431/file/2005-lemercier-la-france-contemporaine.pdf>；<https://nvdatabase.swarthmore.edu/content/french-students-and-workers-campaign-reform-may-revolt-1968>

### 暂无法判断（15 条）

- **#6** 「Certainly it is possible that the advent to power of the masses marks one of the last stages of Western civili…」  
  判断：**暂无法判断**。存档记载了两次世界大战和政治冲击，也记录西欧和北美1950—1973年的经济与生活水平大幅恢复；尚无法把这些变化等同于作者未定义的西方文明末期或完全回归无政府状态。  
  来源：<https://www.commentary.org/articles/arnold-toynbee/can-western-civilization-save-itselfour-present-anxiety-in-the-light-of-history/>；<https://aeon.co/essays/postwar-prosperity-depended-on-a-truce-between-capitalism-and-democracy>；<https://press.princeton.edu/books/hardcover/9780691203485/western-europes-democratic-age>
- **#7** 「Under the Bourbons Napoleon became a sort of idyllic and liberal philanthropist, a friend of the humble who, a…」  
  判断：**暂无法判断**。原文终点是几十个世纪以后，远超2026观察窗；2024年拿破仑基金会仍在整理真实书信，既不能提前判错，也不能把1827年的太阳神话讽刺小册子当作预言兑现。  
  来源：<https://fondationnapoleon.org/en/2024/01/03/the-general-correspondence-of-napoleon-bonaparte-all-the-letters-are-now-available-on-napoleonica-les-archives/>；<https://opensiuc.lib.siu.edu/ocj/vol1903/iss7/1>
- **#10** 「The biological sciences have been transformed since embryology has shown the immense influence of the past on …」  
  判断：**暂无法判断**。长时段史学和遗传/种族研究的深刻更新均见于存档，但尚无材料把它们与胚胎学的变革幅度作同口径比较，也不能证明是接受作者的遗传观念所致。  
  来源：<https://www.cambridge.org/core/journals/annales-histoire-sciences-sociales-english-edition/article/abs/whats-bred-in-the-bone-the-social-sciences-coming-to-grips-with-biological-determinism-review-article/1C7EF8410F2AC1C8178F0C76BF4024B8>；<https://doi.org/10.4000/ccrh.2362>
- **#11** 「At the present day we are very uneasy with regard to the threatening aspirations of the masses and the destruc…」  
  判断：**暂无法判断**。存档既记载1870—1914年共和政府巩固，也记载1940年迅速崩溃；时间本身、不靠其他干预恢复哪一种均衡仍缺可区分的事实标准。  
  来源：<https://www.taylorfrancis.com/books/mono/10.4324/9781315841885/france-1870-1914-robert-gildea>；<https://doi.org/10.1093/oso/9780198700586.003.0003>；<https://www.h-net.org/reviews/showrev.php?id=860>
- **#12** 「Could they by chance succeed in this attempt, their success would at once be the signal for a frightful civil …」  
  判断：**暂无法判断**。存档确认1981年以后法国成为分权的单一制国家，而非摧毁中央国家；这不能无条件触发原文全面摧毁中央集权的强前提。  
  来源：<https://www.gold.uclg.org/sites/default/files/France_0.pdf>；<http://repub.eur.nl/pub/758>
- **#16** 「It is in the schoolroom that socialists and anarchists are found nowadays, and that the way is being paved for…」  
  判断：**暂无法判断**。存档记载法国、意大利、西班牙战后教育扩张，并具体描述西班牙由落后威权走向繁荣民主；但原文拉丁民族衰落没有可操作尺度，教育致衰的因果也未获识别。  
  来源：<https://doi.org/10.1596/9209>；<https://www.cedefop.europa.eu/files/3030_en_short.pdf>；<https://econ-papers.upf.edu/papers/1373.pdf>
- **#20** 「To bring about the recognition that Protection ruins the nations who adopt it, at least twenty years of disast…」  
  判断：**暂无法判断**。两份首轮NBER存档确认保护主义可能损害贸易和生产率，但它们不测法国群众认识危害所需的至少二十年时间，故不能用经济损失替代观念改变。  
  来源：<https://www.nber.org/papers/w5509>；<https://www.nber.org/papers/w33100>；<https://shs.cairn.info/revue-histoire-et-mesure-2014-2-page-155?lang=fr>
- **#22** 「This is what we see happening at the present day with regard to the socialist doctrines which are beginning to…」  
  判断：**暂无法判断**。红色恐怖首批受害者包括贵族、旧军官和财产所有者，但该存档未区分他们在此前是否接受社会主义；贵族家族研究证实迫害同时也记载生存互助。  
  来源：<https://www.encyclopedia.com/history/encyclopedias-almanacs-transcripts-and-maps/red-terror>；<https://doi.org/10.1179/fch.2005.8.1.004>；<https://www.tandfonline.com/doi/full/10.1080/09546540500091076>
- **#24** 「The President of the Court of Appeal has immortalised himself by condemning Ferdinand de Lesseps, for the nati…」  
  判断：**暂无法判断**。2024法律史文章确保存了审判长Samuel Périvier姓名，2015案史也保存诉讼；但保存姓名不等于后世每代不断追问，没有公众关注或代际频率指标。  
  来源：<https://jss.fr/post/EMPREINTES_D-HISTOIRE_Il_avait_concu_les_ecluses_du_canal_de_Panama_pourquoi_Gustave_Eiffel_estil_incarcere_a_la_Conciergerie_en_1893_-4385>；<https://www.lagbd.org/Existait-il_un_droit_%C3%A0_l%27erreur_dans_l%27affaire_de_Panama_%3F_Plaidoirie_de_B%C3%A2tonnier_Henri_Barboux_pour_Ferdinand_et_Charles_de_Lesseps_(1893)_(fr)>
- **#34** 「A portion of these writers advocate a jury recruited solely from the ranks of the enlightened classes; but we …」  
  判断：**暂无法判断**。陪审研究确有教育和人口构成变量，但美国一般混合陪审团不是原文只由有学识阶层组成的法国改革；尚不能据相似研究确认该条件下裁决完全不变。  
  来源：<https://www.uh.edu/~jlehman2/papers/lehmann_smith_jurycomposition.pdf>；<https://doi.org/10.1111/j.1740-1461.2005.00035.x>；<https://www.service-public.gouv.fr/particuliers/vosdroits/F1540>
- **#36** 「Doubtless, too, the votes recorded by crowds are often very dangerous. They have already cost us several invas…」  
  判断：**暂无法判断**。存档确认1940年惨败和战后全面重建，但这些损失不等于人民主权反复无常所造成的代价。后续战争原因研究也没有提供可将该因素与此前侵略损失比较的统一尺度。  
  来源：<https://encyclopedia.ushmm.org/content/en/article/france>；<https://www.hup.harvard.edu/books/9780674976412>；<https://doi.org/10.1093/oso/9780198700586.003.0003>
- **#37** 「Must it be believed that with a restricted suffrage--a suffrage restricted to those intellectually capable if …」  
  判断：**暂无法判断**。知识选民研究指出有知识者亦受党派偏见影响，但另一篇把资格考试限制选举权作为提案讨论；不能据此确认法国实际限定受教育者并观察选票是否改善。  
  来源：<https://journals.sagepub.com/doi/10.1177/1470594X211065080>；<https://www.cambridge.org/core/journals/episteme/article/voter-ignorance-and-the-limits-of-reform/35D2479966DFEB9B601270BCB75EF75C>；<https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000571356/2025-09-18>
- **#38** 「In consequence, were the electorate solely composed of persons stuffed with sciences their votes would be no b…」  
  判断：**暂无法判断**。实验发现政治知识能改变空间考量权重，另有研究发现高学历党派人士对事实分歧更大；方向复杂，且没有把全体选民都变为饱学者的政策场景。  
  来源：<https://www.cambridge.org/core/journals/canadian-journal-of-political-science-revue-canadienne-de-science-politique/article/impact-of-political-knowledge-on-the-voting-decision/16E96BCC9739B63A8276C7707DEE333F>；<https://onlinelibrary.wiley.com/doi/10.1111/polp.12098>；<https://www.tandfonline.com/doi/full/10.1080/01402380802234607>
- **#39** 「They would be guided in the main by their sentiments and by party spirit. We should be spared none of the diff…」  
  判断：**暂无法判断**。政治能力门槛论文研究英印美历史案例、提出规范性批评；哈佛文献反而说明普选长期扩张。二者都未确认法国变为全体饱学者选民后出现集团专制的政策后果。  
  来源：<https://ora.ox.ac.uk/objects/uuid:67ce90d0-a2f4-4e1b-b105-45c9b86c3fc3/files/m6fdcb145704ce0c745174681f0f5ae06>；<https://jlhochschild.scholars.harvard.edu/publications/if-democracies-need-informed-voters-how-can-they-thrive-while-expanding-en>
- **#49** 「Judging by the lessons of the past, and by the symptoms that strike the attention on every side, several of ou…」  
  判断：**暂无法判断**。文明周期理论批评指出斯宾格勒体系内在矛盾，另有战后繁荣资料；但这既不能确定作者所谓若干现代文明极度衰老，也无法检验无截止期的所有民族同样生灭阶段。  
  来源：<https://hrcak.srce.hr/file/318090>；<https://aeon.co/essays/postwar-prosperity-depended-on-a-truce-between-capitalism-and-democracy>；<https://jbh.journals.villanova.edu/index.php/JBH/article/download/3180/2945>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/le-bon-the-crowd-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/le-bon-the-crowd-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/le-bon-the-crowd-v5/audit/manual_review_2026-11-15.py`
canonical报表在NF={}时的候选为人工挑选系固定模板，不是本书流程：全文104/104块通读，只由原工具排除1机制和保留6unclear。补查包括第二轮20个主题40查询，及五条共享自适应查询（文明/时间/教育史学、制度前提、保护主义与记忆、社会主义上层受害者、人民主权战争代价）；具体映射见audit/research_method.json。所有判分及局限以assess和逐字存档为准。
