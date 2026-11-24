---
name: forecast-optimizer
description: 基于全库 132 部著作、8,130 条历史预测与发布时点历史状态训练的超学习器（Super-Learner），对用户的预测命题与推理方法执行数据驱动校准、反事实方法寻优、翻车陷阱扫雷与三轴贝叶斯更新。支持任何 Agent 终端通过 MCP 或 CLI 调用。
---

# Forecast Optimizer（数据驱动预测方法优化）技能指南

当用户提出一个预测直觉、希望改进某条预测的准确度、评估既有预测账本的方法质量，或在新增证据后做概率更新时，启用本技能。

本技能底层由全库 **132 部著作、8,130 条可评分预测（5,060 条已判定结果 + 2,553 条非预测噪音对照 + 1531–2026 发布时点宏观历史状态特征）** 按著作分组交叉验证（Out-of-Book Grouped 5-Fold CV）训练的 **`SuperLearner` 对数线性池化校准引擎** 驱动，绝不凭大模型主观拍脑袋给概率。

---

## 一、双通道调用方式（自动适配任何 Agent 终端）

1. **优先通道（MCP Server 已挂载时）**：直接调用 `forecast-lab-optimizer` MCP 工具：
   - `optimize_forecast`：对原始预测草案执行可操作化体检、噪音陷阱识别、五类/四类校准概率估算与反事实方法寻优；
   - `query_reference_class`：查询同领域、同时间跨度的层级经验贝叶斯（Empirical Bayes）基准率与正反历史先例；
   - `bayesian_update_forecast`：输入正反双向新证据，执行事件轴/机制轴/时间轴阻尼对数赔率更新；
   - `audit_forecast_ledger`：批量体检并优化 `my-forecasts` 账本；
   - `register_optimized_forecast`：将优化定稿后的预测一键冻结写入账本并通过 `pipeline.py check` 字节级校验。
2. **通用零配置通道（任意终端 CLI 直接调用，零第三方依赖）**：
   ```bash
   # 1. 对任意预测草案执行数据驱动方法优化（输出 Markdown 或 JSON）
   python3 toolkit/forecast_optimizer.py optimize \
     --statement "<用户的原始预测表述>" \
     --domain "<领域>" \
     --horizon "<期限，如 2026-2030>" \
     --format markdown

   # 2. 查询同领域同跨度经验贝叶斯基准率与 330 精选库正反先例
   python3 toolkit/forecast_optimizer.py reference-class \
     --domain "<领域>" --horizon-years 5 --keyword "<核心词>"

   # 3. 对现有预测账本执行批量方法体检
   python3 toolkit/forecast_optimizer.py audit-ledger --case my-forecasts

   # 4. 基于正反双向新证据执行三轴贝叶斯后验更新
   python3 toolkit/forecast_optimizer.py update \
     --statement "<预测命题>" --domain "<领域>" \
     --evidence-json '[{"relation":"support","source_tier":"official_stats","axis":"event","summary":"..."},{"relation":"counter","source_tier":"institutional","axis":"time","summary":"..."}]'
   ```

---

## 二、标准五步方法优化工作流（Agent 必循协议）

### Step 1：先跑基线诊断，量化“不改写直接发”的翻车风险
拿到用户的原始判断后，**不要先凭感觉改写**，第一时间调用 `optimize_forecast`（或 CLI `optimize`），读取三项硬指标：
- **有效预测置信度（Stage 0 Denoiser）**：识别是否混入了“应该如何”的规范倡议或不可证伪的静态格言；
- **六要素完整度（`score_out_of_6`）**：检查主体/对象、含分母可测指标、唯一权威结算源、明确期限、定量证伪阈值、领先观测指标；
- **高赔率噪音陷阱命中（`traps_detected`）**：重点拦截无账本硬数字外推（CMH 控制后严格胜率 `-9.1pp`）、无账本超越/取代断言（错误率 `+7.9pp`）、阶段顺风单调外推（`-8.6pp`）、跨层乌托邦跳跃（`-17.9pp`）与复合捆绑命题（`-6.7pp`）。

### Step 2：依据反事实寻优结果切换“主透镜 + 反校验透镜 + 承诺硬度”
读取引擎遍历 **6 大信号方法原型 × 3 类承诺硬度** 后给出的最优配置（`recommended_optimization`）：
- **短中期（`1–10 年`）**：优先采用 **约束账本法 / 制度激励法 + 显式区间门槛**（同时间档控制下，有硬账本支撑的显式期限比无账本拍脑袋日期严格胜率高 **`+14.8pp`**、错误率低 **`-5.9pp`**）；
- **中长期（`5–25 年`）**：优先采用 **多情景条件分支法 $P(A) \times P(B\mid A)$** 或 **技术功能扩散链法**，将触发前提与结果解耦；
- **超长周期（`>15 年`）**：锚定 **地缘底盘法 / 人口代际队列**，剔除无产能周期支撑的精确年份点位。

### Step 3：锚定历史正反先例（防“故事好听但基准率极低”）
向用户展示引擎匹配的 1–2 条 **同领域高光成功范式（`H001–H100`）** 与 **大师翻车警示（`M01–M50`）**，说明为什么同类问题上前人赢在哪里、死在哪里。

### Step 4：二次校准验证（Before vs. After 闭环）
协助用户拟定收敛后的规范预测文本（补齐分母、权威数据源、主反双透镜、领先指标与证伪阈值），**再次调用 `optimize_forecast`** 验证可操作化得分升至 `6/6`、噪音陷阱清零，并向用户呈现优化前后的校准严格胜率、方向命中率与错误率变化。

### Step 5：事前冻结入库与持续三轴复盘
经用户确认后，调用 `register_optimized_forecast`（或 `periodic_tracker.py add` + `pipeline.py check`）将优化后的预测卡及校准先验概率原子化写入 `my-forecasts/`。后续巡检时强制成对输入 `support` 与 `counter` 证据，调用 `bayesian_update_forecast` 追踪概率演进。
