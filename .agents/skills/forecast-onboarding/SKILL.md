---
name: forecast-onboarding
description: 零代码引导用户通过 4 个问题构建专属预测领域、Markdown 预测账本、Agent 自动正反事实核查与 Polymarket 盘口认证/历史盲测回测，并支持从 GitHub 只读同步最新《信号与噪音》方法表。
---

# Forecast Onboarding（零代码纯文本接入技能）

本技能遵循根目录 [`AGENT_SETUP.md`](../../../AGENT_SETUP.md) 与公开方法数据表 [`method-pack/manifest.json`](../../../method-pack/manifest.json)，**全程无需用户下载或运行任何外部程序**。

## 执行步骤

1. **只读加载最新方法表**：
   读取本地 `method-pack/manifest.json`（若在外部独立仓库中，只读获取 `https://raw.githubusercontent.com/nebulonvc/forecast-lab/main/method-pack/manifest.json`）。
2. **四问访谈定位需求**：
   向用户简短确认：① 目标模式（前瞻记账 / Polymarket 练习 / 历史盲测 / 全部开启）；② 关注领域（自动匹配历史基准胜率与主/反双透镜）；③ 存储环境（本地目录 / 自有 GitHub 仓库 / 自有 Agent 平台）；④ 复盘与事实核查频率。
3. **生成纯 Markdown 空间**：
   在目标工作区创建定制版 `AGENTS.md` 与 `forecasts/README.md` 总账本（纯 `.md` 文本，肉眼可审）。
4. **日常协助闭环**：
   - **设计预测**：按七步法补齐六要素，用 `noise_linter_rules` 拦截绝对化口号与缺失分母，生成 `forecasts/cards/<id>.md`；
   - **自动事实核查**：用 Agent 自带搜索同时检索支持证据与反面证据（优先官方统计与财报），追加卡片第 5 节【事件 × 机制 × 时间】三轴日志；
   - **Polymarket 对标与认证**：只读读取 `https://gamma-api.polymarket.com/events` 与 `/markets/<id>`，记录主观概率并对标市场隐含概率，结算后计算 Brier Score $(P_{\text{user}} - Y)^2$ 与 Market Edge；
   - **历史盲测回测**：读取 `method-pack/curated_backtest_questions.json`，在用户给出概率前隐藏 `actual_outcome` 与截点盘口概率，作答后揭晓评分并记入账本。
