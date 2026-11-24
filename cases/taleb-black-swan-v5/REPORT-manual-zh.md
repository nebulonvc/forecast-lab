# 纳西姆·尼古拉斯·塔勒布《黑天鹅》（The Black Swan: The Impact of the Highly Improbable，2007）：出版后预测人工核查

- 案例目录：`cases/taleb-black-swan-v5/`
- 出版日期：Random House 初版 2007 年 4 月 17 日。所用文件为 2007 年初版英文 PDF，ISBN 978-1-4000-6351-2，版权页 Copyright © 2007 by Nassim Nicholas Taleb，401 PDF 页；不是 2010 年第二版（无 On Robustness and Fragility 长文）。观察窗口按初版 2007-04 起算，至 2026-11-15。PDF 为 reading-library/2026-11-15-未来判断书单/04-经济和金融/27-黑天鹅.pdf，sha256 0976a6609f48761607cbcacf30129fee3b4ce15fa21ab4d81b99f510e4d7c2b3（已与 catalog.json 核对）。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

按仓库 DeepSeek 管线手工代替模型调用：以 `pdftotext -enc UTF-8` 生成全书 TXT（sha256 `f33415a308912c7df612813b18193d889ada561934dc5d1186806f8cddf4a458`，930,014 字符），`prepare_book.split_text(3500, 600)` 得到 269 个 chunk。自定义 matter_spans 排除文前护封/推荐语/版权/献词/目录（0–12418）与文后致谢、术语表、注释、参考文献、索引、作者简介和 ABOUT THE TYPE（722341–930014），保留序言与尾声《Yevgenia’s White Swans》，对 txt-00004–txt-00209 共 206 个正文块逐块通读。经 `validate_chunk_predictions` 与 `claims_from_results` 导入 23 条可解析预测（全部 `claim_type=forecast`，无降为 unclear、无重叠去重）。引文均为 TXT 逐字片段，英文 `changes` 为同一物理行上的原文子串。记录字符偏移与 TXT/PDF sha256。全文 TXT 未入库。边界块只抽正文、不抽目录与致谢。虚构的叶甫根尼娅故事、纯认识论格言、规范建议和出版前史实不作为预测。核验按 METHOD.md §4：每条先定 scope，再各做一次 support/counter 检索（Exa pool key 4，仅经文件路径读取），从返回 URL 中选源并归档到 `data/sources/`（sha256），写入 `data/evidence.jsonl`，再 `pipeline.py apply assess`。本稿由助手逐条对照书中原文，并依据 2007-04 至 2026-11-15 窗口内已归档的公开来源人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 23 条，剔除非预测 0 条，计入 **23 条预测**，其中 **22 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 9 |
| 趋势符合 | 1 |
| 部分符合 | 12 |
| 错误 | 0 |
| 暂无法判断 | 1 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **40.9%**（9/22） |
| 加权胜率 | **71.6%** |
| 错误率 | **0.0%**（0/22） |
| 未定占比（暂无法判断/预测） | 4.3%（1/23） |

## 总体评价

《黑天鹅》主要是一本关于归纳、叙事和预测限度的认识论著作，不是一份密密麻麻的预言清单。逐块通读后，真正构成“出版时尚不确定、此后可核对”的判断，集中在金融脆弱性、全球化的连锁风险、极值之地的赢家更迭，以及“未来会更难预测、黑天鹅仍会击穿预测”这一组总命题上。点名判断里，最清楚的是房利美：2008 年 9 月被联邦住房金融局接管，与“坐在炸药桶上”直接对应。银行损失由公共部门托底、表面低波动的机构藏着爆炸性风险、受雇预测者继续给出糟糕预测、2008 年和新冠等冲击主导随后历史并击穿官方预测，这些也与书中的方向相符。全球化在降低日常波动的同时制造相互锁定的脆弱性，以及“更多平静期、问题集中在少数黑天鹅”的波动形态，也被金融危机和疫情冲击所支持。全球市值榜在保持高度集中的同时榜首多次易主，也符合“不断变换的极值之地”。说得过满或需要打折的，主要是长尾和文化商业份额、在位巨头是否真的“没有人能站稳”，以及“一家银行倒下则全部倒下”“危机会更少但更严重”这类全称或组合判断：方向往往出现，但平台集中、超级明星企业固化和 2011、2020、2023 等后续冲击，使主结果只能记部分符合。灾害经济损失的名义数字在上升，归一化后是否更严重仍有争议。东京若再来一次同类地震代价将远超 1923 年这一条，因窗口内没有发生可比的东京都会区大地震，记暂无法判断。彭加勒的影响力在窗口内持续，但“多个世纪”尚未到期，记趋势符合。无日期的方向性判断按出版年到截止日计分：方向已经发生则记正确，不降为趋势符合。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（9 条）

- **#3** 「when "conservative" bankers make profits, they get the benefits; when they are hurt, we pay the costs」  
  判断：**正确**。2008年TARP及美联储紧急流动性，以及2023年硅谷银行、签名银行倒闭时财政部、美联储和FDIC动用系统风险例外、担保未保险存款，都表明银行受创后仍由公共部门托底，盈利归私人、损失社会化的模式在窗口内再次出现。  
  来源：<https://www.congress.gov/crs-product/IF12378>；<https://www.nbcnews.com/business/business-news/silicon-valley-bank-getting-government-bailout-not-2008-sense-rcna74581>；<https://www.americanbanker.com/news/dud-frank-post-2008-reforms-played-little-role-in-bank-resolutions>
- **#7** 「I know that history is going to be dominated by an improbable event, I just don't know what that event will be」  
  判断：**正确**。2008年全球金融危机和2020年新冠疫情都是事先难以按常规外推的极值事件，并在随后数年主导了世界经济与政策议程；即便还有中国技术追赶等渐进趋势，也不足以否定窗口内历史被小概率冲击主导这一主结果。  
  来源：<https://www.investopedia.com/significant-financial-events-8700894>；<https://kof.ethz.ch/en/news-and-events/kof-bulletin/kof-bulletin/2021/10/Comparing-the-coronavirus-crisis-and-the-financial-crisis-eight-differences-and-similarities.html>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC7665755/>
- **#8** 「elusive, enough to kill our forecasts」  
  判断：**正确**。IMF和欧央行等机构在2021–2022年通胀、新冠冲击和金融危机期间的预测出现大幅偏离，说明仍有足够多的黑天鹅能击穿重要官方预测；个别选举或专项预测表现较好，并不否定“足以摧毁我们的预测”这一判断。  
  来源：<https://www.imf.org/-/media/files/publications/wp/2023/english/wpiea2023102-print-pdf.pdf>；<https://www.ecb.europa.eu/press/key/date/2024/html/ecb.sp241118_1~2c31ddbaa8.en.html>；<https://www2.gwu.edu/~forcpgm/Ahir_Loungani.pdf>
- **#11** 「we see "conservative" bankers sitting on a pile of dynamite but fooling themselves because their operations se…」  
  判断：**正确**。北岩银行挤兑、贝尔斯登和雷曼倒闭表明，危机前看似可经营、波动不大的大型金融机构内部隐藏了足以引爆的风险，决策者事先也低估了暴露程度，与“坐在炸药上还自以为业务沉闷”相符。  
  来源：<https://ftp.aeaweb.org/articles?id=10.1257%2Fjep.23.1.101>；<https://fcic-static.law.stanford.edu/cdn_media/fcic-reports/fcic_final_report_chapter1.pdf>；<https://fcic-static.law.stanford.edu/cdn_media/fcic-testimony/2009-1020-Baily-article.pdf>
- **#12** 「people will continue to predict foolishly, especially if they are paid for it, and you cannot put an end to in…」  
  判断：**正确**。对IMF《世界经济展望》等职业预测的事后评估显示，2008–2012年产出预测和2021–2022年通胀预测都出现系统性、往往偏乐观的大误差，受雇预测者在窗口内继续给出糟糕预测。  
  来源：<https://www2.gwu.edu/~forcpgm/Ahir_Loungani.pdf>；<https://doi.org/10.1002/for.3088>；<https://www.imf.org/-/media/files/publications/wp/2023/english/wpiea2023102-print-pdf.pdf>
- **#16** 「it will be an ever-changing Ex­ tremistan」  
  判断：**正确**。全球市值榜在窗口内保持高度集中，同时榜首多次易主：从石油和传统巨头转向苹果、微软，英伟达更从约第800名升至世界前列，符合“仍是极值之地、但具体赢家不断变换”。  
  来源：<https://www.lseg.com/en/insights/ftse-russell/king-of-the-world>；<https://en.wikipedia.org/wiki/list_of_public_corporations_by_market_capitalization>；<https://makeyourchart.com/templates/largest-companies-market-cap>
- **#19** 「we will see more periods of calm and stability, with most problems concentrated into a small number of Black S…」  
  判断：**正确**。金融波动呈现明显的集聚：危机前和2010年代中后期都有较长低波动平静期，冲击则集中在2008年金融危机和2020年疫情等少数极端事件，符合“更多平静、问题集中于少数黑天鹅”的形态。  
  来源：<https://www.allquant.co/post/volatility-clustering-and-the-dawn-of-a-new-era>；<https://kevincoldiron.substack.com/p/why-this-market-looks-more-dotcom>；<https://www.reuters.com/markets/europe/rip-great-moderation-hello-great-volatility-2022-08-30/>
- **#20** 「it creates interlocking fragility, while reducing volatility and giving the appearance of stability. In other …」  
  判断：**正确**。2008年次贷问题通过高度关联的短期融资市场扩散为全球金融危机，2020年疫情又经全球供应链迅速变成全球性供给与需求冲击，证实全球化在相互锁定的同时制造了破坏性黑天鹅。  
  来源：<https://bengolub.net/wp-content/uploads/2022/05/fragilitysurvey.pdf>；<https://www.atlanticcouncil.org/blogs/new-atlanticist/can-we-compare-the-covid-19-and-2008-crises/>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC7781181/>
- **#22** 「the government-sponsored institution Fanny Mae, when I look at their risks, seems to be sitting on a barrel of…」  
  判断：**正确**。2008年9月6–7日，联邦住房金融局在财政部支持下将房利美和房地美置于接管，因其资本和信贷状况在抵押贷款违约潮中急剧恶化，与“坐在炸药桶上”的点名判断相符。  
  来源：<https://home.treasury.gov/news/press-releases/hp1129>；<https://www.fhfa.gov/history-fannie-mae-and-freddie-mac-conservatorships>；<https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr719.pdf>

### 趋势符合（1 条）

- **#9** 「will continue for centuries to come」  
  判断：**趋势符合**。彭加勒在动力系统、数学与科学哲学中仍被持续引用和评述，斯坦福哲学百科等仍将其作为核心人物；“持续多个世纪”的终点尚未到来，但2007年以来的方向与预测一致。  
  来源：<https://plato.stanford.edu/entries/poincare/>；<https://www.nieuwarchief.nl/serie5/pdf/naw5-2012-13-3-201.pdf>；<https://mathshistory.st-andrews.ac.uk/SH/poincare_sh.pdf>

### 部分符合（12 条）

- **#1** 「the future will be increasingly less predictable」  
  判断：**部分符合**。窗口内既出现2008年危机、新冠疫情等把官方宏观经济预测打穿的冲击，也有超级预测者和部分气象/机器学习预测技能的改进；“越来越不可预测”这一单调方向并未被单独度量清楚，但社会经济领域的预测失败反复出现。  
  来源：<https://www.richmondfed.org/-/media/richmondfedorg/publications/research/working_papers/2021/wp21-10.pdf>；<https://www.ecb.europa.eu/press/key/date/2024/html/ecb.sp241118_1~2c31ddbaa8.en.html>；<https://goodjudgment.com/resources/the-superforecasters-track-record/>
- **#2** 「someone will laugh at their beliefs in the (disappointingly near) future」  
  判断：**部分符合**。2010年代社会科学出现大规模可重复性危机，大量心理与经济实验结果无法复现，相当于对2007年前后发表成果的显著翻案；但自然科学与部分社会科学的核心共识并未被整体推翻。  
  来源：<https://www.nature.com/articles/s41562-018-0399-z>；<https://www.science.org/content/article/about-40-economics-experiments-fail-replication-survey>；<https://en.wikipedia.org/wiki/Replication_crisis>
- **#4** 「an earthquake or hurri­ cane commands more and more severe economic consequences than it did in the past」  
  判断：**部分符合**。瑞士再保险sigma显示近年自然灾害经济损失和承保损失处于高位（如2021、2023年经济损失约2800亿美元，2024年承保损失1370亿美元），名义损失加重与网络化、暴露增加相符；但按Pielke等做归一化后，未必能证明同等暴露下的损失趋势在上升，人员死亡则显著下降。  
  来源：<https://www.swissre.com/institute/research/sigma-research/sigma-2025-01-natural-catastrophes-trend.html>；<https://www.swissre.com/institute/research/sigma-research/sigma-2024-01/in-short.html>；<https://rogerpielkejr.substack.com/p/disasters-cost-more-than-ever-but>
- **#6** 「the gains in our ability to model (and predict) the world may be dwarfed by the increases in its complexity—im…」  
  判断：**部分符合**。标准宏观模型未能预见2008年危机，新冠流行病学与通胀预测也出现显著失败，支持“复杂度压过既有模型”的一面；但天气临近预报等具体领域的机器学习技能在同期有改进，不能说所有建模进步都被压倒。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC7447267/>；<https://www.pnas.org/doi/10.1073/pnas.2011542117>；<https://doi.org/10.1038/s41612-024-00834-8>
- **#10** 「someone will be just as justified in laughing at us on some not too remote day」  
  判断：**部分符合**。2008年后华尔街常用风险模型尤其是VaR遭到公开检讨，被指不仅未能防护、还加重了系统性风险，当年的“精密风控”方案确实受到嘲笑式清算；但宏观政策与央行的核心框架并未被整体抛弃，只是局部修补。  
  来源：<https://www.newyorker.com/news/john-cassidy/whats-wrong-with-risk-models>；<https://www.economist.com/sites/default/files/special-reports-pdfs/15487757.pdf>；<https://doi.org/10.1111/padm.12567>
- **#13** 「many of them will be out of business a few decades later, while firms nobody ever heard of will have popped on…」  
  判断：**部分符合**。2007–2026年标普500成分有大量变更，也出现特斯拉等后来居上的新公司；但按变更原因，破产退市只占极少数，合并和市值再平衡居多，严格意义上“许多主导公司不再经营”只部分成立，更多是名录更迭而非大批倒闭。  
  来源：<https://gravitonhouse.com/en/sp-500-additions-and-deletions-what-changed-from-1957-to-2026-and-why/>；<https://fortune.com/2025/09/28/why-half-fortune-500-from-2000-is-gone-ceo-failures-artificial-intelligence/>；<https://www.arcadiaprivate.com/blog/the-largest-company-in-america-has-changed-every-decade-that-is-why-you-stay-diversified>
- **#14** 「the small guys, collectively, should con­ trol a large segment of culture and commerce」  
  判断：**部分符合**。数字发行使利基内容和独立厂牌得以存活，长尾商品确实存在；但Elberse等人及流媒体、畅销榜数据表明，大热门和平台集中仍然主导收入，“小参与者加总占据很大份额”并未成为主要格局。  
  来源：<https://martech.org/blockbusters-why-the-long-tail-is-dead-and-go-big-strategies-pay-off/>；<https://newrepublic.com/article/116248/economics-blockbusters-anita-elberse-reviewed>；<https://researchonline.lse.ac.uk/id/eprint/110440/1/businessreview_2018_11_19_the_digitisation_of_recorded_music_studying.pdf>
- **#15** 「destabilizing the well-seated winner, and bringing about another winner」  
  判断：**部分符合**。诺基亚、百视达、柯达、部分报业和零售商被新数字赢家取代，长尾/数字渠道确实动摇了一批在位者；但同期超级明星企业和平台锁定也在加强，商业活力下降，并非所有稳坐其位的赢家都被颠覆。  
  来源：<https://www.straitstimes.com/opinion/ten-lessons-from-a-history-of-disruptions>；<https://fee.org/articles/lessons-from-the-rise-of-netflix-and-the-fall-of-blockbuster/>；<https://www.imf.org/-/media/files/publications/sdn/2021/english/sdnea2021001.pdf>
- **#17** 「The long tail will help foster cognitive diversity」  
  判断：**部分符合**。传统新闻机构受众下降，社交媒体和创作者成为更重要的新闻来源，来源表面上更多样；但过滤气泡、极化与平台集中的研究同时表明，认知多样性并未单向提高，甚至在部分维度上收窄。  
  来源：<https://reutersinstitute.politics.ox.ac.uk/sites/default/files/2026-06/DNR%202026%20FINAL_2.pdf>；<https://niemanreports.org/news-influencers-content-creators-social-media-journalism/>；<https://reutersinstitute.politics.ox.ac.uk/echo-chambers-filter-bubbles-and-polarisation-literature-review>
- **#18** 「now becomes extremely unfair for the big man. Nobody is truly established」  
  判断：**部分符合**。财富500强和市值冠军确有可观更迭，一些大人物失去位置；但苹果、微软、谷歌等超级明星企业的市场势力和加成率在2007年后更加稳固，所谓“没有人能真正站稳”并不普遍成立。  
  来源：<https://fortune.com/2025/09/28/why-half-fortune-500-from-2000-is-gone-ceo-failures-artificial-intelligence/>；<https://www.bridgewater.com/research-and-insights/the-life-cycle-of-market-champions>；<https://www.ddorn.net/papers/ADKPV-SuperstarFirms.pdf>
- **#21** 「when one falls, they all fall」  
  判断：**部分符合**。2008年雷曼破产后，关联机构和市场出现严重传染，多家具有系统重要性的机构需要救助，体现了“一家倒下、体系共振”；但并非字面意义上全部银行倒闭，2023年硅谷银行等事件也显示在改革后的处置框架下可以局部控制，主结果只部分对应。  
  来源：<https://elischolar.library.yale.edu/cgi/viewcontent.cgi?article=1007&context=journal-of-financial-crises>；<https://www.federalreserve.gov/newsevents/testimony/bernanke20100902a.htm>；<https://www.elibrary.imf.org/view/journals/065/2024/001/article-A001-en.xml>
- **#23** 「we will have fewer but more severe crises」  
  判断：**部分符合**。2008年危机在高收入国家同步爆发的广度上确实突出，烈度和全球性支持“一旦发生更严重、更全球”；但窗口内还有欧债、新冠金融冲击和2023年银行风波，“更少发生”只在与某些高频中小危机年代相比时部分成立。  
  来源：<https://www.foreignaffairs.com/articles/world/forgotten-history-financial-crisis-adam-tooze>；<https://www.imf.org/-/media/files/publications/wp/2026/english/wpiea2026094-source-pdf.pdf>；<https://www.fdic.gov/analysis/cfr/staff-studies/2020-02.pdf>

### 暂无法判断（1 条）

- **#5** 「the consequences of another such earthquake in Tokyo would be far costlier than that of its predecessor」  
  判断：**暂无法判断**。2007–2026年未发生与1923年关东大地震或1994年神户地震相当的东京都会区大地震；2011年东北太平洋近海地震震中在东北，不是作者所外推的“东京再来一次同类地震”，条件未满足，无法比较经济代价是否远超1923年。  
  来源：<https://www.jma.go.jp/jma/en/2011_Earthquake/Information_on_2011_Earthquake.html>；<https://www.swissre.com/en/japan/news-insights/articles/natural-catastrophes/100-year-legacy-japan-great-kanto-earthquake-japan.html>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/taleb-black-swan-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/taleb-black-swan-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/taleb-black-swan-v5/audit/manual_review_2026-11-15.py`

## 说明

- 所用文件为 2007 年初版，不含 2010 年第二版新增长文，不按第二版内容计分。
- 序言计入正文；致谢、术语表、注释、书目和索引不抽预测。
- 英文可解析密度：206 个保留块、约 71 万正文字符、23 条可解析预测，约每块 0.11 条、每 10 万字符约 3.2 条。低于英语预测密集书 0.2–0.35/块的参考区间，主要因为本书大部分是方法论、历史寓言和机制说明，而不是一份面向未来的命题清单；抽取来自逐块通读，未用非预测句凑数。
- 全部 23 条可评分预测均有 `data/sources/` 存档和 `data/evidence.jsonl` 记录。

