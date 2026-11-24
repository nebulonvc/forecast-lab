## 方法说明

实际方法：对队列SHA256精确匹配的原生TXT按原代码3500/600分块，**91/91块全部顺序通读**，包括两套许可证、2003/2004说明、正文、致谢与RDF元数据；无关键词筛选，无双栏或表格需恢复。按DISCOVER_PROMPT_V5逐块手写JSON，由未修改的85e6da1原代码验证、归属筛选、重叠处理并导入。102条原始候选的quote全部精确匹配；1条rebutted由原代码排除，0条重叠去重，保留101条unclear。所有context已清空。

**本例resolvable=0。** 101条均是明确具名叙述者/角色或推荐人的表述，原代码以`third_party_view_not_endorsed`自动降为unclear；未因无日期、体裁或语义重复排除。为防将“小说没有作者预测”当作预设，保留了死亡治愈、声望、脑机接口、远程机器人、无期限社会方向、极远宇宙期限等具体候选，并逐条完成归属ASSESS和六维semantic review。99条角色场景的作者背书证据为unknown，2条封面推荐人归属明确；均不进入现实真假判分。这里的101项nonforecast是严格作者归属口径，不是101项错误或未定预测。

实际辅助研究为**1轮WebSearch正反各1查询**，SELECT选择3个搜索返回URL，WebFetch阅读后用urllib公开HTTPS抓取、存档并记sha256；未调用Exa或DeepSeek，无第3轮。3条evidence仅支持作品/归属边界，不是技术结果证据。零resolvable意味着逐预测PLAN任务数为0；不能据此声称逐条做了101项技术结果检索。原`pipeline.py apply assess → check → report`已执行；后由canonical manual_report.py生成，再对该报告中不适用于零分母案例的固定Exa/人工挑选模板句作如实的本案例修正，共享工具未改。

归属边界：2010年访谈（2015重刊）中Doctorow称自己“predict the present”，也把Free Energy称为思想实验的前提；同一访谈又承认自己预期过某些Disney设施会继续存在，且讨论Whuffie可能呈幂律分布。两面均保留，不能用一句“从不预测”就认定其全部设定无预测意味；也不能把2010新断言回填为2003原书预测。零分母只是在本次原严格归属规则下的结论，建议协调者复核后归档，不表示小说没有前瞻性。

