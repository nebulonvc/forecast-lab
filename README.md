# Forecast Lab · 信号与噪音：可复盘的预测实验室

**对 132 部著作与机构报告中的 8,130 条预测进行逐条事实核验，检验历史预测的准确度、有效方法与典型失误。**

[![CI](https://github.com/nebulonvc/forecast-lab/actions/workflows/check.yml/badge.svg)](https://github.com/nebulonvc/forecast-lab/actions/workflows/check.yml)
[![Code: MIT](https://img.shields.io/badge/Code-MIT-3D6B52)](LICENSE)
[![Data: CC BY 4.0](https://img.shields.io/badge/Data-CC%20BY%204.0-C85A3A)](LICENSE)

---

## 研究目的

关于未来的著作与报告层出不穷，但其中的判断很少在事后被系统性检验。缺少检验，会导致两种常见的误判：一是将偶然命中视为能力，进而高估作者在其他领域的判断；二是因个别失误而否定作者在结构性问题上的长期洞见。

本项目受纳特·西尔弗（Nate Silver）《信号与噪音》启发，尝试以可复核的方式回答三个问题：

1. **哪些预测者在哪些领域、哪些时间跨度上显著优于同类基准？**
2. **准确的预测依赖哪些可迁移的推理方法？**
3. **即使是顶尖预测者，失误又集中在哪些模式上？**

研究覆盖 16 世纪至 2025 年的 132 部作品，涉及地缘政治、宏观金融、科技商业、人工智能、能源与人口、社会制度、科幻推演七个领域，作者包括伯克、马尔萨斯、威尔斯、凯恩斯、基辛格、克里斯坦森、库兹韦尔，以及 IEA、OECD、世界银行等机构。

> **推荐首先阅读：[核心研究发现](docs/00-key-insights.md)**——包括数据分布、各领域超越基准的预测者、可借鉴的方法、需规避的失误模式，以及 12 个详细的历史案例。

---

## 核心发现

![8,130 条预测的核验结果](docs/figures/fig01-overview.png)

### 一、准确度最高的群体是具备"约束账本"习惯的专业机构

| 作者类型 | 作品数 | 严格胜率 | 方向命中率 | 错误率 |
| :--- | ---: | ---: | ---: | ---: |
| **国际机构与政府智库**（IEA、OECD、世界银行、英国政府科学办公室等） | 21 | **47.0%** | **65.2%** | **6.3%** |
| 政治家与战略实务者（李光耀、布热津斯基、基辛格等） | 15 | 33.1% | 61.9% | 8.5% |
| 地缘与社科学者（扎卡利亚、卡普兰、亨廷顿等） | 27 | 34.3% | 52.6% | 11.7% |
| 经济学家与投资人（凯恩斯、塔勒布、达利欧等） | 17 | 30.3% | 42.7% | 13.9% |
| 科技商业思想家（克里斯坦森、弗里德曼、凯文·凯利等） | 19 | 28.8% | 55.2% | 10.8% |
| 古典思想家与科幻作家（威尔斯、凡尔纳、贝拉米等） | 33 | 29.6% | 35.4% | 31.3% |

*严格胜率 = 正确 ÷ 可判定；方向命中率 = (正确 + 趋势符合) ÷ 可判定；错误率 = 错误 ÷ 可判定。*

机构报告多为近年出版，可能受益于观察窗口较短。但在**控制时间跨度后**，智库在 0–9 年档（47.7%，其他群体 20%–25%）与 10–39 年档（46.1%，其他群体 32%–40%）均保持领先。其优势主要来自三个习惯：先核算存量、产能与成本约束；避免绝对化结论；以条件情景表达不确定性。

![锁定同一时间跨度后，国际机构与智库在可比的两档中均居首位](docs/figures/fig04-author-types-by-horizon.png)

### 二、预测能力具有明显的领域边界

同一作者在不同题材上的表现差异显著：

- **H. G. 威尔斯**：《预言》（1901）推演技术功能扩散，严格胜率 52.2%；《公开的阴谋》（1928）构想世界政府，错误率 40.9%。
- **瑞·达利欧**：《债务危机》（2018）零错误；《原则：应对变化中的世界秩序》（2021）严格胜率仅 12.3%。
- **凯文·凯利**：《失控》（1994）经 32 年检验错误率 5.7%；《必然》（2016）在具体公司与年份上多次失误。

因此，评估一条预测时应关注其是否落在作者的能力圈内，而非作者的整体声誉。

![同一作者在不同题材上的差距](docs/figures/fig07-same-author.png)

### 三、失误多源于将方向判断硬化为缺乏依据的精确数字

全库中写明期限的预测错误率为 17.9%，未写死期限的方向判断为 12.3%。英国政府科学办公室《制造业的未来》（2013）尤为典型：趋势判断错误率 3.7%，写明年份的判断错误率高达 56%。

但这并不意味着应回避量化。IEA、米尔斯海默、杰文斯写明期限的预测严格胜率仍在 50%–63% 之间。**关键在于数字背后是否有存量、产能和建设周期的核算支撑。**

![写死期限的预测错误更多](docs/figures/fig08-explicit-vs-implicit.png)

### 四、观察窗口越长，检验越严格

出版 3 年内作品的错误率为 2.9%，40 年以上升至 25%–40%。短窗口的低错误率在很大程度上是因为大量预测尚未到期（未定率 60.7%），而非作者更为准确。因此，**本项目对任何作品的评价都以同一时间跨度档的平均水平为基准**。

![观察窗口越长，错误率越高](docs/figures/fig02-time-horizon.png)

### 五、错误集中于五种可识别的模式

对 689 条错误预测的归因显示，绝大多数可归入以下五类：

1. **忽略替代供给与技术跃迁**：马尔萨斯、埃利希未能预见化肥与绿色革命对粮食供给的改变。
2. **将方向判断偷换为固定速率、精确年份或极端量词**：如"边际成本每年下降 50%""金砖四国 2015 年 GDP 超过美国"。
3. **跨层跳跃**：由"技术可行"直接推出"社会政治终局"，如"航空将消灭战争与民族主义"。
4. **忽略行动者的绕行与政策反制**：如断言美洲鹤必然灭绝，未考虑后续保护立法。
5. **将阶段性趋势外推为长期单调变化**：如将战后短期通胀视为持续上涨。

凡出现"无论采取何种措施都必将""永远不会""几乎全部"等绝对化表述，其出错率显著高于平均水平。

![超过一半的大师失误源于把正确的方向硬化为精确数字](docs/figures/fig10-failure-modes.png)

### 附：哪些作品同时跑赢了同档基准

横轴为严格胜率超出同一时间跨度平均水平的幅度，纵轴为错误率低于同档平均水平的幅度。右上象限的作品既更常完全命中，也更少出错。

![超越同档基准且错误更少的作品](docs/figures/fig05-beat-the-baseline.png)

各领域领先与落后作品的完整对比、方法表现与数据分布，见[核心研究发现](docs/00-key-insights.md)中的 10 幅图表。

---

## 代表性历史案例

| 作者 | 预测内容 | 后续结果 |
| :--- | :--- | :--- |
| **伯克**（1790） | 法国大革命缺乏财政、军纪与社会秩序支撑，终将由军事强人收场 | 拿破仑掌权；全书 31 条可判定预测零错误 |
| **杰文斯**（1866） | 英国煤耗增长无法长期维持 ✅；煤炭耗尽前不会出现更强替代能源 ❌ | 英国煤产量 1913 年见顶；石油与天然气随后兴起 |
| **威尔斯**（1901） | 很可能在 1950 年前出现成功往返的飞行器 | 1903 年莱特兄弟首飞 |
| **克里斯坦森**（1997） | 传统车企将长期忽视电动车 ✅；电动车将从低端廉价市场切入 ❌ | 打开市场的是高性能、高价位的特斯拉 Roadster |
| **卡普兰**（2012） | 21 世纪欧洲仍将在关键意义上受其与俄罗斯关系的影响 | 2014 年克里米亚事件、2022 年俄乌战争 |
| **马汉**（1897） | 运河必建于尼加拉瓜 ❌；无论建于何处都将成为全球贸易枢纽 ✅ | 运河建于巴拿马，并成为全球航运咽喉 |
| **埃利希**（1968） | 无论采取何种紧急措施，1970 年代都将有数亿人饿死 | 绿色革命使粮食增长超过人口增长；全书错误率 51.1% |
| **库兹韦尔**（2005） | 将半导体的指数增长外推至纳米制造与生物医学 | 20 年后严格胜率 5.4%，错误率 27.0% |

各案例的背景、成败原因与可借鉴之处，详见[核心研究发现 · 第六节](docs/00-key-insights.md#六十二个历史案例详解)。完整的 100 条精彩预测与 50 条大师失误，见 [330 条精选预测全集](docs/reports/curated-330-compendium.md)。

---

## 可借鉴的推理方法

准确的预测集中于以下六类方法：

| 方法 | 核心做法 | 代表 |
| :--- | :--- | :--- |
| **约束账本法** | 拆解存量、流量、在建产能、成本与付费方，以硬约束限定结论 | IEA、杰文斯、李光耀 |
| **制度与激励结构法** | 分析决策权、考核指标与成本承担者，而非公开表态 | 伯克、克里斯坦森、塔勒布 |
| **地缘底盘法** | 以地理、海上通道与邻国安全焦虑等慢变量为锚 | 扎卡利亚、卡普兰、麦金德 |
| **技术功能扩散法** | 预测"将能实现何种功能"，而非"由何种产品或企业实现" | 威尔斯、戴维、弗里德曼 |
| **风险边界法** | 不预测点位，而识别风险暴露、损失承担者与兜底机制 | 塔勒布、鲁比尼 |
| **多情景条件法** | 并列多条路径，并给出判别各路径的领先信号 | OECD、世界银行、梅多斯 |

**按时间跨度选择方法**：3 年以内依据已开工产能、排期与立法日程，可给出具体时间；3–15 年依据制度激励，以情景分支表达；15 年以上仅判断地理、人口结构与技术功能等慢变量，不给出精确年份或具体企业。

完整的七步操作流程见[数据阅读与预测实践指南](docs/03-data-and-forecasting-guide.md)。

---

## 演示视频

| 《手把手学预测》（6 分钟） | 《百大精彩 · 五十翻车 · 未来方向全景》（8 分钟） |
| :---: | :---: |
| [![](media/previews/video1-tutorial-preview.gif)](https://github.com/nebulonvc/forecast-lab/releases/download/v1.0.0/01-hands-on-forecasting-tutorial.mp4) | [![](media/previews/video2-panoramic-preview.gif)](https://github.com/nebulonvc/forecast-lab/releases/download/v1.0.0/02-panoramic-330-forecasts.mp4) |
| 全库结论、七步预测法与美国数据中心用电推演 · [观看](https://github.com/nebulonvc/forecast-lab/releases/download/v1.0.0/01-hands-on-forecasting-tutorial.mp4) | 100 条精彩命中、50 条失误归因与六大领域 180 条未来方向 · [观看](https://github.com/nebulonvc/forecast-lab/releases/download/v1.0.0/02-panoramic-330-forecasts.mp4) |

章节时间轴见 [media/README.md](media/README.md)。

---

## 数据驱动的预测方法优化与 Agent 接入（MCP & Skill）

定性归纳出六类有效方法之后，更关键的一步是**用全库实证数据训练一套可计算的预测方法优化模型**，让用户在任何 AI Agent 终端提出判断时，都能根据数据自动完成概率校准、失误扫雷与推理方法寻优。

### 一、基于 132 部著作与 $t_0$ 历史状态的超学习器（Super-Learner）

我们将仓库内 **132 部独立作品的 10,683 条样本**（**8,130 条可评分预测、5,060 条明确判定、2,553 条剔除非预测对照**）构建为严格防信息穿越的训练集——仅提取预测发布时点 $t_0 \in [1531, 2026]$ 当时可知的事前特征（含 $t \le t_0 - 10$ 时点因果滚动基准率、宏观通胀/技术狂热/地缘压力历史状态面板、承诺硬度与推理透镜，绝不读取事后核验文本）。

融合**三层经验贝叶斯收缩**（Kahneman & Tversky 1979; Efron & Morris 1975）、**右删失两阶段风险分解**（Kalbfleisch & Prentice 2002）、**FFORMA 特征驱动方法元学习**（Montero-Manso et al. 2020 二阶牛顿直方图提升树 `HistXGBoost`）与**对数线性意见池温度校准**（Genest & Zidek 1986; Satopää et al. 2014），在严格的**按著作整书隔离五折交叉验证（Out-of-Book 5-Fold Grouped CV）**中取得全面最优拟合：

| 模型架构（整书隔离样本外评测） | 5 类 Brier ↓ | 5 类 LogLoss ↓ | 已判定 4 类 Brier ↓ | 已判定 4 类 LogLoss ↓ | 序数 RPS ↓ | 方向校准误差 ECE ↓ |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| 静态时间跨度档 × 显隐期限查表基线 | 0.7537 | 1.4756 | 0.7128 | 1.2827 | 0.1913 | 7.04% |
| 正则化广义线性模型（含 $t_0$ 历史状态 + 透镜） | 0.6855 | 1.3580 | 0.7178 | 1.2962 | 0.1924 | 3.70% |
| 二阶牛顿直方图提升树（`HistXGBoost`） | **0.6684** | **1.3198** | 0.7033 | 1.2684 | 0.1891 | 1.84% |
| **温度校准对数线性超学习器（生产采用）** | **0.6701** | **1.3215** | **0.7002** | **1.2637** | **0.1884** | **1.79%** |

同时，通过 **Cochran-Mantel-Haenszel (CMH) 分层检验**锁死同一 `(时间跨度分档 × 显隐期限)` 剥离短窗红利后，数据直接给出了方法寻优的定量依据：**有硬账本支撑的显式期限相比无账本拍脑袋日期，同层严格胜率高出 `+14.84pp`、错误率降低 `-5.88pp`**；而无账本硬数字外推（严格胜率 `-8.73pp`）、阶段顺风单调速率外推（错误率 `+8.80pp`）、无账本“超越/取代”定时断言（错误率 `+7.00pp`）及多目标捆绑命题（严格胜率 `-6.64pp`）均显著拉低表现。

### 二、优化器对每条预测执行的四步干预（强制把预测方法写出来）

当任何 Agent 调用本优化器处理用户的原始预测想法时，会自动完成四步闭环：

1. **伪预测过滤与规范要素体检**：运行 Stage 0 去噪器剔除“应当如何”的倡议或不可证伪格言，检查主体、对象、含分母指标、权威结算源、期限、证伪阈值及方法披露完整度。
2. **高赔率失误陷阱定量拆雷**：自动识别无账本硬数字、单调指数外推、无基数超越断言与跨层乌托邦跳跃，并检索同领域大师翻车反例（`M01–M50`）提示具体死因。
3. **反事实方法与承诺硬度寻优**：遍历 **6 大主推理方法 × 反校验透镜 × 承诺硬度**（短中期显式账本区间 / 中长期条件分支 $P(A) \times P(B\mid A)$ / 超长周期结构方向），输出改写前后的严格胜率提升与错误率下降幅度，并匹配同领域精彩先例（`H001–H100`）。
4. **终局预测强制显式写出预测方法**：严禁只输出一句孤立结论或拍脑袋概率——最终交付的《终局预测卡》必须把 **【可核验预测承诺 + 选用的主预测方法与四步推导链 + 反校验对冲逻辑 + 8,130 库校准概率 + 领先指标与证伪红线】** 完整写出来。

### 三、三种接入方式（支持任何 AI Agent 终端，纯 Python 3.11+ 标准库零依赖）

#### 方式 1：复制下面这段话发给任何 Agent 终端即可接入（最简推荐）

适用于 **Claude Code、Antigravity、Cursor、Codex CLI、Windsurf、Cline、OpenCode** 等任意终端（即便当前在空白目录或其他项目目录，Agent 也会自动零依赖拉取并挂载预固化模型 [`datasets/forecast_optimizer_model.json`](datasets/forecast_optimizer_model.json)）：

```text
请帮我接入开源的 Forecast Lab 数据驱动预测方法优化器（仓库：https://github.com/nebulonvc/forecast-lab.git ，纯 Python 3.11+ 标准库零依赖）：
1. 若当前目录不在 forecast-lab 仓库内，请先执行 `test -d ~/.forecast-lab || git clone --depth 1 https://github.com/nebulonvc/forecast-lab.git ~/.forecast-lab`（若已在仓库内则直接使用当前目录），并阅读 `.agents/skills/forecast-optimizer/SKILL.md`；若当前终端支持配置本地 MCP Server，可将 `python3 <仓库路径>/toolkit/forecast_mcp.py` 挂载为 `forecast-lab-optimizer`。
2. 接下来每当我提出一个预测想法或请你做趋势判断时，你必须先调用 MCP 工具 `optimize_forecast`（或运行 `python3 <仓库路径>/toolkit/forecast_optimizer.py optimize --statement "<预测草案>" --domain "<领域>"`），用全库 132 部著作、8,130 条历史预测训练的 Super-Learner 诊断高赔率翻车陷阱、匹配同领域历史正反先例并完成反事实方法寻优。
3. 【强制交付规范——必须把预测方法写出来】：你最终输出给我的每一条预测，绝不允许只给一句裸结论或拍脑袋概率，必须将“预测结论”与“预测方法”作为整体完整写出：
   (a) 可核验预测承诺（主体 + 对象 + 量词 + 含分母可测指标 + 唯一权威结算数据源 + 明确期限 + 排除边界）；
   (b) 显式预测方法与四步推导链（明确写出选用哪套主方法原型、如何从基期存量/在建流量/否决权激励/成本门槛一步步推导出该结论、搭配什么反校验透镜对冲盲区、为何匹配当前承诺硬度）；
   (c) 8,130 库样本外校准先验概率（展示优化前基线 vs 优化后的严格胜率、方向命中率、部分符合率、错误风险对比）；
   (d) 2–3 个季度/半年度可查的领先观测指标，以及事件×机制×时间三轴明确证伪红线。
准备好后请回复我：“Forecast Lab 预测方法优化引擎已就绪，请告诉我你的预测想法。”
```

#### 方式 2：挂载标准 MCP Server（[`.mcp.json`](.mcp.json) / [`toolkit/forecast_mcp.py`](toolkit/forecast_mcp.py)）

在仓库根目录启动 Claude Code、Cursor 或 Antigravity 时会自动识别 [`.mcp.json`](.mcp.json)；在其他全局客户端中添加以下配置即可调用 6 个标准工具（`optimize_forecast`、`query_reference_class`、`bayesian_update_forecast`、`audit_forecast_ledger`、`register_optimized_forecast`、`get_optimizer_benchmark`）：

```json
{
  "mcpServers": {
    "forecast-lab-optimizer": {
      "command": "python3",
      "args": ["/path/to/forecast-lab/toolkit/forecast_mcp.py"]
    }
  }
}
```

#### 方式 3：通过通用 Agent Skill 或命令行直接调用

仓库内置技能定义 [`.agents/skills/forecast-optimizer/SKILL.md`](.agents/skills/forecast-optimizer/SKILL.md)，或直接在终端运行 CLI 输出包含四步推导链与终局预测卡的完整优化报告：

```bash
python3 toolkit/forecast_optimizer.py optimize \
  --statement "到2028年底，AI将彻底取代50%以上的软件工程师工作，代码编写成本每年减半。" \
  --domain "AI"
```

完整的数学推导、八组模型交叉验证表与工具契约见 **[《数据驱动的预测方法优化与 MCP/Skill 接入指南》](docs/06-forecast-method-optimization.md)**。

---

## 接入预测账本系统、自动事实核查与市场回测

完成预测方法的校准与寻优后，下一步是将预测纳入长期账本持续追踪核对。本项目提供**两种账本运行模式**，可按使用场景任选：

### 模式一：零代码纯文本账本（无需下载或运行任何程序，支持 Polymarket 对标与盲测回测）

如果你不希望在本地下载或运行任何外部脚本，也无需克隆 132 部原书仓库，可以直接让 AI Agent **仅通过只读公开 Markdown/JSON 文档**建立纯 `.md` 预测账本：

```text
请只读阅读 https://raw.githubusercontent.com/nebulonvc/forecast-lab/main/AGENT_SETUP.md 与方法表 https://raw.githubusercontent.com/nebulonvc/forecast-lab/main/method-pack/manifest.json ，帮我以“零代码、纯 Markdown”方式接入《信号与噪音》预测系统（全程不要下载或运行任何外部脚本程序）：
1. 先通过对话向我问 4 个简短问题，确定我的预测目标、关注领域、存放位置（本地目录、我的 GitHub 仓库或自有 Agent 系统）与复盘频率；
2. 根据我的回答，从 manifest.json 提取对应领域的历史基准胜率、主推理透镜、反校验透镜与一手数据源，在当前目录创建纯文本规则 `AGENTS.md` 与预测总账本 `forecasts/README.md`；
3. 后续每次做预测或复盘前重新只读读取一次最新 `manifest.json` 以保持方法同步，并协助我完成：七步法去噪立卡、联网正反双向事实核查、只读访问 Polymarket 公开接口拉题与结算认证，或开展历史时间截点盲测回测。
```

- **预测方法自动热同步**：预测透镜与基准率表托管于公开纯数据文件 [`method-pack/manifest.json`](method-pack/manifest.json)，方法迭代后 Agent 重新只读拉取即可生效，不影响本地账本。
- **Agent 自动事实核查与 Polymarket 结算认证**：Agent 用自带搜索成对核查支持与反面一手数据；并直接只读访问 Polymarket 官方公开接口（`gamma-api.polymarket.com`，免密钥、免钱包）拉取题目、认证 UMA 终局结果并计算 Brier Score 与超额优势（Market Edge）；亦可读取 [`curated_backtest_questions.json`](method-pack/curated_backtest_questions.json) 立即进行时间截点隔离的历史盲测练习。

详见 [给 Agent 的零代码接入协议 (`AGENT_SETUP.md`)](AGENT_SETUP.md) 与 [零代码接入、事实核查与 Polymarket 回测指南](docs/05-quickstart-onboarding-and-polymarket.md)。

### 模式二：整仓 Fork 审计账本（SHA-256 证据校验与 GitHub Actions 定时巡检）

克隆或 Fork 本仓库后，可使用内置的 [`my-forecasts/`](my-forecasts/) 账本与自动化工作流：

1. **优化定稿并冻结入账**：通过 MCP 工具 `register_optimized_forecast` 或 [`toolkit/periodic_tracker.py`](toolkit/periodic_tracker.py) 将带显式方法推导链的预测卡写入 `my-forecasts/`，并由 `pipeline.py check` 执行字节级哈希校验。
2. **云端每月自动检索正反证据**：配置 DeepSeek 与 Exa 的 API Key 后，GitHub Actions（[`periodic-forecast.yml`](.github/workflows/periodic-forecast.yml)）每月自动并发检索支持与反驳证据，并以 Issue 推送复盘简报。
3. **三轴阻尼贝叶斯后验复盘**：无外部 API 时，由本地 Agent 检索一手统计数据并调用 `bayesian_update_forecast` 按事件、机制、时间三轴更新概率分布。

详见 [Fork 与定期预测工作流指南](docs/04-fork-and-agent-workflow.md)。

---

## 文档导航

| 目的 | 文档 |
| :--- | :--- |
| **了解核心研究发现** | [docs/00-key-insights.md](docs/00-key-insights.md) |
| **数据驱动的预测方法优化（MCP & Skill）** | [docs/06-forecast-method-optimization.md](docs/06-forecast-method-optimization.md) |
| **复制给 AI Agent 的零代码接入协议** | [AGENT_SETUP.md](AGENT_SETUP.md) |
| **零代码接入、事实核查与 Polymarket 回测** | [docs/05-quickstart-onboarding-and-polymarket.md](docs/05-quickstart-onboarding-and-polymarket.md) |
| 理解研究方法与判定标准 | [docs/01-methodology-signal-and-noise.md](docs/01-methodology-signal-and-noise.md) |
| 了解核验管线的工程设计 | [docs/02-engineering-architecture.md](docs/02-engineering-architecture.md) |
| 学习阅读数据与实践预测 | [docs/03-data-and-forecasting-guide.md](docs/03-data-and-forecasting-guide.md) |
| 建立个人定期预测账本 | [docs/04-fork-and-agent-workflow.md](docs/04-fork-and-agent-workflow.md) |
| 浏览 100 条精彩预测、50 条失误与 180 条未来方向 | [docs/reports/curated-330-compendium.md](docs/reports/curated-330-compendium.md) |
| 阅读完整统计报告与人物画像 | [docs/reports/panoramic-report.md](docs/reports/panoramic-report.md) |
| 查询任一作品的统计数据（CSV） | [datasets/](datasets/README.md) |
| 逐条核对原文引文与证据 | [cases/](cases/README.md) |

<details>
<summary><b>判定标准</b></summary>

每条预测归入以下五类之一，类别互斥：

| 类别 | 定义 | 全库条数 |
| :--- | :--- | ---: |
| 正确 | 在声明的口径与观察窗口内，主要可检验结果已发生 | 1,686 |
| 趋势符合 | 持续的客观数据支持预测方向，但终点尚未到达 | 971 |
| 部分符合 | 复合命题中分项有对有错，或不同合理口径结论不同 | 1,714 |
| 错误 | 主要可检验结果与预测相反，或期限届满未发生 | 689 |
| 暂无法判断 | 期限未到、前提未触发或缺乏可靠公开证据 | 3,070 |

- 抽取阶段剔除比喻、格言、政策建议、历史复述等非预测语句，共 2,553 条。
- "部分符合"不折算为 0.5 分；"趋势符合"不计入终局命中。
- 证据不足时保留"暂无法判断"，不强行判定。
- 每条判定均绑定公开证据并保存文件哈希，可独立复核。

</details>

<details>
<summary><b>本地运行</b></summary>

仅需 Python 3.11+，无第三方依赖：

```bash
python3 -m unittest discover -s toolkit/tests -v
python3 toolkit/pipeline.py --case cases/lky-guantianxia check
python3 toolkit/periodic_tracker.py --case my-forecasts digest
```

</details>

---

## 研究局限与许可

- **回顾性研究**：全部结果均为事后核验，选书受文本可得性与研究者偏好影响，不构成公平的预测竞赛排名。
- **非独立性**：同一作品中的多条预测可能共享同一事件簇，不宜作为独立样本进行显著性检验。
- **版权**：仓库不含任何原书全文，仅保留必要的短引文与公开证据快照，原文版权归原作者所有。
- **许可**：代码采用 [MIT](LICENSE)，研究报告与数据集采用 [CC BY 4.0](LICENSE)。

**谨此致谢纳特·西尔弗的《信号与噪音》，它是本项目的思想起点。**
