# 马汉《美国海权的利益：现在与未来》v5人工审读

- Worker：bot1-w19；只处理 mahan-interest-of-america-in-sea-power，未重新领书。
- 书籍：Alfred Thayer Mahan, The Interest of America in Sea Power, Present and Future；统一出版年1897；截止2026-11-15（Asia/Shanghai）。
- 原始TXT镜像：https://gutenberg.pglaf.org/cache/epub/15749/pg15749.txt
- SHA256：e8c98c42baf5c57285180e8a44da98dd6718bd245b9c8a9fac59e18fc9d6e9ca；368397 bytes，解码368293字符。与队列原书一致，未修订文本。
- toolkit：85e6da1dc0f185830a6ea9037d731fd39a27411e；与/workspace/forecast-batch-a/repo/toolkit逐文件相同。

## 实际方法

107块（3500/600）逐块全文审读，包含前后matter检查；每块均记录手写提案（可为空）。84条原始提案由原代码validate_chunk_predictions及claims_from_results确定性处理，导入79候选（67可核验、12 unclear），排除3 hypothetical、1 mechanism、1 normative；重叠去重0。没有按主题语义合并或在ASSESS中自行标duplicate。全部claims及claims_proposals的context为空。

67条各预先固定scope并做support/counter各一条检索，第一轮134次；18条进入同一自适应第二轮，共38次（其中#48四条，其余各两条），合计172次。URL均来自真实Exa返回；实际Exa contents抓取后，只用存档内可定位原句写ASSESS和语义复核。未调用DeepSeek。长网页多为前12000字符，不使用未存档后文或仅见于搜索摘要的内容。

124条evidence对应124个URL/存档；200条针对性evidence_notes。全部源文件sha256及引句连续性已经逐项核对。tasks/results是人工核验完成后按工具结构物化的审计记录，不冒充自动模型调用或其请求收据。

## 结果

最终67预测、58可判定：正确29、趋势符合0、部分符合19、错误10、暂无法判断9。strict=29/58=50.00%；weighted=(29+0.5×19)/58=66.38%；错误率=10/58=17.24%。9条未定为2条前提已改变、5条定义含混、2条缺决定性结果证据。12条unclear保留在候选数据，未纳入胜率。

## 报告与复现

- REPORT-manual-zh.md及output/manual-final/为中文展示与固定统计；canonical生成器/workspace/forecast-line-b/tools/manual_report.py，MD5 682248fa9f6c63e3492a559ccac12761。方法段如实记载Exa。
- audit/manual_review_2026-11-15.py为人工决定源；audit/semantic_review.json为逐项二次语义复核，未定保留相应unknown，不伪装证据充足。
- output/verify-v5-run/含tasks/results/summary/report、assess和真实检索日志；output/verify-final/为合并结果。
- 在同版toolkit下运行pipeline.py --case CASE check、report；apply评断的原始输入在output/verify-v5-run/assess.jsonl。
- 209单元测试及canonical quotes六项测试、check、源哈希、数字出处、密钥与全书重合检查的结果见audit/acceptance.json和audit/checks/。
- 全书TXT、分块plans、requests、checkpoints、Exa缓存和任何密钥均不在交付物。恢复原书可从上述镜像下载并先校验SHA；config另记录阅读库原路径。

## 质量边界

原作系多篇论文合集，相似主题反复出现，密度18.2条/十万英文字符高于8–10参考值；所有非重叠独立句均保留。主题敏感性在audit/theme-sensitivity.json与PR_BODY，仅作压力测试，不是新去重或正式改分。

THE ISTHMUS章标题June 1898与目录September 1893及全书1897不一致，疑排字问题；TXT未改，统一使用书籍出版年。#23数字从严，以注明海里的同起讫距离资料核对，未用另一份内部不自洽的英里概数拉宽容差。#36承认私产豁免与倡议该原则的区别、#53统一的隐含观察窗、#55缓冲区与租借地、#56文明与族群、#64最终基地、#67整岛与多米尼加的范围均须保留审慎解读。软件测试通过不代表这些历史语义争议自动消失。
