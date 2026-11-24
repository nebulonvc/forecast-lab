# Irving Fisher《The Purchasing Power of Money》（1920修订版）：出版后预测人工核查

- 案例目录：`cases/fisher-purchasing-power-of-money-v5/`
- 出版日期：1920修订版（原作1911；本案仅以1920为信息基准）
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

原TXT共291块，先前阅读账本记录已逐块全文通读；本轮不重复抽读。96原始候选经原v5确定性处理并修复连续引文后保留32条，30条resolvable。未使用关键词挑选替代全文阅读，亦未进行ASSESS语义duplicate。先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 30 条，剔除非预测 0 条，计入 **30 条预测**，其中 **17 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 7 |
| 趋势符合 | 0 |
| 部分符合 | 9 |
| 错误 | 1 |
| 暂无法判断 | 13 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **41.2%**（7/17） |
| 加权胜率 | **67.6%** |
| 错误率 | **5.9%**（1/17） |
| 未定占比（暂无法判断/预测） | 43.3%（13/30） |

## 总体评价

理论货币著作以机制、历史统计与政策方案为主，条件未实施与证据口径不匹配导致较多未定。货币制度、供金和价格方向需区别判断，不能把百年后物价上涨当全部黄金因果正确。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（7 条）

- **#6** 「The most careful review of present gold-mining con­ ditions shows that we may expect a continuance of gold inf…」  
  判断：**正确**。此处gold inflation按供金扩张而非物价必涨理解：统计显示世界黄金产量从1920年约1615万盎司增至1940年约4056万盎司，IMF的1950年供金统计也高于1920年；一代以上黄金供给扩张成立。  
  来源：<https://www66.statcan.gc.ca/eng/1942/194203650299_p.%20299.pdf>；<https://www.elibrary.imf.org/view/journals/024/1958/001/article-A004-en.xml>
- **#9** 「It must be remembered that it is the stock of gold and not the annual production which influences the price le…」  
  判断：**正确**。黄金年产量确有下降阶段，但仍有正产出；黄金协会说明黄金几乎不可毁灭，绝大部分历史产出仍存在且约三分之二在1950年后开采，符合年产减速后总存量仍累积的方向。  
  来源：<https://goldpercapita.com/research/gold-mine-production-history>；<https://www.gold.org/goldhub/data/how-much-gold>
- **#10** 「So the stock of gold will continue to increase long after the annual production of gold has stopped increasing…」  
  判断：**正确**。存档记录黄金产出在1940年后下降、战后多个地区产量停滞，而历史产出大部分仍作为地上库存存在；这支持年产停止增长并不立即阻止总存量继续增加。  
  来源：<https://www.allangray.co.za/latest-insights/markets-and-economy/gold-a-history-of-its-price/>；<https://www.gold.org/goldhub/data/how-much-gold>；<https://www.gold.org/goldhub/research/market-primer/gold-market-primer-market-size-and-structure>
- **#18** 「As soon as any particular government controls a paper currency bearing no relation to gold or silver, excuses …」  
  判断：**正确**。法币条件已现实存在，圣路易斯联储资料明确记录政府迫使央行过量印钞的通胀偏向以及津巴布韦极端通胀，所预警风险确曾出现。  
  来源：<https://www.stlouisfed.org/about-us/resources/why-fed-is-well-designed-central-bank/central-bank-independence-inflation>
- **#19** 「But the contracts based on index numbers would not be affected because made in terms of the index number. Doub…」  
  判断：**正确**。以指数调整金融契约的实践既遭到强烈政策争论，也吸引养老金等特定长期投资群体：英国1981年国债引入过程及养老金偏好研究均支持原句的两个组成部分。  
  来源：<https://oro.open.ac.uk/60077/8/60077.pdf>；<https://www.cnb.cz/en/economic-research/research-publications/cnb-working-paper-series/Hedging-Against-Inflation-International-Evidence-on-Investor-Clientele-Effects-00001/>；<https://www.bostonfed.org/-/media/Documents/neer/neer199a.pdf>
- **#29** 「Of the two terms constituting the “ first approxima­ tion,” the first and most important is susceptible of the…」  
  判断：**正确**。工资已可系统统计：ILOSTAT提供平均小时和月工资等多类表格，2026年调查记载81个报告国中68国在2020–2025年采集过收入数据，符合“将可用统计确定”的方向。  
  来源：<https://ilostat.ilo.org/topics/wages/>；<https://www.ilo.org/sites/default/files/2026-08/Earnings%20data%20collection%20practices%20survey%20report_0.pdf>
- **#30** 「I personally look forward to an upward tendency of prices in the future」  
  判断：**正确**。无日期方向按1920到截止日窗口判断：明尼阿波利斯联储所列美国CPI从1920年20.0上升至2025年321.9，长期物价上行成立，早期通缩不应把长期方向改记趋势。  
  来源：<https://www.minneapolisfed.org/about-us/monetary-policy/inflation-calculator/consumer-price-index-1913->；<https://www.bls.gov/opub/mlr/2014/article/one-hundred-years-of-price-change-the-consumer-price-index-and-the-american-inflation-experience.htm>

### 部分符合（9 条）

- **#1** 「Egypt awaits the advent of scientific agriculture, to usher in trade expansion.」  
  判断：**部分符合**。灌溉现代化与农业生产率改善确已发生，FAO记录2015年农业出口收入为十年前四倍，贸易扩张方向成立；但这不足以把增长全归因于原文未界定的“科学农业”。  
  来源：<https://www.oecd.org/en/publications/policies-for-the-future-of-farming-and-food-in-egypt_cab0cefd-en/full-report/the-agricultural-policy-context-in-egypt_d3486256.html>；<https://openknowledge.fao.org/server/api/core/bitstreams/5da9e6a6-5f9e-43c4-a42f-af5235dd97bd/content>
- **#3** 「Herein lies one of the weaknesses of bimetallism as a practical political proposition, — each country prefers …」  
  判断：**部分符合**。正式金银自由铸币复本位并未重建，但1933年美国提出的白银决议获66国采纳，八国随后签署白银协议；对率先行动和国际协议前景的判断过于悲观，不能仅凭未恢复完整本位给正确。  
  来源：<https://academic.oup.com/book/36016/chapter/313262062>；<https://en.wikipedia.org/wiki/Bimetallism>；<https://www.presidency.ucsb.edu/documents/proclamation-and-statement-ratifying-the-london-agreement-silver>；<https://history.state.gov/historicaldocuments/frus1933v01/d571>
- **#5** 「The outlook for the future is apparently toward a continued rise of prices due to a continued increase in the …」  
  判断：**部分符合**。长期物价上涨的方向出现：BLS记录1920年CPI年均20.0，2024年月值超过300；但金本位时期的严重通缩反驳了以黄金供给持续推动上涨的完整路径。  
  来源：<https://www.bls.gov/cpi/tables/supplemental-files/historical-cpi-u-202412.pdf>；<https://www.nber.org/system/files/chapters/c11482/c11482.pdf/>
- **#7** 「“ For at least thirty years we may count on an output of gold higher than, or at least comparable to, that of …」  
  判断：**部分符合**。后续黄金产量总体扩张且1930年代显著高于1910年代，但1921–1922年产量低于1920年，亦明显低于1910年代后期若干年份；“至少三十年”始终维持相当或更高产出的说法并不完整成立。  
  来源：<https://goldpercapita.com/research/gold-mine-production-history>
- **#8** 「This gold will come from the United States, Alaska, Mexico, the Transvaal, and other parts of Africa and Austr…」  
  判断：**部分符合**。加拿大统计证实1939年南非、美国、苏联（包括西伯利亚）是主要供金地；美国矿务局也记载1927年朝鲜有黄金产出，但玻利维亚、智利当时产量很小，不能确认整份地区名单及“稍后”顺序都实现。  
  来源：<https://www66.statcan.gc.ca/eng/1941/194103150253_p.%20253.pdf>；<https://digital.library.unt.edu/ark:/67531/metadc40311/m2/1/high_res_d/bomeconpapers_6_w.pdf>
- **#12** 「If we let imagination run a little ahead of our times, we may expect similar improvements in the future whereb…」  
  判断：**部分符合**。1960年代末出现低品位金矿堆浸并广泛应用，低品位开采部分兑现；MBARI明确指出海水含金浓度低到无法实现所述取金方案，海水分支未兑现。  
  来源：<https://www.mininghistoryassociation.org/Journal/MHJ-v28-2021-McQueen%20Heap%20Leaching%20in%20NV.pdf>；<https://www.mbari.org/wp-content/static/chemsensor/au/gold.html>
- **#20** 「A widow, or a trustee, or other long-time investor, would prefer to buy bonds which guaranteed a regular yearl…」  
  判断：**部分符合**。养老金基金确实超配通胀保值债，长期投资者的购买力保护需求得到支持；但保险机构反而低配，且零售及早期TIPS需求有限，不能把所有长期投资者或寡妇受托人都判作更偏好指数债。  
  来源：<https://www.cnb.cz/en/economic-research/research-publications/cnb-working-paper-series/Hedging-Against-Inflation-International-Evidence-on-Investor-Clientele-Effects-00001/>；<https://www.nber.org/reporter/2013number3/inflation-indexed-bonds>
- **#23** 「it would involve the trouble of translating money into the tabular standard and would therefore fail to attrac…」  
  判断：**部分符合**。公开资料确证公众对指数化有抵触，UF计算复杂性仍是缺点；但政府设立的UF又成功促进长期融资并被其他国家复制，原句关于实际吸引力和可推广性过于悲观。  
  来源：<https://www.brookings.edu/wp-content/uploads/1997/01/1997a_bpea_shiller_schultze_hall.pdf>；<https://obtienearchivo.bcn.cl/obtienearchivo?id=repositorio%2F10221%2F37432%2F2%2FInforme_BCN._UF_como_mecanismo_de_precios_y_casos_internacionales_FINAL.pdf>；<https://www.nber.org/papers/w6356>
- **#24** 「money into the tabular standard and would therefore fail to attract the public sufficiently to warrant its com…」  
  判断：**部分符合**。部分指数化确有增加通胀惯性的风险，但智利经验同时显示私人契约和长期金融市场获益，UF又扩散到其他国家；“弊端加剧并阻止继续推广”的两部分只得到部分支持。  
  来源：<https://repositoriodigital.bcentral.cl/xmlui/bitstream/handle/20.500.12580/3626/BCCh-sbc-v02-p001_018.pdf?isAllowed=y&sequence=1>；<https://www.nber.org/papers/w6356>

### 错误（1 条）

- **#13** 「the gold production of the future would continue excessive and probably cause the present rise of prices to co…」  
  判断：**错误**。该句强调让“当前上涨”在未来继续一段时间，但1920之后出现价格下跌，1930年代金本位相关的国际通缩尤其严重，方向与这一延续上涨路径相反。  
  来源：<https://www.nber.org/system/files/chapters/c11482/c11482.pdf/>；<https://www.federalreserve.gov/boarddocs/speeches/2004/200403022/>；<https://www.allangray.co.za/latest-insights/markets-and-economy/gold-a-history-of-its-price/>

### 暂无法判断（13 条）

- **#2** 「we may be tolerably confident that, if initially successful with the film near the middle 'position, internati…」  
  判断：**暂无法判断**。所检制度史记录的是1920年代恢复金本位，不是预测要求的、起初成功且金银比例居中的国际复本位实验；不能拿后来金本位崩溃判这个条件句错误。  
  来源：<https://academic.oup.com/book/36016/chapter/313262062>；<https://www.brookings.edu/wp-content/uploads/1982/01/1982a_bpea_cooper_dornbusch_hall.pdf>
- **#4** 「The silver dollars (and there­ fore the silver certificates) maintain their value on a parity with gold primar…」  
  判断：**暂无法判断**。1933年黄金兑付暂停、1963年银券停止发行均有存档，但未找到银元/银券自身黄金平价遭疑后财政部是否提出“专门以黄金赎回”的直接记录。  
  来源：<https://www.federalreservehistory.org/essays/roosevelts-gold-program>；<https://www.bep.gov/system/files/2022-02/factsheet-silvercertificate-20130425.pdf>
- **#11** 「That for many years, however, gold will outrun trade seems probable, for the reason that there is no immediate…」  
  判断：**暂无法判断**。WTO资料显示1950后国际贸易扩张远快于黄金总量，但书中trade还包含国内交易量，且“未来许多年”从1920年起；现有跨期与口径不同的序列不能直接证明该句正确或错误。  
  来源：<https://www.wto.org/english/res_e/statis_e/trade_evolution_e/evolution_trade_wto_e.htm>；<https://www.gold.org/goldhub/data/how-much-gold>
- **#14** 「I cannot but believe that the diffusion among business men of the fuller knowledge of the equation of exchange…」  
  判断：**暂无法判断**。央行政策学习与企业财务教育改善表现均有证据，也有2008年企业预测普遍失准的反证；但没有识别商界普及交换方程、存款与信用周期知识对危机总体损失的独立影响。  
  来源：<https://www.stlouisfed.org/the-great-depression/online-resources/-/media/project/frbstl/stlouisfed/files/pdfs/great-depression/wheelock_march_april_2010_review.pdf>；<https://www.cfo.com/news/future-tense/670930/>；<https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3696377>
- **#15** 「There has been for centuries, and promises to be for centuries to come, a race between money and trade.」  
  判断：**暂无法判断**。原文明确把竞逐持续时间写为未来几个世纪，1920到截止日只覆盖其中一部分；现有货币及贸易研究不足以确认整个承诺时段。  
  来源：<https://link.springer.com/article/10.1007/s11079-023-09739-0?code=23fcc2ac-2754-41e7-a943-9b13d0b8c5fd&error=cookies_not_supported>；<https://www.imf.org/-/media/files/publications/esr/2025/english/ch2.pdf>
- **#16** 「Bimetallism, then, even could it be maintained, would offer but an indifferent remedy for the variations in th…」  
  判断：**暂无法判断**。版后重建的主要是金本位而非两金属自由铸币的复本位制度；没有满足原句前提的版后持续实验，不能用19世纪格雷欣法则史实直接判对。  
  来源：<https://academic.oup.com/book/36016/chapter/313262062>；<https://en.wikipedia.org/wiki/Bimetallism>
- **#17** 「that of poly­ metallism looks to the contemporaneous circulation of more than two. So long as several metals c…」  
  判断：**暂无法判断**。搜索得到的瑞典三金属经验发生在1624–1776年，早于本版；1920年代满洲多币并行则缺少作者要求的共同固定多金属本位前提，不能用来判必然驱逐结论。  
  来源：<https://doi.org/10.1093/ereh/hes007>；<https://crossworks.holycross.edu/cgi/viewcontent.cgi?article=1096&context=econ_working_papers>
- **#21** 「The beginnings of such a plan for “ a tabular standard of value” could be made at any time by private con­ tra…」  
  判断：**暂无法判断**。存档记载1925年Rand Kardex指数债实验并不成功、债券后来被黄金条款债替换，未满足“试验总体使当事人满意”的前提；不能以当时没有模仿者把条件句判错。  
  来源：<https://www.richmondfed.org/-/media/RichmondFedOrg/publications/research/economic_review/1974/pdf/er600601.pdf>；<https://doi.org/10.3386/w10183>
- **#22** 「The system of making contracts in terms of the price level is not intended directly to prevent fluctuations in…」  
  判断：**暂无法判断**。现实存在指数化金融合约，但NBER说明UF尚非支付媒介，其他文献也只是部分市场实践或模型；并未出现原句所设想的普遍以购买力计价的完整契约体系，不能拿模型结论当实现。  
  来源：<https://www.nber.org/papers/w6356>；<https://fraser.stlouisfed.org/files/docs/historical/frbclev/wp/frbclv_2011-17.pdf>；<https://www.imf.org/external/pubs/ft/wp/wp9815.pdf>
- **#25** 「So simple are the duties of maintaining the goldexchange par, and so unfailingly has the system been faithfull…」  
  判断：**暂无法判断**。战间期金汇兑制度确有政策失灵；补查也找到菲律宾准备金挪用，但明确挪用发生于1918年，不能把版前事实算1920后的反证。尚缺本版之后与原句简单操作制度严格对应的新滥用记录。  
  来源：<https://academic.oup.com/book/36016/chapter/313262062>；<https://www.jstage.jst.go.jp/article/sea1971/2001/30/2001_30_3/_article/-char/en>；<https://hal.science/hal-00375342v1>
- **#26** 「It will be seen that the plan here proposed requires no revolution of the world’s currencies. It requires lit­…」  
  判断：**暂无法判断**。Bordo等文献明确称Fisher补偿美元计划从未实施；原句关于实施后仍用熟悉货币、普通人无感的后果因此不能实际验收。  
  来源：<https://files.stlouisfed.org/files/htdocs/wp/2003/2003-014.pdf>；<https://www.richmondfed.org/-/media/RichmondFedOrg/publications/research/economic_quarterly/1993/summer/pdf/patinkin.pdf>
- **#27** 「The danger of abuse or fraud in the Statistical Office, the work of which is based on published market prices …」  
  判断：**暂无法判断**。方案未实施，因此也没有方案所设国际统计局的实际舞弊率可供检验；一般统计机关的公开价格工作不能替代该机构。  
  来源：<https://files.stlouisfed.org/files/htdocs/wp/2003/2003-014.pdf>
- **#28** 「No in­ dividual nation could inflate the currency without withdrawing from the international arrangement and i…」  
  判断：**暂无法判断**。国际补偿美元安排未落地，无法观测参与该特定协议的国家是否会同时立通胀法；后来脱离金本位的共同扩张并不满足这个条件。  
  来源：<https://files.stlouisfed.org/files/htdocs/wp/2003/2003-014.pdf>；<https://www.richmondfed.org/-/media/RichmondFedOrg/publications/research/economic_quarterly/1993/summer/pdf/patinkin.pdf>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/fisher-purchasing-power-of-money-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/fisher-purchasing-power-of-money-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/fisher-purchasing-power-of-money-v5/audit/manual_review_2026-11-15.py`
本轮原首轮68条检索未重复；第二轮20条，另按缺口改变策略补5条自适应（全球总交易量、商界知识因果、金汇兑滥用、多金属本位实例、银元银券平价前提）。清空context后逐条扩连续引文，原代码新增3条overlap删除及1条historical屏蔽；详见audit/quote-review-map.json。
