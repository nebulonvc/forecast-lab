# AGENTS.md — Forecast Lab 智能体协作规范

欢迎来到 **Forecast Lab（信号与噪音：可复盘的预测实验室）**！
当你（Claude Code、Antigravity、Cursor、Codex、Gemini CLI 等编码与研究 Agent）在本仓库协助用户时，请严格遵循以下方法论与工程纪律。

---

## 1. 核心认知与必读文档

执行任何预测创建、证据检索或书籍拆解任务前，请按需查阅：
- **预测方法论与五类结论定义**：[`docs/01-methodology-signal-and-noise.md`](docs/01-methodology-signal-and-noise.md) 与 [`toolkit/METHOD.md`](toolkit/METHOD.md)
- **七步预测法与八大场景透镜速查表**：[`docs/03-data-and-forecasting-guide.md`](docs/03-data-and-forecasting-guide.md)
- **个人定期预测工作流**：[`docs/04-fork-and-agent-workflow.md`](docs/04-fork-and-agent-workflow.md) 及专用技能 [`.agents/skills/forecast-tracker/SKILL.md`](.agents/skills/forecast-tracker/SKILL.md)
- **零代码智能体接入、动态方法包与 Polymarket 回测**：远程接入协议 [`AGENT_SETUP.md`](AGENT_SETUP.md)、实战指南 [`docs/05-quickstart-onboarding-and-polymarket.md`](docs/05-quickstart-onboarding-and-polymarket.md)、动态方法源 [`method-pack/manifest.json`](method-pack/manifest.json) 及接入技能 [`.agents/skills/forecast-onboarding/SKILL.md`](.agents/skills/forecast-onboarding/SKILL.md)
- **社区共建书籍拆解与 PR 合入数据库**：实战指南 [`docs/07-contribute-a-book.md`](docs/07-contribute-a-book.md)、共建工具 [`toolkit/contribute_book.py`](toolkit/contribute_book.py) 及技能 [`.agents/skills/book-contributor/SKILL.md`](.agents/skills/book-contributor/SKILL.md)
- **数据驱动的预测方法优化（MCP & Skill）**：[`docs/06-forecast-method-optimization.md`](docs/06-forecast-method-optimization.md)、MCP 服务 [`toolkit/forecast_mcp.py`](toolkit/forecast_mcp.py) 及优化技能 [`.agents/skills/forecast-optimizer/SKILL.md`](.agents/skills/forecast-optimizer/SKILL.md)
- **半导体预测的落地规程（补充文档，不改引擎、不登记预测）**：[`docs/09-semiconductor-forecast-framework.md`](docs/09-semiconductor-forecast-framework.md)。具体预测须逐步执行并在报告中留下自检矩阵；用户未确认前不冻结入库

---

## 2. 四类常见用户任务的标准执行协议

### 任务 A：帮用户把一个想法转化为规范的“可核验预测”并执行数据驱动方法优化
1. **先跑数据驱动基线体检、方法寻优与历史同构校准**：优先调用 MCP 工具 `optimize_forecast`（技术/产业类命题同步参考 `evaluate_tech_differentiation`，或运行 `python3 toolkit/forecast_optimizer.py optimize --statement "..."`），用全库 10,745 条预测 `SuperLearner` 与 150 年 12 次技术浪潮 Bass 扩散曲线给出“历史同构骨架斜率”，并根据返回的 `realtime_parameters_to_fetch_now` 联网核查当下的真实行业瓶颈数据（如并网排队、BOM回本周期、付费留存率）。
2. **去噪拆题并完整写出预测方法（严禁只给结论不写方法）**：协助用户补齐 **主体 + 对象 + 量词 + 可测指标（含分母，严分增量流量 vs 存量保有量 + 权威数据源） + 期限 + 前提条件**（严查 `出现 ≠ 普及 ≠ 主导 ≠ 取代`），并在终局预测中**显式写出选用的预测方法、代入实时参数的四步推导链、历史同构校准说明、反校验透镜、领先观测指标与证伪条件**，再次调用 `optimize_forecast` 核验可操作化达 `6/6`、`explicit_method_disclosed=true` 且陷阱清零。
3. **调用标准工具登记**：调用 MCP `register_optimized_forecast` 或使用 `toolkit/periodic_tracker.py` 写入 `my-forecasts/`，不要手拼残缺 JSON：
   ```bash
   python3 toolkit/periodic_tracker.py --case my-forecasts add \
     --id "<唯一ID>" --domain "<领域>" --statement "<冻结承诺>" \
     --horizon "<期限>" --scope "<统计口径>" --method "<主透镜>" \
     --counter-lens "<反校验透镜>" --indicators "<领先指标>" --falsification "<证伪条件>"
   python3 toolkit/pipeline.py --case my-forecasts check
   ```

### 任务 B：对 `my-forecasts/` 执行定期追踪、搜证与三轴复盘
1. 先推进账本观察截止日：`python3 toolkit/periodic_tracker.py --case my-forecasts bump-cutoff`
2. **获取正反双向证据**：
   - 若环境配置了 `BOOKPRED_DEEPSEEK_API_KEY` 与 `EXA_API_KEY`，可运行：
     ```bash
     python3 toolkit/verify_prediction.py --case my-forecasts --all-forecasts \
       --workers 4 --budget-cny 5 --exa-budget-usd 1 \
       --output-dir my-forecasts/output/search_verify/latest
     python3 toolkit/periodic_tracker.py --case my-forecasts digest \
       --search-run-dir my-forecasts/output/search_verify/latest
     ```
   - 若无上述 API Key，请利用你自身的联网搜索工具，**强制成对搜索每条预测的支持证据与反面证据**（优先官方统计局、央行、IEA/OECD/世行、财报等一手数据），将来源正文保存至 `my-forecasts/data/sources/`，计算真实 SHA-256 登记到 `my-forecasts/data/evidence.jsonl`。
3. **三轴汇报，不静默篡改**：向用户分拆汇报 **事件轴、机制轴、时间轴** 的最新进展。未经用户确认，不要直接覆盖冻结承诺原文（`quote`）。

### 任务 C：拆解新书、长篇报告或人物访谈并提交 PR 合入数据库
1. **初始化并选择路径**：使用 `python3 toolkit/contribute_book.py init --case cases/<slug> ...` 初始化案例（详见 [`.agents/skills/book-contributor/SKILL.md`](.agents/skills/book-contributor/SKILL.md) 与 [`docs/07-contribute-a-book.md`](docs/07-contribute-a-book.md)）：
   - **路径 A（自有 Agent 原生并行防偷懒模式）**：优先调用 Antigravity `run_workflow` 执行 [`toolkit/antigravity_book_workflow.py`](toolkit/antigravity_book_workflow.py)（或分步执行 `contribute_book.py chunk-txt --batch-size 4` → 并行子智能体逐分片抽取并附带 `body_sha256_12` + `tail_anchor` 块尾阅读证明 → `audit-progress` → `import-extractions --require-proof` → `export-verify-tasks --batch-size 3` → 并行子智能体成对联网搜证与六维自检 → `apply-assessments --require-dual-evidence`），从根源上保证分片并行、Context 零膨胀且绝不跳读偷懒；
   - **路径 B（自有 API 并发模式）**：`prepare_book.py txt --apply`（支持 `--api-base`）→ `contribute_book.py trim-contexts` → `verify_prediction.py --all-forecasts` → `contribute_book.py import-verify`。
2. **严守版权与隐私红线**：完整原书 TXT/PDF 必须放在仓库外或被忽略的 `cases/<slug>/input/` 目录，**严禁将完整原书、未裁剪的长上下文、API 密钥或中间包含全文的 `txt_import` 分块计划提交进 Git**。
3. **合入总表与门禁验收**：提交 PR 前必须同步数据库并通过全部门禁：
   ```bash
   python3 toolkit/contribute_book.py sync-database --case cases/<slug>
   python3 toolkit/contribute_book.py pr-check --case cases/<slug>
   python3 -m unittest discover -s toolkit/tests -v
   ```

### 任务 D：零代码外部轻量接入、动态方法同步、Polymarket 练习认证与盲测回测
1. **零代码先访谈再建账本**：外部用户无需下载任何脚本程序。请按 [`AGENT_SETUP.md`](AGENT_SETUP.md) 只读读取 [`method-pack/manifest.json`](method-pack/manifest.json)，先向用户确认目标模式、关注领域、存放环境与复盘频率，生成纯文本 `AGENTS.md` 与 `forecasts/README.md` 账本。
2. **随时从 GitHub 只读同步最新方法**：每次预测设计或复盘前重新读取一次上游 `method-pack/manifest.json`，自动应用最新迭代的双透镜、分档基准率与噪音体检规则。
3. **Polymarket 只读对标与盲测回测**：通过只读访问 Polymarket 公开接口（`gamma-api.polymarket.com`）拉取题目、认证官方结算并计算 Brier Score 与 Market Edge；或读取 [`method-pack/curated_backtest_questions.json`](method-pack/curated_backtest_questions.json) 按 `as_of` 时间截点隐藏答案开展盲测训练。
