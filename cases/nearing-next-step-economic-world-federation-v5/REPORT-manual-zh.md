# 斯科特·尼尔林《下一步：经济世界联邦计划》：出版后预测人工核查

- 案例目录：`cases/nearing-next-step-economic-world-federation-v5/`
- 出版日期：1922
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

原TXT按3500/600逐块全文审读；85e6da1工具确定性处理，只人工替换模型调用，所有context清空。证据实际来自Exa检索与Exa contents公开页存档；不是WebSearch/WebFetch，未调用DeepSeek。实际导入44候选，其中35可核验进入完整PLAN/SELECT/ASSESS/SEMANTIC REVIEW，9条unclear保留不评分；核验另将1条纯制度方案按normative排除，未按主题语义去重。先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 35 条，剔除非预测 1 条，计入 **34 条预测**，其中 **23 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 12 |
| 趋势符合 | 0 |
| 部分符合 | 9 |
| 错误 | 2 |
| 暂无法判断 | 11 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **52.2%**（12/23） |
| 加权胜率 | **71.7%** |
| 错误率 | **8.7%**（2/23） |
| 未定占比（暂无法判断/预测） | 32.4%（11/34） |

## 总体评价

境外资源依赖、国联局限、全球性议题与部分英美竞争判断有后发事实支持；全球生产者社会等终局多保留未定。科学规划和文化参与只在实际部分成立时计部分符合；没有凭未被反驳给趋势分。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（12 条）

- **#1** 「Manufacturing and transport depend for their maintenance upon minerals and fuels, and those countries that pro…」  
  判断：**正确**。资源面板直接确认各类材料对世界市场的依赖增加，矿物和化石燃料尤为突出；美国长期进口来源变化提供了对应实例。  
  来源：<https://www.resourcepanel.org/reports/international-trade-resources>；<https://pubs.usgs.gov/fs/2015/3082/fs20153082.pdf>；<https://thebhc.org/node/97340>
- **#3** 「With economic life established on a world scale, it is inevitable that the range of men's thoughts and the lin…」  
  判断：**正确**。历史研究确认跨国社团生活与全球互联意识的发展；跨地域联合的社会运动也构成出版后的实际观察。  
  来源：<https://www.cambridge.org/core/journals/journal-of-global-history/article/editorial-the-roots-of-global-civil-society-and-the-interwar-moment/6B75786C408182481525AAAE55A76D49>；<https://www.ipinst.org/wp-content/uploads/1970/01/pdfs_lupel_globalizations2_1.pdf>
- **#4** 「Political, sectional and provincial in its point of view, the League, as a means of world organization, was de…」  
  判断：**正确**。联合国档案明确评述国联未完成使命，且未能遏制导致世界大战的国际秩序恶化，符合其作为世界组织手段失败的主结论。  
  来源：<https://www.ungeneva.org/en/about/league-of-nations/transition>；<https://www.ungeneva.org/en/about/league-of-nations/at-work>
- **#6** 「Soviet Russia is and for a time must remain a source of international bitterness among the great capitalist na…」  
  判断：**正确**。国会图书馆记录出版后美苏仍长期缺乏正式外交关系，并存在与西方的深刻猜疑和敌意；符合仍将持续一段时期的判断。  
  来源：<https://www.loc.gov/exhibits/archives/sovi.html>；<https://history.state.gov/milestones/1921-1936/ussr>
- **#9** 「Before the war the centre of the world's economic power was Great Britain. To-day the economic centre has shif…」  
  判断：**正确**。历史研究明确确认英美在出版后继续展开经济政治霸权竞争，并以美国霸权清晰确立为结果，符合一方胜出的主结论。  
  来源：<https://www.tandfonline.com/doi/abs/10.1111/j.1931-0846.2009.tb00439.x>；<https://www.hoover.org/research/safe-passage-transition-british-american-hegemony>
- **#14** 「It is so vital a part of the social life, and it yields itself so readily to structural co-ordination that the…」  
  判断：**正确**。康托罗维奇自述该领域吸引有才华的年轻科学家、培养数学经济交叉人才并建立专门实验室，符合杰出结构与数学人才转入经济组织问题的主要方向。  
  来源：<https://www.nobelprize.org/prizes/economic-sciences/1975/kantorovich/biographical/>；<https://cooperative-individualism.org/stabile-donald_veblen-and-the-political-economy-of-the-engineer-1986-jan.pdf>
- **#22** 「The economic, social and cultural life of civilization has passed beyond national boundaries. Until this fact …」  
  判断：**正确**。国联缺少主要大国支持、解决大国争端的能力有限，随后仍发生世界大战，符合广域组织尚不足时冲突灾难继续的观察。  
  来源：<https://www.nationalww2museum.org/war/articles/world-war-ii-and-founding-united-nations>；<https://www.ungeneva.org/en/about/league-of-nations/at-work>
- **#24** 「A number of economic questions, such as the control of resources and of transport, have already passed beyond …」  
  判断：**正确**。环境会议及跨国环境、健康条约的发展表明资源和运输之外的新议题进入世界治理，符合其他问题上升为世界性问题。  
  来源：<https://www.cambridge.org/core/services/aop-cambridge-core/content/view/894F702B0DAFE4A9E9610F1DECEFCEB0/9781009177801pre1_i-iv.pdf/stockholm-and-the-rise-of-global-environmental-governance.pdf>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC6642604/>
- **#25** 「a story of limited, localized resources upon which the expanding industries will be compelled to make ever inc…」  
  判断：**正确**。环境署明确记录全球材料资源使用持续增长；物质足迹研究还指出部分看似脱钩的成绩被高估，符合工业对资源不断增加需求的方向。  
  来源：<https://www.unep.org/en/news-and-stories/speech/global-resources-outlook-press-statement-unep-executive-director>；<https://doi.org/10.1073/pnas.1220362110>
- **#26** 「there must ensue a ferocious struggle among the nations to secure and hold the resource key to economic advant…」  
  判断：**正确**。日本在石油禁运压力下决定侵入东南亚并夺取荷属东印度，构成直接以武力争取关键资源的后发实例，符合国家间激烈资源争夺会出现。  
  来源：<https://press.armywarcollege.edu/cgi/viewcontent.cgi?article=1632&context=monographs>；<https://academic.oup.com/jpr/article/51/2/227/8365607>；<https://www.belfercenter.org/publication/oil-conflict-and-us-national-interests>
- **#27** 「Its next stage will include a struggle between Great Britain and the United States for the possession of the w…」  
  判断：**正确**。历史研究确认出版后英美仍争夺全球石油供应，美国随后参与中东油田权益安排，符合下一阶段包括英美石油争夺的判断。  
  来源：<https://www.tandfonline.com/doi/abs/10.1111/j.1931-0846.2009.tb00439.x>；<https://history.state.gov/milestones/1921-1936/red-line>；<https://digitalcommons.odu.edu/cgi/viewcontent.cgi?article=1123&context=history_etds>
- **#28** 「Still, the jail, the gallows and the lynching-bee have not kept experimenters quiet in the past, and they will…」  
  判断：**正确**。苏联异议群体在持续管制下仍保持活动，后来人权诉求还进入放宽限制的改革，符合镇压未能让实验者整体沉默的主要结果。  
  来源：<https://www.wilsoncenter.org/publication/the-evolution-soviet-policies-towards-dissidents>；<https://www.loc.gov/exhibits/archives/intn.html>

### 部分符合（9 条）

- **#7** 「As the resources of the earth become better known, and their extent more definitely established, there is ever…」  
  判断：**部分符合**。战时与工业社会对资源的大量需求以及境外资源争夺确有记录，需求增强这一子项成立；材料不足以确认控制行动总体越来越具侵略性。  
  来源：<https://doi.org/10.1017/chol9780521837194.024>；<https://academic.oup.com/jpr/article/51/2/227/8365607>
- **#8** 「The United States will be an object of envy, jealousy, suspicion, cajolery and hatred in the eyes of those peo…」  
  判断：**部分符合**。经济竞争者、债权人与现代性范本的美国确成为欧洲希望和恐惧的焦点，实力也成为摩擦来源。嫉妒、拉拢、仇恨等整套心理及其统一财富动因并未全部获证。  
  来源：<https://doi.org/10.1017/cbo9781139016872.004>；<https://www.pewresearch.org/global/2002/04/29/international-surveys-what-we-are-finding/>
- **#10** 「scientist and the engineer upon whose shoulders will rest the burden of rebuilding the new society, tighten th…」  
  判断：**部分符合**。科学家实际进入经济规划并形成专门机构，规划实践也影响社会重建；这一专业参与子项成立。但承担整个新社会重建的主要责任并未获证，技治运动还有明显失败。  
  来源：<https://www.nobelprize.org/prizes/economic-sciences/1975/kantorovich/biographical/>；<https://discovery.ucl.ac.uk/id/eprint/10087411/3/Hebbert_Planning%20Knowledge%20and%20Technocracy%202019%20final%20ms.pdf>；<https://www.cambridge.org/core/journals/contemporary-european-history/article/technocratic-moment-in-1930s-belgium-governmental-planning-between-democracy-and-fascism/FE2458D091F25098BB79EEA61E3B6008>
- **#12** 「While the owning class continues, without labor, to derive an income from the labor of the workers, the former…」  
  判断：**部分符合**。智利工人实际要求工作场所社会化，反对业主权利的这一子项成立；美国工会也被描述为在资本主义内争取待遇，而非一概否定体系。  
  来源：<https://staging.jacobin.com/2022/08/workers-means-of-production-chile-allende-yarur-textile-factory-unity-popular>；<https://www.law.georgetown.edu/denny-center/blog/labor-unions-capitalism/>
- **#13** 「Economic life has been haphazard in the past. In the future it will be one of the most scientifically built of…」  
  判断：**部分符合**。运筹学确在咨询公司和研究机构建立，显示经济管理中的科学设计已形成实践；但其专业权限受到限制，不能确认整个经济已是最科学构建的制度之一。  
  来源：<https://www.cambridge.org/core/journals/business-history-review/article/abs/operations-research-visavis-management-at-arthur-d-little-and-the-massachusetts-institute-of-technology-in-the-1950s/ECB3FAAE411361ED5CF2E39AEAC5B92E>；<https://pubsonline.informs.org/do/10.1287/orms.2015.03.08/full/>
- **#15** 「As time goes on, the nature of the economic system may be greatly modified, and its structure simplified corre…」  
  判断：**部分符合**。跨国企业确发生广泛组织结构改变并趋于扁平化，经济组织改变这一子项有实际依据；生产分散和复杂网络仍存在，未证经济体系整体相应简化。  
  来源：<https://link.springer.com/article/10.1007/s11575-025-00585-5>；<https://www.wto.org/english/res_e/booksp_e/gvcs_report_2017_chapter1.pdf>
- **#18** 「The life of local economic units will be carried on to-morrow very much as it is carried on to-day by the mass…」  
  判断：**部分符合**。出版后的北卡罗来纳仍有大量人口依靠地方农业生计，这一局部延续子项成立；失地、佃农增加又显示生活并非完全不变。  
  来源：<https://www.ncanchor.org/anchor/how-twenties-roared-north>
- **#31** 「Social science, still in its infancy, has ahead of it decades of advancement before it attains a position corr…」  
  判断：**部分符合**。社会科学后续确有理论、实证和方法进展，地位、支持及现实预测仍有局限；进步并持续面临困难的子项成立。  
  来源：<https://thecanadianencyclopedia.ca/en/article/social-science>；<https://www.cell.com/trends/cognitive-sciences/abstract/S1364-6613(23)00263-2>
- **#35** 「The development of modern industry, with its facility in the production of livelihood, promises a time, and th…」  
  判断：**部分符合**。战间期服装工人组成业余剧团并接受艺术训练，确有普通劳动者参与文化创造的局部后发实践；未证机会很快成为世界人人共有。  
  来源：<https://ilgwu.ilr.cornell.edu/announcements/28.html>；<https://pure-oai.bham.ac.uk/ws/portalfiles/portal/74401469/West_within_the_reach_of_all_bringing_art_to_the_people_in_interwar_Britain_Modernist_Cultures_2019.pdf>；<https://www.unesco.org/en/culture/global-report/global-report-cultural-policies/chapter-1>

### 错误（2 条）

- **#19** 「The great accumulations of economic power that were made in this way during the past generation are now being …」  
  判断：**错误**。公司治理史明确记录大型公司兴起时家族公司衰落、家族资本主义转向经理资本主义，与经济领导权趋于世袭的主方向相反。  
  来源：<https://doi.org/10.1017/cbo9780511488696.009>；<https://www.cambridge.org/core/journals/law-and-society-review/article/abs/law-in-the-development-of-dynastic-families-among-american-business-elites-the-domestication-of-capital-and-the-capitalization-of-family/7C59CFCC9428554779B2CB6DE6C0F4BC>
- **#34** 「The present age has not as yet developed its culture, and it seems now as though capitalism, with its heritage…」  
  判断：**错误**。后发艺术批评明确讨论资本主义相关的后现代审美形式，文化史也记录大众文化及象征交流的新理解，反驳其来不及形成可辨识自身文化的先后判断。  
  来源：<https://newleftreview.org/issues/i152/articles/terry-eagleton-capitalism-modernism-and-postmodernism.pdf>；<https://www.pennpress.org/9780812243956/consuming-pleasures/>

### 暂无法判断（11 条）

- **#2** 「The principal deposits of iron, coal, copper and petroleum are apparently in the Western Hemisphere, and parti…」  
  判断：**暂无法判断**。资源研究显示储量估计会随新发现改变，澳大利亚也有重要资源储量；这不能证明原前提成立时世界必然依赖美洲。  
  来源：<https://collections.unu.edu/eserv/UNU%3A1020/rm1995-026.pdf>；<https://www.ga.gov.au/aimr2025/world-rankings>
- **#5** 「Reasoning, foresight and experience will convince the people of the world that a benefit to one is a benefit t…」  
  判断：**暂无法判断**。援助调查同时观察到互利取向和国家利益取向的转变；跨国零和信念研究也不是世界人民已接受一荣俱荣的证明。  
  来源：<https://developmentengagementlab.org/what-is-aid-for-how-public-views-are-evolving/>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC6162082/>
- **#11** 「When this point is reached--when the costs of expansion beyond boundary lines of a nation are so great that th…」  
  判断：**暂无法判断**。新政与战后制度调整表明资本主义能够改变组织方式和缓和危机；现有材料没有证明扩张成本已触发全球制度终结。  
  来源：<https://econweb.umd.edu/~wallis/MyPapers/wallis_did_the_new_deal_save_democracy_and_capitalism.pdf>；<https://aeon.co/essays/postwar-prosperity-depended-on-a-truce-between-capitalism-and-democracy>
- **#17** 「Ultimately, the economic units of which society is composed will differ completely from those now existing.」  
  判断：**暂无法判断**。平台经济带来新组织形式，但研究同时记录旧生产者通过合作竞争适应新平台；新旧共存不等于所有经济单位最终完全不同。  
  来源：<https://link.springer.com/article/10.1007/s11187-021-00561-x>；<https://openaccess.city.ac.uk/id/eprint/25321/11/1-s2.0-S0148296320308894-main.pdf>
- **#20** 「Under any form of society that can be foreseen in the immediate future, the need of close co-operation between…」  
  判断：**暂无法判断**。出版后近期国际会议确认相互依赖与协调需要，但未提供该需要相较出版时增加的同口径观察；合作失败也不等于合作需要减少或增加。  
  来源：<https://history.state.gov/historicaldocuments/frus1927v01/d203>；<https://press.umich.edu/pdf/0472113054-ch4.pdf>
- **#21** 「The logic of economic development is compelling men to turn from the owners' society of the present day to a p…」  
  判断：**暂无法判断**。合作社、员工收购等真实存在，但现代市场中多数员工控制企业仍然罕见，混合经济也继续包含私人所有和国家所有。局部形式不足以证实全球业主社会已转向生产者社会。  
  来源：<https://www.ilo.org/sites/default/files/wcmsp5/groups/public/@ed_emp/@emp_ent/@coop/documents/publication/wcms_705803.pdf>；<https://www.bu.edu/eci/files/2021/08/Comparative-Economic-Systems.pdf>；<https://blogs.lse.ac.uk/businessreview/2026/01/19/if-worker-co-operatives-work-why-arent-there-more-of-them/>
- **#23** 「owning class society is coming to an end--falling of its own weight.」  
  判断：**暂无法判断**。后续资料仍将资本主义描述为广泛存在的生产方式，而非全球有产阶级社会已经终结；但原句没有给出最终终点。  
  来源：<https://www.foreignaffairs.com/articles/united-states/2019-12-10/clash-capitalisms>；<https://www.imf.org/en/publications/fandd/issues/series/back-to-basics/capitalism>
- **#29** 「recent experiences with the war, and with the present post-war plight of Europe suggest that the capitalist ex…」  
  判断：**暂无法判断**。大萧条、改革以及战后协调缓和危机均有记录，但灾难性经济危机不等于整个资本主义实验最终失败。作者保留了成功整顿的真实例外，却未给出异常成功的可操作阈值。  
  来源：<https://www.federalreservehistory.org/essays/great-depression>；<https://econweb.umd.edu/~wallis/MyPapers/wallis_did_the_new_deal_save_democracy_and_capitalism.pdf>
- **#30** 「war, revolution and other disasters which inevitably destroy some portion of society, and which, in the end wi…」  
  判断：**暂无法判断**。战争预防已有研究框架，预警也有一定作用；这些资料没有给出战争革命与疾病饥荒预防能力等同的比较。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC10794494/>；<https://www.iss.europa.eu/publications/briefs/power-and-limits-data-peace>
- **#32** 「If there is to be an organization of economic society that will function successfully and autonomously, the kn…」  
  判断：**暂无法判断**。经济知识理解与参与存在障碍，所有权网络研究也能揭示公司控制，但这些并不直接检验整个经济由业主个人意愿支配。研究还强调国家所有权和间接控制，不能简化为私人业主随意决定。  
  来源：<https://www.ecnmy.org/research/report-2017/>；<https://feps-europe.eu/wp-content/uploads/2024/06/Building-Economic-Democracy-in-Europe-WEB-Single-Pages.pdf>；<https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0237862>
- **#33** 「Since it is apparent that the organized producers will be the dominant element in the new society,」  
  判断：**暂无法判断**。南斯拉夫工人自我管理是局部历史实践，后续材料仍描述资本所有者取得大部分增长收益和员工控制企业罕见，不能证明有组织生产者已主导全球新社会。  
  来源：<https://transversal.at/transversal/0805/kuljic/en>；<https://www.iza.org/en/publications/dp/13238/towards-economic-democracy-and-social-justice-profit-sharing-co-determination-and-employee-ownership>；<https://blogs.lse.ac.uk/businessreview/2026/01/19/if-worker-co-operatives-work-why-arent-there-more-of-them/>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| 16 | Like every social structure, the economi… | normative | 该段说明拟议新社会要有效运作所需的组织构造，前后均在列举有效单位的必要特征与可建议的层级，属于制度方案而非独立实现承诺。 |

## 文件

- 本文：`cases/nearing-next-step-economic-world-federation-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/nearing-next-step-economic-world-federation-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/nearing-next-step-economic-world-federation-v5/audit/manual_review_2026-11-15.py`
canonical报告中的候选35为可核验层，不是全部44个导入候选。#16方案边界、#19领导权与财富继承、#34文化定义及密集同题独立句的敏感性见PR_BODY。
