# 兰斯洛特·劳·怀特《阿基米德，或物理学的未来》（Lancelot Law Whyte, Archimedes; or, The Future of Physics）：出版后预测人工核查

- 案例目录：`cases/whyte-archimedes-future-of-physics-v5/`
- 出版日期：**1927** 年由伦敦 Kegan Paul, Trench, Trubner & Co. 与纽约 E. P. Dutton 出版（To-Day and To-Morrow 丛书短篇科学前瞻）。正文用 `reading-library/2026-11-15-未来判断扩展100本/05-技术与科学/093-archimedes-or-the-future-of-physics.txt`，与 Project Gutenberg #75452（`pg75452.txt` / `ebooks/75452.txt.utf-8`）逐字节一致（135,224 字节，sha256 `c2997b1af90ce7f1ce53bf632d6f9ab0f29352c51e6a8580962fd8c542413a05`），CRLF 原样使用，未转换。TXT 不入库。预测窗口按 1927→2026-11-15 计。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

本稿按 METHOD.md 复刻 DeepSeek 流水线，只把模型调用换成助手人工阅读。抽取：用仓库 prepare_book v5（toolkit 来自 main `85e6da1`，prepare_book.py md5 `01fc49ad64…`）把全文切成 39 块（3500 字符、600 字符上下文），助手逐块通读（含前后附文块），按 DISCOVER_PROMPT_V5 写出模型本应返回的 JSON（可为空），再由仓库代码完成引文对齐、非预测筛除、归属降级和去重，得到 20 条候选、全部为可核验预测（resolvable）。英文 `changes` 均为 quote 的逐字单行子串。核验：每条可核验候选先定 scope，用 Exa 各做一次 support/counter 检索，只从检索返回的 URL 中选源，存档到 `data/sources/`（sha256），写入 `data/evidence.jsonl`（36 条），再经 `pipeline.py apply assess → check → report`。本稿由助手逐条对照书中原文与存档证据人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 20 条，剔除非预测 0 条，计入 **20 条预测**，其中 **20 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 0 |
| 趋势符合 | 0 |
| 部分符合 | 8 |
| 错误 | 12 |
| 暂无法判断 | 0 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **0.0%**（0/20） |
| 加权胜率 | **20.0%** |
| 错误率 | **60.0%**（12/20） |
| 未定占比（暂无法判断/预测） | 0.0%（0/20） |

## 总体评价

这是一本 1927 年的短篇科学前瞻，第六章更以“明确预言”列出物理、生物、心理的具体断言，近百年窗口使绝大多数条目可判定。20 条可核验预测全部可判定：无正确、无趋势符合，8 条部分符合，12 条错误。部分符合主要是方向对、机制或时点不对的条目（科学交叉与社会影响未达“人类进化阶段”、生命控制并未“不久”实现、原子钟最终成为时间标准但远晚于“不久”、牛顿体系被取代但基础物理仍大体时间可逆、量子化学很快统一了化学键但并未按作者的电子速度/不可逆方案同时纳入胶体、生命/非生命界限模糊但未被取消、控制过程被发现但并非统一的生命函数 f、传染病大减但器质性疾病并未全部消灭）。错误集中在带明示时点或可实验判定的命题：量子定律并未改写成明确不可逆形式；1940 年前原子理论并未“触底”简化；偏转电子速度并不构成不同于厘米/秒的量、直线径迹速度也不总等于光速；约 1947 年既无足够知识开始人造人实验，也未创立国际进化研究所；数年之内并未完成从细胞到创造性思考的整合阶谱；1950 年前既未确立生命函数 f 的主控因素，癌症也远未可控制或易于预防；产程并未被减至自然最短限度；遗传病的克服并非靠调控发育速率；1920 年代“返老”疗法并不安全有效。严格胜率 0，加权胜率 20.0%，错误率 60.0%。对趋势符合从严：仅方向持续、终点未到才记趋势符合，本卷带时点的失败与已完成窗口内的相反结果一律记错误或部分符合。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 部分符合（8 条）

- **#1** 「whose influence on thought and social custom will be so profound that it will mark a stage in human evolution」  
  判断：**部分符合**。二十世纪确有物理学家进入生物学并促成分子生物学、神经科学等交叉领域，对思想与社会理解产生深远影响；但物理、生物、心理并未完成单一科学综合，也未被史家普遍判定为“人类进化的一个阶段”。主结果只部分实现。  
  来源：<https://plato.stanford.edu/archives/fall2020/entries/scientific-unity/>；<https://journals.sagepub.com/doi/10.1177/0263276412456569>
- **#2** 「life and consciousness will soon be subject to the first stages of a theoretically-grounded control」  
  判断：**部分符合**。生命与部分精神过程后来确实进入有理论依据的干预（抗生素、遗传学、精神药理学等），但并非1927年后“不久”即出现；意识研究在二十世纪大部分时间被边缘化，至今也未达到对意识的理论化控制。时机与范围均与原预测有实质差距。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC7058250/>；<https://www.annualreviews.org/content/journals/10.1146/annurev-clinpsy-050718-095514>
- **#4** 「Perhaps the physicist will soon be able to use the atom as the theoretical clock for physics」  
  判断：**部分符合**。原子确已成为物理学的理论与实用时间标准：NIST于1949年制成首台原子钟，1967年第13届CGPM将秒定义为铯原子跃迁。但“不久”并未在1920年代末实现，中间仍长期使用地球自转与历书时。结果出现、时点明显滞后。  
  来源：<https://www.nist.gov/atomic-clocks/brief-history-atomic-time>；<https://www.bipm.org/en/committees/cg/cgpm/13-1967/resolution-1>
- **#11** 「a new system of physical conceptions will be built up appropriate to irreversible processes, which will be sub…」  
  判断：**部分符合**。牛顿力学确被相对论与量子力学取代，但取代它的基本理论在基础层面上仍大体时间可逆（幺正演化、CPT对称）。普里戈金等对不可逆过程的研究是重要补充，并未成为取代牛顿可逆体系的新基础物理框架。  
  来源：<https://en.wikipedia.org/wiki/Time-reversal_symmetry>；<https://royalsocietypublishing.org/rsta/article/376/2124/20170365/115575/The-rehabilitation-of-irreversible-processes-and>
- **#12** 「The conceptions which will be built up on electron velocity experiments will very quickly bring within one sim…」  
  判断：**部分符合**。化学键很快被量子力学统一：Heitler–London 1927–1928年工作被视为共价键量子理解的开端，随后被Pauling等发展。但这并非建立在作者所设想的电子速度实验与不可逆新概念之上；胶体/软物质长期仍是相对独立的领域，直至二十世纪后期才形成统一软物质科学。子项与机制均有实质差异。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC8001733/>；<https://physicstoday.aip.org/features/from-simple-liquids-to-colloids-and-soft-matter>
- **#13** 「biology will soon cease to draw a definite line between inanimate and living systems」  
  判断：**部分符合**。病毒、生命起源与合成生物学使生命/非生命界限明显模糊，许多论述承认分界是连续、含糊的；但生物学教材与实践仍在定义并划分生命体系，明确界线并未被取消。方向出现，终点未达，且“不久”并未在1920年代立即实现。  
  来源：<https://www.scientificamerican.com/article/are-viruses-alive-2004/>；<https://edu.rsc.org/feature/the-origin-of-life/2000129.article>
- **#14** 「In each class of organism a central controlling process will be discovered and its laws formulated with some p…」  
  判断：**部分符合**。稳态、代谢与电化学信号等控制过程已被广泛研究，电化学也被视为理解生命的重要途径；但并未在每一类有机体中发现并精确表述单一的中枢控制过程或作者的生命函数f。发现了多种控制机制，而非统一、可精确定量表述的单一过程。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC7076167/>；<https://med.libretexts.org/Bookshelves/Anatomy_and_Physiology/Anatomy_and_Physiology_(Boundless)/1%3A_Introduction_to_Anatomy_and_Physiology/1.2%3A_Life/1.2A%3A_Life_Functions>
- **#20** 「gradually eliminate all the organic diseases which attack the body」  
  判断：**部分符合**。二十世纪疫苗、抗生素和环境卫生使多种传染病得到控制或消灭（如天花），器质性疾病负担结构发生重大变化；但WHO估计显示，到2023年缺血性心脏病、癌症等非传染性器质性疾病仍是全球主要死因，“消灭所有侵袭身体的器质性疾病”并未实现。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC7100685/>；<https://www.who.int/news-room/fact-sheets/detail/the-top-10-causes-of-death>

### 错误（12 条）

- **#3** 「the atomic physicists will soon formulate the quantum laws in a clearly irreversible form which admits of prec…」  
  判断：**错误**。主流量子力学在1920–30年代被表述为幺正、时间可逆的薛定谔/狄拉克形式；维格纳1932年讨论的是量子理论中的时间反演对称，而非把量子定律改写成可精确检验的明确不可逆形式。主结果相反。  
  来源：<https://arxiv.org/pdf/quant-ph/0508041>；<https://en.wikipedia.org/wiki/Time-reversal_symmetry>
- **#5** 「In twenty years’ time scientific knowledge will be adequate for the beginning of this giant task」  
  判断：**错误**。约1947年科学知识远不足以开始“人造人/受控再进化”。1953年Miller–Urey实验才得到氨基酸等有机分子；至今仍无人从无机物从头造出生命，更无论人造人。该二十年内知识就绪的预测不成立。  
  来源：<https://en.wikipedia.org/wiki/History_of_research_into_the_origin_of_life>；<https://www.sciencehistory.org/stories/magazine/constructing-life/>
- **#6** 「we shall be subscribing our guineas for the foundation of the Institute」  
  判断：**错误**。检索未见1927–1947年间创立名为International Institute of Evolutionary Research、由公众认捐并在国际联盟下于瑞士开展人造进化实验的机构。当时国际生物学组织是1919年成立的IUBS；瑞士苏黎世进化医学研究所迟至2014年才建立，性质与任务均不同。  
  来源：<https://www.iubs100years.org/history>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC12879187/>
- **#7** 「in a few years those who are studying the physiology of the central nervous system will be able to indicate ho…」  
  判断：**错误**。“数年之内”画出从最简单细胞到创造性思考者的综合/整合步数并为各阶段归派觉知模式，并未发生。即使到2024年，创造性能力的神经元基础仍被综述称为未知，意识的经验研究也迟至1990年代才重新成为主流。明示短期终点已过且主结果未出现。  
  来源：<https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2024.1367922/full>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC7058250/>
- **#8** 「Before 1940 a very remarkable simplification will be made in atomic theory, which will indicate that in quantu…」  
  判断：**错误**。1940年前原子理论并未“非常显著地简化”或“触底”。1932年中子等发现曾一度显得图像完整，随即新粒子与核物理使图景更复杂。爱丁顿等人关于e、m、M、c、h简单关系的方案未被物理学界接受为原子理论的简化完成。  
  来源：<https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=912195>；<https://arxiv.org/pdf/1510.04046>
- **#9** 「‘Electron velocity’ as calculated from deflection experiments will be found not to be the same as the directly…」  
  判断：**错误**。偏转实验（Kaufmann–Bucherer等）测量的是电子动量/质量随速度的变化，并与狭义相对论及后来的飞行时间直接测速相一致；并未发现“偏转算出的电子速度”是不同于厘米/秒的另一种量。主结果不成立。  
  来源：<https://en.wikipedia.org/wiki/Kaufmann%E2%80%93Bucherer%E2%80%93Neumann_experiments>；<https://web.mit.edu/8.13/JLExperiments/JLExp09.pdf>
- **#10** 「in the case of straight electron tracks, the measured velocity may be found to be always that of light」  
  判断：**错误**。电子有静质量，速度可以低于光速。β射线速度典型约0.3c–0.9c；Bertozzi等实验表明电子速率随能量趋近但并不总等于光速。直线径迹测速“总是光速”的预测与实验相反。  
  来源：<https://physicsanduniverse.com/properties-beta-rays/>；<https://www.savemyexams.com/a-level/physics/aqa/17/revision-notes/12-turning-points-in-physics/12-3-special-relativity/12-3-10-bertozzis-experiment/>
- **#15** 「The most important factors which influence the life-function ‘f’ (i.e. which affect the central controlling pr…」  
  判断：**错误**。到1950年，维生素、激素与中间代谢等生命过程因素确有重大进展，但作者所定义的定量生命函数f本身从未被建立，因而谈不上在约1950年前获知其“最重要影响因素”。该条的知识完备目标未实现。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC7076167/>；<https://www.annualreviews.org/content/journals/10.1146/annurev.ph.12.030150.002443>
- **#16** 「cancer will not only be controllable, but easily prevented」  
  判断：**错误**。约1950年癌症既非“易于预防”，也非普遍可控制。1953年美国癌症相对五年生存率仅约35%；1950年代主要治疗仍是创伤性手术和相对粗放的放疗，生存很差。明示1950年前的医学结果不成立。  
  来源：<https://www.ncbi.nlm.nih.gov/books/NBK294309/>；<https://news.cancerresearchuk.org/2012/06/03/celebrating-60-years-of-progress/>
- **#17** 「the duration of child-birth will be reduced to a natural minimum」  
  判断：**错误**。催产素等干预可以缩短部分产程，但人群层面的证据显示，与约五十年前相比，当代产妇分娩时间更长，而非被减至某一“自然最短限度”。主结果未出现，方向甚至相反。  
  来源：<https://www.nih.gov/news-events/news-releases/nih-study-finds-women-spend-longer-labor-now-than-50-years-ago>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC3655692/>
- **#18** 「hereditary tendencies to specific weakness or disease will be overcome by accelerating or retarding the rate o…」  
  判断：**错误**。克服遗传性疾病的成功途径主要是早期筛查与饮食（如苯丙酮尿症）、酶替代和近年的基因治疗，而不是在受孕至成熟之间加速或减缓整体发育速率。调控发育速率主要用于部分生长/青春期障碍，并非作者所预言的普遍遗传疾病克服方法。  
  来源：<https://www.nichd.nih.gov/health/topics/pku/conditioninfo/treatments>；<https://www.ncbi.nlm.nih.gov/books/NBK535378/>
- **#19** 「Rejuvenation will soon be safe and efficient, but not as a means for attempting immortality」  
  判断：**错误**。1920–30年代的Steinach手术、Voronoff腺体移植等“返老”疗法不久即被证明缺乏根据且不可靠，并非“安全而有效”。当代抗衰老研究仍未实现安全高效的返老还童。明示“不久”的技术预测不成立。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC3955324/>；<https://bcmj.org/blog/rejuvenation>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/whyte-archimedes-future-of-physics-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/whyte-archimedes-future-of-physics-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/whyte-archimedes-future-of-physics-v5/audit/manual_review_2026-11-15.py`

## 说明

- 抽取密度（20 条可核验 / 39 块 ≈ 0.51）高于 METHOD §5 英文书参考区间（约 0.2–0.35）。本书是 priority 1 的“未来之物理学”短篇前瞻，第六章公开宣布给出“definite prophecies”。所收均为作者本人、可独立核验的方向性或定时预测；未收入文学性结语（如“physics will create a new hope for man”）、对话中的规范建议、以及与第六章预言重复的前文复述。前/后附文块预测为空，拉低了分母，但正文预言密度仍偏高，属文本体裁使然，未为凑数放宽或收紧。
- 前后附文人工排除记录：仓库 `matter_spans` 只识别中文“序/目录/参考文献”和 `Chapter \d+` 标题，对本卷英文 `CHAPTER I`、`CONTENTS`、`NOTES` 无匹配，故 `excluded_matter_spans=[]`，须人工排除。封面/版权/献词/目录：字符偏移 0–2276（Gutenberg 头部至 `CHAPTER I` 之前），主要落在 txt-00001 前半，未抽预测。正文为第 I–VI 章，自 offset 2276（`CHAPTER I`）至 NOTES 之前。NOTES（脚注与参考文献，自 `NOTES` 标题起）、丛书广告 `TO-DAY AND TO-MORROW` 全目、以及 Gutenberg 许可协议为后附文，主要落在 txt-00024 后半至 txt-00039，未抽预测。txt-00001 与 txt-00024 为前后附文与正文交界块，只对正文段落抽取。全部 20 条引文偏移均在正文区间内。
- 第 5、6 条“二十年内”按约 1947 年终点判断；第 8 条“Before 1940”、第 15–16 条“before about 1950”、第 7 条“in a few years”均按明示窗口判断，窗口已过且主结果未出现则记错误。
- 第 10 条原文为 “may be found to be always that of light”，仍作为作者提出的可检验实验命题核对，实验表明电子速度可低于光速，记错误。
- 第 17 条 NIH 新闻稿未能存档（抓取失败），改以该研究的 PMC 全文（Laughon 等, *Changes in labor patterns over 50 years*）为据，结论相同：当代产程较约五十年前更长。
- 检索摘录均取自第三方存档页面，未见与原书连续 300 字符重合而需截断的情形。
- 案例的 `context` 字段按协调者口径清空（`data/claims.jsonl` 与 `output/txt_import/claims_proposals.jsonl`）。
- 出版前史实（1927 年及以前的原子模型、相对论争论等）未计入可判定预测。

