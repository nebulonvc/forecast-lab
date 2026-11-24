---
name: forecast-tracker
description: 创建可证伪预测卡、执行正反双向证据巡检，并按《信号与噪音》事件/机制/时间三轴框架维护用户的定期预测账本（my-forecasts）。当用户希望做新预测、定期复盘预测进展或检验某份报告预测时启用。
---

# Forecast Tracker 技能操作指南

本技能帮助用户将模糊判断转化为可复盘的实证承诺，并进行定期贝叶斯更新。

## 一、新增预测五步检查（调用 `periodic_tracker.py add` 前必查）

1. **六要素齐备**：主体、对象、量词、指标与分母、明确期限、触发条件是否清晰？
2. **查询同跨度历史基准率**：在 `datasets/all_cases_summary.csv` 或 `datasets/curated_330_forecasts.csv` 检索同领域、同时间跨度的历史胜率与常见死因。
3. **双透镜配对**：不仅选定主推理方法（约束账本 / 制度激励 / 地缘底盘 / 功能扩散 / 风险边界 / 条件分支），还必须挂载至少一个反校验视角（如杰文斯反弹、替代供给、政策反制、能力参差）。
4. **可观测领先指标**：给出无需等到终局、每个季度/半年就能查到数据的 2–3 个先行指标。
5. **写入并校验**：
   ```bash
   python3 toolkit/periodic_tracker.py --case my-forecasts add ...
   python3 toolkit/pipeline.py --case my-forecasts check
   ```

## 二、定期预测复盘流程（Periodic Bayesian Update）

1. 读取 `my-forecasts/data/claims.jsonl` 与 `my-forecasts/cards/*.md`。
2. 运行 `python3 toolkit/periodic_tracker.py --case my-forecasts bump-cutoff` 将截止日更新至今日。
3. 对每条在册预测同时检索 **支持证据（Support）** 与 **反面证据（Counter）**：
   - 若调用 `verify_prediction.py`，输出至 `my-forecasts/output/search_verify/<YYYY-MM-DD>` 后执行 `periodic_tracker.py digest`。
   - 若由 Agent 自身检索，请**强制成对检索支持证据与反面证据**（优先官方统计局、央行、IEA、财报），存档原始统计摘要至 `my-forecasts/data/sources/`，核对 `sha256` 后登记进 `my-forecasts/data/evidence.jsonl`（若用户采用轻量纯 Markdown 账本，直接将核实链接与日期追加至预测卡第 5 节表格即可，详见 [`AGENT_SETUP.md`](../../../AGENT_SETUP.md)）。
4. 在预测卡第 5 节“三轴复盘记录”追加一行巡检日志，区分：
   - **事件轴**：指标数值向目标移动还是背离？
   - **机制轴**：当初假设的驱动瓶颈（如电网排队、成本曲线）是否真的是主因？
   - **时间轴**：推进速度符合预期、提前还是滞后？
5. 若正式更新账本评估状态，构造全量评估提案后运行：
   ```bash
   python3 toolkit/pipeline.py --case my-forecasts apply assess <proposals.jsonl>
   python3 toolkit/pipeline.py --case my-forecasts check
   python3 toolkit/pipeline.py --case my-forecasts report
   python3 toolkit/periodic_tracker.py --case my-forecasts digest
   ```
