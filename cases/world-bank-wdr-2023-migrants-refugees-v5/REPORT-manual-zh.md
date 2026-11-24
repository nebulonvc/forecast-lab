# 世界银行《2023年世界发展报告：移民、难民与社会》（World Development Report 2023: Migrants, Refugees, and Societies）：出版后预测人工核查

- 案例目录：`cases/world-bank-wdr-2023-migrants-refugees-v5/`
- 出版日期：World Bank，Washington DC，2023-04-26（世界银行 Documents & Reports 文件日期），CC BY 3.0 IGO。**按 2023-04-26 起算**，观察窗口约 3.5 年（2023-04-26 至 2026-11-15）。报告的人口与气候预测大多以 2030、2050、2100 年为终点。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

按仓库 DeepSeek 管线手工代替模型调用：以 `pdftotext -enc UTF-8` 生成全文 TXT（PDF sha256 `0e6b0b4d…`，与队列记录一致；TXT sha256 `65f798f9…`，1,189,180 字符），`prepare_book.split_text(3500, 600)` 得到 345 个 chunk，逐块通读，没有用关键词筛选。参考文献、图表数值和注释中的历史数据没有抽取；政策建议（规范性陈述）和一般机制不计为预测。经 `validate_chunk_predictions` 与 `claims_from_results` 导入 59 条可解析预测（全部 `claim_type=forecast`，显式时点 33 条、隐含时点 26 条，降级 0、重复 0）。引文均为 TXT 逐字片段，`changes` 不跨行。全文未入库。本稿由助手逐条对照报告原文，依据 2023-04 至 2026-11-15 窗口内可公开访问的来源人工复核（Exa 检索 40 次，结果存档于 `data/sources/`，带 sha256，共 46 条证据）：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 59 条，剔除非预测 0 条，计入 **59 条预测**，其中 **21 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 8 |
| 趋势符合 | 13 |
| 部分符合 | 0 |
| 错误 | 0 |
| 暂无法判断 | 38 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **38.1%**（8/21） |
| 加权胜率 | **84.5%** |
| 错误率 | **0.0%**（0/21） |
| 未定占比（暂无法判断/预测） | 64.4%（38/59） |

## 总体评价

这是一份以人口结构与气候变化为主线的政策报告，大量数字是 2050–2100 年的联合国人口预测或气候情景，在约 3.5 年的窗口里无法检验，所以 59 条中有 38 条记为“暂无法判断”。能在窗口内检验的 21 条没有一条被推翻：8 条正确，13 条趋势符合。正确的主要是“短期内不会改变”一类的判断与制度安排：老龄化国家出生人数继续创新低（意大利、日本），法国提高退休年龄的改革在 2025 年被暂停，支持难民的国际资金不升反降（官方发展援助 2024 年降 7.1%、2025 年降 23.1%，难民署 2025 年只拿到 33% 的所需资金），武装冲突数量 2024 年创二战后新高，跨境移民存量 2024 年达 3.04 亿；第二届全球难民论坛（2023 年 12 月）与第二届国际移民审查论坛（2026 年 5 月）都按“每四年一次”举行。趋势符合主要是方向已出现、但终点或规模未到的判断：日本、意大利、泰国、波兰等国扩大引进外劳，日本外国劳动者 2025 年达 257 万人；经合组织成员国 65 岁以上人口占比 2025 年升至 19.0%；墨西哥生育率降至 1.2；2024 年首次全年升温超过 1.5°C。需要注意的反向信号：经合组织称 2024 年流入成员国的劳动移民下降两成多，多国收紧移民政策；2025 年灾害导致的国内流离失所比 2024 年减少 35%；韩国 2025 年出生人数回升 6.7%。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（8 条）

- **#30** 「Because the demographic decline is already well advanced, it is not likely to be reversed soon, if at all.」  
  判断：**正确**。窗口内老龄化国家的人口下降没有逆转：意大利2024年出生人数369,944，比上年减2.6%，生育率创历史新低；日本2024年出生686,061人，降5.7%，为1899年有统计以来最低。韩国2025年出生人数增长6.7%、生育率回升到0.8，但仍远低于更替水平，不构成人口下降的逆转。"短期内不会逆转"在窗口内成立。  
  来源：<https://www.istat.it/en/press-release/births-and-fertility-of-the-resident-population-year-2024/>；<https://www.theguardian.com/world/2025/jun/05/japan-records-lowest-number-of-births-in-more-than-a-century-as-population-fears-grow>；<https://en.yna.co.kr/view/AEN20260826004400320>
- **#32** 「The current public opposition to reform proposals regarding the retirement age and welfare programs in many We…」  
  判断：**正确**。路透（2025年10月14日）：法国总理勒科尔尼承诺把马克龙的标志性养老金改革暂停到2027年大选之后，以换取议会支持；美联社：2025年12月9日国民议会以微弱多数通过社保预算，暂停这项提高退休年龄、不受欢迎的改革；路透评论称法国是又一个推迟养老金改革的政府，各国政府在向老年选民让步。书中"提高退休年龄的改革不会容易"得到印证。  
  来源：<https://www.reuters.com/world/europe/french-pm-lecornu-deliver-key-speech-his-fate-hangs-balance-2025-10-14/>；<https://apnews.com/article/france-pension-reform-suspended-health-care-budget-63eed2ffe11ecd9103f3954d8befd6b8>；<https://www.reuters.com/business/finance/why-europe-cant-face-its-pension-black-hole-2025-10-16/>
- **#49** 「In light of the competing demands on external financing needs—on issues such as climate change, food security,…」  
  判断：**正确**。支持难民的国际资金不但没有大幅增加，反而收缩：经合组织称官方发展援助2024年实际下降7.1%（其中人道援助下降），2025年再降23.1%，为有记录以来最大年度降幅；联合国难民署2025年只获得所需资金的33%，并因资金削减压缩援助。书中"不太可能大幅增加"成立。  
  来源：<https://www.oecd.org/en/about/news/press-releases/2025/04/official-development-assistance-2024-figures.html>；<https://www.oecd.org/en/about/news/press-releases/2026/04/international-aid-fell-sharply-in-2025-says-oecd.html>；<https://unrefugees.ch/en/news/emergency-impact-report-2025-unhcrs-global-response-displacement>
- **#50** 「Looking ahead, the priority is to strengthen aid effectiveness because the share of ODA available for refugee-…」  
  判断：**正确**。经合组织初步数据：2024年官方发展援助实际下降7.1%，其中人道援助下降13.7%，捐助国境内难民支出比2023年减少16.9%（279亿美元，占援助总额的13%）；2025年援助再降23.1%，为有记录以来最大降幅。用于难民相关项目的资金及其份额都没有大幅上升，书中判断成立。  
  来源：<https://focus2030.org/en/official-development-assistance-falls-in-2024/>；<https://www.oecd.org/en/about/news/press-releases/2025/04/official-development-assistance-2024-figures.html>；<https://www.oecd.org/en/data/insights/data-explainers/2026/04/a-historic-decline-in-foreign-aid-preliminary-2025-oda-data.html>
- **#52** 「There is no reason to believe that the number of crises, conflicts, natural disasters, and other situations th…」  
  判断：**正确**。UCDP数据：2024年国家参与的武装冲突达到61起，为二战后最高，连续第二年上升。联合国难民署称2025年底被迫流离失所者为1.178亿，十年来首次下降，但仍处于高位，降幅有限。引发困境性流动的危机与冲突在窗口内没有显著减少，书中判断成立。  
  来源：<https://www.prio.org/news/3616>；<https://www.uu.se/en/news/2025/2025-06-11-ucdp-sharp-increase-in-conflicts-and-wars>；<https://www.unhcr.org/nordic-and-baltic/news/press-releases/10-things-know-about-global-trends>
- **#54** 「Global imbalances, local shocks, and societies’ evolving needs will continue to generate cross-border movement…」  
  判断：**正确**。联合国经社部统计：2024年全球国际移民约3.04亿人，自1990年以来几乎翻倍；经合组织称2024年流入成员国的新永久移民为620万人，虽比2023年减少4%，但比2019年高15%。跨境人口流动在窗口内持续，书中判断成立。  
  来源：<https://www.destatis.de/EN/Themes/Countries-Regions/International-Statistics/Data-Topic/Population-Labour-Social-Issues/DemographyMigration/Migrants.html>；<https://www.oecd.org/en/publications/international-migration-outlook-2025_ae26c893-en.html>
- **#57** 「It will meet every four years.」  
  判断：**正确**。第二届国际移民审查论坛于2026年5月5日至8日在纽约联合国总部举行，闭幕时通过进展宣言，与首届（2022年）相隔四年，书中"每四年举行一次"成立。  
  来源：<https://www.iom.int/news/governments-review-migration-priorities-new-york>；<https://migrationnetwork.un.org/international-migration-review-forum-2026>
- **#58** 「will also meet every four years.」  
  判断：**正确**。第二届全球难民论坛于2023年12月13日至15日在日内瓦举行，与首届（2019年）相隔四年；难民署称论坛"每四年举行一次"。书中判断成立。  
  来源：<https://www.unhcr.org/events/global-refugee-forum-2023>；<https://emergency.unhcr.org/sites/default/files/2024-07/outcomes-global-refugee-forum-2023%20%284%29.pdf>

### 趋势符合（13 条）

- **#1** 「These trends will spark a global competition for workers.」  
  判断：**趋势符合**。窗口内多国在扩大或争取外国劳动力：意大利宣布2026–2028年发放近50万份非欧盟工作签证以应对劳动力短缺；日本拟把特定技能签证扩展到更多行业；美国提高H-1B费用后，加拿大、德国、中国等国趁机吸引外国人才。不过经合组织称2024年流入成员国的劳动移民下降超过两成，多国收紧政策。"争夺劳动力"的方向已经出现，但并非普遍，故只记趋势符合。  
  来源：<https://www.reuters.com/world/italy-issue-half-million-non-eu-work-visas-over-next-three-years-2025-06-30/>；<https://rollcall.com/2025/10/09/countries-try-to-lure-foreign-talent-after-trumps-h-1b-visa-fee-hike/>；<https://www.dw.com/en/wealthy-nations-curb-labor-migration-as-demand-surges/a-74978505>
- **#4** 「Regardless of politics, wealthy countries will need foreign workers to sustain their economies and honor their…」  
  判断：**趋势符合**。富裕国家对外国劳动力的依赖在加深：日本外国劳动者到2025年10月达到创纪录的257万人，同比增11.7%，厚生劳动省称原因是人口减少导致的严重劳动力短缺；意大利为应对劳动力缺口计划2026–2028年发放近50万份工作签证。方向一致，但"维持经济与社会承诺"的长期需求无法在窗口内完整检验，故只记趋势符合。  
  来源：<https://www.japantimes.co.jp/news/2026/01/30/japan/foreign-workers-record-high/>；<https://www.reuters.com/world/italy-issue-half-million-non-eu-work-visas-over-next-three-years-2025-06-30/>
- **#5** 「Many middle-income countries, traditionally the main sources of migration, will soon need to compete for forei…」  
  判断：**趋势符合**。传统移民来源的中等收入国家开始引进外劳：泰国内阁批准引进1万名斯里兰卡工人，以弥补柬埔寨工人回国造成的缺口；波兰的研究把雇用外国人视为应对人口老龄化与劳动年龄人口减少的办法；中国自2025年10月起推出K字签证吸引外国青年科技人才。方向已经出现，但"争夺"的规模尚难量化，故只记趋势符合。  
  来源：<https://www.reuters.com/world/asia-pacific/thailand-turning-sri-lankan-workers-cope-with-cambodian-exodus-official-says-2025-08-19/>；<https://zeszyty.fem.put.poznan.pl/pdf-202592-125031?filename=Zatrudnienie-cudzoziemcow.pdf>；<https://www.reuters.com/sustainability/sustainable-finance-reporting/chinas-new-k-visa-beckons-foreign-tech-talent-us-hikes-h-1b-fee-2025-09-29/>
- **#6** 「But at a time of renewed tensions in the international community, progress may be slow.」  
  判断：**趋势符合**。多边移民治理进展缓慢、国际分歧明显：2026年5月第二届国际移民审查论坛通过了进展宣言，但美国没有参加论坛，并拒绝支持这份宣言。合作仍在推进但阻力明显，与"进展可能缓慢"一致；"缓慢"本身难以量化，故只记趋势符合。  
  来源：<https://www.state.gov/releases/office-of-the-spokesperson/2026/05/the-united-states-rejects-international-migration-review-forum>；<https://www.iom.int/news/governments-review-migration-priorities-new-york>
- **#8** 「the populations of low-income countries are expected to continue to grow」  
  判断：**趋势符合**。澳大利亚人口中心整理的联合国《世界人口展望2024》按收入组汇总：低收入和中低收入国家将驱动全球人口增长；2025年这两组国家占世界人口的50.1%，而1950年高收入和中高收入国家占66.9%。资料显示低收入国家人口仍在增长、份额上升，方向与书中一致；但这类资料以预测为框架，窗口内逐年的实测增长数据不在所存页面里，所以严格起见只记趋势符合。  
  来源：<https://population.gov.au/sites/population.gov.au/files/2025-02/2024-un-world-pop-prospects.pdf>；<https://www.wiltonpark.org.uk/reports/towards-demographic-dividends-in-africa-action-and-investments/demographic-trends-and-why-they-matter/>
- **#11** 「Its demographic pyramid has begun to assume an inverted shape, and it is set to become even more unbalanced by…」  
  判断：**趋势符合**。INEGI 2025年中期普查：墨西哥总和生育率降到1.2，人口中位年龄升至32岁，年增长率0.7%、为二十年来最低。人口结构老化的方向与书中一致；"到2050年更加失衡"的终点未到，故只记趋势符合。  
  来源：<https://mexicobusiness.news/health/news/mexicos-population-growth-slows-two-decade-low-inegi>；<https://mexiconewsdaily.com/news/mexicos-population-growth-130-million-fertility-rate-falls/>
- **#12** 「The country is likely to remain young well through the middle of the century.」  
  判断：**趋势符合**。2025年尼日利亚人口中位年龄约18.1–18.2岁，是世界上最年轻的人口之一；ISS预测到2043年中位年龄仍只有21.6岁。窗口内"仍然年轻"成立；终点是本世纪中叶，故只记趋势符合。  
  来源：<https://www.prio.org/publications/14557>；<https://futures.issafrica.org/geographic/guide.pdf?geography=NG&topic=02-current-path>
- **#15** 「is expected to increase further, reaching 29 percent by midcentury.」  
  判断：**趋势符合**。经合组织成员国65岁以上人口占比2025年为19.0%，为1960年有数据以来最高；经合组织《养老金概览2025》称每100名劳动年龄人口对应33名65岁以上老人，老龄化在加速。占比持续上升的方向与书中一致；"本世纪中叶达29%"的终点未到，且证据口径是经合组织而非全部高收入国家，故只记趋势符合。  
  来源：<https://data.pispace.eu/countries/oecd-members/population-aged-65-and-over-share>；<https://www.oecd.org/en/publications/pensions-at-a-glance-2025_e40274c1-en/full-report/demographic-old-age-to-working-age-ratio_25476b96.html>
- **#18** 「In the absence of migration, it is expected to fall by a further 37 percent by 2050.」  
  判断：**趋势符合**。日本总务省人口估计：2025年10月1日15–64岁人口为7352.9万人，比上年减少19.9万人（-0.27%）；按住民基本台账，日本国籍人口2024年减少逾90万人，为有记录以来最大降幅。劳动年龄人口继续下降，方向与书中一致；"到2050年再降37%"的终点未到，故只记趋势符合。  
  来源：<https://www.stat.go.jp/data/jinsui/pdf/202603.pdf>；<https://www.cnn.com/2025/08/07/asia/japan-biggest-population-decline-record-intl-hnk>
- **#35** 「The reduction in technological barriers could lead firms to hire more “tele-migrants” in lower-wage countries」  
  判断：**趋势符合**。2025年行业报告显示，美国公司正迅速把远程招聘扩展到亚太地区（Native Teams），近岸和离岸远程用工因工资上涨和人才短缺而增长，拉美和菲律宾的远程机会大增（We Work Remotely）。但同期返岗政策增多，这类报告样本也有限，故只记趋势符合。  
  来源：<https://www.globenewswire.com/news-release/2025/04/24/3067630/0/en/u-s-companies-rapidly-expand-remote-hiring-into-apac-according-to-new-native-teams-report.html>；<https://weworkremotely.com/blog/welcome-to-we-work-remotely-s-state-of-remote-work-report-2025>
- **#36** 「Many of these countries were once sources of migration, but with declining fertility rates and rapidly aging p…」  
  判断：**趋势符合**。与第5条同：泰国批准引进斯里兰卡工人以弥补劳动力缺口；波兰研究把雇用外国人视为应对老龄化与劳动年龄人口减少的办法。中等收入国家需要外国劳动力的方向已经出现，但规模有限，故只记趋势符合。  
  来源：<https://www.reuters.com/world/asia-pacific/thailand-turning-sri-lankan-workers-cope-with-cambodian-exodus-official-says-2025-08-19/>；<https://zeszyty.fem.put.poznan.pl/pdf-202592-125031?filename=Zatrudnienie-cudzoziemcow.pdf>
- **#37** 「At current rates, it is likely to reach 1.5 degrees Celsius between 2030 and 2050.」  
  判断：**趋势符合**。据哥白尼气候变化服务，2024年是第一个全年平均气温明显高于工业化前1.5°C的年份；世界气象组织确认2025年约高1.43°C，2015–2025年是有记录以来最暖的11年。长期平均升温正逼近1.5°C，方向与书中一致；"2030–2050年间达到"的窗口还没到，故只记趋势符合。  
  来源：<https://climate.copernicus.eu/global-climate-highlights-2024>；<https://wmo.int/publication-series/state-of-global-climate/state-of-global-climate-2025>
- **#55** 「In most cases, automation, pro-natalist policies, and policy reforms in education, pension, and health care de…」  
  判断：**趋势符合**。日本外国劳动者到2025年达到创纪录的257万人，政府解释是人口减少造成严重劳动力短缺；意大利同样以劳动力短缺为由扩大合法劳动移民渠道。老龄化国家仍需劳动移民，方向一致；"自动化与政策改革不足以弥补缺口"无法在窗口内直接检验，故只记趋势符合。  
  来源：<https://www.japantimes.co.jp/news/2026/01/30/japan/foreign-workers-record-high/>；<https://www.reuters.com/world/italy-issue-half-million-non-eu-work-visas-over-next-three-years-2025-06-30/>

### 暂无法判断（38 条）

- **#2** 「Italy, with a population of 59 million, is projected to shrink by almost half, to 32 million, by 2100」  
  判断：**暂无法判断**。意大利人口到2100年降至3200万属长期预测；终点在2030年以后（或为长期情景），出版（2023年4月）至截止日（2026-11-15）的观察窗口只有约3.5年，无法判断。  
  来源：—
- **#3** 「Nigeria, by contrast, is expected to expand its population from 213 million to 791 million, becoming the secon…」  
  判断：**暂无法判断**。尼日利亚到本世纪末人口7.91亿、成为第二人口大国；终点在2030年以后（或为长期情景），出版（2023年4月）至截止日（2026-11-15）的观察窗口只有约3.5年，无法判断。  
  来源：—
- **#7** 「Some of the longterm drivers of mobility have been strengthening, and they are expected to intensify further i…」  
  判断：**暂无法判断**。人口、气候、收入差距等长期驱动因素在未来几十年进一步加强，为几十年尺度的判断；终点在2030年以后（或为长期情景），出版（2023年4月）至截止日（2026-11-15）的观察窗口只有约3.5年，无法判断。  
  来源：—
- **#9** 「In the decades to come, migration is likely to be driven largely by the needs of destination countries, which …」  
  判断：**暂无法判断**。未来几十年移民主要由目的地需求驱动、争夺日益缩小的合格劳动力池，为长期判断；终点在2030年以后（或为长期情景），出版（2023年4月）至截止日（2026-11-15）的观察窗口只有约3.5年，无法判断。  
  来源：—
- **#10** 「Mexico’s population is also set to decline」  
  判断：**暂无法判断**。墨西哥人口到2100年降至1.16亿：INEGI 2025年中期普查显示人口仍在增长（1.309亿），只是增速降到二十年来最低；终点在2030年以后（或为长期情景），出版（2023年4月）至截止日（2026-11-15）的观察窗口只有约3.5年，无法判断。  
  来源：<https://mexiconewsdaily.com/news/mexicos-population-growth-130-million-fertility-rate-falls/>
- **#13** 「while the world as a whole is rapidly aging, low-income countries will remain young throughout the century」  
  判断：**暂无法判断**。低收入国家"整个世纪"保持年轻，终点为2100年；终点在2030年以后（或为长期情景），出版（2023年4月）至截止日（2026-11-15）的观察窗口只有约3.5年，无法判断。  
  来源：—
- **#14** 「By 2050, it will be double that of children under age five and larger than the number of youth ages 15–24.」  
  判断：**暂无法判断**。2050年全球65岁以上人口是5岁以下儿童两倍；终点在2030年以后（或为长期情景），出版（2023年4月）至截止日（2026-11-15）的观察窗口只有约3.5年，无法判断。  
  来源：—
- **#16** 「Overall, the elderly population in highincome countries is projected to grow by about 118 million by 2050, whi…」  
  判断：**暂无法判断**。2050年高收入国家老年人口增1.18亿、劳动年龄人口减5300万为终点数值；终点在2030年以后（或为长期情景），出版（2023年4月）至截止日（2026-11-15）的观察窗口只有约3.5年，无法判断。  
  来源：—
- **#17** 「In the European Union, the shortage of health care workers is projected to reach 4.1 million by 2030, includin…」  
  判断：**暂无法判断**。欧盟医护人员缺口到2030年达410万为终点数值，没有检索窗口内可比的实际缺口统计；终点在2030年以后（或为长期情景），出版（2023年4月）至截止日（2026-11-15）的观察窗口只有约3.5年，无法判断。  
  来源：—
- **#19** 「It is projected to drop to below 2.0 by 2050」  
  判断：**暂无法判断**。高收入经合组织国家劳动年龄与老年人口之比到2050年降至2.0以下；终点在2030年以后（或为长期情景），出版（2023年4月）至截止日（2026-11-15）的观察窗口只有约3.5年，无法判断。  
  来源：—
- **#20** 「these countries are projected to increase public expenditures by up to 7.6 percentage points of gross domestic…」  
  判断：**暂无法判断**。到2060年老龄化相关公共支出增加最多7.6个百分点；终点在2030年以后（或为长期情景），出版（2023年4月）至截止日（2026-11-15）的观察窗口只有约3.5年，无法判断。  
  来源：—
- **#21** 「Without major policy reforms, aging could raise the public debt burden of advanced economies in the Group of T…」  
  判断：**暂无法判断**。若无改革，到2050年G20发达经济体债务上升180%：为条件性模型情景，终点在2030年以后（或为长期情景），出版（2023年4月）至截止日（2026-11-15）的观察窗口只有约3.5年，无法判断。  
  来源：—
- **#22** 「the sustainability of pension systems will already be at risk in the coming decade.」  
  判断：**暂无法判断**。"未来十年"养老金体系可持续性面临风险：没有检索到窗口内这些国家养老金体系可持续性的统一评估；十年期未到，无法判断。  
  来源：—
- **#23** 「In the second-most populous country, India, the population is projected to fall after midcentury.」  
  判断：**暂无法判断**。印度人口本世纪中叶后下降；终点在2030年以后（或为长期情景），出版（2023年4月）至截止日（2026-11-15）的观察窗口只有约3.5年，无法判断。  
  来源：—
- **#24** 「The share of elderly in their population is expected to double by 2050.」  
  判断：**暂无法判断**。中高收入国家老年人口占比到2050年翻倍；终点在2030年以后（或为长期情景），出版（2023年4月）至截止日（2026-11-15）的观察窗口只有约3.5年，无法判断。  
  来源：—
- **#25** 「It is expected to peak by 2050 in lower-middle-income countries.」  
  判断：**暂无法判断**。中低收入国家劳动年龄人口占比2050年前见顶；终点在2030年以后（或为长期情景），出版（2023年4月）至截止日（2026-11-15）的观察窗口只有约3.5年，无法判断。  
  来源：—
- **#26** 「Among the emerging economies in the G20, aging could raise public debt burdens by an average of 130 percent of…」  
  判断：**暂无法判断**。若无改革，到2050年G20新兴经济体债务上升130%：为条件性情景，终点在2030年以后（或为长期情景），出版（2023年4月）至截止日（2026-11-15）的观察窗口只有约3.5年，无法判断。  
  来源：—
- **#27** 「Sub-Saharan Africa—where most lowincome countries are located—is expected to be the only region whose populati…」  
  判断：**暂无法判断**。撒哈拉以南非洲是2050年后唯一人口仍增长的地区；终点在2030年以后（或为长期情景），出版（2023年4月）至截止日（2026-11-15）的观察窗口只有约3.5年，无法判断。  
  来源：—
- **#28** 「In the absence of emigration, low- and lowermiddle-income countries are expected to add 1.05 billion people to…」  
  判断：**暂无法判断**。到2050年低收入与中低收入国家劳动年龄人口增加10.5亿；终点在2030年以后（或为长期情景），出版（2023年4月）至截止日（2026-11-15）的观察窗口只有约3.5年，无法判断。  
  来源：—
- **#29** 「Many of these economies are unlikely to grow sufficiently fast to generate the jobs needed to absorb their you…」  
  判断：**暂无法判断**。世界银行2025年称未来十年发展中国家将有12亿年轻人进入劳动年龄，但预计只新增约4.2亿个就业岗位。这本身仍是预测而非观测结果，窗口内没有取得足以判定的实际就业缺口数据，无法判断。  
  来源：<https://www.worldbank.org/en/news/immersive-story/2025/04/17/jobs-the-surest-way-to-fight-poverty>
- **#31** 「In high-income OECD countries, the working age (20–64 years) to elderly ratio was 2.9 in 2022, and it is likel…」  
  判断：**暂无法判断**。高收入经合组织国家劳动年龄与老年人口之比到2050年降至1.85；终点在2030年以后（或为长期情景），出版（2023年4月）至截止日（2026-11-15）的观察窗口只有约3.5年，无法判断。  
  来源：—
- **#33** 「Occupations employing large numbers of people today will likely be automated in the coming decades.」  
  判断：**暂无法判断**。目前雇用大量人员的职业"未来几十年"被自动化；终点在2030年以后（或为长期情景），出版（2023年4月）至截止日（2026-11-15）的观察窗口只有约3.5年，无法判断。  
  来源：—
- **#34** 「Automation and technological innovations are, however, unlikely to fully offset the increase in demand for wor…」  
  判断：**暂无法判断**。自动化不太可能完全抵消老龄化国家的劳动力需求：没有取得窗口内可检验的指标，属于长期判断，无法判断。  
  来源：—
- **#38** 「Climate change is already accelerating internal migration through both sudden- and slow-onset impacts. These e…」  
  判断：**暂无法判断**。气候对国内迁移的影响"随时间增强"：IDMC称2024年国内流离失所人数创纪录（8340万），但2025年灾害导致的流离失所为2990万次，比2024年的异常高位下降35%。单年数据方向相反，长期趋势无法判断。  
  来源：<https://www.iom.int/news/idmc-report-record-83-million-people-living-internal-displacement-worldwide>；<https://www.nrc.no/news/2026/conflict-and-violence-become-the-leading-driver-of-internal-displacements?ceid=%7B%7BContactsEmailID%7D%7D&emdi=ea000000-0000-0000-0000-000000000001>
- **#39** 「Projections to 2050 of climate-related internal migration across developing countries range from 44 million to…」  
  判断：**暂无法判断**。到2050年气候相关国内迁移4400万至2.16亿；终点在2030年以后（或为长期情景），出版（2023年4月）至截止日（2026-11-15）的观察窗口只有约3.5年，无法判断。  
  来源：—
- **#40** 「The population is expected to grow from 1.2 billion today to 2.5 billion in 2050.」  
  判断：**暂无法判断**。撒哈拉以南非洲2050年人口25亿；终点在2030年以后（或为长期情景），出版（2023年4月）至截止日（2026-11-15）的观察窗口只有约3.5年，无法判断。  
  来源：—
- **#41** 「As a result, Sub-Saharan Africa is likely to see further movements in the coming decades, some under distresse…」  
  判断：**暂无法判断**。撒哈拉以南非洲"未来几十年"出现更多流动，为长期判断；终点在2030年以后（或为长期情景），出版（2023年4月）至截止日（2026-11-15）的观察窗口只有约3.5年，无法判断。  
  来源：—
- **#42** 「Even with adaptation, certain areas could eventually become unsuitable for food production under high-emission…」  
  判断：**暂无法判断**。高排放情景下部分地区最终不适合粮食生产：为条件性长期情景，无法判断。  
  来源：—
- **#43** 「Globally, US$7–$14 trillion in coastal infrastructure assets could be at risk by 2100」  
  判断：**暂无法判断**。到2100年7–14万亿美元沿海资产面临风险；终点在2030年以后（或为长期情景），出版（2023年4月）至截止日（2026-11-15）的观察窗口只有约3.5年，无法判断。  
  来源：—
- **#44** 「In these states, sea levels are projected to rise by 0.15–0.40 meters by 2050 in worst-case scenarios」  
  判断：**暂无法判断**。最坏情景下小岛屿国家海平面到2050年上升0.15–0.40米：为条件性情景，终点在2030年以后（或为长期情景），出版（2023年4月）至截止日（2026-11-15）的观察窗口只有约3.5年，无法判断。  
  来源：—
- **#45** 「In some parts of South Asia, tropical Sub-Saharan Africa, and Latin America, climate change is expected to red…」  
  判断：**暂无法判断**。气候变化降低南亚等地户外工作能力：没有检索到窗口内可比的观测指标，无法判断。  
  来源：—
- **#46** 「Climate change could lead to large, distressed cross-border movements.」  
  判断：**暂无法判断**。气候变化"可能"导致大规模困境跨境迁移，为可能性陈述且无时点，无法判断。  
  来源：—
- **#47** 「it is still headed toward 2.8 degrees Celsius of warming by the end of the century」  
  判断：**暂无法判断**。联合国环境署《排放差距报告2025》：按国家自主贡献完全实施，本世纪升温预估为2.3–2.5°C（上年为2.6–2.8°C），方法调整占其中约0.1°C。本世纪末升温终点无法在窗口内观察，终点在2030年以后（或为长期情景），出版（2023年4月）至截止日（2026-11-15）的观察窗口只有约3.5年，无法判断。  
  来源：<https://www.unep.org/en/news-and-stories/press-release/new-climate-pledges-only-slightly-lower-dangerous-global-warming>
- **#48** 「This new policy is expected to benefit both Syrian refugee women and Jordanian women whose ability to work out…」  
  判断：**暂无法判断**。约旦允许注册家庭作坊的政策让两国女性受益：没有检索到窗口内的效果评估，无法判断。  
  来源：—
- **#51** 「Even with access to the labor market, these refugees are unlikely to become fully self-reliant in the short to…」  
  判断：**暂无法判断**。残障比例高的叙利亚难民中短期内不能完全自立：没有检索到窗口内针对这一群体的评估，无法判断。  
  来源：—
- **#53** 「According to the US Bureau of Labor Statistics, the top three occupations that will add the highest number of …」  
  判断：**暂无法判断**。美国劳工统计局对2030年新增就业最多职业的预测，终点2030年；终点在2030年以后（或为长期情景），出版（2023年4月）至截止日（2026-11-15）的观察窗口只有约3.5年，无法判断。  
  来源：—
- **#56** 「The International Monetary Fund (IMF) estimated that by 2030 this policy could increase Colombia’s gross domes…」  
  判断：**暂无法判断**。国际货币基金组织估计到2030年该政策最多使哥伦比亚GDP提高4.5个百分点：为反事实估计，终点2030年，无法判断。  
  来源：—
- **#59** 「As the world struggles to cope with global economic imbalances, diverging demographic trends, and climate chan…」  
  判断：**暂无法判断**。未来几十年移民成为各收入水平国家的必需，为几十年尺度的判断；终点在2030年以后（或为长期情景），出版（2023年4月）至截止日（2026-11-15）的观察窗口只有约3.5年，无法判断。  
  来源：—

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/world-bank-wdr-2023-migrants-refugees-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/world-bank-wdr-2023-migrants-refugees-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/world-bank-wdr-2023-migrants-refugees-v5/audit/manual_review_2026-11-15.py`

## 说明

- 抽取密度：345 个 chunk 中有 59 条可解析预测（约每 chunk 0.17 条，每 10 万字符约 5 条），低于英文书 0.2–0.35 的参考值。原因是本报告约四成篇幅为参考文献、注释、图表和政策案例框，第 4–9 章以描述现状与政策建议为主；预测集中在第 1、3 章的人口与气候部分。没有为凑数抽取政策建议或一般机制。
- 条件句与情景数字（如“若无改革到 2050 年债务上升 180%”、高排放情景）按条件处理，条件未成立或不可观察，记暂无法判断。
- 趋势符合只用于窗口内方向已被存档证据明确证实、但数值或终点尚未到期的条目。

