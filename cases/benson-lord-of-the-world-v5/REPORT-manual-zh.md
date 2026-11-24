# 罗伯特·休·本森《世界之主》（Lord of the World，1907）：出版后预测人工核查

- 案例目录：`cases/benson-lord-of-the-world-v5/`
- 出版日期：Robert Hugh Benson《Lord of the World》于 **1907** 年首次出版（前言署 CAMBRIDGE 1907）。所用文件为 Project Gutenberg #14021 的 cache/epub 纯文本（https://www.gutenberg.org/cache/epub/14021/pg14021.txt）。原文 sha256 `ce5924e44c9d50a3a4857ab9436ae7085c50b3b97885abd6f277d67e6171cc82`（605,041 字节），已与队列逐字节核对一致。观察窗口按 1907 年起算，至 2026-11-15。全书文本不入库。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

本稿按 METHOD.md 复刻 DeepSeek 流水线，只把模型调用换成助手人工阅读。抽取：用仓库 prepare_book v5（toolkit 来自 main `85e6da1`）把 TXT 全文切成 173 块（3500 字符、600 字符上下文），助手逐块通读正文，按 DISCOVER_PROMPT_V5 写出模型本应返回的 JSON（前后附文块回答为空，或只对混合块中的正文部分抽取），再由仓库代码完成引文对齐、非预测筛除和去重，得到 11 条候选，全部为可核验。核验：每条可核验候选先定 scope，用 Exa 各做一次 support/counter 检索（必要时第二轮补充），只从检索返回的 URL 中选源，存档到 `data/sources/`（sha256），写入 `data/evidence.jsonl`，再经 `pipeline.py apply assess → check → report`。本稿由助手逐条对照书中原文与存档证据人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 11 条，剔除非预测 0 条，计入 **11 条预测**，其中 **11 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 0 |
| 趋势符合 | 0 |
| 部分符合 | 1 |
| 错误 | 10 |
| 暂无法判断 | 0 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **0.0%**（0/11） |
| 加权胜率 | **4.5%** |
| 错误率 | **90.9%**（10/11） |
| 未定占比（暂无法判断/预测） | 0.0%（0/11） |

## 总体评价

这是一部 1907 年的未来史小说。队列要求只抽取具体、有时间界限的社会或技术主张，不为寓言与情节本身打分。173 块中有 11 条可核验预测，几乎都是序章及后文中带明确年份（或可还原的两位年份）的制度与立法判断。可判定的 11 条中，0 条正确，0 条趋势符合，1 条部分符合（美国 1914 年反托拉斯立法确实挤破部分垄断泡沫，但 1916–1917 年立法并未阻止其再形成），10 条错误（工党 1917 年执掌并开始共产主义、1935 年废除上院、1929 年最终废除英格兰国教会、1919 年弃用尼西亚信经、1960 年职业国有化法案、1959 年确立教条式世俗主义的教育法、1989 年接受马克思主义、1914 年法国教会大屠杀、1918 年 Gerome 披露、1998 年普遍《释放法》等均未按所述发生）。密度偏低是因为按小说口径排除了无年份的布景与寓言情节，未为提高数量而放宽标准。趋势符合按严格口径使用，本批未使用。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 部分符合（1 条）

- **#10** 「the famous old laws of 1914 had burst some of the stinking bubbles of the time; and the enactments of 1916 and…」  
  判断：**部分符合**。1914年美国确有著名的反托拉斯立法：克莱顿法与联邦贸易委员会法，用来遏制托拉斯与垄断，可以说部分“挤破了当时的泡沫”。但1916–1917年立法主要是战争筹款与战时措施（如1916年遗产税），并非使财阀泡沫无法再形成；此后1920年代财富与产业集中仍然延续，谈不上结束财阀政治。  
  来源：<https://history.house.gov/Historical-Highlights/1901-1950/hh_1914_10_15_clayton_antitrust/>；<https://archivesfoundation.org/newsletter/broken-trust/>；<https://www.encyclopedia.com/defense/energy-government-and-defense-magazines/financing-world-war-i>；<https://www.taxnotes.com/tax-history-project/tax-history-century-estate-tax-made-revenue-not-redistribution/2016/09/06/g86j>

### 错误（10 条）

- **#1** 「After the fall of the French Church at the beginning of the century and the massacres of 1914」  
  判断：**错误**。1914年法国进入的是第一次世界大战与各派（含天主教会）参与的联合（Union Sacrée），并非“法国教会衰落后的1914年大屠杀”。此前的政教分离发生在1905年，早于本书出版，不能把战争动员改写成教会崩溃后的屠杀。  
  来源：<https://bcd.bzh/becedia/en/july-august-1914-the-bretons-go-to-war>；<https://linguaromana.byu.edu/2018/09/04/war-memory-and-politics-the-case-of-the-french-clergy-in-the-first-world-war/>
- **#2** 「in 1917 the Labour party gathered up the reins, and Communism really began.」  
  判断：**错误**。1917年英国执政的是劳合·乔治战时联合政府，不是工党掌权，更没有“共产主义由此真正开始”。工党首次组阁是1924年少数政府，英国也从未建立共产主义政体。  
  来源：<https://history.blog.gov.uk/2014/01/22/whats-the-context-britains-first-labour-government-takes-office-22-january-1924/>
- **#3** 「till ’35 that the House of Lords fell for the last time」  
  判断：**错误**。1935年英国上院并未“最后一次倾覆”。议会仍有上院；1911年与1949年议会法只是削弱否决权，1999年改革去掉大多数世袭议员，但议院本身一直存续到核验截止日。1935年汉萨德记录的是改革讨论而非废除。  
  来源：<https://www.parliament.uk/business/lords/lords-history/history-of-the-lords/>；<https://www.parliament.uk/about/living-heritage/evolutionofparliament/houseoflords/parliamentacts/keydates/>；<https://api.parliament.uk/historic-hansard/lords/1935/dec/04/house-of-lords-reform>
- **#4** 「The Established Church had gone finally in ’29.」  
  判断：**错误**。英格兰国教会并未在1929年最终被废除。英国下院图书馆仍称英格兰圣公会为英格兰的国教会；威尔士国教会按1914年威尔士教会法于1920年解除国教地位，既不是1929年，也不覆盖英格兰。  
  来源：<https://commonslibrary.parliament.uk/research-briefings/cbp-8886/>；<https://en.wikipedia.org/wiki/Church_of_England>；<https://en.wikipedia.org/wiki/Welsh_Church_Act_1914>
- **#5** 「Convocation of ’19, when the Nicene Creed dropped out」  
  判断：**错误**。英格兰教会并未在1919年公会议上废除《尼西亚信经》。至核验截止日，该信经仍是英格兰教会官方信仰表述，并用于崇拜；2000年总议会还在审议并通过新的英译，说明其并未在1919年被弃用。  
  来源：<https://www.churchofengland.org/faith/what-we-believe/nicene-creed>；<https://anglicansonline.org/archive/news/articles/2000/000305a.html>
- **#6** 「the _Necessary Trades Bill_ became law in ’60」  
  判断：**错误**。1960年英国并未通过名为Necessary Trades Bill、把许多职业国有化的法律。当时仍是混合经济，1950–60年代主要是既有国有产业的调整而非全面职业国有化；同年《辅助医疗职业法》讨论的是职业规制，不是国有化。不能把战后局部国有化牵强算作命中。  
  来源：<https://commonslibrary.parliament.uk/research-briefings/cbp-8325/>；<https://api.parliament.uk/historic-hansard/lords/1960/may/30/professions-supplementary-to-medicine>
- **#7** 「the final Education Act of ’59, whereby dogmatic secularism was established」  
  判断：**错误**。1959年《教育法》的宗旨是扩大教育大臣对受助学校（aided schools）和特别协议学校的拨款、补助与贷款，实际上提高了对教会受助学校的资助比例，而不是确立“教条式世俗主义”。1944年巴特勒法所要求的宗教教育与集体崇拜框架也并未被该法废止。  
  来源：<https://www.education-uk.org/documents/acts/1959-education-act.html>；<https://en.wikipedia.org/wiki/Voluntary_aided_school>；<https://www.secularism.org.uk/opinion/2016/03/the-surprising-origin-of-collective-worship-in-schools>
- **#8** 「acceptance of Karl Marx’s doctrines in ’89--but the former came in ’77」  
  判断：**错误**。1989年英国并未接受马克思学说：当时是撒切尔执政后期，议会辩论的是东欧社会主义崩溃之后“社会主义的未来”。遗产税方面，资本转移税出自1975年财政法，遗产税改于1986年，1977年并非关键节点，更不能把它写成通向1989年接受马克思主义的步骤。  
  来源：<https://api.parliament.uk/historic-hansard/commons/1989/dec/15/future-of-socialism>；<https://www.bbc.co.uk/history/british/modern/thatcherism_01.shtml>；<https://en.wikipedia.org/wiki/Inheritance_tax_in_the_United_Kingdom>
- **#9** 「the revelations of 1918, when P. Gerome, the Dominican and ex-Mason, had made his disclosures with regard to t…」  
  判断：**错误**。检索未找到历史上名为P. Gerome的多明我会前共济会员在1918年披露Mark-Masons的非虚构记录。天主教世界中广为人知的“共济会内幕披露”是1890年代的Taxil骗局，发生在本书出版之前，不能替代这一有具体人名与年份的1918年事件。  
  来源：<https://en.wikipedia.org/wiki/Taxil_hoax>；<https://www.casebook.org/dissertations/freemasonry/anti-mason/>
- **#11** 「the passing of the Release Act in 1998」  
  判断：**错误**。1998年并不存在使安乐死“已经相当常见”的普遍《释放法》。英国当时并未将安乐死或医师协助死亡合法化；俄勒冈《尊严死亡法》是1997年的州法且范围有限，荷兰立法在2001年，都不能等同于本书英国背景下1998年的Release Act。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC2585714/>；<https://researchbriefings.files.parliament.uk/documents/LIF-2017-0019/LIF-2017-0019.pdf>；<https://publications.parliament.uk/pa/cm5804/cmselect/cmhealth/321/report.html>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/benson-lord-of-the-world-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/benson-lord-of-the-world-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/benson-lord-of-the-world-v5/audit/manual_review_2026-11-15.py`

## 说明

- 抽取密度（11 条可核验 / 173 块 ≈ 0.064）低于 METHOD §5 英文书参考区间（约 0.2—0.35）。本书是虚构未来史；只计入有明确年份的社会、政治或技术主张，未把无年份的布景（如 volor、地下住宅）、角色近前情节法案，或反基督／人道主义宗教等寓言本身计为预测。作者短序按前言排除。未为提高数量而放宽标准。
- 两位年份按序章叙事还原为二十世纪：’19=1919、’29=1929、’35=1935、’59=1959、’60=1960、’77=1977、’89=1989。
- 趋势符合按严格口径使用；本批无此类判断。
- 证据以独立第三方为主（英国议会与议会图书馆、立法文本、英格兰教会、美国国会与国家档案馆相关记述、学术与百科条目），不用本书原文作为证据。
- `data/claims.jsonl`、`output/txt_import/claims_proposals.jsonl` 及评估快照中的 `context` 字段已清空。

