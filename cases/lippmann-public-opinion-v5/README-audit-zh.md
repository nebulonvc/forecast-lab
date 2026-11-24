# 《公众舆论》审计与复现说明

## 文本来源与版本

- ID：`lippmann-public-opinion`；worker：`bot1-w17-next`；Walter Lippmann《公众舆论》（Public Opinion），1922年出版；核验截止日2026-11-15（Asia/Shanghai）。
- 原始TXT：https://www.gutenberg.org/ebooks/6456.txt.utf-8 ，645,335 bytes、645,231字符，保留CRLF；与队列字节及SHA256完全一致，无PDF替代或文本清洗。
- TXT SHA256：`57d387a66be0964d71934d5d648c44762b2452f302357832e6862e9aa5ad3288`。
- TXT仅在独立worker目录books；case和tar无全书、分块正文、请求或checkpoint。旧Hirsch Ballin交付不改，新书独立子目录。

## 实际方法与统计

按原3500/600分块，186/186块全文通读，47个原始提案。原claims_from_results历史筛选排除1条、重叠去重6条，得到40 candidates/38 resolvable，2条reported/unclear保留但不计作者成绩。38条均完成PLAN→SELECT→ASSESS→SEMANTIC REVIEW；其中16条为机制、规范方案或制度思想实验，最终22条预测。没有额外主题去重或语义duplicate。所有claims及候选备份context清空；指代通过原书逐字连续扩引处理。

实际联网工具是Exa search与contents存档抓取，无DeepSeek。38条初轮76个正反查询；9条改变策略再查18个查询，共94查询，7个最终未定均有第二轮。最多3个选择来源/条，跨条复用在SELECT明示。51条evidence对应51个真实公开来源JSON，sha256全部复核；72段绑定源引句逐字复验。语义复核由同一助手完成，不冒称独立人类/另一模型审查。

toolkit为`/workspace/forecast-batch-a/repo`的`85e6da1dc0f185830a6ea9037d731fd39a27411e`，32个Python文件逐个哈希与本地副本相同；不改共享工具。报告实际调用canonical `/workspace/forecast-line-b/tools/manual_report.py`，MD5 `682248fa9f6c63e3492a559ccac12761`，方法说明如实写Exa与存档。

| 指标 | 结果 |
|---|---:|
| 最终预测 / decidable | 22 / 15 |
| 正确 / 趋势符合 / 部分符合 / 错误 / 未定 | 4 / 0 / 11 / 0 / 7 |
| strict | 4/15 = 26.666667% |
| weighted | (4 + 0×0.75 + 11×0.5)/15 = 63.333333% |
| 错误率 | 0/15 = 0% |
| evidence / sources | 51 / 51 |

apply assess接收40条；check为`OK: 40 claims; 51 verified evidence records`；pipeline report与canonical manual_report均成功。209项单元测试及6项manual_report quotes测试通过。原书引文offset/精确连续匹配、全部来源SHA256、源引句、检索URL溯源、理由数字及U二轮记录均检查通过。

## 质量风险（必须随包阅读）

- Gutenberg TXT与队列sha256一致，CRLF原样保留；早期续跑曾按通用read_text换行归一化生成草稿，已废止。最终重新按原字节解码生成186块，逐块通读并精确校验47个原始引句；只打包哈希/条目覆盖证据，不打包全文、分块正文和请求。
- 原代码排除1条historical、去除6个重叠项，40 candidates/38 resolvable；2个reported/unclear不评分。历史屏幕排除项涉及科学与行动互惠的未来句，但引文包含旧脚注而触发历史筛选；原提案和原因保留，未改过滤或暗加分母。38项中16项经体裁复核为机制、规范方案或工团制度思想实验，因此最终仅22项预测；本书主要是认识论、历史分析和制度设计，密度低于典型预测书，仍有体裁边界与漏收风险，不为密度凑数。
- 正式只按claims_from_results重叠规则去重，未加主题或语义duplicate。同类独立句的相关性会放大条目级胜率：相关近义组各留最早句为20预测/13可判，正3/趋0/部10/错0/未7，strict23.08%、weighted61.54%；更宽主题组各留最早句为13预测/6可判，正1/趋0/部5/错0/未7，strict16.67%、weighted58.33%。两组错误率均0，但不是独立抽样的准确率；分组见audit/sensitivity.json。
- 全称终局否定#20/#22一律未定，不把当前不足当作永远不可能；#3的地区长期仇恨效应不替代个体终身视觉记忆；#34的soon不被拉长至今天补命中；#27的管理层独立不替代董事会和股东独立。
- #10/#32/#35采用实际真假辨别或偏见分项的实验材料，仅判部分，不把分享意向直接改成信念准确性；#31的去极化不等于真理或整体自治成功。#24/#36虽主结果符合，专业权力的定性范围和资料搜集的多种动机仍有解释空间。
- 研究实际为Exa search/contents，共94个正反查询；9项改变策略再查，7个最终未定都完成二轮。每项最多3个选择来源，跨条复用在SELECT明示；51个公开来源存档与51条evidence逐一sha256核验。部分正文截断、发布元数据缺失，非阻断警告保留；不声称HTTP逐站独立验证，也不用截断的LA Times来源评分。
- 语义复核由同一助手完成，不声称独立人类或另一模型验收。原文引用均逐字连续；context一律空。toolkit来自85e6da1，manual_report实际使用canonical版，md5 682248fa9f6c63e3492a559ccac12761。
## 打包与安全

采用300字符、解码字段感知的原书重合检查；仅豁免经原始TXT复验的quote/support_quote/model_quote必要引文，最长1279个规范化字符。CSV先按真实字段解析，不忽略其内容。非引文字段原书长重合、非空context、指定Exa密钥内部精确匹配及常见API/私钥模式均零命中，不展示配置或密钥值。

初次安全扫描定位到40个候选context、9个搜索highlight含原书长片段，以及CSV转义引句的原始粗扫命中：前两类按统一要求清空/移出交付，原始记录和哈希留在私有work，保留查询、URL、题名与日期；CSV用字段解析后核对真实引句。评分来源正文及SHA均未改，处理记录见audit/payload-minimization.json。原Exa响应缓存不打包，ledger及检索/选择/证据审计仍保留。

航空来源深取成功后，临时/dev/fd路径的映射保存发生本地参数错误；实际存档已完整写出，使用现存首轮URL映射和搜索记录完成核验，非API抓取失败，未重抓或伪造来源（见audit/operational_notes.md）。

只准备本地交付，未commit/push/创建PR，未修改其他已接受数据。tar仅含cases/lippmann-public-opinion-v5；manifest和SHA256附后。全部验收后写队列done并保留锁。
