# 克莱顿·克里斯坦森《创新者的窘境》（The Innovator’s Dilemma，1997；2000 年增订重印本）：出版后预测人工核查

- 案例目录：`cases/christensen-innovators-dilemma-v5/`
- 出版日期：Harvard Business School Press 初版 1997 年（献词署 1997 年 4 月，Boston）。版权页署 Copyright 1997, 2000。所用文件为后来重印的 Harvard Business Review Press 英文电子版（ISBN 978-1-4221-9602-1，340 PDF 页）。正文未见另写的 2011 年新序；书末 About the Author 提到 Thinkers50 与《你要如何衡量你的人生》，属重印时更新的作者介绍，已作后页排除。**默认按 1997 年起算**；引言“WHERE DISRUPTIONS ARE HAPPENING TODAY”与第 8 章写明“本章写于 2000 年 2 月”的戴姆勒–克莱斯勒段落，按 **2000 年**起算。观察窗口至 2026-11-15。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

按仓库 DeepSeek 管线手工代替模型调用：以 `pdftotext 25.03.0 -enc UTF-8` 生成全书 TXT（sha256 `9ef58c092f27d19eeb50793ab979d89a3535f0c4d77c45169bb9e88c35910b09`，530,963 字符），`prepare_book.split_text(3500, 600)` 得到 154 个 chunk。自定义 matter_spans 排除文前系列说明/版权/目录/致谢（0–5921）与文后 Book Group Guide / About the Author（518128–530963），保留 txt-00002–txt-00150 共 149 块并逐块通读。经 `validate_chunk_predictions` 与 `claims_from_results` 导入 34 条可解析预测（全部 `claim_type=forecast`，无降为 unclear、无重叠去重）。引文均为 TXT 逐字片段，`changes` 为同一物理行上的原文子串。记录字符偏移与 TXT/PDF sha256。全文 TXT 未入库。边界块只抽正文、不抽致谢与书友指南。第 1–4 章主体为 1997 年前产业史，未把史实写成预测。本稿由助手逐条对照书中原文，并依据各条适用的出版年（1997 或 2000）至 2026-11-15 窗口内可公开访问的来源人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 34 条，剔除非预测 0 条，计入 **34 条预测**，其中 **34 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 14 |
| 趋势符合 | 0 |
| 部分符合 | 17 |
| 错误 | 3 |
| 暂无法判断 | 0 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **41.2%**（14/34） |
| 加权胜率 | **66.2%** |
| 错误率 | **8.8%**（3/34） |
| 未定占比（暂无法判断/预测） | 0.0%（0/34） |

## 总体评价

《创新者的窘境》的可核验判断，一部分是跨产业的破坏性创新机制，一部分是第 10 章里把同一套机制用到当时尚未成形的电动汽车上的具体预言。机制性判断在 1997 年后的窗口里整体方向偏对：闪存没有被 Quantum、Seagate 这类磁盘公司做成市场领导者；数码摄影、移动电话、智能手机/平板和在线渠道确实冲击了胶片、固网和个人电脑；把破坏性技术硬塞给当前主流客户、或把它关在实验室里打磨到“够好”再上市，事后往往不如先为现有属性找到市场的做法。戴姆勒整合克莱斯勒后的结局，也和 2000 年增订文字里的担心一致。miss 得比较清楚的，集中在电动汽车的早期形态。作者几乎肯定最初的价值网会是一个把短续航、慢加速变成优点的市场，第一阶段的获胜设计会以简单和便利为特征；后来真正打开高速公路电动车市场的，是 2008 年特斯拉 Roadster 那种高性能、高价跑车，而不是社区代步车。Saturn“很快上移并在低端留下真空”也没有成为事实，品牌在尝试 Aura 之后于 2010 年停掉。带日期或速率的电动车轨迹则对了一半：续航与加速后来确实进入主流可用区间，但提升速度远快于书中按当时 2%–4%/年外推的假设，特斯拉 Model S 在 2012 年就有 265 英里 EPA 续航，加速的交叉也早于 2020。政府强制令既出现过积分交易等扭曲，也在中国等地成为做大市场的政策工具，不能写成只扭曲、不解决问题。无日期的方向性判断按出版年到截止日计分：方向已经发生则记正确，不降为趋势符合。2000 年才写入的“正在颠覆”表和戴姆勒段落，不按 1997 年的有利位置计分。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（14 条）

- **#2** 「disruptive technologies that may underperform today, relative to what users in the market demand, may be fully…」  
  判断：**正确**。这一条是对破坏性技术供给轨迹的一般判断，不是单一产品预言。窗口内多次出现“今天不够好、后来在同一市场变得有竞争力”的情形：闪存固态盘进入曾由磁盘占据的笔记本和数据中心；数码影像取代胶片；智能手机和平板承担了大量原先只有个人电脑才做得好的任务；电动汽车续航和加速也进入可与燃油车相比的区间。方向已经发生。  
  来源：<https://evertiq.com/news/2025-03-05-weak-demand-pushes-4q24-nand-revenue-down-62>；<https://www.reuters.com/article/us-kodak-bankruptcy/focus-on-past-glory-kept-kodak-from-digital-win-idUSTRE80I1N020120119/>；<https://www.theguardian.com/technology/2013/aug/30/pc-boom-over-tablets-smartphones>；<https://www.iea.org/reports/global-ev-outlook-2025/executive-summary>；<https://chargedevs.com/newswire/epa-certifies-a-range-of-265-miles-for-tesla-model-s-deliveries-begin/>
- **#4** 「But the electric car is a disruptive technology and potential future threat.」  
  判断：**正确**。电动汽车后来确实成为对在位车企的实质性威胁。国际能源署《全球电动汽车展望 2025》写明：2024 年全球电动汽车销量超过 1700 万辆、份额超过 20%，仅 2024 年相对前一年的增量就超过 2020 年全年销量；中国电动汽车已占当年汽车销量近一半，美国超过十分之一。特斯拉、比亚迪等新进入者改变了竞争格局。无日期的方向性判断，方向已经发生。  
  来源：<https://www.iea.org/reports/global-ev-outlook-2025/executive-summary>；<https://www.iea.org/reports/global-ev-outlook-2024/trends-in-the-electric-vehicle-industry>
- **#6** 「Why this happened, and is still happening, is the subject of the next chapter.」  
  判断：**正确**。作者在总结硬盘史后断言，领先企业被破坏性技术颠覆的模式“仍在发生”。1997 年后的窗口里，这一模式在胶片、功能手机、传统个人电脑、实体零售和部分汽车业务中反复出现，不能视为已经被证伪的历史描述。  
  来源：<https://www.reuters.com/article/us-kodak-bankruptcy/focus-on-past-glory-kept-kodak-from-digital-win-idUSTRE80I1N020120119/>；<https://www.theguardian.com/technology/2013/aug/30/pc-boom-over-tablets-smartphones>；<https://www.npr.org/2024/12/06/nx-s1-5116270/ev1-general-motors-electric-vehicle>；<https://www.iea.org/reports/global-ev-outlook-2025/executive-summary>
- **#7** 「the value network framework would predict that firms similar to Quantum and Seagate are not likely to build ma…」  
  判断：**正确**。价值网框架的这一具体预测被后来的市场结构证实。TrendForce 口径的 2024 年四季度 NAND 营收份额为：三星 33.9%、SK 集团 20.5%、铠侠 16.1%、美光 13.8%、西部数据/闪迪 11.4%，名单中没有 Seagate，也没有 Quantum。与磁盘厂商同类的西部数据通过收购闪迪进入 NAND，但并未取得市场领先地位。  
  来源：<https://evertiq.com/news/2025-03-05-weak-demand-pushes-4q24-nand-revenue-down-62>
- **#8** 「whether market and technological trajectories may eventually intersect, carrying technologies that do not addr…」  
  判断：**正确**。市场与技术轨迹相交、使起初不满足主流需求的技术后来迁入主流，是窗口内多次被观察到的结果：闪存进入计算机存储，智能手机进入原属电脑的计算与通信，电动汽车续航进入可日常使用的区间。方向已经发生。  
  来源：<https://evertiq.com/news/2025-03-05-weak-demand-pushes-4q24-nand-revenue-down-62>；<https://www.theguardian.com/technology/2013/aug/30/pc-boom-over-tablets-smartphones>；<https://chargedevs.com/newswire/epa-certifies-a-range-of-265-miles-for-tesla-model-s-deliveries-begin/>；<https://www.iea.org/reports/global-ev-outlook-2025/executive-summary>
- **#12** 「However, integrating the two companies would likely vaporize the key processes that made Chrysler such an attr…」  
  判断：**正确**。该条按 2000 年 2 月起算。戴姆勒与克莱斯勒在 1998 年合并后确实推进整合，随后出现文化冲突、克莱斯勒核心高管在 2000 年前后大量离职，梅赛德斯方面也不信任克莱斯勒的产线与品控。2007 年戴姆勒把克莱斯勒以约 74 亿美元卖给 Cerberus，远低于当初约 350 亿美元的合并估值。《哈佛商业评论》称两者从未变成一个真正一体的组织，潜在协同并未实现。整合努力之后，使克莱斯勒值得被收购的流程与班子明显被消耗，与预测方向一致。  
  来源：<https://www.theguardian.com/business/2007/may/14/motoring.lifeandhealth>；<https://hbr.org/2007/05/why-the-daimlerchrysler-merger>
- **#13** 「The rank-ordering of the criteria by which customers choose one product or service over another will change,」  
  判断：**正确**。条件是出现性能供给过剩。个人电脑在时钟频率和基准性能超过典型需求后，竞争转向便携、续航、价格和形态，并让出大量任务给手机和平板；存储、消费电子和后来的汽车电动化中，也出现过“功能够用之后改比别的属性”的转换。条件在多个产业被触发，方向已经发生。  
  来源：<https://www.computerworld.com/article/1705275/intel-sets-cruise-control-on-pentium-4.html>；<https://www.theguardian.com/technology/2013/aug/30/pc-boom-over-tablets-smartphones>；<https://www.marketwatch.com/story/one-chart-shows-how-mobile-has-crushed-pcs-2016-04-20?link=sfmw_sm>
- **#15** 「companies that keep disruptive technologies bottled up in their labs, working to improve them until they suit …」  
  判断：**正确**。把尚未适合主流的技术关在实验室或合规项目里打磨，窗口内的结果通常不如先为现有属性找到市场。通用汽车的 EV1 在主流汽车框架里推进后被收回销毁；特斯拉则先把当时的锂离子电池用在跑车市场，再进入更大的轿车市场。柯达对损害胶片利润的数码技术长期犹豫，也是同一对照。  
  来源：<https://www.npr.org/2024/12/06/nx-s1-5116270/ev1-general-motors-electric-vehicle>；<https://www.hagerty.com/media/car-profiles/ev1-may-have-been-first-demise-launched-tesla/>；<https://www.technologyreview.com/2008/08/19/219217/tesla-roadster-2/>；<https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/whats-wrong-with-this-picture-kodaks-30-year-slide-into-bankruptcy/>
- **#16** 「the consequent likelihood that disruptive approaches will change the nature of competition in their industry.」  
  判断：**正确**。在性能供给过剩或新属性被市场接受后，破坏性路径确实改变了多个产业的竞争性质：智能手机改变了计算与通信的主战场，流媒体和在线零售改变了媒体与渠道，电动汽车正在改变汽车业的动力、渠道和成本结构。  
  来源：<https://www.theguardian.com/technology/2013/aug/30/pc-boom-over-tablets-smartphones>；<https://www.iea.org/reports/global-ev-outlook-2025/executive-summary>；<https://www.reuters.com/article/us-kodak-bankruptcy/focus-on-past-glory-kept-kodak-from-digital-win-idUSTRE80I1N020120119/>
- **#17** 「this could create an opportunity for a disruptive technology—applets picked off the internet and used in simpl…」  
  判断：**正确**。典型用户对完整个人电脑和桌面软件的功能需求，在 2000 年代后明显被“超过”：大量任务转到浏览器、手机应用和云端。Chromebook、智能手机和平板正是从下方进入的“互联网电器”类设备；BBC 与 ABI 都记录了 Chromebook 对低端 PC 和教育市场的冲击，IDC 则把 PC 见顶主要归因于手机和平板。条件成立，结果发生。  
  来源：<https://www.bbc.com/news/technology-24472567>；<https://www.abiresearch.com/press/chromebooks-cloud-centric-computing-style-disrupts>；<https://www.theguardian.com/technology/2013/aug/30/pc-boom-over-tablets-smartphones>
- **#18** 「Is it possible that sometime soon the speed and cost of Intel’s new microprocessors might overshoot market dem…」  
  判断：**正确**。“不久之后”按 1990 年代末起算，到 2004–2005 年已经可以核验：Intel 在 Pentium 4 上触及频率墙，因功耗和发热放弃继续堆主频，转向双核与每瓦性能。时钟频率不再是主流买家的首要尺度，低功耗与移动端需求改由 ARM 等路径占据。这一“可能超过市场需求”的设问，被随后的频率墙和后 PC 转移坐实。  
  来源：<https://www.computerworld.com/article/1705275/intel-sets-cruise-control-on-pentium-4.html>；<https://www.eetimes.com/intels-a-victim-of-its-own-success/>；<https://www.theguardian.com/technology/2013/aug/30/pc-boom-over-tablets-smartphones>
- **#20** 「Ironically, I would expect most automakers to focus precisely and myopically on the mainstream market because …」  
  判断：**正确**。在特斯拉打开市场之前，多数在位车企的确把资源集中在当时的主流燃油车：通用汽车在加州强制令放松后于 2002–2003 年终止 EV1 并收回车辆。后来的叙述也把在位者当时的兴趣缺位，视为特斯拉得以起步的条件之一。无日期方向已经发生；2010 年代后期传统车企大规模跟进，并不否定此前长时间的主流聚焦。  
  来源：<https://www.npr.org/2024/12/06/nx-s1-5116270/ev1-general-motors-electric-vehicle>；<https://www.hagerty.com/media/car-profiles/ev1-may-have-been-first-demise-launched-tesla/>；<https://www.iea.org/reports/global-ev-outlook-2025/executive-summary>
- **#30** 「For many years into the future, the market for electric vehicles will be so small that this business is unlike…」  
  判断：**正确**。“未来许多年”从 1997 年看，在接下来大约二十年里确实如此：即便到 2020 年，全球电动车销量仍小于 2024 年一年的增量（国际能源署：2024 年增量约 350 万辆，已超过 2020 年全球总销量）。在很长一段时间里，它对大型车企的营收和利润都不足以构成主业贡献。该判断并不要求这一市场永远很小；2010 年代末以后特斯拉、比亚迪以及大众等车企电动车业务变得显著，并不否定“许多年里很小”已经成立。  
  来源：<https://www.iea.org/reports/global-ev-outlook-2025/executive-summary>；<https://www.volkswagen-group.com/en/press-releases/volkswagen-group-achieves-robust-annual-results-for-2023-with-a-strong-fourth-quarter-18250>
- **#34** 「conventional managerial wisdom at established firms constitutes an entry and mobility barrier that entrepreneu…」  
  判断：**正确**。在位企业按既有利润模型拒绝或推迟破坏性业务，在窗口内多次成为新进入者可以利用的缝隙：特斯拉方面把通用汽车结束 EV1、在位者当时公开的兴趣不足视为机会；柯达对损害胶片利润的技术长期犹豫，也为新的数码厂商让出空间。这并不保证创业者一定成功，但“可以指望”的进入壁垒确实存在并被利用。  
  来源：<https://www.hagerty.com/media/car-profiles/ev1-may-have-been-first-demise-launched-tesla/>；<https://www.npr.org/2024/12/06/nx-s1-5116270/ev1-general-motors-electric-vehicle>；<https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/whats-wrong-with-this-picture-kodaks-30-year-slide-into-bankruptcy/>

### 部分符合（17 条）

- **#1** 「In the near future, “internet appliances” may become disruptive technologies to suppliers of personal computer…」  
  判断：**部分符合**。书中“不远的将来”指向的网络电脑和第一代互联网电器，在 1990 年代末到 2001 年前后并没有颠覆个人电脑：Oracle 的网络电脑业务约 1999 年收摊，当时媒体已把互联网电器称作“PC 杀手”的落空。真正从下方冲击 PC 供应商的，是约十年后的智能手机和平板：IDC 称全球 PC 出货在 2011 年约 3.59 亿台见顶，此后被手机和平板分流，戴尔、惠普等未能在移动端补上缺口。近预期落空，较晚的方向成立，故记部分符合。  
  来源：<https://www.wired.com/2009/12/fail-oracle/>；<https://www.cnn.com/2001/TECH/ptech/04/16/net.appliances.idg/index.html>；<https://doi.org/10.1504/ijtip.2007.013035>；<https://www.theguardian.com/technology/2013/aug/30/pc-boom-over-tablets-smartphones>；<https://www.theguardian.com/technology/2011/apr/14/pc-market-has-passed-its-peak>
- **#3** 「it becomes progressively more difficult for them to enter the even newer small markets destined to become the …」  
  判断：**部分符合**。柯达面对数码摄影、通用汽车中止 EV1、以及多家个人电脑厂商未能切入智能手机等案例，都符合“成功的大公司难以进入后来做大的新小市场”。但并非定律：有的在位者后来仍进入或并购补位（西部数据经 SanDisk 进入 NAND，传统车企在 2010 年代后期大规模跟进电动车）。主方向常见，普遍性不足，记部分符合。  
  来源：<https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/whats-wrong-with-this-picture-kodaks-30-year-slide-into-bankruptcy/>；<https://www.npr.org/2024/12/06/nx-s1-5116270/ev1-general-motors-electric-vehicle>；<https://www.theguardian.com/technology/2013/aug/30/pc-boom-over-tablets-smartphones>；<https://evertiq.com/news/2025-03-05-weak-demand-pushes-4q24-nand-revenue-down-62>
- **#5** 「Each of the innovations in the right column—in the form of a new technology or a new business model—is now in …」  
  判断：**部分符合**。该表是 2000 年增订，按 2000 年起算。此后多项右栏创新确实冲击了左栏：数码摄影伴随柯达 2012 年破产；移动电话订户在 2002 年前后超过固定电话；在线零售、在线券商、手持数字设备、IP 与分组交换等也明显改写了相应行业。但并非每一行都完成颠覆：PlayStation II 和当年的互联网电器并未取代桌面电脑（后者的冲击来得更晚、形态也不同）；许多早期 B2B 交易所并未取代工业分销；管理研究生院和电力公司也未被企业大学或分布式发电整体取代。表中“每一项都正在颠覆”说得过满，记部分符合。  
  来源：<https://www.reuters.com/article/us-kodak-bankruptcy/focus-on-past-glory-kept-kodak-from-digital-win-idUSTRE80I1N020120119/>；<https://www.itu.int/ITU-D/finance/work-cost-tariffs/events/tariff-seminars/prague-03/10-Shaw-mobile-overtakes-fixed.pdf>；<https://www.theguardian.com/technology/2013/aug/30/pc-boom-over-tablets-smartphones>；<https://www.iea.org/reports/global-ev-outlook-2025/executive-summary>
- **#9** 「Ultimately, the number of users at the highest-performance end of the market, toward which the laser jet divis…」  
  判断：**部分符合**。作者预期激光打印不断上移后，最高性能端用户会变少，喷墨可能从下方蚕食。实际演化更接近整个打印市场成熟、纸面用量下降，以及办公场景里激光仍占主导：惠普在 2021 年停掉面向办公的 PageWide 喷墨产品线，分析认为办公喷墨与激光在成本、体积和性能上已经接近，激光仍是办公创新的重点。高端用户“变少”在整个市场收缩的意义上部分出现，但被喷墨掏空激光高端的机制并未清楚发生。  
  来源：<https://keypointintelligence.com/keypoint-blogs/a-second-take-on-hps-discontinuation-of-pagewide-office-products>
- **#10** 「Experts’ forecasts will always be wrong.」  
  判断：**部分符合**。把专家对破坏性技术市场的预测写成“将总是错误”，过强。网络电脑、早期互联网电器和若干电动车时间表确实严重偏离，但窗口内也有被后来数据大致坐实的判断（例如智能手机、平板对 PC 出货的分流，以及电池成本的长期下降）。常常错，不是总是错。  
  来源：<https://www.wired.com/2009/12/fail-oracle/>；<https://www.theguardian.com/technology/2013/aug/30/pc-boom-over-tablets-smartphones>；<https://about.bnef.com/insights/clean-energy/lithium-ion-battery-pack-prices-hit-record-low-of-139-kwh/>；<https://www.iea.org/reports/global-ev-outlook-2025/executive-summary>
- **#11** 「companies’ initial strategies for entering these markets will generally be wrong.」  
  判断：**部分符合**。进入新破坏性市场时先走错、再靠试错纠正，在特斯拉从跑车到轿车再到量产车、以及许多互联网和硬件创业中都能看到。但“一般都会错”无法在窗口内被全面计量，也有第一次策略就大致成立的反例，故记部分符合。  
  来源：<https://www.technologyreview.com/2008/08/19/219217/tesla-roadster-2/>；<https://ir.tesla.com/press-release/tesla-motors-delivers-worlds-first-premium-electric-sedan>；<https://www.hagerty.com/media/car-profiles/ev1-may-have-been-first-demise-launched-tesla/>
- **#14** 「Customers will prefer those products that are the most convenient to use and those vendors that are most conve…」  
  判断：**部分符合**。功能→可靠性→便利→价格的排序，是对若干成熟市场的有用简化（手机在性能够用后转向易用和价格带分层）。但汽车、奢侈品和操作系统仍长期靠品牌、生态和性能指标竞争，并未干净地走到“便利被满足后只剩价格”。机制部分成立，不是普遍定律。  
  来源：<https://www.theguardian.com/technology/2013/aug/30/pc-boom-over-tablets-smartphones>；<https://www.iea.org/reports/global-ev-outlook-2025/executive-summary>
- **#19** 「the performance of electric vehicles is improving at a faster rate—between 2 and 4 percent per year— suggestin…」  
  判断：**部分符合**。电动汽车后来确实从无法竞争于主流，走到了可竞争的位置，国际能源署显示 2024 年全球销量份额已超过 20%。但实现路径不是书中当时观察到的每年约 2%–4% 的改进：BloombergNEF 记录锂离子电池包价格在 2010–2023 年按 2023 年美元计下降约 90%（约 1391 美元/千瓦时降至 139 美元/千瓦时），能量密度的年改进也快于 2%–4%。终点发生，速率假设明显偏低。  
  来源：<https://www.iea.org/reports/global-ev-outlook-2025/executive-summary>；<https://about.bnef.com/insights/clean-energy/lithium-ion-battery-pack-prices-hit-record-low-of-139-kwh/>；<https://chargedevs.com/newswire/epa-certifies-a-range-of-265-miles-for-tesla-model-s-deliveries-begin/>
- **#21** 「Government mandates, incidentally, are likely to distort rather than solve the problem of finding a market.」  
  判断：**部分符合**。加州零排放车强制令确实出现过积分储存与交易、用合规手段代替真实销量的扭曲，并于此后多次修订，与“扭曲而非解决如何找到市场”部分相符。但同一窗口里，政策支持也被国际能源署列为中国和部分新兴市场电动车放量的关键因素，并不能写成强制令只扭曲、不创造市场。  
  来源：<https://itspubs.ucdavis.edu/download_pdf.php?id=1038>；<https://www.journals.uchicago.edu/doi/10.1086/713055>；<https://www.iea.org/reports/global-ev-outlook-2025/executive-summary>
- **#23** 「we can safely predict that the basis of product competition and customer choice will shift away from these mea…」  
  判断：**部分符合**。安全、可靠、信息和驾驶辅助等属性确实变得更重要，购车决策不再只看马力和极速。但窗口内功能竞争并未退出：SUV 的尺寸与通过性、电动车的加速指标和续航数字仍是重要卖点，尤其在特斯拉之后，性能本身再次成为营销中心。转向发生了，但不是从功能指标上的干净迁出。  
  来源：<https://www.iea.org/reports/global-ev-outlook-2025/executive-summary>；<https://www.technologyreview.com/2008/08/19/219217/tesla-roadster-2/>；<https://chargedevs.com/newswire/epa-certifies-a-range-of-265-miles-for-tesla-model-s-deliveries-begin/>
- **#26** 「A battery breakthrough is not likely to be required of companies whose executives choose to harness or account…」  
  判断：**部分符合**。若真的另建一个让短续航、低速成为优点的市场，低速电动车和邻里车辆确实不需要电池突破，这一条件路径存在。但窗口内做成大市场的路径，仍依赖锂离子电池在成本和能量密度上的大幅改进。因此“未必需要突破”只在利基市场上成立，不是主导商业路径。  
  来源：<https://about.bnef.com/insights/clean-energy/lithium-ion-battery-pack-prices-hit-record-low-of-139-kwh/>；<https://www.technologyreview.com/2008/08/19/219217/tesla-roadster-2/>；<https://www.iea.org/reports/global-ev-outlook-2025/executive-summary>
- **#27** 「The companies that ultimately achieve the advances in battery technology required to power cars for 150-mile c…」  
  判断：**部分符合**。150 英里续航这一条件已经被触发：2012 年交付的特斯拉 Model S，EPA 续航达到 265 英里；2017 年雪佛兰 Bolt 达到 238 英里。特斯拉确实用已有的锂离子电芯开辟了新的价值网，并随后进入更大市场，与“先建新价值网再发展持续性技术”部分相符。但它是先做高端再进入量产，而不是从低端新市场向上走；松下、宁德时代、比亚迪、LG 以及后来的在位车企同样是续航进步的重要来源。  
  来源：<https://ir.tesla.com/press-release/tesla-motors-delivers-worlds-first-premium-electric-sedan>；<https://chargedevs.com/newswire/epa-certifies-a-range-of-265-miles-for-tesla-model-s-deliveries-begin/>；<https://www.cbsnews.com/sanfrancisco/news/chevrolet-bolt-238-miles-charge-tesla-electric-car/>；<https://www.iea.org/reports/global-ev-outlook-2025/executive-summary>
- **#28** 「the impetus to find the battery breakthrough will indeed be strongest among the disruptive innovators, which w…」  
  判断：**部分符合**。推动电池大幅进步的，既有特斯拉、比亚迪这类新进入者，也有松下、LG、宁德时代等电芯企业和随后加大投入的在位车企。特斯拉并不是“先建立低端电动车市场再向上走”的典型；把最强动力完全归给这类破坏性创新者，并不符合后来的产业分工。  
  来源：<https://about.bnef.com/insights/clean-energy/lithium-ion-battery-pack-prices-hit-record-low-of-139-kwh/>；<https://ir.tesla.com/press-release/tesla-motors-delivers-worlds-first-premium-electric-sedan>；<https://www.iea.org/reports/global-ev-outlook-2025/executive-summary>
- **#29** 「I’d bet that mainstream dealers of gasoline-powered automobiles would not view the sorts of disruptive electri…」  
  判断：**部分符合**。在电动车仍属边缘产品时，主流燃油车经销商确实没有把它视为成功的关键，这也是特斯拉走直销、并与经销商游说集团长期冲突的背景（凯托研究所 2014 年的综述记录了特许经营法之争）。当电动车销量变得可观之后，传统经销商也开始销售、租赁和维修电动车，态度不再是单纯忽视。前半段符合，后半段已变化。  
  来源：<https://www.cato.org/regulation/summer-2014/tesla-car-dealers-lobby>；<https://www.iea.org/reports/global-ev-outlook-2025/executive-summary>
- **#31** 「we would expect the cruising range of electric cars, for example, to intersect with the average range demanded…」  
  判断：**部分符合**。前提是“若当时的改进速率得以维持”。实际速率远快于书中 2%–4% 的外推（电池包价格 2010–2023 年约降 90%）。续航方面，高端的 Model S 在 2012 年已达 265 英里，量大面广的主流车则要到 2016–2017 年的 Bolt 才稳定越过 200 英里；加速性能的交叉更早，Roadster 与 Model S 在 2008–2012 年就已经明显快于许多燃油车，早于 2020。交点大致出现，但前提未按原速率满足，时间表也对得不整齐。  
  来源：<https://about.bnef.com/insights/clean-energy/lithium-ion-battery-pack-prices-hit-record-low-of-139-kwh/>；<https://chargedevs.com/newswire/epa-certifies-a-range-of-265-miles-for-tesla-model-s-deliveries-begin/>；<https://www.cbsnews.com/sanfrancisco/news/chevrolet-bolt-238-miles-charge-tesla-electric-car/>；<https://www.technologyreview.com/2008/08/19/219217/tesla-roadster-2/>
- **#32** 「If, as most successful companies try to do, a company stretches or forces a disruptive technology to fit the n…」  
  判断：**部分符合**。在技术仍明显低于主流需求时，硬把它做成现有主流车的替代，窗口内多次失败或停滞，EV1 是典型。可一旦电池使电动车能够满足主流行程和加速，按主流轿车形态推出的车型（Model 3、比亚迪若干车型、大众 ID 系列等）也可以成功。“几乎肯定会失败”作为早期警告很强，作为无期限的普遍法则过绝对。  
  来源：<https://www.npr.org/2024/12/06/nx-s1-5116270/ev1-general-motors-electric-vehicle>；<https://ir.tesla.com/press-release/tesla-motors-delivers-worlds-first-premium-electric-sedan>；<https://www.iea.org/reports/global-ev-outlook-2025/executive-summary>
- **#33** 「Disruptive innovations entail significant first-mover advantages: Leadership is important.」  
  判断：**部分符合**。破坏性创新里确实常有先发并做大的例子（特斯拉在现代电动轿车、亚马逊在电商与云）。但先发失败、后发居上同样常见：网络电脑厂商、早期互联网电器、Better Place 以及许多第一代网站并未保住领导地位。先发有时重要，不是破坏性创新的一般定律。  
  来源：<https://www.technologyreview.com/2008/08/19/219217/tesla-roadster-2/>；<https://www.wired.com/2009/12/fail-oracle/>；<https://www.cnn.com/2001/TECH/ptech/04/16/net.appliances.idg/index.html>；<https://www.iea.org/reports/global-ev-outlook-2025/executive-summary>

### 错误（3 条）

- **#22** 「though it is impossible to predict, it almost surely will be one in which the weaknesses of the electric vehic…」  
  判断：**错误**。作者认为最初的价值网“几乎可以肯定”是一个把电动汽车弱点（短续航、慢加速、简单）视为优点的市场。真正打开现代高速公路电动车市场的，是 2008 年特斯拉 Roadster：MIT Technology Review 等当时报道把它作为高性能锂离子跑车，加速与续航是卖点而不是被当成优点的弱点。社区电动车、高尔夫球车等利基市场存在，但不是启动这一产业的价值网。“几乎可以肯定”没有发生。  
  来源：<https://www.technologyreview.com/2008/08/19/219217/tesla-roadster-2/>；<https://en.wikipedia.org/wiki/Tesla_Roadster_(first_generation)>；<https://ir.tesla.com/press-release/tesla-motors-delivers-worlds-first-premium-electric-sedan>
- **#24** 「it, too, judging by recent reports, 15 will soon take its turn moving upmarket, creating a new vacuum at the l…」  
  判断：**错误**。作者预测 Saturn 很快也会转向上端，并在低端留下真空。Saturn 虽在 2007 年推出更偏中级车的 Aura，但未能改写品牌命运；2009 年出售计划失败后，通用汽车关闭该品牌，经销权在 2010 年 10 月结束。上移没有站稳，也没有留下被更简单交通工具占据的持久低端真空。  
  来源：<https://www.reuters.com/article/business/gm-to-close-saturn-as-sale-to-penske-collapses-idUSTRE58T709/>；<https://www.nytimes.com/2008/12/04/business/04saturn.html>；<https://en.wikipedia.org/wiki/Saturn_Corporation>
- **#25** 「the winning design in the first stages of the electric vehicle race will be characterized by simplicity and co…」  
  判断：**错误**。第一阶段真正产生示范效应的电动车设计，不是以简单和便利为特征的代步车，而是昂贵、强调性能和续航的 Roadster，以及随后的 Model S 豪华轿车。日产聆风更接近简单家用车，但并不是设定后续竞赛路线的“获胜设计”。  
  来源：<https://www.technologyreview.com/2008/08/19/219217/tesla-roadster-2/>；<https://ir.tesla.com/press-release/tesla-motors-delivers-worlds-first-premium-electric-sedan>；<https://chargedevs.com/newswire/epa-certifies-a-range-of-265-miles-for-tesla-model-s-deliveries-begin/>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/christensen-innovators-dilemma-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/christensen-innovators-dilemma-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/christensen-innovators-dilemma-v5/audit/manual_review_2026-11-15.py`

## 说明

- 所用文件含 2000 年增订文字。引言表“WHERE DISRUPTIONS ARE HAPPENING TODAY”和第 8 章“本章写于 2000 年 2 月”的戴姆勒–克莱斯勒判断，按 2000 年起算。
- 前言、致谢、目录、书友指南和更新过的作者介绍不抽预测。
- “专家预测将总是错误”“先发优势很重要”这类全称或机制句，按窗口内既有正例也有反例记部分符合，不因个别成功或失败改写成正确或错误。
- 英文可解析密度：149 个保留块、约 51.6 万正文字符、34 条可解析预测，约每块 0.23 条、每 10 万字符约 6.6 条，落在英语书 0.2–0.35/块目标的下沿。

