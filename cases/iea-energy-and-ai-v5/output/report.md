# 能源与人工智能（Energy and AI）：五类评估

证据截止日：2026-11-15。已处理 72/72 条全书候选；尚未处理 0 条。

累计已完成全量抽取复核 72 条；保留旧抽样抽取 0 条，两者不重复相加。

已补充扩展观点 72 条；其中 0 条仍有待确认的代指、对象或范围，已逐条标记。扩展观点不自动改变原有评估。

本轮沿用候选清单逐条核查，不保证没有漏抽。PDF记录使用PDF页码，TXT记录使用原始文本行号。扩展观点是依据所给语境的解释，原文短引文另行保留。

|类别|父记录数|
|---|---:|
|正确|10|
|趋势符合|6|
|部分符合|4|
|错误|1|
|暂无法判断|51|
|排除：非预测|0|
|排除：重复|0|
|尚未处理|0|

可判定覆盖率：21/72 = 29.2%。
绑定外部证据的预测：21/72；未绑定：51。绑定不代表证据充分或研究已完成。
“正确”占已判定记录：10/21 = 47.6%。

趋势符合 6 条单独列出，与部分符合互不重复；它表示已有持续证据支持方向，最终结果仍待验证。

以上是回顾性的记录统计，不是独立预测准确率或事前预测能力检验。部分符合不折算成 0.5 分；暂无法判断不算错误。跨章相关判断尚未完全去重，同一父记录也不因多个观察而增加命中次数。没有作者明确给出的概率，不计算 Brier 分数。

## 评估口径

正确：在列明口径和观察窗口内，主要可检验内容符合。趋势符合：已有持续客观证据支持预测方向，最终结果尚待验证。部分符合：具体分项部分成立、部分不符，或合理口径产生不同结果。错误：所评内容与已发生结果相反。暂无法判断：无法确认趋势或结果、条件不明、对象难测或证据仍不足；缺证据不能自动换成趋势符合或部分符合。

明确未来终点尚未到达时，可以评价已有趋势，并保留原期限；这类进展单列为趋势符合，不作终局正确。单次波动、未来预测数据或仅有因果解释不算趋势证据。真正的前提条件仍须确认成立，作者的因果解释不自动增加为额外触发门槛。无期限持续判断可评价已观察阶段，不能证明永久成立。出版年只是未找到发言日期时的研究起点代理，出版前已知事实不是新的预见力证据。

“不太可能”没有被转换为数值概率；低概率事件发生可记录为方向反例，不能据单次结果证明概率失准。官方声明证明立场或制度安排，不自动证明实际成效；同时出现的政策与结果不自动证明因果。

## 暂无法判断的原因

|原因类型|记录数|
|---|---:|
|证据不足|11|
|明确未来期限未到|40|
时间窗口来源：原文写出 34 条，隐含的出版年至截止日 38 条。


## 逐条结果

### 1. TXT 第 736 行 · 趋势符合（最终结果待验证）

记录：`txt-d3d4afc2e6-000027534-000027623`

原文：Data centre electricity consumption is set to more than double to around 945 TWh by 2030.

时间窗口：原文写出（by 2030）。

扩展观点（解释，非原文）：全球数据中心用电量到2030年将翻一番以上，达到约945太瓦时。


口径与范围：核验对象：全球数据中心用电量到2030年将翻一番以上，达到约945太瓦时。
判定：第三方（CFA Institute 2026-08）引用的估计显示全球数据中心用电从2024年约415TWh升至2025年约485TWh（约+17%），快于到2030年翻倍所需的约12%年增速；终点2030年未到，方向持续符合。
限制：485TWh估计源于IEA自身后续更新，经第三方CFA引用；只看2025年增速与翻倍路径是否一致。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-5a993e59855d](https://www.cfainstitute.org/insights/articles/data-centers-driving-alternative-energy-investment)；[ev-3e04cbe87437](https://www.iea.org/news/data-centre-electricity-use-surged-in-2025-even-with-tightening-bottlenecks-driving-a-scramble-for-solutions)

### 2. TXT 第 739—741 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000027900-000028009`

原文：In the
United States, data centres account for nearly half of electricity demand growth between
now and 2030.

时间窗口：隐含，从出版年 2025 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：在美国，从现在到2030年数据中心将占电力需求增长的近一半。


口径与范围：核验对象：在美国，从现在到2030年数据中心将占电力需求增长的近一半。
判定：预测终点（2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 3. TXT 第 741—743 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000028010-000028209`

原文：By the end of the decade, the country is set to consume more electricity for
data centres than for the production of aluminium, steel, cement, chemicals and all other
energy-intensive goods combined.

时间窗口：原文写出（By the end of the decade）。

扩展观点（解释，非原文）：到本十年末，美国数据中心用电将超过铝、钢、水泥、化工等所有高耗能产品生产用电之和。


口径与范围：核验对象：到本十年末，美国数据中心用电将超过铝、钢、水泥、化工等所有高耗能产品生产用电之和。
判定：预测终点（By the end of the decade）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 4. TXT 第 743—744 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000028254-000028351`

原文：our Base Case
sees global data centre electricity consumption rising to around 1 200 TWh by 2035.

时间窗口：原文写出（by 2035）。

扩展观点（解释，非原文）：基准情景下全球数据中心用电到2035年升至约1200太瓦时。


口径与范围：核验对象：基准情景下全球数据中心用电到2035年升至约1200太瓦时。
判定：预测终点（by 2035）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 5. TXT 第 749—750 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000028668-000028761`

原文：Renewables
generation is projected to grow by over 450 TWh to meet data centre demand to 2035

时间窗口：原文写出（to 2035）。

扩展观点（解释，非原文）：到2035年为满足数据中心需求，可再生能源发电将增加450太瓦时以上。


口径与范围：核验对象：到2035年为满足数据中心需求，可再生能源发电将增加450太瓦时以上。
判定：预测终点（to 2035）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 6. TXT 第 754—755 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000029039-000029135`

原文：Natural gas expands by 175 TWh to meet growing data centre demand, notably in the
United States.

时间窗口：隐含，从出版年 2025 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：为满足数据中心需求，天然气发电增加175太瓦时，主要在美国。


口径与范围：核验对象：为满足数据中心需求，天然气发电增加175太瓦时，主要在美国。
判定：表述为无具体指标的方向性/定性判断，或依赖情景模型的长期结果，在2025-04至2026-11的短窗口内缺少可判定的公开观测，暂无法判断。
限制：原文无明确年份终点；窗口内缺少可判定的公开观测（缺少决定性事实）。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 7. TXT 第 756—757 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000029278-000029335`

原文：The first small modular
reactors come online around 2030.

时间窗口：原文写出（around 2030）。

扩展观点（解释，非原文）：首批小型模块化反应堆约在2030年投运。


口径与范围：核验对象：首批小型模块化反应堆约在2030年投运。
判定：预测终点（around 2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 8. TXT 第 764 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000029453-000029538`

原文：Data centres account for around one-tenth of global electricity demand growth to 2030

时间窗口：原文写出（to 2030）。

扩展观点（解释，非原文）：到2030年数据中心约占全球电力需求增长的十分之一。


口径与范围：核验对象：到2030年数据中心约占全球电力需求增长的十分之一。
判定：预测终点（to 2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 9. TXT 第 774—775 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000030090-000030181`

原文：In this group of countries, data centres
account for more than 20% of demand growth to 2030

时间窗口：原文写出（to 2030）。

扩展观点（解释，非原文）：在发达经济体，到2030年数据中心将占电力需求增长的20%以上。


口径与范围：核验对象：在发达经济体，到2030年数据中心将占电力需求增长的20%以上。
判定：预测终点（to 2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 10. TXT 第 779—780 行 · 部分符合

记录：`txt-d3d4afc2e6-000030419-000030539`

原文：we estimate that unless these risks
are addressed, around 20% of planned data centre projects could be at risk of delays

时间窗口：隐含，从出版年 2025 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：除非电网风险得到处理，约20%的规划数据中心项目可能面临延误。


口径与范围：核验对象：除非电网风险得到处理，约20%的规划数据中心项目可能面临延误。
判定：Sightline Climate/Currence等第三方估计2026年计划投运的大型数据中心容量有30%-50%可能延误，延误风险确实兑现且风险未被消除；但比例明显高于书中“约20%”，量级不符。
限制：第三方统计口径为2026年计划投运容量的延误比例，与书中“计划项目”口径不完全相同。
观察终点：2026-11-15；条件状态：satisfied。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-312a5bea373d](https://www.networkworld.com/article/4201941/up-to-50-of-data-center-capacity-slated-for-2026-could-be-delayed.html)；[ev-ca8007da9c82](https://www.axios.com/2026/02/24/ai-data-center-boom-projects-numbers)

### 11. TXT 第 810—811 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000033022-000033120`

原文：By 2035, the range of data centre electricity demand
across our cases spans from 700 to 1 700 TWh.

时间窗口：原文写出（By 2035）。

扩展观点（解释，非原文）：到2035年，各情景下数据中心用电在700至1700太瓦时之间。


口径与范围：核验对象：到2035年，各情景下数据中心用电在700至1700太瓦时之间。
判定：预测终点（By 2035）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 12. TXT 第 837 行 · 正确

记录：`txt-d3d4afc2e6-000034820-000034893`

原文：The industry of the future will be increasingly digitalised and automated

时间窗口：隐含，从出版年 2025 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：未来的工业将日益数字化和自动化。


口径与范围：核验对象：未来的工业将日益数字化和自动化。
判定：IFR统计2025年全球工业机器人安装量首次超过60万台、运行存量增长9%至创纪录的500万台，工业自动化在窗口内继续加深。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-d8ef51da8642](https://ifr.org/news/five-million-robots-now-operate-in-factories-globally/)

### 13. TXT 第 898—899 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000038964-000039076`

原文：Our estimates indicate that in 2030, demand for gallium for data centres
could reach over 10% of today's supply.

时间窗口：原文写出（in 2030）。

扩展观点（解释，非原文）：到2030年数据中心对镓的需求可能超过目前供应量的10%。


口径与范围：核验对象：到2030年数据中心对镓的需求可能超过目前供应量的10%。
判定：预测终点（in 2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 14. TXT 第 927—928 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000040865-000040987`

原文：Emissions from electricity use by data centres grows from 180 million tonnes (Mt) today to
300 Mt in the Base Case by 2035

时间窗口：原文写出（by 2035）。

扩展观点（解释，非原文）：数据中心用电排放从目前1.8亿吨增至2035年的3亿吨（基准情景）。


口径与范围：核验对象：数据中心用电排放从目前1.8亿吨增至2035年的3亿吨（基准情景）。
判定：预测终点（by 2035）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 15. TXT 第 2414—2415 行 · 正确

记录：`txt-d3d4afc2e6-000096856-000096967`

原文：data centres and especially AI are expected
to be the key drivers of semiconductor demand in the years to come.

时间窗口：原文写出（in the years to come）。

扩展观点（解释，非原文）：未来几年数据中心尤其是AI将成为半导体需求的主要驱动力。


口径与范围：核验对象：未来几年数据中心尤其是AI将成为半导体需求的主要驱动力。
判定：WSTS统计2025年全球半导体销售增长26%至7956亿美元，德勤等指出增长主要由AI基础设施/数据中心推动；BNP提醒2026年增长部分来自涨价和工业补库，但AI/数据中心仍是关键驱动。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-d172eb37174d](https://www.wsts.org/76/103/Global-Semiconductor-Market-grows-26-in-2025-to-796B)；[ev-7bd660a687a3](https://www.deloitte.com/us/en/insights/industry/technology/technology-media-telecom-outlooks/semiconductor-industry-outlook.html)；[ev-beea0d33a961](https://cib.bnpparibas/semiconductor-market-2026-it-is-not-solely-about-ai/)

### 16. TXT 第 2683—2684 行 · 正确

记录：`txt-d3d4afc2e6-000110102-000110201`

原文：substantial
progress has been made in making models more efficient, and this is certain to continue

时间窗口：隐含，从出版年 2025 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：AI模型效率提升将继续。


口径与范围：核验对象：AI模型效率提升将继续。
判定：Epoch AI（2026-09）测算过去三年同等性能AI的成本每季度下降约47%，模型效率在窗口内持续快速提升；反证（彭博2025-12）显示推理模型单次耗电更高，但不否定同等性能效率提升。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-8f302a505a0a](https://epoch.ai/publications/the-plunging-price-of-thought)；[ev-b28e6e1a5a3a](https://www.bloomberg.com/news/articles/2025-12-04/the-rise-of-ai-reasoning-models-comes-with-a-big-energy-tradeoff)

### 17. TXT 第 2685—2687 行 · 正确

记录：`txt-d3d4afc2e6-000110263-000110389`

原文：cheaper, more efficient
models are likely not only to incentivise greater use but also more compute use to
improve performance

时间窗口：隐含，从出版年 2025 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：更便宜高效的模型可能不仅刺激更多使用，也会带来更多算力消耗（反弹效应）。


口径与范围：核验对象：更便宜高效的模型可能不仅刺激更多使用，也会带来更多算力消耗（反弹效应）。
判定：Silicon Data指数显示单个token价格自2023年降逾90%而LLM支出仍翻倍；Dell’Oro统计2025年数据中心资本开支增长57%，更便宜的模型带来更多使用与更多算力投入。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-5ee6beb2d8ca](https://finance.yahoo.com/technology/ai/articles/tokens-getting-cheaper-companies-spending-185229986.html)；[ev-e69816e2671e](https://www.prnewswire.com/news-releases/data-center-capex-surges-57-percent-in-2025-as-ai-deployments-accelerate-according-to-delloro-group-302715242.html)

### 18. TXT 第 2951—2952 行 · 趋势符合（最终结果待验证）

记录：`txt-d3d4afc2e6-000119930-000120062`

原文：In the Base Case, electricity consumption from data centres rises to around 945 TWh
by 2030, more than doubling from the 2024 level.

时间窗口：原文写出（by 2030）。

扩展观点（解释，非原文）：基准情景下数据中心用电到2030年达到约945太瓦时，比2024年翻倍以上。


口径与范围：核验对象：基准情景下数据中心用电到2030年达到约945太瓦时，比2024年翻倍以上。
判定：与第1条同一预测（正文重复）：2025年全球数据中心用电约485TWh、较2024年增约17%，增速快于2030年翻倍路径；终点未到。
限制：与第1条重复抽取（执行摘要与正文），判定一致。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-5a993e59855d](https://www.cfainstitute.org/insights/articles/data-centers-driving-alternative-energy-investment)；[ev-3e04cbe87437](https://www.iea.org/news/data-centre-electricity-use-surged-in-2025-even-with-tightening-bottlenecks-driving-a-scramble-for-solutions)

### 19. TXT 第 2952—2953 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000120063-000120151`

原文：The United States sees by far the
largest absolute growth, followed by China and Europe.

时间窗口：隐含，从出版年 2025 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2030年美国数据中心用电绝对增量最大，其次为中国、欧洲。


口径与范围：核验对象：到2030年美国数据中心用电绝对增量最大，其次为中国、欧洲。
判定：预测终点（2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。
限制：终点晚于核验截止日；窗口内只有约19个月观测。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 20. TXT 第 3066—3068 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000126158-000126326`

原文：Efficiency improvements are expected to continue playing a pivotal
role in limiting strong growth in energy consumption, despite increasing demand for
digital services.

时间窗口：隐含，从出版年 2025 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：尽管数字服务需求增加，效率改善预计将继续对限制能耗快速增长发挥关键作用。


口径与范围：核验对象：尽管数字服务需求增加，效率改善预计将继续对限制能耗快速增长发挥关键作用。
判定：表述为无具体指标的方向性/定性判断，或依赖情景模型的长期结果，在2025-04至2026-11的短窗口内缺少可判定的公开观测，暂无法判断。
限制：原文无明确年份终点；窗口内缺少可判定的公开观测（缺少决定性事实）。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 21. TXT 第 3503—3504 行 · 部分符合

记录：`txt-d3d4afc2e6-000140376-000140488`

原文：some AI inferencing workloads could move from data centres to end-user devices such
as mobile phones and laptops

时间窗口：隐含，从出版年 2025 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：部分AI推理负载可能从数据中心转移到手机、笔记本等终端设备。


口径与范围：核验对象：部分AI推理负载可能从数据中心转移到手机、笔记本等终端设备。
判定：端侧推理在窗口内确有增长（NPU手机/AI PC），但Futurum指出多数助手与智能体体验仍依赖云端，推理负载并未明显从数据中心转出，仅部分符合。
限制：原文为“could”，只核对端侧推理是否已明显分流数据中心负载。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-7c08b7465c97](https://rcrtech.com/semiconductor-news/ai-is-shifting-to-the-edge/)；[ev-fa36bbff3a7a](https://futurumgroup.com/press-release/ai-capable-devices-slow-to-deliver-on-cloudless-agentic-ai-experiences/)

### 22. TXT 第 3601 行 · 正确

记录：`txt-d3d4afc2e6-000142981-000143033`

原文：However, the sector appears poised for rapid growth.

时间窗口：隐含，从出版年 2025 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：印度数据中心行业将快速增长。


口径与范围：核验对象：印度数据中心行业将快速增长。
判定：印度2025年新增数据中心容量387MW IT，较2024年的191MW翻倍；2026年上半年再新增约258MW、同比增59%，行业在窗口内快速增长。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-e9dbd252877d](https://ddnews.gov.in/en/indias-data-centre-capacity-more-than-doubled-in-2025/)；[ev-ef6c9a6bd9f6](https://www.savills.in/research_articles/165611/237969-0)

### 23. TXT 第 3615—3616 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000143717-000143833`

原文：over 2 GW of further maximum designed capacity is
in the pipeline and planned to come online over the next two years

时间窗口：原文写出（over the next two years）。

扩展观点（解释，非原文）：印度超过2吉瓦的新增数据中心设计容量计划在未来两年内投运。


口径与范围：核验对象：印度超过2吉瓦的新增数据中心设计容量计划在未来两年内投运。
判定：书中“两年内上线逾2GW（最大设计容量）”终点约为2027年4月；窗口内实际新增IT容量约650MW（2025年387MW+2026年上半年258MW），步伐明显偏慢，但口径（设计容量与IT负载）不同且终点未到，暂无法判断。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 24. TXT 第 3616—3617 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000143835-000143916`

原文：This means that total
installed capacity is on track to reach nearly 5 GW by 2030

时间窗口：原文写出（by 2030）。

扩展观点（解释，非原文）：印度数据中心总装机到2030年将接近5吉瓦。


口径与范围：核验对象：印度数据中心总装机到2030年将接近5吉瓦。
判定：预测终点（by 2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 25. TXT 第 3632—3633 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000144697-000144763`

原文：the dominance of coal in the mix is likely to continue beyond
2030

时间窗口：隐含，从出版年 2025 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：煤电在印度电力结构中的主导地位可能延续到2030年以后。


口径与范围：核验对象：煤电在印度电力结构中的主导地位可能延续到2030年以后。
判定：预测终点（2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 26. TXT 第 3708—3709 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000146449-000146548`

原文：while coal
dominates the electricity mix in India, the share of renewables increases to 35% by then

时间窗口：隐含，从出版年 2025 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2030年印度可再生能源发电占比升至35%。


口径与范围：核验对象：到2030年印度可再生能源发电占比升至35%。
判定：预测终点（2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。
限制：终点晚于核验截止日；窗口内只有约19个月观测。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 27. TXT 第 3852 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000152020-000152096`

原文：The total stock of servers is projected to increase by more than 60% by 2030

时间窗口：原文写出（by 2030）。

扩展观点（解释，非原文）：全球服务器存量到2030年将增加60%以上。


口径与范围：核验对象：全球服务器存量到2030年将增加60%以上。
判定：预测终点（by 2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 28. TXT 第 3867—3868 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000153090-000153182`

原文：In the Base
Case, the total installed capacity of data centres more than doubles from around

时间窗口：隐含，从出版年 2025 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：基准情景下数据中心总装机从约100吉瓦增至2030年约225吉瓦。


口径与范围：核验对象：基准情景下数据中心总装机从约100吉瓦增至2030年约225吉瓦。
判定：预测终点（2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。
限制：终点晚于核验截止日；窗口内只有约19个月观测。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 29. TXT 第 3879—3880 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000153759-000153855`

原文：The global weighted average
PUE is projected to improve, decreasing from 1.41 to 1.29 on average

时间窗口：隐含，从出版年 2025 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：全球加权平均PUE将由1.41降至1.29（至2030年）。


口径与范围：核验对象：全球加权平均PUE将由1.41降至1.29（至2030年）。
判定：预测终点（2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。
限制：终点晚于核验截止日；窗口内只有约19个月观测。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 30. TXT 第 3893—3894 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000154349-000154446`

原文：conventional servers are expected to see
significant efficiency improvements over the next decade

时间窗口：原文写出（over the next decade）。

扩展观点（解释，非原文）：未来十年普通服务器能效将显著改善。


口径与范围：核验对象：未来十年普通服务器能效将显著改善。
判定：预测终点（over the next decade）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 31. TXT 第 4013 行 · 正确

记录：`txt-d3d4afc2e6-000157027-000157115`

原文：The United States, China and Europe are projected to remain the largest regions for data

时间窗口：隐含，从出版年 2025 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：美国、中国和欧洲将继续是数据中心用电最大的地区。


口径与范围：核验对象：美国、中国和欧洲将继续是数据中心用电最大的地区。
判定：Synergy（2025-07）显示北弗吉尼亚和北京地区占全球超大规模容量约20%、美国占比最高；Visual Capitalist汇总显示美国、欧洲、中国为装机最大的地区，窗口内仍为三大地区。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-6dd49bfb04cc](https://www.srgresearch.com/articles/synergy-updates-its-ranking-of-the-worlds-top-20-hyperscale-data-center-locations)；[ev-5af40d8e27f3](https://www.visualcapitalist.com/data-center-capacity-around-the-world/)

### 32. TXT 第 4017 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000157381-000157457`

原文：electricity demand from data centres is expected to more than double by 2030

时间窗口：原文写出（by 2030）。

扩展观点（解释，非原文）：东南亚数据中心用电到2030年将翻一番以上。


口径与范围：核验对象：东南亚数据中心用电到2030年将翻一番以上。
判定：预测终点（by 2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 33. TXT 第 4025 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000157852-000157902`

原文：In China it increases by around 175 TWh (up 170%).

时间窗口：隐含，从出版年 2025 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2030年中国数据中心用电增加约175太瓦时（+170%）。


口径与范围：核验对象：到2030年中国数据中心用电增加约175太瓦时（+170%）。
判定：预测终点（2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。
限制：终点晚于核验截止日；窗口内只有约19个月观测。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 34. TXT 第 4675—4676 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000180990-000181125`

原文：the shift towards AI inference at the edge
is likely to reduce energy use in data centres with only a limited increase in energy use by

时间窗口：隐含，从出版年 2025 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：AI推理向终端转移可能减少数据中心能耗，而设备能耗只小幅增加。


口径与范围：核验对象：AI推理向终端转移可能减少数据中心能耗，而设备能耗只小幅增加。
判定：表述为无具体指标的方向性/定性判断，或依赖情景模型的长期结果，在2025-04至2026-11的短窗口内缺少可判定的公开观测，暂无法判断。
限制：原文无明确年份终点；窗口内缺少可判定的公开观测（缺少决定性事实）。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 35. TXT 第 4688 行 · 错误

记录：`txt-d3d4afc2e6-000181583-000181642`

原文：could accelerate device replacement cycles in the near term

时间窗口：原文写出（in the near term）。

扩展观点（解释，非原文）：端侧AI能力与硬件门槛可能在近期加快设备更换周期。


口径与范围：核验对象：端侧AI能力与硬件门槛可能在近期加快设备更换周期。
判定：窗口内PC换机主要由Windows 10停服驱动（Gartner），Constellation称AI PC换机周期“爬行”；手机持有周期反而延长（Kadence），未见AI加速设备更换。
限制：原文为“could”；只核对窗口内换机是否因AI加速，Windows 10停服为混杂因素。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-0bb17e421ea5](https://www.constellationr.com/insights/news/ai-pc-upgrade-cycle-crawling-amid-murky-value)；[ev-20a0becd1f74](https://www.gartner.com/en/newsroom/press-releases/2025-10-16-gartner-says-worldwide-pc-shipments-grew-8-percent-in-third-quarter-of-2025)；[ev-c90c61a8ae8f](https://kadence.com/en-us/knowledge/why-tech-buyers-are-saying-not-yet/)

### 36. TXT 第 4710 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000183600-000183676`

原文：AI is unlikely to have a noticeable impact on network energy use, especially

时间窗口：隐含，从出版年 2025 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：AI不太可能对通信网络能耗产生明显影响，近期尤其如此。


口径与范围：核验对象：AI不太可能对通信网络能耗产生明显影响，近期尤其如此。
判定：表述为无具体指标的方向性/定性判断，或依赖情景模型的长期结果，在2025-04至2026-11的短窗口内缺少可判定的公开观测，暂无法判断。
限制：原文无明确年份终点；窗口内缺少可判定的公开观测（缺少决定性事实）。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 37. TXT 第 5335—5337 行 · 趋势符合（最终结果待验证）

记录：`txt-d3d4afc2e6-000200266-000200468`

原文：The uptick in activity has meant that other
elements of supply chains, including labour and other goods, are also tight, potentially
delaying the commissioning of new gas-fired power plants beyond 2030.

时间窗口：原文写出（beyond 2030）。

扩展观点（解释，非原文）：燃气轮机及其他供应链紧张，可能使新建燃气电厂投运推迟到2030年以后。


口径与范围：核验对象：燃气轮机及其他供应链紧张，可能使新建燃气电厂投运推迟到2030年以后。
判定：大型燃气轮机交货期已排至2029-2030年（Turbomachinery），GE Vernova积压约116GW、相当于数年产能（East Daley）；新燃气电厂投运推迟的方向已明确，是否推迟到2030年后尚待观察。
限制：以燃气轮机交货期/积压为代理指标，实际电厂投运延期需到2030年后才能观测。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-12e7a3b5c4d9](https://www.turbomachinerymag.com/view/steam-turbines-gas-turbine-bottleneck-siemens-energy)；[ev-7f614504d963](https://eastdaley.com/daley-note/get-in-line-turbine-delays-stall-demand-growth-in-gas-market)

### 38. TXT 第 5681 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000216493-000216582`

原文：Global electricity generation to supply data centres is projected to grow from 460 TWh in

时间窗口：隐含，从出版年 2025 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：供给数据中心的全球发电量将由2024年460太瓦时增至2030年1000太瓦时以上、2035年1300太瓦时。


口径与范围：核验对象：供给数据中心的全球发电量将由2024年460太瓦时增至2030年1000太瓦时以上、2035年1300太瓦时。
判定：预测终点（2030、2035）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。
限制：终点晚于核验截止日；窗口内只有约19个月观测。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 39. TXT 第 5770 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000218216-000218292`

原文：renewables remain the fastest-growing source of electricity for data centres

时间窗口：隐含，从出版年 2025 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：可再生能源仍是数据中心增长最快的电源（2024—2030年年均增22%）。


口径与范围：核验对象：可再生能源仍是数据中心增长最快的电源（2024—2030年年均增22%）。
判定：预测终点（2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。
限制：终点晚于核验截止日；窗口内只有约19个月观测。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 40. TXT 第 5777—5778 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000218921-000219017`

原文：Natural
gas and coal together are expected to meet over 40% of the additional electricity demand

时间窗口：隐含，从出版年 2025 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2030年天然气和煤电合计满足数据中心新增用电的40%以上。


口径与范围：核验对象：到2030年天然气和煤电合计满足数据中心新增用电的40%以上。
判定：预测终点（2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。
限制：终点晚于核验截止日；窗口内只有约19个月观测。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 41. TXT 第 5782—5783 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000219312-000219458`

原文：the resulting increase in nuclear electricity generation leads to an
absolute decline in coal-fired generation for data centre operations by 2035.

时间窗口：原文写出（by 2035）。

扩展观点（解释，非原文）：到2035年数据中心用煤电绝对量下降。


口径与范围：核验对象：到2035年数据中心用煤电绝对量下降。
判定：预测终点（by 2035）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 42. TXT 第 5784 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000219473-000219560`

原文：CO2 emissions from electricity generation for data centres peak at around 320 Mt CO2 by

时间窗口：隐含，从出版年 2025 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：数据中心发电排放约在2030年达峰（约3.2亿吨），2035年降至约3亿吨。


口径与范围：核验对象：数据中心发电排放约在2030年达峰（约3.2亿吨），2035年降至约3亿吨。
判定：预测终点（2030、2035）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。
限制：终点晚于核验截止日；窗口内只有约19个月观测。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 43. TXT 第 5802—5803 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000220632-000220740`

原文：natural gas is the largest
source of additional supply, adding over 130 TWh of annual generation until 2030.

时间窗口：原文写出（until 2030）。

扩展观点（解释，非原文）：美国数据中心新增供电中天然气最大，到2030年增加130太瓦时以上。


口径与范围：核验对象：美国数据中心新增供电中天然气最大，到2030年增加130太瓦时以上。
判定：预测终点（until 2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 44. TXT 第 5809 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000221203-000221274`

原文：adding 110 TWh to data centre electricity supply between 2024 and 2030.

时间窗口：原文写出（between 2024 and 2030）。

扩展观点（解释，非原文）：美国可再生能源为第二大新增来源，2024—2030年为数据中心增加110太瓦时。


口径与范围：核验对象：美国可再生能源为第二大新增来源，2024—2030年为数据中心增加110太瓦时。
判定：预测终点（between 2024 and 2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 45. TXT 第 5824 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000222034-000222107`

原文：sources account for over 55% of the US data centre electricity supply mix

时间窗口：隐含，从出版年 2025 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2035年低排放电源占美国数据中心供电结构的55%以上。


口径与范围：核验对象：到2035年低排放电源占美国数据中心供电结构的55%以上。
判定：预测终点（2035）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。
限制：终点晚于核验截止日；窗口内只有约19个月观测。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 46. TXT 第 5867 行 · 部分符合

记录：`txt-d3d4afc2e6-000222584-000222652`

原文：Natural gas is set to continue to dominate the near-term data centre

时间窗口：原文写出（near-term）。

扩展观点（解释，非原文）：近期天然气将继续主导美国数据中心供电，中国以煤电为主。


口径与范围：核验对象：近期天然气将继续主导美国数据中心供电，中国以煤电为主。
判定：Axios（2026-02）称燃气是数据中心自建电源的明显赢家；但Ember显示2025年美国新增用电需求的61%由太阳能满足，电网层面增量并非燃气主导，只部分符合。
限制：缺少2025-2026年美国数据中心实际供电结构的直接统计，以自建电源与电网增量两类证据代理。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-1c6e5bd1b1ae](https://www.axios.com/2026/02/04/ai-natural-gas-power-data-centers)；[ev-9575d300db4c](https://ember-energy.org/latest-updates/solar-met-61-of-us-electricity-demand-growth-in-2025/)

### 47. TXT 第 5875 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000223017-000223106`

原文：both coal and renewables – mostly solar PV and wind – add about 90 TWh to the data centre

时间窗口：隐含，从出版年 2025 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：2024—2030年中国煤电和可再生能源各为数据中心增加约90太瓦时。


口径与范围：核验对象：2024—2030年中国煤电和可再生能源各为数据中心增加约90太瓦时。
判定：预测终点（2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。
限制：终点晚于核验截止日；窗口内只有约19个月观测。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 48. TXT 第 5880—5881 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000223539-000223623`

原文：By 2035, both sources
together make up 60% of China’s data centre electricity supply

时间窗口：原文写出（By 2035）。

扩展观点（解释，非原文）：到2035年可再生能源和核电合计占中国数据中心供电的60%。


口径与范围：核验对象：到2035年可再生能源和核电合计占中国数据中心供电的60%。
判定：预测终点（By 2035）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 49. TXT 第 5882—5883 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000223639-000223784`

原文：In Europe, renewables and nuclear are set to supply most of the additional electricity
required, with their combined share rising to 85% by 2030.

时间窗口：原文写出（by 2030）。

扩展观点（解释，非原文）：欧洲新增数据中心用电主要由可再生能源和核电供应，到2030年合计占比升至85%。


口径与范围：核验对象：欧洲新增数据中心用电主要由可再生能源和核电供应，到2030年合计占比升至85%。
判定：预测终点（by 2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 50. TXT 第 5892—5893 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000224271-000224404`

原文：In both regions, coal remains a key pillar
of the data centre electricity supply, but renewables are projected to eclipse it by 2035.

时间窗口：原文写出（by 2035）。

扩展观点（解释，非原文）：东南亚和印度数据中心供电中，可再生能源到2035年将超过煤电。


口径与范围：核验对象：东南亚和印度数据中心供电中，可再生能源到2035年将超过煤电。
判定：预测终点（by 2035）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 51. TXT 第 5946 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000227806-000227891`

原文：capacity is commissioned between 2030 and 2035, mostly from SMRs in the United States

时间窗口：原文写出（between 2030 and 2035）。

扩展观点（解释，非原文）：2030—2035年将投运近20吉瓦新核电装机，主要为美中两国的SMR。


口径与范围：核验对象：2030—2035年将投运近20吉瓦新核电装机，主要为美中两国的SMR。
判定：预测终点（between 2030 and 2035）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 52. TXT 第 6641—6642 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000250750-000250848`

原文：their share of system-wide peak electricity
demand is set to increase from 6% today to 13% by 2030

时间窗口：原文写出（by 2030）。

扩展观点（解释，非原文）：美国数据中心占全系统峰值负荷的比重将从目前6%升至2030年13%。


口径与范围：核验对象：美国数据中心占全系统峰值负荷的比重将从目前6%升至2030年13%。
判定：预测终点（by 2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 53. TXT 第 6861—6862 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000260495-000260624`

原文：studies suggest that 30-50% of workloads are delay tolerant,
a figure likely to rise with the uptake of AI training and inference

时间窗口：隐含，从出版年 2025 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：可延迟负载占比（30%—50%）可能随AI训练和推理普及而上升。


口径与范围：核验对象：可延迟负载占比（30%—50%）可能随AI训练和推理普及而上升。
判定：表述为无具体指标的方向性/定性判断，或依赖情景模型的长期结果，在2025-04至2026-11的短窗口内缺少可判定的公开观测，暂无法判断。
限制：原文无明确年份终点；窗口内缺少可判定的公开观测（缺少决定性事实）。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 54. TXT 第 7218—7219 行 · 正确

记录：`txt-d3d4afc2e6-000278436-000278520`

原文：fossil fuels still dominate primary energy
supply, but their share is set to decline

时间窗口：隐含，从出版年 2025 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：化石燃料在一次能源供应中的占比将下降。


口径与范围：核验对象：化石燃料在一次能源供应中的占比将下降。
判定：能源研究所《世界能源统计年鉴2026》显示2025年化石燃料占一次能源86%，为历史最低（Carbon Brief）；IER强调仍为86%，但份额下降方向成立。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-d431bb09b373](https://www.carbonbrief.org/six-charts-show-how-clean-power-was-worlds-largest-source-of-new-energy-in-2025)；[ev-09277194ee5c](https://www.instituteforenergyresearch.org/fossil-fuels/fossil-fuels-dominate-global-energy-supply-in-2025/)

### 55. TXT 第 7307—7308 行 · 部分符合

记录：`txt-d3d4afc2e6-000282370-000282497`

原文：The overall share of total final energy consumption met by
electricity has been steadily rising and is projected to accelerate.

时间窗口：隐含，从出版年 2025 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：电力在终端能源消费中的占比上升将加速。


口径与范围：核验对象：电力在终端能源消费中的占比上升将加速。
判定：2025年全球电力需求增长约3.0%，快于能源总供应的1.7%，电力份额继续上升；但电力需求增速从2024年的4.4%放缓至约2.8%-3%，“加速”未出现。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-64c872c7339a](https://ember-energy.org/latest-insights/energy-institute-statistical-review-of-world-energy/)；[ev-d3709d21545c](https://asian-power.com/news/global-electricity-demand-hits-record-31779-twh-in-2025-growth-pace-eases)

### 56. TXT 第 7407 行 · 趋势符合（最终结果待验证）

记录：`txt-d3d4afc2e6-000285793-000285859`

原文：the number of connected devices is set to double from 2024 to 2030

时间窗口：原文写出（from 2024 to 2030）。

扩展观点（解释，非原文）：联网自动化设备数量2024—2030年将翻一番。


口径与范围：核验对象：联网自动化设备数量2024—2030年将翻一番。
判定：IoT Analytics统计2025年联网IoT设备增长14%至211亿台，高于2024-2030年翻倍所需的约12%年增速；蜂窝IoT增速放缓至13%，终点未到，方向符合。
限制：IoT Analytics口径的IoT连接数与书中“联网设备”口径可能不同。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-f15d7d4a6f62](https://iot-analytics.com/number-connected-iot-devices/)；[ev-88acfcaa3a2d](https://iot-analytics.com/cellular-iot-market-update-spring-2026/)

### 57. TXT 第 7670—7672 行 · 正确

记录：`txt-d3d4afc2e6-000293242-000293453`

原文：The Society of Petroleum Engineers, in collaboration with Aramco
for financing, is delivering its catalogue of books and papers to a large language model, which
will be commercially available in the near future.

时间窗口：原文写出（in the near future）。

扩展观点（解释，非原文）：石油工程师学会与沙特阿美合作开发的行业大语言模型将在近期商业化上市。


口径与范围：核验对象：石油工程师学会与沙特阿美合作开发的行业大语言模型将在近期商业化上市。
判定：JPT（SPE，2026-09）称EnRG-LLM在2025年进入会员测试后不久即开放给油气公司授权使用，预测的商业可用已实现（但需求不及预期）。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-972a9a7d03bb](https://jpt.spe.org/industry-executives-offer-practical-advice-on-how-to-use-modern-ai-models-wisely)；[ev-1e2bf56a3e41](https://jpt.spe.org/curiosity-meets-comprehension-how-energy-llm-is-bridging-knowledge-gaps)

### 58. TXT 第 10098—10099 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000399889-000400013`

原文：the sector contributes to 70% of
peak electricity demand on average in advanced economies, and this share is set to increase

时间窗口：隐含，从出版年 2025 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：建筑在发达经济体峰值电力需求中的占比（约70%）近期将因供暖电气化、制冷普及和电动车充电而上升。


口径与范围：核验对象：建筑在发达经济体峰值电力需求中的占比（约70%）近期将因供暖电气化、制冷普及和电动车充电而上升。
判定：表述为无具体指标的方向性/定性判断，或依赖情景模型的长期结果，在2025-04至2026-11的短窗口内缺少可判定的公开观测，暂无法判断。
限制：原文无明确年份终点；窗口内缺少可判定的公开观测（缺少决定性事实）。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 59. TXT 第 10330—10331 行 · 正确

记录：`txt-d3d4afc2e6-000411541-000411646`

原文：AI methods will
probably complement rather than replace physics-based numerical weather prediction in the

时间窗口：隐含，从出版年 2025 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：AI天气预报方法未来可能补充而非取代基于物理的数值天气预报。


口径与范围：核验对象：AI天气预报方法未来可能补充而非取代基于物理的数值天气预报。
判定：ECMWF在2025年2月和7月先后让AIFS单一与集合AI预报投入业务运行，均与传统物理模式IFS并行，AI补充而非取代数值预报。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-5706e48a2cf1](https://www.ecmwf.int/en/about/media-centre/news/2025/ecmwfs-ensemble-ai-forecasts-become-operational)；[ev-8d336a82a31a](https://www.ecmwf.int/en/about/media-centre/news/2025/ecmwfs-ai-forecasts-become-operational)

### 60. TXT 第 10549 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000422518-000422582`

原文：The implementation of AI solutions will face regulatory hurdles.

时间窗口：隐含，从出版年 2025 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：AI解决方案的落地将面临监管障碍。


口径与范围：核验对象：AI解决方案的落地将面临监管障碍。
判定：表述为无具体指标的方向性/定性判断，或依赖情景模型的长期结果，在2025-04至2026-11的短窗口内缺少可判定的公开观测，暂无法判断。
限制：原文无明确年份终点；窗口内缺少可判定的公开观测（缺少决定性事实）。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 61. TXT 第 10553—10554 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000422909-000422983`

原文：The desire to preserve some element of human control is likely to
persist.

时间窗口：隐含，从出版年 2025 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：对AI保留一定人类控制的意愿可能持续。


口径与范围：核验对象：对AI保留一定人类控制的意愿可能持续。
判定：表述为无具体指标的方向性/定性判断，或依赖情景模型的长期结果，在2025-04至2026-11的短窗口内缺少可判定的公开观测，暂无法判断。
限制：原文无明确年份终点；窗口内缺少可判定的公开观测（缺少决定性事实）。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 62. TXT 第 11601 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000468089-000468164`

原文：are likely to remain a major bottleneck in bringing new products to market.

时间窗口：隐含，从出版年 2025 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：严格的安全与性能测试要求及供应链建设可能仍是新电池产品上市的主要瓶颈。


口径与范围：核验对象：严格的安全与性能测试要求及供应链建设可能仍是新电池产品上市的主要瓶颈。
判定：表述为无具体指标的方向性/定性判断，或依赖情景模型的长期结果，在2025-04至2026-11的短窗口内缺少可判定的公开观测，暂无法判断。
限制：原文无明确年份终点；窗口内缺少可判定的公开观测（缺少决定性事实）。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 63. TXT 第 11647—11648 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000469379-000469466`

原文：energy-dense fuels are likely to be indispensable for some use cases,
such as aviation.

时间窗口：隐含，从出版年 2025 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：高能量密度燃料在航空等部分用途中可能不可或缺。


口径与范围：核验对象：高能量密度燃料在航空等部分用途中可能不可或缺。
判定：表述为无具体指标的方向性/定性判断，或依赖情景模型的长期结果，在2025-04至2026-11的短窗口内缺少可判定的公开观测，暂无法判断。
限制：原文无明确年份终点；窗口内缺少可判定的公开观测（缺少决定性事实）。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 64. TXT 第 12690 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000518624-000518712`

原文：However, the recent wave of AI growth is not likely to further accelerate nuclear fusion

时间窗口：隐含，从出版年 2025 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：本轮AI热潮不太可能进一步加快核聚变部署，也不会使SMR部署提前到2030年之前。


口径与范围：核验对象：本轮AI热潮不太可能进一步加快核聚变部署，也不会使SMR部署提前到2030年之前。
判定：预测终点（2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。
限制：终点晚于核验截止日；窗口内只有约19个月观测。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 65. TXT 第 13037 行 · 趋势符合（最终结果待验证）

记录：`txt-d3d4afc2e6-000533480-000533563`

原文：Cumulative data centre investment totals USD 4.2 trillion to 2030 in the Base Case.

时间窗口：原文写出（2030）。

扩展观点（解释，非原文）：基准情景下到2030年数据中心累计投资达4.2万亿美元。


口径与范围：核验对象：基准情景下到2030年数据中心累计投资达4.2万亿美元。
判定：2025年全球数据中心投资超过5800亿美元（Colliers），Dell’Oro预计2026年资本开支超过1万亿美元；按此路径2025-2030年累计4.2万亿美元的方向成立，终点未到。
限制：Colliers与Dell’Oro口径不同（是否含IT设备），2026年为年内预测值。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-15849a0ff6af](https://www.datacenterdynamics.com/en/news/colliers-data-center-investment-tops-580-billion-beating-oil-investment-for-the-first-time/)；[ev-b329282e6050](https://convergedigest.com/delloro-ai-infrastructure-spending-pushes-2026-data-center-capex-above-1-trillion/)

### 66. TXT 第 13051 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000534310-000534396`

原文：Data centres are on track to account for 3% of the power sector and 1% of total energy

时间窗口：隐含，从出版年 2025 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2030年数据中心将占电力部门排放的3%、能源部门总排放的1%。


口径与范围：核验对象：到2030年数据中心将占电力部门排放的3%、能源部门总排放的1%。
判定：预测终点（2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。
限制：终点晚于核验截止日；窗口内只有约19个月观测。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 67. TXT 第 13293 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000546785-000546872`

原文：Natural gas demand to power data centres is expected to grow by nearly 35 billion cubic

时间窗口：隐含，从出版年 2025 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：基准情景下2024-2035年全球数据中心发电用天然气需求增长近350亿立方米。


口径与范围：核验对象：基准情景下2024-2035年全球数据中心发电用天然气需求增长近350亿立方米。
判定：预测终点（2035）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。
限制：终点晚于核验截止日；窗口内只有约19个月观测。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 68. TXT 第 13944 行 · 正确

记录：`txt-d3d4afc2e6-000572930-000573024`

原文：In the medium term, the digital sector will play a greater role in the energy sector as demand

时间窗口：原文写出（medium term）。

扩展观点（解释，非原文）：中期内随着数据中心需求上升，数字部门将在能源部门发挥更大作用。


口径与范围：核验对象：中期内随着数据中心需求上升，数字部门将在能源部门发挥更大作用。
判定：Alphabet于2025-12以47.5亿美元收购清洁能源开发商Intersect；Meta在一年内出资建设至少十几座燃气电厂，数字/科技部门在能源部门的角色在窗口内明显加大。
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-3dcfeed3692a](https://www.reuters.com/technology/alphabet-buy-data-center-infrastructure-firm-intersect-475-billion-deal-2025-12-22/)；[ev-5f829fea4cdc](https://techcrunch.com/2026/07/23/meta-drops-out-of-a-major-clean-energy-pact-as-its-natural-gas-buildout-accelerates/)

### 69. TXT 第 14072 行 · 趋势符合（最终结果待验证）

记录：`txt-d3d4afc2e6-000577697-000577785`

原文：albeit at a slower rate, surpassing USD 800 billion per annum before 2030 to accommodate

时间窗口：原文写出（before 2030）。

扩展观点（解释，非原文）：基准情景下数据中心年投资继续增长（增速放缓），2030年前超过每年8000亿美元。


口径与范围：核验对象：基准情景下数据中心年投资继续增长（增速放缓），2030年前超过每年8000亿美元。
判定：Dell’Oro称2026年全球数据中心资本开支有望超过1万亿美元，2026年二季度同比增长92%；超过每年8000亿美元已接近实现，但全年数据尚未出，暂记趋势符合。
限制：2026年全年数据未出，Dell’Oro为年中预测；口径为数据中心资本开支。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-b329282e6050](https://convergedigest.com/delloro-ai-infrastructure-spending-pushes-2026-data-center-capex-above-1-trillion/)；[ev-5ce8d13c1454](https://www.prnewswire.com/news-releases/data-center-capex-grew-92-percent-in-2q-2026-driven-by-surging-ai-demand-and-memory-costs-according-to-delloro-group-302879910.html)

### 70. TXT 第 14512 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000591378-000591460`

原文：Nevertheless, data centres are unlikely to fundamentally alter the environment for

时间窗口：隐含，从出版年 2025 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：数据中心不太可能根本改变多数新兴市场和发展中经济体的可再生能源投资环境。


口径与范围：核验对象：数据中心不太可能根本改变多数新兴市场和发展中经济体的可再生能源投资环境。
判定：表述为无具体指标的方向性/定性判断，或依赖情景模型的长期结果，在2025-04至2026-11的短窗口内缺少可判定的公开观测，暂无法判断。
限制：原文无明确年份终点；窗口内缺少可判定的公开观测（缺少决定性事实）。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 71. TXT 第 15001 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000610249-000610340`

原文：developing economies excluding China, electricity demand is on track to rise faster than in

时间窗口：隐含，从出版年 2025 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：未来十年，除中国外的新兴市场和发展中经济体电力需求增速将快于发达经济体。


口径与范围：核验对象：未来十年，除中国外的新兴市场和发展中经济体电力需求增速将快于发达经济体。
判定：十年期相对增速预测；2025年印度能源需求增速仅约1%、美国电力需求增约3.1%，与预测方向相反，但仅一年且受季风天气影响，不足以判断十年结果。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

### 72. TXT 第 15551 行 · 暂无法判断

记录：`txt-d3d4afc2e6-000627868-000627963`

原文：560 billion litres per year, and this could rise to around 1200 billion litres per year in 2030

时间窗口：原文写出（2030）。

扩展观点（解释，非原文）：全球数据中心耗水量约5600亿升/年，基准情景下2030年可能升至约1.2万亿升/年。


口径与范围：核验对象：全球数据中心耗水量约5600亿升/年，基准情景下2030年可能升至约1.2万亿升/年。
判定：预测终点（2030）晚于核验截止日2026-11-15，窗口仅约19个月；属情景模型的长期结果，现有观测不足以确认方向，暂无法判断。
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unknown。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：尚无足以判定的外部证据；本条仅作原文范围或条件审阅。

## 证据登记

哈希校验只证明本地保存内容未改变。检索摘录与完整原始文件会按证据记录注明；两者均不能代替对来源与命题对应关系的判断。

- [ev-5a993e59855d](https://www.cfainstitute.org/insights/articles/data-centers-driving-alternative-energy-investment)；资料日期：2026-08-11；覆盖：Why data centers are driving investment in alternative energy | CFA Institute。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-3e04cbe87437](https://www.iea.org/news/data-centre-electricity-use-surged-in-2025-even-with-tightening-bottlenecks-driving-a-scramble-for-solutions)；资料日期：2026-04-16；覆盖：Data centre electricity use surged in 2025, even with tightening bottlenecks driving a scramble for solutions - IEA。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-312a5bea373d](https://www.networkworld.com/article/4201941/up-to-50-of-data-center-capacity-slated-for-2026-could-be-delayed.html)；资料日期：2026-07-27；覆盖：Up to 50% of data center capacity slated for 2026 could be delayed | Network World。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-ca8007da9c82](https://www.axios.com/2026/02/24/ai-data-center-boom-projects-numbers)；资料日期：2026-02-24；覆盖：Why the AI data center boom is stalling worldwide。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-d8ef51da8642](https://ifr.org/news/five-million-robots-now-operate-in-factories-globally/)；资料日期：未确定；覆盖：Five Million Robots now Operate in Factories Globally - International Federation of Robotics。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-d172eb37174d](https://www.wsts.org/76/103/Global-Semiconductor-Market-grows-26-in-2025-to-796B)；资料日期：未确定；覆盖：Global Semiconductor Market grows 26% in 2025 to $796B。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-7bd660a687a3](https://www.deloitte.com/us/en/insights/industry/technology/technology-media-telecom-outlooks/semiconductor-industry-outlook.html)；资料日期：2026-02-04；覆盖：2026 Semiconductor Industry Outlook | Deloitte Insights。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-beea0d33a961](https://cib.bnpparibas/semiconductor-market-2026-it-is-not-solely-about-ai/)；资料日期：2026-03-24；覆盖：Semiconductor market 2026: it is not solely about AI - BNP Paribas CIB。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-8f302a505a0a](https://epoch.ai/publications/the-plunging-price-of-thought)；资料日期：2026-09-22；覆盖：The plunging price of thought | Epoch AI。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-b28e6e1a5a3a](https://www.bloomberg.com/news/articles/2025-12-04/the-rise-of-ai-reasoning-models-comes-with-a-big-energy-tradeoff)；资料日期：2025-12-04；覆盖：The Rise of AI Reasoning Models Comes With A Big Energy Tradeoff - Bloomberg。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-5ee6beb2d8ca](https://finance.yahoo.com/technology/ai/articles/tokens-getting-cheaper-companies-spending-185229986.html)；资料日期：2026-06-17；覆盖：Tokens are getting cheaper, but companies are spending even more on AI as a result, top economist warns。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-e69816e2671e](https://www.prnewswire.com/news-releases/data-center-capex-surges-57-percent-in-2025-as-ai-deployments-accelerate-according-to-delloro-group-302715242.html)；资料日期：2026-03-17；覆盖：Data Center Capex Surges 57 Percent in 2025 as AI Deployments Accelerate, According to Dell'Oro Group。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-7c08b7465c97](https://rcrtech.com/semiconductor-news/ai-is-shifting-to-the-edge/)；资料日期：2025-10-22；覆盖：AI is shifting to the edge。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-fa36bbff3a7a](https://futurumgroup.com/press-release/ai-capable-devices-slow-to-deliver-on-cloudless-agentic-ai-experiences/)；资料日期：未确定；覆盖：AI-Capable Devices Slow to Deliver on Cloudless Agentic AI Experiences。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-e9dbd252877d](https://ddnews.gov.in/en/indias-data-centre-capacity-more-than-doubled-in-2025/)；资料日期：未确定；覆盖：India’s data centre capacity more than doubled in 2025 | DD News。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-ef6c9a6bd9f6](https://www.savills.in/research_articles/165611/237969-0)；资料日期：未确定；覆盖：Savills India | Data Centre Market Watch H1 2026。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-6dd49bfb04cc](https://www.srgresearch.com/articles/synergy-updates-its-ranking-of-the-worlds-top-20-hyperscale-data-center-locations)；资料日期：2025-07-16；覆盖：Synergy Updates Its Ranking of the World’s Top 20 Hyperscale Data Center Locations | Synergy Research Group。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-5af40d8e27f3](https://www.visualcapitalist.com/data-center-capacity-around-the-world/)；资料日期：2025-07-30；覆盖：Mapped: Data Center Capacity Around the World。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-0bb17e421ea5](https://www.constellationr.com/insights/news/ai-pc-upgrade-cycle-crawling-amid-murky-value)；资料日期：未确定；覆盖：The AI PC upgrade cycle is crawling amid murky value。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-20a0becd1f74](https://www.gartner.com/en/newsroom/press-releases/2025-10-16-gartner-says-worldwide-pc-shipments-grew-8-percent-in-third-quarter-of-2025)；资料日期：2025-10-16；覆盖：Gartner Says Worldwide PC Shipments Grew 8.2% in Third Quarter of 2025。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-c90c61a8ae8f](https://kadence.com/en-us/knowledge/why-tech-buyers-are-saying-not-yet/)；资料日期：2025-09-22；覆盖：Why Tech Buyers Are Saying ‘Not Yet.’ | Kadence。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-12e7a3b5c4d9](https://www.turbomachinerymag.com/view/steam-turbines-gas-turbine-bottleneck-siemens-energy)；资料日期：未确定；覆盖：Is Steam the Answer to the Gas Turbine Bottleneck?。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-7f614504d963](https://eastdaley.com/daley-note/get-in-line-turbine-delays-stall-demand-growth-in-gas-market)；资料日期：2026-08-05；覆盖：Get in Line: Turbine Delays Stall Demand Growth in Gas Market | East Daley。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-1c6e5bd1b1ae](https://www.axios.com/2026/02/04/ai-natural-gas-power-data-centers)；资料日期：2026-02-04；覆盖：How AI data centers are making natural gas more important。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-9575d300db4c](https://ember-energy.org/latest-updates/solar-met-61-of-us-electricity-demand-growth-in-2025/)；资料日期：2026-01-16；覆盖：Solar met 61% of US electricity demand growth in 2025。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-d431bb09b373](https://www.carbonbrief.org/six-charts-show-how-clean-power-was-worlds-largest-source-of-new-energy-in-2025)；资料日期：2026-06-29；覆盖：Six charts show how clean power was world’s largest source of new energy in 2025 - Carbon Brief。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-09277194ee5c](https://www.instituteforenergyresearch.org/fossil-fuels/fossil-fuels-dominate-global-energy-supply-in-2025/)；资料日期：未确定；覆盖：Fossil Fuels Dominate Global Energy Supply in 2025。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-64c872c7339a](https://ember-energy.org/latest-insights/energy-institute-statistical-review-of-world-energy/)；资料日期：2026-06-30；覆盖：Energy Institute Statistical Review of World Energy。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-d3709d21545c](https://asian-power.com/news/global-electricity-demand-hits-record-31779-twh-in-2025-growth-pace-eases)；资料日期：2026-04-22；覆盖：Global electricity demand hits record 31,779 TWh in 2025, but growth pace eases | Asian Power。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-f15d7d4a6f62](https://iot-analytics.com/number-connected-iot-devices/)；资料日期：2025-10-28；覆盖：Number of connected IoT devices growing 14% to 21.1 billion。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-88acfcaa3a2d](https://iot-analytics.com/cellular-iot-market-update-spring-2026/)；资料日期：2026-04-29；覆盖：Cellular IoT market update 2026: Connections grew 13% in 2025, slowest since 2020 - IoT Analytics。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-972a9a7d03bb](https://jpt.spe.org/industry-executives-offer-practical-advice-on-how-to-use-modern-ai-models-wisely)；资料日期：2026-09-10；覆盖：Industry Executives Offer Practical Advice on How To Use Modern AI Models Wisely。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-1e2bf56a3e41](https://jpt.spe.org/curiosity-meets-comprehension-how-energy-llm-is-bridging-knowledge-gaps)；资料日期：2025-03-27；覆盖：Curiosity Meets Comprehension: How Energy LLM Is Bridging Knowledge Gaps。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-5706e48a2cf1](https://www.ecmwf.int/en/about/media-centre/news/2025/ecmwfs-ensemble-ai-forecasts-become-operational)；资料日期：2025-07-01；覆盖：ECMWF’s ensemble AI forecasts become operational | ECMWF。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-8d336a82a31a](https://www.ecmwf.int/en/about/media-centre/news/2025/ecmwfs-ai-forecasts-become-operational)；资料日期：2025-02-25；覆盖：ECMWF’s AI forecasts become operational | ECMWF。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-15849a0ff6af](https://www.datacenterdynamics.com/en/news/colliers-data-center-investment-tops-580-billion-beating-oil-investment-for-the-first-time/)；资料日期：2026-03-26；覆盖：Colliers: Data center investment tops $580 billion, beating oil investment for the first time - DCD。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-b329282e6050](https://convergedigest.com/delloro-ai-infrastructure-spending-pushes-2026-data-center-capex-above-1-trillion/)；资料日期：2026-06-10；覆盖：Dell'Oro: AI Infrastructure Spending Pushes 2026 Data Center Capex Above $1 Trillion - Converge Digest。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-3dcfeed3692a](https://www.reuters.com/technology/alphabet-buy-data-center-infrastructure-firm-intersect-475-billion-deal-2025-12-22/)；资料日期：2025-12-22；覆盖：Alphabet to buy clean energy developer Intersect in $4.75 billion deal amid AI push | Reuters。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-5f829fea4cdc](https://techcrunch.com/2026/07/23/meta-drops-out-of-a-major-clean-energy-pact-as-its-natural-gas-buildout-accelerates/)；资料日期：2026-07-23；覆盖：Meta drops out of a major clean energy pact as its natural gas buildout accelerates | TechCrunch。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-5ce8d13c1454](https://www.prnewswire.com/news-releases/data-center-capex-grew-92-percent-in-2q-2026-driven-by-surging-ai-demand-and-memory-costs-according-to-delloro-group-302879910.html)；资料日期：2026-09-16；覆盖：Data Center Capex Grew 92 Percent in 2Q 2026, Driven by Surging AI Demand and Memory Costs, According to Dell'Oro Group。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
