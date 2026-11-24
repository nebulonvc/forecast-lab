# 审计与复现说明

## 文本来源与版本

- 书名：Security in an Interconnected World: A Strategic Vision for Defence Policy；作者 Ernst Hirsch Ballin、Huub Dijstelbloem、Peter de Goede；英文版出版日 2020-04-07。
- 实际全文来源：UvA-DARE 公开存储的出版社终版 PDF，https://pure.uva.nl/ws/files/59742604/10.1007_978_3_030_37606_2.pdf 。189页（含大学封面），4,420,744 bytes。
- PDF sha256：`a95ef7aae0dbb7a440f48af40e4af706aeff4d026536c0b39711769597de4abd`。
- `pdftotext -enc UTF-8` 生成 TXT，535,677 字符；TXT sha256：`9b0f6a50cb562fc9f12bbe9129d9215f6e2cae3bdf7b3b3c59cb3aa5af77e668`。
- 队列私有PDF为5,661,333 bytes，sha256 `212cc907666a6593a000b3014fb943a255031e4827b77c5f5f8662021dd00cd2`；未取得该字节版本，不声称与公开镜像字节一致。没有将任何全书PDF或TXT打入case/bundle。
- 抽取严格以2020版出版后核验，尽管书籍承袭2017年的报告。原TXT保存在worker私有books/work目录供本地引文复验，不进入交付。

## 实际方法与统计

156块（3500/600）全部通读，61项原始抽取；工具原历史筛选排除5项、重叠去重1项，55 candidates、48 resolvable；7条第三方转述降为unclear不评分。去重只按原claims_from_results重叠规则，不作主题合并。所有claims及备份context均为空。

toolkit使用 `/workspace/forecast-batch-a/repo` 的 `85e6da1dc0f185830a6ea9037d731fd39a27411e`，32个.py文件逐个哈希与本地副本一致。canonical报告实际调用 `/workspace/forecast-line-b/tools/manual_report.py`，md5 `682248fa9f6c63e3492a559ccac12761`。原文引文连续精确匹配TXT，指代依赖使用最短可用连续扩展引文，不借context补义。

实际研究为Exa search + contents存档，并非DeepSeek或其他研究API：48项初轮96查询，11项改策略补查22查询，所有6项未定都有第二轮。每项至多8个来源，跨条复用已检索来源在SELECT中明示；113段证据绑定引句与77个实际网页/文件JSON原文逐段一致，全部URL可追溯到真实检索结果。SEMANTIC REVIEW由同一助手完成，不声称独立人类/另一模型评审。

最终48预测、42 decidable；正确22、趋势符合0、部分符合16、错误4、暂无法判断6。

- strict=22/42=52.380952%。
- weighted=(22+0×0.75+16×0.5)/42=71.428571%。
- 错误率=4/42=9.523810%。
- evidence 77条，source JSON 77个，sha256全部实际复核。

apply assess接收55条；check为 `OK: 55 claims; 77 verified evidence records`；report和canonical manual report均成功。209单元测试与6项manual_report quotes测试通过。所有55原书引句、113源引句、数字理由与存档、证据SHA、URL检索溯源、U二轮记录均另行检查通过。

## 质量风险（必须随包阅读）

1. 私有队列PDF未取得，使用公开出版社终版镜像，存在源字节/分页版本差异；不把2017–2020的已发生事件当作2020版命中。
2. 原代码历史屏幕排除5项，其中4项仍含明显未来部分（战略概念回顾、轮驻延续、技术脆弱性跨页图注、北约协议后续经费）；原始提案及排除原因完整保留，未篡改确定性筛选或塞回已接受claims。它们构成已知漏评风险。此前续跑笔记中的“4 historical/2 overlap”是未定稿误计，最终以5 historical/1 overlap为准。
3. 同主题独立句重复可能放大条目级胜率。正式不主题去重；仅作敏感性：近似重述组各取最早句，39预测/33可判、正15/部14/错4/未6，strict45.45%、weighted66.67%、错12.12%；更宽主题组36预测/30可判、正13/部13/错4/未6，strict43.33%、weighted65.00%、错13.33%。两组趋势均0，具体分组见audit/sensitivity.json。
4. 出版年油价低基期、定性重要性和因果归属、复合国家组/多分项范围以及动态页日期元数据存在解释风险；只按实际存档支持的对象、地域、指标和时限判定，不以未来模型、新计划、累计个案量替代已观察兑现或频率。大西洋2030增产份额尚未到期；气候迁移的国内/跨境分母与贸易/战争频率不可混用。6项未定缺口均明示。
5. 部分网页/PDF经Exa截断，日期/可访问性非阻断警告原样保留（见audit/validation_warnings.json），不声称HTTP逐站独立核实。未定不是空证据，证据均有真实可复验原文。
6. 安全扫描对指定Exa密钥作内部精确匹配及常见API/私钥模式检查，零命中、不展示配置。全文重合采用300字符字段感知检查：只豁免经TXT验证的quote/support_quote/model_quote必要引句，最长954个规范化字符；非引文字段重合为零，包内无全书。原始粗扫会命中合法引文和URL中task-/risk-字样，不将其误报成密钥或虚报“原始重合零”。

本地续跑、来源与测试日志见audit；抽取的全文分块请求、checkpoint载荷以及未使用抓取源都已移出case。只生成本地提交准备包，没有commit/push/开PR，也没有修改其他已接受数据。
