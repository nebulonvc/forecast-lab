# `method-pack/` — 纯文本预测方法与回测数据表（零可执行代码）

本目录是 **Forecast Lab（信号与噪音）** 对外开放的**纯数据方法源（Zero-Code Data Registry）**，仅包含两个人类与 AI Agent 均可直接阅读的纯 JSON 文本文件：

- [`manifest.json`](manifest.json)：当前最新版本的七步预测协议、接入访谈问题、7 大领域历史基准率与主/反双透镜、五大翻车模式扫雷规则及三轴事实核查标准。
- [`curated_backtest_questions.json`](curated_backtest_questions.json)：精选高信噪比历史已结算预测校准题库（附带时间截点 `as_of`、截点前公开背景、当时预测市场隐含概率与真实结算结果）。

## 为什么采用“纯文本 Markdown + JSON”而非让用户下载程序？

1. **零木马与供应链风险**：外部用户和 AI Agent 接入时**无需下载、安装或运行任何 `.py` / `.sh` 脚本或第三方包**，仅通过只读方式读取本目录下的公开 JSON 与根目录的 [`AGENT_SETUP.md`](../AGENT_SETUP.md)。
2. **预测方法动态热更新**：当主仓库升级预测透镜、更新基准率或补充反例规则时，用户的 Agent 只需重新读取一次 `manifest.json` 的公开 GitHub 链接，即可自动获得最新方法，完全不影响用户本地或自有仓库中的 `.md` 预测账本。
3. **跨平台全兼容**：无论是本地编码 Agent（Claude Code、Antigravity、Cursor、Codex），还是网页端/企业自建智能体平台（Claude Projects、Custom GPTs、Dify、Coze、LangGraph），均可直接挂载这两个静态文本文件作为知识库与规则源。
