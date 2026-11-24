# 美国国家科学技术委员会（NSTC）技术委员会《为人工智能的未来做准备》（Preparing for the Future of Artificial Intelligence，2016）：出版后预测人工核查

- 案例目录：`cases/us-nstc-preparing-for-future-of-ai-v5/`
- 出版日期：2016 年 10 月 12 日由美国总统行政办公室 / NSTC 技术委员会发布。原 PDF 下载自 obamawhitehouse.archives.gov，与队列记录 sha256 `599ead4d…` 逐字节一致（1,221,037 字节，58 页）；用 `pdftotext -enc UTF-8` 整本转为 TXT（165,443 字符，sha256 `18b5efe9…`）。观察窗口为 2016-10 至 2026-11-15。
- 截止日：2026-11-15（Asia/Shanghai）

## 方法说明

按 METHOD.md 执行。抽取：用仓库 prepare_book v5 流水线（85e6da1 工具包）把全文切成 48 块（每块 3500 字符，带 600 字符上下文；第 1—4 块为封面、致信、名单和目录，第 43—48 块为建议汇总、缩略语和参考文献）。助手逐块通读，没有用关键词筛选，按 DISCOVER_PROMPT_V5 写出模型本应返回的 JSON，再由仓库代码完成引文对齐、归属降级、去重和导入：共 24 条候选，其中 18 条为可核验预测；6 条为 unclear（2 条转述第三方预测被降级，4 条过于笼统或属机构计划），另有 3 条（机制说明、程序性事项、转述的行业预测）被排除。执行摘要与正文重复的同一判断只抽取一次；封面致信属于前言，按规则不抽取。核验：每条先写 scope，各做一次 support 与 counter 的 Exa 检索，其中 6 条（第 2、4、5、10、13、14 条）追加一轮自适应检索；只从检索返回的 URL 中选源。原文用 Exa contents 抓取存档于 data/sources（53 份，sha256），写入 data/evidence.jsonl（53 条）；理由中的数字均已在存档文本中核对。助手阅读后按“正确／趋势符合／部分符合／错误／暂无法判断”规则逐条评断，再经 pipeline.py apply assess → check → report。本稿由助手逐条对照书中原文与存档证据人工复核：先剔除非预测（出版前已发生的史实、一般规律、规范建议、反事实推演等），再对每条预测用 Exa 检索公开来源并抓取存档（`data/sources/`，sha256 记于 `data/evidence.jsonl`）核对至截止日。没有写明终点的预测按“出版日→2026-11-15”的隐含窗口判断；写明的终点未到、或条件句的前提从未出现，一律记“暂无法判断”，不强行判对错。所有来源均为实际抓取并存档的公开页面或文件；本稿未使用 DeepSeek 自动核验结论作为最终判断。

五级判断：正确／趋势符合（方向对、程度或时点未完全到位）／部分符合（一部分成立）／错误／暂无法判断。严格胜率＝正确÷可判定；加权胜率＝（正确＋0.75×趋势符合＋0.5×部分符合）÷可判定；错误率＝错误÷可判定；可判定＝前四级之和。

## 统计

候选 18 条，剔除非预测 0 条，计入 **18 条预测**，其中 **16 条可判定**。

| 判断 | 条数 |
|---|---:|
| 正确 | 8 |
| 趋势符合 | 1 |
| 部分符合 | 6 |
| 错误 | 1 |
| 暂无法判断 | 2 |

| 指标 | 数值 |
|---|---:|
| 严格胜率 | **50.0%**（8/16） |
| 加权胜率 | **73.4%** |
| 错误率 | **6.2%**（1/16） |
| 未定占比（暂无法判断/预测） | 11.1%（2/18） |

## 总体评价

这份 2016 年的白宫报告对 AI 走向的多数定性判断已经应验：私营部门成为 AI 进步的主要引擎；AI 在网络攻防中的作用明显上升；关于致命自主武器的国际讨论持续不断；AI 成为 OECD、联合国等国际议程的重要议题；无人船已用于飓风观测和渔业监控；商业实验室趋于保密后，外界监测进展更难，公众担忧上升；后续的自动化经济报告也在预告的几个月内发布。自动驾驶方面，Waymo 在运营范围内的事故率已明显低于人类，但只限少数城市，判部分符合或趋势符合。部分符合的还有：AI 带来的生产率提升只在微观层面出现，宏观数据尚未体现；机器人自动化的冲击集中在中低收入蓝领，但生成式 AI 的暴露度反而在高工资职业更高，受冲击的主要是 AI 高暴露职业里的年轻人；电子病历预测模型已普及，但质量参差；哥伦布智慧城市的自动驾驶数据远不如预期；无人机“扩展运行”规则截至截止日仍未定稿。判错的一条是高低学历工资差会扩大：2016 年后大学工资溢价持平甚至下降。“通用人工智能至少几十年内不会实现”和“智能汽车每年在全球挽救数十万生命”两条，终点未到或缺少决定性事实，记为暂无法判断。

## 逐条判断

编号为 `data/claims.jsonl` 中可判定候选的顺序号。

### 正确（8 条）

- **#2** 「UAS will offer many economic benefits」  
  判断：**正确**。无人机已形成规模化商业用途：FAA统计注册无人机837,513架、持证远程飞行员481,760名；FAA 2026年航空预测显示2025年有超过12.6万商业运营者登记新设备（2024年超过13.5万）；行业估计美国商用无人机市场2024年约14亿美元。反例是配送业务受挫：DroneUp增长停滞，沃尔玛2025年终止合作。“带来许多经济收益”这一定性判断成立。  
  来源：<https://www.faa.gov/node/26>；<https://www.researchandmarkets.com/reports/6095632/united-states-commercial-drones-market-size>；<https://www.unmannedairspace.info/uncategorized/faa-reports-lower-drone-commercial-registrations-but-stronger-forecast-growth/>；<https://vcij.org/stories/virginia-beach-tech-startup-falls-to-earth>
- **#6** 「Today’s AI has important applications in cybersecurity, and is expected to play an increasing role for both de…」  
  判断：**正确**。攻防两端的作用都在上升：Google GTIG 2025年11月首次发现PROMPTFLUX、PROMPTSTEAL等在运行中调用大模型的恶意软件；Anthropic 2025年11月披露，一个被高度确信为中国国家支持的组织操纵Claude Code，对约30个全球目标发起入侵并在少数案例中得手；SANS 2025年调查显示约一半组织已把AI用于网络安全任务。判正确。  
  来源：<https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools>；<https://www.anthropic.com/news/disrupting-AI-espionage>；<https://www.sans.org/white-papers/sans-2025-ai-survey-measuring-ai-impact-security-three-years-later>
- **#7** 「anticipates continued robust international discussion of these potential weapon systems」  
  判断：**正确**。国际讨论持续活跃：2024年12月2日联大以166票赞成、3票反对、15票弃权通过关于致命自主武器系统的第79/62号决议，并设立新的联合国讨论论坛；CCW政府专家组2025年9月仍在开会，但分歧持续（RSIS）；路透2025年5月报道主要大国抵制有约束力的规则。书中只预测讨论会持续而活跃，没有预测达成条约，判正确。  
  来源：<https://www.hrw.org/news/2024/12/05/killer-robots-un-vote-should-spur-treaty-negotiations>；<https://www.reuters.com/sustainability/society-equity/nations-meet-un-killer-robot-talks-regulation-lags-2025-05-12/>；<https://rsis.edu.sg/rsis-publication/idss/ip25095-international-regulation-of-lethal-autonomous-weapon-systems-a-long-road-ahead/>
- **#11** 「Autonomous watercraft may be much cheaper to operate than manned ships, and may someday be used for enhanced w…」  
  判断：**正确**。两类用途都已实现：NOAA 2024年飓风观测任务在大西洋、加勒比海和墨西哥湾部署12艘Saildrone，第4年任务采集768天数据、16次穿越飓风；2026年10月美国海岸警卫队给Saildrone追加850万美元合同，为新英格兰外海渔场提供海域态势感知。判正确。  
  来源：<https://www.pmel.noaa.gov/usv-hurricane/2024/index.html>；<https://www.saildrone.com/news/hyperactive-hurricane-season-provides-wealth-research-data>；<https://oceannews.com/news/defense/saildrone-voyagers-expand-coast-guard-fisheries-surveillance-in-northeast/>
- **#15** 「If competition drives commercial labs towards increased secrecy, monitoring of progress may become more diffic…」  
  判断：**正确**。前提成立：OpenAI的GPT-4技术报告以“竞争格局和大模型的安全影响”为由，不披露架构等细节；Verge指出它几乎没有公布训练数据、能耗、硬件和方法；斯坦福基础模型透明度指数中GPT-4的“数据规模”一项为0分（未披露）。后果也出现：外界监测模型的难度上升；皮尤2023年调查显示52%的美国人对AI“担忧多于兴奋”，比2022年12月的38%上升14个百分点。判正确。  
  来源：<https://www.theverge.com/2023/3/15/23640180/openai-gpt-4-launch-closed-research-ilya-sutskever-interview>；<https://crfm.stanford.edu/fmti/May-2024/company-reports/OpenAI_GPT-4.html>；<https://www.pewresearch.org/short-reads/2023/08/28/growing-public-concern-about-the-role-of-artificial-intelligence-in-daily-life/>
- **#16** 「To be sure, the private sector will be the main engine of progress on AI.」  
  判断：**正确**。斯坦福AI Index 2024：2023年产业界产出51个重要机器学习模型，学界只有15个；MIT Sloan称约70%的AI博士进入产业界，二十年前为20%。私营部门已成为AI进步的主要引擎，判正确。  
  来源：<https://hai.stanford.edu/ai-index/2024-ai-index-report?hl=en-US>；<https://mitsloan.mit.edu/ideas-made-to-matter/study-industry-now-dominates-ai-research>
- **#17** 「The White House will conduct an additional interagency study on the economic impact of automation on the econo…」  
  判断：**正确**。白宫于2016年12月20日发布《人工智能、自动化与经济》报告，距本报告约两个月；ExecutiveGov称它是10月《为人工智能的未来做准备》的后续研究。判正确。  
  来源：<https://obamawhitehouse.archives.gov/blog/2016/12/20/artificial-intelligence-automation-and-economy>；<https://www.executivegov.com/articles/white-house-releases-report-on-potential-economic-impact-of-ai-driven-automation>
- **#18** 「The U.S. Government expects AI to be a topic of increasing interest in international engagements.」  
  判断：**正确**。OECD于2019年5月通过《OECD AI原则》（首个政府间AI标准，2024年5月更新，现有47个加入方）；2024年3月21日联大未经表决通过关于“安全、可靠、值得信赖”AI的决议，这是联大首次就该领域通过决议。AI在国际交往中的分量明显上升，判正确。  
  来源：<https://oecd.ai/en/ai-principles>；<https://news.un.org/en/story/2024/03/1147831>；<https://press.un.org/en/2024/ga12588.doc.htm>

### 趋势符合（1 条）

- **#1** 「In the long run, AVs will likely save many lives by reducing driver error and increasing personal mobility」  
  判断：**趋势符合**。Waymo发表于Traffic Injury Prevention（2025）的同行评议研究基于5670万英里无人驾驶里程，显示其受伤上报、气囊弹出和疑似重伤以上碰撞率都显著低于人类基准，路口车对车受伤碰撞减少96%；Verge报道其行人受伤减少92%。这与“减少人为失误、挽救生命”的方向一致。但部署只限少数城市，Artifipedia指出结论只适用于Waymo划定的运营边界内；全社会层面“挽救大量生命”尚未出现，“长期”终点未到，判趋势符合。  
  来源：<https://pubmed.ncbi.nlm.nih.gov/40378124/>；<https://www.theverge.com/news/658952/waymo-injury-prevention-human-benchmark-study>；<https://artifipedia.com/blog/waymo-boundary>

### 部分符合（6 条）

- **#3** 「AI’s central economic effect in the short term will be the automation of tasks that could not be automated bef…」  
  判断：**部分符合**。只在微观层面应验：QJE 2025年研究5,172名客服人员，生成式AI助手使每小时解决的问题数平均提高15%。但书中说的是“短期内”提高生产率、创造财富，宏观上并未出现：Brynjolfsson等（NBER w24001，2017）指出测得的生产率增速在过去十年下降了一半；ING 2024年称AI的影响尚未在国家层面数据中显现。判部分符合。  
  来源：<https://academic.oup.com/qje/article/140/2/889/7990658>；<https://think.ing.com/articles/macro-level-productivity-gains-ai-coming-artificial-intelligence-the-effect-smaller/>；<https://www.nber.org/system/files/working_papers/w24001/w24001.pdf>
- **#4** 「the negative effect of automation will be greatest on lower-wage jobs」  
  判断：**部分符合**。机器人自动化的冲击确实集中在中低收入群体：Acemoglu与Restrepo估计每千名工人增加一台机器人，工资下降0.42%、就业人口比下降0.2个百分点，主要影响中低收入的蓝领常规体力岗位（数据期早于本书）。但AI，尤其生成式AI的冲击并不以低工资岗位为主：OpenAI等的研究发现高工资职业对大模型的暴露度通常更高；斯坦福“矿井金丝雀”研究发现AI高暴露职业中22—25岁年轻人的就业比低暴露同龄人低19%，同时没有经济整体性的岗位替代。判部分符合。  
  来源：<https://mitsloan.mit.edu/ideas-made-to-matter/a-new-study-measures-actual-impact-robots-jobs-its-significant>；<https://digitaleconomy.stanford.edu/publication/canaries-in-the-coal-mine-six-facts-about-the-recent-employment-effects-of-artificial-intelligence/>；<https://ar5iv.labs.arxiv.org/html/2303.10130>
- **#10** 「Given the current transition to electronic health records, predictive analysis of health data may play a key r…」  
  判断：**部分符合**。ONC数据显示，2024年71%的美国医院使用与电子病历整合的预测性AI（2023年为66%）；TREWS脓毒症预警的前瞻多中心研究显示，警报在3小时内被确认的患者院内死亡率相对下降18.7%。但被数百家医院采用的Epic脓毒症模型外部验证AUC只有0.63；原文点名的精准医疗和癌症研究领域，存档证据没有直接覆盖。判部分符合。  
  来源：<https://healthit.gov/data/data-briefs/hospital-trends-use-evaluation-and-governance-predictive-ai-2023-2024/>；<https://www.nature.com/articles/s41591-022-01894-0>；<https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2781307>
- **#12** 「The consensus of experts is that automated surface vehicle technology will eventually be safer than human driv…」  
  判断：**部分符合**。在Waymo的运营范围内已比人类驾驶更安全：Swiss Re对Waymo 2530万英里的保险理赔分析显示，财产损失理赔减少88%、人身伤害理赔减少92%，与配备ADAS的新车相比也分别少86%和90%。但这只是少数城市里的一家公司；特斯拉FSD仍因闯红灯、逆行等被NHTSA调查（58份报告，含14起碰撞、23人受伤）；“避免美国每年数万起死亡中的大部分”远未实现。判部分符合。  
  来源：<https://www.theverge.com/2024/12/19/24324492/waymo-injury-property-damage-insurance-data-swiss-re>；<https://www.reinsurancene.ws/waymo-shows-90-fewer-claims-than-advanced-human-driven-vehicles-swiss-re/>；<https://www.reuters.com/business/autos-transportation/us-opens-probe-into-28-million-tesla-vehicles-over-traffic-violations-when-using-2025-10-09/>
- **#13** 「vehicles in Columbus, Ohio, winner of the Department of Transportation’s $40 million Smart City Challenge in 2…」  
  判断：**部分符合**。互联汽车试点数据确实公开了：data.gov上有纽约CV试点经独立评估方处理的事件数据、坦帕CV试点的交通信息消息样本等数据集。但哥伦布的自动驾驶部署远未达到预期：最终报告显示自动驾驶接驳车在一名乘客受伤后暂停运营；市中心接驳车2018年12月至2019年9月共16,062人次乘坐；Wired称这场“革命从未到来”。“丰富的基线与交互数据”只部分实现，判部分符合。  
  来源：<https://www.smartcitiesdive.com/news/smart-columbus-ohio-smart-city-challenge-winner-lessons-learned/607999/>；<https://smartcolumbus.com/insights/2023-07-whats-next-for-smart-columbus>；<http://catalog.data.gov/?keyword=project%3A+cvp>；<https://www.wired.com/story/us-smart-city-didnt-get-much-smarter/>
- **#14** 「In particular, DOT is currently developing a Notice of Proposed Rulemaking proposing a regime for certain type…」  
  判断：**部分符合**。第一步应验：允许小型无人机在人群上方和夜间飞行的最终规则于2021年4月21日生效。但后续的“扩展运行”规则（超视距BVLOS，Part 108）只发布了提案，截至2026年11月7日仍无最终规则，自2026年7月10日起一直在白宫OIRA审查，国会设定的期限是2026年12月7日。判部分符合。  
  来源：<https://www.faa.gov/newsroom/new-drone-rules-take-effect-today>；<https://droneauthority.org/laws/part-108>；<https://dronexl.co/2026/11/10/faa-auvsi-utm-2-2-million-flights-part-108-type-certification/>

### 错误（1 条）

- **#5** 「there is a risk that AI-driven automation will increase the wage gap between less-educated and moreeducated wo…」  
  判断：**错误**。窗口内高低学历工资差没有扩大：旧金山联储2023年称大学工资溢价近年持平或下降，疫情后明显下降；明尼阿波利斯联储2025年引述研究称过去20年大学与高中学历的工资差“基本没动”；Autor、Dube等发现疫情后劳动力市场紧张使工资分布出现“意外压缩”，底部工资相对快速增长。主结果与预测方向相反，判错误。  
  来源：<https://www.frbsf.org/research-and-insights/publications/economic-letter/2023/08/falling-college-wage-premiums-by-race-and-ethnicity/>；<https://www.minneapolisfed.org/article/2025/what-happened-to-the-college-wage-premium>；<https://www.nber.org/papers/w31010>

### 暂无法判断（2 条）

- **#8** 「Smart vehicles may save hundreds of thousands of lives every year worldwide, and increase mobility for the eld…」  
  判断：**暂无法判断**。WHO《2023年全球道路安全现状报告》显示全球年道路交通死亡人数只“小幅下降”到119万；IIHS称自动紧急制动可使追尾碰撞减少50%。但存档证据不能说明智能汽车已在全球每年挽救数十万生命；原文是没有时间的“可能”，决定性事实缺失，判暂无法判断。  
  来源：<https://www.who.int/publications/i/item/9789240086517>；<https://www.iihs.org/news/detail/iihs-president-vehicle-technology-is-not-a-silver-bullet-for-safety>
- **#9** 「The current consensus of the private-sector expert community, with which the NSTC Committee on Technology conc…」  
  判断：**暂无法判断**。截至2026年11月没有公认的AGI：Science News 2025年称AGI仍是定义不清、有争议的概念；New Scientist报道，对475名AI研究者的调查中约76%认为靠扩展现有方法“不太可能”实现AGI。但80,000 Hours的综述指出各类预测群体近年都缩短了AGI时间表，2030年前实现AGI已在专家意见范围内。预测终点“至少数十年”（约2036年以后）未到，专家预期又在朝相反方向移动，判暂无法判断。  
  来源：<https://www.sciencenews.org/article/artificial-general-intelligence-ai-unclear>；<https://80000hours.org/2025/03/when-do-experts-expect-agi-to-arrive/>；<https://www.newscientist.com/article/2471759-ai-scientists-are-sceptical-that-modern-models-will-lead-to-agi/>

## 剔除的非预测

| 编号 | 原文 | 类型 | 说明 |
|---:|---|---|---|
| — | （无） | — | 候选为人工挑选，未收入非预测 |

## 文件

- 本文：`cases/us-nstc-preparing-for-future-of-ai-v5/REPORT-manual-zh.md`
- 逐条结构化结果：`cases/us-nstc-preparing-for-future-of-ai-v5/output/manual-final/results.manual.jsonl`（review_source = `manual-assistant-2026-11-15`），汇总 `output/manual-final/summary.json`
- 人工决定源文件：`cases/us-nstc-preparing-for-future-of-ai-v5/audit/manual_review_2026-11-15.py`
