# 单条预测的联网验证

`verify_prediction.py` 将一条预测作为独立任务：DeepSeek 规划查询和判断，Exa 搜索并取得正文，另一条独立LLM请求复核判断，必要时修正一次再复核；仍有缺口则程序自动返回未定及具体原因。批量模式共用同一个验证函数，任务完成即写入结果并发出 `task_finished` 事件。运行不需要聊天里的主代理逐条裁定。

默认8条并发。开场最多两轮搜索，每轮支持和反证各一次、每次最多10条结果，每轮最多读取8个来源。初判若仍是“暂无法判断”，模型必须写下决定性缺口，并自己再设计最多3轮补检索；每轮最多5次搜索，而且必须换策略（措辞、指标或代理、时间段、来源类型或语言）。某一轮已经能够给出判断就停止。跨轮重复的查询和URL不再抓取。整条最多18次LLM调用，其中仍只有一次结构或引用校验修正、一次语义修订。搜证前的判断口径固定传给后续阶段；后轮不同口径只保留为建议，不静默替换。复核还会检查这个口径是否符合原文，不能把固定口径当作正确性的证明。

## 运行

需要 Python 3.11+，仅使用标准库。密钥通过 `EXA_API_KEY`、`BOOKPRED_DEEPSEEK_API_KEY`（兼容 `DEEPSEEK_API_KEY`），或 `--exa-key-file`、`--key-file` 提供。不要把密钥放入案例文件、命令参数明文或Git仓库。

先准备明确的预测清单，不调用网络：

```sh
python3 toolkit/verify_prediction.py \
  --case cases/america-against-america \
  --claim-id txt-1c4066fc0c-000188277-000188300 \
  --claim-id txt-1c4066fc0c-000208790-000208831 \
  --prepare-only
```

两条实际试跑，分别限制LLM人民币预算与Exa美元预算：

```sh
python3 toolkit/verify_prediction.py \
  --case cases/america-against-america \
  --claim-id txt-1c4066fc0c-000188277-000188300 \
  --claim-id txt-1c4066fc0c-000208790-000208831 \
  --workers 2 --budget-cny 1 --exa-budget-usd 0.10 \
  --key-file "$HOME/.config/forecast-lab/deepseek.key" \
  --exa-key-file "$HOME/.config/forecast-lab/exa.key"
```

使用 `--ids-file path/to/ids.json` 可代替重复的 `--claim-id`，文件为预测ID字符串的JSON数组。必须显式选择ID，程序不会自动重跑全书。原文须已核验且已有接受的抽取，非预测和重复记录不进入任务。

日常运行也可用 `--unresolved` 冻结当前未定预测，或用 `--all-forecasts` 明确选择全部预测；两者与ID选择互斥。先带 `--prepare-only` 检查任务数，然后用相同配置去掉该参数运行。以下是运行当前未定集合的命令示例，10元和3美元为这次整批的停止上限，不是预估账单；本次开发没有执行这整批：

```sh
python3 toolkit/verify_prediction.py \
  --case cases/america-against-america --unresolved \
  --workers 8 --budget-cny 10 --exa-budget-usd 3 \
  --key-file "$HOME/.config/forecast-lab/deepseek.key" \
  --exa-key-file "$HOME/.config/forecast-lab/exa.key" \
  --output-dir cases/america-against-america/output/search_verify/batch-01
```

默认运行目录是案例下的 `output/search_verify/`，已加入gitignore。新一轮使用新的 `--output-dir`。同一目录只允许一个命令行进程，模型、范围、预算或任务配置变化须新建目录。调用函数的程序应自行持有跨进程目录锁。

## 输出

|文件|内容|
|---|---|
|`manifest.json`、`tasks.jsonl`|运行配置和冻结输入|
|`jobs/<id-hash>/input.json`|单条原文、抽取、旧证据、版本和输入哈希|
|`jobs/<id-hash>/progress.json`|已完成步骤、查询、来源状态和错误|
|`jobs/<id-hash>/result.json`、`receipt.json`|单条完整结果及内容校验凭据|
|`jobs/<id-hash>/*.txt`|Exa返回的正文提取件；不是完整原始网页|
|`results.jsonl`|按输入顺序汇总，任务逐条完成时刷新|
|`report.md`|便于阅读的运行状态、五类建议与缺口表|
|`summary.json`|技术状态、研究未定、供应商用量及费用估计分列|
|`llm/`、`exa/`|请求、响应、哈希缓存和各供应商账本|

函数接口为 `run_job(packet, run_dir, llm, exa)`，批量接口为 `run_jobs(packets, run_dir, llm, exa, workers=8, on_complete=callback)`。批量按完成次序调用callback，最终列表按输入顺序返回。

每条结果包含原文身份、输入哈希、`task_state`、`assessment`、`raw_assessment`、`evidence_candidates`、双向查询、逐URL状态（`source_statuses`）、单页抓取失败记录（`source_errors`）、任务级错误（`errors`）和具体缺口。`assessment`沿用现有字段，另加逐来源原句、关系及剩余缺口；趋势仍按现有兼容字段显示为第五类。`draft_history`、`semantic_reviews`和`revision_count`保留初判、复核及修正过程；`round_history`记录每一轮查询、策略为何改变、补检索前的缺口和该轮判断后的缺口。`autonomous_decision=true`表示程序已经完成自动判断流程，`semantic_validation`区分接受或因具体问题自动未定。

## 程序内的判断复核

复核逐项检查对象对应、真实条件、时间对应、证据支持、反证处理和结论逻辑。全部通过才接受；现有资料能修正的问题允许一次修改，再由新的请求复核；缺少关键资料或修正后仍不通过，则自动转为“暂无法判断”，返回具体问题。没有要求主代理或用户逐条选择结果，也不允许无限循环直到模型同意。

复核意见须引用本任务原文或来源；指出草稿自身的逻辑或时间矛盾时可引用草稿，但标明其来源，不能冒充事实证据。所有复核建议同样按结构、来源范围和引文匹配校验。未能产生有效输出时返回明确的部分执行或失败状态，不伪称得到判断。

这使用同一模型的不同请求和不同角色提示词，并非独立人类或独立模型验证；双方仍可能犯相同错误。独立抽查可以评估系统质量，但不是每次任务运行的必要步骤。

## 判断与运行状态

`completed`表示本次研究流程产生了有效建议，建议仍可为“暂无法判断”。`partial`表示有阶段材料但流程或验证存在错误；`failed`表示任务失败；预算不足且尚未产生请求收据的任务可为`not_started`。返回码0表示所选任务均完成，2表示存在失败或部分执行。任何一种状态都不代表事实已经获证实。单个选中网页抓取失败（`page_text_unavailable`）会保留在`source_statuses`和`source_errors`中，不会仅因此把已正常完成评估和复核的任务降级为`partial`；只有当所有选中网页均未取回可用正文（`all_selected_pages_unavailable`）或发生任务级错误时，才会保持`partial`。

模型只能选择搜索实际返回的URL，引用只允许本条实际提供的材料，逐条引句必须能对应提供给模型的正文连续片段。PDF换行造成的空白差异仅在唯一可对齐时恢复为真实正文，同时保留模型原句；字词、标点、数字差异及多处歧义均拒绝。明确未来日期、越界引用或伪造引句仍拒绝。原始模型响应仍可审阅。

来源发表精度、截止前可得性与事实观察期分开：保留年/月/日精度，不补造日期；发表范围上界在截止日前，或本程序在截止日前取得的Exa正文，都可证明该版本当时可得。后者不证明发表时间、观察时期或事实真伪。发表日期缺失、日期范围跨过截止日、或模型自填日期未被元数据证实，只保留警告，不再把已经形成并被复核接受的判断改成未定。发表范围整体晚于截止日的材料仍然拒绝。历史截止日之后的抓取不能反推历史可得性。

搜证、初判、复核、修订使用同一 `decision_policy.py` 口径，允许透明且对应原命题的回顾性指标，同时检查过度断言和无依据的未定。正式复核只接收原文、初判与来源事实，不再提前接收程序生成的“应为未定”判决。`decision_trace` 保留每轮初判、机械候选、复核及警告；`context_coverage`保留每份来源实际提供给模型的字节数与截断状态。

搜索日期过滤只是辅助，发表日期元数据也可能不准确；模型须说明真实观察时段。程序不能通过关键词检查证明事实、因果或日期语义，语义检查由任务内的独立复核请求完成；检查通过仍不保证判断正确。

Exa新取得材料的 `verified=false`是旧证据表的登记状态，可以参与自动判断，不会因其为false单独判未知；此次运行不修改旧证据表。复用的旧证据保留既有登记状态并检查本地存档哈希。来源超长时保留归档。判断和复核不再把固定预算平均分给每个来源：统计类页面和靠近搜索摘要命中处的段落优先，其余来源仍保留一段可见正文，并写明截断。规划检索使用较小的正文预算。因此没有读到的后文仍可能包含重要反证。

联网验证器的总请求上限为180,000字节，为原文、判断稿、复核意见和引用编号预留空间；判断阶段的证据正文预算为64,000字节，放不下时会缩小正文而不是丢弃原文。其他批处理继续使用48,000字节上限。费用预留仍按实际完整请求计算，超出总上限则明确保留部分执行，不丢弃原文或反证来强行通过。[供应商模型元数据](https://api-docs.deepseek.com/api/list-models/)列出的上下文窗口为1,048,576 tokens，此处更小的字节限制是本程序的成本与体积约束。

“暂无法判断”只作为补检索之后的最后选择，并且必须点名一个决定性缺口。允许写明边界的回顾性代理；条件预测在前提未知时仍评价已经观察到的后果或分项，使用部分符合或趋势符合。复核不会仅因代理不完美、缺少从出版年起的连续序列或日期元数据缺失而拒绝。拒绝仍限于对象换了、证据与结论矛盾，或引用不能支持结论。五类含义不变，引文仍须能对上实际提供的正文。

抽取版本 v5 里，`claim_type` 不是 forecast、或 `resolvable` 为 false 的记录，不能得到“正确”。核查还会直接检查引文：比喻、格言、政策建议、必然仪式、早于出版年的历史、没有未来结果的机制、过去反事实和假设战争情景，都不能判为正确。写出变化方向但没有写时间的预测仍可评分：窗口是出版年到截止日（`horizon_source=implicit_publication_to_cutoff`）。该窗口内主要方向已经发生则判正确，方向相反则判错误；不要因为作者没写日期就改成暂无法判断或趋势符合。这不改写已经接受的 v4 判定。

## 预算、失败与恢复

两家供应商分币种记账，不合并成未经说明的人民币总价。费用上限通过请求前预留控制，供应商价格变化或回报异常仍需核查，账本估计不是正式账单。失败、无用量或无费用回报保留保守预留，不能记成免费。

Exa普通搜索使用进程共享3 QPS限制。明确429最多重试一次；尊重Retry-After，等待超过30秒则标为待处理而不长时间阻塞。401、403及402停止该供应商后续请求。网络超时、响应丢失和不完整响应不自动重发；保留收据及未知状态，先核对再决定后续运行。

完成任务恢复时检查输入、提示词规则、结果与来源哈希；有不一致则拒绝恢复。中间LLM响应缓存也检查原始响应哈希及其与解析JSON的一致性；没有完整性凭据的旧缓存标为`legacy_unverified`并拒绝自动复用。未完成任务使用已保存的成功响应，已尝试但没有可靠响应的请求保持未决，防止重复计费。已产生终态结果的失败任务不会因重启自动重试；审阅原因后再决定新的运行。

新程序直接生成本次独立运行报告，自动判断到此完成；依照本次授权范围，不覆盖 `data/claims.jsonl`、`data/evidence.jsonl` 或已发布的历史报告。要更新旧案例时另用[现有导入流程](METHOD.md)，保留新旧差异。上传时不要包含默认忽略的原始任务目录，尤其是完整上下文和密钥。

## 验证与供应商依据

本地测试使用模拟API，覆盖真实并发、预算竞争、失败隔离、原文不变、缓存和来源篡改、未知日期、截止日及引用范围。真实试跑的结果另见[验收记录](SEARCH_VERIFIER_VERIFICATION.md)，不得用模拟测试代替真实API或语义验收。

```sh
python3 -m unittest discover -s toolkit/tests -v
```

截至2026-11-09，接口和费用依据为[Exa Search](https://exa.ai/docs/reference/search)、[Contents](https://exa.ai/docs/reference/get-contents)、[价格](https://exa.ai/docs/admin/pricing)、[团队限流](https://exa.ai/docs/admin/billing)与[DeepSeek价格](https://api-docs.deepseek.com/zh-cn/quick_start/pricing/)。Exa的`costDollars`是供应商回报的费用估计，DeepSeek按回报token和公开价格估计；缺失信息单列保留。
