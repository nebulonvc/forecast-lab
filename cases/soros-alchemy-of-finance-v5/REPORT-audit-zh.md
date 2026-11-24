# 索罗斯《金融炼金术》预测核查报告（v5 方法）

- 案例目录：`cases/soros-alchemy-of-finance-v5/`
- 观察窗口：英文原版 The Alchemy of Finance 出版日 **1987-05-01**（Simon & Schuster）至截止日 **2026-11-15**；1988年平装本新增“1987年大崩盘”章、1994年前言、Tudor Jones 序与译序均排除
- 工具：forecast-lab main `85e6da1`（v5 抽取；deepseek + Exa 自适应核验 search-verifier-v3，`--max-rounds 2`，未完成项重试一次后人工复核）
- 抽取：v5 抽取 209 条候选，其中大部分是理论、历史与“历时实验”中出版前已到期的短线判断
- 费用：DeepSeek 约 ¥22.22（抽取 1.07 + 主核验 16.39 + 重试 4.76），Exa 约 $3.41
- 复核时间：2026-11-15（Asia/Shanghai）；未提交、未推送、未开 PR，没有改动其他案例

## 1. 结论

剔除 170 条非预测后，共 **39 条预测**，其中 **35 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 16 |
| 趋势符合 | 1 |
| 部分符合 | 7 |
| 错误 | 11 |
| 暂无法判断 | 4 |

| 指标 | 数值 |
|---|---:|
| 严格胜率（正确/可判定） | **45.7%**（16/35） |
| 加权胜率（正确+0.75×趋势符合+0.5×部分符合）/可判定 | **57.9%** |
| 错误率（错误/可判定） | **31.4%**（11/35） |
| 未定占比（暂无法判断/计分样本） | **10.3%**（4/39） |

索罗斯对信用与资产价格反身性的判断经受住了检验：1987年股灾、杠杆收购与垃圾债崩溃、1990—91年信贷紧缩式衰退、日本泡沫破裂、抵押物贬值引发的信贷骤停（2008年）都基本应验；但他对制度性崩溃的判断普遍落空——浮动汇率体系崩溃、美元灾难性崩溃、日元取代美元、欧佩克解体、美国转向关税保护都没有发生，这些构成主要错误。

## 2. 各阶段变化

| 阶段 | 计分样本 | 正确 | 趋势符合 | 部分符合 | 错误 | 暂无法判断 | 可判定 | 严格 | 加权 | 错误率 | 未定占比 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 机器已完成（含后来剔除的非预测） | 71 | 16 | 5 | 13 | 5 | 32 | 39 | 41.0% | 67.3% | 12.8% | 45.1% |
| 人工审核后（剔除非预测、补齐卡住项并复核） | 39 | 16 | 1 | 7 | 11 | 4 | 35 | 45.7% | 57.9% | 31.4% | 10.3% |
| 隐含窗口重判后（最终） | 39 | 16 | 1 | 7 | 11 | 4 | 35 | 45.7% | 57.9% | 31.4% | 10.3% |

按时间范围分（最终）：

| 时间范围 | 计分样本 | 正确 | 趋势符合 | 部分符合 | 错误 | 暂无法判断 | 可判定 | 严格 | 加权 | 错误率 | 未定占比 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 原文写明时间 | 10 | 2 | 0 | 2 | 6 | 0 | 10 | 20.0% | 30.0% | 60.0% | 0.0% |
| 没写终点（按出版日到截止日判断） | 29 | 14 | 1 | 5 | 5 | 4 | 25 | 56.0% | 69.0% | 20.0% | 13.8% |

## 3. 人工复核

- 非预测剔除：170 条（出版前已到期 109、规范建议/现状描述 21、一般机制 19、史实 17、出版前已兑现 3、现状描述 1）。
- 改判（不含非预测）：21 条，其中卡住项人工补判（`manual-assistant-2026-11-15`）8 条、机器结论审核改判（`manual-audit-2026-11-15`）13 条。人工补判只用真实可查来源，引文存于 `assessment.manual_evidence`。
- 前提从未出现的条件句、终点未到的条目一律记暂无法判断，不强行判对错。

## 4. 全部预测条目（最终）

### 正确（16）

- 「目前，人们都在关注我们可能正在趋近于又一次衰退，但一般都认为这次衰退同以往的历次衰退相比并无二致，而对于我们正处于更大循环的衰退期这一事实却大都未予考虑。我坚持认为，自第二次世界大…」——原文称下一次衰退将不同于战后历次衰退，会发生在实体经济借款能力收缩之时。1990—91年美国衰退伴随明显的信贷紧缩，储蓄机构从1989年起大幅、反常地收缩放贷，方向与预测一致。 来源：https://www.minneapolisfed.org/article/1991/whither-the-credit-crunch；https://www.brookings.edu/articles/the-credit-crunch/
- 「萧条可能会突然降临，尤其是在抵押物清偿价值下降引起了信贷突然压缩之后，其危险程度令人为之色变。」——原文警告抵押物价值下降引起信贷骤然收缩后，萧条可能突然降临。2007—2009年资产价格下跌、回购折价上升引发信贷紧缩，导致大萧条以来最严重的金融危机和衰退，与这一条件判断一致。 来源：https://www.nber.org/digest/mar09/explaining-credit-crunch；https://www.nber.org/system/files/working_papers/w14612/w14612.pdf
- 「１９８７ 年无疑将成为保护主义把国际贸易体制推向崩溃边缘而又不致于超越边界彻底崩溃的一年。」——1987年保护主义压力自第二次石油危机以来持续不减，发达国家诉诸自愿出口限制、报复性进口限制等双边/单边措施，多边体制被描述为处于十字路口、可信度受挑战，符合“推向崩溃边缘”；同时GATT迎来四十周年、乌拉圭回合谈判组于1987年设立并启动实质谈判，体制未彻底崩溃。 来源：https://www.mofa.go.jp/policy/other/bluebook/1987/1987-4-2.htm；https://www.elibrary.imf.org/display/book/9781557750372/C4.xml
- 「贷款集团体制的确立没有经过认真的规划，甚至没有正式宣布过，它从    一开始就是过渡性的，并且注定将被某种另外的形式所替代。」——原文断言贷款集团体制是过渡性的、注定被另一种形式替代。IMF材料显示1989年布雷迪计划以银行贷款换债券、官方推动债务减免，取代了此前以新增贷款维持债务完整性的合作模式，构成体制被替代的直接证据。 来源：https://www.imf.org/en/blogs/articles/2019/04/11/blog-the-imf-30-years-after-brady；https://www.elibrary.imf.org/display/book/9781498382656/ch019.xml
- 「合并热已经创造出自我激励的动量，在它疲软下来之前，无疑将会有一些交易在不理智的价格水平上达成。」——原文预测合并热疲软前会出现一些价格不理智的交易。RJR Nabisco收购战（1988年10-12月）在并购潮见顶前以约250亿美元成交，最终价较竞价前约56美元/股翻倍，被当时媒体和后续学术研究（Kaplan & Stein）认定为价格相对现金流上升、杠杆过高，构成符合预测的具体实例。 来源：https://www.upi.com/Archives/1989/02/09/Kohlberg-Kravis-Roberts-Co-Thursday-completed-the-largest/8375603003600/；https://doi.org/10.1108/eb039310
- 「如果在这个过程中使用了巨额的信贷，那么由此造成的崩溃将是雪崩式的。」——原文称若并购过程中使用了巨额信贷，随之而来的崩溃将是雪崩式的。1989年9月至1990年2月垃圾债券价格急跌，德崇证券倒闭，六年的垃圾债扩张戛然而止，此后违约率超过1981—82年衰退时期，方向一致。 来源：https://fraser.stlouisfed.org/files/docs/historical/frbclev/econcomm/econcomm_19900401.pdf；https://www.csmonitor.com/1991/0412/fjunk.html
- 「整个过程的净效应将是重组公司的巨额债务负担，各种各样的重组    方案将会导致出现债务清偿的困难。」——原文预测重组公司背负巨额债务并出现债务清偿困难。GAO案例显示被收购公司长期债务占比骤升且多家进入破产保护；Altman等统计显示1989-1991年垃圾债券违约金额与违约率创纪录，与主要判断方向一致。 来源：https://chicagounbound.uchicago.edu/cgi/viewcontent.cgi?article=4725&context=uclrev；https://www.thefreelibrary.com/Revisiting+the+high-yield+bond+market.-a013632930
- 「公司    的赢利能力将会得到加强，资产经过重新调配，迟钝的管理机构受到极大的    震动，企业将变得更加精干。」——原文预测并购重组后公司盈利能力增强、资产重新配置、企业更精干。对1985—1989年44宗最大杠杆收购的研究显示，收购后企业经营利润率明显改善，方向一致。 来源：https://doi.org/10.2307/3665678
- 「总的来说，因合并热潮而引发的投机热将要告一段落，至于美国公司的结构重组，则无疑会持续下去。」——LBO实体数从1988年291、1989年293降至1990年177、1991年171，LBO金额从1989年755亿降至1990年176亿，垃圾债券市场1989—1990年崩溃，投机热确实见顶回落，第一分项符合。资产剥离实体数从1987年1004持续升至1995年2227，公司重组延续，第二分项也符合。两个主要分项均有直接证据支持，判正确。 来源：https://hsus.cambridge.org/HSUSWeb/toc/treeTablePathIdCh430-439.html；https://tuck.dartmouth.edu/uploads/centers/files/LBO_Note_%281%29.pdf
- 「当公司交易变得声名狼藉之后，要想重新获得资金的支持将是极为困难的，而垃圾债券的本性也日益暴露出来了。」——原文预测声誉恶化后公司交易融资将极为困难、垃圾债券本性暴露。1989年9月至1990年2月低等级债券价格急跌、一级市场发行骤降、Drexel于1990年2月倒闭，融资困难与垃圾债券风险暴露的主要结果已实现。1987年11月丑闻后垃圾债券短期反弹只说明即时触发被延迟，不构成主要分项未实现。 来源：https://fraser.stlouisfed.org/files/docs/historical/frbclev/econcomm/econcomm_19900401.pdf；https://www.latimes.com/archives/la-xpm-1990-02-18-op-1245-story.html
- 「最终，高涨的股市走向崩溃，不经济的合约纷纷破产，我们又将被国际债务问题所困扰。」——原文预测高涨的股市最终崩溃、不经济的交易纷纷破产、国际债务问题再度困扰。1987年10月19日道指单日暴跌22.6%；1989—1991年杠杆收购公司大批违约破产；拉美债务问题持续到1989年布雷迪计划才缓解。三个分项均在出版后数年内出现。 来源：https://www.federalreservehistory.org/essays/stock-market-crash-of-1987；https://www.csmonitor.com/1991/0412/fjunk.html
- 「真正危险的还是将来的崩盘。」——原文写于1986年4月9日，明确指向“将来”的崩盘风险。1987年10月19日S&P 500单日下跌约20.4%，为1885年以来最大单日跌幅，构成崩盘式暴跌，主要方向与预测一致。 来源：https://www.nber.org/system/files/working_papers/w2954/w2954.pdf；https://www.federalreserve.gov/pubs/feds/2007/200713/index.html
- 「我确信，日本股票市场的崩溃将成为金融史上的一座里程碑。」——原文断言日本股市的崩溃将成为金融史上的里程碑。日经指数1989年末见顶38915点后暴跌，到1992年8月跌至14309点，跌幅超过60%，日本泡沫破裂成为金融史上的标志性事件。 来源：https://www.imes.boj.or.jp/research/papers/english/me19-s1-14.pdf
- 「我们很可能也将会在自己的市场中目睹同样的过程。」——原文以“很可能”预测美国市场将目睹与日本股市崩溃同样的过程。1987年10月19日美国道琼斯工业平均指数单日暴跌约22.6%，S&P 500同期亦大幅下挫，构成与日本市场类似的急剧崩盘，主要方向已发生。 来源：https://www.federalreservehistory.org/essays/stock-market-crash-of-1987；https://www.latimes.com/archives/la-xpm-1987-10-19-mn-10414-story.html
- 「现在的市场行情又是一个 １９２９ 年型的牛市市场的翻版，只是它的结束将会早得多，不可能达到像 １９２９ 年那样的高度。」——原文称当时是1929年型牛市的翻版，但结束得会早得多，达不到1929年的高度。1987年10月股市崩盘，道指从8月高点下跌约36%，牛市在出版后几个月就结束，方向一致。 来源：https://www.nytimes.com/1987/10/20/business/stocks-plunge-508-points-a-drop-of-22.6-604-million-volume-nearly-doubles-record.html
- 「国际资本市场的急剧扩张将发展成为又一种市场过热的形式，就像 ７０ 年代国际银行贷款业务的急剧增长一样。」——BIS长期统计显示国际银行跨境债权从1963年不足世界GDP的2%升至2007年逾60%，且跨境放贷助推了1980年代初拉美债务危机、1990年代末亚洲金融危机和2007-09年全球金融危机前的信贷繁荣，符合“扩张演变为过热形式”的主要判断。 来源：https://www.bis.org/publications/seven-decades-international-banking.pdf；https://newmoneyreview.com/index.php/2021/09/20/gfc-reversed-six-decade-global-banking-boom/

### 趋势符合（1）

- 「如果国际间不能采取有效的合作，保护主义、货币混乱以及偿债中断的危险将会愈益加强，从而相应地增大了体制改革的压力。」——原文称若无有效国际合作，保护主义、货币混乱和偿债中断的危险会加强，并加大体制改革压力。WTO报告显示受新关税影响的贸易额在2024—25年间增长四倍以上，G20自金融危机以来累积的贸易限制措施大幅增加，方向一致；但偿债中断分项证据有限，判趋势符合。 来源：https://www.wto.org/english/news_e/news25_e/trdev_02dec25_225_e.htm

### 部分符合（7）

- 「汇率变动如此剧烈，以致于要么必须由某种形式的政府干预对体系加    以修改，要么它们就注定会崩溃」——原文称汇率剧烈波动，体系要么被政府干预修改，要么崩溃。1987年卢浮宫协议等政策协调确实出现，属于“干预修改”；但IMF史料指出此后正式协调基本消亡，浮动体系既没有被持久修改，也没有崩溃。 来源：https://www.imf.org/external/pubs/ft/history/2001/ch04.pdf
- 「其结果将是游戏规则的彻底改革。」——博伊斯基事件后确有实质制度变化：1988年ITSFEA提高内幕交易处罚、创设私人诉权与控制人责任，1990年Remedies Act赋予SEC民事罚款与禁业令等新权力，SEC规则14e-3获立法/司法确认。但多项材料显示国会未采纳内幕交易统一定义、并购立法多次夭折，联邦并购监管自1980年代末趋于收缩，故“彻底改革”仅部分成立。 来源：https://sechistorical.org/exhibition/the-mechanics-of-legislation-congress-the-sec-and-financial-regulation/rolling-thunder-of-insider-trading/lessons-learned/；https://scholarship.law.unc.edu/cgi/viewcontent.cgi?article=3297&context=nclr
- 「净现金流向垃圾债券的趋势将被逆转，收购者所能够获得的杠杆比例也会受到极大的限制。」——1989-1990年高收益债新发行显著收缩、Drexel破产，垃圾债市场一度萎缩，符合“净现金流向垃圾债券趋势逆转”的方向；但2003年高收益债发行恢复并成为LBO融资主力，杠杆倍数回升至4.5-7倍EBITDA，说明“杠杆比例受到极大限制”并非持续成立。两个主要分项出现实质分化，故判部分符合。 来源：https://fraser.stlouisfed.org/files/docs/historical/frbclev/econcomm/econcomm_19900401.pdf；https://www.kansascityfed.org/documents/1027/1990-The%20Truth%20about%20Junk%20Bonds.pdf
- 「在 １９８７ 年里，将会滋长出保护主义同债务豁免的混和政策形态。」——保护主义分项在1987年内有直接证据：众议院委员会通过强硬贸易法案、参议院通过S.1420、行政当局声明称其使贸易法更趋保护主义。但“债务豁免”分项未实现：行政当局明确反对全面豁免，主要贷款方不支持布拉德利式豁免，国会仅提出债务重组/管理设施提案，最终立法未在1987年内落地。因此混合政策形态仅部分实现。 来源：https://digitalrepository.unm.edu/notisur/498；https://www.upi.com/Archives/1987/04/10/Treasury-Secretary-James-Baker-and-the-worlds-major-public/3302545025600/
- 「１９８７ 年的上半年将经受严峻的考验。」——1987年上半年确实出现体系性压力：4—5月美日贸易摩擦下10年期美债收益率45个交易日内飙升138BP，美元4月跌至40年低点、多国央行大规模干预，3月底全球股市因美对日关税而急跌，OECD在5—6月下调增长预测并称经济状况恶化。但上半年全球增长仍为正、失业率下降、无衰退，体系未发生决定性崩溃，故为部分符合而非完全正确。 来源：https://fraser.stlouisfed.org/title/federal-reserve-bulletin-62/august-1987-20783/fulltext；https://www.sohu.com/a/910241875_522914
- 「在压力减退之后，中央银行的被动抛售将由日元持有者的主动抛售所取代，流动资金将因此而泄漏。考虑到股票价格的膨胀水平，跌势将很快地演变为一场决堤式的崩溃。」——原文预测日本股市跌势将很快演变为决堤式崩溃。日经指数在1990—1992年确实暴跌60%以上，崩溃结果出现；但它发生在作者写作约三年后，且是在1989年见顶之后，并非原文所说的“很快”，触发机制也不同。 来源：https://www.imes.boj.or.jp/research/papers/english/me19-s1-14.pdf
- 「日本股票市场下跌对其他市场的初期影响将是非常积极的，因为看来似乎会有巨额资金回流各个市场。但是，一旦跌势演化为崩盘，整个世界将会为之发抖。」——分项(2)得到直接证据支持：1987年10月19日前后全球主要市场同步剧烈下跌，日本股市随后也大跌，符合“崩盘则世界为之发抖”。但分项(1)相反：日本股市下跌初期（10月19日前后）香港、新加坡、悉尼、伦敦、纽约等市场同步大跌而非上涨，未见资金回流提振其他市场的积极初期效应。 来源：https://www.bankofengland.co.uk/-/media/boe/files/quarterly-bulletin/1988/the-equity-market-crash.pdf；https://rpc.cfainstitute.org/research/financial-analysts-journal/1988/the-international-crash-of-october-1987

### 错误（11）

- 「自由浮动汇率具有内在的不稳定性，并且，这种不稳定性    是累积的，因此自由浮动汇率体系的最终崩溃几乎是毫无疑问的。」——原文断言自由浮动汇率体系内在不稳定、最终崩溃几乎毫无疑问。出版后近四十年，美元、欧元、日元、英镑等主要货币仍自由浮动，IMF分类中仍有大批自由浮动经济体，体系没有崩溃。原文未写终点，按出版至截止日的窗口判断，主要结果相反。 来源：https://en.wikipedia.org/wiki/List_of_countries_by_exchange_rate_regime
- 「到那时，偿债负担和投机资本的逃逸再加上贸易逆差将引发灾难性的美    元崩溃」——原文预测偿债负担、投机资本外逃和贸易逆差将引发灾难性的美元崩溃。出版后近四十年美国逆差和净负债持续扩大，但美元没有崩溃，至今仍是主导性国际货币，主要结果相反。 来源：https://www.atlanticcouncil.org/blogs/what-the-data-shows-and-doesnt-show-about-the-future-of-the-dollar/；https://hfri.phbs.pku.edu.cn/info/1741/15361.htm
- 「也许最终我们将不得不    进入这样一种局面，几家最大的银行都成了公共财产。」——原文以“也许最终”预测几家最大银行可能成为公共财产。2008年危机中，九大银行被政府强制注入优先股资本，但政府持有的是无投票权优先股，随后银行偿还资金、政府售股退出，最大银行并未转为公共财产，主要结果与预测方向相反。 来源：https://www.reuters.com/article/us-financial-banks-meeting/paulson-gave-banks-no-choice-on-government-stakes-memos-idUSTRE54D0NH20090514/；https://home.treasury.gov/news/press-releases/tg453
- 「由于    管理活动短期化倾向的增强，美国的实物投资活动很可能缩减」——原文预测由于管理短期化，美国实物投资很可能缩减。BEA数据显示非住宅固定投资在1988、1989年分别实际增长5.0%和5.7%，此后长期保持增长，只在衰退年份短暂下降，主要方向相反。 来源：https://fred.stlouisfed.org/data/A008RL1A225NBEA；https://fred.stlouisfed.org/data/A008RL1A225NBEA
- 「美国将被迫施行关税保护以挽救国内的生产商，这种保护措施还会扩展到墨西哥，——只要它仍然停留在恶性债务的起跑线上。」——原文预测美国将被迫用关税保护国内生产商，并把保护扩展到墨西哥。实际走向相反：美墨加在1994年实施北美自由贸易协定，立即取消了墨西哥对美一半以上出口的关税。 来源：https://en.wikipedia.org/wiki/North_American_Free_Trade_Agreement
- 「现在，欧佩克的解体也只不过是时间问题了。」——原文断言欧佩克解体只是时间问题。出版后欧佩克一直存续，并陆续吸纳安哥拉（2007年）等新成员、厄瓜多尔重新加入，至今仍在运作。 来源：https://www.reuters.com/article/business/timeline-50-years-of-opec-idUSTRE68C2NK/；https://www.opec.org/member-countries.html
- 「最终，美国将不得不采取措施以保护国内产油商」——原文预测美国最终将不得不采取措施保护国内产油商。1986年国会提出的石油进口费等保护法案均未获表决，此后美国也没有实行石油进口保护关税，主要方向相反。 来源：https://www.govtrack.us/congress/bills/99/hr4662
- 「令人寝食难安的消费支出紧缩可能终将来临」——FRED/BEA年度实际PCE同比序列显示，1987—2025年间仅2009年（-1.3%）和2020年（-2.5%）出现负增长，其余年份均为正增长，2021—2025年分别为8.8%、2.9%、2.3%、2.9%、2.6%，未见显著、持续的消费支出紧缩。主要方向与预测相反。 来源：https://fred.stlouisfed.org/data/DPCERL1A225NBEA；https://fred.stlouisfed.org/data/PCECCA
- 「说不定我们还可以再享受几年低水平的经济增长，而不至于陷入衰退与萧条。」——原文明确说“再享受几年低水平的经济增长，而不至于陷入衰退与萧条”，方向是不出现衰退。NBER官方记录显示1990年7月即进入衰退、1991年3月触底，距原文写作不足四年，落在“几年”窗口内，主要判断被反证。 来源：https://www.nber.org/research/data/us-business-cycle-expansions-and-contractions；https://www.nber.org/news/business-cycle-dating-committee-announcement-april-25-1991
- 「涌向垃圾债券的基金将会回流，从而大大增加它们所载荷的风险的溢价。」——原文预测涌向垃圾债券的资金将回流、风险溢价大幅上升。博伊斯基事件后垃圾债基金的资金流入很快恢复，1987年9月垃圾债相对国债的收益率优势还略有收窄，与预测相反。 来源：https://www.euromoney.com/article/27bjsstsqxhkmh1wmk6ek/capital-markets/there-are-still-gold-nuggets-in-junk/
- 「日元取代美元成为主要的储备货币也只是时间的问题了，转变将伴随着许多混乱与躁动，就像第二次世界大战期间由英镑向美元过渡时那样。」——原文断言日元将取代美元成为主要储备货币。COFER数据显示美元长期稳居第一（2026Q2约56.70%），日元份额自1991年约8.7%峰值后持续下降至2026Q2约4.96%，方向与预测相反。 来源：https://finobservatory.org/reserves；https://www.imf.org/zh/blogs/articles/2024/06/11/dollar-dominance-in-the-international-reserve-system-an-update

### 暂无法判断（4）

- 「大循环成功地回避了的问题，将在它崩溃之后重新出现，并且更加突出。」——原文称大循环回避的问题将在其崩溃后重新出现并更加突出，所指“问题”没有具体化，无法找到可对应的可核验结果。
- 「股票的牛市市场在其发展过程中将不断地为类似事件所打断，直至场内人士对此习以为常，无所畏惧，那也就是我们将要面对崩溃的时刻了。」——原文称牛市会不断被类似事件打断，直到场内人士习以为常、无所畏惧时才会崩溃，并说当时离那个阶段还很远。1987年10月确实发生了崩盘，但当时市场并非“无所畏惧”的状态，原文设定的前提无法核实，暂无法判断。 来源：https://www.federalreservehistory.org/essays/stock-market-crash-of-1987；https://www.gao.gov/assets/ggd-88-38.pdf
- 「最后，货币当局将再也无法容忍飞涨的市场——不过，这一时刻似乎还很遥远，至少对于美国股市而言是如此。」——原文称货币当局最终将无法容忍飞涨的市场，但这一时刻还很遥远。格林斯潘1996年公开讨论资产价格，但美联储随后长期不以抑制股市为目标，是否出现“无法容忍”的政策转向没有明确证据。 来源：https://www.federalreserve.gov/boarddocs/speeches/1996/19961205.htm；https://www.nytimes.com/1996/12/07/business/excerpt-from-the-speech-by-greenspan.html
- 「美国政府可能还会继续增    发超量的流动资金，但我认为这不至于搅起投机的泡沫，因为市场信心已经    严重动摇了，投资者很可能转向流动资产和黄金。」——原文称政府即使继续增发流动性也不会再搅起投机泡沫，投资者会转向流动资产和黄金。这是针对写作时短期市场状态的判断，时间范围和对象不清楚，暂无法判断。

## 5. 文件位置

- 最终结果：`cases/soros-alchemy-of-finance-v5/results.slim.jsonl`（同 `output/verify-final/results.slim.jsonl`），完整记录 `output/verify-final/results.jsonl`，汇总 `output/verify-final/summary.json`
- 人工决定：`cases/soros-alchemy-of-finance-v5/audit/manual_decisions_2026-11-15.py`；合成脚本 `audit/build_final.py`
- 机器原始结果：`output/verify-v5-run/`、`output/verify-v5-retry/`，合并 `output/verify-v5-combined/`
