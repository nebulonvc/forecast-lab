# 超预测：五类评估

证据截止日：2026-11-25。已处理 13/13 条全书候选；尚未处理 0 条。

累计已完成全量抽取复核 13 条；保留旧抽样抽取 0 条，两者不重复相加。

已补充扩展观点 13 条；其中 0 条仍有待确认的代指、对象或范围，已逐条标记。扩展观点不自动改变原有评估。

本轮沿用候选清单逐条核查，不保证没有漏抽。PDF记录使用PDF页码，TXT记录使用原始文本行号。扩展观点是依据所给语境的解释，原文短引文另行保留。

|类别|父记录数|
|---|---:|
|正确|4|
|趋势符合|1|
|部分符合|4|
|错误|0|
|暂无法判断|0|
|排除：非预测|4|
|排除：重复|0|
|尚未处理|0|

可判定覆盖率：9/9 = 100.0%。
绑定外部证据的预测：9/9；未绑定：0。绑定不代表证据充分或研究已完成。
“正确”占已判定记录：4/9 = 44.4%。

趋势符合 1 条单独列出，与部分符合互不重复；它表示已有持续证据支持方向，最终结果仍待验证。

以上是回顾性的记录统计，不是独立预测准确率或事前预测能力检验。部分符合不折算成 0.5 分；暂无法判断不算错误。跨章相关判断尚未完全去重，同一父记录也不因多个观察而增加命中次数。没有作者明确给出的概率，不计算 Brier 分数。

## 评估口径

正确：在列明口径和观察窗口内，主要可检验内容符合。趋势符合：已有持续客观证据支持预测方向，最终结果尚待验证。部分符合：具体分项部分成立、部分不符，或合理口径产生不同结果。错误：所评内容与已发生结果相反。暂无法判断：无法确认趋势或结果、条件不明、对象难测或证据仍不足；缺证据不能自动换成趋势符合或部分符合。

明确未来终点尚未到达时，可以评价已有趋势，并保留原期限；这类进展单列为趋势符合，不作终局正确。单次波动、未来预测数据或仅有因果解释不算趋势证据。真正的前提条件仍须确认成立，作者的因果解释不自动增加为额外触发门槛。无期限持续判断可评价已观察阶段，不能证明永久成立。出版年只是未找到发言日期时的研究起点代理，出版前已知事实不是新的预见力证据。

“不太可能”没有被转换为数值概率；低概率事件发生可记录为方向反例，不能据单次结果证明概率失准。官方声明证明立场或制度安排，不自动证明实际成效；同时出现的政策与结果不自动证明因果。

## 暂无法判断的原因

|原因类型|记录数|
|---|---:|
时间窗口来源：原文写出 5 条，隐含的出版年至截止日 6 条。


## 逐条结果

### 1. TXT 第 445—447 行 · 部分符合

记录：`txt-f97f35ccdb-000031803-000032008`

原文：Big leaps in computing power and continued refinement of
forecasting models may nudge the limits a little further into the future but those
advances gradually get harder and the payoffs shrink toward zero.

时间窗口：原文写出（into the future）。

扩展观点（解释，非原文）：尽管算力的大幅跃升和气象预报模型的持续改进，可能会将天气预报准确性的时间跨度上限略微推向更远的未来，但这些预报改进会逐渐变得越来越困难，其准确率提升的边际收益也将趋近于零。

指代展开：the limits → 天气预报准确性改进的时间跨度上限；上下文依据：There may be limits to such improvements
指代展开：those advances → 通过算力跃升和预报模型持续改进推进天气预报准确性上限的进展；上下文依据：Big leaps in computing power and continued refinement of forecasting models may nudge the limits a little further into the future

口径与范围：观察窗口为 2015 年出版年至 2026-11-25 截止日（原文仅写 into the future，未给明确终点）。对象为全球中期及延伸期天气预报（传统高分辨率 NWP 与机器学习天气预报 MLWP），可观察口径为两项分指标：(1) 中纬度日常天气可预报性时间上限是否仍受内在混沌边界制约（如 ~10–15 天实用/内在上限与缩小初始误差的边际收益）；(2) 算力跃升与模型改进带来的准确率提升是否持续变难且边际收益趋近于零。
判定：2015–2026 年间的气象实证呈现两项分指标的实质分化：一方面，高分辨率模式研究（Zhang et al. 2019）证实中纬度日常天气存在内在动力学可预报性上限，当前实用上限约 10 天，即便将初始误差缩小一个数量级也最多延长约 5 天（至约 15 天），且小尺度天气改进空间更小，最新 AI 集合模型 GenCast 亦仍运行在 15 天中期跨度内，符合“上限难以无限外推、存在收益递减边界”的判断；另一方面，2022–2025 年机器学习天气预报范式（如 GenCast 在 97.4% 的 1,320 项指标上超越 ECMWF ENS 且耗时仅 8 分钟）带来了跨越式而非趋零停滞的准确率与算力效率跃升，且对 2021 年太平洋西北热浪的深度学习敏感性分析将特定大尺度事件的可预报改进探至约 23 天，与“模型改进单调变难、收益趋近于零”的预期存在阶段性反差。
限制：“into the future”无明确终点，本评估仅代表 2015–2026-11-25 观察窗口内的实绩，不断言更长期未来不存在最终渐近上限；此外，arXiv:2406.05019 的 23 天结果属于特定极端热浪个例的最优扰动研究而非日常业务预报常态，且三项来源均为学术论文摘要而非完整业务年报连续序列。
观察终点：2024-06-07；条件状态：satisfied。
思考方法：基于天气系统作为非线性混沌系统（蝴蝶效应）的本质特征，推断预报时距越长、混沌扰动放大越剧烈，从而推导出算力与模型改进的边际收益递减趋势。（原文明确；方法有效性未由此证明）。
证据：[ev-vbatch-0001-01](https://doi.org/10.1175/jas-d-18-0269.1)；[ev-vbatch-0001-02](https://arxiv.org/abs/2312.15796)；[ev-vbatch-0001-03](https://arxiv.org/abs/2406.05019)

### 2. TXT 第 648—650 行 · 排除：非预测

记录：`txt-f97f35ccdb-000048472-000048738`

原文：And machine learning, in combination with burgeoning human-machine interactions that
feed the learning process, promises far more fundamental advances to come. “It’s going to
be one of these exponential curves that we’re kind of at the bottom of now,” Ferrucci said.

时间窗口：隐含，从出版年 2015 到截止日 2026-11-25。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：IBM Watson 首席工程师大卫·费鲁奇认为，机器学习与不断增长、反哺学习过程的人机交互相结合，将在2015年之后带来更加根本性的技术进步，且目前正处于指数级增长曲线的底部。

指代展开：Ferrucci → 在人工智能领域工作了三十年的专家费鲁奇（Ferrucci）；上下文依据：Ferrucci—who has worked in artificial intelligence for thirty years—is more cautious today.
指代展开：It → 机器学习与人机交互结合所带来的技术进步趋势；上下文依据：And machine learning, in combination with burgeoning human-machine interactions that feed the learning process, promises far more fundamental advances to come.

口径与范围：按 v5 规则归类为非可评分预测或重复条目，不计入命中率分母。
判定：抽取阶段识别为非预测、不可解或重复候选，依 METHOD.md 保留审计记录并排除。
限制：排除条目不参与准确度计分。
观察终点：未形成可判定观察终点；条件状态：unconditional。
思考方法：基于计算能力与模式识别能力当前快速提升以及人机交互反哺机器学习的趋势进行外推（原文明确；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 3. TXT 第 657—658 行 · 排除：非预测

记录：`txt-f97f35ccdb-000049320-000049434`

原文：Even with computers making galloping
advances, the sort of forecasting that superforecasters do is a long way off.

扩展观点（解释，非原文）：作者认为，即便计算机技术持续突飞猛进，计算机要完成类似人类超预测者所做的复杂主观判断类预测（例如结合人物意图、性格与政治因果动态判断俄罗斯领导人未来是否会互换职位）仍然距离很遥远。

指代展开：the sort of forecasting that superforecasters do → 需要综合人物意图、性格与复杂因果动态并作出主观判断的预测任务；上下文依据：The latter requires the computer to make an informed guess about the intentions of Vladimir Putin, the character of Dmitri Medvedev, and the causal dynamics of Russian politics, and then integrate that information into a judgment call.

口径与范围：按 v5 规则归类为非可评分预测或重复条目，不计入命中率分母。
判定：抽取阶段识别为非预测、不可解或重复候选，依 METHOD.md 保留审计记录并排除。
限制：排除条目不参与准确度计分。
观察终点：未形成可判定观察终点；条件状态：unconditional。
思考方法：任务机制拆解：区分历史事实检索与复杂因果推理及主观判断的难度差异（原文明确；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 4. TXT 第 661—664 行 · 部分符合

记录：`txt-f97f35ccdb-000049560-000049820`

原文：Machines may get better at “mimicking human meaning,” and thereby better at
predicting human behavior, but “there’s a difference between mimicking and reflecting
meaning and originating meaning,” Ferrucci said. That’s a space human judgment will
always occupy.

时间窗口：原文写出（always）。

扩展观点（解释，非原文）：大卫·费鲁奇与作者认为，未来机器可能会越来越擅长“模仿人类意义”并由此提高预测人类行为的能力，但模仿、反映意义与原创意义存在本质区别，原创意义这一空间将始终由人类判断占据。

指代展开：That → 原创意义（originating meaning）的领域；上下文依据：there’s a difference between mimicking and reflecting meaning and originating meaning

口径与范围：观察窗口为 2015 年出版年至 2026-11-25 截止日（原文后半句含永久终点 always，尚未到期）。对象为人工智能/大语言模型系统相对人类判断的表现，采用两项透明回顾性代理口径：(1) 机器在模仿人类语义与预测人类行为上的能力是否显著提升（以大规模行为预测基础模型 Centaur 为代表）；(2) 人类判断在开放世界预测与深层语义理解/原创意义空间中是否仍保持优势或独占地位（以 ForecastBench 动态预测基准、LeSC 细粒度词义基准及意义中介抽象研究为代理）。
判定：在 2015–2026 年观察窗口内，该复合命题呈现分项实现与边界分化并存：首先，前半句“机器更擅长模仿人类意义并提升预测人类行为能力”已获直接实证支持，例如基于大语言模型与 1,000 万次人类选择微调的 Centaur 能在任意自然语言表达的实验中优于既有认知模型预测人类行为；其次，截至 2024–2025 年，ForecastBench 实证显示人类专家在真实未来事件预测上仍显著优于顶尖 LLM（p < 0.001），且 LeSC 基准显示 GPT-4 在非常见词义理解上仍落后人类 3.9%，支持人类判断在观察期内尚未被取代；但与此同时，2026 年 conlang 任务实证（arXiv:2609.34187）反驳了强“随机鹦鹉”假说、证明统计学习已能涌现“意义中介抽象”，且“原创意义”缺乏统一可测定义、终点“always（始终）”永未到期，故无法判为终局正确。
限制：“originating meaning（原创意义）”属于哲学与认知科学边界概念，本评估以真实世界预测基准、细粒度语义理解和意义中介抽象任务作为回顾性可观察代理；由于原文包含永久时间词“always”，截止日前的阶段性证据无法证实人类将永久独占该空间，且 AI 能力仍在快速演进。
观察终点：2026-09-28；条件状态：unconditional。
思考方法：概念与能力边界区分：区分模式模仿/反映意义与原创意义的本质差异（原文明确；方法有效性未由此证明）。
证据：[ev-vbatch-0001-04](https://arxiv.org/abs/2410.20268)；[ev-vbatch-0001-05](https://arxiv.org/abs/2409.19839)；[ev-vbatch-0001-06](https://arxiv.org/abs/2405.05741)；[ev-vbatch-0001-07](https://arxiv.org/abs/2609.34187)

### 5. TXT 第 665—669 行 · 正确

记录：`txt-f97f35ccdb-000049824-000050184`

原文：In forecasting, as in other fields, we will continue to see human judgment being
displaced—to the consternation of white-collar workers—but we will also see more and
more syntheses, like “freestyle chess,” in which humans with computers compete as
teams, the human drawing on the computer’s indisputable strengths but also occasionally
overriding the computer.

时间窗口：隐含，从出版年 2015 到截止日 2026-11-25。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：作者预测，在预测领域以及其他行业中，人类主观判断将继续被计算机与算法取代（令白领工作者感到不安），但与此同时，越来越多类似“自由式国际象棋”的人机协作团队模式将会涌现——人类借助计算机不可争议的优势，并在必要时推翻计算机的结论。


口径与范围：隐含观察窗口2015年至2026-11-25（implicit_publication_to_cutoff，非作者写明终点），在预测领域（地缘政治/真实事件预测竞赛与实验）及其他白领/知识工作领域，检验两项方向性变化：（1）算法与AI继续替代部分人类判断并冲击白领岗位/任务；（2）更多“人类+计算机”协作团队模式（人类利用机器优势并保留人工调整/推翻权）持续涌现。
判定：2015至2026年间两项预测方向均已明确发生：在白领与知识工作领域，在线劳动力平台大数据记录到与LLM核心能力高度重合子市场的显著替代效应与收缩（ev-vbatch-0002-05），美国CPS数据（截至2026年6月）亦显示高AI暴露度办公与客服岗位中30岁以下从业者显著减少约8%/标准差（ev-vbatch-0002-04）；在人机协作融合方面，预测领域涌现了IARPA混合预测竞赛的SAGE人机融合平台（1,085名预测者，ev-vbatch-0002-01）与LLM辅助人类预测实践（N=991，准确率提升24%-28%，ev-vbatch-0002-02），企业白领服务场景亦大规模引入人机协作助手（如5,172名客服引入生成式AI助手使效率平均提升15%，ev-vbatch-0002-06）。
限制：窗口为出版年至截止日的隐含代理窗口，且两项趋势均存在重要边界：美国CPS数据显示高暴露职业总体就业未出现净坍塌，30-49岁大学学历群体反而获得更多全职岗位（ev-vbatch-0002-04）；此外，大规模元分析表明在AI已强于人类的决策任务中，人机混合（含人工干预推翻）的平均表现反而逊于纯AI（ev-vbatch-0002-03），说明人机团队虽广泛涌现但并非在所有任务中均占优。
观察终点：2026-06-30；条件状态：unconditional。
思考方法：跨领域类比（自由式国际象棋）与当前算法替代人类判断趋势的外推（原文明确；方法有效性未由此证明）。
证据：[ev-vbatch-0002-01](https://arxiv.org/abs/2412.10981)；[ev-vbatch-0002-02](https://arxiv.org/abs/2402.07862)；[ev-vbatch-0002-03](https://arxiv.org/abs/2405.06087)；[ev-vbatch-0002-04](https://arxiv.org/abs/2507.08244)；[ev-vbatch-0002-05](https://arxiv.org/abs/2308.05201)；[ev-vbatch-0002-06](https://arxiv.org/abs/2304.11771)

### 6. TXT 第 670—672 行 · 部分符合

记录：`txt-f97f35ccdb-000050265-000050421`

原文：To reframe the man-versus-machine dichotomy, combinations of
Garry Kasparov and Deep Blue may prove more robust than pure-human or pure-
machine approaches.

时间窗口：隐含，从出版年 2015 到截止日 2026-11-25。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：作者认为，跳出“人与机器对立”的二分法来看，类似卡斯帕罗夫与“深蓝”组合的人机协作预测方法，在未来可能会被证明比纯人类或纯机器方法更具稳健性。

指代展开：combinations of Garry Kasparov and Deep Blue → 人类专家与计算机协同工作的人机结合预测方法；上下文依据：syntheses, like “freestyle chess,” in which humans with computers compete as teams

口径与范围：隐含观察窗口2015年至2026-11-25（implicit_publication_to_cutoff，非作者写明终点），在预测与专业判断任务的实证研究与公开基准测试（地缘政治预测竞赛、LLM辅助预测、零售需求判断预测及跨领域人机协作元分析）中，检验“人机组合（类似卡斯帕罗夫+深蓝）”是否比“纯人类”和“纯机器”方法更具稳健性/更高准确率。
判定：2015至2026年的实证证据显示不同任务类型与能力相对优势下存在实质分化：在开放性地缘政治与综合事件预测中，纯LLM仍落后于人类专家（ForecastBench，p<0.001，ev-vbatch-0002-08），而人机混合系统（如IARPA HFC的SAGE平台与LLM辅助预测实验）显著优于纯人类基线（ev-vbatch-0002-01、ev-vbatch-0002-02），且在人类强于AI或内容创作任务中人机组合带来正向收益（ev-vbatch-0002-03）；但相反，覆盖超100项实验的Nature Human Behaviour元分析发现，总体上人机组合显著逊于单独表现最佳的一方，尤其在决策类任务以及AI本身已强于人类的任务中人机组合反致表现下降（ev-vbatch-0002-03），零售判断性预测实验亦显示统计模型支持未能一致提升人类或LLM的预测精度（ev-vbatch-0002-07）。
限制：原句使用试探性措辞（may prove more robust）且未限定单一指标，评估采用跨任务准确率与预测误差作为稳健性的回顾性代理；此外，元分析（ev-vbatch-0002-03）主要汇总2020-2023年受控实验，随着2025-2026年推理模型演进，具体任务上的相对优势边界仍在动态变化。
观察终点：2025-02-28；条件状态：unconditional。
思考方法：基于自由式国际象棋中人机组合有时能击败纯人类和纯机器的经验类比（原文明确；方法有效性未由此证明）。
证据：[ev-vbatch-0002-01](https://arxiv.org/abs/2412.10981)；[ev-vbatch-0002-02](https://arxiv.org/abs/2402.07862)；[ev-vbatch-0002-03](https://arxiv.org/abs/2405.06087)；[ev-vbatch-0002-07](https://arxiv.org/abs/2312.06941)；[ev-vbatch-0002-08](https://arxiv.org/abs/2409.19839)

### 7. TXT 第 676—678 行 · 部分符合

记录：`txt-f97f35ccdb-000050672-000050884`

原文：Ferrucci sees light at the end of this long dark tunnel: “I think it’s going to get
stranger and stranger” for people to listen to the advice of experts whose views are
informed only by their subjective judgment.

时间窗口：隐含，从出版年 2015 到截止日 2026-11-25。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：大卫·费鲁奇预测（作者在下文表示怀疑他是对的，即表示赞同），随着人们对人类认知局限和心理偏差的认识加深以及计算机辅助的发展，仅靠个人主观判断发言的“专家大师模式”将逐渐过时，人们听信此类纯粹主观专家建议的做法会变得越来越奇怪。

指代展开：this long dark tunnel → 仅依赖专家主观论战的“大师模式”主导政策辩论的现状；上下文依据：What Ferrucci does see becoming obsolete is the guru model that makes so many policy debates so puerile

口径与范围：隐含观察窗口为2015年（出版年代理）至2026-11-25（非作者写明终点）；以美国皮尤研究中心2024–2025年社交媒体“新闻意见领袖”受众调查作为公共政策/舆论场主观评论接受度的回顾性代理，以Wavestone 2024年全球高管数据与AI调查及2024年地缘政治预测综述作为企业与专业预测领域数据/算法辅助替代纯主观判断的回顾性代理。
判定：2015–2025年观察窗口内，原预测在公共舆论场与专业/企业决策场出现实质分化：在大型企业与专业预测领域，数据与分析已成为首要投资重点且人机协同显著提升预测表现（支持方向），但企业全面落实数据驱动思维仍面临阻力且地缘政治预测仍由人类主导；而在原文直接指向的公共评论与政策辩论“大师模式”中，依赖个人主观观点与评述的独立新闻意见领袖不仅未过时，反而持续覆盖21%的美国成年人及38%的18–29岁青年（其中77%无新闻机构背景），与“听信纯主观建议会越来越奇怪”相反。
限制：原文未定义精确指标与截止日期，本评估采用美国公众媒体消费调查、大型企业高管调查与地缘政治预测综述作为回顾性代理，主要覆盖美国与跨国大企业而未穷尽全球所有决策场景；结果仅评估行为与采纳趋势，不验证认知偏差心理学机制。
观察终点：2025-08-24；条件状态：unconditional。
思考方法：基于近一二十年心理学对人类认知偏差的广泛揭示及人机结合趋势进行推断（原文明确；方法有效性未由此证明）。
证据：[ev-vbatch-0003-01](https://www.pewresearch.org/journalism/fact-sheet/news-influencers-fact-sheet/)；[ev-vbatch-0003-02](https://www.pewresearch.org/journalism/2024/11/18/americas-news-influencers/)；[ev-vbatch-0003-03](https://www.wavestone.com/en/insight/data-ai-executive-leadership-survey-2024/)；[ev-vbatch-0003-04](https://pubmed.ncbi.nlm.nih.gov/37642169/)

### 8. TXT 第 2251—2254 行 · 趋势符合（最终结果待验证）

记录：`txt-f97f35ccdb-000174383-000174622`

原文：And as EPJ and other studies have shown, human
cognitive systems will never be able to forecast turning points in the lives of individuals
or nations several years into the future—and heroic searches for superforecasters won’t
change that.

时间窗口：原文写出（never）。

扩展观点（解释，非原文）：根据作者此前的《专家政治判断》（EPJ）研究及其他实证研究，人类认知系统永远无法预测未来数年个人或国家生活中的转折点，即使大力搜寻超级预测者，也无法改变人类认知系统无法预测此类多年期转折点的局限。

指代展开：EPJ → 作者此前开展的《专家政治判断》（Expert Political Judgment）预测锦标赛及研究；上下文依据：my earlier EPJ tournament
指代展开：that → 人类认知系统永远无法预测未来数年个人或国家生活中的转折点；上下文依据：cognitive systems will never be able to forecast turning points in the lives of individuals

口径与范围：观察区间为2015年至2026-11-25，保留原文永久否定终点future_time_text="never"；以2020年PNAS“脆弱家庭挑战赛”160支团队对个体6年期生活结果的预测表现为个人多年期转折代理，以2025年《国际预测杂志》存在性风险说服锦标赛（XPT）中89名超级预测者对长期罕见风险的表现及2025年ForecastBench动态基准为国家/宏观预测与超级预测者能力边界代理，同时检索是否存在推翻“永远无法预测”的多年期转折点确切反例。
判定：趋势符合，最终结果待验证。2015–2025年的多项实证研究持续支持原文关于多年期转折点存在认知与可预测性硬上限的判断：在个人层面，Salganik等（2020）证明即便动用高质量纵向队列数据与160支团队的机器学习模型，对个体6年后生活结果的预测准确度依然很低；在宏观/国家与长期重大风险层面，Karger与Tetlock等（2025）指出即便汇聚高技能超级预测者，在预判罕见或史无前例的远期事件时仍存在明显局限；尽管ForecastBench（2025）显示人类专家预测者在结构化中短期未来问题上显著优于顶尖大语言模型，但并未出现能稳定提前数年预测个人或国家重大转折点的反例。因原文断言为永久性的“never”，当前阶段性实证尚不能构成终局正确。
限制：原文时间终点为开放性的“never”，2015–2025年观察期无法排除遥远未来技术或认知突破的可能；“脆弱家庭挑战赛”主要检验基于调查数据的算法模型而非纯人类直觉，XPT主要聚焦存在性风险且长期问题尚未完成最终结算，二者均作为对应对象的回顾性代理；同时不将预测结果受限本身等同于证明作者的生理极限类比机制。
观察终点：2025-02-28；条件状态：satisfied。
思考方法：依据《专家政治判断》（EPJ）及其他实证研究的长期预测准确率结论，并类比人类视觉系统的生理极限，外推人类认知系统在多年期转折点预测上的硬性上限（原文明确；方法有效性未由此证明）。
证据：[ev-vbatch-0003-05](https://pubmed.ncbi.nlm.nih.gov/32229555/)；[ev-vbatch-0003-06](https://ideas.repec.org/a/eee/intfor/v41y2025i2p499-516.html)；[ev-vbatch-0003-07](https://arxiv.org/abs/2409.19839)

### 9. TXT 第 4739—4740 行 · 排除：非预测

记录：`txt-f97f35ccdb-000364191-000364283`

原文：It’s also why I wouldn’t be at all surprised to see her ultimately become a
superforecaster.

时间窗口：原文写出（ultimately）。

扩展观点（解释，非原文）：基于参赛者安妮（Anne）在预测锦标赛中展现出的毅力与持续反思学习的态度，作者认为如果看到安妮最终成为一名超级预测者，自己一点也不会感到惊讶。

指代展开：her → 安妮（Anne），预测锦标赛中尚未成为超级预测者但展现毅力的参赛者；上下文依据：Anne isn’t a superforecaster, at least not yet, but her results are still impressive.
指代展开：I → 作者（菲利普·泰特洛克）；上下文依据：“I am always trying to grow, to learn, to change,” she wrote me.

口径与范围：按 v5 规则归类为非可评分预测或重复条目，不计入命中率分母。
判定：抽取阶段识别为非预测、不可解或重复候选，依 METHOD.md 保留审计记录并排除。
限制：排除条目不参与准确度计分。
观察终点：未形成可判定观察终点；条件状态：unconditional。
思考方法：基于个体在预测锦标赛中表现出的毅力（grit）、成长心态与持续反思行为进行潜力推断（原文明确；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 10. TXT 第 5250—5251 行 · 正确

记录：`txt-f97f35ccdb-000403379-000403477`

原文：These tools won’t replace intelligence analysts or the officials who synthesize their
conclusions.

时间窗口：隐含，从出版年 2015 到截止日 2026-11-25。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：群体预测与极端化算法等预测聚合工具不会取代情报分析师，也不会取代负责综合情报分析师结论的决策官员。

指代展开：These tools → 群体预测与极端化算法等预测聚合工具；上下文依据：the extremizing algorithm I mentioned in chapter 4

口径与范围：隐含观察窗口（出版年代理2015年至案例截止日2026-11-25，非作者明示终点）。评估对象为美国情报界（IC）中的人类情报分析师及负责综合研判结论的决策官员，检验群体预测、极端化算法及预测市场等预测聚合工具是否取代了上述人类岗位，或仅作为辅助工具嵌入现有情报分析流程。
判定：在2015年至2026年的观察窗口内，群体预测、预测市场与人机混合预测聚合工具并未取代情报分析师或负责综合研判的决策官员。RAND 2026年5月关于情报界分析规范（ICD 203）的研究明确指出，预测工具并不取代涉密情报报告或专家分析，而是作为服务于分析师与既有分析流程的辅助支持功能；同时，IARPA 内部运行多年的情报界预测市场（ICPM）亦于2020年被取消，而非替代传统情报分析体系。
限制：公开文献无法披露美国情报界涉密内部编制与具体岗位增减细节；同时，IARPA 混合预测竞赛（HFC）的 SAGE 研究（2024年12月）表明人机混合预测在扩大问题覆盖面时具备减少部分人力投入的潜力，但截至2026-11-25仍属辅助性人机协同而非对分析师或综合官员的替代。本结论仅限于2015年至2026-11-25已观察窗口，不构成永久有效断言。
观察终点：2026-05-31；条件状态：unconditional。
思考方法：基于高层决策机制的职能边界判断，认为首席执行官始终需要由聪明的顾问团队环绕并综合情报，因此预测工具只能作为廉价辅助输入而非人类分析师的替代品。（原文明确；方法有效性未由此证明）。
证据：[ev-vbatch-0004-01](https://www.rand.org/content/dam/rand/pubs/perspectives/PEA3400/PEA3490-2/RAND_PEA3490-2.pdf)；[ev-vbatch-0004-02](https://atlasinstitute.org/from-analysis-to-probability-modernizing-intelligence-forecasts/)；[ev-vbatch-0004-03](https://arxiv.org/html/2412.10981v1)

### 11. TXT 第 6418—6419 行 · 正确

记录：`txt-f97f35ccdb-000494603-000494729`

原文：Balancing it all out, count me as cautiously optimistic that my work may contribute to an
evidence-based forecasting movement.

时间窗口：隐含，从出版年 2015 到截止日 2026-11-25。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：综合权衡各方阻力与积极进展后，菲利普·泰特洛克审慎乐观地认为，他在本书中阐述的预测研究工作可能会促成一场循证预测运动的兴起与发展。

指代展开：me → 本书作者菲利普·泰特洛克（Philip E. Tetlock）；上下文依据：In 1976 I was a clueless twenty-two-year-old Canadian
指代展开：my work → 菲利普·泰特洛克在本书中阐述的预测研究工作；上下文依据：the research outlined in this book

口径与范围：隐含观察窗口（出版年代理2015年至案例截止日2026-11-25，非作者明示终点）。评估对象为菲利普·泰特洛克及其《超预测》/Good Judgment Project（GJP）研究工作是否对一场“循证预测运动”（evidence-based forecasting movement）的兴起与机构化做出实际推动，同时核查该运动在政府情报界与传统机构采纳中的现实阻力与边界。
判定：2015年至2026年间，泰特洛克及其 GJP/《超预测》研究直接促成了以量化概率、Brier Score 评估与公开/结构化预测锦标赛为核心的循证预测生态兴起。泰特洛克作为首席科学家共同创立的 Forecasting Research Institute（FRI）在第一代预测研究基础上推进 AI、生物安全与地缘政治大规模预测研究，Good Judgment Inc. 将该循证方法论商业化并向外部团队培训推广，RAND 等主流政策智库亦建立了 RAND Forecasting Initiative（RFI）并明确引用《超预测》作为最佳实践标准。
限制：循证预测运动并未全面取代主流媒体评论或彻底制度化进入美国情报界日常运作——例如 IARPA 情报界预测市场（ICPM）于2020年被取消，RAND 2026年5月报告也指出开源可信度核验负担与聚合概率可追溯性仍是情报界采纳的现实障碍；此外 FRI 与 Good Judgment Inc. 官网页未标明发表日期（元数据缺省）且具机构自述属性，但作者原话仅审慎乐观地预期其工作“可能促成一场循证预测运动”，并未断言全面普及，故上述阻力构成范围限制而非反驳。
观察终点：2026-05-31；条件状态：unconditional。
思考方法：历史类比与制度趋势综合权衡（类比循证医学、循证政策、慈善评估与体育数据分析的演进，并结合美国情报界资助IARPA锦标赛及国家情报总监对评分机制的兴趣进行综合判断）（原文明确；方法有效性未由此证明）。
证据：[ev-vbatch-0004-04](https://forecastingresearch.org/about)；[ev-vbatch-0004-05](https://goodjudgment.com/about/)；[ev-vbatch-0004-01](https://www.rand.org/content/dam/rand/pubs/perspectives/PEA3400/PEA3490-2/RAND_PEA3490-2.pdf)；[ev-vbatch-0004-02](https://atlasinstitute.org/from-analysis-to-probability-modernizing-intelligence-forecasts/)

### 12. TXT 第 7367—7368 行 · 正确

记录：`txt-f97f35ccdb-000560007-000560121`

原文：And his statement captures why the IC is
unlikely to invest in cultivating its own superforecasters any time soon.

时间窗口：原文写出（any time soon）。

扩展观点（解释，非原文）：鉴于前国家情报委员会主席托马斯·芬加（Thomas Fingar）认为“预测不是也不应是战略分析的目标”，美国情报界（IC）短期内不太可能投入资源培养自己的超级预测者。

指代展开：his statement → 托马斯·芬加（Thomas Fingar）关于“预测不是也不应是战略分析的目标”的言论；上下文依据：Prediction is not—and should not be—the goal of strategic analysis
指代展开：the IC → 美国情报界（Intelligence Community）；上下文依据：urged the IC to conduct IARPA-style experiments

口径与范围：评估2015年出版后至2026年5月公开记录窗口内（对应原文“any time soon”的短期及后续延续期），美国情报界（IC，含ODNI、NIC、IARPA、DIA等）是否投入资源在内部系统性培养自有超级预测者（如建立常态化概率评分追踪、内部精英预测者选拔与培养机制）。回顾性代理指标为IC内部预测平台（如ICPM）的存续与制度化采纳情况、概率评分在IC分析中的普及度及后续内部平台落地情况。
判定：2015年后十余年间的多源公开证据一致表明，美国情报界并未投资建立培养自有超级预测者的常态化内部体系。Lawfare（2021）指出严格概率推理与评分追踪在IC仍属罕见，DARPA/IARPA早年十余项预测项目几乎均在特朗普时期终止；ICPM承建商Cultivate Labs（2025）与国安记者Sasha Ingber（2026）的一手调查进一步证实，IC内部预测市场ICPM于2018年被NIC退回IARPA并于2020年关闭，运行期间从未进入PDB或NIE且截至2025-2026年无活跃内部替代项目，推动DIA赞助INFER也未落地。
限制：反面与边界情况在于：IARPA于2017年仍启动了为期四年的混合预测竞赛（HFC）并与Good Judgment Inc.等合作，但该研发项目依赖外部承包商与数千名外部志愿者而非在IC内部培养自有超级预测者；此外ICPM在2015-2020年间曾维持有限运行。公开证据无法完全排除涉密渠道中存在未披露的小规模内部试点，且结果符合不单独证明Thomas Fingar所代表的战略分析文化是唯一因果机制。
观察终点：2026-05-26；条件状态：unconditional。
思考方法：依据情报界资深官员托马斯·芬加公开表态“预测不应是战略分析的目标”，推断情报界内部文化与认知惯性使其短期内不太可能投入资源培养自身的超级预测者（原文明确；方法有效性未由此证明）。
证据：[ev-vbatch-0005-01](https://www.lawfaremedia.org/article/how-us-government-can-learn-see-future)；[ev-vbatch-0005-02](https://sashaingber.substack.com/p/exclusive-the-life-and-death-of-the)；[ev-vbatch-0005-03](https://www.cultivatelabs.com/posts/how-the-u-s-intelligence-community-s-prediction-market-made-analysis-better)；[ev-vbatch-0005-04](https://intelligencecommunitynews.com/iarpa-launches-hybrid-forecasting-competition/)

### 13. TXT 第 7902—7904 行 · 排除：非预测

记录：`txt-f97f35ccdb-000595463-000595660`

原文：This line of research
implies that even superforecasters won’t be able to beat deep liquid markets in which
many very smart and well-capitalized traders are relentlessly second-guessing each other.

扩展观点（解释，非原文）：基于主动管理共同基金无法持续跑赢被动指数基金的既有研究，作者推断即便经过验证测试，超级预测者也无法在深度、高流动性且聚集了大量高智商、资金雄厚交易者持续相互博弈的市场中持续跑赢市场。

指代展开：This line of research → 关于主动管理共同基金无法稳定跑赢被动指数基金（如标普500）的研究证据（包括Jeff Sommer 2015年3月15日《纽约时报》文章）；上下文依据：See Jeff Sommer, “How Many Mutual Funds Routinely Rout the Market? Zero,” New York Times, March 15, 2015.

口径与范围：按 v5 规则归类为非可评分预测或重复条目，不计入命中率分母。
判定：抽取阶段识别为非预测、不可解或重复候选，依 METHOD.md 保留审计记录并排除。
限制：排除条目不参与准确度计分。
观察终点：未形成可判定观察终点；条件状态：unconditional。
思考方法：从主动管理共同基金长期难以持续跑赢被动指数基金的经验研究外推至超级预测者在深度高流动性市场中的表现边界（原文明确；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

## 证据登记

哈希校验只证明本地保存内容未改变。检索摘录与完整原始文件会按证据记录注明；两者均不能代替对来源与命题对应关系的判断。

- [ev-vbatch-0001-01](https://doi.org/10.1175/jas-d-18-0269.1)；资料日期：2019-04-01；覆盖：中纬度日常天气可预报性上限与缩小初始误差边际收益的高分辨率全球模式研究（ECMWF 9-km 与 NGGPS 3-km）。限制：该研究基于2019年前的传统物理数值模式（ECMWF 9 km 与 NGGPS 3 km），未涵盖2022年后兴起的机器学习概率集合预报范式；结论聚焦中纬度日常确定性天气预报。
- [ev-vbatch-0001-02](https://arxiv.org/abs/2312.15796)；资料日期：2024-05-01；覆盖：Google DeepMind 概率扩散天气模型 GenCast 与 ECMWF ENS 在 15 天全球中期集合预报上的精度与速度对比。限制：GenCast 仍运行在15天中期预报跨度内，证明的是模型范式革新带来新一轮精度与效率跃升，并不意味着已突破两周以外的日常确定性混沌上限；预印本摘要未列出分年评估截止日。
- [ev-vbatch-0001-03](https://arxiv.org/abs/2406.05019)；资料日期：2024-06-07；覆盖：基于 GraphCast 深度学习敏感性分析对 2021 年太平洋西北极端热浪可预报性上限的实证检验。限制：该结果为针对 2021 年 6 月太平洋西北极端热浪的回顾性个例最优初始扰动实验，代表特定大尺度事件的理论可预报上限，而非日常业务预报的普遍水平。
- [ev-vbatch-0001-04](https://arxiv.org/abs/2410.20268)；资料日期：2025-04-28；覆盖：基于大语言模型微调的人类认知基础模型 Centaur 在 160 项心理学实验、1,000 万次选择上预测人类行为的实证表现。限制：Centaur 证明的是机器通过自然语言表征与大规模人类选择数据微调后在实验场景中预测人类行为的能力跃升，无法直接证明机器具备人类式的“原创意义”或主体意向性。
- [ev-vbatch-0001-05](https://arxiv.org/abs/2409.19839)；资料日期：2025-02-28；覆盖：无数据泄漏动态真实世界预测基准 ForecastBench 上人类专家预测者与顶尖大语言模型的对比评测。限制：该基准衡量的是真实世界事件概率预测准确率，作为“人类判断优势”的回顾性代理指标；且评测反映的是 2024–2025 年模型水平，无法证明永久（always）结论。
- [ev-vbatch-0001-06](https://arxiv.org/abs/2405.05741)；资料日期：2024-05-09；覆盖：细粒度词义理解基准 LeSC 上主流闭源与开源大语言模型相对人类在非常见词义理解上的表现差距。限制：该研究主要测试 2024 年前后的 GPT-4 等模型在词汇语义理解基准上的表现，不能直接等同于“原创意义”的哲学命题，也不排除后续模型在该具体基准上缩小差距。
- [ev-vbatch-0001-07](https://arxiv.org/abs/2609.34187)；资料日期：2026-09-28；覆盖：在颠覆表层统计模式的人造语言任务上检验大语言模型“意义中介抽象”能力与强随机鹦鹉假说的实证研究。限制：该研究反驳的是“LLM 只能做表层模式复述”的强随机鹦鹉假说，并指出生成仍受表层合理性强烈约束，尚未证明 LLM 已具备人类式自主价值创造或完全取代人类判断的原创意义能力。
- [ev-vbatch-0002-01](https://arxiv.org/abs/2412.10981)；资料日期：2024-12-14；覆盖：IARPA混合预测竞赛（HFC）中SAGE人机混合地缘政治预测系统的实证结果（1,085名预测者、398道真实问题、历时8个月）。限制：该实验主要比较人机混合系统与纯人类基线，未将纯机器模型单独作为独立对照测试全部开放性地缘政治问题。
- [ev-vbatch-0002-02](https://arxiv.org/abs/2402.07862)；资料日期：2024-08-22；覆盖：大语言模型助手辅助人类预测的预注册随机实验（N=991，6道真实预测题）。限制：论文指出单题离群值对效应量有显著影响，且对照组使用较弱的非数值预测模型而非独立纯前沿LLM，稳健性仍需进一步检验。
- [ev-vbatch-0002-03](https://arxiv.org/abs/2405.06087)；资料日期：2024-10-29；覆盖：人机组合表现的系统综述与元分析（超过100项实验研究、300余个效应量，发表于Nature Human Behaviour）。限制：纳入研究主要来自2020-2023年间的受控实验任务，涵盖决策与内容创作等多种任务，并非全部聚焦长期地缘政治预测。
- [ev-vbatch-0002-04](https://arxiv.org/abs/2507.08244)；资料日期：2026-11-20；覆盖：美国人口普查局CPS劳动力数据（截至2026年6月）对AI能力演进与白领/办公职业就业影响的实证研究。限制：数据仅覆盖美国劳动力市场，且总体就业未出现净下降，表明替代效应目前主要集中在入门级与特定办公/客服岗位而非全面白领裁员。
- [ev-vbatch-0002-05](https://arxiv.org/abs/2308.05201)；资料日期：2026-06-25；覆盖：头部在线劳动力平台大数据对生成式AI引发的知识工作替代效应与市场收缩的实证研究。限制：样本来自在线自由职业平台而非全部传统企业正式雇员，主要反映与LLM核心能力高度重合的认知型子市场。
- [ev-vbatch-0002-06](https://arxiv.org/abs/2304.11771)；资料日期：2024-11-06；覆盖：5,172名客服人员分阶段引入生成式AI对话助手的真实企业实地研究。限制：聚焦单一企业的客户支持岗位，且对经验最丰富、技能最高员工的质量呈现小幅下降，反映人机协作效果因技能分层而异。
- [ev-vbatch-0002-07](https://arxiv.org/abs/2312.06941)；资料日期：2024-05-17；覆盖：零售需求判断性预测对照实验（123名人类预测者与5个LLM在统计预测模型支持下的表现比较）。限制：聚焦零售促销场景的定量时间序列需求预测，且LLM版本为2023-2024年初代模型（GPT-4、GPT-3.5、Bard、Bing、Llama2）。
- [ev-vbatch-0002-08](https://arxiv.org/abs/2409.19839)；资料日期：2025-02-28；覆盖：ForecastBench动态预测基准（1,000道无数据泄漏的真实未来事件题，比较专家人类、公众与前沿LLM）。限制：该版论文评估的是2024-2025年初的前沿LLM与人类专家在200道随机子集问题上的对照，未单独单列同一题集上人机混合团队的同步得分。
- [ev-vbatch-0003-01](https://www.pewresearch.org/journalism/fact-sheet/news-influencers-fact-sheet/)；资料日期：2025-11-04；覆盖：美国成年人（含18-29岁青年群体）从社交媒体新闻意见领袖获取新闻与评论的比例追踪（2024及2025年8月调查）。限制：仅覆盖美国成年人社交媒体新闻消费，未直接量化传统政策智库或企业内部咨询中主观专家的采纳率。
- [ev-vbatch-0003-02](https://www.pewresearch.org/journalism/2024/11/18/americas-news-influencers/)；资料日期：2024-11-18；覆盖：美国热门社交媒体新闻意见领袖的机构背景（77%无新闻机构背景）及受众获取观点/评论的特征（2024年夏季调查，样本10,658人）。限制：该报告聚焦美国社交媒体平台上的新闻意见领袖，属于公共舆论与评论消费的回顾性代理，而非直接测度全部专业领域专家。
- [ev-vbatch-0003-03](https://www.wavestone.com/en/insight/data-ai-executive-leadership-survey-2024/)；资料日期：2024-05-17；覆盖：财富1000强及全球领先企业100余位数据与AI高管关于数据投资优先级、生成式AI规模化落地及企业级数据驱动思维障碍的年度调查（2023年数据）。限制：网页摘要仅展示部分核心结论且样本集中于100余家大型领先企业，未给出主观专家判断占比的精确百分比。
- [ev-vbatch-0003-04](https://pubmed.ncbi.nlm.nih.gov/37642169/)；资料日期：2024-09；覆盖：地缘政治预测中人类判断与算法模型分工及人机协同效果的权威心理学综述（Perspectives on Psychological Science, 2024年9月）。限制：该文为学术综述摘要，聚焦地缘政治预测领域，说明算法辅助提升准确率但人类仍掌握主导权。
- [ev-vbatch-0003-05](https://pubmed.ncbi.nlm.nih.gov/32229555/)；资料日期：2020-04-14；覆盖：“脆弱家庭挑战赛”160支研究团队基于高质量出生队列纵向数据预测个体6项多年期生活结果的大规模实证研究（PNAS, 2020年4月14日）。限制：该研究主要测试基于纵向调查数据的机器学习与统计模型对美国城市家庭个体生活结果的预测上限，属于个人多年期生活轨迹可预测性的重要实证代理，未直接测试人类主观直觉。
- [ev-vbatch-0003-06](https://ideas.repec.org/a/eee/intfor/v41y2025i2p499-516.html)；资料日期：2025；覆盖：2022年存在性风险说服预测锦标赛（XPT）中89名超级预测者与80名领域专家对长期重大风险与罕见转折预测表现的研究（International Journal of Forecasting, 2025）。限制：该文发表于2025年，锦标赛主体于2022年开展；由于长周期存在性风险尚未到期结算，论文主要呈现分歧、未收敛机制及对高技能预测者长期预测局限的评估，而非长期转折点的终局Brier结算。
- [ev-vbatch-0003-07](https://arxiv.org/abs/2409.19839)；资料日期：2025-02-28；覆盖：ForecastBench动态预测基准中人类专家预测者（含超级预测者）、公众与顶尖大语言模型在未来事件预测上的对照结果（arXiv:2409.19839v5, 2025年2月）。限制：ForecastBench评测的是动态生成的未来事件问题（多为中短期可结算问题），证明人类专家预测者在结构化预测中仍具显著优势，但并不构成对“多年期个人或国家重大转折点”可预测性的反证。
- [ev-vbatch-0004-01](https://www.rand.org/content/dam/rand/pubs/perspectives/PEA3400/PEA3490-2/RAND_PEA3490-2.pdf)；资料日期：2026-05；覆盖：RAND Corporation Perspective (PE-A3490-2, May 2026): Aligning Forecasting Methods to Support Intelligence Community Analytic Tradecraft, covering how crowdsourced forecasting tools align with ICD 203 standards, complement (not replace) IC analysts, reference Tetlock & Gardner Superforecasting, and face IC adoption constraints.。限制：RAND 研究报告反映 2026 年 5 月美国情报界分析方法论与 RAND Forecasting Initiative (RFI) 视角，不直接披露美国情报界涉密内部编制数据；发表日期精确到月（2026-05）。
- [ev-vbatch-0004-02](https://atlasinstitute.org/from-analysis-to-probability-modernizing-intelligence-forecasts/)；资料日期：2026-01-03；覆盖：Atlas Institute for International Affairs (2026-01-03): review of DARPA Policy Analysis Market (shut down 2003), IARPA Intelligence Community Prediction Market (2009-2020, cancelled in 2020), and limited institutional adoption of prediction markets in the U.S. Intelligence Community.。限制：第三方国际事务智库综述文章，二手整理了 DARPA PAM 与 IARPA ICPM 的存废历史，侧重预测市场而非全部群体预测工具。
- [ev-vbatch-0004-03](https://arxiv.org/html/2412.10981v1)；资料日期：2024-12-14；覆盖：USC Information Sciences Institute / IARPA Hybrid Forecasting Competition (HFC) paper (arXiv:2412.10981v1, 2024-12-14): evaluation of SAGE hybrid human-machine crowdsourced forecasting across 1,085 users and 398 real-world geopolitical problems.。限制：学术实验基于 8 个月、398 个公开地缘政治问题的 IARPA HFC 竞赛，反映人机混合预测的效率潜力而非对美国情报界现役分析师岗位的实际替代。
- [ev-vbatch-0004-04](https://forecastingresearch.org/about)；资料日期：未确定；覆盖：Forecasting Research Institute (FRI) official About page describing how first-generation forecasting research spearheaded by Philip Tetlock established a rigorous standard for prediction accuracy and how FRI builds on it with large-scale forecasting studies on AI, biosecurity, and geopolitics.。限制：机构官方自我介绍页面，未标注具体页面发表日期（截至 2026-11-25 公开可得），侧重 FRI 自身生态传承，不代表主流政府决策层的全面采纳。
- [ev-vbatch-0004-05](https://goodjudgment.com/about/)；资料日期：未确定；覆盖：Good Judgment Inc. official About page documenting the post-2015 commercialization of Philip Tetlock and Barbara Mellers Good Judgment Project (GJP) methodology, global network of professional Superforecasters, and evidence-based forecasting training.。限制：Good Judgment Inc. 官方商业介绍页面，未标注具体页面发表日期（截至 2026-11-25 公开可得），存在商业宣传属性，但可证实 2015 年后 GJP 方法论的机构化与商业化延续。
- [ev-vbatch-0005-01](https://www.lawfaremedia.org/article/how-us-government-can-learn-see-future)；资料日期：2021-05-09；覆盖：2008-2021年美国情报界（IC）与政府对定量概率预测、评分追踪及IARPA预测项目的采用与停滞情况。限制：属于政策分析与倡议文章（合著者之一 Michael C. Horowitz 曾为 IARPA ACE/Good Judgment Project 研究员），仅基于公开可获信息评估，无法涵盖可能存在的涉密内部项目。
- [ev-vbatch-0005-02](https://sashaingber.substack.com/p/exclusive-the-life-and-death-of-the)；资料日期：2026-05-26；覆盖：2008-2026年美国情报界内部预测市场（ICPM）在ODNI、IARPA与NIC间的流转、2020年关闭以及后续DIA赞助INFER告吹的一手调查。限制：为独立国安记者基于多位前情报高官与承建商访谈的调查报道，部分受访者匿名；主要聚焦内部预测市场（ICPM）与INFER，未穷尽各情报机构全部未公开内部培训。
- [ev-vbatch-0005-03](https://www.cultivatelabs.com/posts/how-the-u-s-intelligence-community-s-prediction-market-made-analysis-better)；资料日期：2025-07-22；覆盖：ICPM软件承建商Cultivate Labs确认ICPM于2020年取消，且截至2025年7月据其所知美国政府内部已无活跃的内部预测项目。限制：来源为曾承建ICPM软件的商业公司Cultivate Labs，可能存在推广自身预测平台的商业视角，且其陈述限定于“据我们所知”（to our knowledge），无法覆盖完全保密的内部项目。
- [ev-vbatch-0005-04](https://intelligencecommunitynews.com/iarpa-launches-hybrid-forecasting-competition/)；资料日期：2017-08-20；覆盖：2017年8月IARPA启动为期四年的混合预测竞赛（HFC），说明IC研发分支在2015年后仍资助预测方法研究，但测试依靠外部承包商与数千名外部志愿者而非培养IC内部超级预测者。限制：属于项目启动时的行业新闻报道，反映2017年IARPA的立项与合同架构，未涵盖HFC项目2020年结题后在IC作战/分析部门的转化结果。
