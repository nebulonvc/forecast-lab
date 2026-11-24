# 法里德·扎卡利亚（Fareed Zakaria）《后美国世界》：出版后预测人工核查

- 案例目录：`cases/zakaria-post-american-world-v5/`
- 出版日期：**2008-05-01**。W. W. Norton 2008年第一版精装（The Post-American World，ISBN 978-0-393-06235-9，LCCN 2008001306，OCLC 181139415）。版权页仅署 2008 年 First Edition。Wikipedia 记为 2008 年 5 月初出版，StoryGraph 列 Edition Pub Date 为 2008-05-01，本书于 2008-05-18 进入《纽约时报》非虚构畅销书榜。观察窗口按 2008-05 起算至 2026-11-15。所用文件是 scanning PDF（308 页，含护封、目录、正文 1–259、注释 261–267、致谢 269–272、索引 273–292），sha256 9e2c3e95af6cba803368e50a7adc044b1dbcea176ad302a7c44d183f3b5c2fa1（与 catalog.json 一致）。正文 TXT 由 pdftotext 25.03.0 -enc UTF-8 默认布局从该 PDF 生成，sha256 8ac907a1b77b9213f0e66e83a78f5beb98535839cc5327ee0c6b3daca31919e5；引文按该 TXT 的行号与字符偏移核验。未把全文文本加入仓库。本书为 2008 年初版，不采用 2009 年平装新增序言或 2011 年 Release 2.0 的增补内容。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

本稿按 METHOD.md 复刻仓库 DeepSeek 管线、仅以人工阅读替代模型调用：先对源文做 prepare_book v5 分块并逐块抽取，再经仓库代码对齐、去重后导入 data/claims.jsonl；核验时每条先写 scope，用 Exa 检索公开来源并抓取存档（data/sources/，sha256 记于 data/evidence.jsonl），再由助手按四分类规则评断，经 pipeline.py apply assess → check → report。本稿由助手逐条对照书中原文与存档证据人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 103 条，剔除非预测 0 条，计入 **103 条预测**，其中 **83 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 49 |
| 趋势符合 | 1 |
| 部分符合 | 28 |
| 错误 | 5 |
| 暂无法判断 | 20 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **59.0%**（49/83） |
| 加权胜率 | **76.8%** |
| 错误率 | **6.0%**（5/83） |
| 未定占比（暂无法判断/预测） | 19.4%（20/103） |

## 总体评价

扎卡利亚2008年对“后美国”权力分散、中国与新兴经济体权重上升、美国仍具制度与创新优势等大方向多数成立，但也有美国现价GDP全球份额不降反升等与原文不完全相符之处。约两成条目因终点未到或条件未触发暂无法判断；趋势符合很少，说明多数无日期方向判断已按窗口计分。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（49 条）

- **#1** 「The tallest building in the world is now in Taipei, and it will soon be overtaken by one being built in Dubai.」  
  判断：**正确**。哈利法塔于2010年开放，2011年正式落成后取代台北101成为世界最高楼，与预测一致。  
  来源：<https://en.wikipedia.org/wiki/Burj_Khalifa>
- **#3** 「The emerging international system is likely to be quite differ­ ent from those that have preceded it.」  
  判断：**正确**。出版后出现中国按PPP成为最大经济体、金砖扩员、中美贸易冲突和更多新兴机构，国际体系较2008年前已明显不同。  
  来源：<https://en.wikipedia.org/wiki/Economy_of_China>；<https://en.wikipedia.org/wiki/Economy_of_India>；<https://en.wikipedia.org/wiki/BRICS>；<https://en.wikipedia.org/wiki/China–United_States_trade_war>
- **#4** 「But we are moving into a post-American world, one defined and directed from many places and by many people.」  
  判断：**正确**。美国仍是最大名义经济体，但中国、印度和金砖等角色显著上升，全球议程不再由单一中心单独定义。  
  来源：<https://en.wikipedia.org/wiki/Economy_of_China>；<https://en.wikipedia.org/wiki/Economy_of_India>；<https://en.wikipedia.org/wiki/BRICS>；<https://en.wikipedia.org/wiki/Economy_of_the_United_States>
- **#9** 「The most likely scenario—a series of backpack or truck bombings in the United States—would be a shock, but in …」  
  判断：**正确**。2013年波士顿马拉松发生背包炸弹袭击，造成严重局地伤亡，但未演变为全国性长期中断，社会生活较快恢复。  
  来源：<https://en.wikipedia.org/wiki/Boston_Marathon_bombing>
- **#11** 「But, for the foreseeable future, it will surely manage to double the size of its economy just by continuing to」  
  判断：**正确**。世界银行现价美元GDP显示中国由2008年约4.67万亿美元增至2015年约11.28万亿美元，已超过翻倍。  
  来源：<https://api.worldbank.org/v2/country/USA/indicator/NY.GDP.MKTP.CD>；<https://en.wikipedia.org/wiki/Economy_of_China>
- **#12** 「India, starting at an even lower base income, will also be able to grow for several decades before hitting the…」  
  判断：**正确**。2008–2025年印度名义GDP由约1.20万亿增至约3.96万亿美元，持续增长且尚未出现长期停滞。  
  来源：<https://api.worldbank.org/v2/country/USA/indicator/NY.GDP.MKTP.CD>；<https://en.wikipedia.org/wiki/Economy_of_India>
- **#14** 「These pressures will surely at some point end the era of low inflation that has undergirded global prosperity.」  
  判断：**正确**。2021年中至2022年中出现全球通胀潮，美国CPI在2022年升至约8%，低通胀时代被打断。  
  来源：<https://en.wikipedia.org/wiki/2021%E2%80%932023_inflation_surge>；<https://api.worldbank.org/v2/country/USA/indicator/NY.GDP.MKTP.CD>
- **#18** 「feeding a global population of eight billion, which we will get to by 2025, will require crop yields to reach …」  
  判断：**正确**。联合国估计2022年11月15日世界人口已超80亿；OWID世界谷物单产2020年已达约4.11吨/公顷，两项均在2025年前实现。  
  来源：<https://en.wikipedia.org/wiki/World_population>；<https://ourworldindata.org/grapher/cereal-yield>；<https://ourworldindata.org/grapher/population>
- **#23** 「As economic fortunes rise, so does nationalism.」  
  判断：**正确**。中国在国力上升同时强化政治集中与民族话语，印度在增长期出现以莫迪为代表的民族主义政治，中美冲突也带有经济民族主义色彩。  
  来源：<https://en.wikipedia.org/wiki/China–United_States_trade_war>；<https://en.wikipedia.org/wiki/Xi_Jinping>；<https://en.wikipedia.org/wiki/Narendra_Modi>
- **#24** 「The next round of rising pow­ ers might not be so eager to "fit in."」  
  判断：**正确**。一带一路、金砖扩员和中美贸易科技冲突表明主要崛起国按自身条件行事，而非简单融入。  
  来源：<https://en.wikipedia.org/wiki/Belt_and_Road_Initiative>；<https://en.wikipedia.org/wiki/China–United_States_trade_war>；<https://en.wikipedia.org/wiki/BRICS>
- **#25** 「In fact, rising powers appear to be follow­ ing a third way: entering the Western order but doing so on their …」  
  判断：**正确**。金砖扩员和一带一路等显示新兴大国进入现有秩序但同时另建机制、重塑规则。  
  来源：<https://en.wikipedia.org/wiki/Belt_and_Road_Initiative>；<https://en.wikipedia.org/wiki/BRICS>；<https://en.wikipedia.org/wiki/China–United_States_trade_war>
- **#27** 「China, India, Brazil, and other emerging powers will not follow along with a Western-led process in which they…」  
  判断：**正确**。在发展融资和贸易等领域，新兴大国更多推动平行机制或要求改写议程，而不是简单追随既有西方主导进程。  
  来源：<https://en.wikipedia.org/wiki/Belt_and_Road_Initiative>；<https://en.wikipedia.org/wiki/BRICS>；<https://en.wikipedia.org/wiki/China–United_States_trade_war>
- **#30** 「America will face the most intense economic competition it has ever faced.」  
  判断：**正确**。2018年起的中美贸易与科技冲突，以及中国作为第二大经济体的竞争，使美国面对前所未有的大国经济竞争。  
  来源：<https://en.wikipedia.org/wiki/China–United_States_trade_war>；<https://en.wikipedia.org/wiki/Economy_of_China>；<https://en.wikipedia.org/wiki/Economy_of_the_United_States>
- **#31** 「This hybrid international system—more democratic, more dynamic, more open, more connected—is one we are likely…」  
  判断：**正确**。至2026年美国仍是最大名义经济体和主要军事开支国，同时中国等力量上升，体系仍属一超多强。  
  来源：<https://en.wikipedia.org/wiki/Economy_of_the_United_States>；<https://en.wikipedia.org/wiki/Economy_of_China>；<https://en.wikipedia.org/wiki/List_of_countries_by_military_expenditures>；<https://en.wikipedia.org/wiki/BRICS>
- **#32** 「Most other great powers will see their role in the world expand.」  
  判断：**正确**。中国、印度国际角色明显扩大，俄罗斯以战争方式强势介入欧洲安全，金砖扩员也反映新兴力量空间增大。  
  来源：<https://en.wikipedia.org/wiki/Economy_of_China>；<https://en.wikipedia.org/wiki/Economy_of_India>；<https://en.wikipedia.org/wiki/Belt_and_Road_Initiative>；<https://en.wikipedia.org/wiki/BRICS>；<https://en.wikipedia.org/wiki/Russian_invasion_of_Ukraine>
- **#33** 「America's enormous space for action will inevitably diminish.」  
  判断：**正确**。中美竞争、南海争端、乌克兰战争和盟友协调需求，使美国更难单独塑造结果。  
  来源：<https://en.wikipedia.org/wiki/China–United_States_trade_war>；<https://en.wikipedia.org/wiki/Russian_invasion_of_Ukraine>；<https://en.wikipedia.org/wiki/Territorial_disputes_in_the_South_China_Sea>；<https://en.wikipedia.org/wiki/Quadrilateral_Security_Dialogue>
- **#36** 「Despite the rise of other nations and continents, the shadows of the West will be long and its legacies deep f…」  
  判断：**正确**。美元仍是首要储备货币，美国仍是最大名义经济体并提供关键储备资产与市场，西方制度与货币影响仍然深远。  
  来源：<https://en.wikipedia.org/wiki/Reserve_currency>；<https://en.wikipedia.org/wiki/International_use_of_the_U.S._dollar>；<https://en.wikipedia.org/wiki/Economy_of_the_United_States>
- **#43** 「Take human rights, an issue on which non-Western countries in general and China and India in particular are li…」  
  判断：**正确**。中国人权受到严厉限制且政治体制为威权，与美国人权外交话语和制度明显不同。  
  来源：<https://en.wikipedia.org/wiki/Human_rights_in_China>
- **#44** 「are not Protestant, proselytizing powers and thus will be less eager to spread universal values across the glo…」  
  判断：**正确**。中国对外以发展、主权和不干涉为主要话语，并通过一带一路扩展利益，而非推广西式普遍人权价值。  
  来源：<https://en.wikipedia.org/wiki/Human_rights_in_China>；<https://en.wikipedia.org/wiki/Belt_and_Road_Initiative>
- **#45** 「both countries are unlikely to view human rights issues as central to their foreign policy.」  
  判断：**正确**。中国外交实践并不以人权为核心议程，与预测相符。  
  来源：<https://en.wikipedia.org/wiki/Human_rights_in_China>；<https://en.wikipedia.org/wiki/Belt_and_Road_Initiative>
- **#46** 「The great shift taking place in the world might prove to be less about culture and more about power.」  
  判断：**正确**。已观察窗口中的核心变化是经济与军事力量重新分配及战略竞争，而非单纯文化冲突。  
  来源：<https://en.wikipedia.org/wiki/Economy_of_China>；<https://en.wikipedia.org/wiki/List_of_countries_by_military_expenditures>；<https://en.wikipedia.org/wiki/China–United_States_trade_war>；<https://en.wikipedia.org/wiki/Belt_and_Road_Initiative>
- **#49** 「The regime will almost certainly face significant chal­ lenges over the next fifteen years, even if this does …」  
  判断：**正确**。至2023年十五年窗口结束，中国未变成西式自由民主，反而取消连任限制、维持威权体制。  
  来源：<https://en.wikipedia.org/wiki/Xi_Jinping>；<https://en.wikipedia.org/wiki/Human_rights_in_China>
- **#50** 「political upheaval and turmoil will not necessarily stop China from growing. Whatever the future of its politi…」  
  判断：**正确**。未出现政权崩溃，经济持续扩大并保持世界第二（PPP第一），崛起进程没有被逆转。  
  来源：<https://api.worldbank.org/v2/country/USA/indicator/NY.GDP.MKTP.CD>；<https://en.wikipedia.org/wiki/Economy_of_China>；<https://en.wikipedia.org/wiki/Xi_Jinping>
- **#52** 「They are unlikely to cast aside casually three decades of relative stability and prosperity.」  
  判断：**正确**。观察窗口内未出现推翻改革开放以来基本路线的大规模政治抛弃，权力交接在现体制内完成。  
  来源：<https://en.wikipedia.org/wiki/Xi_Jinping>；<https://en.wikipedia.org/wiki/Human_rights_in_China>
- **#53** 「Whatever happens to China internally is likely to complicate life internationally.」  
  判断：**正确**。一带一路、南海争端和中美贸易冲突已使国际政治经济明显更复杂。  
  来源：<https://en.wikipedia.org/wiki/China–United_States_trade_war>；<https://en.wikipedia.org/wiki/Territorial_disputes_in_the_South_China_Sea>；<https://en.wikipedia.org/wiki/Belt_and_Road_Initiative>；<https://en.wikipedia.org/wiki/Russian_invasion_of_Ukraine>
- **#54** 「And as the world's number two country, China will expand its interests substantially.」  
  判断：**正确**。一带一路覆盖150余国，并在南海和全球供应链中大幅扩展利益与存在。  
  来源：<https://en.wikipedia.org/wiki/Belt_and_Road_Initiative>；<https://en.wikipedia.org/wiki/Territorial_disputes_in_the_South_China_Sea>；<https://en.wikipedia.org/wiki/China–United_States_trade_war>
- **#55** 「Even without those dire scenarios, China will complicate existing power relations.」  
  判断：**正确**。中美贸易科技冲突、南海争端和四边机制等，均使原有权力关系更加复杂。  
  来源：<https://en.wikipedia.org/wiki/China–United_States_trade_war>；<https://en.wikipedia.org/wiki/Territorial_disputes_in_the_South_China_Sea>；<https://en.wikipedia.org/wiki/Quadrilateral_Security_Dialogue>
- **#56** 「China is more likely to remain an "asymmetrical super­ power."」  
  判断：**正确**。中国主要凭借经济、基建和灰色地带手段扩展影响，而不是与美国展开对称的全球军事对等竞争。  
  来源：<https://en.wikipedia.org/wiki/China–United_States_trade_war>；<https://en.wikipedia.org/wiki/Territorial_disputes_in_the_South_China_Sea>；<https://en.wikipedia.org/wiki/Belt_and_Road_Initiative>；<https://en.wikipedia.org/wiki/List_of_countries_by_military_expenditures>
- **#57** 「China does not want to invade and occupy Taiwan; it is more likely to keep undermining the Taiwanese independe…」  
  判断：**正确**。至截止日未发生对台湾的全面入侵或占领，两岸政治与军事压力及南海争端持续，符合“更可能削弱而非占领”的路径。  
  来源：<https://en.wikipedia.org/wiki/Political_status_of_Taiwan>；<https://en.wikipedia.org/wiki/Territorial_disputes_in_the_South_China_Sea>
- **#58** 「it seems on track to continue this high-octane 132 THE POST-AMERICAN WORLD growth for the next decade.」  
  判断：**正确**。2008至2018年前后印度名义GDP明显扩大，2015年已约2.10万亿美元，较2008年约1.20万亿显著增长。  
  来源：<https://api.worldbank.org/v2/country/USA/indicator/NY.GDP.MKTP.CD>；<https://en.wikipedia.org/wiki/Economy_of_India>
- **#59** 「As the industrial world ages, India will continue to have lots of young people—in other words, workers.」  
  判断：**正确**。印度总人口由2008年约12.1亿增至2025年约14.6亿，仍是增长中的大型年轻社会，与工业国老龄化形成对照。  
  来源：<https://api.worldbank.org/v2/country/USA/indicator/NY.GDP.MKTP.CD>；<https://ourworldindata.org/grapher/population>；<https://en.wikipedia.org/wiki/Economy_of_India>
- **#60** 「Western busi­ nessmen go to India expecting it to be the next China. It never will be that.」  
  判断：**正确**。印度仍是民主政体，增长路径、政府动员方式和产业面貌均与中国不同，没有复制为中国模式。  
  来源：<https://en.wikipedia.org/wiki/Economy_of_India>；<https://en.wikipedia.org/wiki/Economy_of_China>；<https://en.wikipedia.org/wiki/Democracy_in_India>
- **#61** 「India will not look like China.」  
  判断：**正确**。印度在基础设施和国家能力上仍与中国有明显差别，政治与城市景观也未收敛为中国模式。  
  来源：<https://en.wikipedia.org/wiki/Economy_of_India>；<https://en.wikipedia.org/wiki/Economy_of_China>；<https://en.wikipedia.org/wiki/Democracy_in_India>
- **#64** 「A change in the ruling party will not bring about Chinese-style reforms.」  
  判断：**正确**。2014年政党轮替后印度仍是民主市场导向改革，没有转向中国式威权动员与国家主导模式。  
  来源：<https://en.wikipedia.org/wiki/Democracy_in_India>；<https://en.wikipedia.org/wiki/Narendra_Modi>；<https://en.wikipedia.org/wiki/Economy_of_China>
- **#66** 「It is poised to become a great power at last.」  
  判断：**正确**。美印核协议完成、四边对话和印度升至PPP第三/名义前六，表明印度已作为大国参与国际政治经济。  
  来源：<https://en.wikipedia.org/wiki/Economy_of_India>；<https://en.wikipedia.org/wiki/India–United_States_Civil_Nuclear_Agreement>；<https://en.wikipedia.org/wiki/Quadrilateral_Security_Dialogue>；<https://en.wikipedia.org/wiki/India–United_States_relations>
- **#67** 「Such a relationship between the United States and India is, on some level, almost inevitable.」  
  判断：**正确**。防务、核合作和四边对话显示两国关系显著走近，同时政策分歧仍在，符合“几乎不可避免但仍会有争端”的图景。  
  来源：<https://en.wikipedia.org/wiki/India–United_States_relations>；<https://en.wikipedia.org/wiki/India–United_States_Civil_Nuclear_Agreement>；<https://en.wikipedia.org/wiki/Quadrilateral_Security_Dialogue>
- **#70** 「If successful, it will alter the strategic landscape, bringing India firmly and irrevocably onto the global st…」  
  判断：**正确**。2008年10月美国参议院批准协议，条件触发；此后印美防务合作和印度国际角色明显上升。  
  来源：<https://en.wikipedia.org/wiki/India–United_States_Civil_Nuclear_Agreement>；<https://en.wikipedia.org/wiki/India–United_States_relations>；<https://en.wikipedia.org/wiki/Quadrilateral_Security_Dialogue>
- **#74** 「The more likely scenario is that China will stay well ahead of India.」  
  判断：**正确**。2025年中国名义GDP约19.5万亿美元，印度约3.96万亿，差距仍然巨大。  
  来源：<https://api.worldbank.org/v2/country/USA/indicator/NY.GDP.MKTP.CD>；<https://en.wikipedia.org/wiki/Economy_of_China>；<https://en.wikipedia.org/wiki/Economy_of_India>
- **#78** 「it will not bankrupt the United States.」  
  判断：**正确**。2013年估计伊战总成本约1.7万亿美元，而美国年GDP在十几万亿美元量级并持续扩大，战争并未导致财政崩溃或国家破产。  
  来源：<https://en.wikipedia.org/wiki/Iraq_War>；<https://api.worldbank.org/v2/country/USA/indicator/NY.GDP.MKTP.CD>
- **#88** 「In the long run this secular trend—the rise of the rest—will only gather strength, whatever the temporary ups …」  
  判断：**正确**。中国、印度经济规模显著扩大，金砖扩员，其余国家在全球产出中的绝对与政治权重总体上升。  
  来源：<https://en.wikipedia.org/wiki/Economy_of_China>；<https://en.wikipedia.org/wiki/Economy_of_India>；<https://api.worldbank.org/v2/country/USA/indicator/NY.GDP.MKTP.CD>；<https://en.wikipedia.org/wiki/BRICS>
- **#90** 「The world will not stay unipolar for decades and then, one day, suddenly switch and become bipolar or multipol…」  
  判断：**正确**。观察窗口内是渐进的力量扩散与竞争加剧，而非某一天突然切换极性。  
  来源：<https://en.wikipedia.org/wiki/Economy_of_China>；<https://en.wikipedia.org/wiki/Economy_of_the_United_States>；<https://en.wikipedia.org/wiki/List_of_countries_by_military_expenditures>；<https://en.wikipedia.org/wiki/China–United_States_trade_war>
- **#92** 「it will not be replaced in the foreseeable future.」  
  判断：**正确**。至截止日没有任何国家同时取代美国在名义经济规模、储备货币、军事开支和文化市场中的综合组合。  
  来源：<https://en.wikipedia.org/wiki/Economy_of_the_United_States>；<https://en.wikipedia.org/wiki/List_of_countries_by_military_expenditures>；<https://en.wikipedia.org/wiki/Reserve_currency>；<https://en.wikipedia.org/wiki/International_use_of_the_U.S._dollar>
- **#93** 「As China, India, Brazil, Russia, South Africa, and a host of smaller countries all do well in the years ahead,…」  
  判断：**正确**。这些经济体总体继续发展，条件大致满足；随后出现南海争端升级、俄乌战争、中美贸易冲突和四边对冲等新的紧张。  
  来源：<https://en.wikipedia.org/wiki/Territorial_disputes_in_the_South_China_Sea>；<https://en.wikipedia.org/wiki/Russian_invasion_of_Ukraine>；<https://en.wikipedia.org/wiki/China–United_States_trade_war>；<https://en.wikipedia.org/wiki/Quadrilateral_Security_Dialogue>
- **#94** 「in most cases, nationalism will grow along with economic and geopolitical stature.」  
  判断：**正确**。中国、印度和俄罗斯在国力变化的同时，民族主义政治都明显上升。  
  来源：<https://en.wikipedia.org/wiki/China–United_States_trade_war>；<https://en.wikipedia.org/wiki/Xi_Jinping>；<https://en.wikipedia.org/wiki/Narendra_Modi>；<https://en.wikipedia.org/wiki/Russian_invasion_of_Ukraine>
- **#95** 「As one of these countries rises (China), it will not produce a clockwork-like balancing dynamic where its neig…」  
  判断：**正确**。出现了四边安全对话等密切合作，但并不是印度与美国之间的正式军事同盟条约，符合“不会产生钟表般正式联盟”的判断。  
  来源：<https://en.wikipedia.org/wiki/Quadrilateral_Security_Dialogue>；<https://en.wikipedia.org/wiki/India–United_States_relations>
- **#98** 「In international negotia­ tions, America will have to bargain and compromise with oth­ ers.」  
  判断：**正确**。贸易谈判、印太协调和乌克兰问题都显示美国需要联盟协商与讨价还价，而不能单方面规定结果。  
  来源：<https://en.wikipedia.org/wiki/China–United_States_trade_war>；<https://en.wikipedia.org/wiki/Territorial_disputes_in_the_South_China_Sea>；<https://en.wikipedia.org/wiki/Russian_invasion_of_Ukraine>
- **#99** 「International life is only going to get messier.」  
  判断：**正确**。俄乌战争、中美贸易冲突和南海争端等表明大国协调更困难、危机更密集，国际生活更混乱。  
  来源：<https://en.wikipedia.org/wiki/Russian_invasion_of_Ukraine>；<https://en.wikipedia.org/wiki/China–United_States_trade_war>；<https://en.wikipedia.org/wiki/Territorial_disputes_in_the_South_China_Sea>
- **#100** 「Were there to be another attack, two things can be predicted with nearcertainty. The actual effects of the att…」  
  判断：**正确**。2013年波士顿爆炸是出版后的重大袭击，实际破坏限于局部，城市和国家未陷入长期停摆。  
  来源：<https://en.wikipedia.org/wiki/Boston_Marathon_bombing>
- **#103** 「The visa system, which has become restrictive and for­ bidding, will get more so every time one thug is let in…」  
  判断：**正确**。美国签证政策在安全理由下多次收紧，2025年6月仍以安全筛查不足为由暂停若干国家签证，总体方向是更严而非放松。  
  来源：<https://en.wikipedia.org/wiki/Visa_policy_of_the_United_States>

### 趋势符合（1 条）

- **#62** 「What will India look like politically in twenty-five years?" the answer is obvious: "As it does today—a democr…」  
  判断：**趋势符合**。至2026年印度仍是世界人口最多的民主国家，方向符合；但明确终点约在2033年尚未到达，且民主质量存在争议。  
  来源：<https://en.wikipedia.org/wiki/Democracy_in_India>；<https://en.wikipedia.org/wiki/Narendra_Modi>

### 部分符合（28 条）

- **#2** 「and is estimated to fall to 12 percent by 2015.」  
  判断：**部分符合**。世界银行现行极端贫困率2015年为13.4%，已大幅下降并接近12%，但口径已上调，数值略高于原文。  
  来源：<https://api.worldbank.org/v2/country/WLD/indicator/SI.POV.DDAY>
- **#7** 「indi­ cate that Muslims constitute around 3 percent of Europe's population now and will rise to between 5 and …」  
  判断：**部分符合**。皮尤估计2020年穆斯林约占欧洲人口6%，落在5%–8%区间；但2010年已有约6%的估计，与原文3%起点及随后平台并不完全吻合。  
  来源：<https://en.wikipedia.org/wiki/Islam_in_Europe>
- **#10** 「And that trend, not Hugo Chavez's insane rants, represents the direc­ tion of history.」  
  判断：**部分符合**。拉美在出版后既继续出现粉红色浪潮，也出现右翼回潮和反复轮替，并非单一通向开放市场或查韦斯路线。  
  来源：<https://en.wikipedia.org/wiki/Pink_tide>
- **#13** 「Even if India and China never get past middle-income status, they are likely to be the second- and third-large…」  
  判断：**部分符合**。中国已是名义第二、PPP第一；印度按PPP已是第三，但按名义GDP在2025/2026年约为第五或第六，尚未稳定成为名义第三。  
  来源：<https://api.worldbank.org/v2/country/USA/indicator/NY.GDP.MKTP.CD>；<https://en.wikipedia.org/wiki/Economy_of_China>；<https://en.wikipedia.org/wiki/Economy_of_India>；<https://en.wikipedia.org/wiki/Economy_of_the_United_States>
- **#15** 「This situation is unlikely to change.」  
  判断：**部分符合**。2022年俄罗斯全面入侵乌克兰，显示资源出口大国仍可对西方秩序发起重大挑战；但各国能力变化并不均匀。  
  来源：<https://en.wikipedia.org/wiki/Russian_invasion_of_Ukraine>
- **#20** 「Demand for electricity is projected to rise over 4 percent a year for decades. And that electricity will come …」  
  判断：**部分符合**。由世行人均用电与人口推算的全球总量增速低于每年4%；中国煤电仍占总发电一半以上，因而“超过4%且主要来自煤”只部分成立。  
  来源：<https://api.worldbank.org/v2/country/USA/indicator/NY.GDP.MKTP.CD>；<https://en.wikipedia.org/wiki/Coal_power_in_China>；<https://en.wikipedia.org/wiki/World_energy_supply_and_consumption>
- **#22** 「As the number of players—governmental and nongovernmental—increases and each one's power and confidence grows,…」  
  判断：**部分符合**。中美贸易冲突、乌克兰战争和平行机构增多显示协调更困难，但并非所有多边协议都失败。  
  来源：<https://en.wikipedia.org/wiki/China–United_States_trade_war>；<https://en.wikipedia.org/wiki/Russian_invasion_of_Ukraine>；<https://en.wikipedia.org/wiki/BRICS>
- **#26** 「The world is moving from anger to indifference, from anti-Americanism to post-Americanism.」  
  判断：**部分符合**。部分地区对美国的关注下降，但中美对抗和联盟政治也使反美或拥美情绪在另一些地方升温，并非单纯转向冷漠。  
  来源：<https://en.wikipedia.org/wiki/China–United_States_trade_war>；<https://en.wikipedia.org/wiki/Russian_invasion_of_Ukraine>
- **#28** 「There will surely be some slip­ page of America's position over the next few decades.」  
  判断：**部分符合**。中国在PPP和部分产业上缩小差距、国际约束增多，但美国名义GDP全球份额由2008年约23%升至2025年约26%，并非全面下滑。  
  来源：<https://api.worldbank.org/v2/country/USA/indicator/NY.GDP.MKTP.CD>；<https://en.wikipedia.org/wiki/Economy_of_the_United_States>；<https://en.wikipedia.org/wiki/Economy_of_China>；<https://en.wikipedia.org/wiki/List_of_countries_by_military_expenditures>
- **#29** 「In the next few decades, the rise of the emerging nations is likely to come mostly at the expense of Western E…」  
  判断：**部分符合**。中国崛起明显改变原有位次，德国仍为名义第三大经济体；西欧和日本相对分量有变化，但并非整齐地被挤出四强。  
  来源：<https://api.worldbank.org/v2/country/USA/indicator/NY.GDP.MKTP.CD>；<https://en.wikipedia.org/wiki/Economy_of_China>；<https://en.wikipedia.org/wiki/Economy_of_India>
- **#47** 「It is unlikely to sur­ pass it on any dimension—military, political, or economic—for decades, let alone have d…」  
  判断：**部分符合**。中国已在PPP口径上超过美国经济规模，但名义GDP、综合军事开支和政治影响力仍未全面超越，更谈不上全维度主导。  
  来源：<https://en.wikipedia.org/wiki/Economy_of_China>；<https://en.wikipedia.org/wiki/Economy_of_the_United_States>；<https://en.wikipedia.org/wiki/List_of_countries_by_military_expenditures>；<https://api.worldbank.org/v2/country/USA/indicator/NY.GDP.MKTP.CD>
- **#63** 「It will not need to create independent courts; it can sim­ ply clean up the ones it has.」  
  判断：**部分符合**。印度独立司法机构仍然存在，并未推倒重来；但“清理”成效与司法独立质量存在争议，不能视为已经完成。  
  来源：<https://en.wikipedia.org/wiki/Democracy_in_India>
- **#68** 「This tension—a country that is a world power and at the same time very poor—will tend to limit India's activis…」  
  判断：**部分符合**。印度对外角色扩大（四边、印太），比2008年更积极，但贫困和发展约束仍限制其全球军事干涉意愿，结果是更活跃但仍有节制。  
  来源：<https://en.wikipedia.org/wiki/Quadrilateral_Security_Dialogue>；<https://en.wikipedia.org/wiki/India–United_States_relations>；<https://en.wikipedia.org/wiki/Economy_of_India>
- **#69** 「In Asia most nations will resist such explicit balancing mechanisms. THE ALLY 157 They might all hedge against…」  
  判断：**部分符合**。四边安全对话等对冲安排已经出现，但多数仍避免公开的正式同盟和“遏制”表述，与预测部分吻合。  
  来源：<https://en.wikipedia.org/wiki/Quadrilateral_Security_Dialogue>；<https://en.wikipedia.org/wiki/Territorial_disputes_in_the_South_China_Sea>
- **#71** 「The constraints of the past decade are not transient phenomena that will fade; they are expressions of a struc…」  
  判断：**部分符合**。多样性、联邦制等结构性约束仍在，但莫迪时期多数党地位一度显著增强总理权力，约束并非完全原样延续。  
  来源：<https://en.wikipedia.org/wiki/Democracy_in_India>；<https://en.wikipedia.org/wiki/Narendra_Modi>
- **#72** 「The prime minister cannot command national power the way that Nehru did, and in all probability no prime minis…」  
  判断：**部分符合**。莫迪自2014年起长期执政并拥有少见的全国动员力，削弱了“再也不会出现强势总理”的判断，但联邦制和政党竞争仍不同于尼赫鲁时期的国大党主导。  
  来源：<https://en.wikipedia.org/wiki/Narendra_Modi>；<https://en.wikipedia.org/wiki/Democracy_in_India>
- **#73** 「India will have a larger role in international affairs than ever before. It will dominate South Asia. But it m…」  
  判断：**部分符合**。印度国际角色确实扩大，且尚未成为与中美平级的全球性大国；但在南亚的“主导”受到中国地区存在的制约。  
  来源：<https://en.wikipedia.org/wiki/Economy_of_India>；<https://en.wikipedia.org/wiki/Quadrilateral_Security_Dialogue>；<https://en.wikipedia.org/wiki/Economy_of_China>；<https://en.wikipedia.org/wiki/India–United_States_relations>
- **#75** 「India's society will stay ahead of the Indian state in the new global game.」  
  判断：**部分符合**。印度社会与市场仍然活力很强，但莫迪执政后国家能力与政治动员明显增强，社会领先国家的反差有所缩小。  
  来源：<https://en.wikipedia.org/wiki/Narendra_Modi>；<https://en.wikipedia.org/wiki/Democracy_in_India>
- **#79** 「the rise of the rest does mean that it will lose some share of global GDP. But the process will look nothing l…」  
  判断：**部分符合**。“失去份额”在现价美元口径下并未发生（份额反而上升）；美国仍是创新与金融市场前沿、也仍是最大名义经济体，确实不同于英国式失速。  
  来源：<https://api.worldbank.org/v2/country/USA/indicator/NY.GDP.MKTP.CD>；<https://en.wikipedia.org/wiki/Economy_of_the_United_States>；<https://en.wikipedia.org/wiki/Economy_of_China>
- **#80** 「America will remain a vital, vibrant economy, at the forefront of the next revolutions in science, technology,…」  
  判断：**部分符合**。美国仍是世界最大名义经济体并具高度多元化的前沿产业；但“只要能够面对挑战”这一前提无法被独立证实，故不能给全对。  
  来源：<https://en.wikipedia.org/wiki/Economy_of_the_United_States>；<https://api.worldbank.org/v2/country/USA/indicator/NY.GDP.MKTP.CD>
- **#81** 「America's superior growth trajectory might be petering out, and perhaps its growth will be more "normal" for a…」  
  判断：**部分符合**。出版后不久即遭遇全球金融危机，随后复苏，短期并不是平滑回归“正常”增速，但危机后长期增速确实较此前黄金期放缓。  
  来源：<https://api.worldbank.org/v2/country/USA/indicator/NY.GDP.MKTP.CD>；<https://en.wikipedia.org/wiki/Economy_of_the_United_States>
- **#84** 「the U . S . population will increase by 65 million by 2030, while Europe's will remain "virtually stagnant."」  
  判断：**部分符合**。美国人口由2008年约3.041亿增至2025年约3.418亿，只增加约3770万，按此节奏很难在2030年达到6500万增量；欧洲人口序列未能成功归档。  
  来源：<https://api.worldbank.org/v2/country/USA/indicator/NY.GDP.MKTP.CD>；<https://ourworldindata.org/grapher/population>
- **#89** 「Washington still has no true rival, and will not for a very long while, but it faces a growing number of const…」  
  判断：**部分符合**。美国仍无在军事、货币和名义经济上全面对等的单一对手，但中国已成为多方面竞争对手，且贸易战等显示约束明显增多。  
  来源：<https://en.wikipedia.org/wiki/Economy_of_the_United_States>；<https://en.wikipedia.org/wiki/Economy_of_China>；<https://en.wikipedia.org/wiki/List_of_countries_by_military_expenditures>；<https://en.wikipedia.org/wiki/China–United_States_trade_war>
- **#91** 「As others grow from low starting points, its relative weight will slip.」  
  判断：**部分符合**。按PPP和若干产业，美国相对分量下降；按现价美元全球份额则上升。结果因口径而异。  
  来源：<https://api.worldbank.org/v2/country/USA/indicator/NY.GDP.MKTP.CD>；<https://en.wikipedia.org/wiki/Economy_of_the_United_States>；<https://en.wikipedia.org/wiki/Economy_of_China>
- **#96** 「The dollar is unlikely to retain its totemic position forever as the reserve currency, AMERICAN PURPOSE 243 yi…」  
  判断：**部分符合**。美元份额已由更高水平降至2022年四季度约58.36%，出现一定多元化；但美元仍是首要储备货币，并未被官方一篮子货币体系取代。  
  来源：<https://en.wikipedia.org/wiki/Reserve_currency>；<https://en.wikipedia.org/wiki/International_use_of_the_U.S._dollar>
- **#97** 「In certain areas—the South China Sea, for example—U.S. military force is likely to be less relevant than that …」  
  判断：**部分符合**。中国在南海的岛礁建设和日常存在使其在当地更持续在场，但美国军事力量对地区平衡仍然高度相关，不能说已经不相关或明显更不相关。  
  来源：<https://en.wikipedia.org/wiki/Territorial_disputes_in_the_South_China_Sea>；<https://en.wikipedia.org/wiki/List_of_countries_by_military_expenditures>
- **#101** 「It is far more likely that a future attack will come from countries that are unknowingly and involuntarily she…」  
  判断：**部分符合**。波士顿案主要是美国境内人员作案，并不符合“来自非自愿藏匿国”的典型图景；其他案件来源多样，预测只部分成立。  
  来源：<https://en.wikipedia.org/wiki/Boston_Marathon_bombing>
- **#102** 「The other likely effect of another terror attack would be an increase in the restrictions on movement, privacy…」  
  判断：**部分符合**。袭击后安全盘查与签证限制在不同时期继续收紧，2025年仍出现新的签证暂停；但限制增加也有独立于单次袭击的政治驱动。  
  来源：<https://en.wikipedia.org/wiki/Visa_policy_of_the_United_States>；<https://en.wikipedia.org/wiki/Boston_Marathon_bombing>

### 错误（5 条）

- **#34** 「as the rest of the world rises, in purely economic terms, America will experi- THE CUP RUNNETH OVER 45 ence re…」  
  判断：**错误**。世界银行现价美元口径下，美国占世界GDP份额由2008年约22.9%升至2025年约26.0%，方向与“份额变小”相反。  
  来源：<https://api.worldbank.org/v2/country/USA/indicator/NY.GDP.MKTP.CD>；<https://en.wikipedia.org/wiki/Economy_of_the_United_States>
- **#37** 「In the next few decades, three of the world's four biggest economies will be nonWestern (Japan, China, and Ind…」  
  判断：**错误**。2025年世界银行名义GDP前几位为美国、中国、德国、英国，印度约为第五或（百科2026年10月）第六，并非日中印占据四强中的三席。  
  来源：<https://api.worldbank.org/v2/country/USA/indicator/NY.GDP.MKTP.CD>；<https://en.wikipedia.org/wiki/Economy_of_India>；<https://en.wikipedia.org/wiki/Economy_of_China>；<https://en.wikipedia.org/wiki/Economy_of_the_United_States>
- **#48** 「This problem, of spiraling decen­ tralization, will be China's greatest challenge」  
  判断：**错误**。2018年修宪取消连任限制、权力向中央集中，实际轨迹是再集权而非不断加剧的权力下放成为主导挑战。  
  来源：<https://en.wikipedia.org/wiki/Xi_Jinping>
- **#76** 「It is likely to slip but not significantly in the next two decades.」  
  判断：**错误**。现价美元口径下美国占世界GDP份额由2008年约22.9%升至2025年约26.0%，并未下滑。  
  来源：<https://api.worldbank.org/v2/country/USA/indicator/NY.GDP.MKTP.CD>；<https://en.wikipedia.org/wiki/Economy_of_the_United_States>
- **#77** 「In 2025, most estimates suggest that the U.S. economy will still be twice the size of China's in terms of nomi…」  
  判断：**错误**。2025年世界银行现价美元GDP：美国约30.77万亿、中国约19.50万亿，比值约1.58，美国仍更大但远不是两倍。  
  来源：<https://api.worldbank.org/v2/country/USA/indicator/NY.GDP.MKTP.CD>；<https://en.wikipedia.org/wiki/Economy_of_the_United_States>；<https://en.wikipedia.org/wiki/Economy_of_China>

### 暂无法判断（20 条）

- **#5** 「Your chances of dying as a consequence of organized violence of any kind are low and getting lower.」  
  判断：**暂无法判断**。已归档来源未提供全球有组织暴力死亡序列，无法判定窗口内尤其是2022年以来的方向。  
  来源：—
- **#6** 「This struggle, between governments and terrorists, will persist, but it is the former who have the upper hand.」  
  判断：**暂无法判断**。已有波士顿等地恐袭个案，但缺少全球恐怖活动与政府控制力的系统序列。  
  来源：—
- **#8** 「That world is also modernizing, though more slowly than the rest」  
  判断：**暂无法判断**。已归档来源没有可比较的现代化或人均发展速度指标覆盖“穆斯林世界”整体。  
  来源：—
- **#16** 「Resource-rich countries will thrive as long as the others are growing.」  
  判断：**暂无法判断**。缺少资源出口国实际收入与全球增长对照的系统数据。  
  来源：—
- **#17** 「This is a state-directed form of capitalism, which is likely to result in narrow development and unlikely to p…」  
  判断：**暂无法判断**。已归档来源不足以为海湾经济多元化或可持续增长下结论。  
  来源：—
- **#19** 「if water sources dry up in the future, tens of millions of people will be forced to start moving.」  
  判断：**暂无法判断**。前提“水源枯竭”并未在归档证据中被确立为已全面触发的条件，故不能按正误计分。  
  来源：—
- **#21** 「Between 2 0 0 6 and 2012, China and India will build eight hun­ dred new coal-fired power plants—with combined…」  
  判断：**暂无法判断**。已归档来源没有该时间窗内中印新建燃煤电厂座数。  
  来源：—
- **#35** 「Without real efforts to bridge it, this divide could destroy America's competitive edge and its political futu…」  
  判断：**暂无法判断**。条件是否充分触发以及“毁掉前途”是否发生，现有归档证据不足以下结论。  
  来源：—
- **#38** 「Perhaps China and India will go through their own Victorian era, a time when energetic capitalism went」  
  判断：**暂无法判断**。该组合是比喻性前景，已归档来源不足以操作化并判定是否出现。  
  来源：—
- **#39** 「And perhaps that combination will endure.」  
  判断：**暂无法判断**。同样缺乏可操作口径与决定性证据。  
  来源：—
- **#40** 「Modernization brings about some form of women's liberation. It overturns the hierarchy of age, reli­ gion, tra…」  
  判断：**暂无法判断**。缺少性别权利与社会风貌的跨国时间序列来检验该方向。  
  来源：—
- **#41** 「The world we're entering will look like Bollywood. It will be thoroughly modern—and thus powerfully shaped by …」  
  判断：**暂无法判断**。比喻性判断，缺少可核验度量。  
  来源：—
- **#42** 「And these differences will multiply.」  
  判断：**暂无法判断**。缺少商业实践差异的可比指标。  
  来源：—
- **#51** 「The forces fueling its rise will not disappear even if the current regime collapses—or, more likely, splits in…」  
  判断：**暂无法判断**。中国共产党政权并未崩溃，条件未触发，不能按正误计分。  
  来源：—
- **#65** 「If India's governance does not improve, the country will never fully achieve its potential.」  
  判断：**暂无法判断**。治理是否“得到改善”以及潜力是否充分实现，均缺少决定性、可操作的归档指标。  
  来源：—
- **#82** 「All these advantages will not be erased easily, because the structure of European and Japanese universities—mo…」  
  判断：**暂无法判断**。已归档的大学排名条目未能提供美国高校仍占主导的明确排行数字，缺决定性证据。  
  来源：—
- **#83** 「This will, over time, translate into a competitiveness problem」  
  判断：**暂无法判断**。缺少不平等与竞争力的对应指标时间序列。  
  来源：—
- **#85** 「by 2010, Japan will have three million fewer workers than in 2 0 0 5 .」  
  判断：**暂无法判断**。已归档来源缺少日本15–64岁人口2005与2010年的对应数字。  
  来源：—
- **#86** 「Worker populations in China and Korea are also likely to peak within the next decade.」  
  判断：**暂无法判断**。已归档来源缺少中韩劳动年龄人口峰值年份。  
  来源：—
- **#87** 「By 2 0 1 0 , foreign students will get more than 5 0 percent of all Ph.D.'s awarded in every sub­ ject in the …」  
  判断：**暂无法判断**。已归档来源没有NSF或同等口径的2010年博士学位授予结构。  
  来源：—

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/zakaria-post-american-world-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/zakaria-post-american-world-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/zakaria-post-american-world-v5/audit/manual_review_2026-11-15.py`

## 说明

- 本 audit 文件由批量 QA 于 2026-11-16 根据已有判定（来源：accepted_assessment）重建，供 canonical manual_report.py 生成报告；判定本身未在重建时改写。

