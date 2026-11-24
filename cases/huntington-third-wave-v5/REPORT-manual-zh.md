# 塞缪尔·亨廷顿（Samuel P. Huntington）《第三波》：出版后预测人工核查

- 案例目录：`cases/huntington-third-wave-v5/`
- 出版日期：**1991-02**。英文原著 The Third Wave: Democratization in the Late Twentieth Century 由 University of Oklahoma Press 于1991年出版。本书写于1989–1990年，作者在前言中写明未纳入1990年之后的事件；前言落款为麻萨诸塞州坎布里奇，1991年2月。所用文本为刘军宁译本电子修订版（2011）PDF（reading-library/2026-11-15-未来判断书单/01-地缘政治/01-第三波.pdf，sha256 190a68c3212ee10820928d37a139e4a5ca4bfa02c0c9fabb294a3dd3e61abe64）。该PDF前部另有译者代译序和2011年文章《第三波：二十年之后看未来》，不属于1991年原书论证，按前言、目录等一起作为前后置不计预测。观察窗口按1991-02起算至2026-11-15；1990年及此前已发生的事件不计入出版后命中。正文由 pdftotext 25.03.0 转为TXT（sha256见 source_sha256），不把全文写入仓库。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

本稿按 METHOD.md 复刻仓库 DeepSeek 管线、仅以人工阅读替代模型调用：先对源文做 prepare_book v5 分块并逐块抽取，再经仓库代码对齐、去重后导入 data/claims.jsonl；核验时每条先写 scope，用 Exa 检索公开来源并抓取存档（data/sources/，sha256 记于 data/evidence.jsonl），再由助手按四分类规则评断，经 pipeline.py apply assess → check → report。本稿由助手逐条对照书中原文与存档证据人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 69 条，剔除非预测 0 条，计入 **69 条预测**，其中 **62 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 21 |
| 趋势符合 | 1 |
| 部分符合 | 35 |
| 错误 | 5 |
| 暂无法判断 | 7 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **33.9%**（21/62） |
| 加权胜率 | **63.3%** |
| 错误率 | **8.1%**（5/62） |
| 未定占比（暂无法判断/预测） | 10.1%（7/69） |

## 总体评价

亨廷顿1991年对第三波扩散及其条件的判断，约三分之一可判定条目完全命中，加权约六成，错误率较低。不少大胆判断写在条件句或复合判断里，记部分符合。真正写错的，主要是对俄国全面民主化和东亚一党独大格局的具体断言。第三波之后可能出现回潮记为趋势符合：全球自由连续下降，但尚未形成与前两次相当的完整反向浪潮。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（21 条）

- **#1** 「到二十世纪末，又有更多的国家具备了民主制度。」  
  判断：**正确**。Freedom House统计的选举民主国家从1990年的76个增至2000年的120个，明显多于1990年。  
  来源：<https://freedomhouse.org/sites/default/files/Number%20and%20Percentage%20of%20Electoral%20Democracy%2C%20FIW%201989-2015.pdf>
- **#9** 「短波收音机、卫星电视、电脑、传真机使得威权政府越来越难以对其精英和公众进行信息封锁，以防止他们知道发生在其他国家有关反对或推翻威权政府的斗争。」  
  判断：**正确**。卫星电视、互联网、移动通讯和社交媒体使威权政府的信息封锁成本显著上升，跨境信息流动远超1991年的短波与传真时代，方向与预测一致。  
  来源：<https://freedomhouse.org/country/china/freedom-net/2025>；<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>
- **#10** 「如果情况果真如此，在南非成功实现民主化的前景比在其他类型威权国家的可能性要大得多。」  
  判断：**正确**。南非于1994年举行首次多种族自由选举，结束种族隔离，此后多次举行被观察为大致自由公正的选举，2024年还首次出现执政党失去绝对多数后的和平权力重组；Freedom House 2025年仍将其评为“自由”（81/100），相对其他多数威权国家前景明显更好。  
  来源：<https://freedomhouse.org/country/south-africa/freedom-world/2025>；<https://www.democracyweb.org/study-guide/consent-of-the-governed/south-africa>
- **#12** 「但记录表明，在中等经济发展程度的国家，军方的权力会随着时间的推移而缩小。」  
  判断：**正确**。在南欧、多数南美及一批中等收入第三波国家，文官对军队的控制在1991年后总体加强，军方制度化否决权下降，与“随着时间推移而缩小”的方向一致。  
  来源：<https://www.tandfonline.com/doi/full/10.1080/13510347.2022.2130260>；<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>
- **#16** 「在德国和日本，对民主的广泛支持是代际交替的产物，因此，在短期内不大可能逆转。」  
  判断：**正确**。德国与日本在1990年代及此后仍是稳定的自由民主国家，对民主的广泛支持没有在“短期内”逆转。  
  来源：<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>
- **#17** 「可以合理地假设，这些社会也将比那些非工业化的社会更有利于新民主政权的巩固。」  
  判断：**正确**。工业化程度较高的新民主国家（南欧、中欧、韩国、台湾）总体比低收入、低工业化社会更成功地巩固了民主，与该项比较性判断一致。  
  来源：<https://www.tandfonline.com/doi/full/10.1080/13510347.2026.2615134>；<https://www.cambridge.org/core/journals/government-and-opposition/article/abs/european-union-accession-dynamics-and-democratization-in-central-and-eastern-europe-past-and-future-perspectives1/06E082A8716BE70FCF347666161DAC65>
- **#18** 「德国的统一使得民主在东德的前景与西德的稳定的民主环境命运悠关。」  
  判断：**正确**。两德统一后，原东德被纳入西德已巩固的宪政民主体制，统一德国持续被评为自由民主国家，东德地区的民主前景确实与西德稳定的民主环境绑定。  
  来源：<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>
- **#22** 「就土耳其目前的边际地位而言，穆斯林的遗产、过去的军人干预和令人怀疑的人权记录而言，土耳其的民主可能需要欧洲共同体的锚地，至少就像在七十年代西班牙、土耳其和希腊的民主那样。若是不能提供这种锚地，将会使得土耳其民主的未来更加…」  
  判断：**正确**。土耳其入盟谈判长期停滞，2018年后基本冻结；与此同时民主与法治显著回潮，Freedom House已将其评为“不自由”。缺少可靠的欧盟锚地后，其民主前景确实更为不确定并走向恶化。  
  来源：<https://freedomhouse.org/country/turkey/freedom-world/2025>；<https://stockholmcf.org/ep-draft-report-says-turkeys-eu-accession-remains-stalled-over-concerns-on-democracy-human-rights/>
- **#25** 「随着苏联控制的放松，更可能的是，民主政治将会在波罗的海国家重新建立起来。」  
  判断：**正确**。爱沙尼亚、拉脱维亚、立陶宛于1991年恢复独立，随即举行多党选举并建立宪政民主，此后持续被Freedom House评为“自由”国家，是前苏联加盟共和国中民主重建最成功的一批。  
  来源：<https://freedomhouse.org/sites/default/files/inline_images/Estonia.pdf>；<https://ponarseurasia.org/wp-content/uploads/attachments/pepm200.pdf>；<https://freedomhouse.org/country/latvia>
- **#26** 「迈向民主的运动也会存在于其他共和国。」  
  判断：**正确**。1990年代在俄罗斯、乌克兰、格鲁吉亚、亚美尼亚、摩尔多瓦等共和国都出现了明确的民主或独立民主运动，此后还有“颜色革命”等后续浪潮，与“也会存在于其他共和国”相符。  
  来源：<https://www.journalofdemocracy.org/articles/russias-road-to-autocracy/>；<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>
- **#27** 「潜伏着发生苏维埃式的热月政变的可能性。」  
  判断：**正确**。1991年8月苏联保守派发动企图推翻戈尔巴乔夫的政变，正是作者所说“苏维埃式热月政变”风险的实现；政变在数日内失败，但不否定“潜伏着可能性”这一判断被事件所证实。  
  来源：<https://en.wikipedia.org/wiki/1991_Soviet_coup_d%27%C3%A9tat_attempt>
- **#34** 「正如第五章所表明的，巩固民主的问题可能会导致在一些国家维持民主的条件不够充分的地方出现倒退。」  
  判断：**正确**。在民主先决条件较弱的一批第三波国家，巩固失败和回潮反复出现，如秘鲁1992年、若干非洲和后苏联案例，以及后来的突尼斯回潮等，与“条件不够充分的地方出现倒退”相符。  
  来源：<https://www.tandfonline.com/doi/full/10.1080/13510347.2022.2130260>；<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>
- **#35** 「民主政权若总是未能有效地运作，这将瓦解其合法性。」  
  判断：**正确**。当民主政府长期治理失败时，其合法性确实会受损，并在一批国家转化为对民主体制本身的怀疑和回潮，与该条件判断一致。  
  来源：<https://www.tandfonline.com/doi/full/10.1080/13510347.2022.2130260>；<https://ourworldindata.org/less-democratic>
- **#41** 「威权的民族主义可能在第三世界国家和东欧变成一种熟悉的现象。」  
  判断：**正确**。威权或威权倾向的民族主义在东欧（匈牙利等）、前苏联空间、土耳其以及一批亚非拉国家已成为常见的政治形态，与“可能变成一种熟悉的现象”相符。  
  来源：<https://www.tandfonline.com/doi/full/10.1080/13510347.2026.2615134>；<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>
- **#43** 「但是什叶派（Shi'ite）和逊尼派（Sunni）的原教旨主义运动（fundamentalist movements）都可能在其它国家掌权。」  
  判断：**正确**。1996年和2021年阿富汗塔利班、2007年后哈马斯在加沙、2012年埃及穆兄会短暂执政等，表明逊尼派（及更早的伊朗什叶派体系之外的）原教旨主义或伊斯兰主义运动确曾在其他国家掌权。  
  来源：<https://link.springer.com/article/10.1007/s12116-011-9086-z>；<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>
- **#44** 「民粹主义的独裁政权也可能就像它们过去对民主保护财产权或其他形式的权利而作出的反应一样在未来出现。」  
  判断：**正确**。1991年后出现了查韦斯–马杜罗治下的委内瑞拉以及一批被文献称为民粹主义威权的政权，证明民粹主义独裁作为对民主的一种反动形式再次出现。  
  来源：<https://www.tandfonline.com/doi/full/10.1080/13510347.2026.2615134>；<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>
- **#46** 「有一个可能也许是，在威权统治下出现的技术专制的电子独裁（techmocratic electronic dictatorship）会因为其操纵信息、媒介或复杂的通讯工具的能力而获得合法性，并变得可能。」  
  判断：**正确**。以中国为主要代表的数字监控、网络审查、生物识别和算法治理，使“依靠操纵信息、媒介和通讯工具而获得控制力的技术专制电子独裁”从设想变成了可观察的政权形态。  
  来源：<https://freedomhouse.org/country/china/freedom-world/2025>；<https://freedomhouse.org/country/china/freedom-net/2025>
- **#49** 「这些领导人的死亡或离职都可能会为其国家的民主化消除障碍，但这也并非必定如此。」  
  判断：**正确**。该判断本身已写明“可能会……但并非必定如此”：印尼、马拉维等出现了开放或转型，朝鲜、古巴、叙利亚等则没有，正好符合这种审慎的或然判断。  
  来源：<https://en.wikipedia.org/wiki/Fall_of_Suharto>；<https://freedomhouse.org/country/china/freedom-world/2025>；<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>
- **#62** 「未来的世界很可能会继续证明这一点。」  
  判断：**正确**。1990年代民主国家数目大幅增加，打破了1970年代的悲观论；2006年以后又出现持续二十年的自由下降和第三波回潮迹象，也打破了“历史终结”式的线性乐观。未来的世界确实继续证明两种简单判断都有差错。  
  来源：<https://freedomhouse.org/sites/default/files/Number%20and%20Percentage%20of%20Electoral%20Democracy%2C%20FIW%201989-2015.pdf>；<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>；<https://www.tandfonline.com/doi/full/10.1080/13510347.2026.2615134>
- **#63** 「第三波，即二十世纪末的“全球性民主革命”不会永远持续下去。」  
  判断：**正确**。按国家计数，第三波在1990年代和21世纪初继续推进并在约2010年代前后见顶，随后进入持续的自由下降和民主回潮，说明这场“全球性民主革命”并未永远持续下去。  
  来源：<https://freedomhouse.org/sites/default/files/Number%20and%20Percentage%20of%20Electoral%20Democracy%2C%20FIW%201989-2015.pdf>；<https://www.tandfonline.com/doi/full/10.1080/13510347.2026.2615134>；<https://ourworldindata.org/less-democratic>
- **#68** 「其次，新形式的威权主义可能会出现在那些富裕的、信息主导的和以技术为基础的社会。」  
  判断：**正确**。在已经相当富裕、高度信息化的中国，出现了以数字监控和信息控制为重要支柱的新型威权统治；其他高收入社会也出现了监控能力扩张的讨论和实践，与“新形式的威权主义可能出现在富裕的、信息主导的、以技术为基础的社会”相符。  
  来源：<https://freedomhouse.org/country/china/freedom-world/2025>；<https://freedomhouse.org/country/china/freedom-net/2025>

### 趋势符合（1 条）

- **#64** 「而且很可能会接踵而至的是新的一波，构成第三次回潮的威权主义浪潮。」  
  判断：**趋势符合**。文献已广泛讨论“第三波威权化/回潮”：Freedom House记录全球自由连续下降20年，选举民主国家从高峰约125个降至2025年的106个，V-Dem显示2012年以来威权化国家数目超过民主化国家。方向与“很可能接踵而至第三次回潮”一致，但回潮幅度仍小于前两次，多数第三波国家仍维持选举制度，完整历史形态尚未收束。  
  来源：<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>；<https://www.democracywithoutborders.org/41714/global-freedom-declined-for-two-consecutive-decades-freedom-house/>；<https://www.tandfonline.com/doi/full/10.1080/13510347.2026.2615134>；<https://ourworldindata.org/less-democratic>

### 部分符合（35 条）

- **#2** 「民主政治运作的长期后果可能是扩大和加深个人的自由。」  
  判断：**部分符合**。许多第三波国家在转型后扩大了公民自由，但Freedom House称2025年全球自由已连续下降20年，生活在“自由”国家的人口比例也低于书中所记1990年约39%。长期后果并非单向扩大。  
  来源：<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>；<https://ourworldindata.org/less-democratic>
- **#3** 「只要这种现象持续下去，民主在世界范围内的扩张就意味着和平地带在世界范围内的扩展。」  
  判断：**部分符合**。已建立的民主国家之间仍极少相互开战，1990年代民主扩张扩大了民主国家之间的和平地带；但此后部分新民主国家回潮，俄罗斯等非民主大国仍卷入大规模国际战争，和平扩展并不等于全球暴力减少。  
  来源：<https://ourworldindata.org/less-democratic>；<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>
- **#5** 「那些处于特定经济发展水平的国家，最可能向民主过渡，而且多数向民主过渡的国家也将在这一经济发展水平上。随着国家实现经济发展并进入这一地带，它们就会出现向民主化过渡的前景。」  
  判断：**部分符合**。中等收入“转型带”国家在1990年代及以后确有较多民主化（如一批拉美、东欧和部分东亚案例），但中国、若干石油富国等反例说明“最可能、多数将在这一水平上”并不严格成立。  
  来源：<https://www.tandfonline.com/doi/full/10.1080/13510347.2026.2615134>；<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>
- **#6** 「涉及到一些重大工业化的经济发展会导致新的、更加多样的、复杂的和互赖的经济，这种经济对威权政权来说越来越难以驾驭。」  
  判断：**部分符合**。工业化带来的经济复杂化确实增加了威权控制的成本，信息与私人部门更难全面管制；但中国、越南等在高度工业化后仍维持威权统治，说明“越来越难以驾驭”并未普遍导致政权失控或转型。  
  来源：<https://freedomhouse.org/country/china/freedom-world/2025>；<https://www.tandfonline.com/doi/full/10.1080/13510347.2026.2615134>
- **#7** 「从长远的观点看，经济发展将为民主政权创造基础。」  
  判断：**部分符合**。长期经济发展与民主之间仍呈正相关，许多进入中高收入的社会后来实现或巩固了民主；但中国等高速成长而持续威权的反例表明，经济发展只是为民主创造基础，并非充分条件。  
  来源：<https://www.tandfonline.com/doi/full/10.1080/13510347.2026.2615134>；<https://freedomhouse.org/country/china/freedom-world/2025>；<https://ourworldindata.org/less-democratic>
- **#8** 「因此，可以合理地假设，基督教的扩张将鼓励民主的发展。」  
  判断：**部分符合**。撒哈拉以南非洲基督徒人数继续增长，1990年代一些转型中教会确曾支持开放；但该地区民主巩固记录冷热不均，基督教扩张并未稳定地“鼓励”出更多持久民主。  
  来源：<https://www.tandfonline.com/doi/full/10.1080/13510347.2026.2615134>；<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>
- **#11** 「因此，从一党制国家民主转型很可能比从军人政权向民主国家的转型更为困难，但是，一旦成功，一党制国家的民主将有可能更为持久。」  
  判断：**部分符合**。前一党制国家（尤其东欧）的转型过程往往更曲折，一旦完成，波罗的海、捷克等案例相当持久；但匈牙利等出现回潮，而许多军人退出的拉美第三波国家也大体维持了选举民主，故“更困难但一旦成功更持久”只部分成立。  
  来源：<https://www.tandfonline.com/doi/full/10.1080/13510347.2022.2130260>；<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>
- **#13** 「不过，在大多数国家，似乎极可能的是，第三波民主政权不能有效地处理好这些问题，而且，他们将极有可能很难比他们的前任威权统治者更成功地做到这一点。」  
  判断：**部分符合**。不少第三波国家在腐败、不平等、债务和治安上表现平平，甚至不优于前任；但西班牙、葡萄牙、韩国、智利等在通胀、增长和治理上明显好于威权时期，故“大多数国家极可能无法更成功”说得过满。  
  来源：<https://www.tandfonline.com/doi/full/10.1080/13510347.2022.2130260>；<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>
- **#14** 「叛乱、通货膨胀、贫困、债务、不平等与机构臃肿都将多多少少地继续存在，就像前十年的情况那样。」  
  判断：**部分符合**。贫困、不平等、债务和治理臃肿在许多第三波国家确实持续存在；但全球极端贫困下降，若干国家通胀得到控制，并非六类问题都“多多少少”原样延续。  
  来源：<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>；<https://ourworldindata.org/less-democratic>
- **#15** 「显然在菲律宾、秘鲁和危地马拉这样的国家，民主面临着极大的压力。那里的问题数不胜数，而且性质严重：这些问题没有自动消失，而且也将得不到解决。」  
  判断：**部分符合**。三国民主长期承受高压：秘鲁1992年出现藤森“自我政变”，菲律宾在杜特尔特时期权利受损，危地马拉反复陷入机构危机；重大社会经济问题也未得到根本解决。但三国仍大体维持选举政治，并非完全崩溃。  
  来源：<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>；<https://www.tandfonline.com/doi/full/10.1080/13510347.2022.2130260>
- **#19** 「这些判断建立在这样一种假设之上，即欧洲共同体和美国将继续致力于促进民主。」  
  判断：**部分符合**。1990–2000年代欧盟扩大与美国的民主援助、支持选举观察等确实延续了促民主政策；但此后力度起伏，Freedom House 2026年报告并记载近年欧洲减少民主援助、2025年美国大幅取消对外援助项目。  
  来源：<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>；<https://www.cambridge.org/core/journals/government-and-opposition/article/abs/european-union-accession-dynamics-and-democratization-in-central-and-eastern-europe-past-and-future-perspectives1/06E082A8716BE70FCF347666161DAC65>
- **#20** 「随着基督徒人数的成倍增加，教会领导人在支持民主方面的活动大概将不会下降。他们的政治权力将会增加。」  
  判断：**部分符合**。1990年代非洲若干转型中教会确实发挥了推动开放的作用，基督徒人口也继续增长；但教会政治权力并非在各国都持续上升，后来在一些国家影响力下降或立场分化。  
  来源：<https://www.tandfonline.com/doi/full/10.1080/13510347.2026.2615134>；<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>
- **#21** 「这将可望导致宗教教徒和活动的增加，同时也对这个国家的民主未来有积极意义。」  
  判断：**部分符合**。苏联解体后东正教和其他宗教活动明显恢复；这对波罗的海等国的民主并无妨碍，但在俄罗斯，宗教复兴并未带来持久的民主巩固。  
  来源：<https://freedomhouse.org/country/russia/freedom-world/2025>；<https://freedomhouse.org/sites/default/files/inline_images/Estonia.pdf>；<https://ponarseurasia.org/wp-content/uploads/attachments/pepm200.pdf>
- **#23** 「取得欧洲共同体成员资格的前景也会加强东欧和中欧新民主国家。」  
  判断：**部分符合**。入盟前景和2004/2007年扩大显著推动了中东欧在1990年代和入盟前后的民主巩固与制度改革；但入盟后条件约束减弱，匈牙利出现系统性的自由民主回潮，波兰也一度明显回潮，故“会加强”并非持续到底。  
  来源：<https://www.cambridge.org/core/journals/government-and-opposition/article/abs/european-union-accession-dynamics-and-democratization-in-central-and-eastern-europe-past-and-future-perspectives1/06E082A8716BE70FCF347666161DAC65>；<https://www.tandfonline.com/doi/full/10.1080/13510347.2022.2130260>
- **#24** 「如果苏联结束或大量减少其对卡斯特罗政权的支持，在古巴也许会出现迈向民主的运动。」  
  判断：**部分符合**。苏联解体后对古巴的援助和贸易大幅下降，1994年哈瓦那爆发“Maleconazo”抗议，之后仍有2021年大规模示威，说明“迈向民主的运动”一度出现；但古巴并未实现民主转型，政权维持至今。  
  来源：<https://en.wikipedia.org/wiki/Maleconazo>；<https://www.washingtonpost.com/outlook/2021/07/22/anticipating-todays-protests-cubans-took-streets-1994-too/>；<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>
- **#28** 「它也可能再次在重要性上趋于次要地位。」  
  判断：**部分符合**。美国促进民主的优先性随政府更迭起伏：1990年代和21世纪初一度上升，之后在若干时期降为次要目标，2025年还出现大幅取消对外援助、减少公开谴责舞弊选举等变化，故“也可能再次趋于次要”说中了方向，但并非直线下降。  
  来源：<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>
- **#29** 「与苏联的冷战和意识形态竞争的结束可能会摒弃其支持反共的独裁者的行动准则，但是也可能减少美国对第三世界的任何实质性的介入。」  
  判断：**部分符合**。冷战后美国不再以“支持反共独裁者”为常规准则，对若干昔日反共伙伴施加了更大的民主压力；但美国并未持续减少对第三世界的实质性介入（海湾战争后仍有多次军事与安全介入），两个分项只说中了一半。  
  来源：<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>
- **#30** 「美国做到这一点的能力似乎可能受到了约束。」  
  判断：**部分符合**。预算约束、伊拉克战争后的政治代价以及2025年援助收缩，都显示美国对外促民主的可用资源与手段受到限制；但1990–2000年代美国仍拥有很强的议程设置能力，故“能力下降”主要体现在窗口后段。  
  来源：<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>
- **#32** 「如果这种情况真的发生了，那么，所体察到的美国的失败会不可避免地被看作民主的失败。世界范围内对民主的诉求也会受到重大的挫折。」  
  判断：**部分符合**。不少国际舆论确实在不同阶段将美国视为相对衰落并伴有国内撕裂，同期全球民主扩张受挫、自由连续下降；但民主衰退有多种原因，无法把“被看作民主的失败”完全归因于对美国典范的观感。  
  来源：<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>；<https://ourworldindata.org/less-democratic>
- **#33** 「可以想象，法国也许会在其以前的非洲殖民地国家促进民主方面起更积极的作用。」  
  判断：**部分符合**。法国在1990年拉博勒讲话后曾把援助与多党化挂钩，在部分前殖民地推动了开放；但此后长期同时维持对若干威权政权的支持，并非持续地“更积极地促进民主”。  
  来源：<https://www.tandfonline.com/doi/full/10.1080/13510347.2026.2615134>；<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>
- **#36** 「然而，若是长期不能提供福利、繁荣、公平、正义、国内秩序或外部安全，就会慢慢地瓦解民主政府自身的合法性。随着对威权失败记忆的淡漠，对民主失败的不满就有可能增加。」  
  判断：**部分符合**。在部分新民主国家，随着对威权失败记忆淡漠，对民主治理失效的不满上升，并出现威权怀旧；但并非所有第三波国家都出现合法性的缓慢瓦解。  
  来源：<https://www.tandfonline.com/doi/full/10.1080/13510347.2022.2130260>；<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>
- **#38** 「任何民主化或正在民主化的大国转向威权主义都可能在其它国家触发类似的滚雪球行为。」  
  判断：**部分符合**。俄罗斯在2000年代以后转向威权，并对外输出影响；中国也提供了另一种威权样板。若干国家出现仿效或受到鼓励，但并未形成像前两次回潮那样全面的“滚雪球”崩溃。  
  来源：<https://www.journalofdemocracy.org/articles/russias-road-to-autocracy/>；<https://www.tandfonline.com/doi/full/10.1080/13510347.2026.2615134>；<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>
- **#39** 「在俄罗斯或苏联朝着威权方向的逆转都有可能会对苏维埃各共和国、保加利亚、罗马尼亚、南斯拉夫和蒙古的民主化产生令人不安的影响，甚至也可能对波兰、匈牙利和捷克产生类似的影响。」  
  判断：**部分符合**。俄罗斯转向威权后，对格鲁吉亚、乌克兰、摩尔多瓦、白俄罗斯等地的民主化与主权选择施加了公开压力乃至战争，邻国受到“令人不安的影响”；但对波兰、匈牙利、捷克的影响更多是间接的，其回潮也有强烈国内原因。  
  来源：<https://www.journalofdemocracy.org/articles/russias-road-to-autocracy/>；<https://freedomhouse.org/country/russia/freedom-world/2025>；<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>
- **#42** 「如果是后者，威权的民族主义政权可能会重返一些东欧的国家。」  
  判断：**部分符合**。1989–1990年东欧革命兼有反专制与民族主义成分，前提难以判定为“主要是后者”；不过匈牙利等国后来确实出现带有民族主义色彩的威权化转向，与可能的回流方向部分相符。  
  来源：<https://www.tandfonline.com/doi/full/10.1080/13510347.2022.2130260>；<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>
- **#45** 「族群型的独裁有可能会出现在有两个以上的民族、种族或宗教集团参与其政治的民主国家。」  
  判断：**部分符合**。在一些多族群社会出现了以主导族群为基础的威权化或排斥性统治（如缅甸、以及若干非洲和巴尔干案例），但并非所有“有两个以上民族、种族或宗教集团参与政治的民主国家”都走向族群型独裁。  
  来源：<https://www.tandfonline.com/doi/full/10.1080/13510347.2022.2130260>；<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>
- **#47** 「民主化的一个障碍可能在九十年代的几个国家中消失。」  
  判断：**部分符合**。1990年代确有一批长期执政者死亡或去职（如马拉维班达失去权力、象牙海岸乌弗埃-博瓦尼去世、苏哈托1998年下台），其中一些国家的民主化障碍随之减弱；但朝鲜、古巴等并未因此出现民主化，故只是“可能在几个国家消失”，并非普遍实现。  
  来源：<https://en.wikipedia.org/wiki/Fall_of_Suharto>；<https://www.tandfonline.com/doi/full/10.1080/13510347.2026.2615134>
- **#48** 「在九十年代，某些人的死亡可能会确保一些威权国家实现这一变革。」  
  判断：**部分符合**。马拉维在班达失去权力后举行了多党选举，印尼在苏哈托下台后开启民主转型，说明“某些人的死亡或去职”与变革有关；但“可能会确保”对朝鲜（金日成1994年去世后政权延续）并不成立。  
  来源：<https://en.wikipedia.org/wiki/Fall_of_Suharto>；<https://www.tandfonline.com/doi/full/10.1080/13510347.2026.2615134>
- **#51** 「这条线现在也许可以把那些民主已经扎根的地区与民主尚未扎根的地区区分开来。」  
  判断：**部分符合**。该线以西的波兰、捷克、斯洛文尼亚、波罗的海等国总体比以东的俄罗斯、白俄罗斯更成功地扎根了民主；但匈牙利严重回潮，乌克兰等国长期在争夺之中，分界线只有粗略的区分力。  
  来源：<https://ponarseurasia.org/wp-content/uploads/attachments/pepm200.pdf>；<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>；<https://www.tandfonline.com/doi/full/10.1080/13510347.2022.2130260>
- **#56** 「贫穷也可能是民主发展的主要障碍。民主的前景取决于经济发展的前景。」  
  判断：**部分符合**。经济发展水平与民主之间的正相关仍然稳固，许多持续贫困的社会仍非自由民主；但印度长期是低收入民主、中国是高增长威权，说明贫穷既非唯一也非不可克服的障碍。  
  来源：<https://www.tandfonline.com/doi/full/10.1080/13510347.2026.2615134>；<https://ourworldindata.org/less-democratic>
- **#57** 「如果这一预测准确的话，民主化在撒哈拉以南非洲的民主化的经济障碍将持续存在下去，并会延伸到二十一世纪。」  
  判断：**部分符合**。1990年代撒哈拉以南非洲人均GDP增速大致停留在很低水平，与世界银行约0.5%的预测同一量级，前提可视为基本满足；经济障碍延续到21世纪初，尽管2000年代增长加快、部分国家出现开放，民主巩固仍然脆弱。  
  来源：<https://data.worldbank.org/indicator/NY.GDP.PCAP.KD.ZG?locations=ZG>；<https://www.imf.org/external/pubs/ft/fandd/2006/03/pattillo.htm>；<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>
- **#58** 「不过，在这些国家的经济发展的低水平通常意味着即使按3%至5% 的年人均增长率，有利于现代化的经济条件仍然需要漫长的时间才会到来。」  
  判断：**部分符合**。对一些低收入亚洲国家而言，进入有利于民主的经济区确实花了很长时间；但中国实际增速远高于3%–5%，在二十年左右已进入中高收入，时间并不“漫长”，且经济条件改善后仍未民主化。  
  来源：<https://freedomhouse.org/country/china/freedom-world/2025>；<https://www.tandfonline.com/doi/full/10.1080/13510347.2026.2615134>
- **#59** 「如果这一成长率能够维持下去，有利于民主化的政治条件就有可能在九十年代的某个时候在这些国家出现。」  
  判断：**部分符合**。五国并未都维持1980–1988年的高增速（1997年亚洲金融危机冲击泰国、马来西亚）；政治上，泰国在1990年代有过开放也有反复，突尼斯要到2011年才出现重大转型，喀麦隆则几乎没有出现有利于民主化的政治条件。  
  来源：<https://www.tandfonline.com/doi/full/10.1080/13510347.2026.2615134>；<https://link.springer.com/article/10.1007/s12116-011-9086-z>；<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>
- **#60** 「如果它们能够维持这一速度，到二十一世纪初就有可能迈入有利于民主化的经济区。」  
  判断：**部分符合**。这些国家的增长轨迹并不一律，进入中等收入、有利于民主化的经济区的程度参差不齐；摩洛哥、塞内加尔有限开放，刚果、津巴布韦、也门则远离稳定的民主转型带，整体不能算作到二十一世纪初普遍迈入该经济区。  
  来源：<https://data.worldbank.org/indicator/NY.GDP.PCAP.KD.ZG?locations=ZG>；<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>
- **#66** 「许多贫穷的社会将继续处于不民主之中，只要它们继续贫困下去。」  
  判断：**部分符合**。持续贫困的社会中不民主政权的比例仍然显著更高，该条件判断大体成立；但存在贫困而维持选举民主、以及致富却不转型的例外，故不能当成严格定律。  
  来源：<https://www.tandfonline.com/doi/full/10.1080/13510347.2026.2615134>；<https://ourworldindata.org/less-democratic>
- **#67** 「对后发展国家（主要指非洲）来说，经济发展也许会比早发展国家更为困难」  
  判断：**部分符合**。1990年代非洲增长确实落后，与早发展国家的差距在一段时间扩大；但2000年代非洲增长加快，东亚等后发展地区出现显著追赶，故“更为困难且差距史无前例地扩大”只部分符合后来的记录。  
  来源：<https://www.imf.org/external/pubs/ft/fandd/2006/03/pattillo.htm>；<https://data.worldbank.org/indicator/NY.GDP.PCAP.KD.ZG?locations=ZG>

### 错误（5 条）

- **#50** 「自由化在苏联正在进行，很可能这也会导致在俄国实现全面的民主化。」  
  判断：**错误**。苏联的自由化并未导致俄国实现全面而巩固的民主。1990年代出现过竞争性选举和不完整的开放，但2000年代以后权力重新集中，Freedom House自2005年起将俄罗斯评为“不自由”，与“很可能导致全面民主化”的主判断相反。  
  来源：<https://freedomhouse.org/country/russia/freedom-world/2025>；<https://www.journalofdemocracy.org/articles/russias-road-to-autocracy/>
- **#52** 「台湾的民主发展似乎也在朝着一种国民党可能会成为一党独大的选举制度方向发展」  
  判断：**错误**。2000年民进党候选人陈水扁当选总统，结束国民党长期执政，其后国民党与民进党多次轮替，台湾并未走向“国民党一党独大的选举制度”。  
  来源：<https://archive.nytimes.com/www.nytimes.com/library/world/asia/031900taiwan-election.html>；<https://www.taipeitimes.com/News/local/archives/2000/05/21/0000036931>；<https://english.president.gov.tw/NEWS/2643>
- **#53** 「民主进步党会被限制在永久反对派的角色之上。」  
  判断：**错误**。民进党不仅未停留在“永久反对派”角色，而且在2000年、2016年、2020年和2024年多次赢得总统选举并执政。  
  来源：<https://archive.nytimes.com/www.nytimes.com/library/world/asia/031900taiwan-election.html>；<https://english.president.gov.tw/NEWS/2643>
- **#54** 「因此，可以想象，其他东亚国家与日本一起会建立一个相对公平的竞技场，而在日本的这一竞技场中政府总是获胜。」  
  判断：**错误**。韩国1997年金大中当选实现轮替，台湾2000年实现轮替，日本自民党也在2009年一度失去政权，说明“相对公平的竞技场上政府总是获胜”并未成为东亚的普遍模式；该判断只在新加坡等地更接近事实。  
  来源：<https://archive.nytimes.com/www.nytimes.com/library/world/asia/031900taiwan-election.html>；<https://www.cambridge.org/core/journals/government-and-opposition/article/abs/power-alternation-in-south-korea/976A1B01580F1E4A1BDC0DEBA5AAD84B>
- **#61** 「在七十年代和八十年代，从一个地区横扫另一个地区的民主化浪潮可能会在九十年代变成中东和北非政治的一个典型特征。」  
  判断：**错误**。1990年代中东和北非出现的是有限、可逆的自由化，而不是像1970–80年代那样横扫地区的民主化浪潮。专门研究指出该地区“错过了第三波”；大规模变动要到2011年阿拉伯之春才出现，且多以失败或内战告终。  
  来源：<https://link.springer.com/article/10.1007/s12116-011-9086-z>；<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>

### 暂无法判断（7 条）

- **#4** 「根据过去的经验，一个民主占主导地位的世界很可能是一个相对免于国际暴力的世界，特别是如果苏联和中国变成了像其他主要大国那样的民主国家，重大的国际战争的可能性就会极大降低。」  
  判断：**暂无法判断**。“苏联和中国变成像其他主要大国那样的民主国家”这一前提在观察窗口内并未出现， accordingly不能用现有战争记录代替该条件预测的结果。一个民主占主导的世界也尚未实现。  
  来源：<https://freedomhouse.org/country/russia/freedom-world/2025>；<https://freedomhouse.org/country/china/freedom-world/2025>
- **#31** 「美国在海湾部署的庞大军队如果能够维持下去的话将对自由化、如果不是民主化起着强有力的外部推动作用，如果出现要求民主的运动的话，这种军事部署完全有可能被维持下去。」  
  判断：**暂无法判断**。约50万美军在海湾的大规模部署在1991年战争结束后并未维持；因此“若能维持将对科威特和沙特自由化起强有力推动”这一条件预测的前提未触发，不能以其后有限的科威特议会政治来代替。  
  来源：<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>
- **#37** 「然而，若是在未来出现规模相当的经济灾难，有一些国家很可能会放弃民主。」  
  判断：**暂无法判断**。1991年以来虽有1997–1998年金融危机、2008年全球金融危机和新冠冲击，但尚未出现与1929–1930年同等规模和持续时间的全球性经济崩溃，前提未触发，不能据此评正确或错误。  
  来源：<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>
- **#40** 「威权政权在印度的确立可能会对其它的第三世界国家产生重大的示范效应。」  
  判断：**暂无法判断**。印度在部分民主指数上出现回潮，但并未确立为明确的威权政权，更谈不上对其他第三世界国家产生“重大示范效应”。前提未充分触发。  
  来源：<https://ourworldindata.org/less-democratic>；<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>
- **#55** 「那时，政府就有可能用镇压不同意见、并强加威权控制的方式来作出反应。」  
  判断：**暂无法判断**。韩国、台湾和日本后来都出现了政党轮替，从而退出了“政治结构不允许把现任者赶下台”的前提；新加坡等地未经历作者所设想的那种增长终结加严重冲突后的全面高压转型。条件未典型触发。  
  来源：<https://www.cambridge.org/core/journals/government-and-opposition/article/abs/power-alternation-in-south-korea/976A1B01580F1E4A1BDC0DEBA5AAD84B>；<https://archive.nytimes.com/www.nytimes.com/library/world/asia/031900taiwan-election.html>
- **#65** 「不过，这并不能排除在二十一世纪在某个时候出现第四次民主化浪潮。」  
  判断：**暂无法判断**。21世纪出现过颜色革命、阿拉伯之春和一些局部开放，但学界并未就“第四波民主化”是否已经到来达成一致，该判断只说“不能排除”，在窗口结束时既不能证实也不能证伪一次清晰的第四波。  
  来源：<https://www.tandfonline.com/doi/full/10.1080/13510347.2026.2615134>；<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>
- **#69** 「如果这样的可能性没有变成现实，经济发展就应该为以民主体制取代威权体制逐步创造条件。时间属于民主一边。」  
  判断：**暂无法判断**。“新形式的威权主义出现在富裕信息社会”这一可能性已经变成现实，因此“如果这样的可能性没有变成现实，时间属于民主一边”的前提未满足，不能用此后民主的总体进退来评正确或错误。  
  来源：<https://freedomhouse.org/country/china/freedom-world/2025>；<https://freedomhouse.org/report/freedom-world/2026/growing-shadow-autocracy>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/huntington-third-wave-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/huntington-third-wave-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/huntington-third-wave-v5/audit/manual_review_2026-11-15.py`

## 说明

- 本 audit 文件由批量 QA 于 2026-11-16 根据已有判定（来源：results.manual.jsonl）重建，供 canonical manual_report.py 生成报告；判定本身未在重建时改写。

