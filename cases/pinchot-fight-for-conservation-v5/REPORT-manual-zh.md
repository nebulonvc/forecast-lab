# Gifford Pinchot《The Fight for Conservation》（1910）：出版后预测人工核查

- 案例目录：`cases/pinchot-fight-for-conservation-v5/`
- 出版日期：1910年；1910-01-01仅为年精度代理，并非已核实月日
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

完整阅读本书45/45个3500字符body（前后600字符context仅助理解），非关键词选句。原始73条由原validate_chunk_predictions与claims_from_results确定性排除5条（格言2、机制1、规范2），保留全部68条且全部resolvable；ASSESS不再排除，没有语义去重或duplicate排除，自动重叠去重0。TXT为单栏，不涉及双栏重排/OCR。实际使用Exa新密钥路径，未使用DeepSeek。每条先写scope及正反查询，再从真实返回URL中选不超过8个来源，读取存档后逐条写中文理由、限制和六维审查。第一轮136个计划查询中135成功，#10 support中断保留不确定请求且未重试；第二轮换查询补足，并对仍缺证据的主题作自适应补查，共29条58个第二轮查询，未用第三轮。总计193个成功查询、128个URL/128份来源存档；Exa contents通常至多12000字符，森林管理历史一页另以urllib+BeautifulSoup抓完整公开HTML。所有判分事实限定存档可见内容。无日期方向按1910→2026-11-15窗口，未触发条件不给正确或错误，未知条件可观察后果仅给部分符合；无终点及缺口明确者保守未定。此为有相关性的回顾性父记录计数，不是独立预测技巧估计。

下述通用流程中，非预测排除发生于原代码抽取阶段；不是按关键词或人工挑选最终候选。先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 68 条，剔除非预测 0 条，计入 **68 条预测**，其中 **43 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 16 |
| 趋势符合 | 0 |
| 部分符合 | 21 |
| 错误 | 6 |
| 暂无法判断 | 25 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **37.2%**（16/43） |
| 加权胜率 | **61.6%** |
| 错误率 | **14.0%**（6/43） |
| 未定占比（暂无法判断/预测） | 36.8%（25/68） |

## 总体评价

资源保护、农业和政治改革的方向性预期有多项发生；资源固定速率耗尽情景须保留条件，不能以今日仍有资源直接证伪。金钱政治将完全退出等绝对政治结果未兑现。68条包含相互关联和重复主题，全部按原代码保留，不进行语义去重；25条未定反映具体条件或证据缺口。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（16 条）

- **#2** 「We shall reach a population of two hundred millions in the very near future, as time is counted in the lives o…」  
  判断：**正确**。人口普查局记载人口钟在1967年11月20日达到2亿，出版后约57年实现了人口规模预测。  
  来源：<https://www.census.gov/library/photos/1967/pop-clock-200-million.html>
- **#5** 「They are accompanied by the certainty of a future loss not less important, for range lands once badly overgraz…」  
  判断：**正确**。USDA的Jornada长期恢复试验报告许多修复失败，成功往往需要持续数十年的维护，符合严重退化牧地恢复缓慢或失败的方向。  
  来源：<https://jornada.nmsu.edu/ecosystem-response/rangeland-restoration>；<https://www.ars.usda.gov/plains-area/las-cruces-nm/range-management-research/docs/ability-to-restore/>
- **#8** 「it is certain that the rate of consumption of timber will increase enormously in the future, as it has in the …」  
  判断：**正确**。Rockefeller工业生态研究记载1990年代美国每年采出木材比1900年多70%，同时森林面积大致稳定，支持在仍有供应时总量大幅增长。  
  来源：<https://phe.rockefeller.edu/publication/searching-leverage-conserve-forests/>；<https://elischolar.library.yale.edu/cgi/viewcontent.cgi?article=1047&context=yale_fes_bulletin>
- **#11** 「We must necessarily begin to suffer from the scarcity of timber long before our supplies are completely exhaus…」  
  判断：**正确**。1942年美国商务部材料记载木材库存不足和战争采购困难，显示未到完全耗尽时已经发生短缺，符合先经历稀缺的顺序判断。  
  来源：<https://fraser.stlouisfed.org/files/docs/publications/SCB/pages/1940-1944/3397_1940-1944.pdf>
- **#22** 「We can not, and we ought not, to continue exclusively, or even chiefly, an agricultural country, because one m…」  
  判断：**正确**。USDA ERS记录20世纪农业的经济和就业比重下降、农场数量减少与规模增大，符合美国不再主要作为农业国的方向。  
  来源：<https://www.ers.usda.gov/media/8254/eib-3.pdf?v=75034>
- **#31** 「River improvement means better conditions of transportation than we have now, but it means development too.」  
  判断：**正确**。密西西比河九英尺航道历史记载廉价运输和区域开发作用，国家科学院资料也讨论航道建设，符合改善运输并促进开发的方向。  
  来源：<https://www.nationalacademies.org/read/10072/chapter/3>；<http://purl.umn.edu/93150>
- **#32** 「The adjustment of opposite demands between conflicting interests and localities, and other questions of large …」  
  判断：**正确**。Kansas诉Colorado及流域治理研究记载跨州用水冲突和多层法律协调，符合河流开发将面对复杂利益及法律问题的判断。  
  来源：<https://www.law.cornell.edu/supremecourt/text/514/673>；<https://www.frontiersin.org/journals/water/articles/10.3389/frwa.2022.1024055/full>
- **#33** 「Nothing that can be said or done will suffice to postpone longer the active phases of this fight; and that is …」  
  判断：**正确**。水电政策历史记载持续争论并通向1920年《Federal Power Act》，符合公共利益与私人权利之争进入公开制度冲突。  
  来源：<https://digitalcommons.law.uidaho.edu/cgi/viewcontent.cgi?article=1046&context=idaho-law-review>；<https://www.repository.law.indiana.edu/cgi/viewcontent.cgi?article=1927&context=facpub>
- **#40** 「Decision made now as to the character of our public life will be valid for many years, for it is but seldom th…」  
  判断：**正确**。第十七修正案在1913年确立参议员直选，其后参议院制度研究仍讨论其代表效果，支持当前政治制度决定产生多年后果的方向。  
  来源：<https://www.brookings.edu/wp-content/uploads/2016/06/Schiller_17th-Amendment_v7.pdf>；<https://bpb-us-w2.wpmucdn.com/voices.uchicago.edu/dist/2/3167/files/2023/04/foy-sutherland-moskowitz-and-rogowski.pdf>
- **#42** 「The greatest work that Theodore Roosevelt did for the United States, the great fact which will give his influe…」  
  判断：**正确**。NPS仍以全国公共土地和保护体系说明罗斯福遗产，表明其保护议题的公共影响持续到该代人之后。  
  来源：<https://www.nps.gov/thrb/learn/historyculture/trandthenpsystem.htm>；<https://www.nps.gov/thro/learn/historyculture/theodore-roosevelt-and-conservation.htm>
- **#46** 「The question of the conservation of our natural resources is not a simple question, but it requires, and will …」  
  判断：**正确**。Krutilla等保护经济学及其后环境成本收益研究显示经济分析成为持续发展的保护议题，符合愈需从经济基础思考的方向。  
  来源：<https://www.science.org/doi/10.1126/science.1073947>；<https://www.journals.uchicago.edu/doi/full/10.1086/718054>；<https://www.cambridge.org/core/journals/journal-of-the-history-of-economic-thought/article/abs/environmental-turn-in-natural-resource-economics-john-krutilla-and-conservation-reconsidered/A3741107606B6D773907B3BFF8B0046C>
- **#49** 「With a fair chance we can and will reclothe these denuded mountains with forests, and we ask for that chance.」  
  判断：**正确**。1925年林务局北落基山研究把苗木造林称为成熟可靠的方法，林务局历史又记载1933年至1930年代后期重新造林面积大增，支持西部山地有机会时恢复森林的实现方向。  
  来源：<https://research.fs.usda.gov/treesearch/48892>；<https://npshistory.com/publications/usfs/fs-628/chap2.htm>
- **#53** 「In the second great crisis, the Civil War, a part of our own people strove for an end which would have checked…」  
  判断：**正确**。CSIS的2025年分析认为美国并不接近内战，选源对当代风险的讨论也未记录一场新的美国内战，符合出版后窗口未重演该类战争的主结果。  
  来源：<https://www.csis.org/analysis/united-states-headed-toward-civil-war>；<https://journals.sagepub.com/doi/10.1177/00953997241244701>
- **#57** 「The conservation movement cannot be checked by the baseless charge that it will prevent development, or that e…」  
  判断：**正确**。NPS与保护运动历史显示运动在20世纪继续发展，未被“阻止开发”或煽动者指责所终止，符合不会被这类指控阻断的方向。  
  来源：<https://www.nps.gov/articles/000/american-conservation-in-the-twentieth-century.htm>；<https://uncpress.org/9781469680484/the-state-of-conservation/>
- **#65** 「If they resist, as doubtless they will, it will call for nerve, endurance, and sacrifice on the part of the pe…」  
  判断：**正确**。反托拉斯历史记载后续商业抵抗、政策反弹和法律收缩，符合特殊利益会抵抗并需长期努力的方向。  
  来源：<https://www.hbs.edu/ris/Publication%20Files/19-110_e21447ad-d98a-451f-8ef0-ba42209018e6.pdf>；<https://tobinproject.org/sites/default/files/assets/AAD%20Ch%204%20-%20Lamoreaux%20-%20Antimonopoly%20and%20State%20Regulation%20of%20Corporations.pdf>
- **#66** 「To these ends, many unfaithful public servants must be retired, much wise legislation must be framed and passe…」  
  判断：**正确**。竞选融资史与2026年研究记载多个时代的改革、规避和继续争议，支持反特殊利益政治斗争漫长且激烈的方向。  
  来源：<https://www.cambridge.org/core/journals/studies-in-american-political-development/article/democracy-under-siege-the-demise-of-successful-united-states-federal-campaign-finance-reform/2E63C93B8088255759FB88F7A3E0E7B2>

### 部分符合（21 条）

- **#6** 「As methods of agriculture improve and new dry-land crops are introduced, vast areas once considered unavailabl…」  
  判断：**部分符合**。大平原旱作确实推动半干旱区定居，但NBER记录蒙大拿1917—1921年旱灾中农场失败与弃耕，扩大耕作不等于持续形成繁荣家园。  
  来源：<https://plainshumanities.unl.edu/encyclopedia/doc/egp.ag.027.html>；<https://www.nber.org/papers/h0127>
- **#10** 「in the price of lumber which marked the opening of the present century is the beginning of a vastly greater an…」  
  判断：**部分符合**。林务局研究记录1964—1985年硬木名义价格近三倍，但多数树种涨幅被通胀抵消，只有部分树种实价上涨，支持涨价而不支持全面更快实价上升。  
  来源：<https://doi.org/10.2737/ne-rp-601>
- **#15** 「The railways, which have as yet failed entirely to develop a satisfactory substitute for the wooden tie (and m…」  
  判断：**部分符合**。1993年混凝土轨枕研究说明替代品可满足其测试条件，反对“必将继续无法开发满意替代品”的绝对判断；森林枯竭导致运输成本上涨的另一部分尚未触发。  
  来源：<https://udspace.udel.edu/items/35bc8f2c-1d30-472b-8485-4a04b17a3e83/full>；<https://railtec.illinois.edu/report/concrete-and-wood-tie-track-performance-through-150-million-gross-tons/>
- **#21** 「But it needs no argument to prove that this comparatively small area will be insufficient to meet the demand w…」  
  判断：**部分符合**。CRS说明国有林只是森林体系的一部分，不能把国有林面积等同全国供给；林务局历史同时明确记载曾预言的全国木材饥荒没有发生，所述必然灾难未兑现。  
  来源：<https://www.everycrsreport.com/files/19980310_98-233_db467d2c51cbb9c5a6cbc47de78dfd7c2643dd58.pdf>；<https://npshistory.com/publications/usfs/fs-518/chap10.htm>
- **#25** 「If we fail, the great interests, increasing their control of our natural resources, will thereby control the c…」  
  判断：**部分符合**。PNAS研究记录油气业政治捐款与议员投票的联系，支持资源利益与政治影响相连的一部分；不能据此证明保护运动整体失败并使人民权利全面转为财富特权。  
  来源：<https://www.pnas.org/doi/10.1073/pnas.1922175117>
- **#26** 「If we do not use it to protect ourselves now, we may be very sure that the trust will give hereafter small con…」  
  判断：**部分符合**。FTC历史研究记载控股公司能削弱州监管对利润的约束、会计信息向外部投资者隐瞒，符合利益冲突下忽视公众的一部分；其后联邦制度重构说明并非始终无保护。  
  来源：<https://thebhc.org/sites/default/files/beh/BEHprint/v019/p0017-p0021.pdf>；<https://thebhc.org/drupal10/web/sites/default/files/HausmanNeufeld_0.pdf>；<https://doi.org/10.7208/chicago/9780226399775.003.0007>
- **#27** 「After we have secured better crops, the next logical and inevitable step is to secure better business organiza…」  
  判断：**部分符合**。合作社历史资料记录1913—1915年约5424家、1924年约10170家，支持农业商业组织发展；但未验证“先改进作物”到“每个农民取得最优收益”的完整链条。  
  来源：<https://doi.org/10.22004/ag.econ.280538>；<http://nationalaglawcenter.org/wp-content/uploads/assets/bibarticles/unsigned_cooperativespart1.pdf>
- **#28** 「By so doing we shall avoid the difficulties and conflicts which will surely arise if we allow vested rights to…」  
  判断：**部分符合**。西部水权研究记载既得权利和公共控制之间持续冲突，支持困难冲突的方向，但城市购水和仍存在的公共制度并非完全脱离政府控制。  
  来源：<https://cawaterlibrary.net/wp-content/uploads/2019/09/SSRN-id874818.pdf>；<https://epress.lib.uts.edu.au/journals/index.php/ijrlp/article/download/2600/2830>
- **#29** 「The outgrowth of conservation, the inevitable result, is national efficiency.」  
  判断：**部分符合**。防护林研究有牲畜收益增加也有作物损失，农业保护政策评估又指出监测和目标问题，说明保护可改善部分效率而非必然提高全部国家效率。  
  来源：<https://le.uwpress.org/content/97/2/321>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC10837406/>
- **#30** 「In the great commercial struggle between nations which is eventually to determine the welfare of all, national…」  
  判断：**部分符合**。生产率研究支持效率与生活水平关联，Krugman则反对把国家福利视作国际零和商业竞赛，故效率重要但未证实这种竞争决定所有国家福利。  
  来源：<https://www.foreignaffairs.com/articles/1994-03-01/competitiveness-dangerous-obsession>；<https://www.foreignaffairs.com/productivity-everything-slaughter-wessel>
- **#37** 「Our rivers, if the forests on the watersheds are properly handled, will never cease to deliver power.」  
  判断：**部分符合**。PNNL记载干旱年水电仍有相当产出，ORNL研究同时发现长期容量因子下降，支持持续供能的一部分而非永久稳定保证。  
  来源：<https://www.nature.com/articles/s41467-024-49553-x>；<https://www.energy.gov/cmei/water/articles/study-finds-hydropower-provides-reliable-electricity-even-during-historic>
- **#41** 「The present strong movement to prevent the political control of public men, law-courts, and legislatures by gr…」  
  判断：**部分符合**。进步改革和公民动员确实发生，但选源记载跨年龄改革者和妇女参与，不能证明年轻男性在很短时间内独自决定人或金钱最终掌权。  
  来源：<https://www.whobuiltamerica.org/book/wba/part-i-monopoly-and-upheaval-1877-1914/radicals-and-reformers-in-the-progressive-era-1900-1914/>；<https://www.nationalcivicleague.org/ncr-article/the-reform-legacy-of-william-dudley-foulke/>
- **#43** 「The time is coming, and I do not believe it is far ahead, when it will not be respectable not to be interested…」  
  判断：**部分符合**。1920年代“civic slacker”及促投票运动显示不参与公共事务受到谴责，但低投票参与说明社会实际行为未普遍转变。  
  来源：<https://doi.org/10.2307/3092346>；<https://sites.socsci.uci.edu/~rdalton/archive/tocqueville.pdf>
- **#44** 「The success of the conservation movement in the United States depends in the end on the understanding the wome…」  
  判断：**部分符合**。妇女俱乐部历史记录妇女推动保护立法、说服议员，支持女性理解和参与的重要性；不能证明运动最终成功只取决于她们。  
  来源：<https://r830.cnr.berkeley.edu/cmerchant/articles/17.pdf>；<https://digitalcommons.lib.uconn.edu/dissertations/AAI9737425/>
- **#45** 「Fortunately there is no question as to our existing in honor, and little if any as to our continuing to exist …」  
  判断：**部分符合**。9/11委员会记载严重袭击及安全失误，显示美国继续存在但持续安全并非原文那样几无疑问。  
  来源：<https://www.9-11commission.gov/report/911Report_Exec.htm>
- **#47** 「As a result the Government has taken possession of that forest and will preserve it for all future generations…」  
  判断：**部分符合**。州公园材料记载1931年北林成为州立公园，1990年法律又记载邻接土地转移，支持公共保护实际延续；但1910年已由联邦接管的前提与后来的州保护并不相同。  
  来源：<https://www.parks.ca.gov/pages/551/files/CalaverasBigTreesFinalWebLayout101816.pdf>；<https://www.govinfo.gov/content/pkg/STATUTE-104/pdf/STATUTE-104-Pg993.pdf>
- **#52** 「With reasonable prudence and preparedness we need never fear another such attempt. If there be danger, it is n…」  
  判断：**部分符合**。1941年及2001年外部袭击说明外部危险并未消失，但9/11委员会记载准备不足，不能假定“合理谨慎和准备”的前提已满足再直接判错。  
  来源：<https://www.annualreviews.org/content/journals/10.1146/annurev.polisci.9.062404.170600>；<https://9-11commission.gov/report/911Report_Ch11.htm>
- **#61** 「Political leaders, Trust-bred and Trust-fed, find it harder and harder to conceal their actual character. The …」  
  判断：**部分符合**。1912年共和党分裂后丢失总统和国会，符合旧政治集团很快失势的一部分；St Louis Fed同时记载党领导仍挡下罗斯福提名，不能说所有特权领袖很快全部退出。  
  来源：<https://www.nytimes.com/1910/11/09/archives/democrats-control-the-house-by-40-early-returns-indicate-a.html>；<https://ashbrook.org/viewpoint/oped-busch-06-1910/>；<https://doi.org/10.1093/acprof:osobl/9780199936625.003.0007>；<https://www.stlouisfed.org/-/media/project/frbstl/stlouisfed/publications/review/pdfs/2025/may/theodore-roosevelt-election-of-1912-founding-of-federal-reserve.pdf>
- **#62** 「The demand of the people for political progress will not be denied.」  
  判断：**部分符合**。进步时代改革有实际推进，但童工和社会政策史也记载覆盖缺口与排除群体，不符合人民政治进步要求都不会被拒绝的绝对表达。  
  来源：<https://link.springer.com/article/10.1007/s11698-024-00287-2>；<https://gianlucarusso.github.io/cll_draft_may20.pdf>；<https://www.cambridge.org/core/journals/journal-of-policy-history/article/bias-of-american-federalism-the-limits-of-welfarestate-development-in-the-progressive-era/C5FEF299408EE0ABD02CBA9868F61777>
- **#64** 「If wisely they accept the inevitable, the adjustment will not be hard. It will do their business no manner of …」  
  判断：**部分符合**。工伤赔偿研究显示企业与工人均可从改革获益，另一研究也指出投入成本负担，支持可相容而非所有接受调整都轻松、无任何业务损害。  
  来源：<https://link.springer.com/article/10.1007/s11698-024-00287-2>；<https://doi.org/10.1017/s0022050705230188>
- **#67** 「The conservation of political liberty will take its proper place alongside the conservation of the means of li…」  
  判断：**部分符合**。保护与进步政治史支持公共利益和资源治理一起扩展，但专家行政与民主参与之间存在张力，未达到普通人长远福利始终至上的完整理想。  
  来源：<https://www.princeton.edu/~tleonard/papers/Expertise.pdf>；<https://api.pageplace.de/preview/DT0400.9780822972037_A49442503/preview-9780822972037_A49442503.pdf>

### 错误（6 条）

- **#9** 「The figures cited are, however, sufficiently reliable to make it certain that the United States has already cr…」  
  判断：**错误**。RFF记载1970—1977年木材净生长超过采伐53%、立木库存上升，并明确反对全国森林正被耗尽的说法；这与每个家庭都受严重全国木材荒冲击的主判断相反。  
  来源：<https://www.resources.org/archives/the-myth-of-timber-famine/>
- **#36** 「Our coal, the experts say, is likely to be exhausted during the next century, our natural gas and oil in this.」  
  判断：**错误**。EIA的2024年年末资料仍报告美国原油探明储量约460亿桶和天然气583.9万亿立方英尺，直接反对油气在20世纪耗尽的已届期部分。  
  来源：<https://www.eia.gov/naturalgas/crudeoilreserves/>；<https://www.eia.gov/naturalgas/crudeoilreserves/pdf/ARR_2024_TABLES_ALL.pdf>
- **#55** 「We have anthracite coal for but fifty years, and bituminous coal for less than two hundred.」  
  判断：**错误**。宾夕法尼亚历史生产表记录1960年及其后仍开采无烟煤，NMA的2024年资料亦列有可回收无烟煤储量，反对无烟煤只够到约1960年的判断。  
  来源：<https://files.dep.state.pa.us/Mining/BureauOfMiningPrograms/BMPPortalFiles/Annual_Reports/AnthraciteAnnualReports/2024/2024AnthraciteMiningActivities_HistoricalSummary.pdf>；<https://nma.org/wp-content/uploads/2024/11/coal_reserves_state_type_24.pdf>
- **#58** 「The special interests must get out of politics, or the American people will put them out of business. There is…」  
  判断：**错误**。当代公司政治参与和竞选融资研究记载企业继续经营并持续参与政治，构成“退出政治或被逐出商业，没有第三条路”的反例。  
  来源：<https://www.efmaefm.org/0EFMAMEETINGS/EFMA%20ANNUAL%20MEETINGS/2025-Greece/papers/Corporate%20Lobbying%20of%20Bureaucrats%20.pdf>；<https://businesslawreview.uchicago.edu/sites/default/files/2024-09/Fisch%20and%20Schwartz.pdf>
- **#60** 「Many of the old-style leaders regard the political truths which alone insure the progress of the Nation, and w…」  
  判断：**错误**。政策影响研究发现富裕者对政策有不成比例的影响，与公共福利而非金钱将“完全主导”不符；Bashir等对寡头解释的反驳限制了最强结论，却未证明金钱影响已经消失。  
  来源：<https://journals.sagepub.com/doi/full/10.1177/2053168015608896>；<https://onlinelibrary.wiley.com/doi/full/10.1111/ssqu.12791>；<https://onlinelibrary.wiley.com/doi/full/10.1002/polq.12577>
- **#68** 「The special interests must be put out of politics. I believe the young men will do it.」  
  判断：**错误**。2015年及2026年的竞选融资研究仍记载私人利益持续进入政治，反对年轻人将把特殊利益逐出政治的主结果；另一研究未发现企业价值收益，并不等于政治参与不存在。  
  来源：<https://daily.jstor.org/two-hundred-thirty-nine-years-money-politics/>；<https://www.cambridge.org/core/journals/studies-in-american-political-development/article/democracy-under-siege-the-demise-of-successful-united-states-federal-campaign-finance-reform/2E63C93B8088255759FB88F7A3E0E7B2>；<https://insight.kellogg.northwestern.edu/article/do-corporate-campaign-contributions-buy-influence>

### 暂无法判断（25 条）

- **#1** 「Unless we do, those who come after us will have to pay the price of misery, degradation, and failure for the p…」  
  判断：**暂无法判断**。1911年《Weeks Act》实施并启动东部森林购地与修复，因此“完全不保护资源”的前提没有按原样出现，不能用现实中的繁荣或贫困直接判真伪。  
  来源：<https://www.fws.gov/testimony/esa-50-destructive-cost-esa>；<https://www.usda.gov/about-usda/news/blog/continuing-conservation-legacy-centennial-weeks-act-1911>
- **#3** 「there is nothing more certain than that this country of ours will some day support double or triple or five ti…」  
  判断：**暂无法判断**。2023年人口普查局主方案预测2080年约3.7亿，和2006年Brookings文章预期的4亿路径不同；两者都是预测，不能代替4亿至10亿繁荣人口的实际结果。  
  来源：<https://www.brookings.edu/articles/america-at-300-million/>；<https://www.census.gov/newsroom/press-releases/2023/population-projections.html>
- **#4** 「Yet our coal supplies are so far from being inexhaustible that if the increasing rate of consumption shown by …」  
  判断：**暂无法判断**。无烟煤历史资料记载1917年产量达到高峰后行业转衰，1960年USGS仍报告大量煤储量；这不是原文“此前75年的消费增速持续”的实验。  
  来源：<https://pubs.usgs.gov/bul/1136/report.pdf>；<https://www.mininghistoryassociation.org/Journal/MHJ-v28-2021-Wolensky%20Northern%20PA%20Anthracite%20Coalfield.pdf>
- **#7** 「If we accept the larger estimate of the standing timber, 2,500 billion feet, and the larger estimate of the an…」  
  判断：**暂无法判断**。林务局资料显示1920年代生长量约为采伐一半，1940年代已大致平衡，1952年生长量超过采伐，不能把固定1910年生长和消费率延长一代人。  
  来源：<https://www.resources.org/archives/the-myth-of-timber-famine/>；<https://research.fs.usda.gov/download/treesearch/6241.pdf>
- **#12** 「What will happen when the forests fail? In the first place, the business of lumbering will disappear.」  
  判断：**暂无法判断**。EPA记载1907—2017年美国森林总面积净增约2500万英亩，未出现原文所设全国森林枯竭，不能据此判断届时伐木业会否消失。  
  来源：<https://phe.rockefeller.edu/publication/searching-leverage-conserve-forests/>；<https://cfpub.epa.gov/roe/indicator.cfm?i=48>
- **#13** 「All forms of building industries will suffer with it, and the occupants of houses, offices, and stores must pa…」  
  判断：**暂无法判断**。2021年木材涨价与建筑压力确有记录，但NC State专家将其主要归于需求、关税、运输和疫情供给冲击而非树木缺乏，不能当成森林枯竭情景兑现。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC8646330/>；<https://cnr.ncsu.edu/news/2021/05/lumber-shortage/>
- **#14** 「Mining will become vastly more expensive; and with the rise in the cost of mining there must follow a correspo…」  
  判断：**暂无法判断**。CDC存档记载20世纪中期煤矿以锚杆替代木支柱，说明技术路径改变；未找到全国森林枯竭使采矿成本和各矿价对应大涨的实际观察。  
  来源：<https://www.iied.org/sites/default/files/pdfs/migrate/G01035.pdf>；<https://stacks.cdc.gov/view/cdc/161477/cdc_161477_DS1.pdf>
- **#16** 「Water power for lighting, manufacturing, and transportation, and the movement of freight and passengers by inl…」  
  判断：**暂无法判断**。森林水文研究可支持植被与水质、水量相关，却没有同口径比较全国森林枯竭对水电、内河运输和蒸汽铁路的相对直接影响。  
  来源：<https://nap.nationalacademies.org/resource/12223/forest_hydrology_final.pdf>
- **#17** 「The cultivation of the soil, with or without irrigation, will be hampered by the increased cost of agricultura…」  
  判断：**暂无法判断**。1916年农业围栏材料谈到木材成本，地方博物馆又记载1916年起有钢筋混凝土及钢围栏柱；这些不能证明全国森林枯竭后农业必然受阻。  
  来源：<https://doi.org/10.5962/bhl.title.109123>；<https://mchistory.org/digital-exhibits/farming-in-the-great-corn-belt/the-cost-of-farming/fencing>
- **#18** 「Irrigated agriculture will suffer most of all, for the destruction of the forests means the loss of the waters…」  
  判断：**暂无法判断**。78项研究的综述发现森林扰动后水量可增、可减或不变，不足以证实灌溉农业会在全国森林毁坏情景下“受害最重”。  
  来源：<https://www.fs.usda.gov/rm/pubs_journals/2020/rmrs_2020_goeking_s001.pdf>；<https://nap.nationalacademies.org/resource/12223/forest_hydrology_final.pdf>
- **#19** 「With the rise in the cost of producing food, the cost of food itself will rise.」  
  判断：**暂无法判断**。食物生产成本与农产品价格资料不能建立原文森林枯竭—农业成本—食品价格这条具体条件链。  
  来源：<https://doi.org/10.22004/ag.econ.280436>
- **#20** 「Commerce in general will necessarily be affected by the difficulties of the primary industries upon which it d…」  
  判断：**暂无法判断**。RFF记录全国木材增长和库存改善，没有提供全国森林枯竭后基础行业困难再传到整体商业的观察。  
  来源：<https://research.fs.usda.gov/download/treesearch/5922.pdf>；<https://www.resources.org/archives/the-myth-of-timber-famine/>
- **#23** 「The nation that will lead the world will be a Nation of Homes.」  
  判断：**暂无法判断**。住房资料记录美国自有住房扩展，但“领导世界”及“Nation of Homes”均无原文阈值，不能凭住房率排位判断世界领导者。  
  来源：<https://www.nber.org/system/files/chapters/c12801/revisions/c12801.rev0.pdf>；<https://www.stlouisfed.org/on-the-economy/2018/june/national-homeownership-rates-negative-predictor-recovery>
- **#24** 「If we succeed, there will exist upon this continent a sane, strong people, living through the centuries in a l…」  
  判断：**暂无法判断**。GAO的土地资料描述公私土地分布，并不测量成功保护改革后数世纪内由“多数人而非少数人”持有土地。  
  来源：<https://www.govinfo.gov/content/pkg/GAOREPORTS-RCED-96-40/html/GAOREPORTS-RCED-96-40.htm>
- **#34** 「So we have allowed ourselves as a Nation, in the flush of the tremendous progress that we have made, to fail t…」  
  判断：**暂无法判断**。NBER的1936—2015年州级研究未发现资源对长期人均收入的同类决定效应，但州级资源禀赋不是全国浪费达到停顿阈值的检验。  
  来源：<https://www.nber.org/system/files/working_papers/w24695/w24695.pdf>；<https://collections.unu.edu/eserv/UNU%3A1020/rm1995-026.pdf>；<https://media.rff.org/documents/RFF-IB-00-tahvonen.pdf>
- **#35** 「Shall we go on in the same lines to the certain destruction of the prosperity which we have created, or shall …」  
  判断：**暂无法判断**。保护政策评估记载实际存在保护项目，不能把现实路径当成原文“继续同样破坏而不改变”的反事实路径。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC10837406/>；<https://www.journals.uchicago.edu/doi/10.1086/726154>
- **#38** 「Under our form of civilization, if a few men ever succeed in controlling the sources of power, they will event…」  
  判断：**暂无法判断**。控股公司历史记载1929年超过八成电力发电受其控制，但这不等于少数人控制全部能源，更不证明继而控制所有工业。  
  来源：<https://www.justice.gov/atr/electricity-restructuring-what-has-worked-what-has-not-and-what-next>；<https://doi.org/10.7208/chicago/9780226399775.003.0006>
- **#39** 「If they succeed in controlling all industry, they will necessarily control the country.」  
  判断：**暂无法判断**。钢铁集中与政治影响研究属于具体行业，不能证明少数人先控制全部工业再控制整个国家的条件链。  
  来源：<https://www.cambridge.org/core/journals/studies-in-american-political-development/article/abs/industrial-concentration-sectional-competition-and-antitrust-politics-in-america-18801980/72E74960EA21112D020A9AD23C8F16E1>；<https://www.anderson.ucla.edu/sites/default/files/document/2024-11/2024-piep-market_power_24nov24.pdf>
- **#48** 「There are many men who believe, and who will always believe, in the divine right of money to rule.」  
  判断：**暂无法判断**。商业政治参与资料只能说明行为和利益，不能直接证明总有人持有“金钱天授权利统治”的特定信念。  
  来源：<https://onlinelibrary.wiley.com/doi/full/10.1111/spsr.12164>；<https://www.annualreviews.org/content/journals/10.1146/annurev-polisci-051921-102505>
- **#50** 「If the Forest Service can not tell what it is doing the time will come when there will be nothing to tell.」  
  判断：**暂无法判断**。宣传史记载国会限制宣传与林务局仍进行传播的斗争，GAO亦有后来宣传材料，未出现完全不能告知公众的情景。  
  来源：<https://doi.org/10.1080/07343468609507972>；<https://www.gao.gov/assets/b-302992.pdf>
- **#51** 「Since the Forest Service called public attention to the rapid absorption of the water-power sites and the thre…」  
  判断：**暂无法判断**。林务局阿拉斯加历史明确记载出版后国会议员批评、削减拨款或转交林地的提案，支持攻击持续，但未提供可比较的增长速度序列。  
  来源：<https://ir-api.ua.edu/api/core/bitstreams/2df132d4-5ee4-41c2-bd8c-0fda93fbb0e2/content>；<https://www.nytimes.com/1910/01/08/archives/pinchot-ousted-party-war-on-president-dismisses-forester-censuring.html>；<https://npshistory.com/publications/usfs/region/10/history/chap4.htm>
- **#54** 「We have timber for less than thirty years at the present rate of cutting.」  
  判断：**暂无法判断**。林业历史与资源统计显示采伐及生长路径改变，全国木材荒未按早期想象发生，不能测试冻结“当前砍伐率”的30年算式。  
  来源：<https://www.fs.usda.gov/research/docs/rpa/pre-1989/1941%20SAWTIMBER%20RESOURCE%20OF%20THE%20US%201630-1930.pdf>；<https://npshistory.com/publications/usfs/fs-518/chap10.htm>；<https://doi.org/10.5962/t.170782>
- **#56** 「For, if we do not take action to conserve the Nation's natural resources, and that soon, our descendants will …」  
  判断：**暂无法判断**。1911年《Weeks Act》及其后购地保护表明很快确有资源保护行动，不能把“如不尽快行动”的条件视为已满足。  
  来源：<https://www.tandfonline.com/doi/abs/10.1080/02646811.2012.11435298>；<https://foresthistory.org/wp-content/uploads/2016/12/2011_Future_Land_Conservation_Policy_weeks-act.pdf>
- **#59** 「As soon as these men have won their battle and consolidated their victory, confidence in Congress will return.」  
  判断：**暂无法判断**。PBS记载Wilson时期改革议程和立法胜利，而Gallup长期信任资料不能单独识别原文人民代表已经“赢得并巩固胜利”的起点。  
  来源：<https://news.gallup.com/poll/171710/public-faith-congress-falls-again-hits-historic-low.aspx>；<https://direct.mit.edu/daed/article/151/4/43/113715/Fifty-Years-of-Declining-Confidence-amp-Increasing>；<https://www.pbs.org/wgbh/americanexperience/features/wilson-legislative-victories/>
- **#63** 「If they resist, both the interests and the people will suffer.」  
  判断：**暂无法判断**。工伤赔偿研究记载1911—1926年的制度争执、受伤工人补偿方式变化，但未找到把企业与民众双方实际损失归于抵抗改革本身的证据。  
  来源：<https://www.nber.org/system/files/chapters/c6578/c6578.pdf>；<https://www.ebhsoc.org/journal/index.php/ebhs/article/download/317/483/1123>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 原代码已从73条原始输出排除5条；保留68条全部核验，ASSESS未额外排除，无语义去重 |

## 文件

- 本文：`cases/pinchot-fight-for-conservation-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/pinchot-fight-for-conservation-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/pinchot-fight-for-conservation-v5/audit/manual_review_2026-11-15.py`
局限：只核实出版年，源快照的SOURCE_COMMIT标85e6da1但无.git，无法独立git log确认；未改toolkit。原TXT/全文计划在工作目录，交付包不含全书。


context清空后，用原toolkit.extraction_provenance函数重绑source-fields receipt（共204条历史/派生记录，实时claims为68条），未改quote、位置、类型、归属或判分；旧新receipt仅保留hash和字段元数据。随后重新apply→check→report，并逐条validate_extraction_provenance及原确定性抽取回放通过。
