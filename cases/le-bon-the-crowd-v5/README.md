# Gustave Le Bon《乌合之众》— v5 完整人工模型替换

1895原著；观察截止2026-11-15。完整阅读104/104块，55候选全部保留，49可核验预测与6原unclear。

- 原书：Project Gutenberg 445；https://www.gutenberg.org/ebooks/445.txt.utf-8
- TXT SHA256：342ce2be9c9cc88ca2975983b182ff634ebf7049c44186327af81317db7e7da1（与queue一致）
- data/claims.jsonl：55行，context全部空；data/evidence.jsonl：109条，data/sources/：109份公开正文存档。
- output/verify-v5-run/assess.jsonl保留55条完整判定；audit/semantic-review.jsonl逐项六维审查。
- REPORT-manual-zh.md为未修改canonical工具生成；output/summary.json是全55候选统计，manual-final为49可核验子集。
- 104块全文、请求/响应、checkpoints及Exa原缓存仅存箱上work/private-extraction-artifacts，不随case或bundle分发。
- 143查询：98首轮、40二轮、5共享自适应；共享主题/claim映射详audit/research_method.json。没有额外语义去重。

判分：正确9，趋势0，部分16，错误9，未定15；decidable34；strict=9/34，weighted=(9+16*0.5)/34，error=9/34。

工具：85e6da1无.git快照，与来源38个冻结toolkit文件逐字一致；不能声称已通过git log独立确认。publication_date的01-01只代表已知出版年。
