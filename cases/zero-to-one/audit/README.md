# 实验与复核审计

本目录支持检查本次程序实验及结论变化，不声明研究已经完成。

- 当前规范数据：[候选与评估](../data/claims.jsonl)、[证据表](../data/evidence.jsonl)、[统计](../output/summary.json)。
- [复核报告](../output/reassessment/复核报告.md)、[24条修改的完整old/new](../output/reassessment/changes.jsonl)、[本轮213条评估](../output/reassessment/assessments.jsonl)。
- 原122条独立审计：[逐条审计](../../../.context/zero-review/audit.jsonl)、[审计摘要](../../../.context/zero-review/findings.md)、[最终质检](../../../.context/zero-review/final-review.md)。审计分类为LLM建议，不是人类金标准。
- [原生抽取覆盖](../output/native-extract/coverage.json)、[初轮原生复核](../output/native-review/summary.json)保留历史过程；当前结论以二轮评估为准。
- [初轮速度/费用实验](../output/experiment.json)保留全部失败、中断与缓存差异。原始运行路径为历史本地路径，GitHub副本按下表索引。

|实验名称|GitHub审计目录|请求/响应数|
|---|---|---:|
|首次整书抽取|[production_extract](provider-runs/production_extract)|27/27|
|预算受限并发对照|[budget_limited_comparison](provider-runs/budget_limited_comparison)|10/10|
|20并发抽取对照|[comparison_20](provider-runs/comparison_20)|27/27|
|预算受限评估|[budget_limited_assessment](provider-runs/budget_limited_assessment)|88/88|
|共享上下文评估|[optimized_assessment](provider-runs/optimized_assessment)|94/94|

[复制清单](provider-runs/manifest.json)记录原始位置、大小和SHA256；共246对原始请求/响应，未改写模型响应。每个目录保存原账本、manifest和summary；首次抽取同时保留原文修复记录和本地接受说明。结构拒绝仍是拒绝，不能把后续本地修复算成API直接成功。

模板、解析缓存、锁文件和检查点未重复提交；完整原始运行目录仍保留在本地。现有44条证据的全部`local_archive`按原相对路径提交，含未绑定资料；下载失败后保存的工具摘录与下载日志也保留。哈希只验证存档完整性，不证明资料内容或研究结论正确。

`output/reassessment/before_*`是二轮前的历史快照，保留当时的统计字段和措辞，不代表当前结论；`before_README.md`里的链接仍相对于它原来的案例根目录。案例报告可从当前规范数据重建，不依赖本机绝对路径、密钥或调用模型；重新做原文抽取仍需书籍输入。

本次后续工作见[改进计划](../改进计划.md)。程序检查和来源完整性通过不代表102条剩余判断已经完成搜证。
