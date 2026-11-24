# AGENTS.md — Forecast Lab 智能体协作规范

欢迎来到 **Forecast Lab（信号与噪音：可复盘的预测实验室）**！
当你（Claude Code、Antigravity、Cursor、Codex、Gemini CLI 等编码与研究 Agent）在本仓库协助用户时，请严格遵循以下方法论与工程纪律。

---

## 1. 核心认知与必读文档

执行任何预测创建、证据检索或书籍拆解任务前，请按需查阅：
- **预测方法论与五类结论定义**：[`docs/01-methodology-signal-and-noise.md`](docs/01-methodology-signal-and-noise.md) 与 [`toolkit/METHOD.md`](toolkit/METHOD.md)
- **七步预测法与八大场景透镜速查表**：[`docs/03-data-and-forecasting-guide.md`](docs/03-data-and-forecasting-guide.md)
- **个人定期预测工作流**：[`docs/04-fork-and-agent-workflow.md`](docs/04-fork-and-agent-workflow.md) 及专用技能 [`.agents/skills/forecast-tracker/SKILL.md`](.agents/skills/forecast-tracker/SKILL.md)
- **数据驱动的预测方法优化（MCP & Skill）**：[`docs/06-forecast-method-optimization.md`](docs/06-forecast-method-optimization.md)、MCP 服务 [`toolkit/forecast_mcp.py`](toolkit/forecast_mcp.py) 及优化技能 [`.agents/skills/forecast-optimizer/SKILL.md`](.agents/skills/forecast-optimizer/SKILL.md)

---

## 2. 四类常见用户任务的标准执行协议

### 任务 A：帮用户把一个想法转化为规范的“可核验预测”并执行数据驱动方法优化
1. **先跑数据驱动基线体检与方法寻优**：优先调用 MCP 工具 `optimize_forecast`（或运行 `python3 toolkit/forecast_optimizer.py optimize --statement "..."`），基于全库 132 部著作、8,130 条预测与 $t_0$ 历史状态训练的 `SuperLearner` 识别伪预测噪音、高赔率翻车陷阱，并获取最优「主透镜 + 反校验透镜 + 承诺硬度」与样本外校准概率。
2. **去噪拆题并完整写出预测方法（严禁只给结论不写方法）**：协助用户补齐 **主体 + 对象 + 量词 + 可测指标（含分母与权威数据源） + 期限 + 前提条件**（严查 `出现 ≠ 普及 ≠ 主导 ≠ 取代`），并在终局预测中**显式写出选用的预测方法、四步推导链、反校验透镜、领先观测指标与证伪条件**，再次调用 `optimize_forecast` 核验可操作化达 `6/6`、`explicit_method_disclosed=true` 且陷阱清零。
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

### 任务 C：拆解新书、长篇报告或人物访谈中的预测
1. 在 `cases/<slug>/` 初始化独立案例：`python3 toolkit/pipeline.py --case cases/<slug> init ...`
2. **严守版权与隐私红线**：完整原书 TXT/PDF 必须放在仓库外或被忽略的 `cases/<slug>/input/` 目录，**严禁将完整原书、API 密钥或中间包含全文的 `txt_import` 分块计划提交进 Git**。
3. 完成后必须通过以下两条门禁才算交付：
   ```bash
   python3 toolkit/pipeline.py --case cases/<slug> check
   python3 -m unittest discover -s toolkit/tests -v
   ```
