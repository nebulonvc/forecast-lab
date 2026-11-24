# 兹比格涅夫·布热津斯基（Zbigniew Brzezinski）《战略远见》：出版后预测人工核查

- 案例目录：`cases/brzezinski-strategic-vision-v5/`
- 出版日期：**2012-01-24**。Basic Books 2012年1月24日初版（Strategic Vision: America and the Crisis of Global Power），电子版 ISBN 9780465029556。所用 PDF 为塔吉克斯坦国立大学网站所载英文电子版，共433页，含引言、四部分、结论、注释、索引（注释自PDF第340页起）。正文为 reading-library/2026-11-15-未来判断书单/01-地缘政治/补-战略远见.pdf，sha256 0edf86ae3fbeef05f9cb3b1570c22638f0e117c7746cf4818d8b91f03718402e（与 catalog.json 一致）。引文逐字取自 pdftotext 25.03.0 按页抽取的文字层，位置记为 PDF 页码与页内字符偏移；未把全文文本加入仓库。窗口为2012-01→2026-11-15。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

本稿按 METHOD.md 复刻仓库 DeepSeek 管线、仅以人工阅读替代模型调用：先对源文做 prepare_book v5 分块并逐块抽取，再经仓库代码对齐、去重后导入 data/claims.jsonl；核验时每条先写 scope，用 Exa 检索公开来源并抓取存档（data/sources/，sha256 记于 data/evidence.jsonl），再由助手按四分类规则评断，经 pipeline.py apply assess → check → report。本稿由助手逐条对照书中原文与存档证据人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 32 条，剔除非预测 0 条，计入 **32 条预测**，其中 **31 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 19 |
| 趋势符合 | 2 |
| 部分符合 | 3 |
| 错误 | 7 |
| 暂无法判断 | 1 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **61.3%**（19/31） |
| 加权胜率 | **71.0%** |
| 错误率 | **22.6%**（7/31） |
| 未定占比（暂无法判断/预测） | 3.1%（1/32） |

## 总体评价

布热津斯基2012年对美国仍具塑造力、中国人均不会接近美国、阿富汗撤军后改革难持久、基辅不会自愿屈服莫斯科、中国2030年前难成宪政民主等判断，在2012–2026窗口内大多成立。主要落空的是土耳其入盟、土耳其民主巩固、更富裕的中国更倾向民主主流、战略公域将出现公平管理安排，以及中国领导层会对崛起时间表保持低调。一条关于西俄达成约束性合作安排的条件句因前提未触发记暂无法判断。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（19 条）

- **#1** 「this book will argue that America’s role in the world will continue to be essential in the years to come.」  
  判断：**正确**。出版后美国仍是军费第一、北约与援乌联盟核心，全球作用未被取代  
  来源：<https://en.wikipedia.org/wiki/List_of_countries_by_military_expenditures>
- **#2** 「Regional flare-ups among them are more likely to occur within the Asia-Pacific region itself.」  
  判断：**正确**。2020加勒万中印冲突、南海争端均在亚太内部发生  
  来源：<https://en.wikipedia.org/wiki/2020%E2%80%932021_China%E2%80%93India_skirmishes>；<https://en.wikipedia.org/wiki/Philippines_v._China>
- **#3** 「is unlikely to be able to replace America’s once-compelling attraction or fill its global role」  
  判断：**正确**。欧盟未取代美国的吸引力与全球角色，美国仍居主导  
  来源：<https://en.wikipedia.org/wiki/List_of_countries_by_military_expenditures>；<https://en.wikipedia.org/wiki/Economy_of_China>
- **#4** 「In a world where systemic rivalry between the United States and China is likely to intensify」  
  判断：**正确**。2018年起贸易战、科技与南海对抗显示竞争显著加剧  
  来源：<https://en.wikipedia.org/wiki/China%E2%80%93United_States_trade_war>；<https://en.wikipedia.org/wiki/Philippines_v._China>
- **#6** 「But neither China nor India will come even close to US levels in per capita GDP」  
  判断：**正确**。2024人均GDP(PPP)美国75,698远高于中国23,841、印度9,416  
  来源：<https://ourworldindata.org/grapher/gdp-per-capita-worldbank>
- **#7** 「modernizing reforms hastily introduced under foreign duress and in conflict with centuries of tradition rooted…」  
  判断：**正确**。2021美军撤离后塔利班迅速夺权、改革逆转，条件触发且结果吻合  
  来源：<https://en.wikipedia.org/wiki/Fall_of_Kabul_(2021)>
- **#8** 「No single power will be ready by then to exercise the role」  
  判断：**正确**。至2025无任何单一大国取代美国角色  
  来源：<https://en.wikipedia.org/wiki/List_of_countries_by_military_expenditures>
- **#10** 「China’s preoccupation with its internal stability is thus likely to increase.」  
  判断：**正确**。建成全球最大监控体系、维稳投入扩大，关注明显上升  
  来源：<https://en.wikipedia.org/wiki/Mass_surveillance_in_China>
- **#12** 「Hence it is likely that the Kremlin will continue to press Ukraine to join a “common economic space” with Russ…」  
  判断：**正确**。2013施压拒签欧盟协议、2014及2022武力干预，施压持续升级  
  来源：<https://en.wikipedia.org/wiki/Euromaidan>；<https://en.wikipedia.org/wiki/Russian_invasion_of_Ukraine>
- **#13** 「At the same time, quiet efforts will go on to infiltrate the Ukrainian security services and military command」  
  判断：**正确**。乌方长期反渗透、查处亲俄内鬼，印证俄方持续渗透  
  来源：<https://en.wikipedia.org/wiki/Security_Service_of_Ukraine>
- **#14** 「time may not be working in favor of a voluntary submission by Kyiv to Moscow」  
  判断：**正确**。乌克兰民族认同强化、2014及2022坚决抵抗，不利于自愿臣服  
  来源：<https://en.wikipedia.org/wiki/Euromaidan>；<https://en.wikipedia.org/wiki/Russian_invasion_of_Ukraine>
- **#15** 「The most likely results of a rapid US disengagement brought on by war fatigue or the early effects of an Ameri…」  
  判断：**正确**。2021撤离后政权崩溃、周边势力介入，条件触发且吻合  
  来源：<https://en.wikipedia.org/wiki/Fall_of_Kabul_(2021)>
- **#16** 「as other nations grow their military capacities they will necessarily challenge the omnipresent position of th…」  
  判断：**正确**。解放军海军规模居全球第一，直接挑战美国海上优势  
  来源：<https://en.wikipedia.org/wiki/People%27s_Liberation_Army_Navy>
- **#19** 「The slow thawing of the Arctic will also change the face of the international competition for important resour…」  
  判断：**正确**。北方航道因融冰成为航运与资源竞争新焦点  
  来源：<https://en.wikipedia.org/wiki/Northern_Sea_Route>
- **#21** 「a percentage that will only increase as China develops the western regions of its territory」  
  判断：**正确**。全球CO2份额由2010年26.1%升至2024年32.1%，持续上升  
  来源：<https://ourworldindata.org/grapher/annual-share-of-co2-emissions>
- **#26** 「before too long that is likely to be the case (and in some respects it already may be so) with regard to its m…」  
  判断：**正确**。解放军海军成全球舰艇最多、军费全球第二，军事能力已居第二  
  来源：<https://en.wikipedia.org/wiki/People%27s_Liberation_Army_Navy>；<https://en.wikipedia.org/wiki/List_of_countries_by_military_expenditures>
- **#27** 「it has a good chance of continuing for a while, though probably at declining annual rates.」  
  判断：**正确**。经济持续增长但增速由约10%降至约5%，与预测吻合  
  来源：<https://en.wikipedia.org/wiki/Economy_of_China>
- **#28** 「In the case of China, however, public disaffection is not likely to express itself through a massive quest for…」  
  判断：**正确**。监控强化、民族主义上升而无大规模民主运动，与预测吻合  
  来源：<https://en.wikipedia.org/wiki/Mass_surveillance_in_China>；<https://en.wikipedia.org/wiki/Two_Centenaries>
- **#30** 「it is unlikely that China will experience in the relatively near future—say by 2030—what many in the West hope…」  
  判断：**正确**。至今中国未出现宪政民主且趋势相反，否定式判断成立  
  来源：<https://en.wikipedia.org/wiki/Xi_Jinping>

### 趋势符合（2 条）

- **#5** 「the foreseeable future (i.e., the next two decades) is still largely America’s to shape.」  
  判断：**趋势符合**。至2026美国仍主导，但“二十年”终点(约2032)未到，暂记趋势符合  
  来源：<https://en.wikipedia.org/wiki/List_of_countries_by_military_expenditures>
- **#9** 「China is not yet —nor will it be for several more decades—ready to assume in full scope America’s role in the …」  
  判断：**趋势符合**。至今中国未全面承接美国角色，终点在数十年后，记趋势符合  
  来源：<https://en.wikipedia.org/wiki/List_of_countries_by_military_expenditures>；<https://ourworldindata.org/grapher/gdp-per-capita-worldbank>

### 部分符合（3 条）

- **#18** 「The threat of water conflicts is likely to intensify as the economic growth and increasing demand for water in…」  
  判断：**部分符合**。2025印度暂停印度河水条约显示水资源对抗加剧，但土-伊拉克一线证据较弱  
  来源：<https://en.wikipedia.org/wiki/Indus_Waters_Treaty>
- **#20** 「the increasingly polarized domestic political environment and the truculent American economic recovery are unl…」  
  判断：**部分符合**。2022年IRA曾取得重大气候立法进展(与预测相反)，但其后出现回撤，结果混合  
  来源：<https://en.wikipedia.org/wiki/Inflation_Reduction_Act>
- **#25** 「In contemporary Asia, internal conflicts derived from ethnic diversity and pre-nation-state tribal loyalties r…」  
  判断：**部分符合**。内部族群冲突与对外领土争端(南海、边境)并存，与“更多来自内部”仅部分吻合  
  来源：<https://en.wikipedia.org/wiki/Philippines_v._China>；<https://en.wikipedia.org/wiki/2020%E2%80%932021_China%E2%80%93India_skirmishes>

### 错误（7 条）

- **#11** 「consideration is likely to incline the Chinese leadership to remain discreet regarding a timetable for China’s…」  
  判断：**错误**。习近平公开提出两个一百年(2021/2049)等明确时间表，与“保持低调”相反  
  来源：<https://en.wikipedia.org/wiki/Two_Centenaries>
- **#17** 「a fair system for allocating management responsibilities is highly likely, even in the evolving landscape of r…」  
  判断：**错误**。南海仲裁被拒、公域军事化，未形成公平分配制度  
  来源：<https://en.wikipedia.org/wiki/Philippines_v._China>
- **#22** 「a more robust Turkish democracy gradually reduces the appeal of religious fundamentalism」  
  判断：**错误**。土耳其转向威权与伊斯兰化，前提与结论均未成立  
  来源：<https://en.wikipedia.org/wiki/Recep_Tayyip_Erdo%C4%9Fan>
- **#23** 「Turkey could by then already be a full member of the EU」  
  判断：**错误**。入盟谈判停滞，土耳其远未成为成员  
  来源：<https://en.wikipedia.org/wiki/Accession_of_Turkey_to_the_European_Union>
- **#29** 「three sensitive US-Chinese issues will have to be peacefully resolved, the first of them probably in the near …」  
  判断：**错误**。抵近侦察、军备与台湾问题均未按该时间表解决，反而对抗加剧  
  来源：<https://en.wikipedia.org/wiki/Philippines_v._China>；<https://en.wikipedia.org/wiki/China%E2%80%93United_States_trade_war>
- **#31** 「an eventually modern and more prosperous China, too, will become more inclined to join the democratic mainstre…」  
  判断：**错误**。中国更趋集权与监控，未汇入民主主流  
  来源：<https://en.wikipedia.org/wiki/Xi_Jinping>；<https://en.wikipedia.org/wiki/Mass_surveillance_in_China>
- **#32** 「is likely to facilitate a more evolutionary adoption of political pluralism」  
  判断：**错误**。习近平集权、监控强化，走向与政治多元化相反  
  来源：<https://en.wikipedia.org/wiki/Xi_Jinping>；<https://en.wikipedia.org/wiki/Mass_surveillance_in_China>

### 暂无法判断（1 条）

- **#24** 「It is also reasonable to assume that in the course of the next two or more decades a genuinely cooperative and…」  
  判断：**暂无法判断**。前提(俄罗斯完成法治民主转型)未满足，2022后关系全面对抗，条件未触发无法按正误计分  
  来源：—

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/brzezinski-strategic-vision-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/brzezinski-strategic-vision-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/brzezinski-strategic-vision-v5/audit/manual_review_2026-11-15.py`

## 说明

- 本 audit 文件由批量 QA 于 2026-11-16 根据已有判定（来源：accepted_assessment）重建，供 canonical manual_report.py 生成报告；判定本身未在重建时改写。

