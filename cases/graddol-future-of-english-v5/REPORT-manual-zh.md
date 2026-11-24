# David Graddol《英语的未来？——21世纪英语受欢迎程度预测指南》（The Future of English? A guide to forecasting the popularity of the English language in the 21st century）：出版后预测人工核查

- 案例目录：`cases/graddol-future-of-english-v5/`
- 出版日期：The British Council 1997 年首版（数字版 © 1997, 2000，The English Company (UK) Ltd 制作；PDF 元数据 CreationDate 2000-12-12，内容为 1997 年首版）。**按 1997 起算**。观察窗口为 1997 至 2026-11-15。书中引用的 Hooke 预测模型、人口与经济预测多以 2010、2025、2050 为终点。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

按仓库 DeepSeek 管线手工代替模型调用：以 `pdftotext -enc UTF-8` 生成全书 TXT（PDF sha256 `0810309d…`，TXT sha256 `38f54bbc…`，392,380 字符；原 PDF 为多栏排版，部分页面栏文交错），`prepare_book.split_text(3500, 600)` 得到 114 个 chunk，逐块通读，按 DISCOVER_PROMPT_V5 逐块手写 JSON，未做关键词筛选。经 `validate_chunk_predictions` 与 `claims_from_results` 导入 114 条候选：94 条可核验预测（`claim_type=forecast`，`resolvable=true`），20 条为书中转述的第三方观点（英国文化协会新闻稿、Wells、美国人口普查局、UNDP、TeleGeography、Krauss 等）按规则降为 unclear、不计分。引文均为 TXT 逐字片段，记录字符偏移与 TXT/PDF sha256。全文未入库。本稿由助手逐条对照书中原文，并依据 1997 至 2026-11-15 窗口内经 Exa 检索并实际存档（`data/sources/`，sha256 见 `data/evidence.jsonl`）的公开来源人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 94 条，剔除非预测 0 条，计入 **94 条预测**，其中 **85 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 39 |
| 趋势符合 | 22 |
| 部分符合 | 17 |
| 错误 | 7 |
| 暂无法判断 | 9 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **45.9%**（39/85） |
| 加权胜率 | **75.3%** |
| 错误率 | **8.2%**（7/85） |
| 未定占比（暂无法判断/预测） | 9.6%（9/94） |

## 总体评价

Graddol 这本 1997 年的小册子以“英语地位并非高枕无忧”为主线，判断大体经得起检验，但最激进的“英语相对地位下降”论点只说中了一半。说中的主要是结构性趋势：OECD/西方经济比重被亚洲侵蚀、服务业就业扩张、美国网民占比 1997 年后迅速下降、非英语网络内容大量涌现、卫星电视走向本地语言、印尼语取代地方语言、英国等母语国英语教学市场承压、伦敦纽约仍是枢纽、英语仍是唯一全球通用语。只对一部分的多是“英语相对重要性下降”一类：英语在网络内容中的份额确实下降，但在科研、商务和学习需求上英语地位反而更强；“语言寡头取代英语霸权”没有发生。明确错了的集中在几个具体判断：中国经济特区移民会扩大粤语、吴语等地区通用语（实际是普通话扩张）；德语在中东欧随欧盟扩大而上升；Hooke 模型对 2010 年学生需求排名（印尼语第四）和 2025 年 ESL 需求增至六倍；南美贸易区十年内并入北美自贸区。以 2050 年为终点的经济与服务业预测尚未到期。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（39 条）

- **#1** 「Although English is unlikely to be displaced as the world’s most important language」  
  判断：**正确**。截至2026年英语仍是世界最主要的全球通用语（英国文化协会称可预见未来仍将主导；约15亿人使用），未被取代。  
  来源：<https://www.britishcouncil.org/voices-magazine/our-rapidly-changing-world-what-future-english-language>；<https://www.newyorker.com/magazine/2024/12/30/how-much-does-our-language-shape-our-thinking>
- **#2** 「There is no imminent danger to the English language, nor to its global popularity」  
  判断：**正确**。英语学习者规模持续在15亿左右的高位，英国文化协会认为英语在可预见未来仍保持主导，全球受欢迎程度未见迫近危险。  
  来源：<https://esldirect.com/global-english-language-learning-trends-statistics/>；<https://www.britishcouncil.org/voices-magazine/our-rapidly-changing-world-what-future-english-language>
- **#3** 「the economic dominance of OECD countries – which has helped circulate English in the new market economies of t…」  
  判断：**正确**。OECD《全球发展展望2014》：非OECD国家在世界GDP(PPP)中的份额于2010年超过OECD国家，主因中印等亚洲经济体快速增长。  
  来源：<https://www.oecd.org/content/dam/oecd/en/publications/reports/2014/07/perspectives-on-global-development-2014_g1g40865/persp_glob_dev-2014-en.pdf>；<https://www.oecd.org/en/publications/perspectives-on-global-development-2019_persp_glob_dev-2019-en/full-report/component-7.html>
- **#18** 「Its use in international forums is unlikely to disappear entirely」  
  判断：**正确**。法语至今仍是联合国六种官方语言之一，并与英语同为秘书处工作语言，未在国际论坛中消失。  
  来源：<https://www.un.org/sg/en/multilingualism/index.shtml>；<https://www.ungeneva.org/en/about/director-general/multilingualism>
- **#19** 「In the 21st century there is likely to be considerable growth in English language publishing in countries wher…」  
  判断：**正确**。印度已成为世界第二/第三大英语图书市场且被称为"蓬勃发展"；尼日利亚独立英语出版亦增长，二语国家英语出版大幅增长成立。  
  来源：<https://www.thenationalnews.com/world/asia/publishers-get-a-measure-of-india-s-booming-english-book-market-1.387386>；<https://www.independentpublishersguild.com/Common/Uploaded%20files/IPG%20document%20library/IPG%20email%20documents/TheIPGIndiaReport.pdf>
- **#21** 「These countries can be regarded as in the process of shifting towards L2 status.」  
  判断：**正确**。瑞典等北欧国家高等教育广泛使用英语；荷兰英语授课学位比例高到政府2024年出台限制，说明英语已深入国内使用，向二语地位转变成立。  
  来源：<https://doi.org/10.1111/weng.12650>；<https://monitor.icef.com/2024/10/dutch-government-set-to-restrict-english-taught-degrees/>
- **#22** 「more and more people in the world will learn languages in the uppermost layer as a result of improved educatio…」  
  判断：**正确**。英国文化协会估计2000年约10亿人学英语，后续估计约15亿人，学习顶层语言英语的人越来越多。  
  来源：<https://teachingenglishwithoxford.oup.com/2013/05/09/ten-things-you-might-not-have-known-about-the-english-language/>；<https://www.theteflacademy.com/blog/english-language-teaching-statistics/>
- **#23** 「with the position of French declining and English becoming more clearly the global lingua franca」  
  判断：**正确**。欧盟机构中法语原有的通用语特权地位丧失，如今欧洲理事会与欧委会90%以上文件使用英语，法语作为国际通用语地位下降，英语成为更明确的全球通用语。  
  来源：<https://blogs.lse.ac.uk/politicsandpolicy/france-has-almost-entirely-failed-in-its-strategy-to-prevent-english-taking-over-as-the-lingua-franca-of-the-eu/>；<https://www.europarl.europa.eu/doceo/document/E-9-2023-000921_EN.html>
- **#25** 「By the year 2000, it is likely that users in the US will be outnumbered by users elsewhere.」  
  判断：**正确**。1998年美国占全球网民约55%，2000年降至约45%（美国互联网委员会），即到2000年美国以外网民已超过美国网民。  
  来源：<https://www.casinocitytimes.com/news/article/us-web-dominance-waning-report-says-117479>；<https://www.irishtimes.com/business/the-internet-reaches-turning-point-as-users-go-international-1.295106>；<https://www.digi.no/juss-og-samfunn/nesten-100-millioner-nettbrukere/3190281>
- **#26** 「In Europe, Germany is expected to be the largest Internet user.」  
  判断：**正确**。2002年Telecompaper报道德国已成为欧洲互联网用户最多的国家。  
  来源：<https://www.telecompaper.com/news/germany-has-the-most-internet-users-in-europe--299799>；<https://www.computerwoche.de/article/2694241/11-3-millionen-deutsche-surfen-im-web.html>
- **#27** 「the proportion of the global Internet population based in the US is expected to increase during 1997, but then…」  
  判断：**正确**。1998年初美国占全球网民54.7%，2000年约45%，2001年约40%，美国占比在1997年后下降。  
  来源：<https://www.digi.no/juss-og-samfunn/nesten-100-millioner-nettbrukere/3190281>；<https://www.ipsos.com/en-us/internet-moves-post-revolutionary-phase-americas-share-global-users-declines-ipsos-reid-study>
- **#28** 「the proportion of wealth created and spent by the west will decrease markedly in the next few decades」  
  判断：**正确**。G7占世界GDP份额由1990年代初约67%降至约46%（PPP口径约32%），2023年约30%，西方财富占比明显下降。  
  来源：<https://dobetter.esade.edu/en/g20-global-leadership>；<https://www.visualcapitalist.com/charted-the-g7s-declining-share-of-global-gdp/>
- **#29** 「Within a few decades, many more people will be employed in the service industries which characterise economic …」  
  判断：**正确**。ILO数据显示全球服务业就业占比由1991年34%升至2019年51%，2007年服务业首次超过农业。  
  来源：<https://ourworldindata.org/data-insights/the-service-sector-now-represents-about-half-of-employment-across-the-world>；<https://www.csmonitor.com/2007/0904/p01s02-wogi.html>
- **#30** 「demographic change is likely to alter the percentage of US citizens who are first-language English speakers」  
  判断：**正确**。美国在家说非英语人口由1980年约1/10升至2019年近1/5，仅说英语者比例持续下降（78.7%→78.3%）。  
  来源：<https://www.census.gov/library/stories/2022/12/languages-we-speak-in-united-states.html>；<https://www.census.gov/newsroom/press-releases/2023/language-at-home-acs-5-year.html>
- **#34** 「As countries grow richer, the OECD countries will become proportionally less important in the world economy.」  
  判断：**正确**。OECD统计显示非OECD国家PPP份额2010年超过OECD；现38个成员国占世界GDP约46%（2021），比重下降。  
  来源：<https://www.oecd.org/en/publications/perspectives-on-global-development-2014_persp_glob_dev-2014-en.html>；<https://www.oecd.org/en/data/insights/statistical-releases/2024/05/share-of-oecd-economies-in-global-gdp-broadly-stable-at-46-in-2021-compared-to-2017.html>
- **#37** 「major changes in culture and language during the next few decades are those connected with computers and commu…」  
  判断：**正确**。互联网、社交媒体与智能手机已成为近几十年语言与文化变化的主要来源，研究记录了数字媒介带来的语言变化。  
  来源：<https://theconversation.com/five-ways-the-internet-era-has-changed-british-english-new-research-172432>；<https://blog.oup.com/2014/06/social-media-changing-language/>
- **#39** 「There seems to be developing a new, global English-speaking market in the knowledge-intensive industries.」  
  判断：**正确**。印度已成为世界第二大计算机与信息服务出口国，爱尔兰凭英语与欧盟成员身份成为软件与科技企业欧洲基地，英语国家在知识密集产业获优势成立。  
  来源：<https://www.wto.org/english/tratop_e/ts4d_e/case_studies_e/india.pdf>；<https://www.ireland.ie/en/invest/why-global-companies-choose-ireland/>
- **#44** 「London and New York are likely to remain key world ‘hubs’ through which ideas, finance and people flow.」  
  判断：**正确**。GFCI 2025中纽约、伦敦仍居前二；科尔尼2024全球城市指数纽约第1、伦敦第2。  
  来源：<https://www.visualcapitalist.com/mapped-the-worlds-top-financial-centers-in-2025/>；<https://www.consultancy.uk/news/38745/london-retains-second-spot-in-global-cities-list-despite-human-capital-hit>
- **#45** 「Indonesia, where there is likely to be a substantial shift towards Bahasa Indonesia – the national language – …」  
  判断：**正确**。基于人口普查的研究显示城市化推动印尼语在家庭中取代地方语言，向国语印尼语的大规模转移正在发生。  
  来源：<https://www.tandfonline.com/doi/full/10.1080/01434632.2022.2055761>；<https://tompepinsky.com/2014/01/29/indonesian-the-language-killer/>
- **#46** 「the larger languages such as Javanese (with around 85 million speakers) are also likely to suffer」  
  判断：**正确**。研究显示爪哇语作为印尼最大地方语言也在年轻人中使用衰退、向印尼语转移，使用人数估计降至约6800万。  
  来源：<https://doi.org/10.1080/14790718.2025.2528662>；<https://e-journal.usd.ac.id/index.php/JOLL/article/download/7020/pdf>
- **#48** 「It is a dominance unlikely to be challenged in the immediate future.」  
  判断：**正确**。欧盟学校英语学习比例持续居首（2009年高中95%，2012年初中96.7%，2024年高中89%），远超法语、德语，主导地位未受挑战。  
  来源：<https://ec.europa.eu/eurostat/documents/2995521/5177306/3-25092014-AP-EN.PDF/568bd6e0-0184-444e-b965-ffc801c7df99>；<https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Foreign_language_learning_statistics>
- **#52** 「some ‘developing’ countries (such as Malaysia) which have expanded their provision for English-medium higher e…」  
  判断：**正确**。马来西亚国际学生超10万并持续增长、被ICEF称为日益受欢迎的留学目的地，已成为国际学生竞争者（虽未达25万目标）。  
  来源：<https://monitor.icef.com/2025/01/malaysias-growing-appeal-as-a-study-destination/>；<https://gslglobal.com/2026/10/23/malaysia-sets-its-sights-on-500000-international-students-but-where-will-they-live/>
- **#53** 「The Hooke model forecasts a rapid rise in off-campus training in the coming decades by distance education」  
  判断：**正确**。美国高校在线课程注册2007年达394万并年增约13%，MOOC学习者达2.2亿，远程/在线培训快速增长。  
  来源：<https://www.insidehighered.com/index%2Ephp/news/2008/11/13/economy-wavers-online-enrollments-climb>；<https://www.classcentral.com/report/moocs-stats-and-trends-2021/>
- **#55** 「Satellite television, a technology which has the capacity to envelop the world audience with a homogeneous pro…」  
  判断：**正确**。印度地方语言卫星频道大量涌现并成为收视增长主力，Star TV等转向本地化，卫星电视反而促进了本地语言多样性。  
  来源：<https://www.thehindubusinessline.com/news/regional-language-content-driving-growth-of-tv-viewership-barc-india/article31050130.ece>；<https://indianjournals.com/article/mw-5-3-011>
- **#56** 「most world regions will be provided with 500 channels or more」  
  判断：**正确**。印度2025年有918个获准私营卫星频道，欧洲有约1.08万个电视频道，多数地区已超500个频道。  
  来源：<https://en.wikipedia.org/wiki/Television_in_India>；<https://rm.coe.int/mavise-report-2020/1680a2fc29>
- **#59** 「the Internet, from its origins as a tool for international communication between a global academic elite, will…」  
  判断：**正确**。互联网已从学术工具演变为广泛的本地化商业与生活平台，研究与行业资料显示本地电商与本地内容服务普及。  
  来源：<https://realestate.wharton.upenn.edu/wp-content/uploads/2017/03/437.pdf>；<https://www.shopify.com/blog/local-ecommerce>
- **#60** 「as the Internet becomes more widely used, it is natural to expect a wider range of languages will be employed」  
  判断：**正确**。维基媒体项目已覆盖320多种语言，网上使用的语言种类大幅增加（尽管少数语言仍占主导）。  
  来源：<https://meta.wikimedia.org/wiki/Research:Incubator_and_language_representation_across_Wikimedia_projects>；<https://wikimediafoundation.org/story/abstract-wikipedia/>
- **#64** 「In future, browser software will transmit ‘language preference’ information when contacting a remote site.」  
  判断：**正确**。浏览器通过HTTP Accept-Language头发送语言偏好，服务器据此内容协商返回对应语言页面，已成为通用标准。  
  来源：<https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Accept-Language>；<https://www.w3.org/International/questions/qa-when-lang-neg.en.html>
- **#73** 「but other languages will be increasingly important to the world’s young」  
  判断：**正确**。日语、韩语等受流行文化推动成为增长最快的学习语言，美国高校韩语课程注册2006-2016增长95%，其他语言对年轻人越来越重要。  
  来源：<https://www.middlebury.edu/language-schools/blog/global-k-pop-impact>；<https://blog.duolingo.com/learning-asian-language-duolingo/>
- **#74** 「an ever more important role in world communications, international business, and social and cultural affairs」  
  判断：**正确**。越来越多跨国公司（乐天、空客、三星等）以英语为企业通用语，英语在国际商务中作用增强。  
  来源：<https://hbr.org/2012/05/global-business-speaks-english>；<https://www.strategy-business.com/article/When-a-Japanese-Company-Adopted-English-as-a-First-Language>
- **#76** 「The most likely scenario thus seems to be a continued ‘polycentrism’ for English – that is, a number of standa…」  
  判断：**正确**。澳大利亚英语（麦考瑞词典）、印度英语等完成或推进本土规范编纂，英语呈多中心、多标准并存，未形成单一世界标准。  
  来源：<https://researchers.mq.edu.au/en/publications/the-codification-of-australian-english/>；<https://doi.org/10.1017/9781108623469.008>
- **#78** 「But intellectual property in English will become more widely produced and marketed in other parts of the world…」  
  判断：**正确**。印度已成为第二大英语出版市场，企鹅兰登印度持续增长，英语出版与内容更多在英美以外地区生产与销售。  
  来源：<https://www.independentpublishersguild.com/Common/Uploaded%20files/IPG%20document%20library/IPG%20email%20documents/TheIPGIndiaReport.pdf>；<https://www.frontlist.in/public/the-year-2022-had-a-major-impact-on-english-language-publishers-in-india>
- **#80** 「it does seem clear that the global fortunes of Spanish are rising quite rapidly」  
  判断：**正确**。塞万提斯学院2024年报告西语使用者首次超6亿，美国成为第二大西语国家，西语全球地位上升。  
  来源：<https://cervantes.org/es/sobre-nosotros/sala-prensa/notas-prensa/espanol-supera-primera-vez-600-millones-hablantes-consolida>；<https://thediplomatinspain.com/en/2024/10/31/spanish-exceeds-600-million-speakers-worldwide-for-the-first-time/>
- **#83** 「The relative positions of the ‘top six’ are likely to change during the coming decades, but it is unlikely tha…」  
  判断：**正确**。Ethnologue 2025：英语以约15亿总使用者居首，各大语言排位有所变化（印地语等上升），但无语言超过英语。  
  来源：<https://www.ethnologue.com/insights/most-spoken-language/>；<https://indianexpress.com/article/trending/top-10-listing/top-10-most-spoken-languages-globally-in-2025-5-indian-languages-ranked-9999661/>
- **#86** 「That British and other native-speaking ELT providers will find the global market much more competitive, will l…」  
  判断：**正确**。英国ELT学生周数较2019年下降约四分之一，2025年继续下滑，母语国ELT提供者面临更激烈竞争并失去份额。  
  来源：<https://monitor.icef.com/2024/12/uk-elt-reports-new-normal-with-softer-student-numbers-for-key-third-quarter/>；<https://www.englishuk.com/en/agents/english-in-the-uk/agent-news?newsId=3568>
- **#87** 「English language programmes will remain, particularly in certain content areas (such as sport and news), but t…」  
  判断：**正确**。印度地方语言内容主导电视收视增长，Netflix 2025年非英语原创剧集首次过半，英语节目已是众多选择之一而非主导。  
  来源：<https://www.ampereanalysis.com/insight/a-first-for-netflix-non-english-content-takes-the-lead-in-tv-originals>；<https://www.thehindubusinessline.com/news/regional-language-content-driving-growth-of-tv-viewership-barc-india/article31050130.ece>
- **#88** 「other major world languages will increase their global reach and the larger providers will localise their serv…」  
  判断：**正确**。Star TV由面向英语精英转为印地语等本地化频道，CNN提供7种语言服务，其他主要语言扩大覆盖、大型提供者本地化成立。  
  来源：<https://www.medianews4u.com/25-years-star-india/>；<https://press.wbd.com/es/emea/brands/cnn-international-6>
- **#89** 「The quantity of Internet materials in languages other than English is set to expand dramatically in the next d…」  
  判断：**正确**。2000-2007年非英语地区网民增长最快（拉美、中东网民分别增长577%、920%），2007年日语成为第一博客语言，非英语内容大幅扩张。  
  来源：<https://cacm.acm.org/research/web-searching-in-a-multilingual-world/>；<https://www.socialmediatoday.com/content/japanese-no-1-blogging-language>
- **#93** 「The indications are that English will enjoy a special position in the multilingual society of the 21st century…」  
  判断：**正确**。英语在约110个国家以母语、官方或广泛二语形式使用，是最常见的第二语言，在多语社会中拥有独特地位。  
  来源：<https://www.theglobalist.com/languages-culture-english-united-states-united-kingdom/>；<https://www.weforum.org/stories/education-and-skills/countries-that-speak-english-as-a-second-language>

### 趋势符合（22 条）

- **#4** 「in the coming decades young adults with disposable income will be found in Asia and Latin America rather than …」  
  判断：**趋势符合**。布鲁金斯/麦肯锡显示全球消费阶层与中高收入家庭重心正转向亚洲，新兴市场消费者以年轻人为主；但美欧人均消费仍高，"主要在亚洲拉美而非美欧"只部分实现，方向一致。  
  来源：<https://www.brookings.edu/articles/asias-tipping-point-in-the-consumer-class/>；<https://www.mckinsey.com/featured-insights/asia-pacific/beyond-income-redrawing-asias-consumer-map>
- **#6** 「it would be foolhardy to imagine that its pre-eminent position as a world language will not be challenged in s…」  
  判断：**趋势符合**。英语在互联网内容中的份额从约80%降至约一半或更低，普通话在东南亚商务中的地位上升，说明英语在部分领域/地区受到挑战；但其总体主导地位仍稳固。  
  来源：<https://www.motionpoint.com/blog/is-english-still-the-lingua-franca-of-the-internet/>；<https://www.bbc.com/news/magazine-17105569>
- **#7** 「within a decade or so, the number of people who speak English as a second language will exceed the number of n…」  
  判断：**趋势符合**。Crystal估算英语母语者与二语使用者均约4亿，已大体持平；另据Crystal到2003年非母语者（含外语学习者）约为母语者3倍。二语者在约十年内超过母语者的方向成立，但严格区分二语与外语的数据不足以确认已明确超过。  
  来源：<https://simple.wikipedia.org/wiki/English-speaking_world>；<https://www.davidcrystal.com/Files/BooksAndArticles/-4031.pdf>
- **#12** 「We have entered a period in which language and communication will play a more central role than ever before in…」  
  判断：**趋势符合**。语言服务业规模持续增长（2024年约717亿美元），语言与传播在经济中的作用扩大，方向一致；"比以往任何时候更核心"难以精确衡量。  
  来源：<https://www.nimdzi.com/nimdzi-100-2025/>；<https://www.statista.com/statistics/257656/size-of-the-global-language-services-market/>
- **#14** 「other countries will emerge to compete with the older, native-speaking countries in both the English language-…」  
  判断：**趋势符合**。菲律宾等非母语国家英语教师通过在线平台与母语国竞争（"我们更便宜所以雇我们"），印度成为重要英语出版市场，方向一致；但国际考试等仍由英美掌控。  
  来源：<https://doi.org/10.1111/josl.12543>；<https://www.degruyterbrill.com/document/doi/10.1515/applirev-2025-0230/html>
- **#15** 「the present dominance of English can be expected to give way to a wider mix of languages」  
  判断：**趋势符合**。网络语言观测显示英语网页占比大幅下降，W3Techs亦显示英语网站份额降至约49%，多语格局扩大；卫星电视与外语学习等领域方向大体一致。  
  来源：<https://researchoutreach.org/articles/reliably-exploring-presence-languages-internet/>；<https://w3techs.com/blog/entry/fact_20250424>
- **#20** 「the economic dominance of the US is expected to decline, as economies in Asia overtake it in size」  
  判断：**趋势符合**。按IMF的PPP口径中国在2014年超过美国成为最大经济体；但按名义GDP美国份额仍约26%，主导地位下降仅部分实现。  
  来源：<https://www.csmonitor.com/Business/Latest-News-Wires/2014/1008/China-just-overtook-US-as-the-world-s-largest-economy-IMF-says>；<https://www.theglobaleconomy.com/usa/gdp_share/>
- **#24** 「whereas the majority of the world’s languages – found at present only at the base – are likely to become extin…」  
  判断：**趋势符合**。Ethnologue统计3226种语言濒危，语言持续消亡（约每6-13周一种），方向一致；但实际消亡速度慢于早期估计，"多数语言灭绝"远未实现。  
  来源：<https://www.ethnologue.com/insights/how-many-languages-endangered/>；<https://nouvelles.umontreal.ca/en/article/2026/10/01/languages-are-dying-but-how-fast>
- **#42** 「Here, however, it is likely to be Bahasa Indonesia which benefits」  
  判断：**趋势符合**。人口普查显示城市化推动印尼语成为更多人的家庭语言，印尼社交媒体以印尼语为主、夹杂英语与方言，方向一致；英语在网络中的使用亦在增长。  
  来源：<https://tompepinsky.com/2018/12/01/urbanization-ethnic-diversity-and-the-rise-of-indonesian/>；<https://jurnal.umsu.ac.id/index.php/ETLiJ/article/download/31675/15916>
- **#43** 「Growing intraregional trade and financial dealings amongst Chinese-speaking business interests will undoubtedl…」  
  判断：**趋势符合**。新加坡"华语化"、马来西亚非华人学华语增多、槟城福建话活力下降，显示普通话在东南亚华人商圈作用增强，方向一致；地区通用语地位仍有限。  
  来源：<https://benjamins.com/catalog/cld.8.1.02won>；<https://www.thinkchina.sg/society/new-mandarin-speakers-malaysian-phenomenon>
- **#47** 「More people will need to acquire a higher proficiency in English.」  
  判断：**趋势符合**。ETS调查显示81%的人力资源决策者认为竞争加剧使其更重视求职者英语水平，企业招聘普遍要求高级英语，方向一致；但缺乏全球"需要高水平英语人数"的直接统计。  
  来源：<https://www.ets.org/pdfs/toeic/ets-toeic-global-english-skills-report.pdf>；<https://researchonline.lse.ac.uk/id/eprint/24729/1/Didiot-Cook_%20etal_Language-needs-in-business_2000.pdf>
- **#54** 「The ‘mega-universities’ such as the British Open University are more likely to proceed through joint ventures …」  
  判断：**趋势符合**。英国开放大学通过认证合作院校与阿拉伯开放大学等合作扩张；英国跨国教育中合作办学是最主要形式（41.6%），方向一致；但大规模远程项目同样存在。  
  来源：<https://university.open.ac.uk/validation-partnerships/about-us/ou-validation-partner-institutions>；<https://www.universitiesuk.ac.uk/what-we-do/policy-and-research/publications/features/uk-higher-education-data-international/transnational-education-tne-data>
- **#57** 「When there are 500 channels to choose from – some showing the same film but at different starting times, other…」  
  判断：**趋势符合**。受众碎片化已成常态（美国超3.2万线性频道），共同收视体验大幅减少；但大型体育直播仍保留共同收视，方向一致。  
  来源：<https://www.nielsen.com/insights/2024/amid-the-fragmented-tv-landscape-time-spent-with-content-is-the-best-planning-data-there-is/>；<https://www.stateofstreaming.com/articles/last-truly-shared-experience-sports-own-attention-economy>
- **#58** 「the number of computer hosts in Asia eventually will outstrip those in the Big Three countries」  
  判断：**趋势符合**。亚洲网民已超26亿、占全球一半以上，超过美日欧；但主机数量本身缺乏直接数据，方向一致。  
  来源：<https://www.hubspot.com/web-guide/asia-digitalmarketing-report/expenditure>；<https://www.itu.int/itu-d/reports/statistics/2023/10/10/ff23-Internet-use/>
- **#63** 「As computer usage spreads, it is predicted that English content on the Internet may fall to 40% of the total m…」  
  判断：**趋势符合**。英语网络内容占比由1990年代中期约80%显著下降（部分估计2011年约27%），但W3Techs口径仍约49%，降至40%与否取决于口径，方向一致。  
  来源：<https://scroll.in/article/836355/regional-language-internet-usage-is-where-the-real-growth-will-be-in-india>；<https://w3techs.com/blog/entry/fact_20250424>
- **#65** 「Such language technologies, widely available, may significantly reduce the need for learning English for the c…」  
  判断：**趋势符合**。谷歌翻译月活约10亿、支持约250种语言，浏览器可自动翻译网页，韩国调查显示AI使学英语动机下降，方向一致；英语学习需求总体仍高。  
  来源：<https://blog.google/products-and-platforms/products/translate/fun-facts-google-translate-20-years/>；<https://www.koreaherald.com/article/10538041>
- **#68** 「The Americas, for example, might become more prominently Spanish-English bilingual.」  
  判断：**趋势符合**。美国已成为全球第二大西语使用国（约5700万潜在使用者），美洲西英双语更突出；但美国拉美裔在家说西语比例下降，方向基本一致。  
  来源：<https://cnnespanol.cnn.com/2024/10/30/ee-uu-segundo-pais-hablantes-espanol-desbancando-colombia-efe>；<https://observatoriodelespanol.cervantes.org/documentos/2024_el-espanol-lengua-para-el-mundo-2024.pdf>；<https://www.pewresearch.org/short-reads/2017/10/31/use-of-spanish-declines-among-latinos-in-major-u-s-metros/>
- **#70** 「countries in the south increasingly providing cheaper labour and backoffice services for those in the north」  
  判断：**趋势符合**。拉美近岸外包(BPO)以同时区与低成本为卖点为美国提供后台服务，国际清算银行亦记录美洲近岸化证据，方向一致。  
  来源：<https://www.bis.org/publications/bulletin-94-evidence-nearshoring-americas.pdf>；<https://www.skycomcallcenter.com/>
- **#75** 「we can also expect to see English develop a larger number of local varieties」  
  判断：**趋势符合**。尼日利亚英语等本地变体快速扩张，eWAVE收录77种英语变体，方向一致；但缺乏变体数量随时间增加的直接统计。  
  来源：<https://onlinelibrary.wiley.com/doi/full/10.1111/weng.12732>；<https://ewave-atlas.org/>
- **#90** 「English will remain pre-eminent for some time, but it will eventually become one language amongst many.」  
  判断：**趋势符合**。英语仍是网络内容第一语言，但英语网民仅约四分之一、中文约19%，英语正走向"众多语言之一"，最终状态尚未完全实现。  
  来源：<https://fastnet.news/index.php/8-fnn/665-active-internet-connections-about-1-400-000-000-users-about-twice-as-many>；<https://w3techs.com/blog/entry/fact_20250424>
- **#91** 「That proportion is expected to fall to around 40% in the next decade.」  
  判断：**趋势符合**。到2007年英语网民占比已降至约31%（低于40%），但网页内容中英语仍约57%，降至约40%取决于口径，方向一致。  
  来源：<https://www.theguardian.com/commentisfree/2007/oct/17/speakingintongues>；<https://www.marioncaris.com/wp-content/uploads/2011/10/Cant-read-wont-buy_2007.pdf>
- **#92** 「ethical, as well as environmental, values are likely to come under increasing public scrutiny and significantl…」  
  判断：**趋势符合**。多项调查显示过半消费者愿转向可持续企业，伦理与环境价值影响品牌忠诚；但"说做差距"显著，方向一致。  
  来源：<https://www.teamlewis.com/magazine/research-roundup-sustainability/>；<https://www.ipsos.com/en-ca/shoppers-want-do-good-brands-are-missing-mark>

### 部分符合（17 条）

- **#8** 「the centre of authority regarding the language will shift from native speakers」  
  判断：**部分符合**。英语通用语(ELF)研究与"世界英语"理念显示规范权威向非母语使用者分散；但英语教学与考试中母语者规范仍占主导，转移并不完整。  
  来源：<https://www.jbe-platform.com/docserver/fulltext/lplp.34.3.01fie.pdf>；<https://global-science-review.com/ojs/index.php/gsr/article/view/1279>
- **#9** 「The language will grow in usage and variety, yet simultaneously diminish in relative global importance.」  
  判断：**部分符合**。英语使用人数与变体持续增长成立；但"相对全球重要性下降"仅在网络内容份额等个别指标上体现，在科研、商务、学习需求等领域英语重要性反而上升。  
  来源：<https://researchoutreach.org/articles/reliably-exploring-presence-languages-internet/>；<https://journal.thebritishacademy.ac.uk/articles/12/1and2/a11>
- **#11** 「the size of the global market for the English language may increase in absolute terms, but its market share wi…」  
  判断：**部分符合**。英语学习市场绝对规模扩大成立；但英语在外语学习中的份额并未下降，多邦果报告显示英语成为更多国家的第一学习语言。  
  来源：<https://www.researchandmarkets.com/reports/5140838/english-language-learning-global-strategic>；<https://blog.duolingo.com/2025-duolingo-language-report/>
- **#13** 「the long-term growth of the learning of English is less secure than might at first appear」  
  判断：**部分符合**。主要留学目的地ELT市场2024-2025连续下滑、欧盟潜在英语学习者因人口变化减少、AI翻译削弱学习动机，显示增长并不稳固；但全球英语学习者总量仍处高位。  
  来源：<https://20029864.fs1.hubspotusercontent-na1.net/hubfs/20029864/Reports/International%20Education/2026/BONARD%20Report%20-%20Global%20ELT%20Annual%20Report%202026.pdf>；<https://www.britishcouncil.org/voices-magazine/will-young-people-in-eu-want-english-in-2025>
- **#16** 「the future will be a bilingual one, in which an increasing proportion of the world’s population will be fluent…」  
  判断：**部分符合**。欧洲小学阶段学外语比例明显上升，约一半以上人口为双语；但缺乏全球"流利双语人口比例上升"的系统数据，只能部分支持。  
  来源：<https://ec.europa.eu/eurostat/documents/3433488/5565660/KS-SF-10-049-EN.PDF>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC4274874/>
- **#17** 「it will be those who speak English as a second or foreign language who will determine its world future」  
  判断：**部分符合**。非母语使用者已远多于母语者，ELF与世界英语研究显示其影响英语发展；但国际考试与标准仍由英美机构主导，"决定未来"只部分体现。  
  来源：<https://futureofenglish.britishcouncil.org/hubfs/Global%20-%20Future%20of%20English/eBook%20and%20Summary/FoE%20Summaries/FoE_Research%20Summary_revisedv4.pdf>；<https://doi.org/10.58304/ijts.250128>
- **#36** 「It is unlikely that the world will be transformed by some extraordinary invention in the next few decades.」  
  判断：**部分符合**。1997年后的重大变化（智能手机、移动互联网）属作者已预见的计算机与通信领域的延续，未出现该领域之外的"非凡新发明"；但智能手机本身的变革程度使该判断只能部分成立。  
  来源：<https://www.reuters.com/article/technology/decade-in-review-what-the-smartphone-has-wrought-idUSKBN1YR1SA/>；<https://www.nature.com/articles/s41586-022-05543-x>
- **#40** 「it seems likely that the preponderance of flow between North-east and Southeast Asia – particularly as it rela…」  
  判断：**部分符合**。东南亚普通话学习随中国投资与商务往来激增（柬埔寨、印尼等），但东盟工作语言仍是英语，普通话尚未成为地区通用语。  
  来源：<https://www.scmp.com/news/asia/southeast-asia/article/3306872/unstoppable-rise-china-fuels-mandarin-learning-boom-cambodia>；<https://www.scmp.com/magazines/post-magazine/article/2105289/speaking-tongues-why-asean-members-stick-english>
- **#62** 「Electronic mail, for example, is expected to be a dominant activity, even when the Web has matured」  
  判断：**部分符合**。皮尤2011年调查显示搜索与电子邮件仍是最常见网络活动；但尼尔森2009年起社交网络在到达率与使用时长上超过电子邮件。  
  来源：<https://www.pewresearch.org/internet/2011/08/09/search-and-email-still-top-the-list-of-most-popular-online-activities/>；<https://www.benton.org/headlines/social-networking-overtakes-e-mail-popularity>
- **#66** 「The likely consequence of economic regionalisation, therefore, is the emergence of regional lingua francas oth…」  
  判断：**部分符合**。东非共同体推动斯瓦希里语作为官方/通用语，体现区域通用语兴起；但东盟以英语为唯一工作语言，区域化同样强化英语。  
  来源：<https://www.eac.int/press-releases/3131-kiswahili-kitukuzwe-regional-leaders-push-for-amendment-of-the-eac-treaty-to-fast-track-the-use-of-kiswahili-as-an-eac-official-language>；<https://doi.org/10.3828/ejlp.2017.2>
- **#67** 「It seems that the trade agreement may be helping to establish Spanish as the regional lingua franca」  
  判断：**部分符合**。巴西2005年立法（与南共市一体化相关）要求高中提供西班牙语，但2017年被废止，西语未确立为地区通用语。  
  来源：<https://en.mercopress.com/2005/07/08/spanish-becomes-second-language-in-brazil>；<https://www12.senado.leg.br/noticias/audios/2017/02/senadores-criticam-retirada-do-espanhol-como-idioma-obrigatorio-no-ensino-medio>
- **#69** 「may continue, with French gradually being squeezed as the extension of the EU favours English and German」  
  判断：**部分符合**。欧盟扩大后英语进一步主导、法语被挤压成立；但德语并未受益（欧委会翻译源文本中德语仅约1%）。  
  来源：<https://www.theguardian.com/world/2004/jul/12/eu.france>；<https://commission.europa.eu/system/files/2023-03/TRAD23-Info%20Session_0.pdf>
- **#71** 「North America will develop a closer relation with Latin America, perhaps eventually forming a single trading b…」  
  判断：**部分符合**。美洲自由贸易区谈判2005年失败，未形成单一贸易集团；但墨西哥成为美国最大贸易伙伴，美拉贸易增长，关系更紧密部分成立。  
  来源：<https://www.npr.org/2005/11/06/4991494/latin-america-summit-ends-with-no-free-trade-zone>；<https://www.congress.gov/crs_external_products/IF/HTML/IF11175.html>
- **#72** 「suggests that the focus of a global youth-culture might shift in the next decade or so from Europe and the US」  
  判断：**部分符合**。韩流等亚洲流行文化成为全球青年文化重要力量；但研究显示英美内容在欧洲青年中仍占霸权，中心并未完全转移。  
  来源：<https://news.yale.edu/2023/08/21/rise-k-pop-and-what-it-reveals-about-society-and-culture>；<https://kclpure.kcl.ac.uk/ws/portalfiles/portal/343043608/esser-steemers-2025-global-platforms-new-media-generations-and-anglo-american-hegemony-an-exploration-of-young-audience.pdf>
- **#82** 「India and Nigeria may experience substantial increase in numbers of first language speakers of English in this…」  
  判断：**部分符合**。尼日利亚城市儿童英语单语现象增多，L1英语者上升；但印度2011年普查英语母语者仅约26万，未见大幅增加。  
  来源：<https://dailytrust.com/the-english-nigerian-children-speak-i/>；<https://themapsdaily.com/posts/in-english-speakers>
- **#84** 「Chinese, Hindi/Urdu, Spanish and Arabic may join English. French and other OECD languages (German, Japanese) a…」  
  判断：**部分符合**。语言力量指数显示普通话、西语、阿拉伯语排名靠前，但法语仍居第三，印地语未进前列，法德日地位下降只部分成立。  
  来源：<https://www.kailchan.ca/2016/05/power-language-index/>；<https://knowledge.insead.edu/leadership-organisations/worlds-most-powerful-languages>
- **#85** 「Second, at some point the increase in people learning English as a foreign language will level out.」  
  判断：**部分符合**。欧盟部分国家潜在英语学习者因人口变化减少、有评论提出"英语见顶"，显示趋平迹象；但全球英语学习者总体仍在增长，尚未普遍趋平。  
  来源：<https://www.britishcouncil.org/education/schools/support-for-languages/thought-leadership/research-report/future-of-english-eu-2025>；<https://www.theguardian.com/commentisfree/2018/feb/27/reached-peak-english-britain-china>

### 错误（7 条）

- **#10** 「We may find the hegemony of English replaced by an oligarchy of languages, including Spanish and Chinese.」  
  判断：**错误**。INSEAD语言力量指数等显示英语仍是唯一世界通用语，普通话远居第二；英语霸权并未被含西语、汉语的"语言寡头"格局取代。  
  来源：<https://knowledge.insead.edu/leadership-organisations/worlds-most-powerful-languages>；<https://time.com/3585847/mandarin-lingua-franca/>
- **#31** 「Migration to these zones is likely to lead to wider usage of regional lingua francas, such as Cantonese or Wu …」  
  判断：**错误**。移民与推普政策使广州、深圳普通话扩张、粤语在年轻人中衰退，而非粤语、吴语等地区通用语使用扩大。  
  来源：<https://u.osu.edu/mclc/2018/03/13/why-has-cantonese-fallen-out-of-favor/>；<https://www.theglobeandmail.com/news/world/mandarin-pushing-out-cantonese/article4293285/>
- **#32** 「the rapid urbanisation in the Shanghai area of northern China, for example, may create a new variety of Wu Chi…」  
  判断：**错误**。上海城市化与移民带来的是上海话衰退（6-20岁居民仅约22%仍使用），未出现有强大经济文化支撑的新吴语变体；近年仅有文化层面的怀旧热。  
  来源：<https://www.chinadaily.com.cn/a/202411/22/WS673fc8d8a310f1265a1cef34_1.html>；<https://www.sixthtone.com/news/1286>
- **#35** 「central and eastern Europe: a trend that may be confirmed as more countries join the European Union」  
  判断：**错误**。中东欧入盟后英语成为首要外语，捷克自1997年起英语超过德语且德语地位持续减弱，德语增长趋势未因欧盟扩大而得到确认。  
  来源：<http://languagemanagement.ff.cuni.cz/system/files/documents/Nekvapil_Sherman_English%20in%20the%20Czech%20Republic%20.pdf>；<https://xlinguae.eu/files/XLinguae4_2023_12.pdf>
- **#49** 「The Hooke model forecasts, primarily on economic grounds, that by 2010 the languages in greatest demand by stu…」  
  判断：**错误**。2010年前后英语居首成立，但西班牙语、法语等才是第二梯队，印尼语学习反而大幅萎缩（澳大利亚入学下降过半），"英、普、西、印尼"的需求排名不成立。  
  来源：<https://www.aph.gov.au/DocumentStore.ashx?id=6c1303cc-a1b6-4f01-ac65-3f3e0ce6152b&subId=779880>；<https://blog.duolingo.com/global-language-report-2020/>
- **#50** 「The Hooke model forecasts that the international demand for specialist courses of English as a second language…」  
  判断：**错误**。2025年八大英语留学目的地仅约90万学生、连续两年下降，远低于2019年水平，国际ESL专门课程需求增至六倍未实现。  
  来源：<https://www.bonardeducation.com/insights/key-takeaways-from-bonards-global-elt-annual-report-2026>；<https://www.bonardeducation.com/media/global-elt-recovery-stalls-across-major-study-destinations>
- **#81** 「the trading areas of the south (Mercosur, Safta) are expected to merge with Nafta in the first decade of the n…」  
  判断：**错误**。美洲自由贸易区谈判在2005年马德普拉塔峰会破裂，南共市等未在新千年第一个十年与北美自贸区合并。  
  来源：<http://news.bbc.co.uk/2/hi/americas/4410190.stm>；<https://www.npr.org/2005/11/06/4991494/latin-america-summit-ends-with-no-free-trade-zone>

### 暂无法判断（9 条）

- **#5** 「the conditions will be established for more settled global relations which may stabilise about 2050」  
  判断：**暂无法判断**。预测终点约2050年，尚未到期，无法判断。  
  来源：—
- **#33** 「The Hooke forecasting model suggests that by 2050 the global economy will have grown a further tenfold to $250…」  
  判断：**暂无法判断**。预测终点为2050年，尚未到期，无法判断。  
  来源：—
- **#38** 「According to the Hooke forecasting model, the services sector will, by 2050, account for 75% of Gross World Pr…」  
  判断：**暂无法判断**。预测终点为2050年，尚未到期，无法判断。  
  来源：—
- **#41** 「The dominance of English in the telephone conversations of the world is unlikely to continue for long.」  
  判断：**暂无法判断**。缺乏按语言统计的全球电话通话数据，现有资料无法判断英语在电话通话中的主导地位是否消退。  
  来源：—
- **#51** 「Since much of the demand will come from Asia, Australian providers are expected to benefit more than the US an…」  
  判断：**暂无法判断**。现有归档资料未提供澳、美、英英语教学提供者受益程度的可比数据，无法判断。  
  来源：—
- **#61** 「‘intranets’ (Internet-like networks within organisations, often ‘fire walled’ against the outside world) are e…」  
  判断：**暂无法判断**。现有资料只显示1998年内网投入巨大，未提供内网与互联网增速的直接比较，无法判断。  
  来源：—
- **#77** 「Britain’s linguistic advantage in attracting investment from Asia may decrease as English becomes more widely …」  
  判断：**暂无法判断**。英国仍是欧洲主要FDI目的地，亚洲对英投资有升有降，现有资料无法分离"语言优势下降"的影响。  
  来源：—
- **#79** 「will appear within the next 50 years to replace English as the global lingua franca」  
  判断：**暂无法判断**。预测窗口为1997年起50年（至约2047年），尚未到期；截至2026年尚无语言取代英语，但无法最终判断。  
  来源：—
- **#94** 「Yesterday it was the world’s poor who were multilingual; tomorrow it will also be the global elite.」  
  判断：**暂无法判断**。仅有零散案例与民族志研究，缺乏全球精英多语化趋势的系统证据，无法判断。  
  来源：—

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/graddol-future-of-english-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/graddol-future-of-english-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/graddol-future-of-english-v5/audit/manual_review_2026-11-15.py`

## 说明

- 无日期的方向性判断按 1997 至 2026-11-15 窗口核验：方向已明确发生记正确，方向一致但程度/口径未完全到位记趋势符合。
- 以 2050 年或“50 年内”为终点的 4 条记暂无法判断；另 5 条因缺乏可比的公开数据记暂无法判断。
- 书中个别判断在不同章节重复出现（如互联网英语内容降至 40%、普通话成为地区通用语），按抽取结果分别核验。

