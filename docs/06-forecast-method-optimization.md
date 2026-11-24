# 数据驱动的预测方法优化：学术模型拟合、反事实寻优与通用 Agent（MCP / Skill）接入指南

在完成对 **132 部著作、8,130 条可评分预测（5,060 条已明确判定 + 2,553 条非预测对照）** 的逐条核验后，一个核心的科学问题随之浮现：

> **我们能否超越定性的经验总结，直接以这 10,683 条历史样本及其发布时点（$t_0$）的宏观历史数据为训练集，吸收现代预测科学（Forecasting Science）的学术成果，拟合出一套可量化评估、可反事实寻优预测方法的数学引擎，并封装为标准 MCP 与 Agent Skill 供任何智能体终端随时调用？**

本文档完整阐述 **Forecast Lab 预测方法优化引擎**（[`toolkit/forecast_optimizer.py`](../toolkit/forecast_optimizer.py) + [`toolkit/forecast_mcp.py`](../toolkit/forecast_mcp.py) + [`.agents/skills/forecast-optimizer/SKILL.md`](../.agents/skills/forecast-optimizer/SKILL.md)）的学术理论底座、防穿越特征工程、样本外模型竞赛结果与多终端接入方法。

---

## 一、学术文献底座：现代预测科学如何优化判断型预测？

不同于高频时间序列外推，地缘、宏观、产业与技术变革属于典型的**判断型与结构型预测（Judgmental & Structural Forecasting）**。我们将五个领域的经典学术方法融合为统一的可计算框架：

| 学术支柱 | 代表性文献 | 解决本库什么核心痛点？ | 在本引擎中的数学落地 |
| :--- | :--- | :--- | :--- |
| **1. 参考类预测与层级经验贝叶斯收缩** | Kahneman & Tversky (1979); Flyvbjerg (2006); Efron & Morris (1975); Gelman & Hill (2007) | 细分维度（领域 × 跨度档 × 作者类型 × 显隐期限）样本量悬殊，直接查表在小样本格子里严重过拟合 | 三层 Dirichlet-Multinomial 部分池化（`HierarchicalEmpiricalBayes`），向高层参考类自动收缩 |
| **2. 右删失生存风险分解（Right-Censoring Hazard）** | Cox (1972); Kalbfleisch & Prentice (2002) | 近期作品未定率高达 60%–90%，忽略“尚未到期/前提未触发”直接做分类会严重扭曲胜率估计 | 链式概率分解：$P(Y_5 \mid X) = P(\text{Decidable} \mid X) \cdot P(Y_4 \mid \text{Decidable}, X)$ |
| **3. 基于特征的预测方法元学习（FFORMA）** | Montero-Manso, Athanasopoulos, Hyndman & Talagala (2020, *IJF* M4 亚军框架) | 没有“万能方法”，最优透镜高度依赖问题特征与时间窗口的非线互作用 | 二阶牛顿直方图梯度提升树（`HistXGBoost`），自动捕获“显式年份 × 有无约束账本”等高阶交互 |
| **4. 分层因果效应剥离（CMH 混杂控制）** | Cochran (1954); Mantel & Haenszel (1959); Imbens & Rubin (2015) | 观察性书库中“时代/时间窗”与“方法”高度混杂（如智库集中在近 10 年，乌托邦集中在百年前） | 在相同 `(时间跨度档 × 显隐期限)` 层内计算 Cochran-Mantel-Haenszel 加权净效应，剥离时间红利 |
| **5. 对数线性意见池、温度校准与严格恰当评分规则** | Bates & Granger (1969); Genest & Zidek (1986); Gneiting & Raftery (2007, *JASA*); Satopää, Tetlock et al. (2014); Halawi et al. (2024, *NeurIPS*) | 单一模型或原始 LLM 口头概率常出现过度自信与分布失真 | 对数线性池化（Log-Linear Opinion Pool）+ 样本外温度缩放 $T$，以多分类 Brier、LogLoss、序数 RPS 与校准误差 ECE 联合寻优 |
| **6. 跨国历史技术采用曲线与四层摩擦定律** | Comin & Hobijn (2004, 2009 *NBER CHAT*); Bass (1969 *S-Curve*); Paul David (1990 *Dynamo Paradox*); Perez (2002) | 评估颠覆性新技术时易陷入“这次不一样”的纯算法速率外推，忽视物理换机与组织重构周转墙 | 12 次历史技术浪潮 Bass $(p,q)$ 扩散反演（`evaluate_tech_differentiation`），分离纯比特层与原子/监管层斜率，联动当下实时瓶颈参数核查 |

---

## 二、严守 $t_0$ 信息边界的训练数据集构建（零事后穿越）

训练预测优化器的最大陷阱是**信息穿越（Look-ahead Leakage）**：绝不能把事后核验阶段生成的评估理由（`assessment.reason`）或事后观察终点当作输入特征。

本引擎从全部 **132 部独立著作** 中精确对齐提取 **10,683 条样本**（8,130 条可评分预测 + 2,553 条非预测对照），所有输入特征 $X_{i, t_0}$ 均严格限定在**预测发布时点 $t_0$ 可知的信息集合**内：

```mermaid
flowchart LR
    subgraph Data["1. 全库对齐训练集 (132 部著作 · 1531–2026)"]
        D1["8,130 条可评分预测\n(5,060 已判定 + 3,070 未定)"]
        D2["2,553 条剔除非预测\n(格言/倡议/静态机制/史实)"]
        D3["t0 宏观历史状态面板\n+ 时点因果滚动基准率"]
    end

    subgraph Models["2. 四路异构基模型 + Stage 0 去噪器"]
        S0["Stage 0: 伪预测去噪器\nP(Forecast | X_t0)"]
        M2["层级经验贝叶斯\n(Dirichlet Partial Pooling)"]
        M4["L2 正则化多分类 GLMM\n(平滑方法与陷阱梯度)"]
        M5["直方图牛顿提升树\n(HistXGBoost 五类直推)"]
        M6["两阶段右删失提升树\nP(可判) × P(四类结局|可判)"]
    end

    subgraph Opt["3. 超学习器校准与反事实寻优"]
        SL["对数线性池化超学习器\nLog-Linear Pool + 温度 T=1.06"]
        CF["反事实策略搜索\n遍历 6 大主透镜 × 反校验 × 承诺硬度\n+ CMH 同层因果净效应校准"]
    end

    Data --> Models --> SL --> CF
```

### 四组严格事前（Ex-Ante）特征族
1. **发布时点 $t_0$ 的宏观历史状态（`hist_*`）与因果滚动先验（`pit_*`）**：
   - 基于经济史与国际关系史客观分期编码 $t_0$ 所处的**统计基础设施成熟度**、**地缘秩序转型压力**、**大宗稀缺/高通胀冲击期**（如 1798、1920、1972、2022）、**技术范式狂热期**（如 1900 电气航空、1998 互联网、2023–2026 生成式 AI）以及**前 10 年全球人均实际 GDP 增速**；
   - **严格因果滚动先验（Point-in-Time Expanding Prior）**：对出版于 $t_0$ 的作品，仅聚合出版于 $t \le t_0 - 10$ 的历史作品胜率与错误率，彻底杜绝跨时代未来信息泄漏。
2. **命题承诺与颗粒度结构（`s_*`）**：显式期限 vs 隐含窗口、解析出的目标跨度年数 $\tau$、是否包含可测统计指标与权威数据源、是否包含“超越/取代”比较级、复合捆绑连词、刺猬式绝对化词 vs 狐狸式概率边界词。
3. **六大信号方法透镜（`m_*`）**：从原文与抽取阶段推理依据（排除核验阶段记录）识别 **约束账本、制度激励、地缘底盘、功能扩散、风险边界、条件分支**。
4. **理论驱动高阶交互项（`ix_*`）**：显式编码 `显式期限 × 有无硬账本`、`技术狂热期 × 刺猬绝对词`、`超越断言 × 显式年份 × 无账本` 等关键交互结构。

---

## 三、样本外按著作分组五折交叉验证（Out-of-Book 5-Fold CV）结果

由于同一本书内的预测共享作者风格、出版年份与相关历史背景，随机切分样本会导致严重的同书泄漏。我们采用严格的 **按著作 `case_slug` 分组五折交叉验证**（测试集中的整本书在训练阶段完全不可见），在全部 8,130 条预测与 5,060 条已判定子集上评测 8 组模型（完整机器可读数据见 [`datasets/optimization_benchmark.json`](../datasets/optimization_benchmark.json)）：

| 模型架构 | 5 类 Brier ↓ | 5 类 LogLoss ↓ | 未定校准误差 ECE ↓ | 已判定 4 类 Brier ↓ | 已判定 4 类 LogLoss ↓ | 序数 RPS ↓ | 方向命中 ECE ↓ |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `M0` 全局边际均匀先验 | 0.7576 | 1.5021 | 7.40% | 0.7215 | 1.3265 | 0.1970 | — |
| `M1` 静态跨度档 × 显隐期限查表 | 0.7537 | 1.4756 | 11.22% | 0.7128 | 1.2827 | 0.1913 | 7.04% |
| `M2` 三层经验贝叶斯部分池化（HEB） | 0.7297 | 1.4710 | 8.23% | 0.7444 | 1.3605 | 0.1991 | 6.57% |
| `M3` 正则化 GLMM（不含历史状态与方法透镜） | 0.6999 | 1.3854 | 6.64% | 0.7207 | 1.3009 | 0.1925 | 4.70% |
| `M4` 正则化 GLMM（含 $t_0$ 历史状态 + 透镜 + 陷阱） | 0.6855 | 1.3580 | 4.27% | 0.7178 | 1.2962 | 0.1924 | 3.70% |
| `M5` 二阶牛顿直方图提升树（`HistXGBoost` 五类） | **0.6684** | **1.3198** | 3.32% | 0.7033 | 1.2684 | 0.1891 | 1.84% |
| `M6` 两阶段右删失风险提升树（`TwoStage HistXGBoost`） | 0.6706 | 1.3222 | **3.28%** | 0.7017 | 1.2690 | 0.1887 | 4.12% |
| **`M7` 温度校准对数线性超学习器（生产采用）** | **0.6701** | **1.3215** | 4.41% | **0.7002** | **1.2637** | **0.1884** | **1.79%** |

### 核心实证结论
1. **$t_0$ 宏观历史背景与方法特征带来显著样本外增益**：对比消融基线 `M3` 与完整特征线性模型 `M4`，引入发布时点宏观历史状态、因果滚动先验与方法透镜后，5 类 Brier 下降 `0.0144`、LogLoss 下降 `0.0274`，未定率校准误差从 `6.64%` 压降至 `4.27%`。
2. **非线性交互树显著跑赢静态查表与线性可加模型**：`HistXGBoost` 将 5 类 Brier 从静态查表的 `0.7537` 大幅降至 `0.6684`（相对改善 **11.3%**），验证了预测成败高度取决于“期限硬度 × 账本约束 × 历史周期位置”的非线性组合。
3. **对数线性池化超学习器（`M7`）在已判定命题上取得最佳综合精度与校准度**：融合权重 `(HEB=0.05, GLMM=0.19, DirectXGB=0.43, TwoStageXGB=0.33, T=1.06)` 在 5,060 条已判定样本上创下最低 **4 类 Brier (`0.7002`)、最低 LogLoss (`1.2637`)、最低序数 RPS (`0.1884`) 与最低方向校准误差 (`1.79%`)**，同时保留了 `GLMM` 对单一方法与陷阱改动的平滑反事实敏感度。

### 控制时间跨度与显隐期限后的 CMH 同层净效应（$n=5,060$）

通过 Cochran-Mantel-Haenszel 分层检验锁死同一 `(时间跨度分档 × 显隐期限)` 后，数据直接量化了不同方法与失误模式的真实边际影响：

| 特征 / 交互模式 | 命中样本数 | 同层 $\Delta$严格胜率 | 同层 $\Delta$错误率 | 方法论含义 |
| :--- | ---: | ---: | ---: | :--- |
| **有硬账本支撑的显式期限** (`ix_anchored_explicit`) | 228 | **`+7.42pp`** | **`-2.94pp`** | 相比无账本拍脑袋给日期（`-7.42pp` / `+2.94pp`），严格胜率正负相差近 **15 个百分点**！ |
| **地缘底盘与权力均衡法** (`m_geopolitical_chassis`) | 316 | **`+5.31pp`** | `+0.02pp` | 长周期战略与秩序推演最稳健的主透镜（方向命中同步提升 `+6.08pp`） |
| **约束账本法** (`m_constraint_ledger`) | 315 | **`+4.62pp`** | `+2.46pp` | 显著提高终局严格兑现率，但需配“替代技术跃迁”反校验以防单点硬数字失误 |
| **制度与激励结构法** (`m_institutional_incentive`) | 218 | **`+3.86pp`** | **`0.00pp`** | 拆解否决权与在位者毛利包袱，稳步提升严格胜率且不放大错误率 |
| **技术功能扩散链法** (`m_functional_diffusion`) | 344 | **`+3.79pp`** | **`-4.70pp`** | 押功能不押单一外观，在提升严格胜率的同时大幅压低错误率 |
| **多情景条件分支法** (`m_conditional_scenario`) | 1,300 | `-7.02pp` | **`-2.28pp`** | 牺牲单点豪赌胜率，换取更低的硬翻车风险与更高的部分/情景覆盖韧性 |
| **无账本硬数字外推** (`s_unanchored_hard_number`) | 121 | **`-8.73pp`** | **`+2.95pp`** | 拍脑袋给百分比/翻倍速率导致严格胜率与方向命中双双跳水 |
| **阶段顺风单调速率外推** (`s_linear_rate_extrapolation`) | 17 | **`-9.34pp`** | **`+8.80pp`** | 将短期斜率外推为指数直线，错误率急剧膨胀 |
| **无账本“超越/取代”定时断言** (`ix_surpass_explicit_no_ledger`) | 91 | **`-5.45pp`** | **`+7.00pp`** | 典型如“某年某国/某技术总量超越/彻底取代在位者”，翻车率高企 |
| **多目标复合捆绑承诺** (`s_compound_claim`) | 340 | **`-6.64pp`** | `+0.78pp` | 把多个目标绑在同一句承诺里，分项一成一败即跌落为“部分符合” |

---

## 四、评估新技术“这次是否不一样”：历史同构扩散曲线 × 当下实时瓶颈校准

针对新技术预测的核心痛点——**“纯语言结构规则不懂当下新事实，如何判断一项颠覆性技术到底是不是‘这次不一样’？”**——我们在 [`datasets/historical_tech_diffusion_atlas.json`](../datasets/historical_tech_diffusion_atlas.json) 中结构化收录了 1882–2025 年 **12 次代表性技术扩散浪潮**，通过 `evaluate_tech_differentiation` 实现定量双校准：

1. **四层摩擦定位与存量/增量分离**：
   - 自动将命题归入 **第 1 层纯比特消费协议**（`5%→50%` 耗时 `2.8–5.5 年`）、**第 2 层消费级硬件替换**（新车/新机 `4.8–6.5 年` vs 保有量 `14.5 年`）、**第 3 层企业核心工作流重塑**（公有云 `7.5–9.5 年`、ERP `9.0–11.5 年`，受制于保罗·大卫“发电机悖论”）或 **第 4 层重资产/电网/具身硬件/零容错强监管**（工业机器人 `14–22 年`、电网发电存量 `22 年`、L4 自动驾驶/临床新药 `14–20 年`）。
2. **Bass (1969) S 曲线解析反演测算透支倍数**：
   $$t(s) = \frac{1}{p+q}\ln\left(\frac{1 + \frac{q}{p}s}{1-s}\right), \qquad \Delta t_{\text{hist}}(s_0 \to s_1) = \gamma_{\text{stock}} \cdot \big[t(s_1) - t(s_0)\big]$$
   当用户设定的期限 $\Delta t$ 要求比历史同构前辈快 **2.2 倍以上**或击穿物理折旧周转底线时，自动触发 `this_time_is_different_speed_overreach` 警报，并输出 `1.0x–1.5x` 校准合理渗透率区间。
3. **实时瓶颈参数核查清单（`realtime_parameters_to_fetch_now`）**：
   历史库负责给出**结构骨架斜率**，同时输出当前必须联网核查的 **3 项当下实时行业指标**（如区域电网并网排队月数、POC 转正式年框留存率、人形整机 BOM 静态回收期），用今天的一手数据修正历史斜率。

---

## 五、如何在任何 AI Agent 终端一键接入？（复制文字即插即用）

整个优化系统**仅依赖 Python 3.11+ 标准库**，无需安装任何 `pip` 依赖包、无需外部 API Key，预训练参数包 [`datasets/forecast_optimizer_model.json`](../datasets/forecast_optimizer_model.json) 毫秒级加载。

### 最简方式：复制下面这段话发给任何 AI Agent 终端（自动拉取并接入 MCP / Skill）

无论你使用的是 **Claude Code、Antigravity、Cursor、Codex CLI、Windsurf、Cline 还是 OpenCode**，哪怕当前在空白目录或其他项目目录，直接复制以下整段文字发给你的 Agent 即可完成接入与预测优化：

```text
请帮我接入开源的 Forecast Lab 数据驱动预测方法优化器（仓库：https://github.com/nebulonvc/forecast-lab.git ，纯 Python 3.11+ 标准库零依赖）：
1. 若当前目录不在 forecast-lab 仓库内，请先执行 `test -d ~/.forecast-lab || git clone --depth 1 https://github.com/nebulonvc/forecast-lab.git ~/.forecast-lab`（若已在仓库内则直接使用当前目录），并阅读 `.agents/skills/forecast-optimizer/SKILL.md`；若当前终端支持配置本地 MCP Server，可将 `python3 <仓库路径>/toolkit/forecast_mcp.py` 挂载为 `forecast-lab-optimizer`。
2. 每当我提出预测想法（尤其是评估 AI、机器人、能源、新产业“这次是否不一样”）时，你必须先调用 MCP 工具 `optimize_forecast` 与 `evaluate_tech_differentiation`（或运行 `python3 <仓库路径>/toolkit/forecast_optimizer.py optimize --statement "<预测草案>" --domain "<领域>"`）：先用 8,130 条历史预测 Super-Learner 与 150 年 12 次技术浪潮 Bass 扩散曲线给“历史同构骨架斜率”，再根据工具列出的 `realtime_parameters_to_fetch_now` 联网查询当下的真实行业瓶颈数据（如并网排期、BOM回本周期、付费留存率）修正斜率。
3. 【强制交付规范——必须把预测方法写出来】：你最终输出给我的每一条预测，绝不允许只给一句结论或拍脑袋概率，必须完整写出：
   (a) 可核验预测承诺（主体 + 对象 + 量词 + 含分母可测指标【严分增量流量 vs 存量保有量】+ 唯一权威结算数据源 + 明确期限 + 排除边界）；
   (b) 显式预测方法与四步推导链（写明选用哪套主方法原型、代入当下实时瓶颈数据的四步推导计算过程、历史同构技术校准结论、反校验透镜对冲逻辑与承诺硬度依据）；
   (c) 8,130 库样本外校准先验概率（优化前 vs 优化后的严格胜率、方向命中率、部分符合率、错误风险对比）；
   (d) 2–3 个季度/半年度可查的领先观测指标，以及事件×机制×时间三轴明确证伪红线。
准备好后请回复我：“Forecast Lab 预测方法优化与历史同构校准引擎已就绪，请告诉我你的预测想法。”
```

---

### 方式一：通过标准 MCP Server 接入（适用于任何支持 MCP 的 Agent 终端）

仓库根目录已内置标准 [`.mcp.json`](../.mcp.json)：

```json
{
  "mcpServers": {
    "forecast-lab-optimizer": {
      "command": "python3",
      "args": ["toolkit/forecast_mcp.py"]
    }
  }
}
```

- **Claude Code / Antigravity / Cursor**：在仓库根目录打开终端或 IDE 时会自动识别 `.mcp.json` 并挂载 `forecast-lab-optimizer` 服务。
- **Codex CLI / Windsurf / Cline / Zed / 全局挂载**：在对应客户端的 MCP 配置文件中添加（将路径替换为本地仓库绝对路径）：
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

挂载后，Agent 即可直接调用 **7 个标准化工具（Tools）**、**4 个只读资源（Resources）** 与 **2 个引导模板（Prompts）**：
1. `optimize_forecast`：输入任意粗糙预测想法，返回可操作化评分、噪音陷阱诊断、新技术历史同构校准、优化前后五类校准概率对比、最优「主透镜 + 四步推导链 + 反校验透镜 + 承诺硬度」与同领域历史正反先例；
2. `evaluate_tech_differentiation`：针对新技术评估执行 150 年 Bass 扩散曲线与四层物理/制度摩擦同构测试，输出合理渗透区间与必查当下实时参数清单；
3. `query_reference_class`：按领域与时间跨度查询三层经验贝叶斯基准率与同领域标杆著作；
4. `bayesian_update_forecast`：基于新增支持/反面证据，按事件轴、机制轴、时间轴执行阻尼对数赔率更新并检测确认偏误；
5. `audit_forecast_ledger`：一键体检 `my-forecasts/` 全部在册预测的方法质量；
6. `register_optimized_forecast`：将优化后的预测卡连同显式推导链与校准先验概率原子写入账本并通过 `pipeline.py check` 校验；
7. `get_optimizer_benchmark`：读取全库交叉验证指标与特征增益。

### 方式二：通过通用 Agent Skill 接入（零 MCP 配置也能即插即用）

仓库内置了标准技能说明文件 [`.agents/skills/forecast-optimizer/SKILL.md`](../.agents/skills/forecast-optimizer/SKILL.md) 及协作规范 [`AGENTS.md`](../AGENTS.md)。即使在不启用 MCP 的终端 Agent 中，只需对 Agent 说：

> 💬 **示例指令：**
> “我想预测：未来三年人形机器人在汽车制造厂会取代大量装配工人。请调用 `forecast-optimizer` 帮我做一次数据驱动的预测方法优化，看看直接这么写翻车率有多高、踩了哪些历史陷阱、应该换哪套方法透镜和口径，再帮我收敛成可冻结入库的预测卡。”

### 方式三：命令行直接运行（CLI）

```bash
# 1. 优化单条预测草案（默认输出结构化 Markdown 报告，加 --format json 输出机器可读 JSON）
python3 toolkit/forecast_optimizer.py optimize \
  --statement "到2028年底，AI将彻底取代50%以上的软件工程师工作，代码编写成本每年减半。" \
  --domain "AI"

# 2. 查询特定领域与时间跨度的经验贝叶斯基准率与历史先例
python3 toolkit/forecast_optimizer.py reference-class --domain "人口、能源、资源与生态" --horizon-years 5

# 3. 批量体检个人预测账本
python3 toolkit/forecast_optimizer.py audit-ledger --case my-forecasts

# 4. 自检 MCP 协议握手与工具调用
python3 toolkit/forecast_mcp.py --self-test

# 5. 从全库 132 部著作重新完整跑一遍五折分组交叉验证并重生成模型文件
python3 toolkit/forecast_optimizer.py train
```
