---
name: book-contributor
description: 协助用户用自有 Agent（零额外 API 费用）或自有 API（DeepSeek / OpenAI 兼容 + Exa）按《信号与噪音》v5 协议拆解新书、完成正反双向一手搜证与六维语义复核，并同步更新数据库总表与通过 PR 门禁。
---

# Book Contributor（社区共建书籍拆解与 PR 入库）技能指南

当用户希望用自己的 Agent 或 API 跑完一本书（或长篇报告）并提交 PR 合入 Forecast Lab 主数据库时，严格遵循本流程。

---

## 一、开场确认 5 项信息 + 执行路径

收到用户请求后，先确认：
1. **书名**（`--book`）与 **作者**（`--author`）；
2. **初版代理年份**（`--publication-year`）；
3. **所属七大标准领域之一**（`地缘政治与国际秩序` / `宏观经济、金融与市场` / `科技、商业与产业颠覆` / `AI与奇点前沿` / `人口、能源、资源与生态` / `社会结构、制度、文化与教育` / `科幻推演与乌托邦/反乌托邦`）；
4. **所属六类标准作者类型之一**（`国际机构与政府智库` / `政治家与战略实务者` / `地缘与社科政治学者` / `经济学家与金融投资人` / `科技商业思想家与产业实践者` / `古典思想家与科幻/乌托邦作家`）；
5. **原书 TXT 路径**与**执行路径选择**：
   - **路径 A（自有 Agent 原生模式，推荐零费用）**：由当前 Agent（及并行子智能体）逐块阅读并利用自带联网搜索完成核查；
   - **路径 B（自有 API 并发模式）**：用户已配置 `BOOKPRED_DEEPSEEK_API_KEY`（或 `BOOKPRED_LLM_BASE_URL` + `BOOKPRED_LLM_API_KEY`）与 `EXA_API_KEY`。

> **版权红线**：原书 TXT 必须放入 `cases/<slug>/input/`（已被 `.gitignore` 忽略）或仓库外，严禁将完整原书提交进 Git。

---

## 二、标准执行流程

### 1. 初始化案例
```bash
python3 toolkit/contribute_book.py init \
  --case cases/<slug> --book "<书名>" --author "<作者>" \
  --publication-year <年份> --domain "<领域>" --author-type "<作者类型>" \
  --execution-mode <agent-native-v5 或 api-pipeline-v5>
```

### 2. 抽取阶段
- **路径 A**：
  1. 运行 `python3 toolkit/contribute_book.py chunk-txt --case cases/<slug> --txt <txt路径>`。
  2. 读取 `cases/<slug>/output/txt_import/prompt_v5.txt` 与 `chunks.jsonl`，对**每一个** chunk_id 写出 `chunk_proposals/<chunk_id>.json`（无预测的块必须写 `{"id":"...","predictions":[]}`，绝不漏读）。
  3. 严守逐字 `quote`、7 类非预测筛除（比喻/格言/倡议/仪式/历史/纯机制/反事实）与代指逐字依据展开。
  4. 运行 `python3 toolkit/contribute_book.py import-extractions --case cases/<slug> --txt <txt路径> --proposals cases/<slug>/output/txt_import/chunk_proposals`（自动对齐、去噪并裁剪 `context` 保护版权）。
- **路径 B**：
  1. 运行 `python3 toolkit/prepare_book.py --case cases/<slug> txt <txt路径> --apply`（支持 `--api-base` 与 `--model`）。
  2. 立即运行 `python3 toolkit/contribute_book.py trim-contexts --case cases/<slug>` 裁剪上下文。

### 3. 双向搜证与六维复核阶段
- **路径 A**：
  1. 运行 `python3 toolkit/contribute_book.py export-verify-tasks --case cases/<slug>`。
  2. 对 `output/verify_tasks.jsonl` 每条预测**成对检索支持证据与反面证据**（优先官方统计、央行、IEA/OECD/世行、财报与学术一手出处），抓取完整公开正文写入 `evidence_raw.jsonl`。
  3. 按 `toolkit/METHOD.md` 五类互斥结论与六维逻辑门（对象匹配、条件逻辑、时间对应、证据支持、反证处理、结论逻辑）自查后写出 `assessments.jsonl`（明确趋势但终点未到使用 `verdict="部分符合"` + `trend_aligned=true`）。
  4. 运行 `python3 toolkit/contribute_book.py apply-assessments --case cases/<slug> --assessments <assessments.jsonl> --evidence-raw <evidence_raw.jsonl>`。
- **路径 B**：
  1. 运行 `python3 toolkit/verify_prediction.py --case cases/<slug> --all-forecasts`（支持 `--api-base` 与 `--model`）。
  2. 运行 `python3 toolkit/contribute_book.py import-verify --case cases/<slug>`。

### 4. 数据库同步与 PR 门禁验收（必跑）
```bash
python3 toolkit/contribute_book.py sync-database --case cases/<slug>
python3 toolkit/contribute_book.py pr-check --case cases/<slug>
python3 -m unittest discover -s toolkit/tests -v
```
确认 `pr-check` 与全量单测全部通过，且 `git status` 无原书或密钥文件后，即可协助用户提交 PR！
