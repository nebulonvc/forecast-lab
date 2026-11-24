# 马姆派斯、普林斯、谢赫、’t Hart（荷兰政府政策科学委员会WRR）《在碎片化世界秩序中航行：荷兰的挑战与机遇》（Navigating a Fragmenting World Order）：出版后预测人工核查

- 案例目录：`cases/mampuys-navigating-fragmenting-world-order-v5/`
- 出版日期：荷兰文原版为 WRR 第109号报告，**2024年7月1日**发布，按2024-07起算；英文改编版由 Springer 于2025年9月16日开放获取出版（CC BY-NC-ND 4.0）。正文用 Springer 英文版 PDF（sha256 `baa12d5d…`，147页，与队列记录一致），用 `pdftotext -enc UTF-8` 转成 TXT（sha256 `3efddbd9…`），TXT 不入库。观察窗口为2024-07-01至2026-11-15。英文版前言写于特朗普第二任期约100天时，属于书前部分，不计入评分。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

抽取：用仓库 prepare_book v5 流水线把全文切成120块（3500字符、600字符上下文），助手逐块通读，按 DISCOVER_PROMPT_V5 写出模型本应返回的 JSON（不做关键词筛选）。仓库代码完成引文对齐、归属降级和去重，导入30条候选，其中14条可核验（resolvable）。核验：每条先写 scope，各做一次 support 和 counter 的 Exa 检索，对第11、13条又各补了一轮检索；只从检索返回的 URL 中选源，原文存档在 data/sources（sha256），写入 data/evidence.jsonl（47条）；助手阅读后按四分类规则判断，再经 pipeline.py apply assess → check → report。本稿由助手逐条对照书中原文与存档证据人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 14 条，剔除非预测 0 条，计入 **14 条预测**，其中 **7 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 2 |
| 趋势符合 | 1 |
| 部分符合 | 3 |
| 错误 | 1 |
| 暂无法判断 | 7 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **28.6%**（2/7） |
| 加权胜率 | **60.7%** |
| 错误率 | **14.3%**（1/7） |
| 未定占比（暂无法判断/预测） | 50.0%（7/14） |

## 总体评价

这是一份政策咨询报告，大部分篇幅在描述现状、提出建议，真正可核验的预测不多（120块中14条，密度约0.12条/块，低于英文书0.2–0.35的目标；第100–120块为专家名单、术语表、参考文献和索引）。有短期具体日期的判断中，荷兰最高法院F-35案预计“2025年初”宣判，实际在2025年10月3日，判为错误。说对的两条：印度人口继续增长，以及国际紧张加剧时荷兰会面对更多针对重要基础设施的攻击（AIVD、MIVD年度报告证实）。部分应验的三条：欧洲国防投资大增但团结和效能仍不足，关键矿产的依赖风险因中国出口管制变成现实但价格并未持续上涨，欧盟—南共市协定在法国、意大利阻挠和欧洲议会提交欧盟法院审查后仍有拖延，但临时贸易协定已于2026年5月1日开始适用。非洲作用上升只记趋势符合。粮价、快速入盟和北约第五条三条复核后都改为暂无法判断：证据只能说明部分事实或政策讨论，不能确认、也不能否定原句的结果。中美经济总量追赶、欧盟扩大、台海冲突风险和去风险化的繁荣损失，或者终点未到，或者前提未发生，或者无法归因，同样记为暂无法判断。可判定的只有7条，样本太小，胜率不宜外推。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（2 条）

- **#2** 「India’s population is set to continue to grow for a considerable time to come」  
  判断：**正确**。联合国《世界人口展望2024》预计印度人口将持续增长至2060年代初约17亿后才见顶；联合国人口基金2025年报告估计印度人口已达约14.64亿（高于2024年的约14.5亿），尽管总和生育率已降到1.9，人口仍在增长，与“还将在相当长时间内继续增长”一致  
  来源：<https://www.thehindu.com/news/national/indias-population-to-peak-in-early-2060s-to-17-billion-before-declining-united-nations/article68395623.ece>；<https://www.thehindu.com/news/national/indias-population-reaches-14639-crore-fertility-rate-drops-below-replacement-level-un-report/article69679518.ece>；<https://casi.sas.upenn.edu/iit/data-for-india-rukmini-2025-part-one>
- **#13** 「the Netherlands will find itself facing even more attacks on vital infrastructure (both physical and digital) …」  
  判断：**正确**。国际紧张这一前提在窗口内成立。荷兰军事情报安全局2024年度报告（2025年4月发布）称荷兰“越来越频繁地”遭受旨在扰乱社会的混合攻击，其中包括针对重要基础设施的网络破坏；通用情报安全局2024、2025年度报告称俄罗斯的破坏、网络攻击和影响行动更具攻击性，2025年网络威胁比此前估计的更大。这与“攻击会更多”一致  
  来源：<https://www.rijksoverheid.nl/actueel/nieuws/2025/04/22/russische-brutaliteit-om-samenleving-te-ontwrichten-neemt-toe>；<https://www.aivd.nl/site/binaries/site-content/collections/documents/2025/04/24/jaarverslag-2024/AIVD+Jaarverslag+2024+.pdf>；<https://www.aivd.nl/actueel/magazines/jaarverslag/jaarverslag/2025/cyberdreigingen>；<https://www.dutchitchannel.nl/news/617026/mivd-nederland-is-steeds-vaker-doelwit-van-hybride-aanvallen>

### 趋势符合（1 条）

- **#4** 「is set to play an increasing role on the global stage due to its enormous demographic expansion」  
  判断：**趋势符合**。方向上有证据支持：2025年南非成为首个担任二十国集团主席国并主办峰会的非洲国家（此前一年非盟已成为G20正式成员），查塔姆研究所2025年12月报告称非洲在全球治理中的影响力日益增强；但这是长期趋势判断，窗口不到两年半，也有研究提醒非洲面临被进一步边缘化的风险，故只记趋势符合  
  来源：<https://www.g20.utoronto.ca/analysis/251115-kirton-prospects.html>；<https://www.chathamhouse.org/sites/default/files/2025-12/Africa%27s%20rising%20influence%20-%20Advancing%20agency%20in%20foreign%20policy%20and%20global%20governance.pdf>；<https://futures.issafrica.org/blog/2025/Africa-needs-a-new-diplomacy>

### 部分符合（3 条）

- **#3** 「This appears to be changing now that the leaders of government of the Member States presented ambitious plans …」  
  判断：**部分符合**。国防投入一项应验：欧洲防务局数据显示欧盟27国国防开支2024年达3430亿欧元（较2023年增19%），2025年达4180亿欧元（再增20%）。但书中说的是“欧洲军事团结与效能不足”正在改变，2025年欧洲防务局、欧洲议会研究处和欧盟安全研究所仍指出防务工业高度碎片化、缺乏联合采购和统一规划，团结和效能的改变只是部分发生  
  来源：<https://eda.europa.eu/news-and-events/news/2025/09/02/eu-defence-spending-hits-343-bln-in-2024-eda-data-shows>；<https://eda.europa.eu/news-and-events/news/2026/07/16/eu-defence-spending---418-billion-in-2025--projected-to--454-billion-in-2026>；<https://www.eesc.europa.eu/en/news-media/news/no-more-national-preference-fragmentation-threat-security-eda-tells-eesc-forum>；<https://www.europarl.europa.eu/RegData/etudes/BRIE/2025/775924/EPRS_BRI(2025)775924_EN.pdf>
- **#5** 「the scarcity of these raw materials will only increase, and with it the risks involved in being dependent on t…」  
  判断：**部分符合**。依赖风险一项应验：国际能源署指出2025年中国对重稀土等实施出口管制，使供应集中风险“变成现实”，冶炼集中度上升。但“稀缺只会加剧”与市场数据不完全一致：2023—2024年关键矿产价格大幅下跌，锂现货价跌约75%，国际能源署2025年展望认为多数矿产供需趋于改善（铜、锂除外）  
  来源：<https://www.iea.org/commentaries/with-new-export-controls-on-critical-minerals-supply-concentration-risks-become-reality>；<https://www.iea.org/reports/global-critical-minerals-outlook-2025/executive-summary>；<https://www.iea.org/reports/global-critical-minerals-outlook-2024/executive-summary>；<https://www.iea.org/reports/global-critical-minerals-outlook-2025/overview-of-outlook-for-key-minerals>
- **#11** 「There is nevertheless a risk of stalling due to individual Member States’ insistence on protecting highly spec…」  
  判断：**部分符合**。停滞风险部分应验：2025年12月法国、意大利以保护农民为由要求推迟，签署一度受阻；2026年1月9日理事会批准签署时法国投反对票；1月21日欧洲议会以334比324将协定提交欧盟法院审查，冻结了批准程序。但临时贸易协定自2026年5月1日起已开始适用，协定整体并未停摆  
  来源：<https://apnews.com/article/mercosur-france-trade-eu-protest-france-farmers-8ab1538cde4af959bd10b6ce7fd0bb25>；<https://www.consilium.europa.eu/en/press/press-releases/2026/01/09/eu-mercosur-council-greenlights-signature-of-the-comprehensive-partnership-and-trade-agreement/>；<https://agenceurope.eu/en/bulletin/article/13791/2/european-parliament-votes-to-refer-matter-to-eu-court-of-justice-thereby-freezing-ratification-process-for-agreement>；<https://trade.ec.europa.eu/access-to-markets/en/news/application-eu-mercosur-interim-trade-agreement-1-may-2026>

### 错误（1 条）

- **#12** 「The Supreme Court’s ruling is expected in early 2025.」  
  判断：**错误**。荷兰最高法院（Hoge Raad）的F-35零部件出口案（案号24/01340）于2025年10月3日宣判，而不是书中预计的“2025年初”  
  来源：<https://uitspraken.rechtspraak.nl/details?id=ECLI%3ANL%3AHR%3A2025%3A1435>；<https://www.hogeraad.nl/actueel/nieuwsoverzicht/2025/oktober/supreme-court-minister-must-perform-reassessment-licence-to-export-35/>；<https://www.reuters.com/business/aerospace-defense/dutch-supreme-court-orders-government-review-israel-weapons-export-policy-2025-10-03/>

### 暂无法判断（7 条）

- **#1** 「it may well catch up with the US within just a few years’ time」  
  判断：**暂无法判断**。书中称中国“可能在短短几年内赶上美国”（经济总量）。窗口内（2024-07至2026-11）尚未发生，且按名义美元计差距在扩大：2025年美国GDP约30.8万亿美元、中国约19.5万亿美元，差距约11.3万亿美元创纪录；但“几年内”的终点尚未完全到期，故暂不判对错，只记录目前方向与预测相反  
  来源：<https://kitegraph.com/insights/us-gdp-29-trillion>；<https://businesstats.com/world-economy/>；<https://doubleline.com/markets-insights/still-number-two/>
- **#6** 「supplying food in a fragmenting world risks becoming more expensive and inefficient」  
  判断：**暂无法判断**。2025年粮价较2024年回升4.3%，但2024年全年价格下降2.1%，且价格指数不等于供应效率；存档不足以把变动归因于碎片化，也不能验证“低效”，故暂无法判断。  
  来源：<https://www.fao.org/newsroom/detail/fao-food-price-index-dips-in-december-despite-higher-world-cereal-quotations/en>；<https://www.france24.com/en/live-news/20250103-world-food-prices-dip-2-in-2024-fao>；<https://www.iep.ru/ru/doc/43106/price-dynamics-on-global-food-markets-in-2025-and-expectations-for-2026-1-206-february-2026.pdf>
- **#7** 「Further enlargement will open the door to more political regimes of this kind.」  
  判断：**暂无法判断**。预测以“进一步扩大”为前提。截至2026年11月欧盟仍为27国，没有新成员加入；欧委会2026年扩大报告称黑山最早可能2028年入盟。前提尚未发生，故不判对错  
  来源：<https://european-union.europa.eu/principles-countries-history/eu-enlargement_en>；<https://www.dw.com/en/eu-says-montenegro-on-track-to-become-blocs-next-member-state-by-2028/a-79855011>；<https://enlargement.ec.europa.eu/news/2026-enlargement-package-shows-reform-commitment-delivers-progress-towards-eu-membership-2026-11-04_en>
- **#8** 「It is possible that accession may be fast-tracked—in the interests of security—because the EU is prepared to r…」  
  判断：**暂无法判断**。存档确认2026年欧委会考虑乌克兰快速、有限权利入盟，但考虑方案不等于实际放宽法治标准并接纳新成员；截至截止日该结果未实现，且原句为无截止日期的可能性，暂无法判断。  
  来源：<https://www.reuters.com/world/eu-executive-weighs-idea-quick-limited-membership-ukraine-2026-01-16/>；<https://www.europarl.europa.eu/RegData/etudes/BRIE/2026/796998/EPRS_BRI%282026%29796998_EN.pdf>；<https://www.rferl.org/a/hungary-veto-eu-enlargement-/33452824.html>
- **#9** 「a US President who openly questions Article 5 of the NATO Treaty could well render the alliance ineffective」  
  判断：**暂无法判断**。2025年6月特朗普公开质疑第五条的条件已满足，但北约海牙宣言随后重申共同防御并作出开支决策，不能据此确认联盟失效；也不能因短期未失效就否定无时间限定的“可能失效”风险，暂无法判断。  
  来源：<https://www.politico.eu/article/donald-trump-nato-summit-sidesteps-article-5-mark-rutte-eu-defense-budget-russia-vladimir-putin-iran-israel-strikes-qatar/>；<https://www.nato.int/en/about-us/official-texts-and-resources/official-texts/2025/06/25/the-hague-summit-declaration>；<https://www.reuters.com/business/aerospace-defense/nato-leaders-set-back-trump-defence-spending-goal-hague-summit-2025-06-24/>
- **#10** 「China’s increasingly assertive policy with regard to Taiwan and in the South China Sea could lead to a large-s…」  
  判断：**暂无法判断**。这是无时间限定的风险判断（“可能导致”）。窗口内中国在台湾周边和南海的军事活动确实增加（2025年12月举行迄今规模最大的演习），但没有爆发大规模地区或全球冲突。风险判断不能凭“尚未发生”判错，故暂无法判断  
  来源：<https://chinapower.csis.org/china-increased-military-activities-indo-pacific-2025/>；<https://www.gbnews.com/news/world/south-china-sea-peaceful-china-launches-biggest-military-exercise-taiwan>；<https://www.uscc.gov/sites/default/files/2025-11/Chapter_2--U.S.-China_Security_and_Foreign_Affairs_Year_in_Review.pdf>
- **#14** 「This shift will inevitably involve a loss of prosperity.」  
  判断：**暂无法判断**。“去风险化必然带来繁荣损失”只能用情景模型间接估计（国际货币基金组织、欧洲央行体系等估算的碎片化成本），无法从实际数据中单独分离出来；同期荷兰经济2024年增长0.9%，2025年增长约1.7%，并未见到可归因于去风险化的明显繁荣损失。证据不足以判断  
  来源：<https://cepr.org/voxeu/columns/trade-wars-and-fragmentation-insights-new-escb-report>；<https://www.imf.org/-/media/files/publications/wp/2024/english/wpiea2024122-print-pdf.pdf>；<https://www.dnb.nl/en/general-news/press-release-2025/dutch-economy-shows-remarkably-higher-growth/>；<https://english.dsta.nl/latest/magazines/quarterly-outlook/2025/q2-2025/economic-outlook>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/mampuys-navigating-fragmenting-world-order-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/mampuys-navigating-fragmenting-world-order-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/mampuys-navigating-fragmenting-world-order-v5/audit/manual_review_2026-11-15.py`

## 说明

- 抽取密度偏低（14/120≈0.12条/块）。原因是本书为政策咨询报告，以现状描述和规范性建议为主；约21块是参考文献、术语表和索引，约12块是章末注释。
- 第7条以“进一步扩大”为前提，窗口内欧盟没有新成员，前提未成立。第9条（美国总统质疑第五条）条件已满足；北约随后重申共同防御并通过开支决定，但这不能确认联盟失效，也不能否定无时间限定的“可能失效”风险，故记为暂无法判断。
- 第6、8条复核后改判暂无法判断：存档说明了粮价波动和欧盟的政策讨论，但不能把粮价归因于碎片化，也不能证明实际快速入盟或放宽标准。
- 第1条（中国“几年内”追上美国）截至2026年差距反而扩大，但“几年内”的终点尚未完全到期，记为暂无法判断。
- 统计以 pipeline.py report 的 summary.json 为准；加权胜率按 manual_report.py 的权重计算（正确×1 + 趋势符合×0.75 + 部分符合×0.5）。

