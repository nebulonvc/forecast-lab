# 超级智能：五类评估

证据截止日：2026-11-15。已处理 100/100 条全书候选；尚未处理 0 条。

累计已完成全量抽取复核 100 条；保留旧抽样抽取 0 条，两者不重复相加。

已补充扩展观点 100 条；其中 0 条仍有待确认的代指、对象或范围，已逐条标记。扩展观点不自动改变原有评估。

本轮沿用候选清单逐条核查，不保证没有漏抽。PDF记录使用PDF页码，TXT记录使用原始文本行号。扩展观点是依据所给语境的解释，原文短引文另行保留。

|类别|父记录数|
|---|---:|
|正确|21|
|趋势符合|9|
|部分符合|14|
|错误|0|
|暂无法判断|51|
|排除：非预测|5|
|排除：重复|0|
|尚未处理|0|

可判定覆盖率：44/95 = 46.3%。
绑定外部证据的预测：94/95；未绑定：1。绑定不代表证据充分或研究已完成。
“正确”占已判定记录：21/44 = 47.7%。

趋势符合 9 条单独列出，与部分符合互不重复；它表示已有持续证据支持方向，最终结果仍待验证。

以上是回顾性的记录统计，不是独立预测准确率或事前预测能力检验。部分符合不折算成 0.5 分；暂无法判断不算错误。跨章相关判断尚未完全去重，同一父记录也不因多个观察而增加命中次数。没有作者明确给出的概率，不计算 Brier 分数。

## 评估口径

正确：在列明口径和观察窗口内，主要可检验内容符合。趋势符合：已有持续客观证据支持预测方向，最终结果尚待验证。部分符合：具体分项部分成立、部分不符，或合理口径产生不同结果。错误：所评内容与已发生结果相反。暂无法判断：无法确认趋势或结果、条件不明、对象难测或证据仍不足；缺证据不能自动换成趋势符合或部分符合。

明确未来终点尚未到达时，可以评价已有趋势，并保留原期限；这类进展单列为趋势符合，不作终局正确。单次波动、未来预测数据或仅有因果解释不算趋势证据。真正的前提条件仍须确认成立，作者的因果解释不自动增加为额外触发门槛。无期限持续判断可评价已观察阶段，不能证明永久成立。出版年只是未找到发言日期时的研究起点代理，出版前已知事实不是新的预见力证据。

“不太可能”没有被转换为数值概率；低概率事件发生可记录为方向反例，不能据单次结果证明概率失准。官方声明证明立场或制度安排，不自动证明实际成效；同时出现的政策与结果不自动证明因果。

## 暂无法判断的原因

|原因类型|记录数|
|---|---:|
|条件未确认或未触发|19|
|证据不足|24|
|明确未来期限未到|8|
时间窗口来源：原文写出 27 条，隐含的出版年至截止日 73 条。


## 逐条结果

### 1. TXT 第 654—655 行 · 暂无法判断

记录：`txt-24d36f2b5e-000020733-000020832`

原文：the world will be some 4.8 times richer
by 2050 and about 34 times richer by 2100 than it is today.

时间窗口：原文写出（by 2050）。

扩展观点（解释，非原文）：If world economic growth continues at the pace of the past fifty years, the world will be about 4.8 times richer by 2050 and about 34 times richer by 2100.


口径与范围：核验对象：If world economic growth continues at the pace of the past fifty years, the world will be about 4.8 times richer by 2050 and about 34 times richer by 2100.
判定：按过去五十年增速外推到2050/2100的条件尚未完结；2014年后全球增速已低于长期均值，前提是否成立也不清楚。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-129f7e9fe4fa](https://tradingeconomics.com/world/full-year-gdp-growth)；[ev-e8cad97ce76a](https://www.worldbank.org/en/research/publication/long-term-growth-prospects)

### 2. TXT 第 760—762 行 · 部分符合

记录：`txt-24d36f2b5e-000025284-000025399`

原文：most technologies
that will have a big impact on the world in five or ten years from now are already
in limited use

时间窗口：原文写出（in five or ten years）。

扩展观点（解释，非原文）：Most technologies that will have a big impact on the world five or ten years after publication are already in limited use at the time of writing.


口径与范围：核验对象：Most technologies that will have a big impact on the world five or ten years after publication are already in limited use at the time of writing.
判定：智能手机、深度学习、CRISPR等2014年已在有限使用或实验室中，其后确实产生重大影响；但Transformer（2017）和ChatGPT所代表的生成式跃迁在出版时并无相应原型。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-f88f49f8b7da](https://en.wikipedia.org/wiki/2010s_in_science_and_technology)；[ev-5642ba2e1e7d](https://en.wikipedia.org/wiki/Transformer_(deep_learning))

### 3. TXT 第 762—763 行 · 部分符合

记录：`txt-24d36f2b5e-000025407-000025515`

原文：technologies that will reshape the world in less than fifteen
years probably exist as laboratory prototypes.

时间窗口：原文写出（in less than fifteen）。

扩展观点（解释，非原文）：Technologies that will reshape the world within fifteen years of publication probably already exist as laboratory prototypes.


口径与范围：核验对象：Technologies that will reshape the world within fifteen years of publication probably already exist as laboratory prototypes.
判定：多数在十五年窗口内产生重大影响的技术在2014年已有实验室或早期形态，但支撑后来最大变革的Transformer架构直到2017年才出现。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-5642ba2e1e7d](https://en.wikipedia.org/wiki/Transformer_(deep_learning))；[ev-9e7754ff2e3c](https://www.technologyreview.com/2023/02/08/1068068/chatgpt-is-everywhere-heres-where-it-came-from/)

### 4. TXT 第 776—777 行 · 暂无法判断

记录：`txt-24d36f2b5e-000026638-000026738`

原文：The train might not pause or even decelerate
at Humanville Station. It is likely to swoosh right by.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：Once human-level machine intelligence is reached, systems are likely to proceed rapidly to superhuman intelligence rather than pausing at the human level.


口径与范围：核验对象：Once human-level machine intelligence is reached, systems are likely to proceed rapidly to superhuman intelligence rather than pausing at the human level.
判定：人类水平机器智能尚未出现，无法核验达到该水平后是否会迅速越过。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：not_met。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-43aa6f41ebe7](https://leap.forecastingresearch.org/reports/wave8)；[ev-2b24180d50bc](https://ai100.stanford.edu/reports/2026-report/standing-questions/sq5-what-are-prospects-more-general-artificial-intelligence)

### 5. TXT 第 1200—1201 行 · 部分符合

记录：`txt-24d36f2b5e-000054359-000054457`

原文：If this rate of improvement continues, they might beat the human
world champion in about a decade.

时间窗口：原文写出（in about a decade）。

扩展观点（解释，非原文）：If go programs continue improving at about one dan per year, they might beat the human world champion in about a decade (around 2022).


口径与范围：核验对象：If go programs continue improving at about one dan per year, they might beat the human world champion in about a decade (around 2022).
判定：围棋程序确实击败了人类世界冠军，但时点早于线性外推的约2022年（2016–2017），路径是深度学习跃迁而非每年一段的匀速提升。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-4c37f46e6298](https://en.wikipedia.org/wiki/AlphaGo)；[ev-674a9aea440f](https://en.wikipedia.org/wiki/AlphaGo_versus_Ke_Jie)

### 6. TXT 第 1231—1234 行 · 部分符合

记录：`txt-24d36f2b5e-000056650-000056935`

原文：an AI that could understand natural language as well as a human
adult, they would in all likelihood also either already have succeeded in creating
an AI that could do everything else that human intelligence can do, or they would
be but a very short step from such a general capability.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：An AI that understands natural language as well as a human adult would in all likelihood already have, or be a very short step from, general human-level capability.


口径与范围：核验对象：An AI that understands natural language as well as a human adult would in all likelihood already have, or be a very short step from, general human-level capability.
判定：大语言模型在多项语言理解任务上已接近或达到人类成人水平，但通用能力、推理与主体性仍有明显缺口，并非“只差很短一步就具备全面人类水平能力”。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-14cd2e36c188](https://arxiv.org/html/2303.08774v4)；[ev-f9c4697f2479](https://pmc.ncbi.nlm.nih.gov/articles/PMC11840437/)；[ev-2b24180d50bc](https://ai100.stanford.edu/reports/2026-report/standing-questions/sq5-what-are-prospects-more-general-artificial-intelligence)

### 7. TXT 第 1413—1414 行 · 排除：非预测

记录：`txt-24d36f2b5e-000071901-000071987`

原文：10% probability of HLMI by 2022, 50% probability by 2040, and 90%
probability by 2075.

时间窗口：原文写出（by 2022）。

扩展观点（解释，非原文）：The combined expert-survey median estimate was a 10% probability of human-level machine intelligence by 2022, 50% by 2040, and 90% by 2075.


口径与范围：不可核验的候选（流水线 resolvable=false）
判定：抽取流水线将其降级为unclear/不可核验，按METHOD.md不进入核验。
限制：非可核验预测
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：流水线归属/可核验规则排除（原文明确；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 8. TXT 第 1488—1490 行 · 暂无法判断

记录：`txt-24d36f2b5e-000073830-000074011`

原文：the median numbers reported in the expert survey do
not have enough probability mass on later arrival dates. A 10% probability of
HLMI not having been developed by 2075 or even 2100

时间窗口：原文写出（by 2075）。

扩展观点（解释，非原文）：The author judges that a 10% probability of HLMI still not existing by 2075 or even 2100 is too low; later arrival dates deserve more probability mass.


口径与范围：核验对象：The author judges that a 10% probability of HLMI still not existing by 2075 or even 2100 is too low; later arrival dates deserve more probability mass.
判定：这是关于2075/2100年概率质量应如何分配的判断，终点仍在未来，无法用2026年的观察判定对错。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-43aa6f41ebe7](https://leap.forecastingresearch.org/reports/wave8)

### 9. TXT 第 1507—1508 行 · 暂无法判断

记录：`txt-24d36f2b5e-000075295-000075415`

原文：I assign a higher probability to superintelligence being created relatively soon
after human-level machine intelligence.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：The author assigns a higher probability than the survey to superintelligence arriving relatively soon after human-level machine intelligence.


口径与范围：核验对象：The author assigns a higher probability than the survey to superintelligence arriving relatively soon after human-level machine intelligence.
判定：超级智能是否会在人类水平机器智能之后很快到来，前提（人类水平机器智能已经出现）尚未满足。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：not_met。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-43aa6f41ebe7](https://leap.forecastingresearch.org/reports/wave8)

### 10. TXT 第 1509—1510 行 · 暂无法判断

记录：`txt-24d36f2b5e-000075474-000075585`

原文：thinking an extremely good or an extremely bad outcome to
be somewhat more likely than a more balanced outcome.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：The author thinks an extremely good or extremely bad long-term outcome of HLMI is somewhat more likely than a balanced outcome.


口径与范围：核验对象：The author thinks an extremely good or extremely bad long-term outcome of HLMI is somewhat more likely than a balanced outcome.
判定：关于人类水平机器智能之长期结局极端好坏更可能的判断，结局尚未展开。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-43aa6f41ebe7](https://leap.forecastingresearch.org/reports/wave8)

### 11. TXT 第 1557—1558 行 · 暂无法判断

记录：`txt-24d36f2b5e-000076422-000076517`

原文：human-level machine
intelligence has a fairly sizeable chance of being developed by mid-century

时间窗口：原文写出（by mid-century）。

扩展观点（解释，非原文）：Human-level machine intelligence has a fairly sizeable chance of being developed by mid-century.


口径与范围：核验对象：Human-level machine intelligence has a fairly sizeable chance of being developed by mid-century.
判定：本世纪中叶（约2050年）尚未到达，人类水平机器智能也尚未被公认实现，无法判定“相当可观的机会”是否成立。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-43aa6f41ebe7](https://leap.forecastingresearch.org/reports/wave8)；[ev-f72e0b899c01](https://santageai.com/agi/agi-timelines)

### 12. TXT 第 1560 行 · 暂无法判断

记录：`txt-24d36f2b5e-000076615-000076682`

原文：it might perhaps fairly soon thereafter result in superintelligence

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：Human-level machine intelligence might perhaps fairly soon thereafter result in superintelligence.


口径与范围：核验对象：Human-level machine intelligence might perhaps fairly soon thereafter result in superintelligence.
判定：取决于人类水平机器智能先出现，该前提尚未满足。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-43aa6f41ebe7](https://leap.forecastingresearch.org/reports/wave8)

### 13. TXT 第 1561 行 · 暂无法判断

记录：`txt-24d36f2b5e-000076693-000076845`

原文：a wide range of outcomes may have a significant chance of occurring, including extremely good outcomes and outcomes that are as bad as human extinction.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：A wide range of long-term outcomes, including ones as bad as human extinction, may have a significant chance of occurring.


口径与范围：核验对象：A wide range of long-term outcomes, including ones as bad as human extinction, may have a significant chance of occurring.
判定：关于长期结局（含灭绝）具有显著概率的判断，无法在截止日前用已实现结果核验。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-43aa6f41ebe7](https://leap.forecastingresearch.org/reports/wave8)

### 14. TXT 第 1639—1640 行 · 排除：非预测

记录：`txt-24d36f2b5e-000082217-000082357`

原文：including David Chalmers and Hans Moravec, to argue that human-level AI is
not only theoretically possible but feasible within this century.

时间窗口：原文写出（within this century）。

扩展观点（解释，非原文）：David Chalmers and Hans Moravec argue that human-level AI is not only theoretically possible but feasible within this century.


口径与范围：不可核验的候选（流水线 resolvable=false）
判定：抽取流水线将其降级为unclear/不可核验，按METHOD.md不进入核验。
限制：非可核验预测
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：流水线归属/可核验规则排除（原文明确；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 15. TXT 第 1729—1730 行 · 暂无法判断

记录：`txt-24d36f2b5e-000089506-000089584`

原文：Even a
century of continued Moore’s law would not be enough to close this gap.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：Even a century of continued Moore’s law would not close the computational gap between current supercomputers and a brute-force recapitulation of the evolution of nervous systems.


口径与范围：核验对象：Even a century of continued Moore’s law would not close the computational gap between current supercomputers and a brute-force recapitulation of the evolution of nervous systems.
判定：“即使再持续一个世纪的摩尔定律也不足以填平与神经系统进化算力的差距”是跨世纪的计算判断，十二年观察不足以判定。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-86203ea531d8](https://epoch.ai/data-insights/compute-trend-post-2010)；[ev-1b34fd454f7e](https://www.fhi.ox.ac.uk/wp-content/uploads/ai-evolution-and-selection-effects.pdf)

### 16. TXT 第 1866 行 · 正确

记录：`txt-24d36f2b5e-000096657-000096716`

原文：More cases like these will surely accumulate in the future.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：Further transfers of ideas from brain science to AI techniques will surely accumulate in the future.


口径与范围：核验对象：Further transfers of ideas from brain science to AI techniques will surely accumulate in the future.
判定：2014年以来，神经编码/解码、脑启发网络和脑成像与深度学习的交叉研究持续积累，方向成立。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-82e25649e888](https://arxiv.org/pdf/2307.10246)；[ev-e184b6e52a0b](https://www.nature.com/articles/s41583-025-00957-8)

### 17. TXT 第 1868—1869 行 · 暂无法判断

记录：`txt-24d36f2b5e-000096840-000096925`

原文：continuing incremental progress in brain science should
eventually discover them all.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：Continuing incremental progress in brain science should eventually discover all the distinct fundamental mechanisms that operate in the brain.


口径与范围：核验对象：Continuing incremental progress in brain science should eventually discover all the distinct fundamental mechanisms that operate in the brain.
判定：“最终发现大脑全部基本机制”的终点尚未到来；果蝇等连接组有进展，但人类大脑机制远未穷尽。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-e184b6e52a0b](https://www.nature.com/articles/s41583-025-00957-8)；[ev-21c582bc458d](https://pmc.ncbi.nlm.nih.gov/articles/PMC13659455/)

### 18. TXT 第 1918 行 · 暂无法判断

记录：`txt-24d36f2b5e-000100939-000100986`

原文：it is likely that most will be—extremely alien.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：Most artificial intelligences will be extremely alien rather than resembling a human mind.


口径与范围：核验对象：Most artificial intelligences will be extremely alien rather than resembling a human mind.
判定：这句话针对未来大多数人工智能的心智形态；当前系统既有异于人类的一面，也深度依赖人类语料，尚不能代表“大多数”。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-2b24180d50bc](https://ai100.stanford.edu/reports/2026-report/standing-questions/sq5-what-are-prospects-more-general-artificial-intelligence)

### 19. TXT 第 1918—1919 行 · 正确

记录：`txt-24d36f2b5e-000100987-000101092`

原文：We should expect
that they will have very different cognitive architectures than biological intelligences

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：Future AIs should be expected to have very different cognitive architectures than biological intelligences.


口径与范围：核验对象：Future AIs should be expected to have very different cognitive architectures than biological intelligences.
判定：深度网络与Transformer等现行人工智能的认知架构已明显不同于生物神经系统，这一方向在截止日前已经实现。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-5642ba2e1e7d](https://en.wikipedia.org/wiki/Transformer_(deep_learning))；[ev-82e25649e888](https://arxiv.org/pdf/2307.10246)

### 20. TXT 第 1982—1983 行 · 趋势符合（最终结果待验证）

记录：`txt-24d36f2b5e-000105590-000105707`

原文：There is good reason to think that the requisite enabling technologies are
attainable, though not in the near future.

时间窗口：原文写出（in the near future）。

扩展观点（解释，非原文）：The enabling technologies for whole brain emulation are attainable, but not in the near future.


口径与范围：核验对象：The enabling technologies for whole brain emulation are attainable, but not in the near future.
判定：全脑仿真的前导技术仍在发展且被普遍认为可以达到，但人类全脑仿真在2014–2026年间并未到来，“近期不会实现”的方向成立，窗口尚未完全结束。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-e5088ffcdbc9](https://alleninstitute.org/news/how-far-are-we-from-a-human-brain-simulation-and-what-does-that-mean-for-science)；[ev-09d1dcb558c0](https://biologyinsights.com/mind-uploading-research-whats-the-current-progress/)

### 21. TXT 第 2143—2145 行 · 暂无法判断

记录：`txt-24d36f2b5e-000111810-000111943`

原文：it
seems quite likely that the first whole brain emulation that we would achieve if
we went down this path would be of a lower grade.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：If the WBE path is pursued, the first whole brain emulation achieved would quite likely be of a lower grade than a high-fidelity copy.


口径与范围：核验对象：If the WBE path is pursued, the first whole brain emulation achieved would quite likely be of a lower grade than a high-fidelity copy.
判定：全脑仿真路径尚未走到第一例人类仿真，无法核验其保真度是否会偏低。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：not_met。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-0283cb442ec3](https://defensesindepth.bio/will-whole-brain-emulation-matter-for-the-ai-transition/)

### 22. TXT 第 2154—2155 行 · 排除：非预测

记录：`txt-24d36f2b5e-000112722-000112832`

原文：the prerequisite capabilities might be available around mid-century, though with a large
uncertainty interval.

时间窗口：原文写出（around mid-century）。

扩展观点（解释，非原文）：A recent technical roadmap concluded that the prerequisite capabilities for human whole brain emulation might be available around mid-century, with a large uncertainty interval.


口径与范围：不可核验的候选（流水线 resolvable=false）
判定：抽取流水线将其降级为unclear/不可核验，按METHOD.md不进入核验。
限制：非可核验预测
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：流水线归属/可核验规则排除（原文明确；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 23. TXT 第 2248—2249 行 · 趋势符合（最终结果待验证）

记录：`txt-24d36f2b5e-000117447-000117538`

原文：the emulation path will not succeed in the near future
(within the next fifteen years, say)

时间窗口：原文写出（within the next fifteen years）。

扩展观点（解释，非原文）：Whole brain emulation will not succeed in the near future (within about fifteen years of publication, i.e. by about 2029), because precursor technologies are still missing.


口径与范围：核验对象：Whole brain emulation will not succeed in the near future (within about fifteen years of publication, i.e. by about 2029), because precursor technologies are still missing.
判定：至2026年11月人类全脑仿真仍未成功，与“未来约十五年（约至2029年）内不会成功”的方向一致，但终点尚未到期。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-e5088ffcdbc9](https://alleninstitute.org/news/how-far-are-we-from-a-human-brain-simulation-and-what-does-that-mean-for-science)；[ev-0283cb442ec3](https://defensesindepth.bio/will-whole-brain-emulation-matter-for-the-ai-transition/)

### 24. TXT 第 2250—2251 行 · 趋势符合（最终结果待验证）

记录：`txt-24d36f2b5e-000117771-000117894`

原文：it is conceivable—though unlikely—that somebody
somewhere will get the right insight for how to do this in the near future.

时间窗口：原文写出（in the near future）。

扩展观点（解释，非原文）：It is conceivable though unlikely that someone will get the right insight to code a seed AI on a then-ordinary personal computer in the near future.


口径与范围：核验对象：It is conceivable though unlikely that someone will get the right insight to code a seed AI on a then-ordinary personal computer in the near future.
判定：在“近期”窗口内尚未出现有人在普通个人计算机上写出种子人工智能的情形，方向与“不太可能”一致，但近窗口尚未完全闭合。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-43aa6f41ebe7](https://leap.forecastingresearch.org/reports/wave8)；[ev-20dfb5ccf00b](https://ai100.stanford.edu/reports/2026-report/deep-dives/deep-dive-two-scaling-era)

### 25. TXT 第 2279—2280 行 · 正确

记录：`txt-24d36f2b5e-000120209-000120395`

原文：it seems implausible, on both neurological and evolutionary grounds, that one could by introducing some chemical into the brain of a
healthy person spark a dramatic rise in intelligence.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：It is implausible that introducing some chemical into a healthy person’s brain would spark a dramatic rise in intelligence.


口径与范围：核验对象：It is implausible that introducing some chemical into a healthy person’s brain would spark a dramatic rise in intelligence.
判定：系统综述显示莫达非尼、哌甲酯等只有中等或有限的认知增强效果，并未出现向健康人脑引入某种化学物质即引发智力戏剧性提升的情形。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-15a4917c4f1e](https://pubmed.ncbi.nlm.nih.gov/32709551/)；[ev-c04d061e2839](https://link.springer.com/article/10.1007/s40267-023-00989-z?code=25a03bc5-a472-4477-a9f2-d97055a317af&error=cookies_not_supported)

### 26. TXT 第 2294—2295 行 · 部分符合

记录：`txt-24d36f2b5e-000121517-000121621`

原文：The range of traits that can be selected for or against will expand
greatly over the next decade or two.

时间窗口：原文写出（the next decade or two）。

扩展观点（解释，非原文）：The range of traits that can be selected for or against in embryos will expand greatly over the next decade or two.


口径与范围：核验对象：The range of traits that can be selected for or against in embryos will expand greatly over the next decade or two.
判定：可选择性状已从单基因检测扩展到多基因风险评分等商业服务，范围确实扩大；但专业学会仍认为其未准备好进入临床，谈不上“大大扩展”并被广泛采用。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-88590988d337](https://academic.oup.com/humupd/article/30/5/529/7684172)；[ev-9726e3d0d5db](https://www.asrm.org/news-and-events/asrm-news/press-releasesbulletins/asrm-ethics-and-practice-committees-release-new-report-concluding-polygenic-embryo-screening-is-not-ready-for-clinical-use/)

### 27. TXT 第 2296—2298 行 · 正确

记录：`txt-24d36f2b5e-000121816-000121966`

原文：is just
now starting to become feasible and will greatly increase our knowledge of the
genetic architectures of human cognitive and behavioral traits.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：Genome-wide complex trait analysis with vast samples is just becoming feasible and will greatly increase knowledge of the genetic architecture of human cognitive and behavioral traits.


口径与范围：核验对象：Genome-wide complex trait analysis with vast samples is just becoming feasible and will greatly increase knowledge of the genetic architecture of human cognitive and behavioral traits.
判定：教育程度与认知相关GWAS样本量从约十万级扩至更大队列，已识别大量位点，对遗传结构的认识显著增加。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-13dc1839a66b](https://www.nature.com/articles/mp201645)；[ev-70f3a67b8234](https://pubmed.ncbi.nlm.nih.gov/27225129/)

### 28. TXT 第 2298—2300 行 · 部分符合

记录：`txt-24d36f2b5e-000121969-000122086`

原文：Any trait with
a non-negligible heritability—including cognitive capacity—could then become
susceptible to selection.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：Once genetic architectures are better known, any trait with non-negligible heritability, including cognitive capacity, could become susceptible to embryo selection.


口径与范围：核验对象：Once genetic architectures are better known, any trait with non-negligible heritability, including cognitive capacity, could become susceptible to embryo selection.
判定：认知等具有遗传力的性状在技术上已可用多基因评分做胚胎筛选，但临床证据不足、多地不支持常规使用，远未成为稳定可及的选择手段。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-0249ba324ebe](https://pmc.ncbi.nlm.nih.gov/articles/PMC11981603/)；[ev-fbe7b5da7156](https://www.hfea.gov.uk/about-us/our-blog/pgt-p-is-not-lawful-in-the-uk-is-not-supported-by-evidence-and-may-reduce-the-chances-of-having-a-baby-overall)

### 29. TXT 第 2354—2355 行 · 趋势符合（最终结果待验证）

记录：`txt-24d36f2b5e-000124105-000124245`

原文：Long before then, more direct and powerful modes of genetic engineering
(not to mention machine intelligence) will most likely be available.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：Long before five successive generations of embryo selection would reach the twenty-second century, more direct and powerful genetic engineering (and machine intelligence) will most likely be available.


口径与范围：核验对象：Long before five successive generations of embryo selection would reach the twenty-second century, more direct and powerful genetic engineering (and machine intelligence) will most likely be available
判定：CRISPR等更直接的基因编辑工具已出现，体细胞疗法进入临床，但安全的人类生殖系增强和相关机器智能都尚未就绪，二十二世纪之前这一终点也未到。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-551daaff3e93](https://www.who.int/health-topics/human-genome-editing)；[ev-85bf5360b552](https://www.cell.com/med/fulltext/S2666-6340(26)00228-X)

### 30. TXT 第 2363—2364 行 · 排除：非预测

记录：`txt-24d36f2b5e-000124823-000124904`

原文：these challenges might put human application “10 or even 50 years
in the future.”

时间窗口：原文写出（10 or even 50 years）。

扩展观点（解释，非原文）：According to one expert, translating stem-cell-derived gametes from animals to safe human use might be 10 or even 50 years in the future.


口径与范围：不可核验的候选（流水线 resolvable=false）
判定：抽取流水线将其降级为unclear/不可核验，按METHOD.md不进入核验。
限制：非可核验预测
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：流水线归属/可核验规则排除（原文明确；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 31. TXT 第 2398—2400 行 · 暂无法判断

记录：`txt-24d36f2b5e-000127365-000127535`

原文：even after the technology has
been perfected, adoption rates will probably start out low. Some countries might
prohibit its use altogether, on moral or religious grounds.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：Even after iterated embryo selection is perfected, adoption rates will probably start out low, and some countries might prohibit its use on moral or religious grounds.


口径与范围：核验对象：Even after iterated embryo selection is perfected, adoption rates will probably start out low, and some countries might prohibit its use on moral or religious grounds.
判定：迭代胚胎选择技术尚未完善，关于完善之后初期采用率和部分国家禁止的判断前提未满足。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-fbe7b5da7156](https://www.hfea.gov.uk/about-us/our-blog/pgt-p-is-not-lawful-in-the-uk-is-not-supported-by-evidence-and-may-reduce-the-chances-of-having-a-baby-overall)

### 32. TXT 第 2581—2583 行 · 暂无法判断

记录：`txt-24d36f2b5e-000138157-000138344`

原文：might not only permit but
actively promote the use of genetic selection and genetic engineering to enhance
the intelligence of their populations once the technology to do so is available.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：Some countries with long-term population policies, perhaps China or Singapore, might not only permit but actively promote genetic selection and engineering to enhance population intelligence once the technology is available.


口径与范围：核验对象：Some countries with long-term population policies, perhaps China or Singapore, might not only permit but actively promote genetic selection and engineering to enhance population intelligence once the 
判定：用于增强群体智力的成熟技术并未被认定已经可用；中国在贺建奎事件后禁止生殖系临床研究，新加坡也未见此类促进计划。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：not_met。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-741d793b4395](https://www.scmp.com/news/china/politics/article/3270285/china-bans-clinical-research-germline-genome-editing-irresponsible)；[ev-d78cd2c54f47](https://en.wikipedia.org/wiki/He_Jiankui_affair)

### 33. TXT 第 2588—2590 行 · 暂无法判断

记录：`txt-24d36f2b5e-000138914-000139122`

原文：There is some chance that a large attitudinal shift could take place over a
relatively short time, perhaps in as little as a decade, once the technology is proven
to work and to provide a substantial benefit.

时间窗口：原文写出（as little as a decade）。

扩展观点（解释，非原文）：Once genetic-selection technology is proven to work and provide substantial benefit, a large attitudinal shift could take place in as little as a decade.


口径与范围：核验对象：Once genetic-selection technology is proven to work and provide substantial benefit, a large attitudinal shift could take place in as little as a decade.
判定：“技术被证明有效并带来显著好处”这一前提尚未成立，无法核验态度是否会在约十年内大幅转变。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-9726e3d0d5db](https://www.asrm.org/news-and-events/asrm-news/press-releasesbulletins/asrm-ethics-and-practice-committees-release-new-report-concluding-polygenic-embryo-screening-is-not-ready-for-clinical-use/)

### 34. TXT 第 2602—2603 行 · 趋势符合（最终结果待验证）

记录：`txt-24d36f2b5e-000140178-000140287`

原文：germline enhancements are unlikely to have a significant
impact on society before the middle of this century.

时间窗口：原文写出（the middle of this century）。

扩展观点（解释，非原文）：Germline enhancements are unlikely to have a significant impact on society before the middle of this century.


口径与范围：核验对象：Germline enhancements are unlikely to have a significant impact on society before the middle of this century.
判定：截至2026年，生殖系增强几乎没有对社会产生显著影响（仅有一例违规事件并随后被禁），与“本世纪中叶前不太可能有显著影响”的方向一致，但中叶终点未到。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-d78cd2c54f47](https://en.wikipedia.org/wiki/He_Jiankui_affair)；[ev-741d793b4395](https://www.scmp.com/news/china/politics/article/3270285/china-bans-clinical-research-germline-genome-editing-irresponsible)

### 35. TXT 第 2603—2604 行 · 暂无法判断

记录：`txt-24d36f2b5e-000140321-000140434`

原文：the intelligence of significant segments of the adult population may begin to
be boosted by genetic enhancements.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：From mid-century onward, the intelligence of significant segments of the adult population may begin to be boosted by genetic enhancements.


口径与范围：核验对象：From mid-century onward, the intelligence of significant segments of the adult population may begin to be boosted by genetic enhancements.
判定：“本世纪中叶起”的窗口尚未开始。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-d78cd2c54f47](https://en.wikipedia.org/wiki/He_Jiankui_affair)

### 36. TXT 第 2644—2646 行 · 暂无法判断

记录：`txt-24d36f2b5e-000143845-000144027`

原文：the probable emergence of a generation of genetically enhanced
populations—voters, inventors, scientists—with the magnitude of enhancement
escalating rapidly over subsequent decades.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：Scenarios stretching into the second half of this century and beyond should take into account the probable emergence of a genetically enhanced generation of voters, inventors and scientists, with the magnitude of enhancement escalating rapidly over subsequent decades.


口径与范围：核验对象：Scenarios stretching into the second half of this century and beyond should take into account the probable emergence of a genetically enhanced generation of voters, inventors and scientists, with the 
判定：本世纪下半叶及以后的增强世代尚未出现。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-d78cd2c54f47](https://en.wikipedia.org/wiki/He_Jiankui_affair)

### 37. TXT 第 2656—2657 行 · 正确

记录：`txt-24d36f2b5e-000144534-000144623`

原文：it seems unlikely that such
interfaces will be widely used as enhancements any time soon.

时间窗口：原文写出（any time soon）。

扩展观点（解释，非原文）：Direct brain–computer interfaces seem unlikely to be widely used as enhancements any time soon.


口径与范围：核验对象：Direct brain–computer interfaces seem unlikely to be widely used as enhancements any time soon.
判定：脑机接口仍主要处于医学试验阶段，用于功能恢复而非被广泛当作增强手段，与“不太可能在近期被广泛用作增强”相符。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-464ab5024a01](https://www.nature.com/articles/s44222-024-00239-5)；[ev-2ee2ccce1f15](https://www.technologyreview.com/2025/04/01/1114009/brain-computer-interfaces-10-breakthrough-technologies-2025/)

### 38. TXT 第 2809 行 · 正确

记录：`txt-24d36f2b5e-000158491-000158590`

原文：Voluntary and involuntary surveillance will amass vast amounts of information about human behavior.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：Voluntary and involuntary surveillance will amass vast amounts of information about human behavior.


口径与范围：核验对象：Voluntary and involuntary surveillance will amass vast amounts of information about human behavior.
判定：智能手机、社交媒体、闭路电视、门铃摄像头和人脸识别等，在2014年后把行为数据的规模又扩大了几个数量级。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-ce9fcfc625ed](https://carnegieendowment.org/files/WP-Feldstein-AISurveillance_final.pdf)；[ev-05328adf0a06](https://www.cctv-focus.com/video-surveillance/vendor-news/ip-camera-boom)

### 39. TXT 第 2811—2812 行 · 部分符合

记录：`txt-24d36f2b5e-000158684-000158829`

原文：soon, these people might begin uploading continuous life recordings from
microphones and video cameras embedded in their smart phones or eyeglass

时间窗口：原文写出（soon）。

扩展观点（解释，非原文）：Social-network users might soon begin uploading continuous life recordings from microphones and cameras in smartphones or eyeglass frames.


口径与范围：核验对象：Social-network users might soon begin uploading continuous life recordings from microphones and cameras in smartphones or eyeglass frames.
判定：出现了可拍照录音的智能眼镜（如Ray-Ban Meta）和部分连续记录设备，但社交网络用户并未普遍开始上传连续生活记录。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-4e78fc5c2d15](https://www.eff.org/deeplinks/2026/03/think-twice-buying-or-using-metas-ray-bans)；[ev-2d3caa104fb2](https://www.reuters.com/business/media-telecom/smart-glasses-ai-pins-privacy-fears-challenge-techs-next-big-bet-2026-09-22/)

### 40. TXT 第 2813 行 · 部分符合

记录：`txt-24d36f2b5e-000158838-000158911`

原文：Automated analysis of such data streams will enable many new applications

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：Automated analysis of continuous life-recording data streams will enable many new applications, sinister as well as benign.


口径与范围：核验对象：Automated analysis of continuous life-recording data streams will enable many new applications, sinister as well as benign.
判定：人脸识别、门铃摄像头和智能眼镜的自动分析已经带来新应用，但针对连续生活记录数据流的全面自动分析远未普及。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-ce9fcfc625ed](https://carnegieendowment.org/files/WP-Feldstein-AISurveillance_final.pdf)；[ev-4e78fc5c2d15](https://www.eff.org/deeplinks/2026/03/think-twice-buying-or-using-metas-ray-bans)

### 41. TXT 第 2856 行 · 暂无法判断

记录：`txt-24d36f2b5e-000162835-000162885`

原文：might plausibly first be attained via the AI path.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：True superintelligence might plausibly first be attained via the AI path.


口径与范围：核验对象：True superintelligence might plausibly first be attained via the AI path.
判定：超级智能尚未被创造，无法核验它是否会首先经由人工智能路径达到。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-43aa6f41ebe7](https://leap.forecastingresearch.org/reports/wave8)

### 42. TXT 第 2861—2863 行 · 暂无法判断

记录：`txt-24d36f2b5e-000163349-000163529`

原文：It seems fairly likely, however, that even if
progress along the whole brain emulation path is swift, artificial intelligence will
nevertheless be first to cross the finishing line

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：Even if progress along the whole-brain-emulation path is swift, artificial intelligence will fairly likely still be first to reach superintelligence, because of neuromorphic AIs based on partial emulations.


口径与范围：核验对象：Even if progress along the whole-brain-emulation path is swift, artificial intelligence will fairly likely still be first to reach superintelligence, because of neuromorphic AIs based on partial emula
判定：全脑仿真路径并未迅速推进到终点，比较哪一条路先达到超级智能尚无法判定。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：not_met。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-0283cb442ec3](https://defensesindepth.bio/will-whole-brain-emulation-matter-for-the-ai-transition/)

### 43. TXT 第 2877 行 · 趋势符合（最终结果待验证）

记录：`txt-24d36f2b5e-000164527-000164600`

原文：Brain–computer interfaces look unlikely as a source of superintelligence.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：Brain–computer interfaces look unlikely as a source of superintelligence.


口径与范围：核验对象：Brain–computer interfaces look unlikely as a source of superintelligence.
判定：脑机接口仍远离超级智能来源，方向与“看起来不太可能”一致，但超级智能本身尚未出现，不能视为终点已验证。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-464ab5024a01](https://www.nature.com/articles/s44222-024-00239-5)；[ev-43aa6f41ebe7](https://leap.forecastingresearch.org/reports/wave8)

### 44. TXT 第 2878 行 · 暂无法判断

记录：`txt-24d36f2b5e-000164601-000164732`

原文：Improvements in networks and organizations might result in weakly superintelligent forms of collective intelligence in the long run

时间窗口：原文写出（in the long run）。

扩展观点（解释，非原文）：Improvements in networks and organizations might result in weakly superintelligent forms of collective intelligence in the long run.


口径与范围：核验对象：Improvements in networks and organizations might result in weakly superintelligent forms of collective intelligence in the long run.
判定：“长期来看”的弱超级智能集体智能尚未成为可核验的既成事实。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-2b24180d50bc](https://ai100.stanford.edu/reports/2026-report/standing-questions/sq5-what-are-prospects-more-general-artificial-intelligence)

### 45. TXT 第 2901—2902 行 · 暂无法判断

记录：`txt-24d36f2b5e-000165933-000166028`

原文：Machines have a number of fundamental advantages which will give
them overwhelming superiority.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：Machines have fundamental advantages that will give them overwhelming superiority over biological minds.


口径与范围：核验对象：Machines have fundamental advantages that will give them overwhelming superiority over biological minds.
判定：机器对生物心智的压倒性优势以机器超级智能为前提，该前提未出现。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-43aa6f41ebe7](https://leap.forecastingresearch.org/reports/wave8)

### 46. TXT 第 2902—2903 行 · 暂无法判断

记录：`txt-24d36f2b5e-000166029-000166085`

原文：Biological humans, even if enhanced, will
be outclassed.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：Biological humans, even if genetically or otherwise enhanced, will be outclassed by machine intelligence.


口径与范围：核验对象：Biological humans, even if genetically or otherwise enhanced, will be outclassed by machine intelligence.
判定：增强后的生物人是否会被机器智能全面超越，取决于后者已经出现，目前无法判定。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-43aa6f41ebe7](https://leap.forecastingresearch.org/reports/wave8)

### 47. TXT 第 2905—2906 行 · 正确

记录：`txt-24d36f2b5e-000166301-000166394`

原文：The range of
specific tasks that can be better performed by software will continue to expand.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：The range of specific tasks that software can perform better than humans will continue to expand.


口径与范围：核验对象：The range of specific tasks that software can perform better than humans will continue to expand.
判定：2014年后软件在围棋、蛋白质折叠、图像识别、翻译和语音等许多具体任务上超过人类，可更好由软件完成的任务范围明显扩大。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-3fd2b59f3615](https://ourworldindata.org/brief-history-of-ai)；[ev-565c29ae5290](https://en.wikipedia.org/wiki/Progress_in_artificial_intelligence)

### 48. TXT 第 3154—3155 行 · 暂无法判断

记录：`txt-24d36f2b5e-000187072-000187234`

原文：The far greater changes in computing resources and
architecture that machine intelligence will enable will probably have consequences that are even more profound.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：The far greater changes in computing resources and architecture that machine intelligence will enable will probably have even more profound consequences than the minor brain differences between humans and other apes.


口径与范围：核验对象：The far greater changes in computing resources and architecture that machine intelligence will enable will probably have even more profound consequences than the minor brain differences between humans
判定：机器智能将带来比人猿脑差异更深远的后果，取决于相关机器智能已经出现。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-43aa6f41ebe7](https://leap.forecastingresearch.org/reports/wave8)

### 49. TXT 第 3210—3211 行 · 正确

记录：`txt-24d36f2b5e-000192027-000192174`

原文：But hardware is rapidly improving, and the ultimate limits of hardware performance are vastly higher than those of biological
computing substrates.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：Computing hardware is rapidly improving, and its ultimate performance limits are vastly higher than those of biological computing substrates.


口径与范围：核验对象：Computing hardware is rapidly improving, and its ultimate performance limits are vastly higher than those of biological computing substrates.
判定：硬件持续改进：前沿模型训练算力约每年增长4–5倍，GPU性价比也在提升；生物计算衬底的物理上限仍远高于当前水平。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-86203ea531d8](https://epoch.ai/data-insights/compute-trend-post-2010)；[ev-dc39772c2f8f](https://epoch.ai/publications/trends-in-gpu-price-performance)

### 50. TXT 第 3263 行 · 暂无法判断

记录：`txt-24d36f2b5e-000196253-000196335`

原文：Given that machines will eventually vastly exceed biology in general intelligence,

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：Machines will eventually vastly exceed biology in general intelligence.


口径与范围：核验对象：Machines will eventually vastly exceed biology in general intelligence.
判定：“最终将在通用智能上大幅超越生物学”的终点尚未到来。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-43aa6f41ebe7](https://leap.forecastingresearch.org/reports/wave8)

### 51. TXT 第 3387—3389 行 · 暂无法判断

记录：`txt-24d36f2b5e-000205186-000205345`

原文：this chapter will present some reasons for thinking that the slow
transition scenario is improbable. If and when a takeoff occurs, it will likely be
explosive.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：If and when an intelligence takeoff occurs, it will likely be explosive; a slow transition is improbable.


口径与范围：核验对象：If and when an intelligence takeoff occurs, it will likely be explosive; a slow transition is improbable.
判定：智能起飞尚未发生，无法核验它是否会是爆炸性的。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：not_met。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-43aa6f41ebe7](https://leap.forecastingresearch.org/reports/wave8)

### 52. TXT 第 3438 行 · 正确

记录：`txt-24d36f2b5e-000208638-000208723`

原文：Pharmacological enhancers might deliver some cognitive gains over the coming decades.

时间窗口：原文写出（the coming decades）。

扩展观点（解释，非原文）：Pharmacological cognitive enhancers might deliver some cognitive gains over the coming decades.


口径与范围：核验对象：Pharmacological cognitive enhancers might deliver some cognitive gains over the coming decades.
判定：随后十多年的综述显示，莫达非尼和兴奋剂等可带来一定认知增益，虽然幅度有限，与“可能带来一些认知增益”相符。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-b346c5ada623](https://pubmed.ncbi.nlm.nih.gov/31433334/)；[ev-e75b9c276341](https://ncbi.nlm.nih.gov/pmc/articles/PMC7826302/)

### 53. TXT 第 3439—3440 行 · 暂无法判断

记录：`txt-24d36f2b5e-000208924-000208978`

原文：subsequent gains will
be increasingly hard to come by.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：After the easiest nootropic fixes, subsequent cognitive gains will be increasingly hard to come by.


口径与范围：核验对象：After the easiest nootropic fixes, subsequent cognitive gains will be increasingly hard to come by.
判定：难以确认“最容易的改进”是否已经完成，以及此后增益是否确实越来越难获得。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：not_met。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-15a4917c4f1e](https://pubmed.ncbi.nlm.nih.gov/32709551/)

### 54. TXT 第 3452—3453 行 · 正确

记录：`txt-24d36f2b5e-000210007-000210123`

原文：Genetic enhancement will get easier as technology is developed for cheap
and effective genetic testing and selection

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：Genetic cognitive enhancement will get easier as cheap and effective genetic testing and selection are developed.


口径与范围：核验对象：Genetic cognitive enhancement will get easier as cheap and effective genetic testing and selection are developed.
判定：廉价基因检测和多基因评分使选择变得更容易，相关技术成本下降并进入商业胚胎筛查。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-88590988d337](https://academic.oup.com/humupd/article/30/5/529/7684172)；[ev-edcb98d55e65](https://www.theatlantic.com/health/archive/2025/01/polygenic-risk-score-ivf/681323/)

### 55. TXT 第 3479—3482 行 · 暂无法判断

记录：`txt-24d36f2b5e-000212349-000212639`

原文：collective intelligence, with a recalcitrance that seems at
the moment to be in the moderate range—progress is somewhat swift but a lot of
effort is going into making this progress happen. It may be expected to increase as
low-hanging fruits (such as search engines and email) are depleted.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：Recalcitrance to further gains in Internet-enabled collective intelligence may be expected to increase as low-hanging fruits such as search engines and email are depleted.


口径与范围：核验对象：Recalcitrance to further gains in Internet-enabled collective intelligence may be expected to increase as low-hanging fruits such as search engines and email are depleted.
判定：互联网集体智能的改进难度是否因低垂果实耗尽而上升，并没有单一可核验的指标；随后又出现了大语言模型等新工具。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-5642ba2e1e7d](https://en.wikipedia.org/wiki/Transformer_(deep_learning))

### 56. TXT 第 3493—3494 行 · 部分符合

记录：`txt-24d36f2b5e-000213438-000213646`

原文：It is entirely possible that the quest for artificial intelligence will appear to be lost in dense jungle until an unexpected breakthrough
reveals the finishing line in a clearing just a few short steps away.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：It is entirely possible that the quest for AI will appear lost until an unexpected breakthrough suddenly reveals that human-level AI is only a few short steps away.


口径与范围：核验对象：It is entirely possible that the quest for AI will appear lost until an unexpected breakthrough suddenly reveals that human-level AI is only a few short steps away.
判定：2017年Transformer和此后的大规模语言模型带有“看似胶着后突然出现突破”的色彩，但并未证明人类水平人工智能的终点已近在咫尺。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-5642ba2e1e7d](https://en.wikipedia.org/wiki/Transformer_(deep_learning))；[ev-43aa6f41ebe7](https://leap.forecastingresearch.org/reports/wave8)

### 57. TXT 第 3587—3589 行 · 暂无法判断

记录：`txt-24d36f2b5e-000222193-000222432`

原文：It will almost certainly prove harder and take longer to build a machine
intelligence that has a general level of smartness comparable to that of a village idiot than to
improve such a system so that it becomes much smarter than any human.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：It will almost certainly prove harder and take longer to build a machine intelligence at the general smartness of a village idiot than to improve such a system until it is much smarter than any human.


口径与范围：核验对象：It will almost certainly prove harder and take longer to build a machine intelligence at the general smartness of a village idiot than to improve such a system until it is much smarter than any human.
判定：尚无公认的、达到“乡村白痴”级通用机器智能的系统，因此无法核验从这一水平再提升到远超人类是否会更容易、更快。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-43aa6f41ebe7](https://leap.forecastingresearch.org/reports/wave8)

### 58. TXT 第 3677—3680 行 · 正确

记录：`txt-24d36f2b5e-000229841-000230074`

原文：Although one cannot bank on this rate of improvement
continuing up to the development of human-level machine intelligence, yet until
fundamental physical limits are reached there will remain room for advances in
computing technology.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：One cannot bank on computing power per dollar continuing to double every 18 months until human-level machine intelligence, but until fundamental physical limits are reached there will remain room for advances in computing technology.


口径与范围：核验对象：One cannot bank on computing power per dollar continuing to double every 18 months until human-level machine intelligence, but until fundamental physical limits are reached there will remain room for 
判定：不能再指望按美元每18个月翻一番一直持续，但在物理极限之前计算技术仍有改进空间，且已被GPU、集群和更长训练所利用。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-dc39772c2f8f](https://epoch.ai/publications/trends-in-gpu-price-performance)；[ev-86203ea531d8](https://epoch.ai/data-insights/compute-trend-post-2010)

### 59. TXT 第 3686—3687 行 · 暂无法判断

记录：`txt-24d36f2b5e-000230762-000230962`

原文：In summary, we can talk about the likelihood of a hardware overhang: when
human-level software is created, enough computing power may already be available to run vast numbers of copies at great speed.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：When human-level software is created, enough computing power may already be available to run vast numbers of copies at great speed (a hardware overhang).


口径与范围：核验对象：When human-level software is created, enough computing power may already be available to run vast numbers of copies at great speed (a hardware overhang).
判定：人类水平软件尚未被创造，硬件过剩是否会出现无法核验。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：not_met。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-43aa6f41ebe7](https://leap.forecastingresearch.org/reports/wave8)

### 60. TXT 第 3734—3737 行 · 暂无法判断

记录：`txt-24d36f2b5e-000234920-000235215`

原文：likely that the applied optimization power will increase during the
transition: initially because humans try harder to improve a machine intelligence
that is showing spectacular promise, later because the machine intelligence itself
becomes capable of driving further progress at digital speeds.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：Applied optimization power will likely increase during the takeoff transition, first because humans try harder and later because the machine itself drives further progress at digital speeds.


口径与范围：核验对象：Applied optimization power will likely increase during the takeoff transition, first because humans try harder and later because the machine itself drives further progress at digital speeds.
判定：判断针对起飞过渡期，该阶段尚未开始。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：not_met。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-43aa6f41ebe7](https://leap.forecastingresearch.org/reports/wave8)

### 61. TXT 第 3737—3739 行 · 暂无法判断

记录：`txt-24d36f2b5e-000235216-000235366`

原文：This would create
a real possibility of a fast or medium takeoff even if recalcitrance were constant or
slightly increasing around the human baseline.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：Rising optimization power would create a real possibility of a fast or medium takeoff even if recalcitrance were constant or slightly increasing around the human baseline.


口径与范围：核验对象：Rising optimization power would create a real possibility of a fast or medium takeoff even if recalcitrance were constant or slightly increasing around the human baseline.
判定：关于起飞速度的可能性判断，起飞尚未发生。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：not_met。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-43aa6f41ebe7](https://leap.forecastingresearch.org/reports/wave8)

### 62. TXT 第 3863—3865 行 · 暂无法判断

记录：`txt-24d36f2b5e-000242109-000242234`

原文：For these reasons, although a fast
or medium takeoff looks more likely, the possibility of a slow takeoff cannot be
excluded.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：Although a fast or medium takeoff looks more likely, the possibility of a slow takeoff cannot be excluded.


口径与范围：核验对象：Although a fast or medium takeoff looks more likely, the possibility of a slow takeoff cannot be excluded.
判定：快速或中速起飞看起来更可能、慢速不能排除，属于对尚未发生之起飞的事先判断。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-43aa6f41ebe7](https://leap.forecastingresearch.org/reports/wave8)

### 63. TXT 第 4143—4145 行 · 正确

记录：`txt-24d36f2b5e-000251911-000252162`

原文：It is possible that globalization and increased surveillance will reduce typical lags between competing technology projects. Yet there is likely to be a lower
bound on how short the average lag could become (in the absence of deliberate
coordination).

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：Globalization and increased surveillance may reduce typical lags between competing technology projects, but there is likely a lower bound on how short the average lag could become in the absence of deliberate coordination.


口径与范围：核验对象：Globalization and increased surveillance may reduce typical lags between competing technology projects, but there is likely a lower bound on how short the average lag could become in the absence of de
判定：全球化与开源使部分技术差距缩短到数月量级，但领先与跟随项目之间仍存在不可压缩的滞后期，并未降到零。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-b64d68e333b3](https://www.wired.com/story/stanford-study-global-artificial-intelligence-index/)；[ev-44eabfd09ca2](https://hai.stanford.edu/assets/files/ai_index_report_2026_chapter_1_research_development.pdf)

### 64. TXT 第 4152—4154 行 · 暂无法判断

记录：`txt-24d36f2b5e-000252691-000252950`

原文：it is highly unlikely that two projects would be close
enough to undergo a fast takeoff concurrently; for a medium takeoff, it could easily go either way; and for a slow takeoff, it is highly likely that several projects
would undergo the process in parallel.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：It is highly unlikely that two projects would undergo a fast takeoff concurrently; for a medium takeoff it could go either way; for a slow takeoff it is highly likely that several projects would undergo the process in parallel.


口径与范围：核验对象：It is highly unlikely that two projects would undergo a fast takeoff concurrently; for a medium takeoff it could go either way; for a slow takeoff it is highly likely that several projects would under
判定：关于不同起飞速度下有多少项目会并行进入起飞的判断，起飞尚未发生。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-43aa6f41ebe7](https://leap.forecastingresearch.org/reports/wave8)

### 65. TXT 第 4183—4185 行 · 暂无法判断

记录：`txt-24d36f2b5e-000255193-000255372`

原文：a scenario of this kind is a serious possibility, and it increases the chances
that the leading project will attain a decisive strategic advantage even if the takeoff
is not fast.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：Because of explosive growth just after the crossover, the leading project may attain a decisive strategic advantage even if the takeoff is not fast.


口径与范围：核验对象：Because of explosive growth just after the crossover, the leading project may attain a decisive strategic advantage even if the takeoff is not fast.
判定：以起飞发生并出现交叉点后的爆炸性增长为前提，前提未出现。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：not_met。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-43aa6f41ebe7](https://leap.forecastingresearch.org/reports/wave8)

### 66. TXT 第 4197—4198 行 · 暂无法判断

记录：`txt-24d36f2b5e-000256327-000256378`

原文：A lone hacker scen­
ario cannot be excluded either.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：A lone-hacker scenario for building a seed AI cannot be excluded, and the last critical breakthrough might come from a single individual or a small group.


口径与范围：核验对象：A lone-hacker scenario for building a seed AI cannot be excluded, and the last critical breakthrough might come from a single individual or a small group.
判定：“不能排除孤独黑客场景”是可能性判断，无法用已实现结果判定对错。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-20dfb5ccf00b](https://ai100.stanford.edu/reports/2026-report/deep-dives/deep-dive-two-scaling-era)

### 67. TXT 第 4200—4201 行 · 暂无法判断

记录：`txt-24d36f2b5e-000256514-000256668`

原文：it is possible that the last critical breakthrough idea might come from
a single individual or a small group that succeeds in putting everything together.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：The last critical breakthrough idea for a seed AI might come from a single individual or a small group that succeeds in putting everything together.


口径与范围：核验对象：The last critical breakthrough idea for a seed AI might come from a single individual or a small group that succeeds in putting everything together.
判定：最后关键突破是否会来自个人或小团体，取决于该突破已经发生。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-20dfb5ccf00b](https://ai100.stanford.edu/reports/2026-report/deep-dives/deep-dive-two-scaling-era)

### 68. TXT 第 4208—4210 行 · 暂无法判断

记录：`txt-24d36f2b5e-000257161-000257365`

原文：The likelihood of the final breakthrough being made by a small project increases
if most previous progress in the field has been published in the open literature or
made available as open source software.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：The likelihood that the final AI breakthrough is made by a small project increases if most previous progress has been published openly or made available as open-source software.


口径与范围：核验对象：The likelihood that the final AI breakthrough is made by a small project increases if most previous progress has been published openly or made available as open-source software.
判定：开放文献与开源软件是否提高小项目做出最后突破的可能性，在最后突破尚未出现时无法核验。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：not_met。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-b8efa39ccc7f](https://developers.redhat.com/articles/2026/01/07/state-open-source-ai-models-2025)；[ev-20dfb5ccf00b](https://ai100.stanford.edu/reports/2026-report/deep-dives/deep-dive-two-scaling-era)

### 69. TXT 第 4222—4224 行 · 暂无法判断

记录：`txt-24d36f2b5e-000258174-000258297`

原文：governments would
likely seek to nationalize any project on their territory that they thought close
to achieving a takeoff.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：Governments would likely seek to nationalize any project on their territory that they thought close to achieving a takeoff.


口径与范围：核验对象：Governments would likely seek to nationalize any project on their territory that they thought close to achieving a takeoff.
判定：尚未有被当局认定“接近起飞”的具体项目被国有化，触发条件并不清楚是否已经满足。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：not_met。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-3baca624b6e3](https://www.thecairoreview.com/essays/will-washington-and-beijing-nationalize-ai-labs/)；[ev-9877843f6ae0](https://www.insidedeeptech.com/global-agi-regulations-2026-september-update/)

### 70. TXT 第 4235—4238 行 · 部分符合

记录：`txt-24d36f2b5e-000259272-000259569`

原文：If and when
it becomes a common belief among prestigious scientists that there is a substantial chance that superintelligence is just around the corner, the major intelligence
agencies of the world would probably start to monitor groups and individuals who
seem to be engaged in relevant research.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：If and when it becomes a common belief among prestigious scientists that there is a substantial chance superintelligence is just around the corner, the major intelligence agencies of the world would probably start to monitor relevant researchers.


口径与范围：核验对象：If and when it becomes a common belief among prestigious scientists that there is a substantial chance superintelligence is just around the corner, the major intelligence agencies of the world would p
判定：2023年后辛顿、本吉奥等著名科学家公开警告，英美等国建立了安全研究所并加强对前沿实验室的评估与报告要求，但并非古典意义上情报机构对研究人员的全面监控。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-587a6715a0cb](https://www.gov.uk/government/publications/ai-safety-institute-overview/introducing-the-ai-safety-institute)；[ev-5308e74db8d6](https://www.federalregister.gov/documents/2023/11/01/2023-24283/safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence?%3F%3F%3Futm_source=adzuna)

### 71. TXT 第 4239—4241 行 · 部分符合

记录：`txt-24d36f2b5e-000259658-000259792`

原文：If political elites were persuaded
by the seriousness of the risk, civilian efforts in sensitive areas might be regulated
or outlawed.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：If political elites were persuaded by the seriousness of the risk, civilian efforts in sensitive areas might be regulated or outlawed.


口径与范围：核验对象：If political elites were persuaded by the seriousness of the risk, civilian efforts in sensitive areas might be regulated or outlawed.
判定：政治精英在一定程度上接受了风险讨论，欧盟人工智能法、出口管制和行政令等已对民用前沿活动加以监管，但并未禁止或取缔民用通用人工智能研究。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-8a3acd42a39b](https://www.bbc.com/future/article/20231107-why-global-regulation-of-artificial-intelligence-is-still-a-long-way-off)；[ev-9877843f6ae0](https://www.insidedeeptech.com/global-agi-regulations-2026-september-update/)

### 72. TXT 第 4279—4281 行 · 部分符合

记录：`txt-24d36f2b5e-000263076-000263262`

原文：a total intelligence failure cannot be ruled out. Such a failure is
especially likely if breakthroughs should occur in the nearer future, before the
issue has risen to public prominence.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：A total intelligence-agency failure to see an intelligence explosion coming cannot be ruled out, and is especially likely if breakthroughs occur in the nearer future before the issue has risen to public prominence.


口径与范围：核验对象：A total intelligence-agency failure to see an intelligence explosion coming cannot be ruled out, and is especially likely if breakthroughs occur in the nearer future before the issue has risen to publ
判定：议题在起飞发生前已进入公众视野，降低了“在声名远扬前突然突破导致完全情报失败”的特定情形；但“不能排除完全失败”本身仍无法被证伪。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-587a6715a0cb](https://www.gov.uk/government/publications/ai-safety-institute-overview/introducing-the-ai-safety-institute)；[ev-1f082f090f5c](https://pubmed.ncbi.nlm.nih.gov/38768279/)

### 73. TXT 第 4672—4673 行 · 暂无法判断

记录：`txt-24d36f2b5e-000289843-000289959`

原文：A project that controls the first superintelligence in the world
would probably have a decisive strategic advantage.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：A project that controls the first superintelligence in the world would probably have a decisive strategic advantage.


口径与范围：核验对象：A project that controls the first superintelligence in the world would probably have a decisive strategic advantage.
判定：世界上第一个超级智能尚未出现，其控制者是否会获得决定性战略优势无法核验。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-43aa6f41ebe7](https://leap.forecastingresearch.org/reports/wave8)

### 74. TXT 第 4833—4836 行 · 暂无法判断

记录：`txt-24d36f2b5e-000300956-000301250`

原文：a superintelligence—at least in the absence
of intellectual peers and in the absence of effective safety measures arranged by
humans in advance—would likely produce an outcome that would involve reconfiguring terrestrial resources into whatever structures maximize the realization
of its goals.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：In the absence of intellectual peers and of effective safety measures arranged by humans in advance, a superintelligence would likely reconfigure terrestrial resources into whatever structures maximize the realization of its goals.


口径与范围：核验对象：In the absence of intellectual peers and of effective safety measures arranged by humans in advance, a superintelligence would likely reconfigure terrestrial resources into whatever structures maximiz
判定：以无智力同侪且事先缺乏有效安全措施的超级智能为前提，前提未出现。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：not_met。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-43aa6f41ebe7](https://leap.forecastingresearch.org/reports/wave8)

### 75. TXT 第 5027—5029 行 · 暂无法判断

记录：`txt-24d36f2b5e-000316689-000316790`

原文：With
a fast or medium takeoff, it is likely that one project will get a decisive strategic
advantage.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：With a fast or medium takeoff, it is likely that one project will get a decisive strategic advantage.


口径与范围：核验对象：With a fast or medium takeoff, it is likely that one project will get a decisive strategic advantage.
判定：以快速或中速起飞为前提，起飞尚未发生。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：not_met。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-43aa6f41ebe7](https://leap.forecastingresearch.org/reports/wave8)

### 76. TXT 第 5029—5030 行 · 暂无法判断

记录：`txt-24d36f2b5e-000316818-000316945`

原文：a superintelligence with a decisive strategic advantage would have immense powers, enough that it could form a stable
singleton

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：A superintelligence with a decisive strategic advantage would have immense powers, enough that it could form a stable singleton.


口径与范围：核验对象：A superintelligence with a decisive strategic advantage would have immense powers, enough that it could form a stable singleton.
判定：拥有决定性战略优势的超级智能尚未出现。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：not_met。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-43aa6f41ebe7](https://leap.forecastingresearch.org/reports/wave8)

### 77. TXT 第 5109—5111 行 · 正确

记录：`txt-24d36f2b5e-000322177-000322312`

原文：it would
be easier to create an AI with simple goals like these than to build one that had
a human-like set of values and dispositions.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：It would be easier to create an AI with simple goals (such as maximizing paperclips) than to build one with a human-like set of values and dispositions.


口径与范围：核验对象：It would be easier to create an AI with simple goals (such as maximizing paperclips) than to build one with a human-like set of values and dispositions.
判定：相对而言，安装简单代理目标或优化指标远比编码人类价值体系容易，对齐文献在2014–2026年间持续记录了这一不对称。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-1706b4eb3d1d](https://dl.acm.org/doi/full/10.1145/3770749)；[ev-101e892046a7](https://theconversation.com/the-decades-old-ai-alignment-problem-has-finally-become-a-reality-solving-it-wont-be-easy-289812)

### 78. TXT 第 5115—5118 行 · 部分符合

记录：`txt-24d36f2b5e-000322628-000322878`

原文：a meaningless reductionistic goal is
easier for humans to code and easier for an AI to learn, it is just the kind of goal
that a programmer would choose to install in his seed AI if his focus is on taking
the quickest path to “getting the AI to work”

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：Because a meaningless reductionistic goal is easier for humans to code and for an AI to learn, it is the kind of goal a programmer would choose to install in a seed AI if the focus is on the quickest path to getting the AI to work.


口径与范围：核验对象：Because a meaningless reductionistic goal is easier for humans to code and for an AI to learn, it is the kind of goal a programmer would choose to install in a seed AI if the focus is on the quickest 
判定：能力优先、先让系统“能用”的激励确实存在，但前沿实验室同时也投入了对齐与安全，并未普遍把无意义的还原论目标装进种子系统。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-1706b4eb3d1d](https://dl.acm.org/doi/full/10.1145/3770749)；[ev-31fff03d4c6e](https://openai.com/index/frontier-model-forum/)

### 79. TXT 第 5440—5441 行 · 暂无法判断

记录：`txt-24d36f2b5e-000348117-000348217`

原文：a
plausible default outcome of the creation of machine superintelligence is existential catastrophe.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：A plausible default outcome of the creation of machine superintelligence is existential catastrophe.


口径与范围：核验对象：A plausible default outcome of the creation of machine superintelligence is existential catastrophe.
判定：机器超级智能尚未被创造，其“说得通的默认结果是存在性灾难”无法用已实现结果判定。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：not_met。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-43aa6f41ebe7](https://leap.forecastingresearch.org/reports/wave8)

### 80. TXT 第 5454—5455 行 · 暂无法判断

记录：`txt-24d36f2b5e-000349487-000349613`

原文：This suggests that—absent a special effort—the first superintelligence may
have some such random or reductionistic final goal.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：Absent a special effort, the first superintelligence may have some random or reductionistic final goal.


口径与范围：核验对象：Absent a special effort, the first superintelligence may have some random or reductionistic final goal.
判定：第一个超级智能尚未出现，是否会在缺乏专门努力时带有任意或还原论的最终目标，尚无法核验。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：not_met。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-43aa6f41ebe7](https://leap.forecastingresearch.org/reports/wave8)

### 81. TXT 第 5468—5469 行 · 暂无法判断

记录：`txt-24d36f2b5e-000350699-000350773`

原文：the outcome could easily be one in which humanity quickly becomes
extinct.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：The outcome of an unaligned first superintelligence could easily be one in which humanity quickly becomes extinct.


口径与范围：核验对象：The outcome of an unaligned first superintelligence could easily be one in which humanity quickly becomes extinct.
判定：未对齐的第一个超级智能是否会轻易导致人类灭绝，取决于该系统已经出现。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-43aa6f41ebe7](https://leap.forecastingresearch.org/reports/wave8)

### 82. TXT 第 5611—5612 行 · 正确

记录：`txt-24d36f2b5e-000361923-000362039`

原文：Benign
failures are bound to occur many times between now and the eventual development of machine superintelligence.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：Benign failures are bound to occur many times between now and the eventual development of machine superintelligence.


口径与范围：核验对象：Benign failures are bound to occur many times between now and the eventual development of machine superintelligence.
判定：在机器超级智能到来之前，已经多次出现资金中断、路线失败或未达到宣称目标的良性失败，与“必定会发生许多次”相符。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-565c29ae5290](https://en.wikipedia.org/wiki/Progress_in_artificial_intelligence)；[ev-43aa6f41ebe7](https://leap.forecastingresearch.org/reports/wave8)

### 83. TXT 第 6173 行 · 正确

记录：`txt-24d36f2b5e-000405909-000406037`

原文：Richer and more complicated virtual worlds will become feasible with improvements in programming techniques and computing power.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：Richer and more complicated virtual worlds will become feasible with improvements in programming techniques and computing power.


口径与范围：核验对象：Richer and more complicated virtual worlds will become feasible with improvements in programming techniques and computing power.
判定：游戏世界、虚拟现实和生成式三维场景都比2014年更丰富、更复杂，编程技术与算力的改进确实使更丰富的虚拟世界变得可行。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-ec878d6a65d5](https://www.meta.com/blog/worldgen-3d-world-generation-reality-labs-generative-ai-research/)；[ev-65baaecbe6be](https://arxiv.org/html/2505.05474)

### 84. TXT 第 7310—7312 行 · 排除：非预测

记录：`txt-24d36f2b5e-000491333-000491550`

原文：Demographers project that the world
population will rise to about 9 billion by mid-century, and that it might thereafter
plateau or decline as the poorer countries join the developed world in this lowfertility regime.

时间窗口：原文写出（by mid-century）。

扩展观点（解释，非原文）：Demographers project that world population will rise to about 9 billion by mid-century, and that it might thereafter plateau or decline as poorer countries join the developed world’s low-fertility regime.


口径与范围：不可核验的候选（流水线 resolvable=false）
判定：抽取流水线将其降级为unclear/不可核验，按METHOD.md不进入核验。
限制：非可核验预测
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：流水线归属/可核验规则排除（原文明确；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 85. TXT 第 7314—7316 行 · 暂无法判断

记录：`txt-24d36f2b5e-000491664-000491940`

原文：Yet there are reasons, if we take a longer view and assume a state of unchanging technology and continued prosperity, to expect a return to the historically
and ecologically normal condition of a world population that butts up against
the limits of what our niche can support.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：Taking a longer view, and assuming unchanging technology and continued prosperity, there are reasons to expect a return to a world population that butts up against the limits of what our niche can support.


口径与范围：核验对象：Taking a longer view, and assuming unchanging technology and continued prosperity, there are reasons to expect a return to a world population that butts up against the limits of what our niche can sup
判定：前提要求“技术不变且持续繁荣”；2014年后技术并未冻结，全球生育率也未见回到栖息地极限的趋势。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：not_met。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-e8cad97ce76a](https://www.worldbank.org/en/research/publication/long-term-growth-prospects)

### 86. TXT 第 9952 行 · 趋势符合（最终结果待验证）

记录：`txt-24d36f2b5e-000701025-000701180`

原文：There are several quite strong reasons to believe that the riskiness of an intelligence explosion will decline significantly over a multidecadal timeframe.

时间窗口：原文写出（a multidecadal timeframe）。

扩展观点（解释，非原文）：There are several quite strong reasons to believe that the riskiness of an intelligence explosion will decline significantly over a multidecadal timeframe.


口径与范围：核验对象：There are several quite strong reasons to believe that the riskiness of an intelligence explosion will decline significantly over a multidecadal timeframe.
判定：控制问题与对齐研究在出版后十余年明显推进，为“风险会在数十年尺度上下降”提供了方向性支持，但数十年窗口未结束，实际起飞风险也无法直接测量。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-1706b4eb3d1d](https://dl.acm.org/doi/full/10.1145/3770749)；[ev-101e892046a7](https://theconversation.com/the-decades-old-ai-alignment-problem-has-finally-become-a-reality-solving-it-wont-be-easy-289812)

### 87. TXT 第 9957—9958 行 · 趋势符合（最终结果待验证）

记录：`txt-24d36f2b5e-000701523-000701736`

原文：It is plausible that the state of the art will advance greatly over the
next several decades; and if the problem turns out to be very difficult, a significant rate of progress might continue for a century or more.

时间窗口：原文写出（next several decades）。

扩展观点（解释，非原文）：The state of the art on the control problem will plausibly advance greatly over the next several decades; if the problem is very difficult, a significant rate of progress might continue for a century or more.


口径与范围：核验对象：The state of the art on the control problem will plausibly advance greatly over the next several decades; if the problem is very difficult, a significant rate of progress might continue for a century 
判定：对齐、强化学习人类反馈和可解释性等使控制问题的技术水平在2014年后明显前进，与“未来数十年将大幅前进”的方向一致，但数十年终点未到，问题也仍未解决。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-1706b4eb3d1d](https://dl.acm.org/doi/full/10.1145/3770749)；[ev-2d673683470e](https://www.transformernews.ai/p/no-ai-alignment-isnt-solved)

### 88. TXT 第 9973—9975 行 · 暂无法判断

记录：`txt-24d36f2b5e-000702856-000703141`

原文：an optimist could expect that the “sanity level” of humanity will rise
over the course of this century—that prejudices will (on balance) recede, that
insights will accumulate, and that people will become more accustomed to thinking about abstract future probabilities and global risks.

时间窗口：原文写出（the course of this century）。

扩展观点（解释，非原文）：An optimist could expect that the sanity level of humanity will rise over the course of this century: prejudices receding on balance, insights accumulating, and people becoming more accustomed to thinking about abstract future probabilities and global risks.


口径与范围：核验对象：An optimist could expect that the sanity level of humanity will rise over the course of this century: prejudices receding on balance, insights accumulating, and people becoming more accustomed to thin
判定：这是对乐观主义者可以期待的本世纪趋势的表述，世纪尚未结束，偏见、洞见与抽象风险思维的净变化也缺乏单一可判定的指标。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-1f082f090f5c](https://pubmed.ncbi.nlm.nih.gov/38768279/)

### 89. TXT 第 9977—9978 行 · 正确

记录：`txt-24d36f2b5e-000703304-000703354`

原文：Scientific progress means that
more will be known.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：Scientific progress means that more will be known.


口径与范围：核验对象：Scientific progress means that more will be known.
判定：科学持续产出新知识，研究文献与可获得的实证结果在2014–2026年间明显增加。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-1706b4eb3d1d](https://dl.acm.org/doi/full/10.1145/3770749)；[ev-565c29ae5290](https://en.wikipedia.org/wiki/Progress_in_artificial_intelligence)

### 90. TXT 第 9978—9980 行 · 部分符合

记录：`txt-24d36f2b5e-000703355-000703562`

原文：Economic growth may give a greater portion of the world’s
population adequate nutrition (particularly during the early years of life that are
important for brain development) and access to quality education.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：Economic growth may give a greater portion of the world’s population adequate nutrition (especially early in life) and access to quality education.


口径与范围：核验对象：Economic growth may give a greater portion of the world’s population adequate nutrition (especially early in life) and access to quality education.
判定：互联网普及和教育完成率等有所提高，但新冠疫情使中低收入国家的学习贫困显著恶化，营养与优质教育的覆盖并非单纯扩大。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-4193dfea38ae](https://data.worldbank.org/indicator/IT.NET.USER.ZS?locations=1W)；[ev-7d63d196b034](https://www.worldbank.org/en/news/press-release/2022/06/23/70-of-10-year-olds-now-in-learning-poverty-unable-to-read-and-understand-a-simple-text)

### 91. TXT 第 9980—9981 行 · 正确

记录：`txt-24d36f2b5e-000703563-000703679`

原文：Advances in
information technology will make it easier to find, integrate, evaluate, and communicate data and ideas.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：Advances in information technology will make it easier to find, integrate, evaluate, and communicate data and ideas.


口径与范围：核验对象：Advances in information technology will make it easier to find, integrate, evaluate, and communicate data and ideas.
判定：搜索、学术数据库、移动互联网和大语言模型使查找、整合、评估和交流数据与观念明显更容易。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-4193dfea38ae](https://data.worldbank.org/indicator/IT.NET.USER.ZS?locations=1W)；[ev-5642ba2e1e7d](https://en.wikipedia.org/wiki/Transformer_(deep_learning))

### 92. TXT 第 9981—9983 行 · 暂无法判断

记录：`txt-24d36f2b5e-000703693-000703832`

原文：by the century’s end, humanity will have
made an additional hundred years’ worth of mistakes, from which something
might have been learned.

时间窗口：原文写出（the century’s end）。

扩展观点（解释，非原文）：By the century’s end, humanity will have made an additional hundred years’ worth of mistakes, from which something might have been learned.


口径与范围：核验对象：By the century’s end, humanity will have made an additional hundred years’ worth of mistakes, from which something might have been learned.
判定：终点是本世纪末，目前无法判定是否会从额外一百年的错误中学到东西。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 93. TXT 第 10161—10162 行 · 暂无法判断

记录：`txt-24d36f2b5e-000718973-000719126`

原文：it is possible that progress toward whole
brain emulation will not yield whole brain emulation. It may instead yield neuromorphic artificial intelligence

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：It is possible that progress toward whole brain emulation will not yield whole brain emulation, but neuromorphic artificial intelligence instead.


口径与范围：核验对象：It is possible that progress toward whole brain emulation will not yield whole brain emulation, but neuromorphic artificial intelligence instead.
判定：全脑仿真路径尚未走到岔口，是否会先得到神经形态人工智能只是一种可能性，无法判定。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-0283cb442ec3](https://defensesindepth.bio/will-whole-brain-emulation-matter-for-the-ai-transition/)

### 94. TXT 第 10484—10485 行 · 正确

记录：`txt-24d36f2b5e-000744129-000744221`

原文：With AI it is always possible that somebody will
make an unexpected conceptual breakthrough.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：With AI it is always possible that somebody will make an unexpected conceptual breakthrough.


口径与范围：核验对象：With AI it is always possible that somebody will make an unexpected conceptual breakthrough.
判定：2017年Transformer论文构成一次事先难以精确预期的概念突破，说明“始终可能有人做出出乎意料的概念突破”在窗口内已经应验。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-5642ba2e1e7d](https://en.wikipedia.org/wiki/Transformer_(deep_learning))；[ev-9e7754ff2e3c](https://www.technologyreview.com/2023/02/08/1068068/chatgpt-is-everywhere-heres-where-it-came-from/)

### 95. TXT 第 10487 行 · 趋势符合（最终结果待验证）

记录：`txt-24d36f2b5e-000744379-000744485`

原文：We can therefore be confident that WBE is not imminent (not less than, say, fifteen or twenty years away).

时间窗口：原文写出（fifteen or twenty years away）。

扩展观点（解释，非原文）：Whole brain emulation is not imminent: not less than about fifteen or twenty years away (from 2014, i.e. not before about 2029–2034).


口径与范围：核验对象：Whole brain emulation is not imminent: not less than about fifteen or twenty years away (from 2014, i.e. not before about 2029–2034).
判定：人类全脑仿真在2026年仍未被认为迫在眉睫，与“至少还要十五到二十年（约至2029–2034年）”的方向一致，但窗口尚未完全结束。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-e5088ffcdbc9](https://alleninstitute.org/news/how-far-are-we-from-a-human-brain-simulation-and-what-does-that-mean-for-science)；[ev-0283cb442ec3](https://defensesindepth.bio/will-whole-brain-emulation-matter-for-the-ai-transition/)

### 96. TXT 第 10549—10551 行 · 正确

记录：`txt-24d36f2b5e-000749039-000749213`

原文：In the development of machine superintelligence, it seems likely that there will
be at least a mild race dynamic, and it is possible that there will be a severe race
dynamic.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：In the development of machine superintelligence, it seems likely that there will be at least a mild race dynamic, and it is possible that there will be a severe race dynamic.


口径与范围：核验对象：In the development of machine superintelligence, it seems likely that there will be at least a mild race dynamic, and it is possible that there will be a severe race dynamic.
判定：OpenAI、Google DeepMind、Anthropic等实验室以及中美之间已形成被广泛讨论的人工智能竞赛，至少出现了轻度甚至更强的竞赛动态。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-a4da12ab6a0f](https://www.foreignaffairs.com/united-states/china-real-artificial-intelligence-race-innovation)；[ev-b64d68e333b3](https://www.wired.com/story/stanford-study-global-artificial-intelligence-index/)

### 97. TXT 第 10830—10832 行 · 暂无法判断

记录：`txt-24d36f2b5e-000769683-000769855`

原文：The required level of
security might be nearly unattainable at present, but advances in lie detection and
surveillance technology could make it feasible later this century.

时间窗口：原文写出（later this century）。

扩展观点（解释，非原文）：The required level of security for closely held international collaboration might be nearly unattainable at present, but advances in lie detection and surveillance technology could make it feasible later this century.


口径与范围：核验对象：The required level of security for closely held international collaboration might be nearly unattainable at present, but advances in lie detection and surveillance technology could make it feasible la
判定：“本世纪晚些时候”尚未到来；测谎技术仍不可靠，尚不足以支撑高度隔离的国际协作安全水平。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-1f05e93a0497](https://doi.org/10.3390/forensicsci6040094)；[ev-48758e7a6e6e](https://www.pnas.org/doi/10.1073/pnas.2412881121)

### 98. TXT 第 11425—11428 行 · 正确

记录：`txt-24d36f2b5e-000815729-000815974`

原文：Attitudes toward human genetic engin­
eering and embryo selection vary significantly across cultures, suggesting that development
and application of new techniques will probably take place even if some countries initially adopt
a cautious stance

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：Because attitudes toward human genetic engineering and embryo selection vary across cultures, development and application of new techniques will probably take place even if some countries initially adopt a cautious stance, though the rate will be influenced by moral, religious, and political pressures.


口径与范围：核验对象：Because attitudes toward human genetic engineering and embryo selection vary across cultures, development and application of new techniques will probably take place even if some countries initially ad
判定：尽管英国等国禁止或限制多基因胚胎筛查，美国等地已有商业应用，说明即使部分国家持谨慎立场，新技术的开发与应用仍会在其他地方发生。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-fbe7b5da7156](https://www.hfea.gov.uk/about-us/our-blog/pgt-p-is-not-lawful-in-the-uk-is-not-supported-by-evidence-and-may-reduce-the-chances-of-having-a-baby-overall)；[ev-edcb98d55e65](https://www.theatlantic.com/health/archive/2025/01/polygenic-risk-score-ivf/681323/)

### 99. TXT 第 11756 行 · 暂无法判断

记录：`txt-24d36f2b5e-000846542-000846804`

原文：It is of course also possible that there will be no takeoff at all. But since, as argued earlier, superintelligence looks technically feasible, the absence of a takeoff would likely be due to the intervention of some defeater, such as an existential catastrophe.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：It is possible that there will be no takeoff at all; but since superintelligence looks technically feasible, the absence of a takeoff would likely be due to a defeater such as an existential catastrophe.


口径与范围：核验对象：It is possible that there will be no takeoff at all; but since superintelligence looks technically feasible, the absence of a takeoff would likely be due to a defeater such as an existential catastrop
判定：尚未发生起飞并不等于最终不会有起飞，因此无法用当前状态核验“可能完全没有起飞、若无则很可能是因为存在性灾难等挫败因素”。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-43aa6f41ebe7](https://leap.forecastingresearch.org/reports/wave8)

### 100. TXT 第 11799—11801 行 · 正确

记录：`txt-24d36f2b5e-000850437-000850558`

原文：it is
unlikely that there will be a vast number of projects that are each well enough resourced to be
serious contenders.

时间窗口：隐含，从出版年 2014 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：It is unlikely that there will be a vast number of projects that are each well enough resourced to be serious contenders for machine superintelligence.


口径与范围：核验对象：It is unlikely that there will be a vast number of projects that are each well enough resourced to be serious contenders for machine superintelligence.
判定：前沿训练仍集中在少数资金充足的实验室，严肃竞争者是一小撮而非海量，与判断相符。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-44eabfd09ca2](https://hai.stanford.edu/assets/files/ai_index_report_2026_chapter_1_research_development.pdf)；[ev-20dfb5ccf00b](https://ai100.stanford.edu/reports/2026-report/deep-dives/deep-dive-two-scaling-era)

## 证据登记

哈希校验只证明本地保存内容未改变。检索摘录与完整原始文件会按证据记录注明；两者均不能代替对来源与命题对应关系的判断。

- [ev-129f7e9fe4fa](https://tradingeconomics.com/world/full-year-gdp-growth)；资料日期：未确定；覆盖：World Full Year GDP Growth。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-e8cad97ce76a](https://www.worldbank.org/en/research/publication/long-term-growth-prospects)；资料日期：未确定；覆盖：Falling Long-Term Growth Prospects。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-f88f49f8b7da](https://en.wikipedia.org/wiki/2010s_in_science_and_technology)；资料日期：2026-11-10；覆盖：2010s in science and technology。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-5642ba2e1e7d](https://en.wikipedia.org/wiki/Transformer_(deep_learning))；资料日期：2026-11-11；覆盖：Transformer (deep learning)。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-9e7754ff2e3c](https://www.technologyreview.com/2023/02/08/1068068/chatgpt-is-everywhere-heres-where-it-came-from/)；资料日期：2023-02-08；覆盖：ChatGPT is everywhere. Here's where it came from | MIT Technology Review。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-43aa6f41ebe7](https://leap.forecastingresearch.org/reports/wave8)；资料日期：2026-06-01；覆盖：Wave 8: Timelines | LEAP。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-2b24180d50bc](https://ai100.stanford.edu/reports/2026-report/standing-questions/sq5-what-are-prospects-more-general-artificial-intelligence)；资料日期：未确定；覆盖：SQ5. What are the prospects for more general artificial intelligence? | AI100 | One Hundred Year Study on Artificial Intelligence。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-4c37f46e6298](https://en.wikipedia.org/wiki/AlphaGo)；资料日期：2026-11-07；覆盖：AlphaGo。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-674a9aea440f](https://en.wikipedia.org/wiki/AlphaGo_versus_Ke_Jie)；资料日期：2026-09-13；覆盖：AlphaGo versus Ke Jie。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-14cd2e36c188](https://arxiv.org/html/2303.08774v4)；资料日期：未确定；覆盖：GPT-4 Technical Report。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-f9c4697f2479](https://pmc.ncbi.nlm.nih.gov/articles/PMC11840437/)；资料日期：2025-02-20；覆盖：Text understanding in GPT-4 versus humans。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-f72e0b899c01](https://santageai.com/agi/agi-timelines)；资料日期：2026-09-24；覆盖：When Will AGI Arrive? Expert Timelines and Predictions (2026) | Santage。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-86203ea531d8](https://epoch.ai/data-insights/compute-trend-post-2010)；资料日期：2024-06-19；覆盖：The training compute of notable AI models has been doubling roughly every six months | Epoch AI。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-1b34fd454f7e](https://www.fhi.ox.ac.uk/wp-content/uploads/ai-evolution-and-selection-effects.pdf)；资料日期：未确定；覆盖：How Hard is Artificial Intelligence? Evolutionary Arguments and Selection Effects。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-82e25649e888](https://arxiv.org/pdf/2307.10246)；资料日期：2023-07-17；覆盖：Deep Neural Networks and Brain Alignment: Brain Encoding and Decoding (Survey)。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-e184b6e52a0b](https://www.nature.com/articles/s41583-025-00957-8)；资料日期：2025-08-13；覆盖：Synaptic connectomics: status and prospects | Nature Reviews Neuroscience。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-21c582bc458d](https://pmc.ncbi.nlm.nih.gov/articles/PMC13659455/)；资料日期：2026-09-29；覆盖：Connectomes: a re-emerging hub dataset for neuroscience。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-e5088ffcdbc9](https://alleninstitute.org/news/how-far-are-we-from-a-human-brain-simulation-and-what-does-that-mean-for-science)；资料日期：2026-05-21；覆盖：How far are we from a human brain simulation and what does that mean for science?。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-09d1dcb558c0](https://biologyinsights.com/mind-uploading-research-whats-the-current-progress/)；资料日期：2026-09-25；覆盖：Mind Uploading Research: What’s the Current Progress? - Biology Insights。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-0283cb442ec3](https://defensesindepth.bio/will-whole-brain-emulation-matter-for-the-ai-transition/)；资料日期：2026-04-25；覆盖：Will whole brain emulation matter for the AI transition? — Defenses in Depth。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-20dfb5ccf00b](https://ai100.stanford.edu/reports/2026-report/deep-dives/deep-dive-two-scaling-era)；资料日期：未确定；覆盖：Deep Dive Two: The Scaling Era | AI100 | One Hundred Year Study on Artificial Intelligence。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-15a4917c4f1e](https://pubmed.ncbi.nlm.nih.gov/32709551/)；资料日期：未确定；覆盖：How effective are pharmaceuticals for cognitive enhancement in healthy adults? A series of meta-analyses of cognitive performance during acute administration of。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-c04d061e2839](https://link.springer.com/article/10.1007/s40267-023-00989-z?code=25a03bc5-a472-4477-a9f2-d97055a317af&error=cookies_not_supported)；资料日期：2023-04-27；覆盖：Cognitive enhancers in healthy individuals have little benefit and significant potential harms。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-88590988d337](https://academic.oup.com/humupd/article/30/5/529/7684172)；资料日期：2024-05-28；覆盖：Screening embryos for polygenic disease risk: a review of epidemiological, clinical, and ethical considerations | Human Reproduction Update | Oxford Academic。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-9726e3d0d5db](https://www.asrm.org/news-and-events/asrm-news/press-releasesbulletins/asrm-ethics-and-practice-committees-release-new-report-concluding-polygenic-embryo-screening-is-not-ready-for-clinical-use/)；资料日期：2025-12-08；覆盖：ASRM Ethics and Practice Committees Release New Report Concluding Polygenic Embryo Screening Is Not Ready for Clinical Use | American Society for Reproductive M。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-13dc1839a66b](https://www.nature.com/articles/mp201645)；资料日期：2016-04-05；覆盖：Genome-wide association study of cognitive functions and educational attainment in UK Biobank (N=112 151) | Molecular Psychiatry。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-70f3a67b8234](https://pubmed.ncbi.nlm.nih.gov/27225129/)；资料日期：2016-05-26；覆盖：Genome-wide association study identifies 74 loci associated with educational attainment - PubMed。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-0249ba324ebe](https://pmc.ncbi.nlm.nih.gov/articles/PMC11981603/)；资料日期：2024-12-19；覆盖：Promises and pitfalls of preimplantation genetic testing for polygenic disorders: a narrative review。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-fbe7b5da7156](https://www.hfea.gov.uk/about-us/our-blog/pgt-p-is-not-lawful-in-the-uk-is-not-supported-by-evidence-and-may-reduce-the-chances-of-having-a-baby-overall)；资料日期：2026-02-04；覆盖：PGT-P is not lawful in the UK, is not supported by evidence, and may reduce the chances of having a baby overall | HFEA。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-551daaff3e93](https://www.who.int/health-topics/human-genome-editing)；资料日期：未确定；覆盖：Human genome editing。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-85bf5360b552](https://www.cell.com/med/fulltext/S2666-6340(26)00228-X)；资料日期：2026-08-14；覆盖：Ethics of gene therapy: Med。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-741d793b4395](https://www.scmp.com/news/china/politics/article/3270285/china-bans-clinical-research-germline-genome-editing-irresponsible)；资料日期：2024-07-13；覆盖：China bans clinical research in germline genome editing as ‘irresponsible’ | South China Morning Post。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-d78cd2c54f47](https://en.wikipedia.org/wiki/He_Jiankui_affair)；资料日期：2026-11-03；覆盖：He Jiankui affair。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-464ab5024a01](https://www.nature.com/articles/s44222-024-00239-5)；资料日期：2024-09-20；覆盖：The state of clinical trials of implantable brain–computer interfaces | Nature Reviews Bioengineering。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-2ee2ccce1f15](https://www.technologyreview.com/2025/04/01/1114009/brain-computer-interfaces-10-breakthrough-technologies-2025/)；资料日期：2025-04-01；覆盖：Brain-computer interfaces face a critical test | MIT Technology Review。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-ce9fcfc625ed](https://carnegieendowment.org/files/WP-Feldstein-AISurveillance_final.pdf)；资料日期：未确定；覆盖：The Global Expansion of AI Surveillance。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-05328adf0a06](https://www.cctv-focus.com/video-surveillance/vendor-news/ip-camera-boom)；资料日期：2025-09-17；覆盖：Global Surveillance Camera Boom: From 50M to 1.5B Eyes by 2026。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-4e78fc5c2d15](https://www.eff.org/deeplinks/2026/03/think-twice-buying-or-using-metas-ray-bans)；资料日期：2026-03-10；覆盖：Think Twice Before Buying or Using Meta’s Ray-Bans | Electronic Frontier Foundation。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-2d3caa104fb2](https://www.reuters.com/business/media-telecom/smart-glasses-ai-pins-privacy-fears-challenge-techs-next-big-bet-2026-09-22/)；资料日期：2026-09-22；覆盖：From smart glasses to AI pins, privacy fears challenge tech's next big bet | Reuters。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-3fd2b59f3615](https://ourworldindata.org/brief-history-of-ai)；资料日期：未确定；覆盖：How did we get here?。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-565c29ae5290](https://en.wikipedia.org/wiki/Progress_in_artificial_intelligence)；资料日期：2026-11-12；覆盖：Progress in artificial intelligence。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-dc39772c2f8f](https://epoch.ai/publications/trends-in-gpu-price-performance)；资料日期：2022-06-27；覆盖：Trends in GPU price-performance | Epoch AI。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-b346c5ada623](https://pubmed.ncbi.nlm.nih.gov/31433334/)；资料日期：未确定；覆盖：The Efficacy of Modafinil as a Cognitive Enhancer: A Systematic Review and Meta-Analysis - PubMed。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-e75b9c276341](https://ncbi.nlm.nih.gov/pmc/articles/PMC7826302/)；资料日期：未确定；覆盖：Cognitive enhancement effects of stimulants: a randomized controlled trial testing methylphenidate, modafinil, and caffeine。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-edcb98d55e65](https://www.theatlantic.com/health/archive/2025/01/polygenic-risk-score-ivf/681323/)；资料日期：2025-01-15；覆盖：No Genetic Test Can Promise You a Perfect Baby - The Atlantic。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-b64d68e333b3](https://www.wired.com/story/stanford-study-global-artificial-intelligence-index/)；资料日期：2025-04-07；覆盖：The AI Race Has Gotten Crowded—and China Is Closing In on the US | WIRED。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-44eabfd09ca2](https://hai.stanford.edu/assets/files/ai_index_report_2026_chapter_1_research_development.pdf)；资料日期：未确定；覆盖：Research and。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-b8efa39ccc7f](https://developers.redhat.com/articles/2026/01/07/state-open-source-ai-models-2025)；资料日期：2026-01-07；覆盖：The state of open source AI models in 2025 | Red Hat Developer。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-3baca624b6e3](https://www.thecairoreview.com/essays/will-washington-and-beijing-nationalize-ai-labs/)；资料日期：2026-06-17；覆盖：Will Washington and Beijing Nationalize AI Labs? – The Cairo Review of Global Affairs。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-9877843f6ae0](https://www.insidedeeptech.com/global-agi-regulations-2026-september-update/)；资料日期：2026-09-10；覆盖：Global AGI Regulations in 2026 (September 2026 Update)。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-587a6715a0cb](https://www.gov.uk/government/publications/ai-safety-institute-overview/introducing-the-ai-safety-institute)；资料日期：2023-11-02；覆盖：Introducing the AI Safety Institute  - GOV.UK。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-5308e74db8d6](https://www.federalregister.gov/documents/2023/11/01/2023-24283/safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence?%3F%3F%3Futm_source=adzuna)；资料日期：2023-11-01；覆盖：Federal Register
       :: 
      Safe, Secure, and Trustworthy Development and Use of Artificial Intelligence。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-8a3acd42a39b](https://www.bbc.com/future/article/20231107-why-global-regulation-of-artificial-intelligence-is-still-a-long-way-off)；资料日期：2023-11-07；覆盖：AI safety: How close is global regulation of artificial intelligence really?。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-1f082f090f5c](https://pubmed.ncbi.nlm.nih.gov/38768279/)；资料日期：2024-05-20；覆盖：Managing extreme AI risks amid rapid progress。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-1706b4eb3d1d](https://dl.acm.org/doi/full/10.1145/3770749)；资料日期：2025-11-21；覆盖：AI Alignment: A Contemporary Survey | ACM Computing Surveys。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-101e892046a7](https://theconversation.com/the-decades-old-ai-alignment-problem-has-finally-become-a-reality-solving-it-wont-be-easy-289812)；资料日期：2026-08-17；覆盖：The decades-old ‘AI alignment problem’ has finally become a reality. Solving it won’t be easy。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-31fff03d4c6e](https://openai.com/index/frontier-model-forum/)；资料日期：2023-07-26；覆盖：Frontier Model Forum | OpenAI。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-ec878d6a65d5](https://www.meta.com/blog/worldgen-3d-world-generation-reality-labs-generative-ai-research/)；资料日期：2025-11-21；覆盖：Research Update: WorldGen — Text to Immersive 3D Worlds | Meta Quest Blog | Meta。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-65baaecbe6be](https://arxiv.org/html/2505.05474)；资料日期：2026-08-12；覆盖：3D Scene Generation: A Survey。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-2d673683470e](https://www.transformernews.ai/p/no-ai-alignment-isnt-solved)；资料日期：2026-03-18；覆盖：No, AI alignment isn’t solved - by Lynette Bye。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-4193dfea38ae](https://data.worldbank.org/indicator/IT.NET.USER.ZS?locations=1W)；资料日期：未确定；覆盖：Individuals using the Internet (% of population) - World | Data。限制：网页存档（curl），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-7d63d196b034](https://www.worldbank.org/en/news/press-release/2022/06/23/70-of-10-year-olds-now-in-learning-poverty-unable-to-read-and-understand-a-simple-text)；资料日期：2022-06-23；覆盖：70% of 10-Year-Olds now in Learning Poverty, Unable to Read and Understand a Simple Text。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-a4da12ab6a0f](https://www.foreignaffairs.com/united-states/china-real-artificial-intelligence-race-innovation)；资料日期：2025-07-09；覆盖：The Real AI Race: America Needs More Than Innovation to Compete With China。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-1f05e93a0497](https://doi.org/10.3390/forensicsci6040094)；资料日期：2026-10-21；覆盖：Deception Detection Technologies: Current Advances andForensic Challenges。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-48758e7a6e6e](https://www.pnas.org/doi/10.1073/pnas.2412881121)；资料日期：2024-12-06；覆盖：Distinguishing deception from its confounds by improving the validity of fMRI-based neural prediction | PNAS。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
