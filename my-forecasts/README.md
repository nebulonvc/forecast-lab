# 我的定期预测工作区（`my-forecasts/`）

这是专门为 **Fork 本仓库的用户** 准备的“个人定期预测分析账本”开箱即用工作区。
它的底层数据格式与全库 134 个经典著作案例 100% 兼容，可直接调用 `toolkit/` 的全部校验、联网双向搜证与定期简报工具。

---

## 快速上手（3 条命令）

### 1. 登记一条你自己的新预测（自动生成冻结预测卡 + JSONL 记录）

```bash
python3 toolkit/periodic_tracker.py --case my-forecasts add \
  --id "2026-my-first-forecast" \
  --domain "AI与产业商业化" \
  --statement "到2028年底，中国新能源汽车在乘用车新车年度销量中的渗透率将超过65%。" \
  --horizon "2026–2028" \
  --scope "以中汽协或乘联会年度国内乘用车零售/批发公布口径为准" \
  --method "约束账本法 + 技术功能扩散链法" \
  --counter-lens "检查充电电网负荷瓶颈、电池原材料价格反弹与购置税政策退坡影响" \
  --indicators "月度新能源乘用车零售渗透率、动力电池装车成本、县域快充桩增速" \
  --falsification "2028年全年新能源乘用车新车渗透率低于65%"
```

### 2. 本地完整性审计与生成追踪简报（无需 API Key）

```bash
python3 toolkit/pipeline.py --case my-forecasts check
python3 toolkit/periodic_tracker.py --case my-forecasts digest
```

生成的简报位于 [`output/periodic_digest.md`](output/periodic_digest.md)，单张预测卡位于 [`cards/`](cards/)。

### 3. 结合 AI Agent 或 GitHub Actions 定期联网搜证

- **与本地 AI Agent 协作**：直接在 Claude Code / Antigravity / Cursor 中打开仓库，对 Agent 说：*“帮我巡检 `my-forecasts` 里的预测，搜索最新正反公开数据并更新定期复盘简报。”*（详见根目录 [`AGENTS.md`](../AGENTS.md)）
- **云端每月自动巡检**：在 Fork 仓库设置 `BOOKPRED_DEEPSEEK_API_KEY` 与 `EXA_API_KEY` 后，[`.github/workflows/periodic-forecast.yml`](../.github/workflows/periodic-forecast.yml) 将每月自动搜证并以 GitHub Issue 推送复盘简报！完整教程见 [`../docs/04-fork-and-agent-workflow.md`](../docs/04-fork-and-agent-workflow.md)。
