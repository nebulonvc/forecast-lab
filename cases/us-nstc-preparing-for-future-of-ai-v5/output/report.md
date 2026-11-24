# 为人工智能的未来做准备：五类评估

证据截止日：2026-11-15。已处理 24/24 条全书候选；尚未处理 0 条。

累计已完成全量抽取复核 24 条；保留旧抽样抽取 0 条，两者不重复相加。

已补充扩展观点 24 条；其中 0 条仍有待确认的代指、对象或范围，已逐条标记。扩展观点不自动改变原有评估。

本轮沿用候选清单逐条核查，不保证没有漏抽。PDF记录使用PDF页码，TXT记录使用原始文本行号。扩展观点是依据所给语境的解释，原文短引文另行保留。

|类别|父记录数|
|---|---:|
|正确|8|
|趋势符合|1|
|部分符合|6|
|错误|1|
|暂无法判断|2|
|排除：非预测|6|
|排除：重复|0|
|尚未处理|0|

可判定覆盖率：16/18 = 88.9%。
绑定外部证据的预测：18/18；未绑定：0。绑定不代表证据充分或研究已完成。
“正确”占已判定记录：8/16 = 50.0%。

趋势符合 1 条单独列出，与部分符合互不重复；它表示已有持续证据支持方向，最终结果仍待验证。

以上是回顾性的记录统计，不是独立预测准确率或事前预测能力检验。部分符合不折算成 0.5 分；暂无法判断不算错误。跨章相关判断尚未完全去重，同一父记录也不因多个观察而增加命中次数。没有作者明确给出的概率，不计算 Brier 分数。

## 评估口径

正确：在列明口径和观察窗口内，主要可检验内容符合。趋势符合：已有持续客观证据支持预测方向，最终结果尚待验证。部分符合：具体分项部分成立、部分不符，或合理口径产生不同结果。错误：所评内容与已发生结果相反。暂无法判断：无法确认趋势或结果、条件不明、对象难测或证据仍不足；缺证据不能自动换成趋势符合或部分符合。

明确未来终点尚未到达时，可以评价已有趋势，并保留原期限；这类进展单列为趋势符合，不作终局正确。单次波动、未来预测数据或仅有因果解释不算趋势证据。真正的前提条件仍须确认成立，作者的因果解释不自动增加为额外触发门槛。无期限持续判断可评价已观察阶段，不能证明永久成立。出版年只是未找到发言日期时的研究起点代理，出版前已知事实不是新的预见力证据。

“不太可能”没有被转换为数值概率；低概率事件发生可记录为方向反例，不能据单次结果证明概率失准。官方声明证明立场或制度安排，不自动证明实际成效；同时出现的政策与结果不自动证明因果。

## 暂无法判断的原因

|原因类型|记录数|
|---|---:|
|证据不足|1|
|明确未来期限未到|1|
时间窗口来源：原文写出 6 条，隐含的出版年至截止日 14 条。


## 逐条结果

### 1. TXT 第 227—228 行 · 趋势符合（最终结果待验证）

记录：`txt-18b5efe9dc-000015019-000015125`

原文：In the long run, AVs will likely save many lives by reducing driver error and
increasing personal mobility

时间窗口：原文写出（In the long run）。

扩展观点（解释，非原文）：从长期看，自动驾驶汽车（AV）很可能通过减少驾驶员失误而挽救大量生命，并提高个人出行能力。


口径与范围：核验对象：从长期看，自动驾驶汽车（AV）很可能通过减少驾驶员失误而挽救大量生命，并提高个人出行能力。
判定：Waymo发表于Traffic Injury Prevention（2025）的同行评议研究基于5670万英里无人驾驶里程，显示其受伤上报、气囊弹出和疑似重伤以上碰撞率都显著低于人类基准，路口车对车受伤碰撞减少96%；Verge报道其行人受伤减少92%。这与“减少人为失误、挽救生命”的方向一致。但部署只限少数城市，Artifipedia指出结论只适用于Waymo划定的运营边界内；全社会层面“挽救大量生命”尚未出现，“长期”终点未到，判趋势符合。
限制：证据只覆盖Waymo在少数城市运营范围内的事故率，不能代表全国或全球；“长期挽救大量生命”的终点尚未到来。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-b180b8cc93b2](https://pubmed.ncbi.nlm.nih.gov/40378124/)；[ev-f2020f1a8e44](https://www.theverge.com/news/658952/waymo-injury-prevention-human-benchmark-study)；[ev-7e8f3a7c9056](https://artifipedia.com/blog/waymo-boundary)

### 2. TXT 第 228 行 · 正确

记录：`txt-18b5efe9dc-000015131-000015168`

原文：UAS will offer many economic benefits

时间窗口：隐含，从出版年 2016 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：无人机（UAS）将带来许多经济收益。


口径与范围：核验对象：无人机（UAS）将带来许多经济收益。
判定：无人机已形成规模化商业用途：FAA统计注册无人机837,513架、持证远程飞行员481,760名；FAA 2026年航空预测显示2025年有超过12.6万商业运营者登记新设备（2024年超过13.5万）；行业估计美国商用无人机市场2024年约14亿美元。反例是配送业务受挫：DroneUp增长停滞，沃尔玛2025年终止合作。“带来许多经济收益”这一定性判断成立。
限制：“经济收益”没有量化标准；以注册量、持证人数和市场规模作为收益的代理指标，市场规模来自商业咨询机构估计。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-ea5d6df62b90](https://www.faa.gov/node/26)；[ev-dc0354283301](https://www.researchandmarkets.com/reports/6095632/united-states-commercial-drones-market-size)；[ev-b160dab2e793](https://www.unmannedairspace.info/uncategorized/faa-reports-lower-drone-commercial-registrations-but-stronger-forecast-growth/)；[ev-d3b8a6d470c9](https://vcij.org/stories/virginia-beach-tech-startup-falls-to-earth)

### 3. TXT 第 256—257 行 · 部分符合

记录：`txt-18b5efe9dc-000017164-000017335`

原文：AI’s central economic effect in the short term will be the automation of tasks that could not be automated
before. This will likely increase productivity and create wealth

时间窗口：原文写出（in the short term）。

扩展观点（解释，非原文）：短期内AI的核心经济效应是把以前无法自动化的任务自动化，这很可能提高生产率、创造财富。


口径与范围：核验对象：短期内AI的核心经济效应是把以前无法自动化的任务自动化，这很可能提高生产率、创造财富。
判定：只在微观层面应验：QJE 2025年研究5,172名客服人员，生成式AI助手使每小时解决的问题数平均提高15%。但书中说的是“短期内”提高生产率、创造财富，宏观上并未出现：Brynjolfsson等（NBER w24001，2017）指出测得的生产率增速在过去十年下降了一半；ING 2024年称AI的影响尚未在国家层面数据中显现。判部分符合。
限制：微观实验证据多出现在2023年以后，不属于书中所说的“短期”；宏观生产率受多种因素影响，没有把AI的贡献单独剥离出来。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-4af313c64372](https://academic.oup.com/qje/article/140/2/889/7990658)；[ev-87fcd41036c4](https://think.ing.com/articles/macro-level-productivity-gains-ai-coming-artificial-intelligence-the-effect-smaller/)；[ev-dd361255e588](https://www.nber.org/system/files/working_papers/w24001/w24001.pdf)

### 4. TXT 第 260 行 · 部分符合

记录：`txt-18b5efe9dc-000017609-000017678`

原文：the negative effect of automation will be greatest on lower-wage jobs

时间窗口：隐含，从出版年 2016 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：自动化的负面影响将在低工资岗位上最大。


口径与范围：核验对象：自动化的负面影响将在低工资岗位上最大。
判定：机器人自动化的冲击确实集中在中低收入群体：Acemoglu与Restrepo估计每千名工人增加一台机器人，工资下降0.42%、就业人口比下降0.2个百分点，主要影响中低收入的蓝领常规体力岗位（数据期早于本书）。但AI，尤其生成式AI的冲击并不以低工资岗位为主：OpenAI等的研究发现高工资职业对大模型的暴露度通常更高；斯坦福“矿井金丝雀”研究发现AI高暴露职业中22—25岁年轻人的就业比低暴露同龄人低19%，同时没有经济整体性的岗位替代。判部分符合。
限制：机器人研究的数据期早于2016年；生成式AI的暴露度不等于实际负面影响；CEA原判断针对的是广义自动化。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-b0e8597fc51d](https://mitsloan.mit.edu/ideas-made-to-matter/a-new-study-measures-actual-impact-robots-jobs-its-significant)；[ev-c8fee811f956](https://digitaleconomy.stanford.edu/publication/canaries-in-the-coal-mine-six-facts-about-the-recent-employment-effects-of-artificial-intelligence/)；[ev-dbd8518e1be8](https://ar5iv.labs.arxiv.org/html/2303.10130)

### 5. TXT 第 261 行 · 错误

记录：`txt-18b5efe9dc-000017689-000017804`

原文：there is a risk that AI-driven automation will increase the wage gap between less-educated and moreeducated workers

时间窗口：隐含，从出版年 2016 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：AI驱动的自动化有可能扩大低学历与高学历劳动者之间的工资差距。


口径与范围：核验对象：AI驱动的自动化有可能扩大低学历与高学历劳动者之间的工资差距。
判定：窗口内高低学历工资差没有扩大：旧金山联储2023年称大学工资溢价近年持平或下降，疫情后明显下降；明尼阿波利斯联储2025年引述研究称过去20年大学与高中学历的工资差“基本没动”；Autor、Dube等发现疫情后劳动力市场紧张使工资分布出现“意外压缩”，底部工资相对快速增长。主结果与预测方向相反，判错误。
限制：原文以“风险”形式表述；工资差未扩大主要源于疫情后劳动力市场紧张，不能据此断言AI本身没有扩大差距的作用。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-e573a715cde5](https://www.frbsf.org/research-and-insights/publications/economic-letter/2023/08/falling-college-wage-premiums-by-race-and-ethnicity/)；[ev-deadbcfe498e](https://www.minneapolisfed.org/article/2025/what-happened-to-the-college-wage-premium)；[ev-f4d8f3b2ea77](https://www.nber.org/papers/w31010)

### 6. TXT 第 313—314 行 · 正确

记录：`txt-18b5efe9dc-000021795-000021942`

原文：Today’s AI has important applications in cybersecurity, and is expected to play an increasing role for both
defensive and offensive cyber measures.

时间窗口：隐含，从出版年 2016 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：AI将在网络防御和网络攻击中发挥越来越大的作用。


口径与范围：核验对象：AI将在网络防御和网络攻击中发挥越来越大的作用。
判定：攻防两端的作用都在上升：Google GTIG 2025年11月首次发现PROMPTFLUX、PROMPTSTEAL等在运行中调用大模型的恶意软件；Anthropic 2025年11月披露，一个被高度确信为中国国家支持的组织操纵Claude Code，对约30个全球目标发起入侵并在少数案例中得手；SANS 2025年调查显示约一半组织已把AI用于网络安全任务。判正确。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-f5c89038a1d5](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)；[ev-4ba107b71a07](https://www.anthropic.com/news/disrupting-AI-espionage)；[ev-714f035ce1a1](https://www.sans.org/white-papers/sans-2025-ai-survey-measuring-ai-impact-security-three-years-later)

### 7. TXT 第 328 行 · 正确

记录：`txt-18b5efe9dc-000023270-000023357`

原文：anticipates continued robust international discussion of these potential weapon systems

时间窗口：隐含，从出版年 2016 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：美国预计关于致命自主武器系统的国际讨论将持续而活跃。


口径与范围：核验对象：美国预计关于致命自主武器系统的国际讨论将持续而活跃。
判定：国际讨论持续活跃：2024年12月2日联大以166票赞成、3票反对、15票弃权通过关于致命自主武器系统的第79/62号决议，并设立新的联合国讨论论坛；CCW政府专家组2025年9月仍在开会，但分歧持续（RSIS）；路透2025年5月报道主要大国抵制有约束力的规则。书中只预测讨论会持续而活跃，没有预测达成条约，判正确。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-dee1846a3b73](https://www.hrw.org/news/2024/12/05/killer-robots-un-vote-should-spur-treaty-negotiations)；[ev-87b47c31a5d0](https://www.reuters.com/sustainability/society-equity/nations-meet-un-killer-robot-talks-regulation-lags-2025-05-12/)；[ev-305d3fe1780d](https://rsis.edu.sg/rsis-publication/idss/ip25095-international-regulation-of-lethal-autonomous-weapon-systems-a-long-road-ahead/)

### 8. TXT 第 346—348 行 · 排除：非预测

记录：`txt-18b5efe9dc-000024636-000024856`

原文：Many areas of public policy, from education and the economic safety
net, to defense, environmental preservation, and criminal justice, will see new opportunities and new
challenges driven by the continued progress of AI.

扩展观点（解释，非原文）：教育、经济安全网、国防、环境与刑事司法等众多公共政策领域，将因AI持续进步而面临新机遇和新挑战。


口径与范围：不可核验的候选（流水线 resolvable=false）
判定：抽取流水线将其降级为unclear/不可核验，按METHOD.md不进入核验。
限制：非可核验预测
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：流水线归属/可核验规则排除（原文明确；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 9. TXT 第 366—367 行 · 暂无法判断

记录：`txt-18b5efe9dc-000025839-000025982`

原文：Smart vehicles may save hundreds of thousands of lives every year worldwide, and increase
mobility for the elderly and those with disabilities.

时间窗口：隐含，从出版年 2016 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：智能汽车可能每年在全球挽救数十万生命，并提高老年人和残障人士的出行能力。


口径与范围：核验对象：智能汽车可能每年在全球挽救数十万生命，并提高老年人和残障人士的出行能力。
判定：WHO《2023年全球道路安全现状报告》显示全球年道路交通死亡人数只“小幅下降”到119万；IIHS称自动紧急制动可使追尾碰撞减少50%。但存档证据不能说明智能汽车已在全球每年挽救数十万生命；原文是没有时间的“可能”，决定性事实缺失，判暂无法判断。
限制：原文为没有时间的“可能”，并以技术被妥善开发为前提；全球死亡人数下降的原因多样，没有可归因于智能汽车的统计。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-719df150d2a8](https://www.who.int/publications/i/item/9789240086517)；[ev-6970d8da66d6](https://www.iihs.org/news/detail/iihs-president-vehicle-technology-is-not-a-silver-bullet-for-safety)

### 10. TXT 第 503—505 行 · 暂无法判断

记录：`txt-18b5efe9dc-000036723-000036899`

原文：The current consensus of the private-sector expert
community, with which the NSTC Committee on Technology concurs, is that General AI will not be
achieved for at least decades.

时间窗口：原文写出（for at least decades）。

扩展观点（解释，非原文）：通用人工智能（AGI）至少在几十年内不会实现。


口径与范围：核验对象：通用人工智能（AGI）至少在几十年内不会实现。
判定：截至2026年11月没有公认的AGI：Science News 2025年称AGI仍是定义不清、有争议的概念；New Scientist报道，对475名AI研究者的调查中约76%认为靠扩展现有方法“不太可能”实现AGI。但80,000 Hours的综述指出各类预测群体近年都缩短了AGI时间表，2030年前实现AGI已在专家意见范围内。预测终点“至少数十年”（约2036年以后）未到，专家预期又在朝相反方向移动，判暂无法判断。
限制：AGI没有公认定义；“至少数十年”的终点约在2036年以后，本窗口只能确认尚未实现。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-e84b6c57b233](https://www.sciencenews.org/article/artificial-general-intelligence-ai-unclear)；[ev-f2394e3212f0](https://80000hours.org/2025/03/when-do-experts-expect-agi-to-arrive/)；[ev-a565e6bf78fa](https://www.newscientist.com/article/2471759-ai-scientists-are-sceptical-that-modern-models-will-lead-to-agi/)

### 11. TXT 第 749—751 行 · 部分符合

记录：`txt-18b5efe9dc-000054518-000054703`

原文：Given the current
transition to electronic health records, predictive analysis of health data may play a key role across many
health domains like precision medicine and cancer research.

时间窗口：隐含，从出版年 2016 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：随着电子病历普及，健康数据的预测分析可能在精准医疗和癌症研究等许多医疗领域发挥关键作用。


口径与范围：核验对象：随着电子病历普及，健康数据的预测分析可能在精准医疗和癌症研究等许多医疗领域发挥关键作用。
判定：ONC数据显示，2024年71%的美国医院使用与电子病历整合的预测性AI（2023年为66%）；TREWS脓毒症预警的前瞻多中心研究显示，警报在3小时内被确认的患者院内死亡率相对下降18.7%。但被数百家医院采用的Epic脓毒症模型外部验证AUC只有0.63；原文点名的精准医疗和癌症研究领域，存档证据没有直接覆盖。判部分符合。
限制：证据集中在医院临床预测（如脓毒症），原文举例的精准医疗与癌症研究没有直接证据。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-85677b0b8440](https://healthit.gov/data/data-briefs/hospital-trends-use-evaluation-and-governance-predictive-ai-2023-2024/)；[ev-2bc2ae632b78](https://www.nature.com/articles/s41591-022-01894-0)；[ev-32b8248cd1dd](https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2781307)

### 12. TXT 第 797—799 行 · 正确

记录：`txt-18b5efe9dc-000057783-000057960`

原文：Autonomous watercraft may be much cheaper to
operate than manned ships, and may someday be used for enhanced weather prediction, climate
monitoring, or policing illegal fishing.

时间窗口：隐含，从出版年 2016 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：自主无人船运营成本可能远低于有人船，并可能有朝一日用于改进天气预报、气候监测或打击非法捕捞。


口径与范围：核验对象：自主无人船运营成本可能远低于有人船，并可能有朝一日用于改进天气预报、气候监测或打击非法捕捞。
判定：两类用途都已实现：NOAA 2024年飓风观测任务在大西洋、加勒比海和墨西哥湾部署12艘Saildrone，第4年任务采集768天数据、16次穿越飓风；2026年10月美国海岸警卫队给Saildrone追加850万美元合同，为新英格兰外海渔场提供海域态势感知。判正确。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-ed48963397c4](https://www.pmel.noaa.gov/usv-hurricane/2024/index.html)；[ev-35c404abf271](https://www.saildrone.com/news/hyperactive-hurricane-season-provides-wealth-research-data)；[ev-5173dbd36758](https://oceannews.com/news/defense/saildrone-voyagers-expand-coast-guard-fisheries-surveillance-in-northeast/)

### 13. TXT 第 1003—1005 行 · 部分符合

记录：`txt-18b5efe9dc-000071832-000072069`

原文：The consensus of experts is that automated surface vehicle
technology will eventually be safer than human drivers and may someday prevent most of the tens of
thousands of fatalities that occur annually on the Nation’s roads and highways.

时间窗口：隐含，从出版年 2016 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：自动驾驶地面车辆技术终将比人类驾驶员更安全，并可能有朝一日避免美国每年数万起道路死亡中的大部分。


口径与范围：核验对象：自动驾驶地面车辆技术终将比人类驾驶员更安全，并可能有朝一日避免美国每年数万起道路死亡中的大部分。
判定：在Waymo的运营范围内已比人类驾驶更安全：Swiss Re对Waymo 2530万英里的保险理赔分析显示，财产损失理赔减少88%、人身伤害理赔减少92%，与配备ADAS的新车相比也分别少86%和90%。但这只是少数城市里的一家公司；特斯拉FSD仍因闯红灯、逆行等被NHTSA调查（58份报告，含14起碰撞、23人受伤）；“避免美国每年数万起死亡中的大部分”远未实现。判部分符合。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-511eea547407](https://www.theverge.com/2024/12/19/24324492/waymo-injury-property-damage-insurance-data-swiss-re)；[ev-01e1593891d1](https://www.reinsurancene.ws/waymo-shows-90-fewer-claims-than-advanced-human-driven-vehicles-swiss-re/)；[ev-07bbe597efcf](https://www.reuters.com/business/autos-transportation/us-opens-probe-into-28-million-tesla-vehicles-over-traffic-violations-when-using-2025-10-09/)

### 14. TXT 第 1032—1033 行 · 排除：非预测

记录：`txt-18b5efe9dc-000074243-000074349`

原文：The FAA estimates that the number of UAS
registered for commercial use will exceed 600,000 by August 2017.

时间窗口：原文写出（by August 2017）。

扩展观点（解释，非原文）：FAA估计到2017年8月登记用于商业用途的无人机将超过60万架。


口径与范围：不可核验的候选（流水线 resolvable=false）
判定：抽取流水线将其降级为unclear/不可核验，按METHOD.md不进入核验。
限制：非可核验预测
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：流水线归属/可核验规则排除（原文明确；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 15. TXT 第 1100—1101 行 · 部分符合

记录：`txt-18b5efe9dc-000079497-000079679`

原文：vehicles in Columbus, Ohio, winner of the Department of Transportation’s $40 million Smart City
Challenge in 2016, will provide rich baseline and interaction data for AI researchers.

时间窗口：隐含，从出版年 2016 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：互联汽车试点和俄亥俄州哥伦布市（智慧城市挑战赛获胜者）的自动驾驶部署，将为AI研究者提供丰富的基线与交互数据。


口径与范围：核验对象：互联汽车试点和俄亥俄州哥伦布市（智慧城市挑战赛获胜者）的自动驾驶部署，将为AI研究者提供丰富的基线与交互数据。
判定：互联汽车试点数据确实公开了：data.gov上有纽约CV试点经独立评估方处理的事件数据、坦帕CV试点的交通信息消息样本等数据集。但哥伦布的自动驾驶部署远未达到预期：最终报告显示自动驾驶接驳车在一名乘客受伤后暂停运营；市中心接驳车2018年12月至2019年9月共16,062人次乘坐；Wired称这场“革命从未到来”。“丰富的基线与交互数据”只部分实现，判部分符合。
限制：没有找到AI研究者实际使用这些数据的量化证据；只核对了数据是否公开和部署规模。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-7f5a77a19497](https://www.smartcitiesdive.com/news/smart-columbus-ohio-smart-city-challenge-winner-lessons-learned/607999/)；[ev-e23cc66be152](https://smartcolumbus.com/insights/2023-07-whats-next-for-smart-columbus)；[ev-18f9a69c6ec7](http://catalog.data.gov/?keyword=project%3A+cvp)；[ev-41d612780c9b](https://www.wired.com/story/us-smart-city-didnt-get-much-smarter/)

### 16. TXT 第 1118—1120 行 · 部分符合

记录：`txt-18b5efe9dc-000081067-000081283`

原文：In particular, DOT is currently developing a Notice of Proposed Rulemaking proposing a regime for
certain types of “micro UAS” to conduct operations over people, with a rule on expanded operations
expected to follow.

时间窗口：隐含，从出版年 2016 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：DOT正在起草允许某些微型无人机在人群上方飞行的规章提案，随后还将出台关于扩展运行的规章。


口径与范围：核验对象：DOT正在起草允许某些微型无人机在人群上方飞行的规章提案，随后还将出台关于扩展运行的规章。
判定：第一步应验：允许小型无人机在人群上方和夜间飞行的最终规则于2021年4月21日生效。但后续的“扩展运行”规则（超视距BVLOS，Part 108）只发布了提案，截至2026年11月7日仍无最终规则，自2026年7月10日起一直在白宫OIRA审查，国会设定的期限是2026年12月7日。判部分符合。
限制：把2016年语境下的“expanded operations”理解为超视距等扩展运行；人群上方飞行规则本身也比原拟的“微型无人机”范围更宽。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-f98db055d151](https://www.faa.gov/newsroom/new-drone-rules-take-effect-today)；[ev-20849dae0ca2](https://droneauthority.org/laws/part-108)；[ev-931b1520729a](https://dronexl.co/2026/11/10/faa-auvsi-utm-2-2-million-flights-part-108-type-certification/)

### 17. TXT 第 1195—1196 行 · 排除：非预测

记录：`txt-18b5efe9dc-000085760-000085887`

原文：DOT intends for the guidance and the model state policy to be routinely updated as new data are learned
and research completed.

扩展观点（解释，非原文）：DOT打算随新数据和研究成果定期更新自动驾驶指南与州政策范本。


口径与范围：不可核验的候选（流水线 resolvable=false）
判定：抽取流水线将其降级为unclear/不可核验，按METHOD.md不进入核验。
限制：非可核验预测
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：流水线归属/可核验规则排除（原文明确；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 18. TXT 第 1225 行 · 排除：非预测

记录：`txt-18b5efe9dc-000087837-000087915`

原文：half believed it is at least 50 percent likely to be achieved by the year 2040

时间窗口：原文写出（by the year 2040）。

扩展观点（解释，非原文）：受访AI研究者中半数认为到2040年实现人类水平通用AI的可能性至少为50%。


口径与范围：不可核验的候选（流水线 resolvable=false）
判定：抽取流水线将其降级为unclear/不可核验，按METHOD.md不进入核验。
限制：非可核验预测
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：流水线归属/可核验规则排除（原文明确；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 19. TXT 第 1272—1274 行 · 正确

记录：`txt-18b5efe9dc-000090447-000090594`

原文：If competition drives
commercial labs towards increased secrecy, monitoring of progress may become more difficult, and
public concern may increase.

时间窗口：隐含，从出版年 2016 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：如果竞争促使商业实验室更加保密，监测AI进展会更难，公众担忧可能上升。


口径与范围：核验对象：如果竞争促使商业实验室更加保密，监测AI进展会更难，公众担忧可能上升。
判定：前提成立：OpenAI的GPT-4技术报告以“竞争格局和大模型的安全影响”为由，不披露架构等细节；Verge指出它几乎没有公布训练数据、能耗、硬件和方法；斯坦福基础模型透明度指数中GPT-4的“数据规模”一项为0分（未披露）。后果也出现：外界监测模型的难度上升；皮尤2023年调查显示52%的美国人对AI“担忧多于兴奋”，比2022年12月的38%上升14个百分点。判正确。
限制：条件式预测：以商业实验室趋于保密为前提，前提已成立；公众担忧上升有多重原因，不能全部归因于保密。
观察终点：2026-11-15；条件状态：satisfied。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-dae7f8b80a54](https://www.theverge.com/2023/3/15/23640180/openai-gpt-4-launch-closed-research-ilya-sutskever-interview)；[ev-ad87b7d9e817](https://crfm.stanford.edu/fmti/May-2024/company-reports/OpenAI_GPT-4.html)；[ev-ec96701d1740](https://www.pewresearch.org/short-reads/2023/08/28/growing-public-concern-about-the-role-of-artificial-intelligence-in-daily-life/)

### 20. TXT 第 1341 行 · 正确

记录：`txt-18b5efe9dc-000095935-000096008`

原文：To be sure, the private sector will be the main engine of progress on AI.

时间窗口：隐含，从出版年 2016 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：私营部门将成为AI进步的主要引擎。


口径与范围：核验对象：私营部门将成为AI进步的主要引擎。
判定：斯坦福AI Index 2024：2023年产业界产出51个重要机器学习模型，学界只有15个；MIT Sloan称约70%的AI博士进入产业界，二十年前为20%。私营部门已成为AI进步的主要引擎，判正确。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-e247d3c81729](https://hai.stanford.edu/ai-index/2024-ai-index-report?hl=en-US)；[ev-6e2e85577bae](https://mitsloan.mit.edu/ideas-made-to-matter/study-industry-now-dominates-ai-research)

### 21. TXT 第 1527—1529 行 · 正确

记录：`txt-18b5efe9dc-000108850-000109034`

原文：The White House will conduct an additional interagency study
on the economic impact of automation on the economy and recommended policy responses, to be
published in the coming months.

时间窗口：原文写出（in the coming months）。

扩展观点（解释，非原文）：白宫将另行开展跨部门研究，评估自动化对经济的影响并提出政策建议，并在未来几个月内发布。


口径与范围：核验对象：白宫将另行开展跨部门研究，评估自动化对经济的影响并提出政策建议，并在未来几个月内发布。
判定：白宫于2016年12月20日发布《人工智能、自动化与经济》报告，距本报告约两个月；ExecutiveGov称它是10月《为人工智能的未来做准备》的后续研究。判正确。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2016-12-20；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-57e2f6aaffdf](https://obamawhitehouse.archives.gov/blog/2016/12/20/artificial-intelligence-automation-and-economy)；[ev-0fe52c368bfe](https://www.executivegov.com/articles/white-house-releases-report-on-potential-economic-impact-of-ai-driven-automation)

### 22. TXT 第 1821—1822 行 · 正确

记录：`txt-18b5efe9dc-000130311-000130408`

原文：The U.S. Government
expects AI to be a topic of increasing interest in international engagements.

时间窗口：隐含，从出版年 2016 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：美国政府预计AI将在国际交往中受到越来越多的关注。


口径与范围：核验对象：美国政府预计AI将在国际交往中受到越来越多的关注。
判定：OECD于2019年5月通过《OECD AI原则》（首个政府间AI标准，2024年5月更新，现有47个加入方）；2024年3月21日联大未经表决通过关于“安全、可靠、值得信赖”AI的决议，这是联大首次就该领域通过决议。AI在国际交往中的分量明显上升，判正确。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-e69ee8da00c6](https://oecd.ai/en/ai-principles)；[ev-ff9f94045baa](https://news.un.org/en/story/2024/03/1147831)；[ev-4c5191a6f080](https://press.un.org/en/2024/ga12588.doc.htm)

### 23. TXT 第 1959—1960 行 · 排除：非预测

记录：`txt-18b5efe9dc-000140439-000140516`

原文：Ultimately, these applications may turn out to be the most
important for DoD.

扩展观点（解释，非原文）：非致命的AI应用最终可能对国防部最为重要。


口径与范围：不可核验的候选（流水线 resolvable=false）
判定：抽取流水线将其降级为unclear/不可核验，按METHOD.md不进入核验。
限制：非可核验预测
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：流水线归属/可核验规则排除（原文明确；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 24. TXT 第 1963 行 · 排除：非预测

记录：`txt-18b5efe9dc-000140734-000140831`

原文：Many new capabilities may soon be possible, and quickly able to be developed and operationalized.

扩展观点（解释，非原文）：许多新的（自主武器）能力可能很快成为可能，并能迅速开发和投入使用。


口径与范围：不可核验的候选（流水线 resolvable=false）
判定：抽取流水线将其降级为unclear/不可核验，按METHOD.md不进入核验。
限制：非可核验预测
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：流水线归属/可核验规则排除（原文明确；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

## 证据登记

哈希校验只证明本地保存内容未改变。检索摘录与完整原始文件会按证据记录注明；两者均不能代替对来源与命题对应关系的判断。

- [ev-b180b8cc93b2](https://pubmed.ncbi.nlm.nih.gov/40378124/)；资料日期：2025-05-16；覆盖：Comparison of Waymo Rider-Only crash rates by crash type to human benchmarks at 56.7 million miles。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-f2020f1a8e44](https://www.theverge.com/news/658952/waymo-injury-prevention-human-benchmark-study)；资料日期：2025-05-01；覆盖：Waymo is still good at avoiding serious distraction and death after 56.7 million miles | The Verge。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-7e8f3a7c9056](https://artifipedia.com/blog/waymo-boundary)；资料日期：2026-07-30；覆盖：220 million miles, inside a boundary Waymo drew。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-ea5d6df62b90](https://www.faa.gov/node/26)；资料日期：未确定；覆盖：FAA By the Numbers | Federal Aviation Administration。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-dc0354283301](https://www.researchandmarkets.com/reports/6095632/united-states-commercial-drones-market-size)；资料日期：未确定；覆盖：United States Commercial Drones Market Size and Share - Outlook Report, Forecast Trends and Growth Analysis (2025-2034)。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-b160dab2e793](https://www.unmannedairspace.info/uncategorized/faa-reports-lower-drone-commercial-registrations-but-stronger-forecast-growth/)；资料日期：2026-08-09；覆盖：FAA reports lower drone commercial registrations but stronger forecast growth - Unmanned airspace。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-d3b8a6d470c9](https://vcij.org/stories/virginia-beach-tech-startup-falls-to-earth)；资料日期：2026-06-04；覆盖：Virginia Beach tech startup falls to earth — Virginia Center for Investigative Journalism。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-4af313c64372](https://academic.oup.com/qje/article/140/2/889/7990658)；资料日期：2025-02-04；覆盖：Generative AI at Work* | The Quarterly Journal of Economics | Oxford Academic。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-87fcd41036c4](https://think.ing.com/articles/macro-level-productivity-gains-ai-coming-artificial-intelligence-the-effect-smaller/)；资料日期：2024-04-12；覆盖：AI productivity gains may be smaller than you’re expecting | ING THINK。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-dd361255e588](https://www.nber.org/system/files/working_papers/w24001/w24001.pdf)；资料日期：未确定；覆盖：Artificial Intelligence and the Modern Productivity Paradox: A Clash of Expectations and Statistics。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-b0e8597fc51d](https://mitsloan.mit.edu/ideas-made-to-matter/a-new-study-measures-actual-impact-robots-jobs-its-significant)；资料日期：2020-07-29；覆盖：A new study measures the actual impact of robots on jobs. It’s significant. | MIT Sloan。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-c8fee811f956](https://digitaleconomy.stanford.edu/publication/canaries-in-the-coal-mine-six-facts-about-the-recent-employment-effects-of-artificial-intelligence/)；资料日期：2025-10-13；覆盖：Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence - Stanford Digital Economy Lab。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-dbd8518e1be8](https://ar5iv.labs.arxiv.org/html/2303.10130)；资料日期：未确定；覆盖：[2303.10130] GPTs are GPTs: An Early Look at the Labor Market Impact Potential of Large Language Models。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-e573a715cde5](https://www.frbsf.org/research-and-insights/publications/economic-letter/2023/08/falling-college-wage-premiums-by-race-and-ethnicity/)；资料日期：2023-08-28；覆盖：Falling College Wage Premiums by Race and Ethnicity - San Francisco Fed。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-deadbcfe498e](https://www.minneapolisfed.org/article/2025/what-happened-to-the-college-wage-premium)；资料日期：2025-09-08；覆盖：What happened to the college wage premium? | Federal Reserve Bank of Minneapolis。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-f4d8f3b2ea77](https://www.nber.org/papers/w31010)；资料日期：2023-03-06；覆盖：The Unexpected Compression: Competition at Work in the Low Wage Labor Market | NBER。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-f5c89038a1d5](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)；资料日期：2025-11-05；覆盖：GTIG AI Threat Tracker: Advances in Threat Actor Usage of AI Tools | Google Cloud Blog。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-4ba107b71a07](https://www.anthropic.com/news/disrupting-AI-espionage)；资料日期：2025-11-13；覆盖：Disrupting an AI-orchestrated cyber espionage campaign \ Anthropic。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-714f035ce1a1](https://www.sans.org/white-papers/sans-2025-ai-survey-measuring-ai-impact-security-three-years-later)；资料日期：2025-09-03；覆盖：SANS 2025 AI Survey: Measuring AI’s Impact on Security Three Years Later | SANS Institute。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-dee1846a3b73](https://www.hrw.org/news/2024/12/05/killer-robots-un-vote-should-spur-treaty-negotiations)；资料日期：2024-12-05；覆盖：Killer Robots: UN Vote Should Spur Treaty Negotiations | Human Rights Watch。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-87b47c31a5d0](https://www.reuters.com/sustainability/society-equity/nations-meet-un-killer-robot-talks-regulation-lags-2025-05-12/)；资料日期：2025-05-12；覆盖：Nations meet at UN for 'killer robot' talks as regulation lags | Reuters。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-305d3fe1780d](https://rsis.edu.sg/rsis-publication/idss/ip25095-international-regulation-of-lethal-autonomous-weapon-systems-a-long-road-ahead/)；资料日期：2025-10-01；覆盖：IP25095 | International Regulation of Lethal Autonomous Weapon Systems: A Long Road Ahead | RSIS。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-719df150d2a8](https://www.who.int/publications/i/item/9789240086517)；资料日期：2023-12-13；覆盖：Global status report on road safety 2023。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-6970d8da66d6](https://www.iihs.org/news/detail/iihs-president-vehicle-technology-is-not-a-silver-bullet-for-safety)；资料日期：2023-03-07；覆盖：IIHS president: Vehicle technology is not a silver bullet for safety。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-e84b6c57b233](https://www.sciencenews.org/article/artificial-general-intelligence-ai-unclear)；资料日期：2025-03-11；覆盖：The meaning of artificial general intelligence remains unclear。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-f2394e3212f0](https://80000hours.org/2025/03/when-do-experts-expect-agi-to-arrive/)；资料日期：2025-03-21；覆盖：When do experts expect AGI to arrive?。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-a565e6bf78fa](https://www.newscientist.com/article/2471759-ai-scientists-are-sceptical-that-modern-models-will-lead-to-agi/)；资料日期：2025-03-14；覆盖：AI scientists are sceptical that modern models will lead to AGI | New Scientist。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-85677b0b8440](https://healthit.gov/data/data-briefs/hospital-trends-use-evaluation-and-governance-predictive-ai-2023-2024/)；资料日期：2025-09-17；覆盖：Hospital Trends in the Use, Evaluation, and Governance of Predictive AI, 2023-2024 - ONC Health IT Research & Analysis。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-2bc2ae632b78](https://www.nature.com/articles/s41591-022-01894-0)；资料日期：2022-07-21；覆盖：Prospective, multi-site study of patient outcomes after implementation of the TREWS machine learning-based early warning system for sepsis | Nature Medicine。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-32b8248cd1dd](https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2781307)；资料日期：2021-06-21；覆盖：External Validation of a Widely Implemented Proprietary Sepsis Prediction Model in Hospitalized Patients | Critical Care Medicine | JAMA Internal Medicine | JAM。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-ed48963397c4](https://www.pmel.noaa.gov/usv-hurricane/2024/index.html)；资料日期：未确定；覆盖：NOAA's USV Observations of Atlantic Hurricanes for Improved Intensity Forecasts - 2024 Mission。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-35c404abf271](https://www.saildrone.com/news/hyperactive-hurricane-season-provides-wealth-research-data)；资料日期：2024-12-18；覆盖：NOAA and Saildrone’s 4th annual hurricane mission collected 768 days of data over 27,000 nautical miles sailed with 16 hurricane intercepts.。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-5173dbd36758](https://oceannews.com/news/defense/saildrone-voyagers-expand-coast-guard-fisheries-surveillance-in-northeast/)；资料日期：2026-10-22；覆盖：Saildrone Voyagers Expand Coast Guard Fisheries Surveillance In Northeast。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-511eea547407](https://www.theverge.com/2024/12/19/24324492/waymo-injury-property-damage-insurance-data-swiss-re)；资料日期：2024-12-19；覆盖：Waymo still doing better than humans at preventing injuries and property damage | The Verge。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-01e1593891d1](https://www.reinsurancene.ws/waymo-shows-90-fewer-claims-than-advanced-human-driven-vehicles-swiss-re/)；资料日期：2024-12-24；覆盖：Waymo shows 90% fewer claims than advanced human-driven vehicles: Swiss Re - Reinsurance News。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-07bbe597efcf](https://www.reuters.com/business/autos-transportation/us-opens-probe-into-28-million-tesla-vehicles-over-traffic-violations-when-using-2025-10-09/)；资料日期：2025-10-09；覆盖：US probes driver assistance software in 2.9 million Tesla vehicles over traffic violations | Reuters。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-7f5a77a19497](https://www.smartcitiesdive.com/news/smart-columbus-ohio-smart-city-challenge-winner-lessons-learned/607999/)；资料日期：2021-10-11；覆盖：6 questions with Smart Columbus on lessons since program’s conclusion | Smart Cities Dive。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-e23cc66be152](https://smartcolumbus.com/insights/2023-07-whats-next-for-smart-columbus)；资料日期：2023-07-11；覆盖：Smart Columbus spent $50 million on transportation. What worked and what's next? — Smart Columbus。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-18f9a69c6ec7](http://catalog.data.gov/?keyword=project%3A+cvp)；资料日期：未确定；覆盖：Catalog - Data.gov。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-41d612780c9b](https://www.wired.com/story/us-smart-city-didnt-get-much-smarter/)；资料日期：2021-06-28；覆盖：America’s ‘Smart City’ Didn’t Get Much Smarter | WIRED。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-f98db055d151](https://www.faa.gov/newsroom/new-drone-rules-take-effect-today)；资料日期：2021-04-21；覆盖：New Drone Rules Take Effect Today | Federal Aviation Administration。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-20849dae0ca2](https://droneauthority.org/laws/part-108)；资料日期：2026-06-13；覆盖：Part 108 Drone Rules Explained (2026): Current BVLOS Status | Drone Authority。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-931b1520729a](https://dronexl.co/2026/11/10/faa-auvsi-utm-2-2-million-flights-part-108-type-certification/)；资料日期：2026-11-11；覆盖：FAA Touts 2.2 Million UTM Drone Flights at AUVSI. Part 108 Still Waits。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-dae7f8b80a54](https://www.theverge.com/2023/3/15/23640180/openai-gpt-4-launch-closed-research-ilya-sutskever-interview)；资料日期：2023-03-15；覆盖：OpenAI co-founder on company’s past approach to openly sharing research: ‘We were wrong’ | The Verge。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-ad87b7d9e817](https://crfm.stanford.edu/fmti/May-2024/company-reports/OpenAI_GPT-4.html)；资料日期：未确定；覆盖：OpenAI: GPT-4。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-ec96701d1740](https://www.pewresearch.org/short-reads/2023/08/28/growing-public-concern-about-the-role-of-artificial-intelligence-in-daily-life/)；资料日期：2023-08-28；覆盖：US public concern grows over role of AI in daily life | Pew Research Center。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-e247d3c81729](https://hai.stanford.edu/ai-index/2024-ai-index-report?hl=en-US)；资料日期：未确定；覆盖：The 2024 AI Index Report | Stanford HAI。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-6e2e85577bae](https://mitsloan.mit.edu/ideas-made-to-matter/study-industry-now-dominates-ai-research)；资料日期：2023-05-18；覆盖：Study: Industry now dominates AI research | MIT Sloan。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-57e2f6aaffdf](https://obamawhitehouse.archives.gov/blog/2016/12/20/artificial-intelligence-automation-and-economy)；资料日期：2016-12-20；覆盖：Artificial Intelligence, Automation, and the Economy | whitehouse.gov。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-0fe52c368bfe](https://www.executivegov.com/articles/white-house-releases-report-on-potential-economic-impact-of-ai-driven-automation)；资料日期：2016-12-21；覆盖：White House Report Examines Potential Economic Impact of AI-Driven Automation。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-e69ee8da00c6](https://oecd.ai/en/ai-principles)；资料日期：未确定；覆盖：AI Principles Overview - OECD.AI。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-ff9f94045baa](https://news.un.org/en/story/2024/03/1147831)；资料日期：2024-03-21；覆盖：General Assembly adopts landmark resolution on artificial intelligence | UN News。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-4c5191a6f080](https://press.un.org/en/2024/ga12588.doc.htm)；资料日期：2024-03-21；覆盖：General Assembly Adopts Landmark Resolution on Steering Artificial Intelligence towards Global Good, Faster Realization of Sustainable Development | UN Meetings。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
