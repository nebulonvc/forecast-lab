# 纳西姆·尼古拉斯·塔勒布《反脆弱》（Antifragile: Things That Gain from Disorder，2012）：出版后预测人工核查

- 案例目录：`cases/taleb-antifragile-v5/`
- 出版日期：Random House 2012 年英文初版精装，美国出版日 **2012-11-27**（ISBN 978-1-4000-6782-4）。所用 PDF 为 `reading-library/2026-11-15-未来判断书单/04-经济和金融/28-反脆弱.pdf`（sha256 `0baacce5c1f23fedd901886e44cbe68dace82eb670ed0e96c1eab2ad12a225f1`，6,065,954 字节，已与队列逐字节核对一致）。经 `pdftotext -enc UTF-8` 生成 TXT（sha256 `bea1087489a460aba78d3835a0d3c2dbf3390106dc7c9945c32cc2422768e9da`，1,113,110 字符；TXT 不入库）。观察窗口按 2012-11-27 起算，至 2026-11-15。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

本稿按 METHOD.md 复刻 DeepSeek 流水线，只把模型调用换成助手人工阅读。抽取：用仓库 prepare_book v5（toolkit 来自 main `85e6da1`）把全文切成 322 块（3500 字符、600 字符上下文），助手逐块通读，按 DISCOVER_PROMPT_V5 写出模型本应返回的 JSON（可为空），再由仓库代码完成引文对齐、非预测筛除、归属降级和去重，得到 22 条候选、全部为可核验（resolvable）预测。核验：每条可核验候选先定 scope，用 Exa 各做一次 support/counter 检索（5 条做了适应性补充检索），只从检索返回的 URL 中选源，存档到 `data/sources/`（sha256），写入 `data/evidence.jsonl`，再经 `pipeline.py apply assess → check → report`。本稿由助手逐条对照书中原文与存档证据人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 22 条，剔除非预测 0 条，计入 **22 条预测**，其中 **15 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 4 |
| 趋势符合 | 5 |
| 部分符合 | 4 |
| 错误 | 2 |
| 暂无法判断 | 7 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **26.7%**（4/15） |
| 加权胜率 | **65.0%** |
| 错误率 | **13.3%**（2/15） |
| 未定占比（暂无法判断/预测） | 31.8%（7/22） |

## 总体评价

本书以反脆弱框架、医源性和“皮肤在场”伦理为主，明确可核验的未来判断并不多。322 块中有 22 条可核验预测。可判定的 15 条中，4 条正确（赢家通吃加剧、印钞后通胀跃升、脆弱性转移更严重、复杂监管成为前监管者金矿），5 条趋势符合（对人造系统越来越不理解、流量/销售向 99/1 靠近但未达到、汽车技术仍存、25 年技术仍在、被数据愚弄随大数据加剧），4 条部分符合（Extremistan 份额、产油国教育开支、城邦与小公司、更大危机），2 条错误（可用药物池应缩小、花旗将再次爆破）。教育机构终将崩溃、黑天鹅效应必然增强、2036 年前大公司应消失、民族国家/央行/经济系权力被严重削弱、经济学家再次把我们搞炸、大型加成公司终将自毁、公司因代理问题最终崩溃等 7 条因终点未到或缺少决定性度量，判为暂无法判断。趋势符合按严格口径使用；无明确期限的长期判断宁可暂无法判断。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（4 条）

- **#2** 「Winner-take-all effects are worsening: success for an author, a company, an idea, a musician, an athlete is pl…」  
  判断：**正确**。Experimental History 2022 年综述指出，电影、电视、音乐、图书和游戏中，越来越小的超级明星卡特尔占据越来越大的市场份额，赢家通吃已从“分一杯羹”变成“通吃大半”；2025 年对文化领域幂律的复盘也支持头部更瘦、中腰更弱。方向在窗口内成立。  
  来源：<https://www.experimental-history.com/p/pop-culture-has-become-an-oligopoly>；<https://dougshapiro.substack.com/p/power-laws-in-culture-revisited>
- **#7** 「central banks can print money; they print and print with no effect (and claim the “safety” of such a measure),…」  
  判断：**正确**。欧洲央行执委施纳贝尔 2023 年指出，疫情后两年半欧元区 M1 增长逾 30%，通胀从 1.2% 升至 9.1%，并于 2022 年 10 月见顶 10.6%；英国 IEA 汇编的 2022 年美、欧、英消费通胀约 8%。书中“先看似无效、再意外跳升”的序列在窗口内出现。局限是部分官方分析同时强调能源冲击与供给因素。  
  来源：<https://www.ecb.europa.eu/press/key/date/2023/html/ecb.sp230925_1~7ad8ef22e2.en.html>；<https://iea.org.uk/wp-content/uploads/2023/09/IEA_SPecial-Editions_1_The-new-great-inflation_web.pdf>
- **#15** 「The effects of transfers of fragility are becoming more acute, as modernity is building up more and more peopl…」  
  判断：**正确**。无日期的方向性判断，按出版至截止日窗口衡量。2023 年硅谷银行等事件后，美国法律评论 2026 年称机构救助已成为“新常态”，并点名储蓄信贷危机、次贷危机至 SVB、Signature；损失社会化和道德风险在窗口内持续甚至再现，主方向成立。  
  来源：<https://digitalcommons.wcl.american.edu/aublr/vol15/iss1/3>；<https://www.directorsandboards.com/risk-oversight/financial-risk/silicon-valley-bank-collapse-lessons-for-boards/>
- **#21** 「Twenty-three hundred pages of regulation— something I can replace with Hammurabi’s rule—will be a gold mine fo…」  
  判断：**正确**。Bloomberg Law 2017 年统计，2016 年初以来离职的 26 名SEC高官中，超过一半进入律所或金融机构；另有商品期货交易委员会市场监管前负责人、货币监理前署长等多起转任律所的公开报道。约 2300 页级复杂监管成为前监管者的“金矿”，在窗口内得到证实。冷却期规则并未阻止这一通道。  
  来源：<https://news.bloomberglaw.com/business-and-practice/new-sec-alums-swarm-revolving-door-to-financial-law-firms>；<https://www.prnewswire.com/news-releases/former-sec-enforcement-director-robert-khuzami-joins-kirkland--ellis-216568301.html>

### 趋势符合（5 条）

- **#3** 「Our sophistication continuously puts us ahead of ourselves, creating things we are less and less capable of un…」  
  判断：**趋势符合**。2012 年后深度网络与大模型被广泛承认为黑箱，2023 年数字人文学刊与 2021 年 Minds and Machines 均指出决策机制不透明、可解释性不足；这与“对人造成物越来越缺乏理解”的方向一致。但缺乏可量化的理解能力指标，且可解释 AI 同时在发展，故记趋势符合而非正确。  
  来源：<https://link.springer.com/article/10.1007/s42803-023-00075-w>；<https://link.springer.com/article/10.1007/s11023-021-09569-4>
- **#9** 「Few realize that we are moving into the far more uneven distribution of 99/1 across many things that used to b…」  
  判断：**趋势符合**。CSI Magazine 转述 Sandvine《2024 年全球互联网现象报告》：谷歌、Facebook 与 Netflix 合计驱动全球固定和移动流量近 70%，集中度已远高于传统 80/20，但尚未达到书中的 99/1；图书方面长尾研究认为向利基的转移有限，亚马逊渠道份额很高。方向成立，终点未到，记趋势符合。  
  来源：<https://www.csimagazine.com/csi/sandvine-2024-internet-report.php>；<https://jindal.utdallas.edu/news/jindal-school-study-shows-why-online-retail-hasnt-transformed-book-sales/>
- **#10** 「A single car is perishable, but the automobile as a technology has survived about a century (and we will specu…」  
  判断：**趋势符合**。书中给出“再存活一个世纪”的明确长期限（约至 2112 年）。IEA 与 SLOCAT 显示 2025 年道路运输仍约占全球旅客周转量三分之二，德国 2025 年千人汽车保有量创新高；电动汽车仍属于汽车技术。技术并未消失，终点未到，记趋势符合。  
  来源：<https://www.iea.org/reports/energy-efficiency-2025/transport>；<https://www.destatis.de/Europa/EN/Topic/Transport/Car.html>
- **#11** 「I would expect the future to be populated with wall-to-wall bookshelves, the device called the telephone, arti…」  
  判断：**趋势符合**。面向约 2036 年的判断。截止日前，书架、电话和手工艺均仍存在：CNN 2026 年报道手工/模拟爱好升温，Dazed 2026 年仍在讨论有线电话的使用。终点未到，方向成立，记趋势符合。  
  来源：<https://www.cnn.com/2026/01/18/business/crafting-soars-ai-analog-wellness>；<https://www.dazeddigital.com/life-culture/article/70467/1/has-having-a-landline-ultimate-flex-corded-phone-digital-burnout>
- **#22** 「The fooled-by-data effect is accelerating.」  
  判断：**趋势符合**。大数据与机器学习中的虚假相关在 2012 年后成为持续扩大的研究主题（过参数化加剧虚假相关、高维回归等）；可重复性危机的大规模复现项目仍报告低再现率。开放科学带来一些程序改进，但并未否定“数据量增大、虚假信息更快增长”的方向，记趋势符合。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC13726918/>；<https://proceedings.mlr.press/v119/sagawa20a.html>

### 部分符合（4 条）

- **#1** 「because of modernity, the share of Extremistan is increasing.」  
  判断：**部分符合**。世界不平等实验室与 Inequality.org 称 2025 年全球最富 1% 占有 20.3% 的全球收入，并给出上升幅度；美国顶级财富集中仍处高位。但世界银行指出，全球（国家间）收入基尼在疫情前近三十年几乎持续下降。尾部/顶端集中与全球基尼走势并不一致，主结果只部分成立。  
  来源：<https://inequality.org/facts/global-inequality/>；<https://blogs.worldbank.org/en/opendata/income-growth-of-the-poor-matters-for-reducing-global-income-ine>
- **#4** 「Their wealth came from oil, not from some vocational know-how, so I am certain that their spending on educatio…」  
  判断：**部分符合**。LSE 与 EPIC 指出阿联酋 PISA 2022 数学/阅读/科学仍低于经合组织平均 41–59 分；IMF 2023 年仍称碳氢收入约占财政总收入 60%。教育开支并非完全无效：WIPO《2025 年全球创新指数》中阿联酋列第 30，非石油部门也有增长。因此“完全徒劳、无法转化为知识型繁荣”只部分成立。  
  来源：<https://blogs.lse.ac.uk/mec/2021/04/13/uae-schooling-risks-missing-the-bus/>；<https://www.elibrary.imf.org/view/journals/002/2023/224/article-A004-en.xml>
- **#13** 「corporations are more likely to be around, even thrive.」  
  判断：**部分符合**。新加坡、迪拜等城邦在窗口内明显存续并扩张（哈佛国际评论等）；但小型公司一端，独立商业研究显示亚马逊等平台挤压中小企业，新企业形成走弱的讨论也在持续。城邦部分更符合，小公司“甚至繁荣”并未普遍成立，故为部分符合。  
  来源：<https://hir.harvard.edu/singapore-dubai-model-opportunities-for-expansion-in-africa-latin-america-and-beyond/>；<https://ilsr.org/article/independent-business/turning-public-money-into-amazons-profits/>
- **#16** 「No wonder we will have larger crises.」  
  判断：**部分符合**。语境是比 2007–2008 年更大的危机。苏黎世理工学院 KOF 称新冠危机引发二战结束以来最严重的全球经济下滑；但德意志银行 2026 年综述认为 2008 年后并未再发生重大金融危机。短期实体收缩一度超过金融危机，金融体系式“更大爆破”并未出现，故为部分符合。  
  来源：<https://kof.ethz.ch/en/news-and-events/kof-bulletin/kof-bulletin/2021/10/Comparing-the-coronavirus-crisis-and-the-financial-crisis-eight-differences-and-similarities.html>；<https://theideafarm.com/global-marcoeconomics/why-hasnt-there-been-a-major-financial-crisis-in-recent-years/>

### 错误（2 条）

- **#5** 「we may be underestimating the interactions of current drugs, those already on the market, by a factor of four …」  
  判断：**错误**。预测是可用药物池应缩小而非扩大。相反，FDA CDER 2025 年批准 46 种前所未有的新药；BioCentury 称截至 2026 年 10 月底新分子实体批准数已追平历史前十个月高点。窗口内新药持续进入市场，主结果与预测相反。  
  来源：<https://www.fda.gov/drugs/novel-drug-approvals-fda/novel-drug-approvals-2025>；<https://www.biocentury.com/article/661500/fda-approvals-on-track-for-record-year>
- **#20** 「Citibank will blow up again (and we taxpayers will end up subsidizing his high salary).」  
  判断：**错误**。窗口内花旗集团并未再次破产或接受 2008 年式救助。惠誉 2025 年 8 月确认长期发行人评级为 A、展望稳定；晨星 DBRS 2026 年 2 月确认长期评级 A（高）、展望稳定，并指 2025 年经营改善。主结果与“将再次爆破”相反。括号中纳税人补贴奥尔萨格高薪亦无新的救助式证据。  
  来源：<http://www-origin.fitchratings.com/research/banks/fitch-affirms-citigroup-inc-at-a-f1-outlook-stable-15-08-2025>；<https://dbrs.morningstar.com/research/473614/morningstar-dbrs-confirms-long-term-credit-ratings-of-citigroup-inc-at-a-high-stable-trend>

### 暂无法判断（7 条）

- **#6** 「Education is an institution that has been growing without external stressors; eventually the thing will collap…」  
  判断：**暂无法判断**。“最终会崩溃”没有可检验的终点。联合国教科文组织 2026 年报告称全球高等教育在校生 2024 年达 2.69 亿，二十年间翻倍以上；英、美确有部分院校关闭或陷入财务危机，但建制教育体系并未崩溃。决定性事实尚未出现。  
  来源：<https://www.unesco.org/en/articles/number-students-higher-education-more-doubled-20-years-inequalities-remain>；<https://publications.parliament.uk/pa/cm5901/cmselect/cmeduc/807/report.html>
- **#8** 「Black Swan effects are necessarily increasing, as a result of complexity, interdependence between parts, globa…」  
  判断：**暂无法判断**。窗口内出现新冠等极端冲击，但检索未得到“黑天鹅效应”在频率或强度上必然增强的可比较度量；国际货币基金组织等仍讨论 2008 年后的金融稳定，无法据此确认或否定“必然增强”。  
  来源：<https://www.imf.org/en/publications/wp/issues/2026/05/14/systemic-banking-crises-database-1970-2025-576036>；<https://www.federalreserve.gov/econres/feds/files/2025043pap.pdf>
- **#12** 「Corporations that are large today should be gone, as they have always been weakened by what they think is thei…」  
  判断：**暂无法判断**。同一 2036 练习的终点尚未到达。晨星 2026 年指出埃克森美孚、沃尔玛等 2012 年前后的巨头仍在存续甚至兴旺，苹果等继续位居市值前列；BCG 称 2005–2025 年多数行业的领导地位更替反而放缓。既不能说“今天的大公司应已消失”，也不能在终点前判错。  
  来源：<https://indexes.morningstar.com/insights/perspective/blt802bb0c3003f3e58/nvidia-lost-top-spot-apple-what-does-history-tell-us-about-no-1-stocks>；<https://www.bcg.com/publications/2026/market-leaders-staying-on-top-longer>
- **#14** 「The nation-state, the currencyprinting central bank, these things called economics departments, may stay nomin…」  
  判断：**暂无法判断**。2036 视野下“权力被严重削弱”的终点未到。疫情与之后央行资产负债表和职责反而扩大（新政治经济学文献称其获得前所未有的权力），同时独立地位受到政治压力；民族国家在防疫、战争和产业政策中仍处核心。复合对象缺少决定性的“严重削弱”事实。  
  来源：<https://www.tandfonline.com/doi/full/10.1080/13563467.2025.2504405>；<https://www.axios.com/2025/08/25/fed-trump-powell-jackson-hole-economy>
- **#17** 「It is a severe disease, one that explains why economists will blow us up again.」  
  判断：**暂无法判断**。“经济学家会再次把我们搞炸”没有期限。2021–22 年通胀被部分人归咎于货币政策误判，但窗口内没有出现与 2008 年相当、由经济学误判驱动的系统性金融崩盘；德意志银行 2026 年亦强调 2008 年后无重大金融危机。既不能判正确，也不宜仅因尚未发生而判错。  
  来源：<https://theideafarm.com/global-marcoeconomics/why-hasnt-there-been-a-major-financial-crisis-in-recent-years/>；<https://www.nber.org/papers/w35673>
- **#18** 「Of course they will eventually self-destruct, but that’s another conversation.」  
  判断：**暂无法判断**。“最终会自我毁灭”属于开放期限。可口可乐与百事可乐 2025 年年报仍显示高额营收与利润，大型制药公司在减肥药带动下继续扩张。个别企业受挫不等于这类公司已经自毁，终点未到。  
  来源：<https://thebusinessstudy.com/compare/coca-cola-vs-pepsico/>；<https://www.contractpharma.com/exclusives/by-the-numbers-top-10-pharma-biopharma-companies/>
- **#19** 「In sum, corporations are so fragile, long-term, that they eventually collapse under the weight of the agency p…」  
  判断：**暂无法判断**。“长期如此脆弱、最终因代理问题崩溃”没有可检验终点。经合组织《2025 年公司治理概况》称 2024 年底全球约有 4.4 万家上市公司、总市值约 125 万亿美元；虽有 Carillion、硅谷银行等个案，公司形态并未崩溃。  
  来源：<https://www.oecd.org/en/publications/oecd-corporate-governance-factbook-2025_f4f43735-en/full-report/global-public-markets-and-corporate-ownership_c5012184.html>；<https://fortune.com/2025/10/07/public-company-why-so-few-ipos-startups-unicorns/>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/taleb-antifragile-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/taleb-antifragile-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/taleb-antifragile-v5/audit/manual_review_2026-11-15.py`

## 说明

- 抽取密度（22 条可核验 / 322 块 ≈ 0.07）低于 METHOD §5 英文书参考区间（约 0.2—0.35）。本书以机制、伦理和框架论证为主，箴言、规范性建议、思想实验和科学规律性陈述未计为预测；未为提高数量而放宽标准。序言目录、章节提要、术语表、附录、注释、参考文献、致谢和作者介绍按前后附文规则人工排除（明细见 PR_BODY）。
- 趋势符合只在存档证据明确证实方向、且明确终点尚未到达时使用。无明确期限的“最终崩溃/再次爆破式”长期判断，若窗口内既未实现也未被相反事实完全证伪，判为暂无法判断；花旗“将再次爆破”因窗口内银行明显稳定、未再破产或救助，判为错误。
- 证据以独立第三方为主（世界不平等实验室/Inequality.org、Experimental History、欧洲央行、FDA、Sandvine/CSI Magazine、IEA、联合国教科文组织、IMF、惠誉、晨星 DBRS、Bloomberg Law 等），并保留相反证据。
- `data/claims.jsonl`、`output/txt_import/claims_proposals.jsonl` 及评估快照中的 `context` 字段已清空，案例不含整段书中原文。

