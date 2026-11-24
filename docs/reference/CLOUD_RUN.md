# 云端整书验证

GitHub Actions 在临时 Ubuntu runner 上调用现有 CLI，按预测并发访问 DeepSeek 和 Exa。这里只验证案例中已接受的全部预测，不重新抽取原书。任务内的模型请求负责搜证、初判、复核和一次修正，主代理不参与逐条判断。

仓库管理员只需配置一次 Secrets。以下命令从本地文件读取，不把密钥写入命令或 Git：

```sh
gh secret set BOOKPRED_DEEPSEEK_API_KEY --repo nebulonvc/forecast-lab < "$HOME/.config/forecast-lab/deepseek.key"
gh secret set EXA_API_KEY --repo nebulonvc/forecast-lab < "$HOME/.config/forecast-lab/exa.key"
```

启动一本书：

```sh
gh workflow run verify-book.yml --repo nebulonvc/forecast-lab --ref main \
  -f case=america-against-america -f workers=8 \
  -f budget_cny=20 -f exa_budget_usd=10
gh run list --repo nebulonvc/forecast-lab --workflow verify-book.yml --limit 5
```

`budget_cny` 和 `exa_budget_usd` 是停止上限，费用保留原币种，不能当作正式账单。每条先做最多两轮双向检索；若初判仍是暂无法判断，再由模型自己做最多三轮补检索，每轮最多五次搜索、每次最多十条结果。整条最多十八次 LLM 请求。工作流最长 180 分钟，同一案例运行排队而不互相取消。研究未定保留具体原因；部分执行或失败使作业返回非零，不会改成成功。

运行先冻结任务清单，再自动执行。结束后，无论存在多少失败，都会尝试上传 `book-verification-<run_id>` 产物。产物保留 30 天，包括机器生成的报告、全部结果、逐条引用/反证/复核历史、状态与费用汇总、输入哈希及运行提交信息。导出排除来源全文、API 请求/响应正文；再扫描已配置密钥，发现泄漏则拒绝整个导出。原始来源哈希保留，但正文不随产物交付，因此这个精简产物不是完整重放缓存。

下载结果（替换运行 ID）：

```sh
gh run download RUN_ID --repo nebulonvc/forecast-lab \
  -n book-verification-RUN_ID -D /absolute/path/to/results
```

工作流没有自动重试整批。GitHub 的 Re-run 会因 `run_attempt` 大于 1 而停止，避免在临时 runner 上悄悄重复付费。只有程序故障时才检查技术日志并修复通用程序；新的付费批次使用一次新的 dispatch，并保留旧批次。强制取消、平台宕机或总时限耗尽可能来不及导出最终产物，应保留运行日志并标为未知执行，不能视作零费用。

技术失败的定向恢复可加 `-f retry_run_id=RUN_ID`。程序下载该批次产物，核对清单、结果与费用文件哈希，只选 `task_state != completed` 的条目；研究结论为未定但技术完成的任务不重跑。预算强制使用上一批上限减去已经承诺的费用（含未知预留），忽略 dispatch 中新的预算输入。恢复是新的独立研究尝试，并非从已省略的原始缓存续接；两轮费用和失败记录都保留。

模型响应未通过结构或引用校验时，任务内最多追加一次 API 修正；不重试超时或未知发送状态。修正仍要通过原校验与语义复核，不能降低引文规则或补造事实。每条最多十八次 LLM 请求，其中结构或引用修正只有一次。错误码、原请求哈希和修正次数随结果导出。补检索轮次、策略变化和缺口写在每条结果的 `round_history`。

语义复核还可选择程序提供的原句编号（`quote_ref`），由程序还原逐字引文和来源，避免模型复制时改写。编号只简化引用方式，相关性仍由模型判断，原来的来源边界和草稿引用限制继续生效；编号无效、冲突或越界仍拒绝。

诊断“全未定”可加 `-f review_audit=true`（本地CLI为`--review-audit`）。程序按预测ID哈希固定选取最多12条，用同一份完整材料做“旧/统一复核口径 × 有/无旧机械判决提示”四臂对照，正式的统一口径无提示请求只执行一次并复用为对照臂；其他三臂仅记录敏感性，不选择正式判决。每个抽样任务最多增加3次诊断请求，失败如实保留，不重试。

该模式另对8个人造契约样例各跑旧、新复核一次，最多16次请求，记录是否符合预先写明的合成逻辑；它不是书籍预测的人工金标准。全部正式任务及恢复完整性预检先完成，校准和影子对照随后只使用剩余预算，避免抢占正式任务的修订额度。诊断与正式任务共用同一LLM账本，`policy_calibration.json`中的费用差额不能再次加到总账。正式臂若经历结构修复，会显式标记并从主要同协议配对统计中排除；失败与排除数仍展示。无需更多已判定才算通过，也不以未定率下降证明判断准确。

`toolkit/diagnose_search_run.py RUN_DIR... --output-dir DIR`按有序产物生成状态路径、检索覆盖、日期门槛与同材料对照统计；只读取程序记录，不进行人工真伪判断。

结果不会自动覆盖已发布的历史案例。模型复核通过不保证事实判断正确；技术完成率与判断类别分别统计。

可将各轮精简产物放在同一个审计目录下，再由程序生成合并报告。它核对产物哈希和父子运行关系，只允许恢复尚未完成的任务，保留全部尝试与累计费用：

```sh
python toolkit/summarize_cloud_runs.py \
  cases/america-against-america/audit/cloud/42582635639 \
  cases/america-against-america/audit/cloud/42584159842 \
  cases/america-against-america/audit/cloud/42585100516 \
  cases/america-against-america/audit/cloud/42585921943 \
  --output-dir cases/america-against-america/audit/cloud
```
