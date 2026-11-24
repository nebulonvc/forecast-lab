# america-full-v4：抽取质量修复 + 重抽 + 验证（美国反对美国）

时间均为 Asia/Shanghai（CST, UTC+8）。数字取自本目录的 summary / ledger / 结果文件。

## 结论先说

- **抽取已修好**：引文不匹配从旧跑的 482/723 条（67%）降到 **0**；整书重抽 **¥0.95**，所有 72 个 chunk 都通过。
- **人工 53 条的召回**：从旧 salvage 的 **14/53** 提升到 **42/53**（其中 37 条是 prediction，5 条因“第三方观点、作者未表态”被降为 unclear）。
- **验证没跑成**：Exa key 额度用完（HTTP 402 `NO_MORE_CREDITS`），第一条检索就被拒。旧版 verifier 遇到这种情况不会停，还继续调用 DeepSeek，所以 150 条全部是 partial、没有任何有效判定。我发现后手动终止了运行，并修了这个问题（见第 4 节）。
- **费用**：DeepSeek 约 **¥17.6（最多 ¥19.1）**，其中 ¥16.66 浪费在没有检索结果的验证上；Exa **$0**。没有超过 ¥50 的预算。

## 1. 引文不匹配的原因与修改

用新校验器重放 full-v3 已付费的 Flash 和 Pro 响应（723 条原始预测），分析结果如下：

| 原因 | 条数 |
|---|---:|
| 原文是硬换行排版（每行约 36 字，行首有缩进），模型抄录时去掉了换行和空格 | 383（flash 229 + pro 154） |
| 引文实际在 context_before/after 里（跨 chunk 边界），而旧校验只认 body | 96 |
| 真正改了字 / 转述 | 3 |
| 同时还有：页码行（`\x0c` + `    37`）、全半角标点、数字两侧空格（`1988 年`） | 包含在上面各项里 |

另一个放大问题的原因：旧校验里只要**一条**引文不对，就会**整个 chunk 作废**，所以 73 个 chunk 里只有 1 个通过，只能事后 salvage，而 salvage 只留下了恰好没有跨行的短句。

修改内容（`toolkit/prepare_book.py`）：

- `align_quote`：先做精确匹配，再做归一化匹配（NFKC、全半角和引号折叠、去掉空白和页码行），最后做保守的模糊匹配（ratio ≥ 0.9，长度比在 0.8–1.25 之间）。匹配结果**映射回原文的精确 span，并存成 quote**，模型原文另存为 `model_quote`，方法和 ratio 记在 `quote_alignment`。
- 搜索窗口是 context_before + body + context_after，偏移量换算为全书全局偏移，同一 span 重叠 ≥80% 时去重。
- 逐条校验 `validate_chunk_predictions`：坏的一条只进 `rejected_predictions.jsonl`，不连累整个 chunk。
- `time_text/condition_text` 为 null 时置为空串；reference 的 support 也按归一化规则比对，对不上的放进 `unsupported_reference_resolutions`，不再整批失败；缺少“[指代待确认：…]”标记时自动补一个可见标记。
- `pipeline.py check/apply` 的 expansion 校验同样改为容忍空白和全半角差异（只会更宽松，不影响已接受案例）。

用新校验器重放旧响应：723 条中精确匹配 285、归一化匹配 436、模糊匹配 2，**任何原因的拒绝都是 0**（另有 2 个响应 JSON 本身无法解析）。

## 2. 非预测排除

- **序言 / 致谢 / 后记**：`matter_spans()` 识别 序 / 前言 / 致谢 / 后记 / 跋 / 目录 等标题，把从书首到第一章标题（`一、不均匀的土地`）之间的部分整体排除，完全落在这段范围内的 chunk 不发送给模型（本书 txt-00001 被跳过）。“一、二千年的传统…”这类正文句子不会被误认成章节标题。可以用 `--include-front-matter` 关闭这项排除。
- **归属检查**：prompt 新增 `attribution`（author / author_endorsed / reported / rebutted）和 `future_oriented` 两个字段，并明确规定序言和致谢不算预测。处理规则是确定性的（`classify_prediction`）：
  - rebutted 排除
  - future_oriented=false 排除
  - reported 降为 unclear
  - 模型标为 author、但 span 落在“…”引号内的，降为 unclear
  - 缺少归属的降为 unclear
- 新增单测 `tests/test_extraction_quality.py`（16 个），`test_verify_prediction.py` 新增 2 个。**全部 177 个测试通过**（原来 159 个 + 18 个）。

## 3. 新抽取计数（deepseek-flash，workers=20）

| 项目 | full-v3（旧） | full-v4（新） |
|---|---:|---:|
| 通过的 chunk | 1/73（其余靠 salvage） | **72/72**（另有 1 个序言 chunk 被跳过） |
| 原始预测条数 | 723（Pro + Flash） | 352 |
| 引文失败 | 482 | **0** |
| 引文对齐方式 | 只接受精确匹配 | 精确 93 / 归一化 227 / 模糊 1 |
| 候选总数 | 203 | **321** |
| prediction | 161 | **262** |
| unclear | 42 | 59（其中 34 条是因第三方观点被降级） |
| 排除的非预测 | — | **9**（序言或致谢 1，非未来 8） |
| 重叠去重 | — | 22 |

抽查：
- 致谢“如若我对这些问题的分析，有助于中国社会的发展和进步…”被排除；“没有他（它）们，本书是不能写成的”所在的 chunk 直接没有发送。
- “由此可见，‘权力的集中化再也不起作用了’…”被标为 reported，降为 unclear，不进入验证。
- 模型从未输出过 rebutted。反驳类观点目前都是靠 reported 或引号规则降级的。

## 4. 与人工 53 条的召回（按 char span 重叠）

- 有重叠的 **42/53**，而且都是强重叠：
  - 37 条是 prediction
  - 5 条是 unclear（罗威、作者朋友、卡罗尔、IBM、布鲁姆，都是第三方转述）
- 漏掉 **11 条**：
  - 5 条作者本人的，例如“电脑多——社会通讯系统变得脆弱…”“门罗主义已难再现”“性解放恐怕已达到高峰”“联邦资助将影响教育政策…”“黑人问题雪球越滚越大”
  - 6 条第三方转述，例如尼克松、加尔布雷斯、图书馆负责人、受访教授
- 逐条对照见 `audit/recall-human53.json`。
- 取舍：按“说话者必须是作者”的口径，人工 53 条里有 11 条第三方预测本来就不在 prediction 里。如果想保留这些，可以把 reported 改成单独验证。

## 5. 验证：被 Exa 额度耗尽阻断

- 运行时间 23:39:37 开始，23:44:54 我手动终止。配置：flash、workers=20、max-rounds=2、adaptive 开启、Exa 每次 10 条、预算上限 ¥48.9。
- 第一条 Exa 请求返回 **HTTP 402 `NO_MORE_CREDITS`**（"exceeded your credits limit, top up at dashboard.exa.ai"）。此后所有检索都直接失败，但旧代码仍对每条预测继续调用 search_plan 和 assess，共 1454 次 LLM 调用、150 条 partial，**没有任何有效判定**。所以本轮的**五类分布、人工一致率和判定抽查都没有可报的数据**。
- 修复（`verify_prediction.py`）：
  - 检索服务出现致命错误（如 402）后，后续任务直接标为 not_started，不再调用 LLM
  - 任务进行中遇到这种错误，立即中止，不再进入 assess
  - 补了两个单测
- 结果文件不可用，作废：`output/verify-flash/`。重跑时请用新目录。

## 6. 费用

| 阶段 | DeepSeek ¥ | Exa $ |
|---|---:|---:|
| 抽取（72 次调用，缓存复用时不重复计费） | 0.95 | 0 |
| 验证（无检索，作废） | 16.66（另有终止时 20 个在途请求最多 ¥1.52，是否计费未知） | 0（1 次 402 失败请求） |
| **合计** | **≈¥17.6，最多 ¥19.1** | **$0** |

¥50 预算剩余约 ¥31。

## 7. 下一步需要用户决定

1. 给 Exa 充值，或换一个有额度的 key，再在新目录重跑验证。262 条按 flash 约 ¥0.28/条估算，大约 ¥70–75，超过剩余的 ¥31。可选方案：先验证与人工对应的 37 条再加一部分，或提高预算。
2. 是否把 reported（第三方）预测也纳入验证。

## 路径

- 报告：`cases/america-full-v4/REPORT-zh.md`
- 抽取：`cases/america-full-v4/output/txt_import/`（`summary.json`、`claims_proposals.jsonl`、`policy_report.json`、`rejected_predictions.jsonl`）；已导入 `cases/america-full-v4/data/claims.jsonl`（321 条）
- 召回：`cases/america-full-v4/audit/recall-human53.json`；验证 id 顺序：`audit/verify-ids.json`（先放与人工对应的 37 条）
- 代码：`toolkit/prepare_book.py`、`toolkit/pipeline.py`、`toolkit/verify_prediction.py`、`toolkit/tests/test_extraction_quality.py`、`toolkit/tests/test_verify_prediction.py`（均为本地改动，未提交、未推送）
