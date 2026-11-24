## 新增书籍案例 PR 清单（Community Book Contribution）

感谢向 **Forecast Lab（信号与噪音）** 贡献实证案例！提交 PR 前请确认已完成以下检查。

### 1. 书籍元数据
- **案例目录**：`cases/<slug>/`
- **书名 / 作者 / 出版年**：
- **所属标准领域**：
- **所属标准作者类型**：
- **执行模式**：`[ ] 路径 A（自有 Agent 原生）` / `[ ] 路径 B（自有 API 并发）`

### 2. 自动化门禁与数据库同步（必填）
- [ ] 已运行 `python3 toolkit/contribute_book.py sync-database --case cases/<slug>`，同步更新了 `datasets/all_cases_summary.csv`、`datasets/same_tier_ranking.csv` 与 `docs/05-same-tier-ranking.md`
- [ ] 已运行 `python3 toolkit/contribute_book.py pr-check --case cases/<slug>` 并返回 `passed`
- [ ] 已运行 `python3 -m unittest discover -s toolkit/tests -v` 且全部测试通过

### 3. 版权与隐私安全红线（必填）
- [ ] 确认未提交任何原书全文（`.txt` / `.pdf` / `.epub` 等，原书仅保留在本地被忽略的 `input/` 目录）
- [ ] 确认未提交任何 API Key 或本机隐私路径（`/Users/...`、`/home/...`）
- [ ] 确认所有已判定预测均绑定了真实公开网页存档（`data/sources/`）及通过校验的 SHA-256
