# W. E. B. 杜波依斯《黑人的灵魂》（The Souls of Black Folk，1903）：出版后预测人工核查

- 案例目录：`cases/du-bois-souls-of-black-folk-v5/`
- 出版日期：1903 年 4 月由 A. C. McClurg（芝加哥）出版；书中多篇曾于 1897—1902 年先刊于《大西洋月刊》等刊物。正文取自 Project Gutenberg #408 纯文本（pg408.txt，与队列记录 sha256 `87f8e832…` 逐字节一致，428,742 字节；按工具包读取为 425,401 字符），原样使用，不做转换。观察窗口为 1903 至 2026-11-15（以 1903 为出版年代理）。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

按 METHOD.md 执行。抽取：用仓库 prepare_book v5 流水线（85e6da1 工具包）把全文（425,401 字符）切成 123 块（每块 3500 字符，带 600 字符上下文；第 118—123 块为全书结尾与 Gutenberg 许可文本）。助手逐块通读，没有用关键词筛选，按 DISCOVER_PROMPT_V5 写出模型本应返回的 JSON（未调用 DeepSeek），再由仓库代码（validate_chunk_predictions + claims_from_results）完成引文对齐、归属降级、去重和导入：共 33 条候选，其中 17 条为可核验预测，16 条为 unclear（序言、转述、神学条件句、价值判断等）；另有 2 条规范陈述、2 条格言、5 条机制陈述、2 条琐碎陈述被排除。去重只按 claims_from_results 的重叠规则，不按主题合并；第二章结尾逐字重申“二十世纪的问题是肤色界线问题”的一条在核验阶段按 ASSESS duplicate 排除。核验：每条先写 scope，各做一次 support 与 counter 的 Exa 检索，第 1、4、8 条追加一轮检索，共 38 次检索；只从检索返回的 URL 中选源。原文用 Exa contents 抓取（失败时 curl 兜底）存档于 data/sources（42 份，sha256），写入 data/evidence.jsonl（42 条）；理由中的数字均已在存档文本中核对。助手阅读后按“正确／趋势符合／部分符合／错误／暂无法判断”规则逐条评断，再经 pipeline.py apply assess → check → report。本稿由助手逐条对照书中原文与存档证据人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 17 条，剔除非预测 1 条，计入 **16 条预测**，其中 **16 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 6 |
| 趋势符合 | 3 |
| 部分符合 | 6 |
| 错误 | 1 |
| 暂无法判断 | 0 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **37.5%**（6/16） |
| 加权胜率 | **70.3%** |
| 错误率 | **6.2%**（1/16） |
| 未定占比（暂无法判断/预测） | 0.0%（0/16） |

## 总体评价

杜波依斯对美国种族关系长期走向的判断大体应验：南方黑人终将自主行动、南方经济社会变化后黑人权利诉求会更响亮、“觉醒”终将到来，都在 1950—1960 年代民权运动中实现；黑人农业劳动者离开土地进城、此后数代南方白人不会承担同情式领导、灵歌不会被世界遗忘，也已得到证实。法定隔离让步、南方白人大学复兴、南方白人态度代际转变只确认了方向，社会隔离和偏见并未消失。部分符合的多是方向对而程度或时间不对：“肤色界线”确是 20 世纪重大问题但并非唯一主线，联邦资助大众教育要到 1965 年才普遍实现，就业中的肤色歧视在法律上被禁止但实际招聘歧视仍在，被剥夺政治权利的黑人经济上相对停滞但并非毫无进步，点名的反华盛顿知识分子中只有部分公开发声，黑带农民中的“社会主义”只短暂出现。判错的是“博雅课程不会改变”。需注意：#5、#9、#15、#16 指向同一“黑人觉醒/揭开帷幕”主题，#7、#12、#14 指向同一“隔离与态度转变”主题，按管线规则分别计分，可能放大胜率（敏感性见 PR 说明）。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（6 条）

- **#5** 「and yet when he does come to think and will and do for himself,—and let no man dream that day will never come,…」  
  判断：**正确**。南方黑人自主思考、自主行动的一天已经到来：1955年12月罗莎·帕克斯引发蒙哥马利公交抵制运动；1960年南方黑人学生发起静坐运动并成立学生非暴力协调委员会（SNCC），显示了基层的力量  
  来源：<https://web.stanford.edu/~ccarson/articles/black_scholar.htm>；<https://kinginstitute.stanford.edu/sit-ins>
- **#9** 「The dangerously clear logic of the Negro’s position will more and more loudly assert itself in that day when i…」  
  判断：**正确**。前提成立：新政和二战带来的经济变化加速了南方的城市化、工业化，种植园势力衰落。后果应验：20世纪中叶民权运动正是在社会经济变化使黑人反抗成为可能的城市地区爆发，1955—1968年黑人以非暴力方式大规模争取权利  
  来源：<https://www.georgiaencyclopedia.org/articles/history-archaeology/civil-rights-movement/>；<https://doi.org/10.1093/actrade/9780190605421.003.0003>；<https://oxfordre.com/americanhistory/display/10.1093/acrefore/9780199329175.001.0001/acrefore-9780199329175-e-594>
- **#11** 「But a change is coming, and slowly but surely even here the agricultural laborers are drifting to town and lea…」  
  判断：**正确**。黑人农业劳动者大规模离开土地进城：约1916—1970年间超过6 million（六百万）黑人从南方农村迁往北部、中西部和西部城市；黑人经营的农场从1920年的峰值925,710个降到1982年的33,250个  
  来源：<https://www.history.com/articles/great-migration>；<https://static.ewg.org/reports/2021/BlackFarmerDiscriminationTimeline/1982_USDA-History.pdf>
- **#12** 「We cannot hope, then, in this generation, or for several generations, that the mass of the whites can be broug…」  
  判断：**正确**。此后数代南方白人大众并未承担起同情式领导：全国民调中1942年只有30%的白人认为黑白学生应同校；1956年一批南方参众议员签署《南方宣言》，誓言以一切“合法手段”抵制种族融合，1957—1958年小石城事件中抵制进一步升级  
  来源：<https://gss.norc.org/content/dam/gss/get-documentation/pdf/reports/social-change-reports/SC21%20American%20Attitudes%20towards%20Race%20Relations.pdf>；<https://www.loc.gov/exhibits/civil-rights-act/civil-rights-era.html>
- **#15** 「Some day the Awakening will come, when the pent-up vigor of ten million souls shall sweep irresistibly toward …」  
  判断：**正确**。“觉醒”已经到来：国家公园管理局称1954—1964年民权运动是美国现代史上最大的群众运动，黑人示威席卷全国；1964年7月2日签署的《民权法》禁止公共场所歧视，“仅限白人”的法定隔离被废除。目标未完全实现，但书中只预言觉醒与冲击  
  来源：<https://www.nps.gov/subjects/civilrights/modern-civil-rights-movement.htm>；<https://www.archives.gov/milestone-documents/civil-rights-act>
- **#17** 「until the Fisk Jubilee Singers sang the slave songs so deeply into the world’s heart that it can never wholly …」  
  判断：**正确**。奴隶歌曲（灵歌）至今未被遗忘：菲斯克欢庆歌手2021年庆祝首次巡演150周年，其专辑获得格莱美最佳传统福音专辑奖  
  来源：<https://www.fisk.edu/university-news-and-publications/the-fisk-jubilee-singers-album-celebrating-fisk-the-150th-anniversary-album-wins-grammy-award-in-best-roots-gospel-album-category/>；<https://apnews.com/article/entertainment-nashville-tennessee-nikki-giovanni-music-68e0b17cd8a036c4b9e3c5ec7b801281>

### 趋势符合（3 条）

- **#7** 「That the present social separation and acute race-sensitiveness must eventually yield to the influences of cul…」  
  判断：**趋势符合**。法定种族隔离确已让步：1954年布朗案判决学校隔离违宪，1964年《民权法》禁止公共场所歧视并要求学校和公共设施一体化。但社会隔离并未消失，斯坦福研究称自1988年以来100个最大学区黑白学生隔离程度上升了64%，方向得到确认但未完全实现  
  来源：<https://www.archives.gov/milestone-documents/civil-rights-act>；<https://civilrightsproject.ucla.edu/wp-content/uploads/2017/05/Brown63_South_052317-RELEASE-VERSION.pdf>；<https://ed.stanford.edu/news/70-years-after-brown-v-board-education-new-research-shows-rise-school-segregation>
- **#8** 「So far as white men are concerned, this fact is to-day being recognized in the South, and a happy renaissance …」  
  判断：**趋势符合**。南方白人大学确在其后迎来进步时代的扩张：北卡罗来纳大学入学人数从1900年的512人增至1914年接近1000人，到1930年从一所小学院转变为成熟的现代州立大学；Dennis著作描述1880—1920年进步主义如何改造新南方的州立大学。但南方高等教育整体仍落后于北方，证据只覆盖少数院校，按趋势符合计  
  来源：<https://focplnc.org/orange-county-books/storylines/unc-enrollment-storyline-1905/>；<https://uncpress.org/9780807879627/the-university-of-north-carolina-1900-1930/>；<https://www.press.uillinois.edu/books/?id=c026171>
- **#14** 「Such an essentially honest-hearted and generous people cannot cite the caste-levelling precepts of Christianit…」  
  判断：**趋势符合**。方向得到确认：一份1960年代的民调综述称此前二十年北方和南方都持续转向接受平等权利；《美国社会学杂志》研究显示1972—1984年南方与非南方的反黑人偏见都在下降，下降部分来自较年轻、偏见较少的世代替代老一代，且南方下降更快。指标是偏见量表，与“感到肤色界线违背其信仰”只是近似；但1950年代不少南方白人福音派以神学为隔离辩护，转变是缓慢的  
  来源：<https://files.eric.ed.gov/fulltext/ED013274.pdf>；<https://www.journals.uchicago.edu/doi/10.1086/228991>；<https://academic.oup.com/jah/article-abstract/110/2/387/7281119>

### 部分符合（6 条）

- **#1** 「The problem of the twentieth century is the problem of the color-line,—the relation of the darker to the light…」  
  判断：**部分符合**。种族/殖民关系确是20世纪的重大问题：美国国务院史料称1945—1960年间亚非有三十多个新国家从欧洲殖民统治下获得自治或独立，联合国称其1945年成立时近三分之一的世界人口生活在殖民附属领土；布鲁金斯称杜波依斯的预言已被证明正确。但20世纪同样被两次世界大战与冷战意识形态对抗所主导，“唯一核心问题”的说法只得到部分证实  
  来源：<https://history.state.gov/milestones/1945-1952/asia-and-africa>；<https://www.un.org/en/global-issues/decolonization>；<https://www.brookings.edu/articles/an-american-tragedy-the-legacy-of-slavery-lingers-in-our-cities-ghettos/>；<https://www.cambridge.org/core/books/abs/transatlantic-century/from-world-war-to-cold-war/FD7DA73050D7E0BEA6E05976069DF416>
- **#3** 「Is it possible, and probable, that nine millions of men can make effective progress in economic lines if they …」  
  判断：**部分符合**。前提成立（南方黑人在1900—1960年代普遍被剥夺选举权）。相对差距方面部分应验：按Higgs基准，黑人与白人人均收入之比1900年为0.35、1940年为0.34，1900—1940年收敛“完全停滞”；但Margo修订后的基准为1900年0.32、1940年0.38，显示1870—1940年大体稳步收敛，且1940年代在南方选举权恢复之前就出现了黑白工资收敛（“大压缩”可解释其中一半到三分之二），说明“不可能取得有效经济进步”过于绝对  
  来源：<https://cepr.org/voxeu/columns/persistence-racial-inequality-us>；<https://www.nber.org/papers/h0044>
- **#4** 「it is difficult to see how men like the Grimkes, Kelly Miller, J. W. E. Bowen, and other representatives of th…」  
  判断：**部分符合**。这一群体确实很快公开发声：1905年杜波依斯等人发起尼亚加拉运动，讨论华盛顿妥协路线之外的方案；阿奇博尔德·格里姆凯与华盛顿意见相左，1913年后投身全国有色人种协进会（NAACP）；鲍恩参与编辑《黑人之声》。但凯利·米勒多被视为温和的调和者，走华盛顿与杜波依斯之间的中间路线，书中点名者并非全部公开站到对立面  
  来源：<https://www.loc.gov/exhibitions/join-in-voluntary-associations-in-america/about-this-exhibition/a-nation-of-joiners/changing-america/niagara-movement/>；<https://www.scencyclopedia.org/sce/entries/grimke-archibald-henry/>；<https://en.wikipedia.org/wiki/The_Voice_of_the_Negro>；<https://www.scencyclopedia.org/sce/entries/miller-kelly-jr/>
- **#10** 「Crime, and a cheap and dangerous socialism, are the inevitable results of this pondering.」  
  判断：**部分符合**。“社会主义”一端有限出现：1931—1936年阿拉巴马佃农联合会是大萧条时期南方腹地最大的共产党组织、黑人领导的群众组织，成员是黑带的黑人佃农和农业工人；但该组织存续很短，“犯罪”一端没有找到可核实的证据，黑带农民的主要出路是迁移而非“不可避免”地走向犯罪和社会主义  
  来源：<https://encyclopediaofalabama.org/article/alabama-sharecroppers-union/>；<https://www.encyclopedia.com/economics/encyclopedias-almanacs-transcripts-and-maps/alabama-sharecroppers-union>；<https://www.history.com/articles/great-migration>
- **#13** 「I am becoming more and more convinced, as I look upon the system of common-school training in the South, that …」  
  判断：**部分符合**。联邦确实介入资助大众教育，但不算“很快”：1965年《中小学教育法》被称为美国历史上第一个一般性学校资助法案，打破了长期阻碍联邦向中小学拨款的僵局；此前的努力屡屡受阻（布莱尔教育法案1886年和1888年两度在参议院通过，但被众议院否决）；1964—1966年联邦K-12支出约增至三倍。距本书出版已过半个多世纪  
  来源：<https://www.encyclopedia.com/politics/encyclopedias-almanacs-transcripts-and-maps/elementary-and-secondary-education-act-79-stat-27-1965>；<https://www.edweek.org/policy-politics/the-evolving-federal-role/1999/11>；<https://doi.org/10.5810/kentucky/9780813140872.003.0008>
- **#16** 「Surely there shall yet dawn some mighty morning to lift the Veil and set the prisoned free.」  
  判断：**部分符合**。制度层面已改：1964年《民权法》第七章禁止基于种族、肤色的就业歧视，并设立平等就业机会委员会（EEOC）。但“只问能不能干、不问是不是白人”并未实现：对现场实验的元分析显示，25年来针对黑人求职者的招聘歧视没有下降  
  来源：<https://www.eeoc.gov/title-vii-civil-rights-act-1964-requiring-discrimination-free-workplaces-60-years>；<https://www.pnas.org/doi/10.1073/pnas.1706255114>；<https://hbr.org/2017/10/hiring-discrimination-against-black-americans-hasnt-declined-in-25-years>

### 错误（1 条）

- **#6** 「And this course of study will not change; its methods will grow more deft and effectual, its content richer by…」  
  判断：**错误**。博雅课程并非“不会改变”：20世纪初选修制瓦解，许多学院改为“专业集中+分布”的通识要求；过去30年本科教育中传统文理核心持续收缩，职业和专业学科扩张，商学学位兴起。哥伦比亚等校保留了核心课程，但书中所指的古典课程体系已发生实质变化  
  来源：<https://higher-ed2000.ucr.edu/Publications/Brint%20et%20al%20(2005).pdf>；<https://www.academia.edu/59926029/Higher_Education_During_the_20th_Century_The_Birth_of_College_Majors>；<https://core100.columbia.edu/about>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| 2 | The problem of the Twentieth Century is … | 重复 | 与第二章开头“二十世纪的问题是肤色界线问题”那条可核验预测为同一句话，在同章结尾逐字重申，按ASSESS duplicate排除，不重复计分 |

## 文件

- 本文：`cases/du-bois-souls-of-black-folk-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/du-bois-souls-of-black-folk-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/du-bois-souls-of-black-folk-v5/audit/manual_review_2026-11-15.py`
