# 实证案例档案馆（`cases/`）

本目录收录了全部已通过 `toolkit/pipeline.py check` 字节级哈希与结构校验的 **134 个案例目录**（去重早期合并版本后对应全景报告中的 **132 部独立作品**）。

每个案例目录彼此完全独立，不共享全局变量或外部数据库，也**绝不包含受版权保护的原书全文**。

---

## 1. 单个案例的标准目录结构

以 [`cases/lky-guantianxia/`](lky-guantianxia/) 或 [`cases/zakaria-post-american-world-v5/`](zakaria-post-american-world-v5/) 为例：

```text
cases/<case-slug>/
├── config.json                  # 书名、作者、出版年代理、证据截止日 (cutoff) 与规则版本
├── REPORT-manual-zh.md          # 中文深度复盘报告（或 REPORT-audit-zh.md / README.md）
├── data/
│   ├── claims.jsonl             # 逐条原文短引文、位置偏移、消歧展开与五类评估结果
│   ├── evidence.jsonl           # 外部公开证据清单（含 URL、事实时期、口径限制与 SHA-256）
│   └── sources/                 # 本地归档的公开统计页面/报告片段（供离线哈希核验）
├── output/
│   ├── report.md                # 由 pipeline.py 自动生成的完整逐条核验报告
│   ├── claims.csv               # 便于表格软件筛选的逐条预测明细表
│   └── summary.json             # 机器可读的五类统计、可判定覆盖率与未决原因分布
└── audit/                       # 历史复核轨迹、改判记录与质量门校验日志（如有）
```

---

## 2. 推荐阅读入口（代表性高光案例）

如果你第一次浏览案例库，推荐从以下几组跨领域标杆案例入手：

- **地缘政治与战略底盘**
  - 法里德·扎卡利亚《后美国世界》(2008)：[`zakaria-post-american-world-v5`](zakaria-post-american-world-v5/)（83 条可判定，严格胜率 59.0%，错误率 6.0%）
  - 罗伯特·卡普兰《地理的复仇》(2012)：[`kaplan-revenge-of-geography-v5`](kaplan-revenge-of-geography-v5/)（131 条可判定，方向命中 69.5%，错误率 6.1%）
  - 李光耀《李光耀观天下》(2013)：[`lky-guantianxia`](lky-guantianxia/)（170 条可判定，方向命中 62.4%）
  - 埃德蒙·伯克《法国革命论》(1790)：[`burke-reflections-on-the-revolution-in-france-v5`](burke-reflections-on-the-revolution-in-france-v5/)（百年长窗 31 条可判定，0 错误）
- **硬约束账本与专业智库**
  - 英国政府科学办公室《智能基础设施 2055》(2006)：[`curry-intelligent-infrastructure-futures-2055-v5`](curry-intelligent-infrastructure-futures-2055-v5/)（20 年检验严格胜率 74.1%）
  - 国际能源署《全球关键矿产展望 2024》：[`iea-global-critical-minerals-outlook-2024-v5`](iea-global-critical-minerals-outlook-2024-v5/)（严格胜率 66.7%，错误率 3.2%）
  - 威廉·斯坦利·杰文斯《煤炭问题》(1866)：[`jevons-coal-question-v5`](jevons-coal-question-v5/)（160 年检验严格胜率 52.8%，提出杰文斯悖论）
- **产业颠覆、互联网与人工智能**
  - 克莱顿·克里斯坦森《创新者的窘境》(1997)：[`christensen-innovators-dilemma-v5`](christensen-innovators-dilemma-v5/)
  - 凯文·凯利《失控》(1994)：[`kelly-out-of-control-v5`](kelly-out-of-control-v5/)（230 条可判定，32 年错误率仅 5.7%）
  - 尼克·博斯特罗姆《超级智能》(2014)：[`bostrom-superintelligence-v5`](bostrom-superintelligence-v5/)（44 条可判定，0 错误）
- **全书横向指标检索**：请直接配合 [`../datasets/all_cases_summary.csv`](../datasets/all_cases_summary.csv) 按 `slug` 列快速定位任意一本书。
