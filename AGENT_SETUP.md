# AGENT_SETUP.md — 《信号与噪音》零代码智能体接入与运行协议

> **安全与透明承诺（Zero-Code & Zero-Malware Guarantee）**
> 本协议为 **100% 零代码纯文本协议**：
> 1. **不下载、不运行任何程序**：全程不需要下载任何 `.py`、`.sh` 或可执行文件，不需要 `pip` / `npm` 安装任何包；
> 2. **不需要任何私钥、账号或钱包**：预测方法读取自 GitHub 公开纯文本 JSON，预测市场数据读取自 Polymarket 官方公开只读网页接口；
> 3. **全部记录均为人类可读的 `.md` 笔记**：所有配置、预测卡与复盘记录均以标准 Markdown 表格保存在你自己的本地文件夹或你自己的 GitHub 仓库中，肉眼一眼可查。

---

## 致 AI Agent 的执行指南

当你（Claude Code、Antigravity、Cursor、Codex、OpenClaw，或 Claude Projects / GPTs / Dify 等任意智能体）收到用户发来的本协议时，请严格遵循**“只读公开文本数据 + 本地仅读写 Markdown 文档”**的原则，依次协助用户完成以下流程。

---

### 第一步：读取上游最新预测方法表，向用户提 4 个简短问题

我们的预测方法、历史基准率与双透镜库会随研究迭代持续更新。请先只读读取最新的方法注册表：
- **最新方法数据表（JSON）**：`https://raw.githubusercontent.com/nebulonvc/forecast-lab/main/method-pack/manifest.json`

读取后，用自然、简洁的语言向用户确认 **4 个问题**（可附带推荐默认项，用户回答“按推荐来”即可一键通过）：
1. **主要目标**：你想做**日常行业/宏观预测记账**、接入 **Polymarket 预测市场练习对标**、做**历史题目盲测回测**，还是**三者全部开启（推荐）**？
2. **专属预测领域**：你主要关注哪些领域？（如：AI 与算力电力、宏观经济与利率、地缘政治与供应链、科技商业颠覆、能源与大宗矿产、加密与数字资产、人口与社会政策，或自定义领域）
3. **保存与运行环境（Runtime）**：预测账本保存在**当前本地文件夹**、提交到**你自己的独立 GitHub 仓库**，还是作为规则嵌入**你自己的智能体系统**？
4. **事实核查与检验频率**：默认由 Agent 在每次复盘时自动执行**正反双向权威搜证 + Polymarket 官方结算核对**（建议每月或每季度一次），是否合适？

---

### 第二步：在用户目录生成纯 Markdown 专属预测空间（仅 2 个文件起步）

根据用户的回答，从 `manifest.json` 的 `domain_catalog` 中提取对应领域的**历史严格胜率基准、主推理透镜、反校验透镜与一手权威数据源白名单**，在当前目录创建以下纯文本 Markdown 文件：

1. **`AGENTS.md`（智能体持久协作规则）**：
   写入用户选定的领域、专属双透镜、权威核验源白名单，并写明一条自动保鲜规则：*“每次协助设计新预测或执行定期复盘前，先只读读取一次 `https://raw.githubusercontent.com/nebulonvc/forecast-lab/main/method-pack/manifest.json`，确保始终使用上游最新版本的去噪规则与基准率。”*（这样 Claude Code / Antigravity / Cursor 每次打开该目录都会自动生效。）

2. **`forecasts/README.md`（预测总账本与概率校准表）**：
   创建一个直接在 GitHub 网页或本地编辑器中清晰可读的汇总表：
   ```markdown
   # 我的《信号与噪音》预测与校准账本

   - **关注领域**：AI与算力、宏观金融
   - **方法源**：动态读取 `nebulonvc/forecast-lab` 最新 `method-pack/manifest.json`
   - **累计已结算 Brier Score 均值**：暂无（越接近 0 越准；二元随机猜测基准 = 0.2500）

   ## 一、在册预测总表

   | 编号 | 创建日期 | 领域 | 核心可核验承诺 | 主观概率 P | 盘口基准 P_mkt | 目标期限 | 当前五类结论 | Brier (超额优势) |
   | :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- |

   ## 二、历史盲测回测记录

   | 题号 | 盲测截点 (as_of) | 题目摘要 | 我的概率 | 截点盘口 | 真实结果 | 我的 Brier | 相对市场优势 |
   | :--- | :--- | :--- | ---: | ---: | :---: | ---: | ---: |
   ```

---

### 第三步：四大核心能力执行规范（全程无需任何外部脚本）

#### 1. 协助设计预测并冻结立卡（七步去噪法）
当用户提出一个判断（或想对某件事做预测）时：
1. **先拆题去噪**：对照 `manifest.json` 中的 `seven_step_protocol` 与 `noise_linter_rules`，帮用户补齐六要素——**主体 + 对象 + 量词 + 可测指标（含分母与权威数据源） + 期限 + 触发条件**。
2. **拦截五大高频翻车陷阱**：检查是否混入了刺猬式绝对词（`100%`、`彻底取代`、`必然崩溃`）、模糊时间词（`很快`、`不久的将来`），严分 `出现 ≠ 普及 ≠ 主导 ≠ 取代`；告知用户该领域与时间跨度的历史基准胜率。
3. **生成冻结预测卡 `forecasts/cards/<编号>.md`** 并登记到 `forecasts/README.md`：
   ```markdown
   # 预测卡：<编号>

   - **创建与冻结日期**：YYYY-MM-DD
   - **所属领域**：<领域>（同档历史基准参考：<读取自 manifest.json>）
   - **事前主观概率（P_user）**：<例如 65%，或定性区间>
   - **关联盘口（可选）**：<Polymarket URL / Market ID / 入场市场隐含概率 P_mkt>

   ## 1. 可核验核心承诺（事前冻结原文，后续严禁事后涂改）
   <六要素完整陈述>

   ## 2. 统计口径、分母与权威数据源
   - **核验数据源与口径**：<官方机构名称与具体指标>
   - **排除边界与前提条件**：<不包括什么>

   ## 3. 双透镜推演
   - **主推理透镜（Signal Lens）**：<存量产能账本 / 制度激励 / 地缘底盘等>
   - **反校验透镜（Counter-Lens）**：<替代供给 / 杰文斯反弹 / 政策反制 / 组织摩擦等>

   ## 4. 定期盯盘领先指标与证伪条件
   - **每季可查领先指标**：<2–3 个先行数据>
   - **明确证伪条件**：<出现什么结果即坦承判断错误>

   ## 5. 三轴复盘记录（事件 × 机制 × 时间）
   | 巡检日期 | 五类结论 | 事件轴进展 | 机制轴验证 | 时间轴节奏 | 正反双向证据摘要与权威链接 |
   | :--- | :--- | :--- | :--- | :--- | :--- |
   | YYYY-MM-DD | 暂无法判断 | 初始冻结 | 待验证 | 窗口期内 | 事前立卡基线 |
   ```

#### 2. 自动执行“正反双向事实核查”（Fact-Check）
当用户说“帮我做一次预测事实核查/复盘”时：
1. 逐张读取 `forecasts/cards/*.md` 中尚未终局结算的预测卡。
2. 利用你自带的联网搜索能力，对每条预测**强制同时执行两组检索**：
   - **支持向证据（Support）**：核查领先指标是否按预期推进；
   - **反面/摩擦证据（Counter）**：专门搜索延期、瓶颈、替代路线或相反统计数据（优先国家统计局、美联储/央行、IEA/OECD/BEA、上市公司财报等一手出处）。
3. 按五类互斥结论（`正确` / `趋势符合` / `部分符合` / `错误` / `暂无法判断`）在预测卡第 5 节追加一行三轴记录（附带真实来源链接与日期），并同步更新 `forecasts/README.md` 总表。**绝不修改第 1 节已冻结的原始承诺文字。**

#### 3. 接入 Polymarket 拉取预测题目与官方结算认证
无需 API Key 或任何插件，直接通过只读网页获取工具（WebFetch）读取 Polymarket 官方公开 JSON 接口：
- **按主题拉取实时开放题目**：
  只读访问 `https://gamma-api.polymarket.com/events?active=true&closed=false&limit=10&tag_slug=economy`（可将 `tag_slug` 替换为 `ai`、`geopolitics`、`tech`、`crypto`、`politics`）。展示二元（Yes/No）题目、交割规则 `description` 与当前市场隐含概率 `outcomePrices`，引导用户先用双透镜独立给出主观概率 $P_{\text{user}}$ 后立卡。
- **自动认证结算结果与计算 Brier Score**：
  对已记录 `market_id` 的预测卡，只读访问 `https://gamma-api.polymarket.com/markets/<market_id>`。
  - 若尚未结算（`closed: false`）：汇报当前市场概率相比入场时的变化；
  - 若官方已终局结算（`closed: true` 且 `umaResolutionStatus: "resolved"`）：根据 `outcomePrices` 读取真实结果 $Y \in \{1, 0\}$，自动计算：
    - **你的 Brier Score**：$(P_{\text{user}} - Y)^2$（范围 0 到 1，越低越准）
    - **入场市场 Brier Score**：$(P_{\text{mkt}} - Y)^2$
    - **相对市场超额优势（Market Edge）**：$(P_{\text{mkt}} - Y)^2 - (P_{\text{user}} - Y)^2$（正值代表跑赢市场共识！）
    并将官方结算链接与得分更新至预测卡与总账本。

#### 4. 历史盲测回测练习（Backtesting）
当用户想立刻练习预测手感或检验一套推理方法时：
1. 只读读取精选回测题库：`https://raw.githubusercontent.com/nebulonvc/forecast-lab/main/method-pack/curated_backtest_questions.json`（或读取 Polymarket `closed=true` 的历史宏观/AI 题目）。
2. **严格盲测防剧透**：每次抽取 1–3 题向用户提问时，**只展示 `as_of`（历史盲测截点日期）、题面、`resolution_criteria` 与 `pre_cutoff_context`**，在用户作答前**严禁透露 `actual_outcome`、`market_prob_at_cutoff` 与 `resolution_summary`**（若测试 Agent 自身，也严禁搜索 `as_of` 之后的信息）。
3. 用户给出主观概率与推理依据后，当场揭晓真实历史结局、当时预测市场赔率与《信号与噪音》机制复盘，算出 Brier Score 与相对市场优势，记录进 `forecasts/README.md` 第二节！

---

### 第四步：如何嵌入用户自建的 Agent 系统或平台？

由于本系统完全基于公开静态 JSON 与清晰的方法规则，用户若拥有自己的智能体系统（如 Claude Projects、ChatGPT Custom GPTs、Dify、Coze、LangGraph、企业内部 Agent），无需部署任何后端服务器：
1. 将本文件核心规则粘贴进该 Agent 的 **System Prompt / Instructions**；
2. 配置两个**只读 HTTP GET 工具（Web Reader）**：
   - 方法源：`https://raw.githubusercontent.com/nebulonvc/forecast-lab/main/method-pack/manifest.json`
   - 预测市场源：`https://gamma-api.polymarket.com/events` 与 `https://gamma-api.polymarket.com/markets/{id}`
3. 挂载用户自己的存储介质（本地 `.md` 目录、GitHub 仓库、飞书文档或 Notion 数据库）即可立即运行。
