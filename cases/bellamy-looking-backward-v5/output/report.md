# 回顾：五类评估

证据截止日：2026-11-15。已处理 51/51 条全书候选；尚未处理 0 条。

累计已完成全量抽取复核 51 条；保留旧抽样抽取 0 条，两者不重复相加。

已补充扩展观点 51 条；其中 0 条仍有待确认的代指、对象或范围，已逐条标记。扩展观点不自动改变原有评估。

本轮沿用候选清单逐条核查，不保证没有漏抽。PDF记录使用PDF页码，TXT记录使用原始文本行号。扩展观点是依据所给语境的解释，原文短引文另行保留。

|类别|父记录数|
|---|---:|
|正确|3|
|趋势符合|6|
|部分符合|11|
|错误|30|
|暂无法判断|1|
|排除：非预测|0|
|排除：重复|0|
|尚未处理|0|

可判定覆盖率：50/51 = 98.0%。
绑定外部证据的预测：51/51；未绑定：0。绑定不代表证据充分或研究已完成。
“正确”占已判定记录：3/50 = 6.0%。

趋势符合 6 条单独列出，与部分符合互不重复；它表示已有持续证据支持方向，最终结果仍待验证。

以上是回顾性的记录统计，不是独立预测准确率或事前预测能力检验。部分符合不折算成 0.5 分；暂无法判断不算错误。跨章相关判断尚未完全去重，同一父记录也不因多个观察而增加命中次数。没有作者明确给出的概率，不计算 Brier 分数。

## 评估口径

正确：在列明口径和观察窗口内，主要可检验内容符合。趋势符合：已有持续客观证据支持预测方向，最终结果尚待验证。部分符合：具体分项部分成立、部分不符，或合理口径产生不同结果。错误：所评内容与已发生结果相反。暂无法判断：无法确认趋势或结果、条件不明、对象难测或证据仍不足；缺证据不能自动换成趋势符合或部分符合。

明确未来终点尚未到达时，可以评价已有趋势，并保留原期限；这类进展单列为趋势符合，不作终局正确。单次波动、未来预测数据或仅有因果解释不算趋势证据。真正的前提条件仍须确认成立，作者的因果解释不自动增加为额外触发门槛。无期限持续判断可评价已观察阶段，不能证明永久成立。出版年只是未找到发言日期时的研究起点代理，出版前已知事实不是新的预见力证据。

“不太可能”没有被转换为数值概率；低概率事件发生可记录为方向反例，不能据单次结果证明概率失准。官方声明证明立场或制度安排，不自动证明实际成效；同时出现的政策与结果不自动证明因果。

## 暂无法判断的原因

|原因类型|记录数|
|---|---:|
|明确未来期限未到|1|
时间窗口来源：原文写出 3 条，隐含的出版年至截止日 48 条。


## 逐条结果

### 1. TXT 第 938—940 行 · 错误

记录：`txt-ddaf515e22-000050945-000051054`

原文：It is
nearly a century since the crude method of combustion on which you
depended for heat became obsolete.

时间窗口：原文写出（nearly a century）。

扩展观点（解释，非原文）：到2000年，波士顿取暖不再靠在室内燃烧燃料，烟囱和烟雾基本消失，这种燃烧取暖约在1900年前后就已过时。


口径与范围：核验对象：到2000年，波士顿取暖不再靠在室内燃烧燃料，烟囱和烟雾基本消失，这种燃烧取暖约在1900年前后就已过时。
判定：2000年人口普查：美国家庭主要取暖燃料中燃气占51.2%、燃油/煤油9.0%、木柴1.7%，用电取暖只有30.3%；室内燃烧取暖远未“过时”
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-bb20e82b61bf](https://www2.census.gov/programs-surveys/decennial/tables/time-series/coh-fuels/fuels2000.txt)；[ev-b6cff9a4797e](https://www.census.gov/data/tables/time-series/dec/coh-fuels.html)

### 2. TXT 第 1097 行 · 错误

记录：`txt-ddaf515e22-000060181-000060237`

原文：As no such thing as the labor question is known nowadays

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年，劳资冲突（劳工问题）将不复存在。


口径与范围：核验对象：到2000年，劳资冲突（劳工问题）将不复存在。
判定：劳资冲突并未消失：BLS统计1947—2025年共有11,685起千人以上的大型停工；2000年波音1.7万名工程师罢工，是美国史上最大的白领罢工之一
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-463406addd71](https://www.bls.gov/wsp/factsheets/summary-of-work-stoppages-in-the-united-states.htm)；[ev-4cbd7c65bc42](https://www.latimes.com/archives/la-xpm-2000-feb-10-fi-62793-story.html)

### 3. TXT 第 1218—1220 行 · 部分符合

记录：`txt-ddaf515e22-000066909-000067033`

原文：During the last decade of the century, such small
businesses as still remained were fast-failing survivals of a past
epoch

时间窗口：原文写出（During the last decade of the century）。

扩展观点（解释，非原文）：19世纪90年代，残存的小企业会迅速衰亡，工商业继续向大公司集中。


口径与范围：核验对象：19世纪90年代，残存的小企业会迅速衰亡，工商业继续向大公司集中。
判定：1895—1904年的“大兼并浪潮”中，大批原本相互竞争的企业合并为占据主导份额的巨型公司，集中趋势应验；但小企业没有“迅速消亡”，自营业主和小企业主在20世纪仍大量存在
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-aa9783e29bca](http://naomi-lamoreaux.squarespace.com/the-great-merger-movement)；[ev-ed2f6a7d98ae](https://ciaotest.cc.columbia.edu/olj/ep/ep_jan06/ep_jan06c.pdf)

### 4. TXT 第 1224—1225 行 · 趋势符合（最终结果待验证）

记录：`txt-ddaf515e22-000067343-000067442`

原文：The railroads had gone on combining till a
few great syndicates controlled every rail in the land.

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：美国铁路会继续合并，直到少数几个大辛迪加控制全国所有铁路。


口径与范围：核验对象：美国铁路会继续合并，直到少数几个大辛迪加控制全国所有铁路。
判定：1893年恐慌后摩根等投资银行主导铁路重组，以“利益共同体”消除竞争，全国干线铁路落入少数几个集团之手；但1904年北方证券案依《谢尔曼法》阻止了进一步合并，并未形成书中那样的完全垄断
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-83172ac154f4](https://digfir-published.macmillanusa.com/roark7e/roark7e_ch18_11.html)；[ev-620c8ef393ff](https://www.annenbergclassroom.org/timeline_event/northern-securities-co-v-united-states/)

### 5. TXT 第 1274—1275 行 · 错误

记录：`txt-ddaf515e22-000070477-000070595`

原文：Early in the last century the evolution was completed by the final
consolidation of the entire capital of the nation.

时间窗口：原文写出（Early in the last century）。

扩展观点（解释，非原文）：20世纪初，美国全部资本会合并为由国家经营的单一托拉斯，国家成为唯一的资本家和雇主。


口径与范围：核验对象：20世纪初，美国全部资本会合并为由国家经营的单一托拉斯，国家成为唯一的资本家和雇主。
判定：受本书启发的“民族主义俱乐部”曾在1880年代末兴起（至少165个），但很快衰落；美国20世纪始终是以私营企业为主的市场经济，全部资本从未收归国家
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-97c5de1e5fb2](https://en.wikipedia.org/wiki/Nationalist_Clubs)；[ev-c7458d88a927](https://usa.usembassy.de/etexts/oecon/chap2.htm)

### 6. TXT 第 1357—1358 行 · 错误

记录：`txt-ddaf515e22-000075440-000075495`

原文：We have no wars now, and our
governments no war powers

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年将没有战争，政府不再拥有战争权力。


口径与范围：核验对象：到2000年将没有战争，政府不再拥有战争权力。
判定：1945年后大国之间确有“长期和平”，但战争并未消失：1990年代美国参与了海湾战争、索马里、科索沃等冲突，各国政府仍保有战争权力
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-bd560fe255ac](https://en.wikipedia.org/wiki/List_of_wars_involving_the_United_States_in_the_20th_century)；[ev-32cc1fa62ab8](https://2001-2009.state.gov/r/pa/ho/time/pcw/index.htm)；[ev-2db61bc04c57](https://en.wikipedia.org/wiki/Long_Peace)

### 7. TXT 第 1376—1377 行 · 错误

记录：`txt-ddaf515e22-000076531-000076660`

原文：We have no parties or politicians, and as for demagoguery and
corruption, they are words having only an historical significance.

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年美国将没有政党和职业政客，煽动与腐败只剩历史意义。


口径与范围：核验对象：到2000年美国将没有政党和职业政客，煽动与腐败只剩历史意义。
判定：2000年美国大选仍是共和党布什与民主党戈尔对决，政党和职业政客照旧主导政治
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-75ae84599579](https://www.archives.gov/electoral-college/2000)；[ev-7bcea9172a77](https://www.presidency.ucsb.edu/statistics/elections/2000)

### 8. TXT 第 1407—1408 行 · 错误

记录：`txt-ddaf515e22-000078325-000078434`

原文：When the nation became the sole employer, all the citizens, by
virtue of their citizenship, became employees

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：国家将成为唯一雇主，全体公民都成为国家雇员。


口径与范围：核验对象：国家将成为唯一雇主，全体公民都成为国家雇员。
判定：2000年人口普查补充调查：只有约14%的就业者是联邦、州或地方政府雇员（约1800万人），绝大多数人受雇于私营部门
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-98b766ca3775](https://www.prb.org/resources/the-size-and-shape-of-americas-government/)；[ev-59cbf4b35247](https://www.bls.gov/opub/mlr/2004/10/art3full.pdf)

### 9. TXT 第 1452—1454 行 · 错误

记录：`txt-ddaf515e22-000080912-000081063`

原文：The period of industrial
service is twenty-four years, beginning at the close of the course of
education at twenty-one and terminating at forty-five.

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年，人们21岁完成教育后开始工作，45岁退休，工作期24年。


口径与范围：核验对象：到2000年，人们21岁完成教育后开始工作，45岁退休，工作期24年。
判定：美国并没有45岁退休的制度：1990—1995年男性平均退休年龄约62.2岁，社会保障的全额退休年龄为65岁并逐步提高到67岁
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-638c0d8669d2](http://www.bls.gov/opub/mlr/2000/07/art2full.pdf)；[ev-cf8395a20fb5](https://www.ssa.gov/benefits/retirement/planner/ageincrease.html)

### 10. TXT 第 1555—1557 行 · 趋势符合（最终结果待验证）

记录：`txt-ddaf515e22-000087284-000087411`

原文：The nation does not maim and slaughter its workmen
by thousands, as did the private capitalists and corporations of your
day.

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年，工伤致死致残将不再以千计，劳动中不卫生和特别危险的条件被消除。


口径与范围：核验对象：到2000年，工伤致死致残将不再以千计，劳动中不卫生和特别危险的条件被消除。
判定：工伤死亡率在20世纪大幅下降（CDC：1933—1997年下降约90%；OSHA成立后死亡人数又减少六成以上），方向应验；但2000年美国仍有5,915人死于工伤，“不再以千计伤亡”并未实现
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-38c45a67c892](https://www.cdc.gov/mmwr/preview/mmwrhtml/mm4822a1.htm)；[ev-e71e301917f8](https://www.bls.gov/iif/fatal-injuries-tables/archive/census-of-fatal-occupational-injuries-news-release-2000.pdf)

### 11. TXT 第 1636—1638 行 · 趋势符合（最终结果待验证）

记录：`txt-ddaf515e22-000092109-000092263`

原文：The schools of technology, of medicine, of art, of music, of
histrionics, and of higher liberal learning are always open to
aspirants without condition.

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年，技术、医学、艺术、音乐和高等文理教育将无条件向所有有志者开放。


口径与范围：核验对象：到2000年，技术、医学、艺术、音乐和高等文理教育将无条件向所有有志者开放。
判定：高等教育大幅普及：NCES数据显示2000年应届高中毕业生的升学率为63%，2016年升至70%；但并非“无条件向所有人开放”，高收入家庭子女升学率（83%）明显高于低收入家庭，学费负担仍是障碍
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-8e3beb09f43e](https://nces.ed.gov/programs/coe/pdf/Indicator_CPA/coe_cpa_2018_05.pdf)；[ev-2d0e1a757f53](https://www.americanprogress.org/article/affordability-of-postsecondary-education-equity-and-adequacy-across-the-50-states/)

### 12. TXT 第 1950—1951 行 · 错误

记录：`txt-ddaf515e22-000109385-000109485`

原文：There is neither selling nor buying nowadays; the distribution of
goods is effected in another way.

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年将不再有买卖和商店，商品改由国家直接分配。


口径与范围：核验对象：到2000年将不再有买卖和商店，商品改由国家直接分配。
判定：到2000年买卖和商店照旧存在：人口普查局的年度零售报告统计了数以百万计的零售企业和数万亿美元的零售额
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-c6aac53a1e06](https://www2.census.gov/retail/releases/benchmark/annpub00.pdf)；[ev-890b99d157c9](https://www2.census.gov/library/publications/2008/compendia/statab/128ed/tables/09s1017.pdf)

### 13. TXT 第 1951—1952 行 · 错误

记录：`txt-ddaf515e22-000109486-000109554`

原文：As to the bankers, having no money we
have no use for those gentry.

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年货币会被废除，银行家随之消失。


口径与范围：核验对象：到2000年货币会被废除，银行家随之消失。
判定：货币和银行没有消失：美联储统计的流通中现金在20世纪持续增长；直到2026年仍有约58%的美国人每周用现金付款，只是用现金的人在减少
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-79c60236d8b4](https://www.federalreserve.gov/newsevents/testimony/roseman20100720a_accessible.htm)；[ev-97bbb5f8ebeb](https://www.pewresearch.org/short-reads/2026/08/26/fewer-americans-use-cash-today-than-a-decade-ago-but-many-still-carry-it/)

### 14. TXT 第 1993—1994 行 · 趋势符合（最终结果待验证）

记录：`txt-ddaf515e22-000111598-000111672`

原文：a credit card issued him with which he procures at the public
storehouses

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年，公民将用国家发放的“信用卡”（credit card）在公共商店取得所需物品，取代现金交易。


口径与范围：核验对象：到2000年，公民将用国家发放的“信用卡”（credit card）在公共商店取得所需物品，取代现金交易。
判定：贝拉米首创“credit card”一词；1950年Diners Club推出首张通用信用卡，到2000年刷卡已是主流支付方式。但卡不是国家发放的额度凭证，也没有取代现金
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-d00c1b522392](https://www.historyofinformation.com/detail.php?entryid=2044)；[ev-1a5df9977c3f](https://www.history.com/articles/when-were-credit-cards-invented)；[ev-e321cd5959e3](https://americanhistory.si.edu/explore/exhibitions/value-money/online/innovations-money/plastic-payments)

### 15. TXT 第 2059—2060 行 · 部分符合

记录：`txt-ddaf515e22-000115366-000115487`

原文：the nation guarantees the nurture, education, and
comfortable maintenance of every citizen from the cradle to the grave.

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年，国家将保障每个公民从摇篮到坟墓的养育、教育和舒适生活。


口径与范围：核验对象：到2000年，国家将保障每个公民从摇篮到坟墓的养育、教育和舒适生活。
判定：美国建立了社会保障、医疗保险等覆盖失业、贫困、疾病和养老的福利国家制度；但远非“从摇篮到坟墓”的全面保障：2000年仍有14.0%的人全年没有医疗保险
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-becdbf4c53fb](https://archives.history.ac.uk/history-in-focus/welfare/articles/katzm.html)；[ev-6a00d5b28d73](https://www.census.gov/library/publications/2001/demo/p60-215.html)

### 16. TXT 第 2145—2146 行 · 错误

记录：`txt-ddaf515e22-000120179-000120235`

原文：we have nothing at all answering
to your idea of wages.

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年将不再有工资制度，所有人按人的身份获得同等份额的收入。


口径与范围：核验对象：到2000年将不再有工资制度，所有人按人的身份获得同等份额的收入。
判定：工资制度依旧，收入差距很大：2000年美国家庭收入基尼系数为0.460，显著高于此前多数年份；1990年代高收入者与中间层差距继续拉大
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-1c3a74b14771](https://www2.census.gov/library/publications/2001/demographics/p60-213.pdf)；[ev-4b668f8d12d0](https://www.epi.org/publication/books_swa2000_swa2000intro/)

### 17. TXT 第 2237—2238 行 · 错误

记录：`txt-ddaf515e22-000125317-000125412`

原文：though we have abolished poverty and the fear of it, and
inordinate luxury with the hope of it

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年美国将消灭贫困以及对贫困的恐惧，同时消灭过度奢侈。


口径与范围：核验对象：到2000年美国将消灭贫困以及对贫困的恐惧，同时消灭过度奢侈。
判定：贫困没有被消灭：2000年美国有3,110万人（11.3%）生活在官方贫困线以下
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-6feae0236447](https://www.bls.gov/cps/cpswp2000.htm)；[ev-4ff5693bef2f](https://www.census.gov/library/publications/2001/demo/p60-214.html)

### 18. TXT 第 2452—2455 行 · 部分符合

记录：`txt-ddaf515e22-000136339-000136556`

原文：All our stores are sample stores, except as to a few classes of
articles. The goods, with these exceptions, are all at the great
central warehouse of the city, to which they are shipped directly from
the producers.

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年零售将改为看样下单：商店只陈列样品，货物从生产者直运城市中央仓库再配送，零售中间商被取消。


口径与范围：核验对象：到2000年零售将改为看样下单：商店只陈列样品，货物从生产者直运城市中央仓库再配送，零售中间商被取消。
判定：“看样下单、仓库发货”的模式在目录展厅零售中出现（Service Merchandise鼎盛时有近350家展厅），后来又有亚马逊式仓配电商；但到2000年普通商店并未普遍改成样品店，Service Merchandise本身也在1999年破产后大批关店
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-94df97fc772e](https://www.encyclopedia.com/social-sciences-and-law/economics-business-and-labor/businesses-and-occupations/service-merchandise-company-inc)；[ev-1d9d735e9736](https://jasonmiller15.substack.com/p/why-some-of-this-retailers-leases)；[ev-817622a5fc98](https://www.aboutamazon.com/news/operations/amazon-fulfillment-center-photo-tour)

### 19. TXT 第 2491—2493 行 · 错误

记录：`txt-ddaf515e22-000138874-000138984`

原文：The packages are then
delivered by larger tubes to the city districts, and thence distributed
to the houses.

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年，订购的商品将通过管道系统从中央仓库快速送到各城区并分送到户，比自己带回家还快。


口径与范围：核验对象：到2000年，订购的商品将通过管道系统从中央仓库快速送到各城区并分送到户，比自己带回家还快。
判定：1890年代起费城、纽约等城市确曾用地下气动管道传送信件，但只限邮局之间的信件，后来被停用；到2000年商品从未通过管道网络送到各家各户
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-d3f0a5f42893](https://postalmuseum.si.edu/exhibition/customers-and-communities-serving-the-cities-city-free-delivery/pneumatic-tube-mail)；[ev-ecf77fd91e5a](https://www.smithsonianmag.com/history/when-a-labyrinth-of-pneumatic-tubes-shuttled-mail-beneath-the-streets-of-new-york-city-180983472/)

### 20. TXT 第 2630—2632 行 · 正确

记录：`txt-ddaf515e22-000145802-000145963`

原文：These halls are connected
by telephone with all the houses of the city whose people care to pay
the small fee, and there are none, you may be sure, who do not.

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年，音乐厅的现场音乐将通过电话线24小时传送到每户人家，按键即可选听。


口径与范围：核验对象：到2000年，音乐厅的现场音乐将通过电话线24小时传送到每户人家，按键即可选听。
判定：1890年代欧洲已有通过电话线收听歌剧的Théâtrophone，1920年代起有经电线传送音乐的Muzak和无线电广播；到2000年家家都能随时收听各类音乐，虽然载体主要是无线电而不是电话线
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-21600f2bb200](https://en.wikipedia.org/wiki/Th%C3%A9%C3%A2trophone)；[ev-c39dcf522599](https://earlyradiohistory.us/sec003.htm)；[ev-a158994597ad](https://www.history.com/articles/muzak-invention-army-general)

### 21. TXT 第 2769—2770 行 · 部分符合

记录：`txt-ddaf515e22-000153926-000154034`

原文：Our washing is all done at public laundries at excessively
cheap rates, and our cooking at public kitchens.

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年，洗衣和做饭将主要由公共洗衣房和公共厨房完成。


口径与范围：核验对象：到2000年，洗衣和做饭将主要由公共洗衣房和公共厨房完成。
判定：外出就餐确实大幅增加，到21世纪初已占美国食品支出的一半左右，并在2023年达到峰值；但洗衣主要靠家用洗衣机（人口普查局统计绝大多数家庭有洗衣机），做饭也没有普遍交给公共厨房
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-f1c5dad7a55f](https://www.ers.usda.gov/media/18720/a-brief-history-of-food-away-from-home-in-the-united-states.pdf?v=41438)；[ev-bf9630549433](http://www.ers.usda.gov/data-products/chart-gallery/110112)；[ev-19083561fbec](https://www2.census.gov/programs-surveys/well-being/tables/1998/tab01a.pdf)

### 22. TXT 第 2771—2772 行 · 部分符合

记录：`txt-ddaf515e22-000154110-000154177`

原文：Electricity,
of course, takes the place of all fires and lighting.

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年，家庭取暖和照明将全部由电力取代明火。


口径与范围：核验对象：到2000年，家庭取暖和照明将全部由电力取代明火。
判定：照明方面基本应验：通电家庭比例由1907年的8%升到1956年的98.8%；但取暖没有“全部改用电力”，2000年用电取暖的家庭只占约30%，燃气占一半以上
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-b97758a30b7c](https://henryutd2021.github.io/learn/x03-transitions-history.html)；[ev-b6cff9a4797e](https://www.census.gov/data/tables/time-series/dec/coh-fuels.html)

### 23. TXT 第 2774 行 · 趋势符合（最终结果待验证）

记录：`txt-ddaf515e22-000154301-000154338`

原文：We have no use for domestic servants.

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年家庭将不再雇用家仆。


口径与范围：核验对象：到2000年家庭将不再雇用家仆。
判定：20世纪初中产家庭普遍雇佣佣人，此后家电普及、佣人大幅减少，到2000年普通家庭基本不再雇用住家佣人；但家政服务并未消失，富裕家庭和部分城市仍有雇佣
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-43f7f565b236](https://daily.jstor.org/how-america-tried-and-failed-to-solve-its-servant-problem/)；[ev-44d78a542f50](https://journals.sagepub.com/doi/10.1177/0891243207300764)

### 24. TXT 第 2840—2842 行 · 正确

记录：`txt-ddaf515e22-000157931-000158061`

原文：None but students who have passed the severe
tests of the schools, and clearly proved their vocation, are permitted
to practice.

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年，只有通过医学院严格考试的人才被允许行医，江湖医生不能再执业。


口径与范围：核验对象：到2000年，只有通过医学院严格考试的人才被允许行医，江湖医生不能再执业。
判定：到1910年美国几乎所有州都设立了医师执照委员会，1910年Flexner报告后医学教育和执照考试日益严格，无证行医成为违法行为
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-a05b23e9a277](https://pmc.ncbi.nlm.nih.gov/articles/PMC7011294/)；[ev-10c55ea1166c](https://www.jmronline.org/content/98/1/20)

### 25. TXT 第 3288—3291 行 · 错误

记录：`txt-ddaf515e22-000183759-000183942`

原文：the great nations of Europe as well as
Australia, Mexico, and parts of South America, are now organized
industrially like the United States, which was the pioneer of the
evolution.

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年，欧洲大国以及澳大利亚、墨西哥和部分南美国家会像美国一样实行国家统一组织的产业制度。


口径与范围：核验对象：到2000年，欧洲大国以及澳大利亚、墨西哥和部分南美国家会像美国一样实行国家统一组织的产业制度。
判定：欧洲各国战后实行的是“混合经济+福利国家”，并非国家统一经营全部产业；1980—1990年代西欧还普遍推行私有化
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-bc4b2c2a7828](https://www.cambridge.org/core/books/abs/an-economic-history-of-twentiethcentury-europe/mixed-economy-and-welfare-state-in-an-integrated-postworld-war-ii-western-europe/E)；[ev-c573a6716ddd](https://feem-media.s3.eu-central-1.amazonaws.com/wp-content/uploads/NDL2006-124.pdf)

### 26. TXT 第 3291—3292 行 · 部分符合

记录：`txt-ddaf515e22-000183943-000184050`

原文：The peaceful relations of these nations are assured by a
loose form of federal union of world-wide extent.

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年，各国的和平关系将由一个松散的全球性联邦联盟及其国际理事会保障。


口径与范围：核验对象：到2000年，各国的和平关系将由一个松散的全球性联邦联盟及其国际理事会保障。
判定：国际联盟（1920）和联合国（1945）先后成立，宗旨正是促进国际合作、维护和平；但它们没有“保障”和平，联合国未能阻止卢旺达、斯雷布雷尼察等惨剧
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-7fa07323af24](https://www.un.org/en/about-us/history-of-the-un/predecessor)；[ev-6fddb83eb469](https://digitalcommons.usf.edu/cgi/viewcontent.cgi?article=1141&context=gsp)

### 27. TXT 第 3355—3356 行 · 暂无法判断

记录：`txt-ddaf515e22-000187767-000187842`

原文：we all look forward to an eventual
unification of the world as one nation.

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：最终世界会统一为一个国家。


口径与范围：核验对象：最终世界会统一为一个国家。
判定：书中把世界统一为一国说成即便到2000年也仍是“最终”的远景，没有给出时间；至今联合国有193个成员国，世界联邦运动在1950年代后衰落，远景仍未到期，无法判断
限制：只核对预测结果是否出现，不评价书中的因果解释；终点或条件尚未到来。
观察终点：未形成可判定观察终点；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-f283b0bf86b2](https://research.un.org/en/unmembers/intro)；[ev-cd2c9dd3475b](https://www.thefederalist.eu/site/index.php/en/essays/1892-the-world-federalist-movements-from-1945-to-1954-and-european-integration)

### 28. TXT 第 3405—3406 行 · 错误

记录：`txt-ddaf515e22-000190663-000190755`

原文：Subject to these regulations,
the right of any man to emigrate at any time is unrestricted.

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年，在国家间补偿安排下，任何人任何时候移居他国的权利不受限制。


口径与范围：核验对象：到2000年，在国家间补偿安排下，任何人任何时候移居他国的权利不受限制。
判定：1948年《世界人权宣言》第13条承认“离开任何国家”的权利，但入境移民普遍受限：美国1924年起实行国别配额，各国至今仍严格管控移民
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-0a773e71fa5c](https://www.ohchr.org/en/human-rights/universal-declaration/translations/english)；[ev-72121719b7b8](https://history.state.gov/milestones/1921-1936/immigration-act)

### 29. TXT 第 3430—3432 行 · 部分符合

记录：`txt-ddaf515e22-000191948-000192083`

原文：The two
minor meals of the day are usually taken at home, as not worth the
trouble of going out; but it is general to go out to dine.

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年，人们正餐普遍去社区公共餐厅吃。


口径与范围：核验对象：到2000年，人们正餐普遍去社区公共餐厅吃。
判定：到20世纪末美国人的饮食重心确已大幅转向外出就餐和外卖；但吃饭的地方是商业餐馆和快餐店，而不是书中设想的社区公共餐厅
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-f1c5dad7a55f](https://www.ers.usda.gov/media/18720/a-brief-history-of-food-away-from-home-in-the-united-states.pdf?v=41438)；[ev-5509ece09bdf](https://ers.usda.gov/sites/default/files/_laserfiche/publications/44117/29269_eib19.pdf?v=83611)

### 30. TXT 第 3578—3579 行 · 错误

记录：`txt-ddaf515e22-000200175-000200291`

原文：She said to me that at the present time all the streets were provided
against inclement weather in the manner I saw

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年，波士顿所有街道下雨时都会放下连续防水顶棚，使人行道成为干燥走廊。


口径与范围：核验对象：到2000年，波士顿所有街道下雨时都会放下连续防水顶棚，使人行道成为干燥走廊。
判定：城市街道没有普遍加装可收放的防雨顶棚；只有少数城市建有局部连廊，例如明尼阿波利斯1962年起建的空中走廊系统（约80个街区）
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-9f3cf7eed59e](https://www.mnhs.org/mnopedia/search/index/structure/minneapolis-skyways)；[ev-a03b4b00af85](https://www.minneapolis.org/map-transportation/minneapolis-skyway-guide/)

### 31. TXT 第 3698—3699 行 · 错误

记录：`txt-ddaf515e22-000206879-000207004`

原文：The equal wealth and equal opportunities of culture which
all persons now enjoy have simply made us all members of one class

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年，财富和受教育机会将完全平等，社会阶级差别消失。


口径与范围：核验对象：到2000年，财富和受教育机会将完全平等，社会阶级差别消失。
判定：财富与阶层差距没有消失：美联储数据显示1989—2016年最富1%家庭的财富份额持续上升；教育虽大幅普及，但教育不平等依然存在
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-85eea30e608a](https://www.federalreserve.gov/econres/notes/feds-notes/wealth-concentration-levels-and-growth-1989-2016-accessible-20200220.htm)；[ev-d991568f4fb7](https://www.pnas.org/doi/full/10.1073/pnas.1907258117)

### 32. TXT 第 3817—3820 行 · 部分符合

记录：`txt-ddaf515e22-000213664-000213840`

原文：There ensued an era
of mechanical invention, scientific discovery, art, musical and
literary productiveness to which no previous age of the world offers
anything comparable.

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：20世纪（社会变革后）将出现前所未有的机械发明、科学发现和文艺创作高潮。


口径与范围：核验对象：20世纪（社会变革后）将出现前所未有的机械发明、科学发现和文艺创作高潮。
判定：20世纪确实出现了前所未有的发明与科学突破（汽车、电话、相对论、量子力学等迅速改变日常生活）；但这并非书中设想的社会制度变革所激发，文艺“空前繁荣”也难以客观衡量
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-1b37ed5d9928](https://www.sciencenews.org/article/century-scientific-innovation-invention-technology)；[ev-f8f5f9548ea0](https://en.wikipedia.org/wiki/20th_century_in_science)

### 33. TXT 第 3954—3956 行 · 错误

记录：`txt-ddaf515e22-000221641-000221763`

原文：The people who take the paper pay the
expense of its publication, choose its editor, and remove him when
unsatisfactory.

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年，报纸由订户出资并选举、罢免编辑，政府不干预其立场。


口径与范围：核验对象：到2000年，报纸由订户出资并选举、罢免编辑，政府不干预其立场。
判定：到2000年美国报纸仍是私人商业经营、主要依靠广告：当年报纸广告支出达487亿美元，报业还在不断集中；订户出资并选举编辑的合作社报纸只是2010年代才出现的零星个案
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-275093315954](https://www.mediapost.com/publications/article/11138/ad-spending-in-newspapers-hit-487-billion-in-200.html)；[ev-ac186cbc18cc](https://pmc.ncbi.nlm.nih.gov/articles/PMC12714153/)

### 34. TXT 第 4397—4398 行 · 部分符合

记录：`txt-ddaf515e22-000246848-000246925`

原文：The prices of the staples grow less year by
year, but rarely, if ever, rise.

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年，生活必需品的价格会逐年下降，几乎从不上涨。


口径与范围：核验对象：到2000年，生活必需品的价格会逐年下降，几乎从不上涨。
判定：按实际价格计，1900—2000年消费者支付的食品价格确有下降，食品支出占收入的比重也持续下降；但名义物价并非“逐年下降、几乎从不上涨”，美国CPI在20世纪大幅上升
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-1ee98eb81adb](https://eh.net/encyclopedia/u-s-agriculture-in-the-twentieth-century/)；[ev-df45fede027b](https://www2.census.gov/library/publications/2004/compendia/statab/123ed/hist/hs-36.pdf)

### 35. TXT 第 4659—4660 行 · 部分符合

记录：`txt-ddaf515e22-000262537-000262607`

原文：Persons of average constitution usually live to
eighty-five or ninety

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年，体质一般的人通常能活到85到90岁。


口径与范围：核验对象：到2000年，体质一般的人通常能活到85到90岁。
判定：寿命显著延长，但“通常活到85—90岁”没有实现：2000年美国出生时预期寿命为76.6岁（女性79.3岁），65岁老人的余寿约18年
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-2e096651c551](https://countryeconomy.com/demography/life-expectancy/usa?year=2000)；[ev-70e416ed1f48](https://www.cdc.gov/nchs/data/nvsr/nvsr51/nvsr51_03.pdf)

### 36. TXT 第 4671—4673 行 · 错误

记录：`txt-ddaf515e22-000263223-000263328`

原文：The
professional sportsmen, which were such a curious feature of your day,
we have nothing answering to

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年将没有职业运动员，体育比赛不设金钱奖励。


口径与范围：核验对象：到2000年将没有职业运动员，体育比赛不设金钱奖励。
判定：职业体育反而高度商业化：2000年美国职棒大联盟球员平均年薪升至约190万美元；奥运会也在1980年代后逐步向职业运动员开放并设奖金
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-cabbc2b9762c](http://cgi.usatoday.com/sports/baseball/salary/00final.htm)；[ev-9a82b06811b3](https://www.reuters.com/sports/key-moments-path-amateurism-professionalism-2024-04-10/)

### 37. TXT 第 4701—4702 行 · 错误

记录：`txt-ddaf515e22-000264872-000264950`

原文：We have no
jails nowadays. All cases of atavism are treated in the hospitals.

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年将没有监狱，犯罪被当作返祖病症在医院治疗。


口径与范围：核验对象：到2000年将没有监狱，犯罪被当作返祖病症在医院治疗。
判定：监狱没有消失，反而急剧扩张：2000年底美国州和联邦监狱关押138万人，监禁率从1980年的每10万人139人升到2000年的478人
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-813921270f90](https://bjs.ojp.gov/content/pub/pdf/p00.pdf)；[ev-b425554586be](https://www.justice.gov/archive/mps/strategic2001-2006/d_incrt.htm)

### 38. TXT 第 4776 行 · 错误

记录：`txt-ddaf515e22-000268970-000269006`

原文：We do without the lawyers, certainly

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年将不再有律师这一职业。


口径与范围：核验对象：到2000年将不再有律师这一职业。
判定：律师职业大幅扩张：1900—2000年美国律师人数从114,460人增至100多万，增长793%
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-011f72ab7349](https://www.americanbar.org/news/profile-legal-profession/demographics/)；[ev-77106b428982](https://www.americanbarfoundation.org/wp-content/uploads/2023/05/2005_lawyer_statistical_report.pdf)

### 39. TXT 第 4914—4915 行 · 错误

记录：`txt-ddaf515e22-000276957-000277012`

原文：We have no army or navy, and no military
organization.

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年美国将没有陆军、海军和任何军事组织。


口径与范围：核验对象：到2000年美国将没有陆军、海军和任何军事组织。
判定：美国2000财年现役士兵约115万人（仅士兵），国防拨款数千亿美元，陆海军依然庞大
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-230a08582b13](https://www.cna.org/pop-rep/2000/html/chapter3/chapter3.htm)；[ev-fd1b902d4d78](https://www.everycrsreport.com/files/19991027_RL30205_2175ae2e3789a83c62acbcdffb6cc4d241ccc85a.html)

### 40. TXT 第 4915—4916 行 · 错误

记录：`txt-ddaf515e22-000277013-000277117`

原文：We have no departments of state or treasury, no excise or
revenue services, no taxes or tax collectors.

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年美国将没有国务院、财政部、税收和税务人员。


口径与范围：核验对象：到2000年美国将没有国务院、财政部、税收和税务人员。
判定：财政部和国务院依然存在，国税局2000财年征收了上万亿美元税款，税收和税务人员并未消失
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-bd8bb10d978b](https://www.irs.gov/pub/irs-soi/00databk.pdf)；[ev-ea21ed69678c](https://home.treasury.gov/about/history/history-overview/history-of-the-treasury)

### 41. TXT 第 4927 行 · 错误

记录：`txt-ddaf515e22-000277637-000277704`

原文：We have no legislation," replied Dr. Leete, "that is, next to none.

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年国会几乎不再立法，州议会不复存在。


口径与范围：核验对象：到2000年国会几乎不再立法，州议会不复存在。
判定：立法没有消失：第106届国会（1999—2000年）制定了580项法律；各州议会也一直存在并持续运作
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-e97ebb50995a](https://en.wikisource.org/wiki/Portal:Acts_of_the_United_States_Congresses/Acts_of_the_106th_United_States_Congress)；[ev-95834d5b999a](https://www.governing.com/politics/the-evolution-of-state-legislatures-throughout-u-s-history)

### 42. TXT 第 5139—5141 行 · 错误

记录：`txt-ddaf515e22-000288403-000288597`

原文：We have simply added to the common school system of
compulsory education, in vogue in Massachusetts a hundred years ago, a
half dozen higher grades, carrying the youth to the age of twenty-one

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年，义务教育将延长到21岁，人人都接受高等教育。


口径与范围：核验对象：到2000年，义务教育将延长到21岁，人人都接受高等教育。
判定：2000年各州义务教育上限一般为16—18岁，并未延长到21岁；2000年人口普查时25岁以上人口中80%有高中及以上学历，但远非人人接受高等教育
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-2f1ad71a2836](https://nces.ed.gov/programs/digest/d02/tables/PDF/table150.pdf)；[ev-77e8efc6b0c0](https://www2.census.gov/library/publications/decennial/2000/briefs/c2kbr-24.pdf)

### 43. TXT 第 5300—5302 行 · 错误

记录：`txt-ddaf515e22-000298409-000298583`

原文：Insanity, for instance, which in the nineteenth century was so
terribly common a product of your insane mode of life, has almost
disappeared, with its alternative, suicide.

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年，精神失常和自杀几乎绝迹。


口径与范围：核验对象：到2000年，精神失常和自杀几乎绝迹。
判定：精神疾病和自杀没有绝迹：美国1990—2003年精神障碍患病率稳定在约30%；CDC统计2000年起年龄调整自杀率每年仍有数万人死亡并在此后上升
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-c85ae524da2d](https://www.nejm.org/doi/full/10.1056/NEJMsa043266)；[ev-6b07ceee3926](https://www.cdc.gov/nchs/data/databriefs/db309%5Ftable.pdf)

### 44. TXT 第 5349—5350 行 · 错误

记录：`txt-ddaf515e22-000301176-000301262`

原文：We have no national, state, county, or municipal
debts, or payments on their account.

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年，各级政府都没有公共债务。


口径与范围：核验对象：到2000年，各级政府都没有公共债务。
判定：各级政府都背负公共债务：2000年联邦债务达数万亿美元，人口普查局另有州和地方政府债务统计
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-284fc740ba74](https://www.govinfo.gov/content/pkg/BUDGET-2002-TAB/pdf/BUDGET-2002-TAB-9-1.pdf)；[ev-fa124f37eca9](https://www.census.gov/data/datasets/2000/econ/local/public-use-datasets.html)

### 45. TXT 第 5383—5386 行 · 错误

记录：`txt-ddaf515e22-000303285-000303457`

原文：Our statisticians
calculate that one eightieth part of our workers suffices for all the
processes of distribution which in your day required one eighth of the
population

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年，商品流通（批发零售）所需劳动力只占全部劳动者的八十分之一，而19世纪占人口的八分之一。


口径与范围：核验对象：到2000年，商品流通（批发零售）所需劳动力只占全部劳动者的八十分之一，而19世纪占人口的八分之一。
判定：流通环节的就业比重不降反升：零售业占美国民用就业的比例从1958年的12.6%升到2000年的16.4%，加上批发业约5%，远高于“八十分之一”
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-31ed8b358e54](https://www2.census.gov/ces/wp/2005/CES-WP-05-30.pdf)；[ev-79ef1f0f5bd3](https://www.bls.gov/careeroutlook/2001/Winter/art04.pdf)

### 46. TXT 第 5625—5626 行 · 错误

记录：`txt-ddaf515e22-000318706-000318805`

原文：Except for slight occasional effects of such
natural causes, there are no fluctuations of business

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年将不再有经济危机和商业周期波动。


口径与范围：核验对象：到2000年将不再有经济危机和商业周期波动。
判定：商业周期没有消失：NBER持续记录20世纪的历次经济衰退，2001年3月美国又进入一轮衰退
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-45b760eccb0c](https://www.nber.org/research/data/us-business-cycle-expansions-and-contractions)；[ev-cc9c6a3925ca](https://www.nber.org/news/business-cycle-dating-committee-announcement-november-26-2001)

### 47. TXT 第 5962—5963 行 · 错误

记录：`txt-ddaf515e22-000337610-000337678`

原文：Then the national party arose to carry it
out by political methods.

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：将会兴起一个以国有化生产和分配为目标的“国家党”，并通过政治手段（赢得全国多数）实现这一变革。


口径与范围：核验对象：将会兴起一个以国有化生产和分配为目标的“国家党”，并通过政治手段（赢得全国多数）实现这一变革。
判定：受本书影响的民族主义运动与1890年代人民党有所交集，社会党在1912年也曾在一些城市获胜；但没有任何以国有化全部生产为目标的政党赢得全国多数，书中设想的变革从未实现
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-7dd633c05f55](https://edwardbellamyhouse.org/2022/10/31/talking-politics-edward-bellamy-populism-and-the-election-of-1892/)；[ev-8e36bfc6f6d9](https://en.wikipedia.org/wiki/Socialist_Party_of_America)

### 48. TXT 第 6015—6016 行 · 趋势符合（最终结果待验证）

记录：`txt-ddaf515e22-000340552-000340670`

原文：Our women, as well as our men, are members of the
industrial army, and leave it only when maternal duties claim them.

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年，女性将和男性一样参加社会劳动，婚后也不必离开工作，只在生育抚养时暂离。


口径与范围：核验对象：到2000年，女性将和男性一样参加社会劳动，婚后也不必离开工作，只在生育抚养时暂离。
判定：女性劳动参与率从1950年的33.9%升到1998年接近60%，女性大规模进入职场、婚后继续工作成为常态；但并非和男性一样全员参加，带婴儿的母亲中工作的比例2000年只有51.0%
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-3d52d1ad04a5](https://www.bls.gov/opub/ted/2000/feb/wk3/art03.htm)；[ev-a9ad7c1b6b2e](https://www.bls.gov/opub/ted/2001/apr/wk5/art04.htm)

### 49. TXT 第 6072—6073 行 · 正确

记录：`txt-ddaf515e22-000344002-000344085`

原文：we have women on the
bench, appointed by the general of the women, as well as men.

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年将有女性法官。


口径与范围：核验对象：到2000年将有女性法官。
判定：女性法官早已出现：Florence Allen成为首位当选司法职务的女性，此后女性陆续进入联邦法院；到2001年联邦法官中约22%是女性
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-bac0139b5e24](https://www.supremecourt.ohio.gov/courts/judicial-system/supreme-court-of-ohio/justices-1803-to-present/florence-allen/)；[ev-c28be85ad83e](https://teachingamericanhistory.org/document/a-latina-judges-voice-2/)；[ev-40c4fed02ec2](https://www.uscourts.gov/data-news/judiciary-news/2015/02/26/women-way-pavers-federal-judiciary)

### 50. TXT 第 6411—6412 行 · 部分符合

记录：`txt-ddaf515e22-000364290-000364362`

原文：he preaches only by telephone, and to audiences often
reaching 150,000.

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年，大多数布道将通过电话线传到订户家中，单场听众可达15万人。


口径与范围：核验对象：到2000年，大多数布道将通过电话线传到订户家中，单场听众可达15万人。
判定：远程布道确实出现并拥有巨大听众：1920年代起有广播布道，Billy Graham等人通过电台、电视面向数以百万计的听众；但大多数布道仍在教堂现场进行，约七成美国人仍是教会成员
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-08a7508cff65](https://billygrahamlibrary.org/blog-billy-grahams-radio-ministry/)；[ev-c0d941366f60](https://www.encyclopedia.com/environment/encyclopedias-almanacs-transcripts-and-maps/religious-broadcasting)；[ev-2e726b11af5d](https://news.gallup.com/poll/2974/america-remains-predominantly-christian.aspx)

### 51. TXT 第 7317—7319 行 · 错误

记录：`txt-ddaf515e22-000419077-000419190`

原文：There had been no personal
advertising in the Boston of the twentieth century, because there was
no need of any

时间窗口：隐含，从出版年 1888 到截止日 2026-11-15。原文未写期限；该窗口内方向发生即按此评分。

扩展观点（解释，非原文）：到2000年，个人和商家广告将完全消失。


口径与范围：核验对象：到2000年，个人和商家广告将完全消失。
判定：商业广告非但没有消失，反而长期维持在GDP的约2%，2026年美国广告总支出估计约3,610亿美元
限制：只核对预测结果是否出现，不评价书中的因果解释；证据为公开统计/权威资料的摘录。
观察终点：2026-11-15；条件状态：unconditional。
思考方法：按METHOD.md §4：先定scope，再各做一次support/counter检索（Exa），从返回URL中选源并存档（data/sources，sha256），由助手阅读后写评断；替代verify_prediction的模型调用（研究者归纳；方法有效性未由此证明）。
证据：[ev-6fb514f3fb7c](https://www.econlib.org/library/Enc/Advertising.html)；[ev-5ff93453c7d5](https://content.ibisworld.com/media/twpnf2mv/total-advertising-expenditure-total-advertising-expenditure-business-environment-profile-by-ibisworld.pdf)

## 证据登记

哈希校验只证明本地保存内容未改变。检索摘录与完整原始文件会按证据记录注明；两者均不能代替对来源与命题对应关系的判断。

- [ev-bb20e82b61bf](https://www2.census.gov/programs-surveys/decennial/tables/time-series/coh-fuels/fuels2000.txt)；资料日期：未确定；覆盖：https://www2.census.gov/programs-surveys/decennial/tables/time-series/coh-fuels/fuels2000.txt。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-b6cff9a4797e](https://www.census.gov/data/tables/time-series/dec/coh-fuels.html)；资料日期：未确定；覆盖：Historical Census of Housing Tables: House Heating Fuel。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-463406addd71](https://www.bls.gov/wsp/factsheets/summary-of-work-stoppages-in-the-united-states.htm)；资料日期：未确定；覆盖：Trends in Work Stoppages : U.S. Bureau of Labor Statistics。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-4cbd7c65bc42](https://www.latimes.com/archives/la-xpm-2000-feb-10-fi-62793-story.html)；资料日期：2000-02-10；覆盖：17,000 Boeing Engineers, Tech Workers Walk Out - Los Angeles Times。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-aa9783e29bca](http://naomi-lamoreaux.squarespace.com/the-great-merger-movement)；资料日期：未确定；覆盖：The Great Merger Movement — Naomi R. Lamoreaux。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-ed2f6a7d98ae](https://ciaotest.cc.columbia.edu/olj/ep/ep_jan06/ep_jan06c.pdf)；资料日期：未确定；覆盖：Small Business in U.S. History - Entrepreneurship and Small Business: Economic Perspectives - Volume 11, Number 1 January 2006。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-83172ac154f4](https://digfir-published.macmillanusa.com/roark7e/roark7e_ch18_11.html)；资料日期：未确定；覆盖：18. Railroads, Business, and Politics in the Gilded Age, 1865–1900。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-620c8ef393ff](https://www.annenbergclassroom.org/timeline_event/northern-securities-co-v-united-states/)；资料日期：未确定；覆盖：Proposed Merger Of Rail Companies Banned – Annenberg Classroom。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-97c5de1e5fb2](https://en.wikipedia.org/wiki/Nationalist_Clubs)；资料日期：2026-11-02；覆盖：Nationalist Clubs。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-c7458d88a927](https://usa.usembassy.de/etexts/oecon/chap2.htm)；资料日期：未确定；覆盖：Outline of the U.S. Economy。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-bd560fe255ac](https://en.wikipedia.org/wiki/List_of_wars_involving_the_United_States_in_the_20th_century)；资料日期：2026-11-08；覆盖：List of wars involving the United States in the 20th century。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-32cc1fa62ab8](https://2001-2009.state.gov/r/pa/ho/time/pcw/index.htm)；资料日期：未确定；覆盖：1989-2000。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-2db61bc04c57](https://en.wikipedia.org/wiki/Long_Peace)；资料日期：2026-11-04；覆盖：Long Peace。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-75ae84599579](https://www.archives.gov/electoral-college/2000)；资料日期：未确定；覆盖：2000 Electoral College Results | National Archives。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-7bcea9172a77](https://www.presidency.ucsb.edu/statistics/elections/2000)；资料日期：未确定；覆盖：2000 | The American Presidency Project。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-98b766ca3775](https://www.prb.org/resources/the-size-and-shape-of-americas-government/)；资料日期：2002-05-01；覆盖：The Size and Shape of America’s Government | PRB。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-59cbf4b35247](https://www.bls.gov/opub/mlr/2004/10/art3full.pdf)；资料日期：未确定；覆盖：Employment in the public sector: two recessions' impact on jobs。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-638c0d8669d2](http://www.bls.gov/opub/mlr/2000/07/art2full.pdf)；资料日期：未确定；覆盖：Gauging the labor force effects of retiring baby-boomers。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-cf8395a20fb5](https://www.ssa.gov/benefits/retirement/planner/ageincrease.html)；资料日期：未确定；覆盖：Benefits Planner: Retirement | Retirement Age Calculator | SSA。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-38c45a67c892](https://www.cdc.gov/mmwr/preview/mmwrhtml/mm4822a1.htm)；资料日期：未确定；覆盖：Achievements in Public Health, 1900-1999: Improvements in Workplace Safety -- United States, 1900-1999。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-e71e301917f8](https://www.bls.gov/iif/fatal-injuries-tables/archive/census-of-fatal-occupational-injuries-news-release-2000.pdf)；资料日期：未确定；覆盖：CF NR National Census of Fatal Occupational Injuries in 2000。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-8e3beb09f43e](https://nces.ed.gov/programs/coe/pdf/Indicator_CPA/coe_cpa_2018_05.pdf)；资料日期：未确定；覆盖：Immediate College Enrollment Rate。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-2d0e1a757f53](https://www.americanprogress.org/article/affordability-of-postsecondary-education-equity-and-adequacy-across-the-50-states/)；资料日期：2005-01-03；覆盖：Affordability of Postsecondary Education: Equity and Adequacy Across the 50 States - Center for American Progress。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-c6aac53a1e06](https://www2.census.gov/retail/releases/benchmark/annpub00.pdf)；资料日期：未确定；覆盖：Annual Benchmark Report for Retail and Food Services:  January 1992 to December 2000。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-890b99d157c9](https://www2.census.gov/library/publications/2008/compendia/statab/128ed/tables/09s1017.pdf)；资料日期：未确定；覆盖：Statistical Abstract of the United States: 2009。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-79c60236d8b4](https://www.federalreserve.gov/newsevents/testimony/roseman20100720a_accessible.htm)；资料日期：未确定；覆盖：Federal Reserve Board - Accessible version。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-97bbb5f8ebeb](https://www.pewresearch.org/short-reads/2026/08/26/fewer-americans-use-cash-today-than-a-decade-ago-but-many-still-carry-it/)；资料日期：2026-08-26；覆盖：Fewer Americans use cash today than in 2015, but many still carry it | Pew Research Center。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-d00c1b522392](https://www.historyofinformation.com/detail.php?entryid=2044)；资料日期：未确定；覆盖：History of Information。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-1a5df9977c3f](https://www.history.com/articles/when-were-credit-cards-invented)；资料日期：2026-01-12；覆盖：When Were Credit Cards Invented? | HISTORY。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-e321cd5959e3](https://americanhistory.si.edu/explore/exhibitions/value-money/online/innovations-money/plastic-payments)；资料日期：未确定；覆盖：Plastic Payments。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-becdbf4c53fb](https://archives.history.ac.uk/history-in-focus/welfare/articles/katzm.html)；资料日期：未确定；覆盖：The American Welfare State by Michael B. Katz。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-6a00d5b28d73](https://www.census.gov/library/publications/2001/demo/p60-215.html)；资料日期：2001-09-01；覆盖：Health Insurance Coverage: 2000。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-1c3a74b14771](https://www2.census.gov/library/publications/2001/demographics/p60-213.pdf)；资料日期：未确定；覆盖：Money Income in the United States: 2000。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-4b668f8d12d0](https://www.epi.org/publication/books_swa2000_swa2000intro/)；资料日期：未确定；覆盖：The State of Working America 2000-01 | Economic Policy Institute。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-6feae0236447](https://www.bls.gov/cps/cpswp2000.htm)；资料日期：未确定；覆盖：A Profile of the Working Poor, 2000 : U.S. Bureau of Labor Statistics。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-4ff5693bef2f](https://www.census.gov/library/publications/2001/demo/p60-214.html)；资料日期：2001-09-01；覆盖：Poverty in the United States: 2000。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-94df97fc772e](https://www.encyclopedia.com/social-sciences-and-law/economics-business-and-labor/businesses-and-occupations/service-merchandise-company-inc)；资料日期：未确定；覆盖：Service Merchandise Company Inc | Encyclopedia.com。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-1d9d735e9736](https://jasonmiller15.substack.com/p/why-some-of-this-retailers-leases)；资料日期：2026-03-18；覆盖：Why Some Of This Retailer’s Leases Still Exist More Than 27 Years After It Filed For Bankruptcy。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-817622a5fc98](https://www.aboutamazon.com/news/operations/amazon-fulfillment-center-photo-tour)；资料日期：2023-04-26；覆盖：See inside an Amazon fulfillment center and how it works。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-d3f0a5f42893](https://postalmuseum.si.edu/exhibition/customers-and-communities-serving-the-cities-city-free-delivery/pneumatic-tube-mail)；资料日期：未确定；覆盖：Pneumatic Tube Mail。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-ecf77fd91e5a](https://www.smithsonianmag.com/history/when-a-labyrinth-of-pneumatic-tubes-shuttled-mail-beneath-the-streets-of-new-york-city-180983472/)；资料日期：2023-12-22；覆盖：When a Labyrinth of Pneumatic Tubes Shuttled Mail Beneath the Streets of New York City。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-21600f2bb200](https://en.wikipedia.org/wiki/Th%C3%A9%C3%A2trophone)；资料日期：2026-08-11；覆盖：Théâtrophone。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-c39dcf522599](https://earlyradiohistory.us/sec003.htm)；资料日期：未确定；覆盖：3. News and Entertainment by Telephone (1876-1930)。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-a158994597ad](https://www.history.com/articles/muzak-invention-army-general)；资料日期：2024-10-15；覆盖：The Army General Who Invented Muzak | HISTORY。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-f1c5dad7a55f](https://www.ers.usda.gov/media/18720/a-brief-history-of-food-away-from-home-in-the-united-states.pdf?v=41438)；资料日期：未确定；覆盖：America’s Eating Habits: Food Away From Home。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-bf9630549433](http://www.ers.usda.gov/data-products/chart-gallery/110112)；资料日期：未确定；覆盖：Food-away-from-home spending share peaked in 2023 | Economic Research Service。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-19083561fbec](https://www2.census.gov/programs-surveys/well-being/tables/1998/tab01a.pdf)；资料日期：未确定；覆盖：Table 1 A. Consumer Durables by Social Characteristics:  Households with Clothes Washer, Clothes Dryer, Dish Washer, and Refrigerator:  1998。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-b97758a30b7c](https://henryutd2021.github.io/learn/x03-transitions-history.html)；资料日期：未确定；覆盖：How fast have energy transitions happened before? – Honglin Li。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-43f7f565b236](https://daily.jstor.org/how-america-tried-and-failed-to-solve-its-servant-problem/)；资料日期：2017-04-03；覆盖：How America Tried (and Failed) to Solve Its "Servant Problem" - JSTOR Daily。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-44d78a542f50](https://journals.sagepub.com/doi/10.1177/0891243207300764)；资料日期：未确定；覆盖：Doing the Dirty Work - Mignon Duffy, 2007。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-a05b23e9a277](https://pmc.ncbi.nlm.nih.gov/articles/PMC7011294/)；资料日期：2019-11-06；覆盖：State Medical Boards, Licensure, and Discipline in the United States - PMC。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-10c55ea1166c](https://www.jmronline.org/content/98/1/20)；资料日期：2012-03-01；覆盖：The History of the Federation of State Medical Boards: Part One — 19th Century Origins of FSMB and Modern Medical Regulation | Journal Of Medical Regulation。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-bc4b2c2a7828](https://www.cambridge.org/core/books/abs/an-economic-history-of-twentiethcentury-europe/mixed-economy-and-welfare-state-in-an-integrated-postworld-war-ii-western-europe/E)；资料日期：未确定；覆盖：https://www.cambridge.org/core/books/abs/an-economic-history-of-twentiethcentury-europe/mixed-economy-and-welfare-state-in-an-integrated-postworld-war-ii-wester。限制：网页存档（curl），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-c573a6716ddd](https://feem-media.s3.eu-central-1.amazonaws.com/wp-content/uploads/NDL2006-124.pdf)；资料日期：未确定；覆盖：Privatization in Western Europe。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-7fa07323af24](https://www.un.org/en/about-us/history-of-the-un/predecessor)；资料日期：未确定；覆盖：Predecessor: The League of Nations | United Nations。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-6fddb83eb469](https://digitalcommons.usf.edu/cgi/viewcontent.cgi?article=1141&context=gsp)；资料日期：未确定；覆盖：Failures to Prevent Genocide in Rwanda (1994), Srebrenica (1995), and Darfur (since 2003)。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-f283b0bf86b2](https://research.un.org/en/unmembers/intro)；资料日期：未确定；覆盖：Introduction - UN Membership - Research Guides at United Nations Dag Hammarskjöld Library。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-cd2c9dd3475b](https://www.thefederalist.eu/site/index.php/en/essays/1892-the-world-federalist-movements-from-1945-to-1954-and-european-integration)；资料日期：未确定；覆盖：The World Federalist Movements from 1945 to 1954 and European Integration。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-0a773e71fa5c](https://www.ohchr.org/en/human-rights/universal-declaration/translations/english)；资料日期：未确定；覆盖：OHCHR | Universal Declaration of Human Rights - English。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-72121719b7b8](https://history.state.gov/milestones/1921-1936/immigration-act)；资料日期：未确定；覆盖：Milestones in the History of U.S. Foreign Relations - Office of the Historian。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-5509ece09bdf](https://ers.usda.gov/sites/default/files/_laserfiche/publications/44117/29269_eib19.pdf?v=83611)；资料日期：未确定；覆盖：Let's Eat Out: Americans Weigh Taste, Convenience, and Nutrition。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-9f3cf7eed59e](https://www.mnhs.org/mnopedia/search/index/structure/minneapolis-skyways)；资料日期：2013-12-31；覆盖：Minneapolis Skyways | MNopedia。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-a03b4b00af85](https://www.minneapolis.org/map-transportation/minneapolis-skyway-guide/)；资料日期：未确定；覆盖：Minneapolis Skyway Guide | Meet Minneapolis。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-85eea30e608a](https://www.federalreserve.gov/econres/notes/feds-notes/wealth-concentration-levels-and-growth-1989-2016-accessible-20200220.htm)；资料日期：未确定；覆盖：Federal Reserve Board - Wealth concentration levels and growth: 1989-2016, Accessible Data。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-d991568f4fb7](https://www.pnas.org/doi/full/10.1073/pnas.1907258117)；资料日期：未确定；覆盖：A century of educational inequality in the United States。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-1b37ed5d9928](https://www.sciencenews.org/article/century-scientific-innovation-invention-technology)；资料日期：2022-03-18；覆盖：What made the last century's great innovations possible?。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-f8f5f9548ea0](https://en.wikipedia.org/wiki/20th_century_in_science)；资料日期：2026-07-02；覆盖：20th century in science。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-275093315954](https://www.mediapost.com/publications/article/11138/ad-spending-in-newspapers-hit-487-billion-in-200.html)；资料日期：未确定；覆盖：Ad Spending in Newspapers Hit $48.7 Billion in 2000 03/07/2001。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-ac186cbc18cc](https://pmc.ncbi.nlm.nih.gov/articles/PMC12714153/)；资料日期：2024-09-23；覆盖：‘You can’t buy a revolution, but you can support a paper fighting for one’: Journalism cooperatives’ organizational traits and journalistic missions。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-1ee98eb81adb](https://eh.net/encyclopedia/u-s-agriculture-in-the-twentieth-century/)；资料日期：未确定；覆盖：U.S. Agriculture in the Twentieth Century – EH.net。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-df45fede027b](https://www2.census.gov/library/publications/2004/compendia/statab/123ed/hist/hs-36.pdf)；资料日期：未确定；覆盖：No. HS-36. Consumer and Gross Domestic Price Indexes: 1913 to 2002。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-2e096651c551](https://countryeconomy.com/demography/life-expectancy/usa?year=2000)；资料日期：未确定；覆盖：United States - Life expectancy at birth 2000 | countryeconomy.com。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-70e416ed1f48](https://www.cdc.gov/nchs/data/nvsr/nvsr51/nvsr51_03.pdf)；资料日期：未确定；覆盖：National Vital Statistics Reports, Vol. 51, No. 3, (12/19/2002)。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-cabbc2b9762c](http://cgi.usatoday.com/sports/baseball/salary/00final.htm)；资料日期：2000-12-21；覆盖：Salaries soared, according to annual survey。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-9a82b06811b3](https://www.reuters.com/sports/key-moments-path-amateurism-professionalism-2024-04-10/)；资料日期：2024-04-10；覆盖：Key moments in path from amateurism to professionalism。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-813921270f90](https://bjs.ojp.gov/content/pub/pdf/p00.pdf)；资料日期：未确定；覆盖：Prisoners in 2000。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-b425554586be](https://www.justice.gov/archive/mps/strategic2001-2006/d_incrt.htm)；资料日期：未确定；覆盖：Description of incarceration rates trend chart。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-011f72ab7349](https://www.americanbar.org/news/profile-legal-profession/demographics/)；资料日期：未确定；覆盖：Demographics。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-77106b428982](https://www.americanbarfoundation.org/wp-content/uploads/2023/05/2005_lawyer_statistical_report.pdf)；资料日期：未确定；覆盖：THE LAWYER STATISTICAL REPORT。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-230a08582b13](https://www.cna.org/pop-rep/2000/html/chapter3/chapter3.htm)；资料日期：未确定；覆盖：Active Component Enlisted Force。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-fd1b902d4d78](https://www.everycrsreport.com/files/19991027_RL30205_2175ae2e3789a83c62acbcdffb6cc4d241ccc85a.html)；资料日期：未确定；覆盖：RL30205 -- Appropriations for FY2000: Defense。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-bd8bb10d978b](https://www.irs.gov/pub/irs-soi/00databk.pdf)；资料日期：未确定；覆盖：P:\WILLIS\databk\00\Data Book 2。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-ea21ed69678c](https://home.treasury.gov/about/history/history-overview/history-of-the-treasury)；资料日期：未确定；覆盖：History of the Treasury | U.S. Department of the Treasury。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-e97ebb50995a](https://en.wikisource.org/wiki/Portal:Acts_of_the_United_States_Congresses/Acts_of_the_106th_United_States_Congress)；资料日期：未确定；覆盖：Acts of the United States Congresses/Acts of the 106th United States Congress - Wikisource, the free online library。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-95834d5b999a](https://www.governing.com/politics/the-evolution-of-state-legislatures-throughout-u-s-history)；资料日期：2025-07-27；覆盖：The Evolution of State Legislatures Throughout U.S. History。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-2f1ad71a2836](https://nces.ed.gov/programs/digest/d02/tables/PDF/table150.pdf)；资料日期：未确定；覆盖：Ages for compulsory school attendance, special education services for students, policies for year-round schools and kindergarten programs, by state: 1997 and 20。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-77e8efc6b0c0](https://www2.census.gov/library/publications/decennial/2000/briefs/c2kbr-24.pdf)；资料日期：未确定；覆盖：Census 2000 Brief: Educational Attainment: 2000。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-c85ae524da2d](https://www.nejm.org/doi/full/10.1056/NEJMsa043266)；资料日期：2005-06-16；覆盖：Prevalence and Treatment of Mental Disorders, 1990 to 2003 | New England Journal of Medicine。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-6b07ceee3926](https://www.cdc.gov/nchs/data/databriefs/db309%5Ftable.pdf)；资料日期：未确定；覆盖：NCHS Data Brief, Number 309, June 2018。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-284fc740ba74](https://www.govinfo.gov/content/pkg/BUDGET-2002-TAB/pdf/BUDGET-2002-TAB-9-1.pdf)；资料日期：未确定；覆盖：Table 7.1—FEDERAL DEBT AT THE END OF YEAR: 1940–2006。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-fa124f37eca9](https://www.census.gov/data/datasets/2000/econ/local/public-use-datasets.html)；资料日期：未确定；覆盖：2000 State & Local Government Finance Historical Datasets and Tables。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-31ed8b358e54](https://www2.census.gov/ces/wp/2005/CES-WP-05-30.pdf)；资料日期：未确定；覆盖：THE ROLE OF RETAIL CHAINS: NATIONAL, REGIONAL, AND INDUSTRY RESULTS。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-79ef1f0f5bd3](https://www.bls.gov/careeroutlook/2001/Winter/art04.pdf)；资料日期：未确定；覆盖：industry employment projection。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-45b760eccb0c](https://www.nber.org/research/data/us-business-cycle-expansions-and-contractions)；资料日期：未确定；覆盖：US Business Cycle Expansions and Contractions | NBER。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-cc9c6a3925ca](https://www.nber.org/news/business-cycle-dating-committee-announcement-november-26-2001)；资料日期：2001-11-26；覆盖：Business Cycle Dating Committee Announcement November 26, 2001 | NBER。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-7dd633c05f55](https://edwardbellamyhouse.org/2022/10/31/talking-politics-edward-bellamy-populism-and-the-election-of-1892/)；资料日期：2022-11-01；覆盖：Talking Politics: Edward Bellamy, Populism, and the Election of 1892 | Edward Bellamy House。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-8e36bfc6f6d9](https://en.wikipedia.org/wiki/Socialist_Party_of_America)；资料日期：2026-10-23；覆盖：Socialist Party of America。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-3d52d1ad04a5](https://www.bls.gov/opub/ted/2000/feb/wk3/art03.htm)；资料日期：2000-02-16；覆盖：Changes in women&rsquo;s labor force participation in the 20th century : The Economics Daily : U.S. Bureau of Labor Statistics。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-a9ad7c1b6b2e](https://www.bls.gov/opub/ted/2001/apr/wk5/art04.htm)；资料日期：2001-05-03；覆盖：Employment of mothers with infants decreases again : The Economics Daily : U.S. Bureau of Labor Statistics。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-bac0139b5e24](https://www.supremecourt.ohio.gov/courts/judicial-system/supreme-court-of-ohio/justices-1803-to-present/florence-allen/)；资料日期：未确定；覆盖：Florence Ellinwood  Allen » Supreme Court of Ohio。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-c28be85ad83e](https://teachingamericanhistory.org/document/a-latina-judges-voice-2/)；资料日期：2001-10-26；覆盖：A Latina Judge’s Voice - Teaching American History。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-40c4fed02ec2](https://www.uscourts.gov/data-news/judiciary-news/2015/02/26/women-way-pavers-federal-judiciary)；资料日期：2015-02-26；覆盖：Women as 'Way Pavers' in the Federal Judiciary。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-08a7508cff65](https://billygrahamlibrary.org/blog-billy-grahams-radio-ministry/)；资料日期：2024-02-06；覆盖：Billy Graham's Radio Ministry。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-c0d941366f60](https://www.encyclopedia.com/environment/encyclopedias-almanacs-transcripts-and-maps/religious-broadcasting)；资料日期：未确定；覆盖：Religious Broadcasting | Encyclopedia.com。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-2e726b11af5d](https://news.gallup.com/poll/2974/america-remains-predominantly-christian.aspx)；资料日期：2000-04-21；覆盖：America Remains Predominantly Christian。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-6fb514f3fb7c](https://www.econlib.org/library/Enc/Advertising.html)；资料日期：2018-02-05；覆盖：Advertising - Econlib。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
- [ev-5ff93453c7d5](https://content.ibisworld.com/media/twpnf2mv/total-advertising-expenditure-total-advertising-expenditure-business-environment-profile-by-ibisworld.pdf)；资料日期：未确定；覆盖：Total advertising expenditure | Business Environment Profile by IBISWorld。限制：网页存档（exa-contents），只用于所引数字/事实；日期为页面发布或检索所示日期，未注明者为 null
