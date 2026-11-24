# AGENTS.md — Forecast Lab 智能体协作规范

欢迎来到 **Forecast Lab（信号与噪音：可复盘的预测实验室）**！
当你（Claude Code、Antigravity、Cursor、Codex、Gemini CLI 等编码与研究 Agent）在本仓库协助用户时，请严格遵循以下方法论与工程纪律。

---

## 1. 核心认知与必读文档

执行任何预测创建、证据检索或书籍拆解任务前，请按需查阅：
- **预测方法论与五类结论定义**：[`docs/01-methodology-signal-and-noise.md`](docs/01-methodology-signal-and-noise.md) 与 [`toolkit/METHOD.md`](toolkit/METHOD.md)
- **七步预测法与八大场景透镜速查表**：[`docs/03-data-and-forecasting-guide.md`](docs/03-data-and-forecasting-guide.md)
- **个人定期预测工作流**：[`docs/04-fork-and-agent-workflow.md`](docs/04-fork-and-agent-workflow.md) 及专用技能 [`.agents/skills/forecast-tracker/SKILL.md`](.agents/skills/forecast-tracker/SKILL.md)

---

## 2. 三类常见用户任务的标准执行协议

### 任务 A：帮用户把一个想法转化为规范的“可核验预测”并入库
1. **先去噪拆题，拒绝模糊口号**：引导或协助用户补齐六要素——**主体 + 对象 + 量词 + 可测指标（含分母与权威数据源） + 期限 + 前提条件**。严查 `出现 ≠ 普及 ≠ 主导 ≠ 取代`。
2. **配齐双透镜与五大翻车体检**：从 [`docs/03-data-and-forecasting-guide.md`](docs/03-data-and-forecasting-guide.md) 匹配“主透镜 + 反校验透镜”，明确写出 **领先观测指标** 与 **证伪条件**。
3. **调用标准工具登记**：使用 `toolkit/periodic_tracker.py` 写入 `my-forecasts/`（或用户指定的账本目录），不要手拼残缺 JSON：
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
