# 约翰·梅纳德·凯恩斯《和平的经济后果》（The Economic Consequences of the Peace）：出版后预测人工核查

- 案例目录：`cases/keynes-economic-consequences-of-the-peace-v5/`
- 出版日期：**1919 年 12 月**（Macmillan，伦敦）。正文为 Project Gutenberg #15776，`reading-library/2026-11-15-未来判断扩展100本/04-经济与资源/061-the-economic-consequences-of-the-peace.txt`，sha256 `47c9ba595e2ea6c1fe2ead0c34ad5c145cb73bc5d9521338a7af4a5e4aff2a81`。观察窗口为 1919-12→2026-11-15；书中明示的终点（1919 年底、1921 年 5 月前、1920-21 年等）分别适用。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

本稿按 METHOD.md 执行。抽取：用仓库 prepare_book v5 流水线（toolkit 85e6da1）把全文切成 131 块（3500 字符、600 字符上下文；第 126 块后半至第 131 块为 Project Gutenberg 许可文本，无预测）。助手逐块通读，按 DISCOVER_PROMPT_V5 写出模型本应返回的 JSON，再由仓库代码完成引文对齐、归属降级、去重和导入，得到 117 条候选，其中 84 条可核验预测（约 0.64 条/块，约 18.5 条/10 万字符）。本书后半部分几乎全是对赔款、煤炭、战债和欧洲前途的明确预测，所以密度高于一般非虚构。核验：按 25 个主题先写 scope，各做一次 support 和一次 counter 的 Exa 检索，第二轮 12 个主题补检，第三轮 1 组自适应检索（5 条），共 79 次检索（连同存档抓取共 91 次 Exa 请求），只使用检索返回的 URL。原文存档于 data/sources（86 份，sha256），写入 data/evidence.jsonl（86 条）。由助手阅读后按四分类规则评断，再经 pipeline.py apply assess → check → report。本稿由助手逐条对照书中原文与存档证据人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 84 条，剔除非预测 0 条，计入 **84 条预测**，其中 **59 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 22 |
| 趋势符合 | 7 |
| 部分符合 | 14 |
| 错误 | 16 |
| 暂无法判断 | 25 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **37.3%**（22/59） |
| 加权胜率 | **58.1%** |
| 错误率 | **27.1%**（16/59） |
| 未定占比（暂无法判断/预测） | 29.8%（25/84） |

## 总体评价

凯恩斯对赔款问题的核心判断大多被历史证实：德国不可能履行和约的全部赔款义务；1921 年伦敦支付计划最终定出的 1320 亿金马克（约 330 亿美元）落在他估计的 320 亿–440 亿美元区间，且其中 820 亿只存在于纸面；德国到 1931 年实际只付了约 200 亿金马克，远低于每年 39 亿美元或 30 年每年 5 亿美元的设想；首期 200 亿金马克未能在 1921 年 5 月前付清；德国交煤远低于每年 4000 万吨；法意竭力强制执行煤炭条款并导致鲁尔危机；协约国间战债成为长期摩擦，最终在 1932–34 年停付；赔款与战债都没有长期支付下去；法国 1919 年的巨额入超难以为继；俄国出现饥荒、出口恢复缓慢；英国未发生社会剧变。主要误判集中在他的悲观经济判断和若干具体机制上：美国在 1920 年代每年都有大量小麦出口剩余，1920–21 年小麦价格暴跌而不是稀缺昂贵，粮食实际成本在 20 世纪持续下降，战后德国很快恢复煤炭出口，德国南美电力公司没有被交给协约国而是转为西班牙的 CHADE，莱茵兰在 1930 年提前撤军，第 231 条的重要性此后反而上升，拉帕洛条约使苏俄与魏玛德国走到一起，西欧没有发生革命，国联也未能阻止大国战争。对奥地利、法意财政和欧洲生活水平的判断只部分应验：1919–23 年确有深重困难，但 1924–29 年出现稳定和复苏。比利时战损、首期付款中金银与证券的构成等细项缺乏可核对的来源，记为暂无法判断。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（22 条）

- **#7** 「the United States can hardly be expected to continue indefinitely to raise by a substantial figure the cost of…」  
  判断：**正确**。战时保证小麦价格未被无限期延续：美国粮食公司于1920年8月按行政令清算，1920年7月农产品价格崩跌，小麦从1919年每蒲式耳2.16美元降至1921年1.03美元。  
  来源：<https://www.presidency.ucsb.edu/documents/executive-order-3320-liquidation-united-states-grain-corporation>；<https://www.ers.usda.gov/media/10790/historical-overview-of-us-agricultural-policies-and-programs.pdf?v=31426>
- **#14** 「But it is evident that Germany cannot and will not furnish the Allies with a contribution of 40,000,000 tons a…」  
  判断：**正确**。Spa会议把德国交煤定为每月200万吨（年约2400万吨），1921-22年实际按赔款账户月均约150万吨，远低于每年4000万吨。  
  来源：<https://history.state.gov/historicaldocuments/frus1920v02/d347>；<https://api.parliament.uk/historic-hansard/commons/1924/feb/27/coal-and-coke-delivery>
- **#16** 「the coal clauses will not be lost sight of so easily,--for the reason that it will be absolutely vital in the …」  
  判断：**正确**。Spa会议上协约国在煤炭问题上不肯让步并以制裁相威胁；1923年法国又因德国赔付不足占领鲁尔，法意确实竭力强制执行。  
  来源：<https://en.wikipedia.org/wiki/Spa_Conference_of_1920>；<https://en.wikipedia.org/wiki/World_War_I_reparations>
- **#20** 「France, having recovered the deposits of Lorraine, may be expected to aim at replacing as far as possible the …」  
  判断：**正确**。法国战后扩张本国钢铁工业：1929年接近满负荷时生产约1010万吨生铁、970万吨粗钢，并于1926年参与国际钢铁卡特尔。  
  来源：<https://documents1.worldbank.org/curated/en/581841468281387936/pdf/NonAsciiFileName0.pdf>；<https://en.wikipedia.org/wiki/International_Steel_Agreement>
- **#27** 「Since it will be impossible for Germany to fulfil the whole of her Reparation obligations」  
  判断：**正确**。德国最终远未履行赔款义务：1320亿金马克中820亿只存在于纸面，1920-1931年实际支付约200亿金马克。  
  来源：<https://www.historyskills.com/classroom/year-10/versailles-reparations-paid/>；<https://en.wikipedia.org/wiki/World_War_I_reparations>
- **#33** 「at the figure of $150 per gross ton, which with the rapid growth of shipbuilding may soon be too high」  
  判断：**正确**。战后航运投机热在1921年随运价崩溃而终结，船厂因运价市场崩溃而倒闭，船舶重置价格很快显得过高。  
  来源：<https://www.cdforskning.no/cdf/catalog/view/202/1165/9754>；<https://www.gracesguide.co.uk/Newcastle_Shipbuilding_Co>
- **#36** 「we have a total claim against Germany of $40,000,000,000.[108] I believe that this figure is fully high enough…」  
  判断：**正确**。1921年伦敦支付计划最终确定1320亿金马克，约合当时330亿美元，确实略低于400亿美元。  
  来源：<https://en.wikipedia.org/wiki/World_War_I_reparations>；<https://www.historyskills.com/classroom/year-10/versailles-reparations-paid/>
- **#38** 「my conclusions in the next section of this chapter indicate that this sum cannot be found within the period in…」  
  判断：**正确**。赔款委员会认定德国到1921年春的交付最多约80亿金马克，并要求在1921年5月1日前付清剩余120亿金马克，德国未能付清首期200亿金马克（约50亿美元）。  
  来源：<https://apps.bundesarchiv.de/aktenreichskanzlei/1919-1933/0001/feh/feh1p/kap1_2/kap2_213/para3_4.html>；<https://archive.spectator.co.uk/article/23rd-april-1921/2/germany-shows-no-intention-of-paying-by-may-1st-th>
- **#39** 「It is, in my judgment, as certain as anything can be, for reasons which I will elaborate in a moment, that Ger…」  
  判断：**正确**。德国1920-1931年实际支付约200亿金马克，远低于每年39亿美元（约156亿金马克）的水平。  
  来源：<https://www.historyskills.com/classroom/year-10/versailles-reparations-paid/>；<https://statecraftencyclopedia.org/entries/dawes-and-young-plans-1924-1930/>
- **#45** 「the social and economic condition of Germany cannot possibly permit a surplus of exports over imports during t…」  
  判断：**正确**。战后德国出口比进口下降更多，贸易逆差大于战前，1921年5月前并未出现出口顺差。  
  来源：<https://fraser.stlouisfed.org/files/docs/publications/FRB/pages/1920-1924/26600_1920-1924.pdf>；<https://www.diw.de/documents/publikationen/73/diw_01.c.400717.de/31-45.pdf>
- **#50** 「I doubt if Germany could be made to pay this sum annually over a period of 30 years」  
  判断：**正确**。道威斯计划年金从10亿金马克升到25亿金马克（约6亿美元）后难以为继，依赖美国贷款，1931年胡佛延期偿付、1932年终止，远未持续30年。  
  来源：<https://statecraftencyclopedia.org/entries/dawes-and-young-plans-1924-1930/>；<https://en.wikipedia.org/wiki/Hoover_Moratorium>
- **#51** 「$10,000,000,000 is a safe maximum figure of Germany's capacity to pay. In all the actual circumstances, I do n…」  
  判断：**正确**。德国1920-1931年实际支付约200亿金马克（约50亿美元），低于100亿美元。  
  来源：<https://www.historyskills.com/classroom/year-10/versailles-reparations-paid/>；<https://en.wikipedia.org/wiki/World_War_I_reparations>
- **#53** 「the sum when fixed will prove in excess of what can be paid in cash and in excess also of what can be paid at …」  
  判断：**正确**。1921年确定的1320亿金马克中有820亿只存在于纸面，实际仅支付约200亿，确定的总额超过了德国实际支付能力。  
  来源：<https://www.historyskills.com/classroom/year-10/versailles-reparations-paid/>；<https://en.wikipedia.org/wiki/World_War_I_reparations>
- **#54** 「If the promised negotiations are really conducted on these lines, they are not likely to be fruitful. It will …」  
  判断：**正确**。赔款总额直到1921年5月5日伦敦支付计划才确定，1919年底前并无一次性总额协议。  
  来源：<https://history.state.gov/historicaldocuments/frus1919Parisv13/ch34subch4>；<https://en.wikipedia.org/wiki/World_War_I_reparations>
- **#57** 「I estimate for this figure an accuracy of 10 per cent in deficiency and 20 per cent in excess, _i.e._ that the…」  
  判断：**正确**。最终确定的1320亿金马克约合当时330亿美元，落在320亿-440亿美元区间内。  
  来源：<https://en.wikipedia.org/wiki/World_War_I_reparations>；<https://www.historyskills.com/classroom/year-10/versailles-reparations-paid/>
- **#59** 「Russia, as much by reason of deficient transport as of diminished output, may herself starve」  
  判断：**正确**。1921-1922年俄国（伏尔加地区）发生大饥荒，死亡人数估计约500万。  
  来源：<https://warwick.ac.uk/services/library/mrc/collections/digital/russia/famine/>；<https://en.wikipedia.org/wiki/Russian_famine_of_1921%E2%80%9322>
- **#63** 「The internal economy of France and its price level in relation to the note circulation and the foreign exchang…」  
  判断：**正确**。法国1919年贸易逆差达240亿法郎，此后改善：1921年进口降至3800万吨（1920年5000万吨），出口增加，巨额入超未能持续。  
  来源：<https://en.wikisource.org/wiki/Page:EB1926_-_Supplement_Volume_2.pdf/131>；<https://fraser.stlouisfed.org/files/docs/publications/FRB/pages/1920-1924/26040_1920-1924.pdf>
- **#65** 「French imports cannot possibly continue at anything approaching these figures, and the semblance of prosperity…」  
  判断：**正确**。法国进口量1921年降至3800万吨，比1920年的5000万吨显著减少，未能维持在接近1919年的水平。  
  来源：<https://fraser.stlouisfed.org/files/docs/publications/FRB/pages/1920-1924/26040_1920-1924.pdf>；<https://en.wikisource.org/wiki/Page:EB1926_-_Supplement_Volume_2.pdf/131>
- **#66** 「I do not perceive in England the slightest possibility of catastrophe or any serious likelihood of a general u…」  
  判断：**正确**。英国战后未发生灾难或全面社会动荡；1926年大罢工持续约9天后结束，未推翻政府。  
  来源：<https://www.nationalarchives.gov.uk/explore-the-collection/stories/the-general-strike/>；<https://www.historytoday.com/archive/feature/general-strike>
- **#71** 「France would be a loser on paper (on paper only, for she will never secure the actual fulfilment of her presen…」  
  判断：**正确**。法国从未得到其赔款要求的实际兑现：总额中820亿金马克只存在于纸面，德国实际只支付约200亿金马克。  
  来源：<https://www.historyskills.com/classroom/year-10/versailles-reparations-paid/>；<https://api.parliament.uk/historic-hansard/commons/1932/feb/11/german-reparations>
- **#73** 「They may be expected, therefore, to make constant attempts to evade or escape payment, and these attempts will…」  
  判断：**正确**。战债成为长期摩擦：法国1932年、英国1934年先后停止对美偿还，英国留下逾40亿美元未付，美国随后通过约翰逊法。  
  来源：<https://ehs.org.uk/the-uks-unpaid-war-debts-to-the-united-states-1917-1980/>；<https://gripe.polisci.ucla.edu/wp-content/uploads/sites/121/2022/09/GRIPE_S06E02_GILL.pdf>
- **#80** 「The process of reviving the Russian export trade is bound in any case to be a slow one.」  
  判断：**正确**。俄国粮食出口1923年后才恢复，且远小于战前、更不稳定，恢复确实缓慢。  
  来源：<https://doi.org/10.2307/1230111>；<https://www.ssoar.info/ssoar/bitstream/handle/document/91436/ssoar-russanald-2023-304-asschenfeldt-Russias_Food_Power_in_the.pdf>

### 趋势符合（7 条）

- **#1** 「by a Peace which, if it is carried into effect, must impair yet further, when it might have restored, the deli…」  
  判断：**趋势符合**。和约赔款条款的执行引发1923年法比占领鲁尔与德国恶性通胀，欧洲战后经济秩序进一步动荡；但1924年道威斯计划后出现复苏，方向一致而非全面应验。  
  来源：<https://en.wikipedia.org/wiki/World_War_I_reparations>；<https://alphahistory.com/weimarrepublic/1923-hyperinflation/>；<https://doi.org/10.1007/978-1-349-00298-6_21>
- **#37** 「it gives to the Reparation Commission a discretion, which the force of facts will compel them to exercise, to …」  
  判断：**趋势符合**。1924年道威斯计划改组赔款委员会，大幅削减德国支付并按能力分级，实质上把维持德国经济所需让给德国，方向一致；但并非委员会按条约自由裁量主动返还。  
  来源：<https://doi.org/10.1007/978-0-230-62949-3_3>；<https://history.state.gov/milestones/1921-1936/dawes>
- **#52** 「Germany's annual savings, after what she has suffered in the war and by the Peace, will fall far short of what…」  
  判断：**趋势符合**。1923年恶性通胀吞噬了德国的储蓄，退休者的毕生积蓄化为乌有，方向一致；来源未给出年度储蓄额的对比。  
  来源：<https://www.richmondfed.org/publications/research/econ_focus/2014/q1/book_review>；<https://alphahistory.com/weimarrepublic/1923-hyperinflation/>
- **#60** 「Austria will have consumed the whole of her own harvest for 1919 before the end of the calendar year.」  
  判断：**趋势符合**。1919年12月英国政府称奥地利粮食形势危急，1919-20年冬维也纳靠美国救济避免儿童饿死，说明本国收成不足以支撑到年底以后，方向一致；来源未直接给出收成耗尽的日期。  
  来源：<https://api.parliament.uk/historic-hansard/commons/1919/dec/16/relief-measures>；<https://www.nzz.ch/international/amerikanische-hilfe-rettete-nach-dem-ersten-weltkrieg-eine-generation-oesterreicher-vor-dem-hungertod-ld.1528199>
- **#68** 「Great privation and great risks to society have become unavoidable.」  
  判断：**趋势符合**。1919年中欧缺煤缺粮、工业停工，1917-1923年革命浪潮与动荡出现，方向一致；但未形成全面社会崩溃。  
  来源：<https://history.state.gov/historicaldocuments/frus1919Parisv12/d75>；<https://en.wikipedia.org/wiki/Revolutions_of_1917%E2%80%931923>
- **#69** 「Yet the League in the hands of the trained European diplomatist may become an unequaled instrument for obstruc…」  
  判断：**趋势符合**。盟约第19条修约机制实际未发挥作用：1935年英国政府仍拒绝为第19条设立执行机制；赔款修订是在国联之外（道威斯计划）完成的，方向一致。  
  来源：<https://api.parliament.uk/historic-hansard/commons/1935/jul/10/treaties-revision>；<https://doi.org/10.1007/978-0-230-62949-3_3>
- **#75** 「In short, I do not believe that any of these tributes will continue to be paid, at the best, for more than a v…」  
  判断：**趋势符合**。赔款在1931年胡佛延期偿付后于1932年实际终止，战债也于1932-34年停付，确实没有长期支付；但前后支付了十余年，比“很少几年”长，方向一致。  
  来源：<https://en.wikipedia.org/wiki/Hoover_Moratorium>；<https://ehs.org.uk/the-uks-unpaid-war-debts-to-the-united-states-1917-1980/>

### 部分符合（14 条）

- **#9** 「Thus the German mercantile marine is swept from the seas and cannot be restored for many years to come on a sc…」  
  判断：**部分符合**。德国商船队1920年仅剩约67万总吨（战前约513万），但到1924年已收复一半以上损失，恢复比“多年内无法恢复”更快，只部分应验。  
  来源：<https://www.shippingwondersoftheworld.com/m/german_shipping.html>；<https://www.historyworm.com/gazete/evening_star/1924-07-10/22>
- **#11** 「it is improbable that the powers of the Central Government will be adequate to restore them to their former fi…」  
  判断：**部分符合**。矿工7小时班确实被视为革命成果、难以由政府恢复；但1923年10月鲁尔矿主单方面把井下工时由7小时延长到8.5小时，1924年仲裁又把加班限期保留，原工时一度被恢复，只部分应验。  
  来源：<https://www.zeit.de/1983/48/heisser-herbst-vor-60-jahren>；<https://library.fes.de/fulltext/bibliothek/chronik/band2/e235f499.html>
- **#12** 「The pre-war figure of 118,000,000 tons net (_i.e._ after allowing for loss of territory and consumption at the…」  
  判断：**部分符合**。德国（现疆界、不含萨尔）煤产量由1913年1.409亿吨降至1920年1.084亿吨、1921年1.139亿吨，下降方向应验；但1925年已回升到1.327亿吨，且凯恩斯所用“净产量”口径与来源不同，只部分应验。  
  来源：<https://marxists-malta.org/archive/varga/1923/03/ruhr.htm>；<https://www.persee.fr/doc/geo_0003-4010_1926_num_35_196_8475>
- **#18** 「the industrial ruin of this latter state, if she cannot obtain coal from Germany, will be complete」  
  判断：**部分符合**。1919年奥地利因严重缺煤，工业普遍停工或极小规模运转；但前提（是否得不到德国煤）无法确认，且1922年国联贷款后奥地利重建，只部分应验。  
  来源：<https://history.state.gov/historicaldocuments/frus1919Parisv12/d75>；<https://www.aeiou.at/aeiou.encyclop.v/v673835_en.htm>
- **#25** 「The further heavy losses under the Treaty will confirm this state of affairs for some time to come」  
  判断：**部分符合**。1920年合并成立的德国国铁的经营亏损是政府赤字的重要直接原因之一，1921-23年预算持续为负；但来源未直接说明机车车辆损失导致低效，只部分应验。  
  来源：<https://thebhc.org/sites/default/files/beh/BEHprint/v027n2/p0477-p0485.pdf>；<https://www.nuffield.ox.ac.uk/economics/history/paper13/13paper.pdf>
- **#32** 「when the inevitable enlightenment comes, as it soon must (both as to their own claims and as to Germany's capa…」  
  判断：**部分符合**。法国因占领鲁尔后仍未收到赔款，1924年5月选举左翼联盟获胜、政府更迭，1924-26年出现信用危机；但未波及社会秩序，只部分应验。  
  来源：<https://en.wikipedia.org/wiki/Cartel_des_Gauches>；<https://financialhistoryinstitute.com/publications/french-floating-debt-crisis-1924-1926>
- **#34** 「Indeed, the position was and remains nearly hopeless. These countries were heading for national bankruptcy.」  
  判断：**部分符合**。法国1924-26年濒临违约但并非财政破产，1926-28年普恩加莱稳定法郎；意大利公债1921年约达GDP的180%，1924-25年预算出现盈余；法国1932年停付对美战债。只部分应验。  
  来源：<https://financialhistoryinstitute.com/publications/french-floating-debt-crisis-1924-1926>；<https://www.elibrary.imf.org/display/book/9781513511795/ch005.xml>；<https://gripe.polisci.ucla.edu/wp-content/uploads/sites/121/2022/09/GRIPE_S06E02_GILL.pdf>
- **#40** 「we may assume that the Reparation Commission will judge it imprudent, having regard to the reaction on their f…」  
  判断：**部分符合**。帝国银行黄金并未被没收；但1921年4月赔款委员会曾要求把全部约11亿金马克黄金转移到被占区作担保，遭德国拒绝，委员会并非完全回避此事，只部分应验。  
  来源：<https://www.usni.org/magazines/proceedings/1921/june/notes-international-affairs>；<https://apps.bundesarchiv.de/aktenreichskanzlei/1919-1933/00r1/wir/wir1p/kap1_2/kap2_175/para3_1.html>
- **#56** 「So long as such statements can be accepted in Paris without protest, there can be no financial or economic fut…」  
  判断：**部分符合**。1924-26年法国出现法郎危机和政府频繁更迭，但并非财政无前途，1926年后普恩加莱稳定了财政，只部分应验。  
  来源：<https://financialhistoryinstitute.com/publications/french-floating-debt-crisis-1924-1926>；<https://www.persee.fr/doc/etudo_1241-3496_1995_num_7_1_1104>
- **#64** 「Thus the menace of inflationism described above is not merely a product of the war, of which peace begins the …」  
  判断：**部分符合**。通胀确实延续到1923年德国恶性通胀和1926年法国物价飞涨，但1924-1928年各国相继稳定货币，并非“看不到尽头”，只部分应验。  
  来源：<https://alphahistory.com/weimarrepublic/1923-hyperinflation/>；<https://www.persee.fr/doc/etudo_1241-3496_1995_num_7_1_1104>
- **#70** 「If we aim deliberately at the impoverishment of Central Europe, vengeance, I dare predict, will not limp. Noth…」  
  判断：**部分符合**。1930年代确实出现纳粹上台和比一战更惨烈的第二次世界大战，舆论常称凯恩斯“预言了纳粹德国”；但前提“蓄意使中欧贫困化”是否成立有争议，形态也不是反动与革命的“内战”，只部分应验。  
  来源：<https://www.nytimes.com/2019/12/07/opinion/keynes-economic-consequences-peace.html>；<https://www.bbc.co.uk/bitesize/guides/zsrwjxs/revision/4>
- **#74** 「There is no European country in which repudiation may not soon become an important political issue.」  
  判断：**部分符合**。赖账确实成为法、英的重要政治议题并在大萧条中付诸实施，但来源只涉及主要债务国，“任何欧洲国家”与“很快”未得到证实，只部分应验。  
  来源：<https://gripe.polisci.ucla.edu/wp-content/uploads/sites/121/2022/09/GRIPE_S06E02_GILL.pdf>；<https://ehs.org.uk/the-uks-unpaid-war-debts-to-the-united-states-1917-1980/>
- **#82** 「I see few signs of sudden or dramatic developments anywhere. Riots and revolutions there may be, but not such,…」  
  判断：**部分符合**。1920年卡普政变失败并被总罢工挫败，未产生根本性变化；但1923年鲁尔危机与恶性通胀属于突然的剧烈事件，只部分应验。  
  来源：<https://www.deutschlandmuseum.de/en/history/calendar/1920-03-13-government-forced-to-flee-berlin/>；<https://alphahistory.com/weimarrepublic/1923-hyperinflation/>
- **#83** 「There may, therefore, be ahead of us a long, silent process of semi-starvation, and of a gradual, steady lower…」  
  判断：**部分符合**。战后欧洲经济长期不振、两次大战之间常被视为停滞期，但1925-1929年经济迅速扩张，到1925年复苏已明显，“漫长的半饥饿和生活水平逐步下降”只部分应验。  
  来源：<https://doi.org/10.1007/978-1-349-00298-6_21>；<https://johnquiggin.com/2021/02/18/economic-lessons-of-the-20-year-armistice/>

### 错误（16 条）

- **#5** 「the date was evidently near when there would be an exportable surplus only in years of exceptionally favorable…」  
  判断：**错误**。1922-27年美国小麦出口平均每年1.8亿蒲式耳，占世界小麦贸易约23%；1921年美国谷物出口按蒲式耳计比1920年多60%，并非只在特别丰收年份才有出口剩余。  
  来源：<https://ia600107.us.archive.org/23/items/CAT31392819/CAT31392819.pdf>；<https://www.historyworm.com/gazete/seattle_star/1921-12-26/14>
- **#6** 「the pre-war scale of production in the United States would only show a substantial surplus over present domest…」  
  判断：**错误**。1922-27年五年间美国小麦出口平均每年1.8亿蒲式耳，持续有大量剩余出口，并非约五年一次才有可观剩余。  
  来源：<https://ia600107.us.archive.org/23/items/CAT31392819/CAT31392819.pdf>；<https://www.historyworm.com/gazete/seattle_star/1921-12-26/14>
- **#10** 「they could pick out--as presumably they will as soon as they are established--the fine and powerful German ent…」  
  判断：**错误**。D.U.E.G.（CATE）并未被赔款委员会处置给协约国利益方：股东为避免没收将其“去德国化”，1920年改组为西班牙公司CHADE。  
  来源：<https://raco.cat/index.php/Dictatorships-Democracies/article/download/n5-castells/431548/491221>；<https://es.wikipedia.org/wiki/CHADE-CADE>
- **#13** 「Germany cannot export coal in the near future (and will even be dependent on her Treaty rights to purchase in …」  
  判断：**错误**。德国在1921、1922年每月按赔款账户交付约150万吨煤（含焦炭），1925年英国已视德国为最主要的煤炭出口竞争对手，“近期不能出口煤炭”未应验。  
  来源：<https://api.parliament.uk/historic-hansard/commons/1924/feb/27/coal-and-coke-delivery>；<http://archive.spectator.co.uk/article/5th-september-1925/7/german-coal-competition>
- **#28** 「the effect of the above provisions will be in practice that the Allies will occupy the left bank of the Rhine …」  
  判断：**错误**。协约国并未无限期占领莱茵兰：占领于1930年6月30日结束，比和约规定的期限更早。  
  来源：<https://en.wikipedia.org/wiki/Occupation_of_the_Rhineland>；<https://thesecondwar.pl/en/end-of-the-occupation-of-the-rhineland>
- **#31** 「In short, it will be difficult to establish a bill exceeding $2,500,000,000 for _physical and material_ damage…」  
  判断：**错误**。法国政府估计物质战损修复总额约1000亿法郎（约8亿英镑金价），远超25亿美元，“难以确立超过25亿美元的账单”未应验。  
  来源：<https://api.parliament.uk/historic-hansard/commons/1932/feb/11/german-reparations>；<https://www.academia.edu/47548031/After_the_Ruins_Restoring_the_Countryside_of_Northern_France_after_the_Great_War>
- **#35** 「which probably seemed much more important at the time than it ever will again between now and Judgment Day」  
  判断：**错误**。第231条后来成为德国抗拒凡尔赛和约的焦点，德国外交部在1920年代开展“战争罪责”宣传，纳粹也利用对和约的怨恨，其重要性并未消退。  
  来源：<https://doi.org/10.7202/030859ar>；<https://www.bbc.co.uk/bitesize/guides/zsrwjxs/revision/4>
- **#49** 「(6) Cereals. There never was and never can be a net export.」  
  判断：**错误**。当代德国已能以本国谷物满足自身需求（2018年大旱为例外），谷物自给率超过100%意味着可净出口，“永远不可能成为净出口”未应验。  
  来源：<https://www.agrarheute.com/markt/marktfruechte/hat-deutschland-genug-getreide-um-versorgen-fakten-591301>；<https://bmel-statistik.de/ernaehrung/versorgungsbilanzen/getreide>
- **#55** 「In point of fact, however, we may safely assume that literal restoration will never be attempted.」  
  判断：**错误**。法国北部确实进行了大规模恢复性重建：到1931年恢复340万公顷土地和834,516栋建筑，1919年法律按毁前价值赔偿，重建在很大程度上恢复了原有面貌。  
  来源：<https://www.academia.edu/47548031/After_the_Ruins_Restoring_the_Countryside_of_Northern_France_after_the_Great_War>；<https://anabf.org/pierredangle/dossiers/construire-dans-l-existant/le-caractere-trompeur-dun-expression-aux-usages-multiples-a-l-identique>
- **#62** 「In the complexer world of Western Europe the Immanent Will may achieve its ends more subtly and bring in the r…」  
  判断：**错误**。1917-1923年革命浪潮在西欧没有成功，西欧各国未发生革命。  
  来源：<https://en.wikipedia.org/wiki/Revolutions_of_1917%E2%80%931923>；<https://www.nationalarchives.gov.uk/explore-the-collection/stories/the-general-strike/>
- **#67** 「the increase in the real cost of food and the diminishing response of nature to any further increase in the po…」  
  判断：**错误**。20世纪农产品实际价格平均每年下降约1%，消费者实际食品价格下降，“粮食实际成本上升”的趋势没有出现。  
  来源：<https://eh.net/encyclopedia/u-s-agriculture-in-the-twentieth-century/>；<http://www.ers.usda.gov/data-products/charts-of-note/chart-detail?chartId=76174>
- **#76** 「This would be much more likely to take place in the event of reactionary movements being successful in each of…」  
  判断：**错误**。1922年魏玛德国与苏俄签订拉帕洛条约，恢复关系并承诺在经济上合作，列宁政权与德国中产阶级政府之间出现了目标一致的合作。  
  来源：<https://germanhistorydocs.org/en/weimar-germany-1918-1933/german-russian-treaty-of-rapallo-april-16-1922>；<https://avalon.law.yale.edu/20th_century/rapallo_001.asp>
- **#77** 「And when Poland finds that the seductive policy of France is pure rhodomontade and that there is no money in i…」  
  判断：**错误**。波兰1921年与法国结盟，此同盟一直维持到第二次世界大战爆发；虽在1934年与纳粹德国签署互不侵犯宣言，但并未“尽快”投向他国。  
  来源：<https://en.wikipedia.org/wiki/Franco-Polish_alliance>；<https://en.wikipedia.org/wiki/German%E2%80%93Polish_declaration_of_non-aggression>
- **#78** 「After 1920 the need of Russian supplies will be even greater than it was before the war」  
  判断：**错误**。战后俄国粮食对国际粮食安全变得几乎无关紧要，海外粮食产量迅速扩张，美加阿出口大增，欧洲对俄粮的需求没有变得更大。  
  来源：<https://www.ssoar.info/ssoar/bitstream/handle/document/91436/ssoar-russanald-2023-304-asschenfeldt-Russias_Food_Power_in_the.pdf>；<https://ia600107.us.archive.org/23/items/CAT31392819/CAT31392819.pdf>
- **#79** 「If trade is not resumed with Russia, wheat in 1920-21 (unless the seasons are specially bountiful) must be sca…」  
  判断：**错误**。对俄贸易未恢复（俄粮出口1923年后才少量恢复），但1920年7月农产品价格崩跌，小麦价格从1919年每蒲式耳2.16美元降至1921年1.03美元，并未稀缺昂贵。  
  来源：<https://www.ers.usda.gov/media/10790/historical-overview-of-us-agricultural-policies-and-programs.pdf?v=31426>；<https://doi.org/10.2307/1230111>
- **#84** 「These Articles make substantially less probable a war between organized Great Powers」  
  判断：**错误**。国联未能阻止大国之间的战争：1930年代满洲、阿比西尼亚危机中失败，第二次世界大战爆发。  
  来源：<https://www.historyskills.com/classroom/year-10/league-of-nations-prevent-wwii/>；<https://www.ungeneva.org/en/about/league-of-nations/at-work>

### 暂无法判断（25 条）

- **#2** 「If the European Civil War is to end with France and Italy abusing their momentary victorious power to destroy …」  
  判断：**暂无法判断**。前提“法意滥用胜利摧毁德奥”是否成立难以界定（赔款后被削减、莱茵兰提前撤军），检索来源无法把法国1940年失败归因于此，暂无法判断。  
  来源：<https://en.wikipedia.org/wiki/Occupation_of_the_Rhineland>；<https://doi.org/10.1007/978-0-230-62949-3_3>
- **#3** 「this principle depended on unstable psychological conditions, which it may be impossible to recreate」  
  判断：**暂无法判断**。“资本积累的心理条件无法重建”属心理/制度判断，检索来源只描述1920年代复苏与停滞，没有可直接核对的指标，暂无法判断。  
  来源：<https://doi.org/10.1007/978-1-349-00298-6_21>；<https://johnquiggin.com/2021/02/18/economic-lessons-of-the-20-year-armistice/>
- **#4** 「the laboring classes may be no longer willing to forego so largely, and the capitalist classes, no longer conf…」  
  判断：**暂无法判断**。工人阶级与资本家消费倾向的变化缺乏来源中的可核对数据，暂无法判断。  
  来源：<https://doi.org/10.1007/978-1-349-00298-6_21>；<https://johnquiggin.com/2021/02/18/economic-lessons-of-the-20-year-armistice/>
- **#8** 「letting loose such human and spiritual forces as, pushing beyond frontiers and races, will overwhelm not only …」  
  判断：**暂无法判断**。前提“迦太基式和约”并未完全实施（赔款缩减、提前撤军），来源无法把法国安全体系的崩溃归因于该前提，暂无法判断。  
  来源：<https://doi.org/10.1007/978-0-230-62949-3_3>；<https://en.wikipedia.org/wiki/Occupation_of_the_Rhineland>
- **#15** 「The more extravagant expectations as to Reparation receipts, by which Finance Ministers have deceived their pu…」  
  判断：**暂无法判断**。“过高赔款期望将不再被提及”缺乏可核对的公开言论统计；来源显示1924年法国仍因赔款落空而政局变动，暂无法判断。  
  来源：<https://en.wikipedia.org/wiki/Cartel_des_Gauches>；<https://financialhistoryinstitute.com/publications/french-floating-debt-crisis-1924-1926>
- **#17** 「Yet if these feelings and these rights are allowed to prevail beyond what wisdom would recommend, the reaction…」  
  判断：**暂无法判断**。前提“情感与权利超出明智限度”的触发点难以界定；虽有1923年鲁尔危机，来源不足以对应该条件命题，暂无法判断。  
  来源：<https://en.wikipedia.org/wiki/World_War_I_reparations>；<https://alphahistory.com/weimarrepublic/1923-hyperinflation/>
- **#19** 「If the distribution of the European coal supplies is to be a scramble in which France is satisfied first, Ital…」  
  判断：**暂无法判断**。前提（煤炭分配成为法国优先的争抢）与“革命前景”均难以从来源中确认，暂无法判断。  
  来源：<https://en.wikipedia.org/wiki/Spa_Conference_of_1920>；<https://en.wikipedia.org/wiki/Revolutions_of_1917%E2%80%931923>
- **#21** 「Much time must elapse before the plant and the skilled labor could be developed within France」  
  判断：**暂无法判断**。来源显示到1925年法国北部已建成新厂，但未给出“需要多长时间”可对照的数据，暂无法判断。  
  来源：<https://doi.org/10.1007/978-1-349-00298-6_21>；<https://documents1.worldbank.org/curated/en/581841468281387936/pdf/NonAsciiFileName0.pdf>
- **#22** 「the effective iron output of Europe will be diminished by a new political frontier」  
  判断：**暂无法判断**。来源只有法国钢铁产量和德国领土损失的一般描述，未给出全欧有效铁产量因新边界变化的数据，暂无法判断。  
  来源：<https://ndl.ethernet.edu.et/server/api/core/bitstreams/807d6fa0-cbba-432e-9d3d-581a4bf58e9f/content>；<https://documents1.worldbank.org/curated/en/581841468281387936/pdf/NonAsciiFileName0.pdf>
- **#23** 「The efficiency and output of the industry seem certain to diminish.」  
  判断：**暂无法判断**。来源说明上西里西亚分割后钢铁厂在经营和所有权上几乎完全分离，但没有效率与产量数据，暂无法判断。  
  来源：<https://moodle2.units.it/pluginfile.php/452986/mod_folder/content/0/Hartshorne_1933.pdf?forcedownload=1>；<https://www.uni-wuppertal.de/en/transfer/science-communication/jahr100wissen-/-100-years-ago/2022/die-abtretung-ostoberschlesiens/>
- **#24** 「will not only diminish the production of useful commodities, but may possibly occupy an immense quantity of hu…」  
  判断：**暂无法判断**。“经济边界减少有用商品生产”缺乏来源中的定量对照，暂无法判断。  
  来源：<https://moodle2.units.it/pluginfile.php/452986/mod_folder/content/0/Hartshorne_1933.pdf?forcedownload=1>；<https://en.wikipedia.org/wiki/International_Steel_Agreement>
- **#26** 「Even without any supply from Upper Silesia and Czecho-Slovakia, Poland could probably meet her requirements by…」  
  判断：**暂无法判断**。前提“没有上西里西亚”未出现：波兰1922年获得部分上西里西亚后才实现煤炭自给，此前依赖进口；条件未触发，不判分。  
  来源：<https://econjournals.sgh.waw.pl/kwes/article/download/20/15>；<https://www.uni-wuppertal.de/en/transfer/science-communication/jahr100wissen-/-100-years-ago/2022/die-abtretung-ostoberschlesiens/>
- **#29** 「I shall be surprised if it proves possible to substantiate claims even to this amount」  
  判断：**暂无法判断**。检索来源未给出比利时最终确立的实物损失索赔金额，暂无法判断。  
  来源：<https://en.wikipedia.org/wiki/Belgium_in_World_War_I>；<https://history.state.gov/historicaldocuments/frus1919Parisv13/ch34subch2>
- **#30** 「it will turn out, I believe, that taking account of casualties, loss of property and burden of future debt, Be…」  
  判断：**暂无法判断**。来源只有伤亡与战争成本的一般比较，没有按伤亡、财产与债务综合衡量的“相对牺牲”排名，暂无法判断。  
  来源：<https://warwick.ac.uk/fac/soc/economics/staff/mharrison/papers/ww1toronto2.pdf>；<https://en.wikipedia.org/wiki/Belgium_in_World_War_I>
- **#41** 「It follows, therefore, that no sum worth speaking of can be expected in the form of gold or silver towards the…」  
  判断：**暂无法判断**。检索来源未给出1921年前首期付款中金银部分的具体数额，暂无法判断。  
  来源：<https://apps.bundesarchiv.de/aktenreichskanzlei/1919-1933/0001/feh/feh1p/kap1_2/kap2_213/para3_4.html>；<https://www.usni.org/magazines/proceedings/1921/june/notes-international-affairs>
- **#42** 「In face of all these considerations, it will be a miracle if much remains for Reparation.」  
  判断：**暂无法判断**。来源未给出可用于赔款的德国海外证券数额，暂无法判断。  
  来源：<https://apps.bundesarchiv.de/aktenreichskanzlei/1919-1933/0001/feh/feh1p/kap1_2/kap2_213/para3_4.html>；<https://www.historyskills.com/classroom/year-10/versailles-reparations-paid/>
- **#43** 「The contribution from all these sources together which the Reparation Commission can hope to secure by May, 19…」  
  判断：**暂无法判断**。来源只给出委员会对全部交付的认定（最多约80亿金马克），未拆分金银、船舶与海外证券，无法对照12.5亿-17.5亿美元区间，暂无法判断。  
  来源：<https://apps.bundesarchiv.de/aktenreichskanzlei/1919-1933/0001/feh/feh1p/kap1_2/kap2_213/para3_4.html>；<https://archive.spectator.co.uk/article/23rd-april-1921/2/germany-shows-no-intention-of-paying-by-may-1st-th>
- **#44** 「Whatever the Treaty may say, the Reparation Commission will not secure any cash payments from Poland.」  
  判断：**暂无法判断**。检索来源未说明赔款委员会是否从波兰收到现金，暂无法判断。  
  来源：<https://history.state.gov/historicaldocuments/frus1919Parisv13/ch34subch2>；<https://archive.spectator.co.uk/article/25th-august-1923/1/it-was-agreed-among-the-allies-at-spa-that-the>
- **#46** 「Belgium may _possibly_ get her $500,000,000 by May, 1921, but none of the other Allies are likely to secure by…」  
  判断：**暂无法判断**。来源只说明比利时享有优先权和各国分配比例，未给出1921年5月前各国实际所得，暂无法判断。  
  来源：<https://history.state.gov/historicaldocuments/frus1919Parisv13/ch34subch2>；<https://archive.spectator.co.uk/article/25th-august-1923/1/it-was-agreed-among-the-allies-at-spa-that-the>
- **#47** 「Unless, therefore, Alsace-Lorraine and Upper Silesia send their iron ore to Germany proper, to be worked up, w…」  
  判断：**暂无法判断**。条件命题涉及阿尔萨斯-洛林与上西里西亚铁矿流向，来源未给出德国铁、机械、煤出口的对照数据，暂无法判断。  
  来源：<https://ndl.ethernet.edu.et/server/api/core/bitstreams/807d6fa0-cbba-432e-9d3d-581a4bf58e9f/content>；<https://www.diw.de/documents/publikationen/73/diw_01.c.400717.de/31-45.pdf>
- **#48** 「(1) Iron goods. In view of Germany's loss of resources, an increased net export seems impossible and a large d…」  
  判断：**暂无法判断**。来源只有德国生铁、钢产能下降的数据，没有铁制品净出口序列，暂无法判断。  
  来源：<https://ndl.ethernet.edu.et/server/api/core/bitstreams/807d6fa0-cbba-432e-9d3d-581a4bf58e9f/content>；<https://www.diw.de/documents/publikationen/73/diw_01.c.400717.de/31-45.pdf>
- **#58** 「I do not myself believe that the Reparation Commission will secure real resources from the above items by May,…」  
  判断：**暂无法判断**。来源未把委员会所获资源按凯恩斯所列项目拆分，无法对照12.5亿美元下限，暂无法判断。  
  来源：<https://apps.bundesarchiv.de/aktenreichskanzlei/1919-1933/0001/feh/feh1p/kap1_2/kap2_213/para3_4.html>；<https://archive.spectator.co.uk/article/23rd-april-1921/2/germany-shows-no-intention-of-paying-by-may-1st-th>
- **#61** 「these Governments are fast rendering impossible a continuance of the social and economic order of the nineteen…」  
  判断：**暂无法判断**。“19世纪社会经济秩序无法延续”属宏观判断，来源无法给出可核对的标准，暂无法判断。  
  来源：<https://johnquiggin.com/2021/02/18/economic-lessons-of-the-20-year-armistice/>；<https://doi.org/10.1007/978-1-349-00298-6_21>
- **#72** 「Failing such a settlement as is now proposed, the war will have ended with a network of heavy tribute payable …」  
  判断：**暂无法判断**。“协约国间贡款总额可能超过从敌国得到的数额”需要战债与赔款实际流量的完整对比，来源未提供，暂无法判断。  
  来源：<https://ehs.org.uk/the-uks-unpaid-war-debts-to-the-united-states-1917-1980/>；<https://www.historyskills.com/classroom/year-10/versailles-reparations-paid/>
- **#81** 「the revival of trade, of the comforts of life and of ordinary economic motive are not likely to promote the ex…」  
  判断：**暂无法判断**。新经济政策下贸易一度复苏，但后来的斯大林体制与贸易复苏的因果关系无法从来源中判定，暂无法判断。  
  来源：<https://doi.org/10.2307/1230111>；<https://www.ssoar.info/ssoar/bitstream/handle/document/91436/ssoar-russanald-2023-304-asschenfeldt-Russias_Food_Power_in_the.pdf>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/keynes-economic-consequences-of-the-peace-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/keynes-economic-consequences-of-the-peace-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/keynes-economic-consequences-of-the-peace-v5/audit/manual_review_2026-11-15.py`

## 说明

- 第 1、79 条是条件句，前提基本出现，按条件满足计分；第 18、70 条前提是否成立无法确认，按“条件未知的有界部分符合”计分；第 2、8、17、19、47、72 条前提是否触发无法确认，第 26 条前提（波兰没有上西里西亚）未出现，均记为暂无法判断。
- 第 3、4、15、21–24、29、30、41–44、46、48、58、61、81 条在检索和存档证据中找不到能直接核对结果的材料（如比利时最终确立的战损索赔、首期付款中金银与海外证券的数额、上西里西亚钢铁效率、资本积累的“心理条件”），按规则记为暂无法判断，没有勉强判定。
- 候选中另有 33 条因归属他人观点、规范性或措辞含糊被流水线降为 unclear，不进入核验。
- 统计以 pipeline.py report 的 summary.json 为准；本表的加权胜率按 manual_report.py 的权重计算。

