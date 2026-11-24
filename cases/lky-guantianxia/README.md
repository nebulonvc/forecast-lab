# 《李光耀观天下》案例

作者：李光耀。出版年代理：2013。证据截止日：2026-11-08。研究完成于2026-11-09。

|结果|条数|
|---|---:|
|正确|53|
|趋势符合|42|
|部分符合|31|
|错误|13|
|暂无法判断|167|

共326条候选，其中306条列为预测，非预测17条、重复3条单列。上述五类互不重复。记录有关联、口径是回顾性选择，不能称为306次独立实验或作者的最终准确率。

- [完整报告](output/report.md)：原文、解释、范围、证据、限制与思考方法。
- [逐条数据](output/claims.csv)：以 `display_verdict` 查看五类结论。
- [统计](output/summary.json)：以 `display_verdicts` 查看互斥计数。
- [二轮变化表](audit/round2/changes.csv)：243条待判断复核的过程与理由。
- [证据目录](data/evidence.jsonl)：216条证据及本地哈希。

第二轮新增78条证据，将原243条待判断中的76条改判。已发生的例子包括越南采购美国军用教练机；方向性例子包括日本老龄化及北美旧LNG进口设施增加出口能力。人民币汇率预测、可再生能源普遍否定等也保留反证。

第二轮事实复核：DeepSeek实际42次调用、峰值12并发、API阶段24.73秒，估计费用¥0.4417—¥0.8834，不是账单。抽取未重跑；模型原答复经过本地LLM复核，未声称独立人类审阅。

本次新增323条扩展观点，3条空白重复占位没有补造引文；21条仍有代指、对象或范围待确认，报告中明确标记。原文及既有评估均未改动。消歧使用已有短引文与语境，另将7处同书候选的补充语境及来源记录在 [本地复核记录](audit/expansions/local_review.json)。例如“他们离得太远”在中东章节指中国，不能套用附近美国的句子；“今后都会转为出口用途”指北美原为进口LNG建成的设施。

消歧另用了41次DeepSeek调用，峰值12并发，API阶段21.25秒，87,023 tokens，估计¥0.1965—¥0.3930。初次有18批共29条记录未通过引文/标记校验，原答复保留，经过本地LLM修正后才接受；共38条有本地修订，不是独立人类审阅，也未重新穷尽核验原书。详见 [消歧执行摘要](audit/expansions/summary.json)、[模型建议](audit/expansions/model_proposals.jsonl) 和 [接受结果](audit/expansions/accepted_expansions.jsonl)。

本案例沿用覆盖全书的候选清单，不声称重新穷尽抽取原书。短引文、页码、两处原文纠正和原始接收凭据已保留；原书及完整候选来源档案不在仓库内。`original-inputs/`、`case-origin/` 在历史字段里是来源标记，不是运行时依赖。

首次迁移只调整文件布局和路径，此后新增扩展观点及上述补充语境。原始、迁移后及补充后的数据哈希见 [迁移清单](audit/export_manifest.json)。`output/extract_decisions_final.jsonl` 是消歧前已接受的抽取，最新扩展另存于 audit/expansions/，完整当前记录以 data/claims.jsonl 为准。证据存档按内容哈希去重；全部证据可在本地重新校验。

从仓库根目录重建：

```bash
python toolkit/pipeline.py --case cases/lky-guantianxia check
python toolkit/pipeline.py --case cases/lky-guantianxia report
```

