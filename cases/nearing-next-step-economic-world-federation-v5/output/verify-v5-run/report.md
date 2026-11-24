# 人工替换核验模型的运行报告

35个原prepare-only任务已完成；全部经历PLAN、SELECT、ASSESS与语义复核。100次Exa查询（首轮70/适应轮30），无失败；81页实际contents存档，69条正式证据，102个逐字引句注记。

已用未改toolkit的validate_stage检验所有PLAN/SELECT/ASSESS，inspect_assessment核对原文与日期，再用semantic_review.validate_review检验六字段及具体缺口。所有U保留unknown项，而非自动全pass。详见audit/semantic_review.json。

原prepare-only清单中的deepseek-flash只是CLI默认模型名，没有模型调用；实际抽取与核验均由助手审读，所有网络请求为Exa公开检索/contents。
