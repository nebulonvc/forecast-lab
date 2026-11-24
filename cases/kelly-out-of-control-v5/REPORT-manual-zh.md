# 凯文·凯利（Kevin Kelly）《失控》（Out of Control: The New Biology of Machines, Social Systems, and the Economic World）：出版后预测人工核查

- 案例目录：`cases/kelly-out-of-control-v5/`
- 出版日期：**1994 年**（版权页 Copyright © 1994 by Kevin Kelly）。所用文本为作者公开的 Illustrated Edition（Photos Copyright © 2008 by Kevin Kelly；目录作 2009 年全本插图版），`reading-library/2026-11-15-未来判断书单/03-科技和AI/19-失控.pdf`，与 catalog 的 source_url 复核，PDF sha256 `1d3959a27ae2e07db8fb114cce9a74b67429d9e23384364df6570f4dab6a5885`。正文由 `pdftotext -enc UTF-8` 转为 TXT，sha256 `7d5e9c38b981d008b171e00cfb4e3690de577a9580e23c762b87ed9347897b71`。插图版主要增加照片，正文版权仍为 1994；观察窗口按 1994→2026-11-15 起算。全文文本未放入案例或打包。封面、目录、致谢与书目注释不计预测。书中写明的终点（soon / someday / 十年后 / 1995 / 1997 / 一百年后 / 两百年后 / 十亿年后 / 星系时间尺度等）分别适用。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

本稿按 METHOD.md 全文通读、复刻 DeepSeek 管线逐步完成（只把原 API 调用换成助手通读）。抽取：用仓库 prepare_book v5 把全文切成 405 块（3500 字符、600 字符上下文），助手逐块通读、按 DISCOVER_PROMPT_V5 写出模型本应返回的 JSON，再由仓库代码完成引文对齐、归属降级、去重和导入，得到 256 条可核验预测、49 条 unclear（约 0.63 条/块；本书是长篇技术未来著作，密度高于一般英语非虚构的 0.2–0.35，与同为预测书的威尔斯《预言》相近）。`claims.jsonl` 的 context 已清空。核验：按 METHOD.md §4 先写 scope，各做一次 support 与 counter 的 Exa 检索（只使用检索返回的 URL，不用 kk.org 书页作核验证据），原文存档于 data/sources（sha256），写入 data/evidence.jsonl（497 条），由助手阅读后按四分类规则评断，经 pipeline.py apply assess → check → report。趋势符合从严（规则 10）。本稿由助手逐条对照书中原文与存档证据人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 256 条，剔除非预测 0 条，计入 **256 条预测**，其中 **230 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 88 |
| 趋势符合 | 2 |
| 部分符合 | 127 |
| 错误 | 13 |
| 暂无法判断 | 26 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **38.3%**（88/230） |
| 加权胜率 | **66.5%** |
| 错误率 | **5.7%**（13/230） |
| 未定占比（暂无法判断/预测） | 10.2%（26/256） |

## 总体评价

凯利在 1994 年对网络化、分布式与生物隐喻的技术图景有不少命中：互联系统与蜂群式组织进入主流，电子货币与日常电子支付广泛出现，计算机动画与视觉特效成为电影常态，工业共生、人工生命研究、演化计算和连接照明等方向都在窗口内留下了可核验的痕迹。主要误判包括：人造世界很快就会完全自主并超出控制、分布式心智必将主导人工心智、解决人工昆虫后人工猿类很快跟上、1997 年微型蚁群式漫游车成为火星任务核心、创造财富的工艺将收缩到生物尺度、2004 年最令人惊叹的消费产品来自人工生命会议、银行借记式无现金方案会夭折、希利斯关于 1995 年并行机器处理量超过串行机器的赌注、已部署且无人能理解的演化航空/电话软件，以及 1997 年后不再有人手绘米老鼠。明确写在更远期（十亿年、星系尺度、一百年/两百年、someday 的开放世界等）或检索证据对不上的条目记为暂无法判断，不强行判对错。趋势符合只保留两条（生物圈二号经验有朝一日用于火星/月球，以及机器与生物学的界限将难以分辨），其余未兑现的方向预测不降格记入趋势符合。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（88 条）

- **#1** 「Machines are becoming biological and the biological is becoming engineered.」  
  判断：**正确**。1994年以来合成生物学兴起：2010年合成细胞、基因组编辑与仿生“生长机器人”等公开记录表明，机器日益引入生物原理，生命也日益被工程化，两个方向都已发生。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC7560693/>；<https://www.science.org/doi/10.1126/science.1190719>
- **#4** 「We have reason to believe yet more can be synthesized and made into something new.」  
  判断：**正确**。合成基因组与合成细胞已被做成新的活体：2010年JCVI-syn1.0由化学合成基因组控制，后续合成染色体与设计蛋白工作继续扩展可合成的生命性状。  
  来源：<https://www.science.org/doi/10.1126/science.1190719>；<https://www.jcvi.org/media-center/synthetic-genomics-advances-and-promise>
- **#6** 「The overlap of the mechanical and the lifelike increases year by year.」  
  判断：**正确**。脑机接口、软体电子与神经形态等公开综述表明，机械装置与类生命系统的交叉在1994–2026年间持续扩大，与“一年比一年扩大”的方向一致。  
  来源：<https://journals.physiology.org/doi/full/10.1152/physrev.00027.2016>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC13319321/>
- **#7** 「Yet beyond semantics, two concrete trends are happening: (1) Human-made things are behaving more lifelike, and…」  
  判断：**正确**。人造系统日益表现自适应与类生命行为，同时CRISPR等基因组编辑使生命被工程化成为常规工具，书中所说的两条具体趋势都已发生。  
  来源：<https://www.tandfonline.com/doi/full/10.1080/14636778.2020.1730166>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC12661890/>
- **#11** 「The most unexpected things will brew in this bionic hivelike supermind.」  
  判断：**正确**。全球已由线路、无线与政治高度互联，社交媒体与网络运动中出现了大量事前难以预料的集体行为与文化涌现，与蜂巢式超级心智中酝酿出“最意想不到的事物”相符。  
  来源：<https://dl.acm.org/doi/pdf/10.1145/1940761.1940803>；<https://arxiv.org/html/2408.01257v2>
- **#13** 「when we construct autonomous robots, I bet we give up some of their potential adaptability in exchange for pre…」  
  判断：**正确**。自主机器人普遍保留人工共享控制、安全约束与接管机制，工程实践正是以牺牲部分潜在适应性来避免其完全脱离控制，与预测一致。  
  来源：<https://arxiv.org/abs/2112.00279>；<https://wisc-rt2.github.io/shared_control_autonomy_survey/survey_preprint.pdf>
- **#14** 「Most tasks will balance some control for some adaptability, and so the apparatus that best does the job will b…」  
  判断：**正确**。群体机器人与分布式系统研究普遍采用并比较集中、分散与混合架构，实践中最胜任的方案常常是兼顾控制与适应性的混合体，与“部分钟表、部分群体”相符。  
  来源：<https://arxiv.org/html/2408.06553v1>；<https://arxiv.org/abs/2403.07635>
- **#15** 「The network is the icon of the 21st century」  
  判断：**正确**。互联网与网络作为21世纪的核心象征已被文化与学术讨论广泛确认；即便气候或人工智能后来也成为时代议题，网络仍是本世纪前四分之一最显著的标志性象征。  
  来源：<http://www.casa.ucl.ac.uk/cupumecid_site/download/Coyne.pdf>；<https://www.fulcrum.org/downloads/n870zt56k?locale=en>
- **#16** 「And this logic will quickly mold the culture of humans living in a networked world.」  
  判断：**正确**。社交平台逻辑已深入日常生活、制度与职业惯例，网络社会理论也记录了网络逻辑迅速重塑人类文化，与“将迅速塑造”相符。  
  来源：<https://www.cogitatiopress.com/mediaandcommunication/article/download/70/60>；<https://www.dhi.ac.uk/san/waysofbeing/data/citizenship-robson-castells-2000c.pdf>
- **#17** 「What we get from heavy-duty communication networks, and the networks of parallel computing, and the networks o…」  
  判断：**正确**。通信网、计算网与分布式器具的发展催生了被明确命名和讨论的“网络文化”，该文化形态已经出现。  
  来源：<https://varnelis.net/wp-content/uploads/2026/08/varnelis-meaning-of-network-culture-2008.pdf>；<https://monoskop.org/images/8/89/Giessmann_Sebastian_The_Connectivity_of_Things_Network_Cultures_since_1832_2024.pdf>
- **#18** 「pervasively networked computers will be the main shaper of humans in the future.」  
  判断：**正确**。手持与随时在线的计算已成为日常常态，信息与通信技术被广泛记录为重塑自我、交往与世界体验的主要技术力量，与“无处不在的网络计算机将成为塑造人类的主要力量”相符。  
  来源：<https://sodacity.net/system/files/Sherry-Turkle_The-Tethered-Self.pdf>；<https://issc.al.uw.edu.pl/wp-content/uploads/sites/2/2022/05/Luciano-Floridi-The-Fourth-Revolution_-How-the-infosphere-is-reshaping-human-reality-Oxford-University-Press-2014.pdf>
- **#19** 「As we wire ourselves up into a hivish network, many things will emerge that we, as mere neurons in the network…」  
  判断：**正确**。算法选择、平台机制与生成式网络内容带来了大量用户作为节点难以预期、难以理解或难以控制的涌现结果，与接入蜂巢网络后的判断相符。  
  来源：<https://www.mediachange.ch/media/pdf/publications/Just_Latzer2016_Governance_by_Algorithms_Reality_Construction.pdf>；<https://academic.oup.com/nsr/article/12/1/nwae323/7762200>
- **#23** 「In the human management of distributed control, hierarchies of a certain type will proliferate rather than dim…」  
  判断：**正确**。在分布式控制的管理实践中，云、平台与大规模网络普遍发展出可扩展的嵌套管理层级，层级并未因分布式而消失，反而随规模增殖。  
  来源：<https://doi.org/10.1109/cnsm.2013.6727803>；<https://doi.org/10.1504/ijcnds.2024.135092>
- **#27** 「Their numbers will outnumber us, as do insects.」  
  判断：**正确**。若把这些“人造生物”理解为与人共生的联网装置，则已超过人类数量：公开统计显示2024–2025年全球联网物联网设备约18.5–21.1亿台，高于同期约80亿人口。  
  来源：<https://iot-analytics.com/number-connected-iot-devices/>；<https://webiano.digital/the-internet-now-has-more-things-than-people-and-that-changes-the-digital-economy/>
- **#28** 「his vision of robots is less that they will be R2D2s serving us beers, than that they will be an ecology of un…」  
  判断：**正确**。实际部署仍以仓库、工厂、物流与后台自动化等无名、视线之外的机器生态为主，端啤酒式的显眼人形服务机器人虽有示范，仍非主流形态。  
  来源：<https://www.cio.com/article/4113204/the-self-creating-supernet.html>；<https://www.bain.com/insights/humanoid-robots-from-demos-to-deployment-technology-report-2025/>
- **#33** 「A democracy of autonomous, evolving machines will be similarly feared as Anarchy Plus.」  
  判断：**正确**。对自主与日益强大的人工智能/机器的公众恐惧与风险讨论已被多次调查和媒体研究所记录，与“将被恐惧为无政府状态加强版”的方向一致。  
  来源：<https://www.existentialriskobservatory.org/papers_and_reports/Trends%20in%20Public%20Attitude%20Towards%20Existential%20Risk%20And%20Artificial%20Intelligence.pdf>；<https://link.springer.com/article/10.1007/s43681-024-00600-9>
- **#34** 「I think humans will accumulate artificial and mechanical abilities, while machines will accumulate biological …」  
  判断：**正确**。假肢、可穿戴与增强技术使人类积累了更多人造/机械能力，机器则通过生物启发与神经网络积累了更强的类生物智能，两个方向都已发生。  
  来源：<https://www.techtarget.com/news/Human-augmentation-is-closer-than-we-think-experts-say/833969/>；<https://doi.org/10.1177/29776481261428353>
- **#36** 「Who will not feel a bit of holy awe on the day when machines talk back to us?」  
  判断：**正确**。从早期聊天机器人到语音助手再到生成式对话系统，机器已经能够反过来与人交谈，该日已经到来。  
  来源：<https://computerhistory.org/stories/chatbots-decoded/>；<https://www.theverge.com/24054603/chatbot-chatgpt-eliza-history-ai-assistants-video>
- **#39** 「Unripe machinery let out before it is fully grown and fully integrated with diversity will be a common complai…」  
  判断：**正确**。过早发布未成熟软件已成为常见抱怨，同时“尽早出货”也成为行业口号，与“不成熟机器提前投放将成为常见抱怨”完全相符。  
  来源：<https://theagilepirate.net/archives/1950>；<https://blog.codinghorror.com/version-1-sucks-but-ship-it-anyway/>
- **#40** 「In a 21st-century society wired into instantaneous networks, marketing is the mirror; the collective consumer …」  
  判断：**正确**。21世纪社会已接入即时网络，实时与社交媒体营销形成企业传播与消费者反应的反馈环，营销如镜、集体消费者如变色龙的机制已经被营销研究记录。  
  来源：<https://doi.org/10.1108/03090560810852940>；<https://journals.sagepub.com/doi/10.1509/jm.15.0033>
- **#41** 「Pervasive digitalization of the approaching future promises clearer, faster, and more omnipresent mirrors.」  
  判断：**正确**。自我追踪、移动数字技术与“数字镜子”实践已迅速普及，数字化带来了更清晰、更快、更无处不在的自我反馈与映照。  
  来源：<https://repositum.tuwien.at/bitstream/20.500.12708/16211/2/Dorfmann%20Max%20-%202020%20-%20The%20Self%20in%20the%20digital%20mirror%20Meanings%20Myths%20and...pdf>；<https://researchonline.lse.ac.uk/id/eprint/137898/>
- **#44** 「The more mutually responsive we construct our economic and material world, the more coevolutionary games we’ll…」  
  判断：**正确**。平台与双边市场把经济世界建造得更加相互响应，平台生态系统中的共同进化动态已被广泛记录，与“会看到越多共同进化博弈”相符。  
  来源：<https://www.mdpi.com/2071-1050/11/3/726>；<https://arxiv.org/html/2502.01792>
- **#47** 「Complexity poured into the artificial medium of machines and silicon chips will only be in further flux.」  
  判断：**正确**。即便摩尔定律放缓，芯片、算法与软件栈的复杂性仍在持续变动，注入硅介质的复杂性确实“只会处在进一步的流变之中”。  
  来源：<https://www.science.org/doi/full/10.1126/science.aam9744>；<https://www.technologyreview.com/2026/10/19/1145904/tr-explains-how-far-can-we-push-computing/>
- **#50** 「They’ll be with us for as long as we have computers.」  
  判断：**正确**。恶意软件统计显示每天仍出现大量新样本，老蠕虫也持续传播，计算机病毒并未被根除，与“只要还有计算机就会伴随我们”相符。  
  来源：<https://av-test.org/en/statistics/malware/>；<https://www.bbc.com/news/technology-44564709>
- **#58** 「The impact of information domestication will be felt initially in industry and business, just as energy and ma…」  
  判断：**正确**。计算机与信息化首先在工商业成为核心工具，随后才大规模渗入家庭与个人生活，时间顺序与预测相符。  
  来源：<https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/sixty-years-of-innovation-key-moments-in-business-technology>；<https://kraut.hciresearch.info/wp-content/uploads/domesticating-computers-21.pdf>
- **#78** 「In the ecological office stocked with swarmish things, the room will know where I am.」  
  判断：**正确**。智能办公室已部署实时占用与室内定位，房间或工位系统能够知道空间是否被使用以及人在哪里，该能力已经实现。  
  来源：<https://www.sonynetworkcom.com/nimway/smart-office>；<https://crackedlabs.org/en/data-work/publications/indoortracking>
- **#80** 「In the future, the smartness of computers will surround you.」  
  判断：**正确**。环境智能、智能音箱与遍在计算使计算机的智能环绕在人周围，该未来已经在很大程度上实现。  
  来源：<https://www.amazon.science/blog/ambient-intelligence-will-accelerate-advancements-in-general-ai>；<https://dl.acm.org/doi/10.1145/3447242>
- **#81** 「Machines too will play on a coevolutionary stage.」  
  判断：**正确**。对抗学习、竞争性共同进化算法与军备竞赛式共同进化已被用于机器/算法相互适应，机器已出现在共同进化舞台上。  
  来源：<https://doi.org/10.1145/3449726.3461419>；<https://www.cs.utexas.edu/~ai-lab/pubs/stanley.jair04.pdf>
- **#83** 「Rooms and buildings will vary in their electronic ecology, as will appliances within」  
  判断：**正确**。智能家居被用户挪用、整合进个性化家庭环境，房间与建筑的电子生态以及其中的器具配置已呈现出明显差异。  
  来源：<https://dl.acm.org/doi/full/10.1145/3544548.3581497>；<https://iihm.imag.fr/publs/2015/SmartHome-Crowley-Coutaz-Ami2015.pdf>
- **#86** 「Machines will never go completely on their own way, but they will become more aware of other machines.」  
  判断：**正确**。工业物联网与机器对机器通信的标准与互操作已使机器更多地感知、连接其他机器；至2026年，机器整体上仍需设计与管控，并未完全自行其是。  
  来源：<https://dl.acm.org/doi/10.1145/3485130>；<https://www.jicce.org/journal/view.html?pn=myread&uid=291&vmd=Full>
- **#89** 「More net-driven “flex-factories” will be able to handle a more erratic quality of resources by running adaptab…」  
  判断：**正确**。可重构制造、柔性制造与工业4.0使更多网络驱动的柔性工厂能够以可适应设备或小批量多品种应对变化，该方向已经发生。  
  来源：<https://blogs.sw.siemens.com/wp-content/uploads/sites/3/2025/05/Industrie-4.0-Breakthrough-Flexible-Manufacturing-Becomes-Reality.pdf>；<https://doi.org/10.1007/s11465-018-0483-0>
- **#101** 「the fast-approaching data superhighway that would connect television, telephones, and the Sixpack family.」  
  判断：**正确**。宽带把语音、视频与数据送入普通家庭，电视、电话与家庭被接入同一数据网络，信息高速公路的核心结果已经实现。  
  来源：<https://www.pewresearch.org/internet/2002/06/23/main-report-the-broadband-difference/>；<https://www.pewresearch.org/short-reads/2014/05/19/32-years-ago-experts-foresaw-much-of-todays-digital-world/>
- **#103** 「Networking at that scale would truly revolutionize almost every business.」  
  判断：**正确**。互联网在商业中的采用极为广泛，电子商务与信息化已实质改变几乎各行各业，公开普查与政府报告均指出其影响将触及各类企业。  
  来源：<https://www.mckinsey.com/~/media/McKinsey/Industries/Technology%20Media%20and%20Telecommunications/High%20Tech/Our%20Insights/Internet%20matters/MGI_internet_matters_exec_summary.pdf>；<http://papers.nber.org/papers/w9287.pdf>
- **#104** 「the feverish cultural brew that will burst as “the Street” takes hold of this web and subverts it to its own u…」  
  判断：**正确**。草根用户把网络转用于自身目的后，混剪、用户生成内容和mashup等文化混杂大规模爆发，该方向已经发生。  
  来源：<https://eprints.qut.edu.au/39302/1/c39302.pdf>；<https://www.diva-portal.org/smash/get/diva2:221434/FULLTEXT01.pdf>
- **#105** 「Networking will also inform the maintenance of products.」  
  判断：**正确**。远程监控、故障预警与预测性维护已成为联网产品的常见维护方式，联网已经塑造了产品维护。  
  来源：<https://en.dmgmori.com/products/digitization/connectivity>；<https://www.hms-networks.com/about-hms/case-studies/case-study/heishin-boosts-pump-reliability-and-predictive-maintenance-with-ewon-flexy>
- **#107** 「It will be hard at times to tell who is working for whom.」  
  判断：**正确**。平台零工、算法调度和被有意隐藏的“幽灵劳动”使雇佣与服务关系经常不透明，有时确实很难分清谁在为谁工作。  
  来源：<https://journals.sagepub.com/doi/10.1177/1461444820977209>；<https://sites.rutgers.edu/critical-ai/wp-content/uploads/sites/586/2022/01/Introduction_Ghost-Work.pdf>
- **#108** 「companies will not break down into a」  
  判断：**正确**。企业边界虽因外包和网络协作而变化，但公司作为组织并未解体成各自为政的个人网络，公司形态仍然普遍存在。  
  来源：<https://link.springer.com/chapter/10.1007/978-3-658-40054-5_6?code=065df8f3-2697-4973-b40e-b38c51be4978&error=cookies_not_supported>；<https://doi.org/10.1080/10919392.1997.9681069>
- **#110** 「The shift from products to service is inevitable because automation keeps lowering the price of physical repro…」  
  判断：**正确**。服务化与订阅模式已成为公开记载的经济大趋势，从产品转向服务在多个行业已经发生，物理复制成本下降是其背景之一。  
  来源：<https://doi.org/10.1080/08956308.2024.2330267>；<https://www.econstor.eu/bitstream/10419/305862/1/id495.pdf>
- **#113** 「it is certain that more and more of what they make depends on more complex software」  
  判断：**正确**。嵌入式系统与软件密集型产品的公开记录表明，企业制造的产品越来越依赖更复杂的软件，源代码规模显著上升。  
  来源：<https://doi.org/10.1109/mc.2007.36>；<https://tech-clarity.com/documents/Tech-Clarity_Perspective_Product_Software.pdf>
- **#116** 「Heads of lettuce, as well as airline tickets, have shifting prices displayed on an LED on the grocery shelf.」  
  判断：**正确**。电子货架标签已在多国超市部署，食品价格可在货架数字标签上调整，出现类似机票的动态定价实践。  
  来源：<https://www.wsj.com/business/retail/surge-grocery-prices-electronic-shelf-labels-a3d47701>；<https://www.supermarketnews.com/grocery-technology/is-dynamic-pricing-feasible-within-supermarkets->
- **#118** 「Products in a network culture become updatable franchises that coevolve in continuous improvement with custome…」  
  判断：**正确**。在网络文化中，软件即服务和持续更新已使产品成为可更新、随使用共同进化的服务特许权，这一产品形态已经成为主流。  
  来源：<https://dlnext.acm.org/doi/10.1109/CloudCom.2014.131>；<https://manytricks.com/blog/?p=5465>
- **#122** 「Finding the right customer in the chaotic web of infinite communications will be a new game.」  
  判断：**正确**。在海量数字通信中获取和定位合适顾客，已成为在线获客、广告与增长实验的新游戏，该方向已经发生。  
  来源：<https://www.mckinsey.com/capabilities/growth-marketing-and-sales/our-insights/new-insights-for-new-growth-what-it-takes-to-understand-your-customers-today>；<https://www.thinkwithgoogle.com/_qs/documents/6680/TWG_APAC_Google_Experiments_IGG.pdf>
- **#128** 「an escalating arms race with a digital IRS might evolve. For every new avenue the digital underground invents …」  
  判断：**正确**。加密资产等数字地下交易与税务、执法部门的追踪形成持续对峙，税务部门增强监管、透明规则跟进，军备竞赛式互动已经出现。  
  来源：<https://scholarship.law.slu.edu/lj/vol64/iss2/4>；<https://doi.org/10.1787/b33c9aa1-en>
- **#131** 「also definitely require the kind of tools the cypherpunks are playing with.」  
  判断：**正确**。密码朋克推动的数字密码、隐私工具已被用于网络政治、抗议与对抗监管的实践，网络经济中的政治确实需要这类工具。  
  来源：<https://www.tandfonline.com/doi/full/10.1080/24701475.2021.1935547>；<https://groups.csail.mit.edu/mac/classes/6.805/articles/crypto/cypherpunks/may-virtual-comm.html>
- **#134** 「this will not stop hackers from siphoning off free information.」  
  判断：**正确**。付费墙与内容保护并不能阻止信息被泄露或被非付费者获取，黑客与社区抽走免费信息的现象持续存在。  
  来源：<https://ijoc.org/index.php/ijoc/article/download/23998/4983/90741>；<https://www.holovaty.com/writing/225/>
- **#140** 「Digital cash could fail in real life, but it is almost certain to flourish in the nascent network culture.」  
  判断：**正确**。早期电子现金在现实与网上都曾失败，但数字支付与加密货币后来在网络文化中繁荣，作者关于其几乎肯定会在网络文化中兴盛的判断成立。  
  来源：<https://bura.brunel.ac.uk/bitstream/2438/15393/4/Fulltext.pdf>；<https://archive.nytimes.com/www.nytimes.com/library/tech/98/11/cyber/articles/28cash.html>
- **#141** 「Bar-code lasers can identify moving cars on the road, and drivers will accept purchasing vouchers.」  
  判断：**正确**。电子收费、车载识别与通行凭证已被司机广泛接受，行驶中的车辆可被自动识别并完成缴费，该方向已经实现。  
  来源：<https://rno-its.piarc.org/en/user-services-electronic-payment-payment-applications/toll-collection>；<https://telematika.com/en/directions/toll_systems/>
- **#142** 「It’s a pretty sound bet that the Internet will be the first place that e-money will infiltrate deeply.」  
  判断：**正确**。电子货币与网络支付最先在互联网商务中深入渗透，互联网支付中介和电子商务支付的出现早于全面线下数字化，该赌注成立。  
  来源：<https://doi.org/10.1145/948005.948053>；<https://www.chicagofed.org/publications/chicago-fed-letter/2001/march-163a>
- **#147** 「It opens the floodgates of commerce onto the Net.」  
  判断：**正确**。电子支付与互联网结合后，电子商务迅速扩大，网络上的商业闸门确实被打开。  
  来源：<https://www.chicagofed.org/publications/chicago-fed-letter/2001/march-163a>；<https://www.bis.org/speeches/20010214-e-commerce-lessons-learned-date.pdf>
- **#149** 「All manner of clever financial instruments will surface once the masses can drink from the same river of elect…」  
  判断：**正确**。大众获得与专业人士类似的电子货币和数字金融通道后，金融科技、零售投资和去中心化金融等新工具大量涌现。  
  来源：<https://www.investopedia.com/important-financial-innovations-8700210>；<https://www.weforum.org/stories/2022/09/decentralized-finance-a-leapfrog-technology-for-the-unbanked/>
- **#150** 「We are headed toward programmed capitalism.」  
  判断：**正确**。算法交易、智能合约与可编程货币表明，资本主义的支付与合约正在被程序化，‘走向可编程的资本主义’这一方向已经发生。  
  来源：<https://cepr.org/publications/books-and-reports/can-blockchain-decentralise-money-contracts-and-finance>；<https://doi.org/10.32855/fcapital.201701.012>
- **#152** 「Paracurrencies will flourish as the network culture flourishes.」  
  判断：**正确**。随着网络文化繁荣，加密货币、代币和各类补充货币等平行货币显著兴起，该方向已经发生。  
  来源：<https://nulan.mdp.edu.ar/id/eprint/3943/1/orzi-etal-2021.pdf>；<https://www.tandfonline.com/doi/full/10.1080/17530350.2025.2585119>
- **#153** 「An electronic matrix is destined to be an outback of hardy underwire economies.」  
  判断：**正确**。暗网市场等地下经济在电子基质上反复重建并持续存在，电子网络确实成为顽强地下经济的活动空间。  
  来源：<https://arxiv.org/abs/1911.09536>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC8452499/>
- **#154** 「once established interstitially in the Net’s links, e-money is probably ineradicable.」  
  判断：**正确**。比特币等网络电子货币一旦立足，尽管多次遭到打击，仍难以被根除，‘很可能无法根除’这一判断成立。  
  来源：<https://escholarship.org/uc/item/7w616491>；<https://www.theguardian.com/technology/2000/aug/17/internetnews.efinance>
- **#156** 「that will have to wait until encryption technology enters the mainstream—as it certainly will.」  
  判断：**正确**。加密技术已进入主流，HTTPS等用途在等待普及后大规模落地，‘它肯定会进入主流’已经实现。  
  来源：<https://en.wikipedia.org/wiki/HTTPS>；<https://timelines.issarice.com/wiki/Timeline_of_HTTPS_adoption>
- **#163** 「the ones that survive will grow in complexity and value.」  
  判断：**正确**。存活下来的虚拟世界在用户规模、复杂性和商业价值上显著增长，并进入主流社会，该方向已经发生。  
  来源：<https://scholar.lib.vt.edu/ejournals/JOTS/v40/v40n2/downey.html>；<https://www.sciencedirect.com/science/article/abs/pii/S016792360900061X>
- **#165** 「allow future cadets to take on the Republican Guard by unleashing what-ifs into the simulation.」  
  判断：**正确**。军方随后确实把模拟训练推进到让学员在虚拟战场中通过多种假设情景作战，SIMNET及其后继系统已用于此类训练。  
  来源：<https://apps.dtic.mil/dtic/tr/fulltext/u2/a319483.pdf>；<https://www.army.mil/article/223038/oklahoma_guard_uses_virtual_battle_space_at_western_strike>
- **#168** 「The dawn of commercial profit-making MUDs in not far away.」  
  判断：**正确**。1990年代中后期Meridian 59、Ultima Online等商业多人在线游戏出现，商业营利性MUD/MMO的黎明确实不远。  
  来源：<https://www.cgw.com/Publications/CGW/2002/Volume-25-Issue-3-March-2002-/Part-1-Gaming-for-the-Masses.aspx>；<https://www.zenofdesign.com/wp-content/uploads/2014/12/Meridian-59.pdf>
- **#170** 「The other thing the man-things should know is that their models won’t be perfect, either. Nor will these imper…」  
  判断：**正确**。人工模型并不完美，也不处于神一般的控制之下，这一判断已被当前人工智能与行为模拟的公开讨论所证实。  
  来源：<https://www.pnas.org/doi/10.1073/pnas.2501660122>；<https://cproth.com/assets/limits-of-behavioral-simulation-with-ai.pdf>
- **#171** 「The next advance in evolutionism is to be able to begin with a human-designed pattern and then arbitrarily bre…」  
  判断：**正确**。交互式进化设计与遗传算法已能从人类给出的图案或种子出发，再继续繁殖演化，该‘下一步’已经出现。  
  来源：<https://dspace.lboro.ac.uk/2134/14064>；<https://figshare.com/articles/online_resource/User-led_development_of_an_Interactive_Evolutionary_Design_system/9340595>
- **#172** 「In the future, lawyers may demand a record of the evolutionary path an artist followed to arrive at an evolved…」  
  判断：**正确**。在人工智能生成作品的著作权争议中，已有司法实践和律师建议要求保留创作过程与路径记录，以证明作品原创、而非抄袭或仅归属于程序。  
  来源：<https://techinsights.linklaters.com/post/102lo55/china-documentation-of-creative-processes-is-crucial-to-claim-copyright-in-ai-ge>；<https://www.nortonrosefulbright.com/en/knowledge/publications/9a6884d0/keeping-records-to-respond-to-an-ai-authorship-challenge-lessons-from-suryast>
- **#174** 「the complexity and cost of extracting the information will surge as the complexity of the artificial worlds su…」  
  判断：**正确**。人工/数字世界变复杂后，取数与数据成本确实上升；但数字化信息的提取与分发总体上仍比未连线的有机世界更容易。  
  来源：<https://arxiv.org/abs/2206.10326>；<https://doi.org/10.3386/w23684>
- **#179** 「One-hundred-million-line programs are not far away.」  
  判断：**正确**。大型代码库后来达到并超过一亿行规模，谷歌单一仓库和大型商业软件的公开记录表明，一亿行级程序‘已经不远’这一判断成立。  
  来源：<https://cacm.acm.org/research/why-google-stores-billions-of-lines-of-code-in-a-single-repository/>；<https://news.ycombinator.com/item?id=8257327>
- **#180** 「When computer programs swell to billions of lines of code, just keeping them up and “alive” will become a majo…」  
  判断：**正确**。已出现数十亿行量级的代码库，软件维护、迁移和‘让系统继续活着’确实成为一项主要工作，条件已满足且后果成立。  
  来源：<https://cacm.acm.org/research/why-google-stores-billions-of-lines-of-code-in-a-single-repository/>；<https://commandline.microsoft.com/agentic-software-engineering-large-scale-code-migration-language-modernization-spec-driven-development/>
- **#181** 「people’s lives will depend on billion-line programs to let them go down for even an instant.」  
  判断：**正确**。社会生活已依赖超大规模软件与云服务，关键系统短暂停摆就会造成全球通信和交通中断，连续性要求已经成为现实。  
  来源：<https://theconversation.com/the-microsoft-outage-is-an-urgent-wake-up-call-for-greater-digital-resilience-296610>；<https://techblog.comsoc.org/2026/11/13/critical-network-outages-why-isnt-redundancy-working-part-i/>
- **#195** 「Mickey, now 66 years old, will 270 soon have to face the digital era.」  
  判断：**正确**。米老鼠很快进入数字制作流程：迪士尼在1990年代初已使用CAPS等数字系统，随后全面进入数字时代，该判断成立。  
  来源：<https://en.wikipedia.org/wiki/Computer_Animation_Production_System>；<https://en.wikipedia.org/wiki/The_Prince_and_the_Pauper_(1990_film)>
- **#198** 「digital characters will be used for dangerous stunts, or worked into composite scenes—but only in long shots, …」  
  判断：**正确**。早期数字角色确实先被用于危险特技、合成大场景和远景人群，例如《泰坦尼克号》中的数字乘客与替身，而不是首先用于特写主演。  
  来源：<http://www.vfxhq.com/1997/titanic-review3.html>；<https://doi.org/10.1145/237170.237293>
- **#207** 「Best of all, he’ll never die, never age.」  
  判断：**正确**。作为角色和品牌，米老鼠被维持为不衰老、不死亡的永恒形象，这一核心结果已经实现并持续。  
  来源：<https://brandequity.economictimes.indiatimes.com/news/marketing/mickey-mouse-will-soon-be-100-why-has-he-not-aged/128958405>；<https://www.psychologytoday.com/us/blog/common-sense-science/202601/what-mickey-mouse-reveals-about-being-human>
- **#210** 「a creation with a mind of its own—a thing we shall see more of.」  
  判断：**正确**。自主或半自主的人工智能造物与有影响力的人类创造者之间的关系已经明显增多，该方向已经发生。  
  来源：<https://www.rightclicksave.com/article/agents-of-eden-gene-kogan-and-xander-steenbrugge-interview-ai-art>；<https://art-recognition.com/magazine/the-great-network-of-relationships-mario-klingemann-botto-and-the-shape-of-machine-intelligence/>
- **#212** 「But the pilot will manage, or shepherd, the computer’s behavior. And the two—machine and human—will be in a co…」  
  判断：**正确**。现代航空中计算机已成为副驾驶式自动化：许多控制超出飞行员直接机械触及，飞行员负责管理或放牧自动化行为，飞机以人机共控方式飞行。  
  来源：<https://arxiv.org/abs/1909.07834>；<https://ntrs.nasa.gov/api/citations/20250002888/downloads/NASA-TM-20250002888.pdf>
- **#215** 「The evolving equations of Sims and Koza are the first step toward a self-reprogramming machine.」  
  判断：**正确**。西姆斯与科扎的遗传规划与演化方程，被后续文献视为通向程序自动生成乃至自我改写机器的早期步骤，作为“第一步”的判断成立。  
  来源：<https://phys.org/news/2018-03-evolutionary-self-programming-machines-years.html>；<https://gpbib.cs.ucl.ac.uk/gp-html/Sims_1994_ieds.html>
- **#216** 「Other workers will engineer a result after months of evolution.」  
  判断：**正确**。将一段时间的进化或实验室进化与随后的工程/设计方法相结合，已成为公开记载的研究与开发做法。  
  来源：<https://phys.org/news/2026-07-combining-ai-protein-laboratory-evolution.html>；<https://doi.org/10.64898/2026.01.16.699985>
- **#221** 「Artificial evolution will probably require a certain amount of artificial learning and intelligence to make it…」  
  判断：**正确**。文献与当前实践表明，若要在人类时间尺度上推进人工进化，通常需要结合学习与智能，该判断成立。  
  来源：<http://www.mli.gmu.edu/papers/96-2000/00-13.pdf>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC13123844/>
- **#223** 「evolution has been, and will keep on, exploring the space of possible evolutions.」  
  判断：**正确**。进化空间的探索是进化生物学的既有事实，公开研究也将其作为将继续进行的过程，该方向性判断成立。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC5665810/>；<https://royalsocietypublishing.org/doi/10.1098/rstb.2009.0154>
- **#227** 「artificial evolution will run slightly differently from natural evolution as long as it is embedded on a diffe…」  
  判断：**正确**。数字等不同基质上的人工进化与自然进化在机制和表现上确有差异，条件已满足，判断成立。  
  来源：<https://www.frontiersin.org/journals/ecology-and-evolution/articles/10.3389/fevo.2021.750779/full>；<https://www.nature.com/articles/s41598-023-50683-3>
- **#230** 「Artificial evolution will not be able to make everything.」  
  判断：**正确**。定向进化和人工进化文献明确指出该方法不能保证成功，也无法制造出一切事物，该限制性判断成立。  
  来源：<https://fondsites.com/synthetic-biology/guidebooks/directed-evolution/>；<https://arxiv.org/html/2611.07048>
- **#233** 「Once life settles in an environment (hot springs, alpine rock, robots) it will tenaciously maintain some prese…」  
  判断：**正确**。生命一旦在极端环境中定居，就会顽强维持存在，极端环境生物学为此提供了充分证据。  
  来源：<https://www.nature.com/articles/35059215>；<https://www.quantamagazine.org/the-organisms-that-make-earths-harshest-places-home-20260720/>
- **#235** 「As we humans introduce genetic engineering and self-programming robots, the makeup of evolution on Earth will …」  
  判断：**正确**。基因工程已经改变地球上的进化构成，可进化机器人也在进入讨论与实验，进化的组成正在继续演化。  
  来源：<https://www.bbc.com/future/article/20220125-how-humans-are-changing-evolution>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC8603346/>
- **#239** 「While long-range predictions will remain essentially unpredictable, short range predictions for complex system…」  
  判断：**正确**。复杂系统研究支持长期预测本质上困难，而短期预测既可能也必要，该判断与公开文献一致。  
  来源：<https://arxiv.org/html/2510.16312v1>；<https://www.quantamagazine.org/machine-learnings-amazing-ability-to-predict-chaos-20180418/>
- **#242** 「In another fifty years, computerized induction, algorithmic chartism, and pocket predictionism will be respect…」  
  判断：**正确**。机器学习、算法预测和预测专业活动在约2044年的到期点之前就已成为体面（尽管仍有争议）的人类事业。  
  来源：<https://artificialcommunication.mitpress.mit.edu/pub/m8xpxiru/download/pdf>；<https://www.sciencedirect.com/science/article/abs/pii/S0016328720300975>
- **#243** 「Forecasting stock markets will remain an oddball case because, more than other systems, stock markets are buil…」  
  判断：**正确**。股市仍然高度建立在预期之上，其可预测性仍被视为特例，公开金融研究持续强调预期在回报中的特殊作用。  
  来源：<https://doi.org/10.1093/rfs/hht082>；<https://arxiv.org/html/2408.01772>
- **#245** 「My bet is that artificial intelligence, when it comes, will be intelligent but not very humanlike.」  
  判断：**正确**。当当代人工智能到来时，它表现出智能，但公开研究强调其并不以人类方式思维，作者这一赌注大体成立。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC11416727/>；<https://theconversation.com/why-ai-cannot-think-like-humans-do-293188>
- **#246** 「It will be one of many nonhuman methods of thought that will probably fill the library of thinking space. This…」  
  判断：**正确**。深度学习等非人类认知方法已被使用，并被描述为黑箱或超出人类表征方式，我们仍在使用它们，该判断成立。  
  来源：<https://journals.sagepub.com/doi/full/10.1177/0263276420966386>；<https://link.springer.com/article/10.1007/s42803-023-00075-w>
- **#247** 「Nonhuman cognitive methods will provide us wonderful results beyond and out of our」  
  判断：**正确**。AlphaFold等非人类认知方法已经提供超出既有人类理解路径的重大结果，该判断成立。  
  来源：<https://deepmind.google/blog/alphafold-a-solution-to-a-50-year-old-grand-challenge-in-biology/>；<https://doi.org/10.31219/osf.io/j7dqb_v1>
- **#249** 「organic life—both wild and domesticated—will continue to be the prime infrastructure of human experience on th…」  
  判断：**正确**。尽管世界日益技术化，有机生命无论野生还是驯化，仍是人类全球经验的主要基础设施，该判断成立。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC13554003/>；<https://royalsocietypublishing.org/rstb/article/381/1942/20240426/479704/Life-on-New-Earth-biodiversity-change-and-humanity>
- **#250** 「Machines will become more biological in character.」  
  判断：**正确**。仿生机器人与具身人工智能表明，机器在特性上已变得更加生物化，该方向已经发生。  
  来源：<https://doi.org/10.1016/j.shpsa.2022.11.007>；<https://arxiv.org/html/2509.24521v1>
- **#255** 「Future bionic hybrids will be more confusing, more pervasive, and more powerful.」  
  判断：**正确**。生物杂交机器人、赛博格和合成生物系统确实变得更普遍、更强大，并带来更多概念上的困惑，该方向已经发生。  
  来源：<https://www.tandfonline.com/doi/full/10.1080/14636778.2021.2007064>；<https://advanced.onlinelibrary.wiley.com/doi/10.1002/adrr.202500196>
- **#256** 「As complex as things are today, everything will be more complex tomorrow.」  
  判断：**正确**。1994年以来，技术与社会系统的复杂性总体上升，“明天的一切都将更加复杂”作为方向性判断成立。  
  来源：<https://www.sciencedirect.com/science/article/abs/pii/S0040162501001718>；<https://arxiv.org/pdf/2605.05229>

### 趋势符合（2 条）

- **#70** 「I have no doubt that someday what is learned here will land on Mars or the Moon.」  
  判断：**趋势符合**。生物圈二号的经验已被用于空间生命保障与月火模拟研究（包括原地的SAM模拟舱），方向是把所学用于地外居住；但这些知识尚未实际登陆火星或月球。  
  来源：<https://spj.science.org/doi/10.34133/2021/8067539>；<https://biosphere2.org/research/research-initiatives/sam-mars-analog>
- **#72** 「Someday the difference between machines and biology will be hard to discern.」  
  判断：**趋势符合**。培养神经元计算、组织内嵌电子和赛博格组织等研究持续模糊机器与生物的边界，方向明确；但日常层面两者仍可分辨，“难以分辨”的终点尚未到来。  
  来源：<https://www.science.org/content/article/neurons-dish-are-newest-computing-machines>；<https://www.cell.com/trends/biotechnology/abstract/S0167-7799(26)00379-3>

### 部分符合（127 条）

- **#2** 「That is, the more mechanical we make our fabricated environment, the more biological it will eventually have t…」  
  判断：**部分符合**。复杂基础设施确出现自愈合、仿生与自适应设计，说明更机械化的系统开始借用生物原则；但常规机械/控制工程仍能使大多数人造环境运转，“最终必须更生物化才能运转”的必要性并未被证明。  
  来源：<https://doi.org/10.1080/09544828.2023.2266864>；<https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020EF001653>
- **#3** 「Our future is technological; but it will not be a world of gray steel. Rather our technological future is head…」  
  判断：**部分符合**。生物经济与生物制造已成为重要技术方向，技术未来并非只有“灰色钢铁”；但全球制造业增加值仍约16.8万亿美元、约占GDP的15%，机械工业仍是主干，“新生物文明”尚未成为技术世界的主导形态。  
  来源：<https://arsenale.bio/thoughts/biomanufacturingintheneo-industrialage>；<https://www.cargoson.com/en/blog/how-big-is-the-manufacturing-industry>
- **#5** 「But milk cows and carrots are more indicative of the kind of inventions humans will make in the future: produc…」  
  判断：**部分符合**。细胞农业、精准发酵等“培育而非制造”的产品已经出现并进入监管评估，方向存在；但截至截止日它们仍非人类发明的主流形态，大多数新产品仍是工厂制造。  
  来源：<https://www.nature.com/articles/s41587-026-03364-1>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC9996699/>
- **#22** 「Inside every solitary machine one day will be a swarm of non-mechanical things.」  
  判断：**部分符合**。许多计算机内部已运行进程集群、神经网络或多智能体，出现了“非机械之物构成的群体”；但远非“每一台单独的机器”内部都如此，大量装置仍是传统机电结构。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC11733729/>；<https://ar5iv.labs.arxiv.org/html/2305.17066>
- **#24** 「While authoritarian “top-down” hierarchies will retreat, no distributed system can survive long without nested…」  
  判断：**部分符合**。分布式系统确实常常依赖自下而上的嵌套协调才能稳定运行；但威权式自上而下层级并未简单退却，平台与政治领域仍有明显的集中控制，只说对了一半。  
  来源：<https://doi.org/10.1109/acsos-c58168.2023.00042>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC9860035/>
- **#25** 「When prodded, Brooks predicts a future filled with artificial creatures living with us in mutual dependence—a …」  
  判断：**部分符合**。家用清洁机器人、工业机器人与部分陪伴装置已进入日常生活，出现有限的相互依赖；但世界并未“充满”与人类形成新共生的人造生物，该前景只部分兑现。  
  来源：<https://spectrum.ieee.org/i-rodney-brooks-am-a-robot>；<https://arxiv.org/abs/2204.13331>
- **#26** 「Most of these creatures will be hidden from our senses, and taken for granted, and engineered with an insect a…」  
  判断：**部分符合**。大量传感与嵌入式装置确实隐藏在感官之外并被当作基础设施；但“大多按昆虫式方法设计”并不成立，主流仍是常规电子与软件工程，显眼的人形机器人也同时受到关注。  
  来源：<https://dl.acm.org/doi/full/10.1145/3640472>；<https://spectrum.ieee.org/robotics-experts-tesla-bot-optimus/experts-on-optimus>
- **#29** 「If Brooks is right, it probably never will. Instead it will grow a mind from a dumb body.」  
  判断：**部分符合**。条件是“若Brooks正确”。此后无身体的大语言模型取得了显著的“心智”能力，说明科学并非“永远无法凭空启动纯粹心智”；同时具身智能仍在发展，两条路径并存，原判断只对了一部分。  
  来源：<https://link.springer.com/article/10.1007/s11023-026-09804-w>；<https://arxiv.org/html/2601.17588>
- **#30** 「That is the next big step for machines. To learn over time, on their own. To not only adapt, but evolve.」  
  判断：**部分符合**。机器学习成为机器发展的下一个重大步骤，机器已能大规模学习与适应；但“而且进化”以及部署后持续自行学习仍不普遍，有文献指出许多已部署模型在运行中几乎不再学习。  
  来源：<https://dl.acm.org/doi/fullHtml/10.1145/3467477>；<https://arxiv.org/html/2603.15381>
- **#35** 「The greatest social consequence of neo-biological civilization will be the grudging acceptance by humans that …」  
  判断：**部分符合**。CRISPR出现后，对人体可被工程改造的讨论与有限接受确实成为重大社会议题；但公众态度仍然分裂，所谓“勉强接受自己是机器的随机祖先”并未成为新生物文明最突出、已被广泛接受的社会后果。  
  来源：<https://www.frontiersin.org/journals/genome-editing/articles/10.3389/fgeed.2023.1284547/full>；<https://www.nature.com/articles/s41431-024-01740-6>
- **#37** 「this patch holds the destiny of machines, for the future of machines is biology.」  
  判断：**部分符合**。仿生、生物计算与生物混合系统已成为机器研究的重要方向，但1994–2026年机器的主线仍是硅基数字技术，“机器的未来就是生物学”并未成为已实现的主导命运。  
  来源：<https://eprints.whiterose.ac.uk/id/eprint/107028/1/Prescott_et_al_SPIE_Biomimetics.final.pdf>；<https://www.techuk.org/insights/guest-insights/beyond-silicon>
- **#38** 「Creating extremely complex machines, such as robots and software programs of the future, will be like restorin…」  
  判断：**部分符合**。复杂软件与网络物理系统确有增量“培育”、模块化与持续演化的做法，类似生态恢复式组装；但极端复杂的机器人与软件仍大量采用一次性设计与交付，并非普遍“像恢复草原一样”被逐步长成。  
  来源：<https://web.eecs.utk.edu/~bmaclenn/papers/Gardening_cyber-physical_systems.pdf>；<https://doi.org/10.1109/iros.2001.976422>
- **#42** 「the lives of modern people are increasingly more codependent than ever.」  
  判断：**部分符合**。全球贸易、资本、信息与人员流动显示系统性相互依赖仍然很高；但文化与心理研究同时记录个人主义上升，因此“生活比以往任何时候都更加相互依赖”只在系统层面部分成立。  
  来源：<https://www.dhl.com/content/dam/dhl/global/delivered/documents/pdf/dhl-global-connectedness-report-2026-complete.pdf>；<https://journal.psych.ac.cn/adps/EN/10.3724/SP.J.1042.2018.02068>
- **#46** 「In this Era, openness wins, central control is lost, and stability is a state of perpetual almost-falling ensu…」  
  判断：**部分符合**。网络时代确实出现过自组织、开源与双赢合作；但开放并未稳定获胜，中央控制也未被丧失，平台与国家后来显著再中心化。  
  来源：<https://www.newamerica.org/insights/how-to-rebuild-the-internet/>；<https://direct.mit.edu/daed/article/145/1/65/27103/As-the-Pirates-Become-CEOs-The-Closing-of-the-Open>
- **#49** 「We are about to make machines as complex as grasshoppers and let them loose in the world. Once born, they won’…」  
  判断：**部分符合**。已有模仿蚱蜢跳跃等的微型机器人被投放使用，其中一些系统持续存在；但“与蚱蜢同样复杂”的机器并未被普遍造出，公开评论仍认为真正的人工昆虫尚未做成。  
  来源：<https://www.cbc.ca/news/science/tiny-robot-replicates-grasshopper-s-long-leaps-1.773135>；<https://www.lesswrong.com/posts/6hDvwJyrwLtxBLHWG/mechanisms-too-simple-for-humans-to-design>
- **#55** 「Indeed, the most meaningful discoveries in this coming century are bound to those that celebrate, explore, and…」  
  判断：**部分符合**。21世纪迄今，基因组、CRISPR、mRNA疫苗、合成生物学与人工智能等重大发现确实大量涉及技术与生命（或类生命系统）的统一；但气候、基本粒子与能源等同样被列为世纪级突破，故不能说最有意义的发现都属于这一类。  
  来源：<https://www.sciencefocus.com/future-technology/experts-pick-the-25-most-significant-breakthroughs-of-the-21st-century>；<https://www.nationalgeographic.com/science/article/top-discoveries-in-the-last-25-years>
- **#56** 「In the future, the essence that both living creatures and machines will have in common—that which will disting…」  
  判断：**部分符合**。自适应与自组织动力学已成为机器与人工生命的重要共同特征，但机器是否已以此作为与普通物质相区别的“共同本质”，仍有争论，且远未完成。  
  来源：<https://www.nature.com/articles/s44260-025-00031-5>；<https://doi.org/10.7551/mitpress/15519.003.0014>
- **#57** 「The central event of the twenty-first century will be the overthrow of information.”」  
  判断：**部分符合**。信息与数据平台确实成为21世纪的核心现象之一；但能源、地缘政治、气候变化与人工智能也被广泛视为世纪中心事件，所谓“中心事件将是对信息的推翻”只部分成立，世纪也尚未结束。  
  来源：<https://www.yanisvaroufakis.eu/2023/09/07/technofeudalism-has-just-arrived/>；<https://www.weforum.org/stories/2026/03/ai-energy-and-geopolitics-leadership/>
- **#59** 「Silicon chips, by the billions, bestowed with selves, will redesign themselves smaller and faster and rule the…」  
  判断：**部分符合**。芯片持续变得更小更快，电机驱动集成电路已被大规模用于控制电机；但“被赋予自我并自我重新设计”只在电子设计自动化/辅助设计的弱意义上部分出现，并非芯片自主重设计。  
  来源：<https://designsolutionsmag.co.uk/allegro-microsystems-achieves-major-milestone-of-three-billion-motor-driver-integrated-circuits-shipped/>；<https://www.machinedesign.com/automation-iiot/article/21828972/whats-next-in-chip-technology>
- **#60** 「And soon, the fibrous networks, by the zillions, bestowed with selves, will rethink the chips and rule all tha…」  
  判断：**部分符合**。光纤与互联网迅速成为重要基础设施，但“很快被赋予自我、重新思考芯片并统治我们允许它们统治的一切”并未在soon的时间窗口内实现，全光计算等更高自主网络也未按时到来。  
  来源：<https://www.wired.com/1997/09/newrules/>；<https://queue.acm.org/detail.cfm?id=1530830>
- **#61** 「In an age of smartness and superintelligence, the most intelligent control methods will appear as uncontrol me…」  
  判断：**部分符合**。自适应、看似“不加控制”的智能控制方法确已出现；但在智能系统治理中，强化集中控制的呼声与实践同样显著，不能说最智能的控制方法已经表现为不加控制。  
  来源：<https://www.mdpi.com/2218-6581/9/3/64>；<https://www.stimson.org/2026/we-cant-let-the-mythos-moment-consolidate-ai-power/>
- **#62** 「on their own, to evolve in their own direction, and grow without human oversight is the next great advance in …」  
  判断：**部分符合**。机器自行学习已成为重大进展，自我复制/演化机器人仍处实验阶段；“无人类监督下生长”尚未成为已实现的下一项重大技术跃迁。  
  来源：<https://www.newscientist.com/article/2309017-meet-the-robots-that-can-reproduce-learn-and-evolve-all-by-themselves/>；<https://www.scientificamerican.com/article/how-close-are-todays-ai-models-to-agi-and-to-self-improving-into/>
- **#63** 「What little time left in this century is rehearsal time for the chief psychological chore of the 21st century:…」  
  判断：**部分符合**。21世纪确有关于向自动系统让渡控制权的心理讨论；但监控资本主义与数据主义同时强化了控制而非“有尊严地放手”，该功课并未成为可观察的世纪主轴。  
  来源：<https://doi.org/10.1016/j.infoandorg.2025.100582>；<https://www.cambridge.org/core/books/being-human-in-the-digital-world/surveillance-and-human-flourishing/0AEF02D8335BBC1652AA3957A5F68A47>
- **#64** 「We can be certain that whatever artificial closed systems we fabricate will sooner or later be opened.」  
  判断：**部分符合**。生物圈二号等人工封闭系统后来被打开，软件与平台封闭系统也常被打开或突破；但也存在维持较长时间的封闭生命保障实验，故“任何人工封闭系统迟早都会被打开”只是常见趋势而非已被证明的全称判断。  
  来源：<https://en.wikipedia.org/wiki/Biosphere_2>；<https://www.biorxiv.org/content/10.1101/2021.01.12.426282v1>
- **#66** 「The 3,800 species will sidestep, outmaneuver, burrow under, and otherwise wear down the “keystone predator” th…」  
  判断：**部分符合**。生物圈二号两次封闭实验都出现氧气下降、物种损失和系统偏离设计等失控问题，说明物种与系统确实部分绕开了乘员控制；但乘员仍作为关键捕食者进行修剪管理，并未被“消耗”到完全失控。  
  来源：<https://en.wikipedia.org/wiki/Biosphere_2>；<https://www.newscientist.com/article/mg14119171-300-second-team-moves-into-the-bio-bubble/>
- **#68** 「The future should birth Bio2s in all sizes and varieties, housing every combination of species.」  
  判断：**部分符合**。Ecotron、受控生态生命保障和火星模拟舱等Bio2式系统后来确实以不同尺度出现；但远未达到“各种尺寸与种类、容纳各种物种组合”的多样化诞生。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC11669164/>；<https://www.scientificamerican.com/article/biosphere-2-the-once-infamous-live-in-terrarium-is-transforming-climate-research/>
- **#69** 「As Mark Nelson told me, “In the future there will be an enormous proliferation of niches for biospheres.”」  
  判断：**部分符合**。人工生物圈与密封微生态的研究生态位有所增加，但并未出现“巨大增殖”。  
  来源：<https://pubs.acs.org/asbcd6/article/13/12/3812/142053/Synthetic-Ecosystems-From-the-Test-Tube-to-the>；<https://www.nature.com/articles/s41598-024-75328-x>
- **#71** 「As we improve our machines they will become more organic, more biological, more like life, because life is the…」  
  判断：**部分符合**。软体机器人、演化形态等使部分机器更有机、更像生命；但机器改进的主线仍是数字化与机电性能，并非普遍变得更加生物化。  
  来源：<https://www.nature.com/articles/s42256-018-0009-9>；<https://chireviewofbooks.com/2021/08/24/god-human-animal-machine/>
- **#73** 「The adaptive house of the future will be more like an ecology of organisms than a single being, more like a ju…」  
  判断：**部分符合**。智能住宅已由多种联网装置组成，具有一定“生态”特征；但主流仍更接近中枢式助手（单一控制中心），而不是丛林般的有机体生态。  
  来源：<https://www.uni-weimar.de/fileadmin/user/fak/medien/professuren/Human-Computer_Interaction/Downloads/Papers_2024/muc2024-SmartHomesUserPerceptions.pdf>；<https://doi.org/10.22215/etd/2017-11903>
- **#74** 「Someday soon, when a visitor rings the doorbell, the doorbell will turn down the vacuum cleaner so that we can…」  
  判断：**部分符合**。门铃自动调低吸尘器音量这一具体互操作，在1994年后的“不久”并未出现；约三十多年后，Matter等智能家居标准使机器人吸尘器与其他设备联动在技术上可行，但并非常见默认行为。  
  来源：<https://www.ecovacs.com/us/blog/robot-vacuums-with-matter>；<https://www.dreametech.com/blogs/blog/matter-robot-vacuum>
- **#75** 「Soon universal time signals will be transmitted through all power and telephone lines.」  
  判断：**部分符合**。通用时间同步后来主要通过NTP、互联网和无线/卫星授时实现，电话拨号授时也存在；但并非“通过所有电力线和电话线”传输，字面路径只部分兑现。  
  来源：<https://www.eecis.udel.edu/~mills/database/papers/history/history.pdf>；<https://www.cisa.gov/sites/default/files/FactSheets/CISA%5FFactSheet%5FTechnical-Level%5FResilient%5FTiming%5FOverview%5FS508C.pdf>
- **#76** 「My prediction in 1994: Smart offices will materialize before smart homes.」  
  判断：**部分符合**。商业楼宇自动化在消费级智能家居大规模普及之前就已存在；但X10等家用智能控制更早出现且长期并行，因而“智能办公室将先于智能住宅出现”并非干净的时间顺序。  
  来源：<https://www.smarthomepoint.com/history/>；<https://www.forbes.com/sites/andrewweinreich/2017/12/18/the-future-of-the-smart-home-smart-homes-iot-a-century-in-the-making/>
- **#77** 「Networked computers and phones are mandatory in offices now; networked lights and furniture will be next.」  
  判断：**部分符合**。办公室内联网灯具已成为明确的下一步并已商业化；联网家具则只在部分工位/传感器家具中出现，并未同等成为标配。  
  来源：<https://images.philips.com/is/content/PhilipsConsumer/PDFDownloads/Global/ODLI20171905_001_en_AA-Philips-Lighting-Philips-Cisco-Connected-lighting-for-Enterprise-White-Paper-INT-A4-LR-DPS.pdf>；<https://facilityexecutive.com/driving-deeper-energy-savings-with-networked-lighting-controls/>
- **#79** 「Linked into the superorganism of a smart room, my chair will recognize me when I sit in it, versus」  
  判断：**部分符合**。用椅子传感器识别坐者的研究原型早已存在，但“我的椅子坐下时认出我”并未成为普遍部署的办公现实。  
  来源：<https://link.springer.com/article/10.1007/s10044-008-0124-z?code=4e5365e5-7da3-4739-b1a9-465bb3bb3d46&error=cookies_not_supported>；<https://ceur-ws.org/Vol-960/paper7.pdf>
- **#82** 「Every room will be different; indeed, every telephone will be different.」  
  判断：**部分符合**。手机与房间在软件配置、个性化方面确实分化；但公开评述同时指出智能手机硬件与外形高度同质化，“每一部电话都将不同”并不成立。  
  来源：<http://widerscreen.fi/assets/ReunanenLucenicNoppariChen2025PDF-1.pdf>；<https://www.forbes.com/sites/simonrockman1/2018/10/08/why-phones-are-all-the-same/>
- **#84** 「There will be nice-dog rooms and bad-dog rooms.」  
  判断：**部分符合**。智能空间“人格”与安防/迎宾等不同行为风格已有研究原型和语音助手实践；但“恶狗式房间咬入侵者、好狗式房间把访客赶到安全处并招待”并未成为普遍部署的房间行为。  
  来源：<https://www.mdpi.com/2411-9660/4/3/18>；<https://dl.acm.org/doi/10.1145/2971648.2971757>
- **#87** 「Eventually, all machines, factories, and human institutions will be members of the greater global bionic syste…」  
  判断：**部分符合**。工业共生、生物启发智能与部分仿生制造网络已经出现，一些工厂和制度进入了类生态协作；但远未达到“所有机器、工厂和人类制度”都成为单一全球仿生系统成员。  
  来源：<https://en.wikipedia.org/wiki/Kalundborg_Eco-industrial_Park>；<https://www.nju.edu.cn/en/info/1057/30621.htm>
- **#90** 「industrial activities would become “sustainable,” to use current jargon, as they become more organic.」  
  判断：**部分符合**。工业共生、生物炼制与循环经济确被用来推动“更有机”的工业活动并服务于可持续目标；但工业整体并未因此变为可持续，有机路径也不自动等于可持续。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC12639295/>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC5362009/>
- **#91** 「A future “hydrogen economy” would use sunlight to crack water into hydrogen and oxygen, and then pump the hydr…」  
  判断：**部分符合**。太阳能/低碳制氢、氢气管网与终端用氢已有项目，技术路径存在；但全球氢生产仍几乎全部来自未减排化石燃料，低碳氢约占1%，且近年出现项目取消与退潮，所描述的氢经济并未成为能源系统。  
  来源：<https://www.iea.org/reports/global-hydrogen-review-2026/production>；<https://h2sciencecoalition.com/trackers/>；<https://www.reuters.com/sustainability/climate-energy/green-hydrogen-retreat-poses-threat-to-emissions-targets-2025-07-23/>
- **#92** 「soon, bioengineered processes that will use gene-spliced organisms to produce silk or vitamins or glues.」  
  判断：**部分符合**。用基因工程微生物生产维生素等物质在1990年代前后已进入工业生物技术；但重组蜘蛛丝等材料长期未能按“很快”实现规模商业化，示例并未整体按时兑现。  
  来源：<https://www.cambridge.org/core/journals/mrs-bulletin/article/synthetic-biologyengineering-nature-to-make-materials/C7EC6D396233E60CEED02B61FFF40637>；<https://www.science.org/content/article/spinning-spider-silk-startup-gold>
- **#93** 「Industry will inevitably adopt biological ways」  
  判断：**部分符合**。工业生物技术、酶制剂与生物制造已在部分行业被采用；但公开评估表明它并未发展得如预期那样快，化学与机械路径仍占主导，“不可避免地采用生物学方式”并未成为工业整体事实。  
  来源：<https://jewettlab.org/wp-content/uploads/2024/10/danielson-et-al-2020-industrial-biotechnology-an-industry-at-an-inflection-point.pdf>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC3520750/>
- **#95** 「Manufacturers will perceive natural biological processes as competitive」  
  判断：**部分符合**。仿生设计与专利趋势表明，部分制造商已把自然生物过程当作创新对标甚至竞争路径；但在大宗化学品上，公开评述认为微生物发酵仍难以在成本与规模上与石油路线竞争。  
  来源：<https://www.reuters.com/sustainability/land-use-biodiversity/bullet-trains-green-buildings-innovators-take-cue-from-nature-through-biomimicry-2025-01-13/>；<https://www.nature.com/articles/s41587-026-03325-8>
- **#96** 「and this will drive manufactured processes toward biological-type solutions.」  
  判断：**部分符合**。美国BioMADE、生物智能制造等表明制造工艺出现转向生物类型方案的推动；但微生物路径无法取代石油化工主体，也有论述反对用活体去制造本可由化学完成的产品，故只是部分转向。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC9996699/>；<https://www.nature.com/articles/s41587-026-03325-8>
- **#97** 「Artificial complex systems will be deliberately infused with organic principles simply to keep them going.」  
  判断：**部分符合**。复杂系统工程文献主张，当经典工程达到极限时需引入进化、发育等有机原则；相关研究与倡议已经出现，但检索结果多为研究论述，尚不能证明“只为维持运转而有意注入有机原则”已成为普遍工程实践。  
  来源：<http://www.cs.mun.ca/~banzhaf/papers/complexity2007.pdf>；<http://www.cui.unige.ch/~dimarzo/papers/IJBIC2011a.pdf>
- **#98** 「the artificial will have to conform to the natural in the long term.」  
  判断：**部分符合**。在生态约束下从事工程、以及人工智能的“地球对齐”等原则表明，人造系统开始被要求顺应自然限度；但长期“不得不顺应”尚未成为系统事实，许多人造系统仍在逆自然约束运行。  
  来源：<https://www.nationalacademies.org/read/4919/chapter/6>；<https://www.microsoft.com/en-us/research/wp-content/uploads/2026/04/Earth-Alignment-AI_-GaffneyLuers_et-al_2025.pdf>
- **#99** 「What the next century will really usher in is hyperbiology: Synthetic Mice. Computer Viruses. Engineered Genes…」  
  判断：**部分符合**。21世纪已出现转基因动物、工程基因、工业生态、定向进化和计算机病毒等“超生物学”要素；但人工生命仍不成熟，且这些并非本世纪唯一或当然的主线。  
  来源：<https://files.catbox.moe/ab57w5.pdf>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC2222615/>
- **#102** 「In a few years—no dream—you would pick up a gadget and get a “video dialtone” which would enable you to send o…」  
  判断：**部分符合**。“几年之内”以1990年代末为期：电子邮件与网页已能传送照片、文本和部分文件，但电信业的“视频拨号音”并未按时成为可向任何人即时收发电影等全媒体的普及装置，完整能力要到此后多年才出现。  
  来源：<https://www.servsig.org/wordpress/wp-content/uploads/2015/02/Video-Dial-Tone.pdf>；<https://jolt.law.harvard.edu/assets/articlePDFs/v06/06HarvJLTech343.pdf>
- **#106** 「In time all machines will be wired into a net so that they warn repairmen when they are flaking out」  
  判断：**部分符合**。大量工业与服务设备已联网并可在异常时向运维报警；但“所有机器”并未接入，故障处理仍常在停机后才被动发现。  
  来源：<https://www.velotic.com/resources/case-study/industrial-equipment-services-provider>；<https://blogs.cisco.com/industrial-iot/maximizing-uptime-the-power-of-ai-troubleshooting-for-industrial-networks>
- **#109** 「It may get to the point that wholly autonomous companies become rare.」  
  判断：**部分符合**。商业生态系统使行业与企业边界明显模糊，完全封闭自主的公司减少；但边界清晰、独立经营的公司远未变得罕见，仍是主流形态之一。  
  来源：<https://www.deloitte.com/content/dam/insights/articles/2024/supply-chains-to-value-webs-business-trends/dup-1048-business-ecosystems-come-of-age-master-final.pdf>；<https://bcghendersoninstitute.com/wp-content/uploads/2020/06/Why-Do-Most-Ecosystems-Fail.pdf>
- **#111** 「Sony lost badly on Beta VCRs but may yet prevail with 8-mm tapes」  
  判断：**部分符合**。8毫米磁带在索尼摄像机市场上曾有较长的成功期，但并未作为主导家用录像格式“胜出”，最终与VHS-C一样被数字格式取代。  
  来源：<https://en.wikipedia.org/wiki/8_mm_video_format>；<https://www.tapedmemories.com/post/the-last-videotape-format>
- **#112** 「When shelf items acquire awareness of each other and themselves and interact with their consumers, they rapidl…」  
  判断：**部分符合**。RFID与智能货架使部分商品可被感知并进入零售流程，条件已在局部触发；但货架商品并未因此迅速涌入一种截然不同的整体经济。  
  来源：<https://www.newark.com/technical-resources/articles/iot-smart-retailing>；<https://www.retailtouchpoints.com/features/are-smart-shelves-the-tech-supermarkets-need/20971/>
- **#114** 「The future of network economics is in devising reliable processes, rather than reliable products.」  
  判断：**部分符合**。DevOps、持续交付和软件即服务把可靠过程放到了网络经济的中心；但产品本身的质量仍被证明是网络市场竞争的关键，并非“只设计可靠过程、不设计可靠产品”。  
  来源：<https://queue.acm.org/doi/full/10.1145/3329781.3338532>；<https://sloanreview.mit.edu/article/how-quality-drives-the-rise-and-fall-of-high-tech-products/>
- **#115** 「The boundaries of a company blur to obscurity.」  
  判断：**部分符合**。平台与商业生态系统确实使公司边界明显模糊；但法律与经营上的公司边界仍然可以辨认，远未到“几乎无法辨认”。  
  来源：<https://sms.onlinelibrary.wiley.com/doi/10.1002/smj.3250>；<https://www.deloitte.com/content/dam/insights/articles/2024/supply-chains-to-value-webs-business-trends/dup-1048-business-ecosystems-come-of-age-master-final.pdf>
- **#117** 「All products are manufactured to personal specifications, but at mass production prices.」  
  判断：**部分符合**。大规模定制已使部分产品能以接近量产的成本按个人规格制造；但并非所有产品都如此，个性化仍常带来额外成本。  
  来源：<https://usersolutions.com/blog/mass-customization-manufacturing>；<https://www.sciencedirect.com/science/article/abs/pii/S0925527319302646>
- **#119** 「Connecting is free; switching is expensive.」  
  判断：**部分符合**。转换成本与锁定效应已有充分证据，切换确实昂贵；但网络连接通常仍需付费，并非普遍免费。  
  来源：<https://www.nuffield.ox.ac.uk/economics/papers/2006/w7/farrell_klempererwp.pdf>；<https://blogs.lse.ac.uk/businessreview/2019/09/24/how-digital-businesses-can-leverage-the-high-cost-for-consumers-to-switch-platforms/>
- **#120** 「Everyday digital cash replaces batch-mode paper money. All accounts become real-time.」  
  判断：**部分符合**。无现金支付与快速支付显著增长，许多账户已接近实时；但纸币并未被日常数字现金完全取代，也并非所有账户都已变成实时账户。  
  来源：<https://www.bis.org/publications/202503-commentary-red-book.pdf>；<https://www.principal.com/financial-inclusion/key-themes/instant-payments-are-rising-cash-isnt-disappearing-everywhere>
- **#121** 「the informal economy booms」  
  判断：**部分符合**。国际劳工组织与世界银行等显示，非正式经济在全球尤其是新兴经济体中仍然庞大并持续存在；但公开估计并非一致表明其在1994年后全面蓬勃扩张，部分国家规模有升有降。  
  来源：<https://ilostat.ilo.org/topics/informality/>；<https://thedocs.worldbank.org/en/doc/37511318c092e6fd4ca3c60f0af0bea3-0350012021/related/Informal-economy-Chapter-2-policy-brief.pdf>
- **#123** 「All matter, big and small, will be linked into vast webs of networks at many levels.」  
  判断：**部分符合**。物联网与“万物互联”已把大量物体接入多层网络；但远非“所有物质无论大小”都被连成一张巨网。  
  来源：<https://instituteofinterneteconomics.org/state-of-the-internet-2026-mid-year-review/>；<https://www.netguru.com/blog/internet-of-everything-guide>
- **#124** 「We humans will be unconscious of what the global mind ponders.」  
  判断：**部分符合**。大规模算法与人工智能系统的不透明性已被公开讨论，人类往往无法理解其整体“思考”；但“全球心智”是隐喻，人类对网络集体过程也并非完全毫无察觉。  
  来源：<https://www.bbc.com/future/article/20230405-why-ai-is-becoming-impossible-for-humans-to-understand>；<https://pure.teikyo.jp/en/publications/on-the-collective-algorithmic-unconscious/>
- **#126** 「network economics will breed a new spiritualism.」  
  判断：**部分符合**。数字宗教与技术灵性实践已形成研究领域，网络确实出现了新的灵性活动；但更多是既有宗教与灵性的数字化延伸，是否“孕育了一种新的灵性主义”并不完整。  
  来源：<https://www.dhi.ac.uk/san/waysofbeing/data/communication-zangana-bell-2006a.pdf>；<https://onlinelibrary.wiley.com/doi/10.1111/rsr.17062>
- **#129** 「pervasive encryption removes economic activity—one driving force of our society—from any hope of central contr…」  
  判断：**部分符合**。加密与区块链被用来构建平行交易系统，但普遍加密并未使经济活动脱离任何集中控制；政府监管、合规交易所和政策干预仍然有效。  
  来源：<https://doi.org/10.2139/ssrn.6959699>；<https://policy.i2coalition.com/wp-content/uploads/2026/04/FINAL-Encryption-at-Risk-Report.pdf>
- **#130** 「its users will sooner or later graduate to commercially supported stuff.」  
  判断：**部分符合**。免费增值和开源商业化确实把一部分免费用户转化为付费或商业支持产品；但仍有大量用户长期停留在免费软件上，“迟早都会升级”并不成立。  
  来源：<https://ideas.repec.org/a/spr/infsem/v23y2025i2d10.1007_s10257-024-00690-2.html>；<https://a16z.com/open-source-from-community-to-commercialization/>
- **#132** 「Most privacy transactions will soon take place in the marketplace rather than in government offices」  
  判断：**部分符合**。1990年代末已出现信息中介与隐私市场尝试，后来隐私技术市场扩大；但“很快大多数隐私交易发生在市场而非政府机关”并未按时实现，政府规制仍是主渠道之一。  
  来源：<https://www.wired.com/1999/08/privaseek-seeks-attention/>；<https://javnost-thepublic.org/article/pdf/2011/2/6/>
- **#133** 「Hundreds of privacy vendors will sell bits of privacy at market rates.」  
  判断：**部分符合**。隐私技术厂商数量与市场规模在2010–2020年代显著扩张，形成按市场价格提供隐私能力的产业；但摘录中明确列出的图谱多为数十家量级，“数百家出售点滴隐私”未在来源中直接证实为已达成。  
  来源：<https://privacyterms.io/privacy-tech-market-size-2026>；<https://www.adexchanger.com/privacy/the-privacy-tech-vendor-landscape-exploded-in-2021/>
- **#135** 「People will readily pay for bits of cheap information before viewing, particularly if the payment invisibly de…」  
  判断：**部分符合**。按篇微支付和自动扣款在部分平台出现（如Blendle、应用内购买），但公开评述认为微支付并未兑现“人们乐意在观看前为廉价点滴信息付费”的主流承诺。  
  来源：<https://en.wikipedia.org/wiki/Blendle>；<https://digiday.com/media/hunt-reader-revenue-publishers-give-micropayments-another-look/>
- **#136** 「When pocket cash goes digital—demassified into data in the same transformation that institutional money underw…」  
  判断：**部分符合**。口袋现金已在很大程度上被数字支付替代，信息经济因此出现深刻变化；但现金仍未消失，所谓“最深刻的后果”已部分出现而非完整应验。  
  来源：<https://research.gold.ac.uk/id/eprint/34104/1/MCCS-%20Tkacz2019a.pdf>；<https://www.newyorker.com/business/currency/why-digital-money-hasnt-killed-cash>
- **#137** 「the full effects of an electronic economy will have to wait until everyday petty cash (and check) transactions…」  
  判断：**部分符合**。支票清算数字化和日常电子支付已带来显著的电子经济效应；但现金交易并未全部数字化，所谓“全部效应必待二者都数字化之后才会出现”并不准确。  
  来源：<https://www.atlantafed.org/who-we-are/atlanta-fed-history/modern-era/payments>；<https://www.stlouisfed.org/publications/page-one-economics/2024/01/02/payment-systems-evolution-how-does-money-move-from-a-buyer-to-seller>
- **#139** 「In variations on Chaum’s basic design, people may also have computer appliances at home, loaded with digital c…」  
  判断：**部分符合**。查姆式eCash确曾作为网络电子现金上线，实现了通过计算机网络收付款；但该具体设计很快商业失败，后来的网络货币采用了不同架构。  
  来源：<https://chaum.com/ecash/>；<https://www.forbes.com/forbes/1999/1101/6411390a.html>
- **#143** 「truly digital money—or, more accurately, the economic mechanics needed for truly digital cash—will rewire the …」  
  判断：**部分符合**。数字支付与货币数字化改变了交换与部分金融安排，公开研究也讨论其对增长和货币职能的影响；但尚未全面改写经济、通信与知识的性质。  
  来源：<https://www.bis.org/publications/working-paper-941-digitalisation-money.pdf>；<https://www.suerf.org/wp-content/uploads/2024/09/SUERF-Policy-Brief-990_-Aguilar-et-al.pdf>
- **#144** 「Digital cash used on a large scale will further accelerate money’s velocity.」  
  判断：**部分符合**。有研究讨论数字支付对货币流通速度的影响，并存在加快交易的机制；但实证结果并不一致，不能认定大规模数字现金已经进一步加快了流通速度。  
  来源：<https://www.tandfonline.com/doi/full/10.1080/00036846.2025.2540611>；<https://journal.uii.ac.id/JEP/article/view/33626>
- **#145** 「Your e-money account pays for each phone call as soon as you hang up, or—how about this?—as you are talking.」  
  判断：**部分符合**。电信预付费和按使用计费使部分通话可以接近使用时扣款；但主流是套餐与月结，并非挂断或通话过程中从电子货币账户为每一通电话即时滴流支付。  
  来源：<https://www.freepatentsonline.com/y2008/0279355.html>；<https://kb.voipcloud.online/au/billing/prepaid-and-postpaid/>
- **#146** 「This puts a crimp on banks which derive a lot of their current profit on the “float”—which instantaneity erase…」  
  判断：**部分符合**。即时支付系统已在多国出现，并被研究认为会冲击银行支付利润与在途资金；但许多转账仍需数日，浮存利润并未被即时性完全抹掉。  
  来源：<https://www.bcb.gov.br/content/publicacoes/WorkingPaperSeries/WP619.pdf>；<https://www.vox.com/the-highlight/400464/bank-transfer-ach-fednow-instant-payments>
- **#148** 「so e-money will break the monopoly of financial Brahmins.」  
  判断：**部分符合**。金融科技与非银行电子货币部分打破了传统金融机构对金钱操控的垄断；但央行和大型银行仍主导货币发行与核心金融权力，垄断并未被打破。  
  来源：<https://cepr.org/voxeu/columns/e-money-and-monetary-policy-transmission>；<https://www.tandfonline.com/doi/pdf/10.1080/13563467.2026.2737130>
- **#151** 「E-money will lower this formidable barrier. By doing so it will provide a powerful tool to private governance …」  
  判断：**部分符合**。加密货币和补充货币降低了私人铸币的部分壁垒；但政府在流通货币上的垄断大体仍在，将其作为叛离族群或边缘城市私人治理的有力工具并未成为普遍事实。  
  来源：<https://www.tandfonline.com/doi/full/10.1080/19420676.2017.1364287>；<https://repository.law.umich.edu/cgi/viewcontent.cgi?article=1339&context=law_econ_current>
- **#155** 「Usable electronic money may be the most important outcome of a sudden grassroots takeover of the formerly esot…」  
  判断：**部分符合**。比特币等可用电子货币确被广泛视为密码朋克草根运动的重要成果；但加密进入主流后还有HTTPS等影响更广的用途，‘最重要成果’这一比较判断并不能确定。  
  来源：<https://www.btcpolicy.org/articles/why-bitcoin-part-1-cypherpunk-dreams>；<https://spectrum.ieee.org/bitcoin-the-cryptoanarchists-answer-to-cash>
- **#157** 「Left to itself, the Net will connect everyone to everyone, everything to everything.」  
  判断：**部分符合**。全球已有约76%的人口上网，物联网也连接了大量事物；但仍有约20亿人离线，并非每个人与每件事都已连接，网络也未被完全放任自行发展。  
  来源：<https://www.itu.int/itu-d/reports/statistics/2026/10/13/ff26-internet-use/>；<https://www.internetsociety.org/blog/2026/11/there-are-6-3-billion-people-connected-to-the-internet-yet-2-billion-remain-offline/>
- **#161** 「Over time, god-customers will evolve fairly sturdy and endearing populations, which they will be eager to test…」  
  判断：**部分符合**。《模拟城市》《孢子》等神游戏中，玩家会培养种群并用灾害去考验它们；但并未普遍达到作者所描绘的、扮演上帝的顾客进化出稳固可爱种群后再急于加以完全渲染自然灾害考验的形态。  
  来源：<https://www.manospondylus.com/2021/11/simearth-ultimate-god-game.html>；<https://tvtropes.org/pmwiki/pmwiki.php/VideoGame/Spore>
- **#164** 「a state-of-the-art supercomputer would spend hours computing a few seconds of a real-time holograph the size o…」  
  判断：**部分符合**。1990年代计算机全息计算确实极为耗时；但后来已出现实时或近实时计算机全息研究，‘可预见未来即使用上所有技巧仍需数小时’并未作为持续约束成立。  
  来源：<https://www.media.mit.edu/spi/SPIPapers/lucente/holo92.pdf>；<https://doi.org/10.4218/etrij.2026-0062>
- **#166** 「What the military is groping towards is “embedded training”—training simulation so real it is indistinguishabl…」  
  判断：**部分符合**。嵌入式训练已被军方采用并写入战车等装备；但公开讨论仍指出模拟与实战存在差距，尚未达到‘真实到无法区分’。  
  来源：<https://www.oasis-ae.com/embedded-training>；<https://library.edvirtus.com/journals/journal-of-battlefield-technology/volume-03/issue-01/3-1-6-darby.html>
- **#169** 「The future of MUDs, then, converges upon the future of SIMNET, the future of SimCity, and the future of virtua…」  
  判断：**部分符合**。多人在线世界后来融合了持久虚拟世界、城市/世界模拟和部分虚拟现实；但与军事SIMNET的全面合流并不完整。  
  来源：<https://publishing-project.rivendellweb.net/from-text-to-telepresence/>；<https://www.usenix.org/legacy/publications/library/proceedings/coots98/vellon/vellon_html/vellon.html>
- **#176** 「It is this supercompatibility between evolution and computers that will propel artificial evolution into our d…」  
  判断：**部分符合**。数字进化已在人工生命、进化算法和部分应用中出现；但尚未全面进入‘我们的数字生活’，更多仍属研究与特定工具。  
  来源：<https://direct.mit.edu/artl/article/26/2/274/93255/The-Surprising-Creativity-of-Digital-Evolution-A>；<https://arxiv.org/abs/1512.02100>
- **#177** 「Evolution will be imported wherever engineering balks.」  
  判断：**部分符合**。在神经网络架构搜索和设计优化等工程受阻处，人们已引入进化方法；但并非在工程受阻的任何地方都如此。  
  来源：<https://arxiv.org/abs/2008.10937>；<https://dl.acm.org/doi/10.1007/s10462-021-10049-5>
- **#182** 「Artificial evolution may be the only way to keep software on its toes, looking lively.」  
  判断：**部分符合**。有人主张用进化式开发维持软件存活，但让软件保持运行的主流办法仍是工程维护与DevOps，人工进化并非“唯一办法”。  
  来源：<https://cacm.acm.org/opinion/time-to-take-evolutionary-development-off-the-shelf/>；<https://www.swebook.org/chapters/15-maintenance-evolution/>
- **#183** 「Artificial evolution is the end of engineering’s hegemony. Evolution will take us beyond our ability to plan.」  
  判断：**部分符合**。进化与学习方法扩展了复杂系统的构造方式，有时会超出事先计划；但工程霸权并未终结，计划与设计仍然主导大多数系统。  
  来源：<https://sderosiaux.medium.com/how-engineering-beats-evolution-4533e35bdc0a>；<https://www.far.ai/event-recordings/stuart-russell-ai-what-if-we-succeed>
- **#184** 「Evolution will craft things we can’t. Evolution will make them more flawless than we can. And evolution will m…」  
  判断：**部分符合**。进化方法能够产生人类不容易事先设计的方案；但并未普遍把产物做得比人工更无瑕，也未以前所未有的方式广泛承担维护。  
  来源：<https://steve.blog/2006/07/13/the-dichotomy-of-design-and-evolution/>；<https://doras.dcu.ie/16678/1/dagstuhl-2009.pdf>
- **#187** 「No one will control the destination of Tom Ray’s soup of critters.」  
  判断：**部分符合**。Tierra等人工生命系统中，数字生物的演化路径确实难以完全预先控制；但该“生物汤”仍是受约束的实验系统，并未失控进入外部世界。  
  来源：<https://www.newscientist.com/article/1850470-its-life-but-not-as-we-know-it-2/>；<https://tomray.me/tierra/whatis.html>
- **#188** 「At some point in the very near future the engineering skills of nanotechnology and the engineering skills of b…」  
  判断：**部分符合**。纳米技术与生物技术的工程能力后来确实走向汇合并形成交叉领域；但并非在1994年所指的“很近的将来”立即完成。  
  来源：<https://doi.org/10.1057/palgrave.jcb.3040156>；<https://doi.org/10.1007/s00289-025-06232-1>
- **#190** 「We will trade correctness for flexibility and durability.」  
  判断：**部分符合**。软件与系统设计中确实存在用灵活性、可适应性去交换严格正确性的做法；但安全关键系统仍强调正确性，这一交换并未成为普遍原则。  
  来源：<https://saassystemscanon.com/layer-0/you-are-always-trading-correctness-for-something/>；<https://worrydream.com/refs/Sussman_1999_-_Robust_Design_through_Diversity.pdf>
- **#191** 「Someday, though, the dinosaurs may become Pinocchios—puppets given their own life.」  
  判断：**部分符合**。数字恐龙和生物动画引入了更多程序化与群体行为模拟；但影视中的恐龙仍主要是动画师驱动的“木偶”，并未普遍成为拥有自身意志的皮诺曹。  
  来源：<https://www.businessinsider.com/jurassic-movies-dinosaurs-evolution-special-effects-technology-cgi-world-dominion-2022-7>；<https://jlupub.ub.uni-giessen.de/server/api/core/bitstreams/c8feb6b2-abf7-491b-a7c8-e468901b29ab/content>
- **#192** 「To make these digital worlds really work in the future, everything in creation will have to be reduced to equa…」  
  判断：**部分符合**。数字世界大量依赖物理与几何方程，水和部分场景已被方程化；但造物中的一切都必须还原为方程，既未完成，也不是所有数字世界运转的前提。  
  来源：<https://www.promptinjection.net/p/matrix-got-closer-but-not-the-way-we-thought-ai-world-models>；<https://marlowe-research.stanford.edu/research/wetzstein-life-in-simulation/>
- **#193** 「every manufactured item in the near future will be designed and produced using CAD (computer-assisted design) …」  
  判断：**部分符合**。计算机辅助设计已成为制造业中广泛采用的工具；但调查显示采用率并非百分之百，谈不上“每件制成品”都用CAD设计和生产。  
  来源：<https://mpra.ub.uni-muenchen.de/121182/1/MPRA_paper_121182.pdf>；<https://www.osti.gov/servlets/purl/14442>
- **#194** 「Someday soon, the printed object will be the authentic part.」  
  判断：**部分符合**。增材制造已使打印件在部分领域成为正品生产零件；但这一转变并非在1994年后不久就实现，而用了更长时间。  
  来源：<https://www.additivemanufacturing.media/articles/from-master-patterns-to-mass-production>；<https://www.ingenia.org.uk/articles/additive-manufacturing-and-3d-printing/>
- **#196** 「Disney is now working on their first completely digital animation, to be released in late 1994.」  
  判断：**部分符合**。迪士尼参与发行的第一部完全数字长片《玩具总动员》确实出现，但上映于1995年11月，而不是计划中的1994年末。  
  来源：<https://thewaltdisneycompany.com/news/toy-story-pixar-history/>；<https://www.dix-project.net/document/computer-graphics-world_1995-08_toy-story>
- **#197** 「But tomorrow, they won’t be. If computer power continues to increase as it has, within five years we’ll see a …」  
  判断：**部分符合**。计算能力持续增长的条件已满足；至约1999年已有以虚拟角色为核心的电影，但五年内并未出现以自主合成行为驱动的合成身体角色真正主演的影片。  
  来源：<https://sf-encyclopedia.com/entry/matrix_the>；<https://en.wikipedia.org/wiki/Virtuosity>
- **#199** 「An entirely convincing virtual human form is tricky, but close at hand.」  
  判断：**部分符合**。虚拟人体外形持续进步，但“完全令人信服已近在眼前”在1994年过于乐观，恐怖谷等问题长期存在。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC4484984/>；<https://interactions.acm.org/archive/view/september-october-2018/avoiding-the-uncanny-valley-in-virtual-character-design>
- **#200** 「Depression, elation, and rage will all be add-on modules for a creature’s operating system.」  
  判断：**部分符合**。抑郁、欣快、愤怒等情绪作为软件模块出现在情感计算和游戏人工智能中；但并未成为普遍的“生物操作系统附加模块”。  
  来源：<https://qrg.northwestern.edu/Resources/aigames.org/2000/IWilson00.pdf>；<https://edukatesg.com/civos-runtime-emotion-feelings-lattice-v1-1-upgrade-pack/>
- **#201** 「Some software companies will sell better versions of the fear emotion than others.」  
  判断：**部分符合**。游戏与情感计算市场已出现可购买、相互竞争的情绪或行为人工智能模块；但专门以“恐惧模块”为商品、并形成公司间明显优劣的产业并不成熟。  
  来源：<https://gamesbyhyper.com/product/routine-driven-npc-framework/>；<https://assetstore.unity.com/packages/tools/behavior-ai/moodme-4-emotions-bad-moments-editions-barracuda-sdk-201980>
- **#203** 「someday Mickey Mouse will have his own agenda.」  
  判断：**部分符合**。迪士尼已在研发可更自然对话的自主机器人和数字角色，方向朝“自己的议程”靠近；但米老鼠拥有独立议程的终点尚未到来。  
  来源：<https://wdwnt.com/2026/11/disney-patents-real-time-ai-technology-that-allows-meet-and-greet-characters-talk-to-guests/>；<https://en.wikipedia.org/wiki/Mickey_Mouse>
- **#204** 「It’s the winter of 2001, in a corner of the Disney studio lot; a trailer is set up as a top-secret research la…」  
  判断：**部分符合**。迪士尼确实设有Secret Lab，但该实验室在2001年10月被宣布关闭，并未在2001年冬交付可自主行走、跳跃、舞蹈的三维米老鼠。  
  来源：<https://jimhillmedia.com/the-sad-tale-of-disneys-secret-lab/>；<https://www.orlandoweekly.com/arts/a-workplace-thats-a-real-bear-2261743/>
- **#206** 「So by 2007, Mickey Mouse is quite an actor.」  
  判断：**部分符合**。到2007年，米老鼠已出现在计算机动画影片和乐园演出中，表演形态更数字化；但并非因此就成为相当出色的自主‘演员’。  
  来源：<https://allears.net/walt-disney-world-chronicles-mickey-mouse-at-walt-disney-world/>；<https://www.behindthevoiceactors.com/movies/Mickeys-Great-Clubhouse-Hunt/>
- **#208** 「someday Disney will have to deal with an autonomous out-of-control Roger Rabbit.」  
  判断：**部分符合**。迪士尼已开始把角色接入生成式人工智能并开发自主角色，因而必须面对控制与治理问题；但“自主失控的罗杰兔”尚未成为必须应对的既成事实。  
  来源：<https://thewaltdisneycompany.com/news/disney-openai-sora-agreement/>；<https://sites.disney.com/waltdisneyimagineering/autonomous-characters/>
- **#209** 「They will remain indirectly under our influence and guidance but free of our domination.」  
  判断：**部分符合**。被赋予更强能力的机器日益需要引导而非完全手控，但整体上仍受人类支配，并未普遍“免于主宰”。  
  来源：<https://link.springer.com/article/10.1007/s43681-026-01400-z?code=9067426c-750a-46e2-9623-56424b79fc29&error=cookies_not_supported>；<https://control-inversion.ai/assets/pdf/Control_Inversion__Final_PubV_6Nov2025.pdf>
- **#211** 「more than we will have in future very complex systems.」  
  判断：**部分符合**。在高度复杂的自主系统中，直接管理减少、更多变成治理或意图监督，这一方向已经出现；但监督并未普遍少到使“管理”一词失效。  
  来源：<https://www.nokia.com/blog/the-glass-box-imperative-governing-intent-based-automation-in-ai-native-networks/>；<https://raeng.org.uk/media/4wxiazh3/engineering-x-safer-complex-systems-an-initial-framework-report-v22.pdf>
- **#213** 「Human actors will not be out of jobs. While some characters will be wholly autonomous, most will be of a cybor…」  
  判断：**部分符合**。人类演员作为群体并未失业，部分角色已高度数字化或由人工智能生成；但大多数角色是人机共控半机械角色这一格局尚未成为演艺业主流。  
  来源：<https://www.theguardian.com/film/2019/jul/03/in-the-age-of-deepfakes-could-virtual-actors-put-humans-out-of-business>；<https://www.businessinsider.com/actors-losing-jobs-to-ai-hollywood-micro-drama-industry-2026-6>
- **#214** 「This was the future of software programming! Define a problem and the machine will find a solution while the e…」  
  判断：**部分符合**。程序综合与生成式编程已能从问题描述出发写出代码；但尚未达到工程师定义问题后便可离场、由机器独自找出解答的程度。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC5597726/>；<https://medium.com/@nick.ciubotariu/syntax-is-dead-long-live-human-engineering-8defdeac54f8>
- **#217** 「Someday hyperlife will blossom in automobiles, buildings, TVs, and test tubes.」  
  判断：**部分符合**。汽车、建筑、电视中的自适应系统以及实验室中的合成生命研究都有进展；但“超生命在这些地方绽放”的终点尚未到来。  
  来源：<https://phys.org/news/2026-07-synthetic-life-lab-spudcell-falls.html>；<https://cyborganthropology.com/index.php/Hyperlife>
- **#218** 「Water striders will forever retain certain characteristics unique to carbon-based life.」  
  判断：**部分符合**。公开文献支持碳基生命具有硅基难以复制的独特化学特征，水黾作为碳基生物至今仍保留这些特征；但“永远”无法在观测窗口内完全证实。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC7345352/>；<https://www.askamathematician.com/2019/12/q-is-silicon-life-possible-why-all-the-fuss-over-carbon-based-life/>
- **#220** 「But daily revolution, I predict, will be headed off by daily evolution. The last revolution in technology will…」  
  判断：**部分符合**。确有论述主张以演化式变革理解技术变化，并质疑不断革命的叙事；但“日常革命将被日常进化阻挡、技术的最后一次革命是拥抱演化式变革”并未成为已完成的技术史事实。  
  来源：<https://link.springer.com/chapter/10.1007/978-3-031-74779-3_2>；<https://www.pmi.org/learning/library/evolution-revolution-defining-elements-concerns-4049>
- **#222** 「The obvious course that evolution seems bound to hit sooner or later is self-direction.」  
  判断：**部分符合**。定向进化等使进化更具导向性；但进化自身“注定走到自我导向”既非已被证明的必然，也尚未成为完成的事实。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC4344831/>；<https://bigquestionsonline.com/2017/01/26/does-evolution-have-direction/>
- **#224** 「that I believe will shape our future in the long term.」  
  判断：**部分符合**。关于深层进化的发现已在合成生物学、病毒演化和人工智能中产生影响；但“将在长期塑造我们的未来”仍是进行中的判断，尚未完全兑现。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC13669622/>；<https://research.a-star.edu.sg/articles/features/where-will-evolution-take-us-in-the-fourth-industrial-revolution/>
- **#225** 「Many of the promises for artificial evolution foretold in this book will still come about if artificial evolut…」  
  判断：**部分符合**。即便把人工进化主要看作适应性微观变化，遗传算法等已兑现本书的部分承诺；但“许多承诺仍将实现”并未整体完成。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC7662872/>；<https://ar5iv.labs.arxiv.org/html/2011.05277>
- **#226** 「Artificial evolution will only take off when it is embodied.」  
  判断：**部分符合**。具身进化机器人是重要方向，有文献主张具身使人工进化更有力；但软件中的人工进化同样取得进展，“只有被赋予身体才会真正起飞”过强。  
  来源：<https://doi.org/10.56367/oag-037-10494>；<https://robot-evolution.info/>
- **#228** 「Required to adapt too far from their origins, most institutions will die.」  
  判断：**部分符合**。制度在被迫远离起源的适应中会出现衰败或失败；但“大多数制度将会消亡”并未被充分证实，也有关于制度长寿的研究。  
  来源：<https://www.cambridge.org/core/journals/economics-and-philosophy/article/how-institutions-decay-towards-an-endogenous-theory/E5426C2B1BC11A6AF97C16165564C1C3>；<https://journals.sagepub.com/doi/10.1177/2053019619886670>
- **#229** 「As we construct an artificial evolution to breed machines and software, we will also need to allow for this he…」  
  判断：**部分符合**。人工进化与自适应软件研究中确有人强调必须允许异质性；但这并非构造机器与软件人工进化时已被普遍遵守的必要条件。  
  来源：<https://doi.org/10.1007/978-3-540-24688-6_72>；<http://www.andrewjamesturner.co.uk/files/AISB2014.pdf>
- **#231** 「Where ideas are free to flow and generate new ideas, the political organization will eventually head toward de…」  
  判断：**部分符合**。观念自由流动的网络一度被看作民主化力量，部分研究显示有民主效应；但后来也有证据表明数字媒体与民主衰退、威权利用并存，“不可避免地走向民主”不成立。  
  来源：<https://journals.sagepub.com/doi/10.1177/1748048508100909>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC9883171/>
- **#234** 「Having infiltrated computers, artificial life will henceforth never retreat from being in some computer, somew…」  
  判断：**部分符合**。人工生命程序自1990年代以来持续存在于某些计算机中，难以被彻底抹去；但“从此再也不会从某台、某处的计算机中完全撤退”是过强的永久判断，无法完全证实。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC12489504/>；<https://pickles.news/posts/ai-creatures-of-the-2000s/>
- **#236** 「Artificial evolution will likewise evolve, both artificially and naturally. We will engineer it to accomplish …」  
  判断：**部分符合**。人工进化本身正被工程化并用于特定任务，也出现多种路径；但“培育许多物种的人工进化以便更好地做特定工作”只部分实现。  
  来源：<https://arxiv.org/html/2604.05142v2>；<https://link.springer.com/article/10.1007/s12052-008-0114-z>
- **#237** 「Many years hence, you’ll be able to select a particular brand of artificial evolution out of a catalog to get …」  
  判断：**部分符合**。多年以后已出现多种进化式人工智能与智能体框架可供选用；但尚未形成可从目录中挑选品牌、以获得恰到好处新奇或完美自我导向的成熟市场。  
  来源：<https://github.com/EvoMap/awesome-agent-evolution>；<https://agentconn.com/blog/self-evolving-ai-agents-evolver-genericagent-deerflow-comparison-2026/>
- **#238** 「Each variety will, for certain, remain out of our exclusive control and carry its own agenda.」  
  判断：**部分符合**。有文献警告可进化人工智能可能超出独占控制并形成自身议程；但并非每一种人工进化都已经如此，多数系统仍受人类设定约束。  
  来源：<https://arduin.io/blog/autonomous-ai-evolution/>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC13123844/>
- **#240** 「the human ability to forecast aspects of our society, economy, and technology will steadily increase despite t…」  
  判断：**部分符合**。企业预期准确度等证据显示某些预测能力有所增强；但社会、经济与技术预测能力并非在所有方面都稳步提高，也有研究质疑预测的信息增量。  
  来源：<https://crei.cat/wp-content/uploads/2025/03/the_macroeconomics_of_data-2.pdf>；<https://papers.ssrn.com/sol3/Delivery.cfm/6944258.pdf?abstractid=6944258&mirid=1&type=2>
- **#241** 「In the future, you may fly a half hour to work.」  
  判断：**部分符合**。城市空中出行和飞行出租车仍在试验阶段；公开评估认为其不太可能成为日常通勤，“也许花半小时飞去上班”尚未实现。  
  来源：<https://aerospaceglobalnews.com/news/air-taxi-evtol-urban-air-mobility-uk/>；<https://www.dronewatch.eu/pwc-uk-evtol-aircraft-unlikely-to-replace-cars-or-trains/>
- **#244** 「others will rush in, somewhat clouding the pattern, but mostly leveling the opportunity to make any money.」  
  判断：**部分符合**。法默团队的量化预测公司确实成立并一度运作，后来相关先锋量化基金被关闭；但“其他人涌入并主要抹平赚钱机会”的完整机制在检索中只有部分旁证。  
  来源：<https://www.wired.com/1994/07/wall-st/>；<https://finanza.repubblica.it/Bloomberg/2018/09/06/millennium_shuts_down_pioneering_quant_hedge_fund-PEMYMG6TTDS201_BLF/>
- **#248** 「When our technology adapts, learns, and evolves then we will have a neo-biological civilization.」  
  判断：**部分符合**。技术已能在相当程度上适应和学习，可进化人工智能也在讨论中；但“我们就将拥有一种新生物学文明”尚未成为既成事实，条件也未完全满足。  
  来源：<https://doi.org/10.1073/pnas.2527700123>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC12452951/>
- **#251** 「Technological networks will make human culture even more ecological and evolutionary.」  
  判断：**部分符合**。有研究把技术网络中的人类文化描述得更像行星尺度的生态过程；但数字化也曾增加环境影响，人类文化并未整体变得更加生态化与进化化。  
  来源：<https://ecoevorxiv.org/repository/object/8150/download/15309/>；<https://www.annualreviews.org/content/journals/10.1146/annurev-environ-120920-100056>
- **#252** 「Engineered biology and biotechnology will eclipse the importance of mechanical technology.」  
  判断：**部分符合**。生物技术与合成生物学的重要性显著上升；但机械技术仍然关键，工程生物学尚未盖过机械技术的重要性。  
  来源：<https://setr.stanford.edu/sites/default/files/2026-01/SETR2026_02-Biotech_web-260109.pdf>；<https://www.asme.org/topics-resources/content/5-mechanical-innovations-to-watch-in-2026>
- **#253** 「Biological ways will be revered as ideal ways.」  
  判断：**部分符合**。仿生设计被广泛尊为可持续创新的重要模板；但生物学方式并未被普遍尊为唯一或当然的理想方式。  
  来源：<https://link.springer.com/article/10.1007/s13347-023-00665-0>；<https://pages.ucsd.edu/~dnorman/DNMss/Being_Analog.html>
- **#254** 「In the coming neo-biological era, all that we both rely on and fear will be more born than made.」  
  判断：**部分符合**。新生物学与生物制造话语已经出现；但我们既依赖又恐惧的事物仍主要是被造出的，而非更多地被生出的，该时代并未完整到来。  
  来源：<https://pressbooks.calstate.edu/explorationsbioanth2/chapter/17/>；<https://www.newcartographies.com/p/ai-and-the-missing-mother>

### 错误（13 条）

- **#10** 「The world of the made will soon be like the world of the born: autonomous, adaptable, and creative but, conseq…」  
  判断：**错误**。“很快”以1994年为起点，要求人造世界不久即像天生世界那样自主、可适应、有创造性并失控。1990年代末至2000年代初并未出现这种整体转变；即便到2026年，人造世界整体仍主要是被设计与管控的，公开评述也指出同期大量技术预测并未按时兑现。  
  来源：<https://frc.ri.cmu.edu/~hpm/project.archive/robot.papers/1999/SciAm.scan.html>；<https://www.wired.com/story/wired25-david-karpf-issues-tech-predictions/>
- **#12** 「distributed mind will certainly prevail.」  
  判断：**错误**。“分布式心智必将在人工心智中占据主导”未被兑现。2026年前后主导的是大型集中式模型与少数科技公司基础设施，分布式/多智能体仍是研究方向而非已占据主导的形态。  
  来源：<https://hashedout.beehiiv.com/p/who-controls-ai>；<https://towardsai.com/p/machine-learning/if-ai-is-centralized-today-it-is-not-a-law-of-nature>
- **#20** 「But ironically Ambler will never Mark Pauline hides under his Walking Thing. 36 make it to Mars because of its…」  
  判断：**错误**。预测的核心对照是：体量庞大的行走机器人因体积到不了火星，蚁群式机器人则可能到。NASA此后成功登陆的是体积逐代增大的漫游车（从Sojourner到Curiosity/Perseverance），蚁群式微型机器人并未登陆火星，该对照被事实翻转。  
  来源：<https://science.nasa.gov/resource/newest-is-biggest-three-generations-of-nasa-mars-rovers/>；<https://science.nasa.gov/resource/evolution-of-a-martian-sojourner-to-perseverance/>
- **#21** 「A flock of these microrovers will probably end up as the centerpiece of the Mars Environmental Survey schedule…」  
  判断：**错误**。1997年着陆的是MESUR Pathfinder，只部署了单辆微型漫游车Sojourner，并非“一批”微型漫游车作为核心；MESUR原计划的多着陆器网络被取消，只有Pathfinder完成。  
  来源：<https://nssdc.gsfc.nasa.gov/planetary/mesur.html>；<https://en.wikipedia.org/wiki/MESUR>；<https://science.nasa.gov/mission/mars-pathfinder/>
- **#32** 「Get artificial insects down, and artificial apes will soon follow.」  
  判断：**错误**。1994年前后昆虫级机器人（如Genghis）已存在，可视为“人工昆虫”已有基础；此后三十多年，猿级智能与敏捷的机器人并未“很快跟上”，该时间判断未兑现。  
  来源：<https://www.science.org/doi/10.1126/scirobotics.abl6334>；<https://www.thestar.com.my/tech/tech-news/2025/12/20/robotics-pioneer-says-the-field-has-lost-its-way>
- **#88** 「perhaps someday soon, also horticulture greenhouses warmed by the power plant’s waste heat.」  
  判断：**错误**。该预测以1994年起“不久”为期，指望卡伦堡在肥田之外再增加由电厂废热供暖的园艺温室。百科全书式梳理与其后综述列出的物质交换包括区域供热、渔场和制药蒸汽，但未出现该园艺温室环节，故未在“不久”内兑现。  
  来源：<https://en.wikipedia.org/wiki/Kalundborg_Eco-industrial_Park>；<https://www.technologyreview.com/1998/01/01/102232/the-greening-of-industrial-parks/>
- **#94** 「Most of the processes that will generate our wealth in the future will shrink to biological scale and resoluti…」  
  判断：**错误**。生物制造与纳米制造虽已形成专门领域，但公开报告仍把常规制造业视为产业骨干，生物制造还受成本制约；创造财富的大多数工艺并未收缩到生物尺度与分辨率。  
  来源：<https://www.bcg.com/publications/2024/breaking-the-cost-barrier-on-biomanufacturing>；<https://www.unidoindiaprogramme.org/unido-images/images/reports/IDR26.pdf>
- **#100** 「Ten years from now the wowiest products in your living room, office, or garage will be based on ideas from the…」  
  判断：**错误**。以约2004年为到期点：客厅/办公室/车库里最令人惊叹的产品主要并非源自人工生命、遗传算法等先驱会议；当年进入客厅的多为娱乐机器人等小众产品，不能代表最炫产品的主线。  
  来源：<https://www.technologyreview.com/2004/05/01/232944/humanoids-for-the-home/>；<https://www.wired.com/2004/04/this-aint-woody-allens-orb/>
- **#138** 「this version of the cashless concept slights both user and merchant; therefore it has slept on the drawing boa…」  
  判断：**错误**。作者认为会留下消费记录、因而将死在图纸上的银行智能借记卡式无现金方案，在1990年代试点中受挫，但借记卡、预付卡与账户绑定的电子支付后来成为无现金主流，该方案并未死去。  
  来源：<https://www.wired.com/1998/11/smarting-over-smartcards/>；<https://www.pewresearch.org/short-reads/2026/09/30/from-cash-to-credit-how-americans-payment-methods-have-changed-in-the-past-decade/>
- **#178** 「as early as 1995, more bits per month would be processed by parallel machines than by serial machines.」  
  判断：**错误**。希利斯打赌：到1995年并行机器每月处理的比特数将超过串行机器。公开记录表明戈登·贝尔赢了这场赌，该到期判断未兑现。  
  来源：<https://seclists.org/interesting-people/1995/Dec/58>；<https://www.newscientist.com/article/1838798-truly-madly-deeply-parallel/>
- **#185** 「Nobody will understand the evolved aviation software that will fly Danny Hillis. It will be an indecipherable …」  
  判断：**错误**。载送希利斯飞行、无人能理解却无瑕运行的演化航空软件并未出现；航空软件仍受认证与可理解性约束，公开事故也表明其并非无瑕。  
  来源：<https://www.usni.org/magazines/proceedings/2019/june/aircraft-software-ready-replace-wetware>；<https://users.ece.cmu.edu/~koopman/depend/book/rtca92.htm>
- **#186** 「No human will be able to troubleshoot the living software running Ackley’s evolved telephone system. The lines…」  
  判断：**错误**。阿克利的活计算研究仍主要是实验室工作，公用电话系统并未由无人能排查、故障时自我修复的演化活软件来运行。  
  来源：<https://www.cs.unm.edu/~ackley/>；<https://doi.org/10.1109/2.585151>
- **#205** 「After 1997, nobody ever draws Mickey again.」  
  判断：**错误**。1997年之后仍有人用手绘方式制作米老鼠，包括后来的手绘短片和漫画，‘再也没有人会手绘米老鼠’被证伪。  
  来源：<https://thedisneyblog.com/2014/07/15/disney-animated-shorts-artist-paul-rudish-draws-mickey-mouse/>；<https://www.disneyanimation.com/process/hand-drawn-animation/>

### 暂无法判断（26 条）

- **#8** 「When the union of the born and the made is complete, our fabrications will learn, adapt, heal themselves, and …」  
  判断：**暂无法判断**。该判断以“天生之物与人造之物的结合完成”为前提。公开文献仍把当今机器人描述为能力有限的单体机器，学习、适应、自修复与进化并未同时成为人造物的常规能力，前提尚未成立，故不按正误计分。  
  来源：<https://www.science.org/doi/10.1126/sciadv.adu6897>
- **#9** 「The aggregate capacity of millions of biological machines may someday match our own skill of innovation.」  
  判断：**暂无法判断**。“有朝一日”的终点未到。现有证据显示生成式AI在科学发现与创造力上结果混杂，生产率收益仍不确定，尚不能确认数百万生物机器的总体创新能力已走上赶上人类的清晰轨道。  
  来源：<https://www.nature.com/articles/s41598-025-93794-9>；<https://www.man.com/insights/the-productivity-paradox>
- **#31** 「Its descendants someday will be rodents, and someday further, as smart and nimble as apes.」  
  判断：**暂无法判断**。“有朝一日”达到啮齿类再达到猿类的智能与敏捷，终点未到。公开综述仍强调动物在运动与操作上优于机器人，尚不能确认已形成通向该水平的清晰、持续轨道。  
  来源：<https://www.science.org/doi/10.1126/scirobotics.adi9754>；<https://arxiv.org/html/2611.02510v1>
- **#43** 「The figure has risen from the deep paleologic past and is expected to keep rising.」  
  判断：**暂无法判断**。寄生比例在显生宙是否上升、以及是否将继续上升，现有研究仍缺乏对大多数野生寄生生物的长期检验，关键事实不足，不能判定持续上升的预测。  
  来源：<https://besjournals.onlinelibrary.wiley.com/doi/10.1111/1365-2656.13794>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC8450635/>
- **#45** 「A billion years from now life on Earth may be primarily social, and stuffed with 72 parasites and symbionts; a…」  
  判断：**暂无法判断**。“十亿年后”的终点远未到来，当前关于社会性、寄生共生或联盟网络的证据不足以判断该宇宙时间尺度上的结果。  
  来源：<https://www.pnas.org/doi/10.1073/pnas.2026029118>
- **#48** 「But because ecological change is so body bound, we cannot synthesize it well until we can more easily simulate…」  
  判断：**暂无法判断**。“更轻松地模拟身体和更丰富人工环境”这一前提是否已经满足、以及生态变化是否因此就能被很好地合成，现有模型进展尚不足以给出明确正误。  
  来源：<https://research.chalmers.se/publication/552537/file/552537_Fulltext.pdf>
- **#51** 「As long as the universe continues to cool down, life will build up in more curious varieties and in further mu…」  
  判断：**暂无法判断**。宇宙冷却这一前提成立，但该判断是宇宙学时间尺度上的生命积累；在可观察的地球窗口内，物种形成速率与多样性反而受人类活动威胁，无法据此判定远期命题。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC33226/>；<https://www.science.org/doi/10.1126/sciadv.adz3071>
- **#52** 「I believe the answer is that if left alone, the Earth will be solid green someday.」  
  判断：**暂无法判断**。判断以“若放任不管”为条件。人类并未停止干预地球，条件未触发，不能按正误计分。  
  来源：<https://en.wikipedia.org/wiki/Gaia_hypothesis>
- **#53** 「The galaxy may be green someday too.」  
  判断：**暂无法判断**。“银河系有朝一日变绿”属于远期胚种/生命扩散猜想，尚无足以判定方向的观察证据。  
  来源：<https://doi.org/10.1089/ast.2021.0199>
- **#54** 「But somewhat perversely I take their boast as a scientific proposition: life will fill 96 the universe.」  
  判断：**暂无法判断**。“生命将填满宇宙”被当作科学命题接受，但费米悖论与现有观测都不能证实或证伪该终点，暂无法判断。  
  来源：<https://ar5iv.labs.arxiv.org/html/1806.02404>；<https://www.sciencefocus.com/space/humans-seeded-aliens-panspermia-2>
- **#65** 「the closed systems of planets will be penetrated and shared in a type of cross-panspermia」  
  判断：**暂无法判断**。跨行星或跨恒星胚种传播在理论上被讨论，并有陨石交换的间接支持，但行星封闭系统已被穿透并共享物种这一点尚未被观测证实，属于星系时间尺度上的未决命题。  
  来源：<https://www.scientificamerican.com/article/did-life-come-from-anothe/>；<https://doi.org/10.1089/153110703321632525>
- **#67** 「Machines and machine systems, once we build them with sufficient complexity and flexibility, will also pop.」  
  判断：**暂无法判断**。“一旦建造得足够复杂和灵活”这一前提是否已经满足并不清楚；机器系统出现突然质变/跃迁的证据仍不充分，不能判定。  
  来源：<https://www.pnas.org/doi/10.1073/pnas.2300081120>
- **#85** 「People will acquire reputations on how well-trained their computers are and how well-groomed their computation…」  
  判断：**暂无法判断**。检索结果主要落在个人网络声誉、数字卫生和使用生成式AI的社会评价，没有直接证明或证伪“人们因计算机训练得好、计算生态打理得好而获得名声”。  
  来源：<https://iet.ucdavis.edu/technews/tidy-stay-safe-your-digital-hygiene-action-plan>；<https://pmc.ncbi.nlm.nih.gov/articles/PMC12088386/>
- **#125** 「its subsequent actions—will be out of our control and beyond our understanding.」  
  判断：**暂无法判断**。该条检索结果主要落在“全球意识项目”随机数实验，以及人类在人工智能时代仍保有角色的论述，与作者所说网络全球心智的行动是否超出控制与理解不能直接对应，关键事实不足。  
  来源：<https://www.global-mind.org/introduction.html>；<https://luesak.com/en/my-quotes/human-roles-in-human-world/>
- **#127** 「the quest will be to find the “I am” of the global mind, the source of its coherence.」  
  判断：**暂无法判断**。关于互联网或全球意识之“我是”与连贯性源头的讨论仍属学术与文化边缘，检索结果不能证明这已成为未来的主要求索。  
  来源：<https://wired.jp/article/sz-membership/2021/01/25/is-internet-conscious/>；<https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.755465/full>
- **#158** 「A hundred years from now nothing will keep us away from artificial cosmos cartridges we can purchase and pop i…」  
  判断：**暂无法判断**。到期点为约2094年的一百年尺度。虽已有程序化世界和模拟游戏，但‘购买人造宇宙卡匣塞进世界机器观看生物自行活过来’这一终点仍在未来，既未实现也未明确证伪。  
  来源：<https://conflict-simulations-llc.itch.io/veridian-contraption>；<https://arstechnica.com/science/2024/01/could-our-universe-be-a-simulation-how-would-we-even-tell/>
- **#159** 「and to keep our world going we will pay it.」  
  判断：**暂无法判断**。原意是人们会为维持人造世界/角色互动而向造世者付费；检索结果却落在实体基础设施投资，与主张不能对应，缺少可用核验证据。  
  来源：<https://www.aberdeenplc.com/en-gb/news/all-news/keeping-the-lights-on>；<https://www.nber.org/system/files/working_papers/w27446/w27446.pdf>
- **#160** 「Organized crime will make billions of dollars peddling crude artificial calamities—first class hurricanes or h…」  
  判断：**暂无法判断**。原意是有组织犯罪向成瘾者兜售人造模拟灾变；检索结果误打到真实天气操纵谣言，无法核验该模拟灾变黑市是否存在或已赚取数十亿美元。  
  来源：<https://www.usatoday.com/story/news/factcheck/2022/11/09/fact-check-no-patents-do-not-prove-weather-modification-real/10606592002/>；<https://www.factcheck.org/2024/10/baseless-claims-proliferate-on-hurricanes-and-weather-modification/>
- **#162** 「For the poor there will surely be underground exchanges of generic mutant beings and pilfered scenarios.」  
  判断：**暂无法判断**。检索结果主要是游戏模组和幻想设定中的变异生物交易，不能证明面向穷人的通用变异生物与盗版剧本地下市场已经出现或被证伪。  
  来源：<https://www.moddb.com/mods/x-piratez>；<https://d-infinity.net/posts/developer-blog/trade-mutant-future>
- **#167** 「Perhaps someday he wouldn’t really be able to tell the difference between them.」  
  判断：**暂无法判断**。‘有一天’无法分辨战前模拟、经监视器进行的实战和事后复盘模拟，这一终点尚未到来；现有训练模拟仍可被区分，既未实现也未明确证伪。  
  来源：<https://www.theguardian.com/uk-news/2026/aug/04/fortnite-on-steroids-the-virtual-gaming-worlds-transformed-to-train-british-soldiers>；<https://www.mscoe.org/document/beyond-the-simulation-effect-assessing-the-contradictions-and-limitations-of-wargaming-for-warfighting-readiness/>
- **#173** 「If we can’t engineer a computer that will be proud of us, we 252 may have to evolve it.」  
  判断：**暂无法判断**。条件‘无法工程出一台会为我们感到骄傲的计算机’含义隐喻，是否成立无法判定；也尚未出现必须改用进化才能得到此类计算机的事实。  
  来源：<https://www.technologyreview.com/2006/07/01/228769/technology-design-or-evolution/>；<https://edge.org/conversation/w_daniel_hillis-something-that-goes-beyond-ourselves>
- **#175** 「Two hundred years from now, artificial adaptation—tamed, measured and piped into every type of mechanical appa…」  
  判断：**暂无法判断**。到期点约为2194年的两百年尺度，人工适应是否成为社会核心组织力量既未实现也未明确证伪，按远期规则暂无法判断。  
  来源：<https://jamesm.blog/ai/the-year-2126/>；<https://syntheticcivilization.org/essays/the-500-year-ai-state/>
- **#189** 「When the phone system is run by adaptable, evolved software, there will be no correct way to run it.」  
  判断：**暂无法判断**。条件是电话系统由可适应的演化软件运行。该条件尚未成立，因此“将不再有一种正确的运行方式”不按正误计分。  
  来源：<https://trembit.com/blog/freeswitch-in-production/>；<https://signalwire.com/blog/from-freeswitch-to-swml>
- **#202** 「Maybe they’ll sell “relational fear”」  
  判断：**暂无法判断**。检索结果主要是心理学中的关系性恐惧和情绪课程，不能证明或证伪软件公司出售会渗入后续模块并随时间消退的“关系性恐惧”商品。  
  来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC9169032/>；<https://www.howtothink.ai/learn/healthy-relational-emotions-are-the-fruit-of-all-previous-em>
- **#219** 「Someday, we will create an open-ended world that can keep going, and keep creating perpetual novelty.」  
  判断：**暂无法判断**。“总有一天”创造出持续运转、不断产生永久新奇的开放世界，仍是人工生命中未解决的开放式演化问题，终点未到，也未被明确证伪。  
  来源：<https://alife-in-the-wild.github.io/artificial-life-in-the-wild.pdf>；<https://www.tim-taylor.com/papers/taylor2012exploring.pdf>
- **#232** 「also the seven trends that will bias artificial evolution when it goes marathon」  
  判断：**暂无法判断**。条件是人工进化进入“马拉松”式长期运行。现有长期遗传规划研究显示存在结构偏差与复杂动态，但七种趋势是否因此偏置其方向，缺少可直接对应的核验事实。  
  来源：<https://doi.org/10.1016/j.swevo.2024.101812>；<https://dl.acm.org/doi/10.1145/3067695.3075965>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/kelly-out-of-control-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/kelly-out-of-control-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/kelly-out-of-control-v5/audit/manual_review_2026-11-15.py`

## 说明

- 第 70 条（生物圈二号所学有朝一日将登上火星或月球）与第 72 条（有朝一日机器与生物学的差别将难以分辨）按趋势符合记录：方向有进展，但明示的 someday 终点尚未到来。
- 第 88 条（卡伦堡污泥/废热园艺温室“不久”建成）、第 100 条（十年后最令人惊叹的产品来自那些先驱会议）、第 138 条（银行借记无现金方案会夭折）、第 178 条（希利斯 1995 年并行对串行赌注）、第 185–186 条（演化航空/电话软件将被部署且无人能排查）和第 205 条（1997 年后不再手绘米老鼠）均按原期限核对，记为错误。
- 第 196 条《玩具总动员》实际于 1995 年 11 月上映，晚于书中“1994 年末”的时点，记为部分符合。
- 若干条目（如第 85、125、127、159、160、162、202 条）检索结果与核验对象不匹配，未另造来源，记为暂无法判断。
- 统计以 pipeline.py report 的 summary.json 为准；本表的加权胜率按 manual_report.py 的权重计算。

