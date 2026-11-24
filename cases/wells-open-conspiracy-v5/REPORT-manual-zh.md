# H. G. Wells《公开的阴谋》（The Open Conspiracy: Blue Prints for a World Revolution）：出版后预测人工核查

- 案例目录：`cases/wells-open-conspiracy-v5/`
- 出版日期：**1928** 年由纽约 Doubleday, Doran and Company, Inc. 出版的英文初版。正文用 `reading-library/2026-11-15-未来判断扩展100本/02-政治与治理/022-the-open-conspiracy.txt`，与队列记录及 Project Gutenberg #75786（`gutenberg.pglaf.org/cache/epub/75786/pg75786.txt`；官网 `ebooks/75786` 同源）逐字节一致（244,145 字节，sha256 `75f17a784e281a5c503a3fbd44d859dc9ac9c53fd3866600bf1d05be67c1ce4e`），CRLF 原样使用，未转换。gutenberg.org 直链对本环境返回 403，故从官方镜像 pglaf 下载后核对哈希。TXT 不入库。预测窗口按 1928→2026-11-15 计。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

本稿按 METHOD.md 复刻 DeepSeek 流水线，只把模型调用换成助手人工阅读。抽取：用仓库 prepare_book v5（toolkit 来自 main `85e6da1`，prepare_book.py md5 `01fc49ad64…`）把全文切成 71 块（3500 字符、600 字符上下文），助手逐块通读（含前后附文块），按 DISCOVER_PROMPT_V5 写出模型本应返回的 JSON（可为空），再由仓库代码完成引文对齐、非预测筛除、归属降级和去重，得到 22 条候选、全部为可核验预测（resolvable）。英文 `changes` 均为 quote 的逐字单行子串。核验：每条可核验候选先定 scope，用 Exa 各做一次 support/counter 检索（密钥仅按文件路径读取 `~/.config/forecast-lab/exa-new-2.key`，未打印、未入库），只从检索返回的 URL 中选源，存档到 `data/sources/`（sha256），写入 `data/evidence.jsonl`（42 条），再经 `pipeline.py apply assess → check → report`。报告由 canonical `/workspace/forecast-line-b/tools/manual_report.py`（md5 `682248fa…`）生成，未手改。本稿由助手逐条对照书中原文与存档证据人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 22 条，剔除非预测 0 条，计入 **22 条预测**，其中 **22 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 7 |
| 趋势符合 | 1 |
| 部分符合 | 5 |
| 错误 | 9 |
| 暂无法判断 | 0 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **31.8%**（7/22） |
| 加权胜率 | **46.6%** |
| 错误率 | **40.9%**（9/22） |
| 未定占比（暂无法判断/预测） | 0.0%（0/22） |

## 总体评价

这是一本 1928 年的政治—宗教纲领，副题为“世界革命的蓝图”。全书大量篇幅是公开的阴谋应当如何组织的规范方案和机制说明，可核验的世界事态预测相对集中：科学与技术能力扩张、美国爱国利益延续、航空与殖民隔绝、种族紧张、边疆战事、定向遗传能力等方向性断言有的已经实现；关于该运动将成为大多数能人的实践宗教、取得与社会主义/共产主义同等规模并控制莫斯科与纽约、人群不久成为时代错误、世界政府观念很快成为普遍思想背景等核心纲领性预测则未实现。22 条可核验预测全部可判定：正确 7、趋势符合 1、部分符合 5、错误 9、暂无法判断 0。正确条目包括定向育种进入能力范围、科学力量扩张、美国爱国利益延续、马克思主义教条化、航空削弱殖民隔绝、种族紧张长期持续、以及边疆战事仍大量存在。趋势符合仅 1 条：身体健康改善方向持续、但“普遍境遇”尚未到达。部分符合包括亚洲民族主义的本土性与西式建制并存、苏联长期演变后解体、亚洲对日本欧化模式的不完全仿效、全球行政经济渗透但未“无处不达”、以及生育转变只部分缓解人口差异。错误集中在该书的运动愿景（公开的阴谋成为世界宗教并掌控莫斯科/纽约）、近端时点（新条件“不久”成为一般思想背景、宣传潮流“不久”反向流入俄国、人群“不久”过时）以及工业心理学改写经济学议程、石油垄断者被视为过时、后世对战争世界感到不可思议等。严格胜率 31.8%，加权胜率 46.6%，错误率 40.9%。对趋势符合从严：仅方向持续且终点未到才记趋势符合。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（7 条）

- **#2** 「There is a clear hope that later, directed breeding will come within his scope, but that goes beyond his prese…」  
  判断：**正确**。1928年后，定向改变遗传组成已进入人类可操作范围：重组DNA、体细胞与胚胎基因组编辑，以及广泛使用的植入前遗传学检测（PGT/PGD）已能筛查并选择胚胎。虽然全面的人类优生“育种”受伦理和法律限制，但作者所说“进入其能力范围”这一能力条件已经实现。  
  来源：<https://www.rbmojournal.com/article/S1472-6483(25)00052-5/fulltext>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC7659539/>
- **#4** 「We believe that the persistent exploration of our outward and inward worlds by scientific and artistic endeavo…」  
  判断：**正确**。1928年以来，科学与技术能力出现核能、计算、航天、生物技术等当时难以设定上限的扩张，并对全球经济增长产生深远影响。虽有报酬递减与物理极限的讨论，但就出版至截止窗口内的方向与幅度而言，主结果成立。  
  来源：<https://www.imf.org/external/pubs/ft/fandd/2018/06/impact-of-science-and-technology-on-global-economic-growth/mokyr.pdf>；<https://www.nationalreview.com/articles/end-future-peter-thiel>
- **#5** 「but the patriotic interests are so established now that they go on and will go on.」  
  判断：**正确**。美国的旗帜崇拜、经济民族主义与关税保护在1928年后并未消亡：两次大战之间继续高关税，此后爱国象征反复被动员（如2001年后），21世纪贸易政策中保护主义与爱国式经济话语再次显著。主结果成立。  
  来源：<https://www.encyclopedia.com/history/united-states-and-canada/us-history/flags>；<https://history.state.gov/milestones/1921-1936/protectionism>
- **#11** 「Entrenched in Moscow from searching criticism, the Marxist ideology may become more and more dogmatic and unpr…」  
  判断：**正确**。1920年代末至1930年代，苏联意识形态由相对多元转向斯大林时期的官方正统，《联共（布）党史简明教程》等被用作教条化叙事，1920年代的理论争论空间明显收窄。‘可能愈加教条、停滞’这一方向已经实现。  
  来源：<https://facultystaff.richmond.edu/~dbranden/images/Stalin%E2%80%99s%20Master%20Narrative%20Summary.pdf>；<https://www.persee.fr/doc/slave_0080-2557_1996_num_68_2_6334>
- **#12** 「As the old methods of passenger transport are superseded by flying, it will be more and more difficult to keep…」  
  判断：**正确**。航空在英属印度晚期和独立前后确实扩展了人员与信息流动，飞机在分区迁徙和建国过程中已不可或缺；殖民当局愈发难以维持对母国思想与本地政治的隔绝，印度于1947年独立。方向性结果成立。  
  来源：<https://india.oup.com/product/the-aeroplane-and-the-making-of-modern-india-9780192864208/>；<https://caravanmagazine.in/history/lessons-from-indias-long-journey-to-gain-the-right-to-fly>
- **#14** 「there is--and there is bound to be for many years to come--much racial tension.」  
  判断：**正确**。在美国和南非等黑白共处社会，法定隔离、种族歧视频仍延续数十年（吉姆·克罗、种族隔离至1994年），其遗产在财富、住房和教育差距中延续至今。“未来许多年仍将有大量种族紧张”成立。  
  来源：<https://www.splcenter.org/resources/stories/america-250-apartheid-us-racial-discrimination/>；<https://www.loc.gov/classroom-materials/united-states-history-primary-source-timeline/great-depression-and-world-war-ii-1929-1945/race-relations-in-1930s-and-1940s/>
- **#20** 「But there is still much actual warfare before mankind, on the frontiers everywhere, against brigands,」  
  判断：**正确**。1928年后人类并未告别边疆与外围战事：20世纪存在大量殖民战争、非国际性武装冲突和独立战争，21世纪仍有数十国处于战争状态。‘前方仍有大量实际战事’成立。  
  来源：<https://en.wikipedia.org/wiki/List_of_wars:_1900%E2%80%931944>；<https://www.elac.ox.ac.uk/programmes-projects/solferino-21/warfare-today-and-tomorrow/>

### 趋势符合（1 条）

- **#21** 「but the elation of physical well-being will some day be the common lot of mankind.」  
  判断：**趋势符合**。全球出生时预期寿命自20世纪中叶以来空前提高，2023年约73.3岁，健康改善方向持续且显著；但健康不平等、非传染性疾病与精神障碍负担仍使“身体健康的振奋成为人类普遍境遇”这一终点尚未到达。属趋势符合而非已完成。  
  来源：<https://www.who.int/data/gho/data/themes/mortality-and-global-health-estimates/ghe-life-expectancy-and-healthy-life-expectancy>；<https://www.who.int/publications/i/item/9789240125018>

### 部分符合（5 条）

- **#7** 「Their nationalism will remain largely indigenous; the social traditions to which they will try to make the new…」  
  判断：**部分符合**。一战后亚洲、非洲民族主义确实大量以本土认同和反抗殖民为内核，并非简单移植欧美社会等级。但印度采用议会联邦民主、中国吸收社会主义与市场制度等，也广泛借用了西方政治经济形式。本土性与西式建制并存，主结果只部分实现。  
  来源：<https://thediplomat.com/2021/02/nicholas-spykman-and-asian-nationalism/>；<https://www.iimb.ac.in/sites/default/files/2019-04/WP%20No.%20589.pdf>
- **#8** 「Nevertheless it has maintained itself for more than ten years and it seems far more likely to evolve than to p…」  
  判断：**部分符合**。苏俄/苏联政权在1928年后确实经历数十年演变（斯大林、去斯大林化、改革），并维持到1991年；但该联邦国家最终解体，并未沿演变路线存续至今。长期演变与最终灭亡同时成立，主结果只部分符合。  
  来源：<https://en.wikipedia.org/wiki/Dissolution_of_the_Soviet_Union>；<https://history.state.gov/milestones/1989-1992/collapse-soviet-union>
- **#10** 「It is extremely doubtful whether any other Asiatic community will now set itself to a parallel imitation」  
  判断：**部分符合**。并非所有亚洲社会都按明治日本的欧洲议会—君主制—私人工商业模式整体仿效：中国等走了不同道路。但印度继承威斯敏斯特议会制，东亚后来也发展出资本主义民主，西方宪制模式在亚洲有显著扩散。‘极不可能再有任何仿效’过强，主结果只部分成立。  
  来源：<https://www.iimb.ac.in/sites/default/files/2019-04/WP%20No.%20589.pdf>；<https://ipa.org.au/ipa-review-article/colombo-picked-the-wrong-plan>
- **#13** 「It seems inevitable that the development of modern means of communication and the conquest of tropical disease…」  
  判断：**部分符合**。热带医学、全球交通和现代行政经济体系在20世纪大幅扩张，大量原野与原住民社会被纳入市场和国家治理，物质基础遭到严重破坏。但“无处不达”并未完成，亚马孙等地仍有上百个主动隔离的无接触群体存续。主方向出现，终点未尽。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC3026700/>；<https://theguardian.com/global-development/2025/oct/27/brazil-and-peru-are-failing-uncontacted-people-and-the-amazon-future-is-at-stake>
- **#15** 「The steady advance of birth control may mitigate the biological factors of this tension later on,」  
  判断：**部分符合**。避孕普及与生育转变确实缩小了部分社会（如美国黑人与白人完成生育规模已接近）的生育率差距，符合“缓解生物学因素”的一面；但差距并未普遍消失，撒哈拉以南等地区转变滞后，且种族紧张并未因此消除。只部分实现。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC4618673/>；<https://www.demographic-research.org/articles/volume/46/4/>

### 错误（9 条）

- **#1** 「These are the new conditions that unfold themselves before the more alert minds of our generation and which wi…」  
  判断：**错误**。世界政府或世界共同体观念在二战前后一度升温，但并未在1928年后不久成为普遍思想背景。民族国家逻辑长期主导，世界政府方案在冷战期间边缘化，近年亦常被迅速否定。主结果未出现。  
  来源：<https://greattransition.org/publication/global-government-revisited/>；<https://www.cooperative-individualism.org/weiss-thomas_what-happened-to-the-idea-of-world-government-2009-jun.pdf>
- **#3** 「As the science of industrial psychology in particular develops, we shall find all this discussion of ownership…」  
  判断：**错误**。工业/组织心理学虽已发展，但仍是心理学中相对较小的领域，并未把所有权、利润、工资与金融从经济学首要议题的位置上排挤出去。20世纪中叶定型的经济学工具箱仍被使用，所有权与市场仍是改革与教学的核心范畴。主结果相反。  
  来源：<https://www.cambridge.org/core/journals/industrial-and-organizational-psychology/article/an-essay-about-work-psychology-and-the-psychology-of-working/679337D3EE436733125DA38F8E706CF8>；<https://www.vox.com/policy-and-politics/2019/9/13/20862607/economics-inequality-deregulation-wealth-taxes-policy>
- **#6** 「In the modern world, crowds are a survival and they will presently be an anachronism」  
  判断：**错误**。人群并未在1928年后不久成为时代错误。体育场馆、广场和街头在20–21世纪仍是政治、抗议与公共生活的核心场所，群众集会传统延续至今。主结果相反。  
  来源：<https://news.columbia.edu/news/stadium-site-politics-and-protest>；<https://www.rsis.edu.sg/wp-content/uploads/rsis-pubs/WP230.pdf>
- **#9** 「The time may be not far distant when the tide of propaganda will flow in the reverse direction.」  
  判断：**错误**。1928年后的近端窗口内，宣传主流仍是莫斯科经共产国际等向外输出，而非潮流迅速反向灌入俄国。对苏西方广播（如美国之音）主要是二战末期至冷战产物，远晚于“不久”。近端主结果未出现。  
  来源：<https://yalebooks.yale.edu/2019/08/23/a-century-of-moscows-meddling-in-us-politics/>；<https://www.history.com/this-day-in-history/february-17/voice-of-america-begins-broadcasts-to-russia>
- **#16** 「and sooner or later it will be discovered, conscious and potent, the working religion of most sane and energet…」  
  判断：**错误**。威尔斯的公开的阴谋并未成为大多数健全而有活力者的实践性宗教。相关实践主要体现为小型人文/进步团体和韦尔斯学会一类文学社团，世界政府观念仍属知识史与边缘政治运动，从未取得大众信仰地位。  
  来源：<https://heritage.humanists.uk/the-progressive-league/>；<https://en.wikipedia.org/wiki/H.G._Wells_Society>
- **#17** 「The character of the Open Conspiracy will now be plainly displayed. It will have become a great world movement…」  
  判断：**错误**。世界联邦主义在1940年代一度活跃，但从未达到与社会主义或共产主义相当的世界规模，更未取而代之成为世界宗教。公开的阴谋作为一场运动没有获得与社共运动同等的群众性和建制地位。  
  来源：<https://mondial.press/articles/2021/09/short-history-world-federalist-movement/>；<https://modernismmodernity.org/forums/posts/chambers-open-conspiracy>
- **#18** 「it may be in control of Moscow before it is in control of New York.」  
  判断：**错误**。检索与史实均表明，并不存在公开的阴谋或世界政府运动控制莫斯科或纽约的事实。苏联由共产党政权统治，美国亦无该运动掌权；相关倡议只是1930年代出现的小型世界政府竞选团体等。先后控制两城的预测未实现。  
  来源：<https://en.wikipedia.org/wiki/Campaign_for_World_Government>；<https://en.wikipedia.org/wiki/Political_views_of_H.G._Wells>
- **#19** 「A day will come when the gentlemen who are trying to control the oil supplies of the world without reference t…」  
  判断：**错误**。尽管出现能源转型讨论，国际能源署等仍强调在清洁能源过渡期必须持续重视石油安全；欧佩克对供应的管理延续一个多世纪，石油地缘政治在21世纪仍是核心议题。把控制世界石油供应视为古怪过时角色的那一天并未到来。  
  来源：<https://www.iea.org/commentaries/a-strong-focus-on-oil-security-will-be-critical-throughout-the-clean-energy-transition>；<https://blogs.worldbank.org/en/developmenttalk/a-century-and-a-half-of-oil-supply-management--opec-s-endurance->
- **#22** 「A time will come when men will sit with history before them or with some old newspaper before them, and ask in…」  
  判断：**错误**。当代人并未面对旧报纸而怀疑那个充满战争与生存斗争的世界是否存在过。21世纪仍有数十国处于战争，公众持续以新闻和直播关注冲突，战争被当作当前现实而非不可思议的史前梦魇。主结果未出现。  
  来源：<https://www.elac.ox.ac.uk/programmes-projects/solferino-21/warfare-today-and-tomorrow/>；<https://www.foreignaffairs.com/ukraine/how-wars-dont-end>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/wells-open-conspiracy-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/wells-open-conspiracy-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/wells-open-conspiracy-v5/audit/manual_review_2026-11-15.py`

## 说明

- 抽取密度（22 条可核验 / 71 总块 ≈ 0.31；按正文 62 块计 ≈ 0.35）落在 METHOD §5 英文书参考区间（约 0.2–0.35）的上沿。本书主体是运动蓝图、规范方案和机制分析，“will” 大量用于计划语气而非对世界事态的断言；未把公开的阴谋“应当/必须如何组织”的纲领句收为预测，也未为凑密度放宽标准。所收 22 条均为作者本人、指向出版后可核验结果的方向性或定时判断。
- 前后附文人工排除记录：仓库 `matter_spans` 只识别中文“序/目录/参考文献”和 `Chapter \d+` 标题，对本卷英文 `PREFACE`、`CONTENTS`、`_Chapter I_` 及后记无匹配，故 `excluded_matter_spans=[]`，须人工排除。前附文：字符偏移 0–7013（Gutenberg 头部与许可证、START 标记、作者书目、1928 年标题页与版权页、题献、PREFACE 序言、CONTENTS），主要落在 txt-00001、txt-00002 及 txt-00003 开端极短扉页残留，未抽预测。正文为第 I–XVII 章，自 offset 7013（`_Chapter I_`）至后记之前。后附文自 offset 220364 起：`NOTE ON THE MARGIN OF THESE BLUE PRINTS`（作者边注/后记，按 METHOD 排除）、THE END、Transcriber’s Note、Gutenberg 许可证，主要落在 txt-00064 后半至 txt-00071，未抽预测。txt-00003 与 txt-00064 为前后附文与正文交界块，只对正文段落抽取。全部 22 条引文偏移均在正文区间内（最末一条结束于 220354，后记之前）。
- 带近端时点的条目按明示窗口判断：第 1、6 条“presently”、第 9 条“not far distant”均视为出版后较近的窗口；窗口已过且主结果未出现则记错误。第 2 条“later”、第 14 条“many years to come”、第 15 条“later on”、第 19 条“A day will come”、第 21 条“some day”、第 22 条“A time will come”按出版日至截止日的观察窗口判断；其中第 21 条健康改善方向持续、终点未到，记趋势符合。
- 第 8 条“更可能演变而非灭亡”：苏联在 1928 年后长期演变并维持至 1991 年，但联邦国家最终解体，记部分符合，而非把数十年演变抹掉单记错误，也不因曾经演变而记正确。
- 第 16–18 条是该书核心运动预测（成为大多数能人的实践宗教、取得与社共同等规模并取而代之、先控制莫斯科再控制纽约），均未实现，记错误。
- 检索摘录均取自第三方存档页面，未见与原书连续 300 字符重合而需截断的情形。证据优先独立第三方（IMF、IEA、世界银行、WHO、美国国务院史学办公室、国会图书馆、PMC/学术期刊、牛津、卫报等）；关于公开的阴谋本身规模，辅以该运动史与韦尔斯学会等条目。
- 案例的 `context` 字段按协调者口径清空（`data/claims.jsonl` 与 `output/txt_import/claims_proposals.jsonl`）。
- 出版前史实（1928 年及以前的战事、苏俄已维持十余年等）未计入可判定预测。本卷无因出版前已发生而剔除的候选。
- Gutenberg 官网直链对本环境返回 403，所用 TXT 来自官方镜像 pglaf，哈希与字节数与队列完全一致，无版本分歧。

