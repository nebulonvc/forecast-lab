# Doctorow《魔法王国的落魄》v5手工模型替代案例

2003原版；截止2026-11-15（Asia/Shanghai）。全文91块，102原始候选，原规则保留101个reported/unclear，resolvable=0。最终预测0，decidable0；各准确率均N/A。101条并非未定预测。

见REPORT-manual-zh.md、audit/BOUNDARY-zh.md了解严格作者归属的零分母边界及反证。3条evidence/3个存档仅支持边界审查，不是技术结果证据。未因小说体裁或无日期排除，不做额外语义去重。

- 原代码85e6da1；38个toolkit文件Git blob SHA均经GitHub核对。
- data/claims.jsonl与data/evidence.jsonl为主数据，context全部为空。
- output/txt_import为原模型替代抽取/原代码后处理产物，全文plan与请求不打包。
- output/verify-v5-run/assess.jsonl覆盖101条；resolvable=0故tasks为空，另有一轮WebSearch正反2查询的归属边界研究。实际WebFetch阅读+urllib公开HTTPS存档，未用Exa或DeepSeek。
- 原pipeline apply/check/report执行完；canonical报告经audit/render_report.py如实替换零分母固定模板。209+6测试通过。
- SOURCE TXT不在此case；工作目录books/book.txt的SHA为d2d6e549b1c5f62173eebd97e1f2f2259199d1c3fde2abca7243038757b42a93。
- 本地来源从GitHub规范TXT连接器获取，连接器省略UTF-8 BOM，恢复后字节数301963且队列SHA精确匹配；未改正文。
