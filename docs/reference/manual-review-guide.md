# 人工复刻 DeepSeek 书籍审读管线

写于 2026-11-19。对照的默认分支是 `origin/main` 提交 `ccf9d45ac66adbd5e4074b3c927eb0243b6feb95`（2026-11-17 01:45:13 UTC，合并 PR #32，只加入预测流程文档）。同日 `git diff 85e6da1dc0f185830a6ea9037d731fd39a27411e origin/main -- toolkit/` 为空，因此下面的程序行为同时是该提交与当前 `toolkit/` 的行为。以后 `toolkit/` 若有新提交，以新代码为准，并在验收里写明提交号。

本文只描述方法和交接。它不新增预测，不修改 `cases/`，也不生成一份新的剩余书队列。

## 1. 要复刻的是哪条管线

原管线用 DeepSeek 阅读 TXT 分块、抽取预测，再对可核验候选做检索计划、选源、评估和语义复核，最后用确定性代码校验并写报告。人工复刻只替换模型调用：由阅读者逐块读正文，写出模型本应写出的 JSON。分块、引文对齐、非预测筛除、归属降级、重叠去重、ID、证据哈希和 `pipeline.py check` 都调用仓库代码，不另写一套。

不要调用 DeepSeek。下列命令会请求模型，人工复刻时不要执行：

```bash
python3 toolkit/prepare_book.py --case cases/<slug> txt book.txt
python3 toolkit/prepare_book.py --case cases/<slug> txt book.txt --apply
python3 toolkit/run_parallel.py --case cases/<slug>
python3 toolkit/verify_prediction.py --case cases/<slug> --all-forecasts
```

`verify_prediction.py` 的 `--prepare-only` 也不要拿来代替阅读。检索可以用环境里真实可用的搜索和抓取；用了什么就写什么。抓不到正文时，不能把记忆、搜索摘要或「模型说已经读过」写成证据。

## 2. 2026-11-19 已核实的仓库状态

### 2.1 代码与测试

- 抽取提示词是 [toolkit/prepare_book.py](../../toolkit/prepare_book.py) 的 `DISCOVER_PROMPT_V5`。当日正文 sha256 为 `b7aed8488b66ed9f74ff0e27d20830e7214ca26198c3f973a0609e635d689cc4`。抽查 `brzezinski-strategic-vision-v5` 已保存的 `prompt_sha256` 与此相同。
- 研究规则在 [toolkit/METHOD.md](../../toolkit/METHOD.md)。冲突见第 3 节。
- `python3 -m unittest discover -s toolkit/tests` 当日跑完为 209 项，结果 `OK`。这个数字不是程序里的常量。接手时重跑，并记录实际数量。
- 只读抽查 `pipeline.py check`：`brzezinski-strategic-vision-v5`（33 条主张、20 条证据）、`huntington-third-wave-v5`（71、52）、`oecd-governing-with-ai-v5`（5、3）均为 `OK`。没有对全部案例重跑 check。

### 2.2 已合并案例

`cases/` 下有 97 个 `*-v5` 目录，另有 5 个非 v5 案例：`america-against-america`、`america-full-v4`、`clash-of-civilizations-v4`、`lky-guantianxia`、`zero-to-one`。

2026-11-17 合并的人工复刻批次是 PR [#27](https://github.com/nebulonvc/forecast-lab/pull/27)、[#28](https://github.com/nebulonvc/forecast-lab/pull/28)、[#30](https://github.com/nebulonvc/forecast-lab/pull/30)、[#31](https://github.com/nebulonvc/forecast-lab/pull/31)、[#29](https://github.com/nebulonvc/forecast-lab/pull/29)。按合并结果计目录：20 + 20 + 18 + 20 + 4 = 82。这 82 个目录的 `data/evidence.jsonl` 都非空，`execution_mode` 都是 `prepare_book-txt v5 (manual model replacement) + manual verify`，`cutoff` 都是 `2026-11-15`，`rules_version` 都是 `simple-v3-trend-four-class`。

另外 15 个 v5 目录的 `data/evidence.jsonl` 为空，例如 `allison-destined-for-war-v5`、`fukuyama-end-of-history-v5`、`soros-alchemy-of-finance-v5`。这 15 本的 `data/claims.jsonl` 里也都没有 `assessment`。`allison-destined-for-war-v5` 当日 `check` 为 `OK: 92 claims; 0 verified evidence records`，是因为主张上没有已接受评估。它们的核验摘要在 `output/verify-final/` 一类目录，没有写回主张。新的人工复刻要把评估写入主张；有计分结论时不能沿用空证据。

82 个目录共有的路径是：

- `config.json`
- `REPORT-manual-zh.md`
- `audit/manual_review_2026-11-15.py`
- `data/claims.jsonl`
- `data/evidence.jsonl`
- `data/sources/*`
- `output/manual-final/results.manual.jsonl`
- `output/manual-final/summary.json`
- `output/next_batch.json`
- `output/summary.json`

`output/report.md` 与 `output/claims.csv` 在 81 个目录里有。`oecd-governing-with-ai-v5` 没有这两个生成文件；[预测流程说明](../reports/case-inspired-process.md) 已记录这一限度。不要为了补齐它而重跑报告。当时简报写的「7 文件格式」没有列出文件名，不能把这句当成目录规范。

77 个已合并人工案例的 `context` 全空。仍有非空 `context` 的是 `christensen-innovators-dilemma-v5`、`huntington-third-wave-v5`、`lee-ai-2041-v5`、`tegmark-life-3-0-v5`、`unesco-reimagining-our-futures-together-v5`。继续剩余书时不要回头修改它们。

### 2.3 报告脚本不在仓库

`pipeline.py report` 会写 `output/report.md`、`output/claims.csv`、`output/summary.json`、`output/next_batch.json`。已合并案例里的 `REPORT-manual-zh.md` 和 `output/manual-final/` 来自当时工作台的 `manual_report.py`。该脚本和它的 6 项引文测试都没有入库。没有这个文件时，必须写明中文人工报告脚本未运行，不能另写一个同名脚本并称它就是当时的 canonical 工具。

## 3. 与 toolkit/METHOD.md 及旧操作说明的冲突

下面各项以 2026-11-19 的源码和已合并案例为准。

| 事项 | 仓库程序 / [toolkit/METHOD.md](../../toolkit/METHOD.md) | 2026-11-16 人工批次实际采用的更严口径 |
|---|---|---|
| 综合分数 | 第 4 节写明趋势符合、部分符合不折成 0.5，也不把「正确 + 趋势符合」称作最终准确率。`pipeline.py` 把 `partial_numeric_weight` 和 `brier` 写成 null。`correct_share_of_decided` 是「正确 / 可判定」。 | worker brief 的展示公式是 `(正确×1 + 趋势符合×0.75 + 部分符合×0.5 + 错误×0) / 可判定`。已合并的 `output/manual-final/summary.json` 含「加权胜率」，那是未入库脚本的输出。 |
| 证据文件 | 正确、部分符合、错误必须引用已核验证据；暂无法判断可以不引用。证据表为空时，`check` 只在没有需要证据的已接受评估时通过。15 个早期 v5 案例证据文件为空，主张上也没有 `assessment`。 | 每条计分主张都要有 `data/sources/` 存档和 `data/evidence.jsonl` 记录。82 个已合并人工案例的证据文件非空。 |
| `context` | `claims_from_results` 把 `context` 写成块前文、正文和后文的拼接。 | 导入后把 `context` 清空。指代依据改由 quote 承担。 |
| 引文模糊匹配 | `align_quote` 在精确和空白归一之后，仍接受比率不低于 0.9 的 fuzzy。 | 人工标准只保留 `exact`、`exact_offset`、`normalized`。fuzzy 要改引文后重跑，不能靠它放过改字。 |
| 自适应检索 | `verify_prediction.py`：初始轮最多 2 轮；结论仍是暂无法判断时，最多再做 `ADAPTIVE_ROUNDS = 3` 轮，每轮最多 `ADAPTIVE_SEARCHES = 5` 条新查询。 | 2026-11-15 的本地操作说明写成「最多 2 轮，外加 1 轮自适应」。该句比当前代码短，不要再按那一句截断。 |
| 复核失败 | 语义复核只允许修订一次。修订后仍不接受时，程序把结论收成暂无法判断，不能保留计分结论。 | 人工复刻执行同一收口。不能为了保留正确或错误而忽略 fail。 |
| 密度 | 方法文件不把密度当准确率目标。 | 2026-11-15 操作说明给过对照区间：中文非虚构大约每块 0.55–1.0 条可核验，英文大约 0.2–0.35。只作事后解释。偏离时说明原因，不增删主张去贴区间。 |
| 抽取收据 | `validate_extraction_provenance` 会比较提示词、配置和来源字段的哈希。`pipeline.py check` 不调用它。 | 抽查已合并案例：清空 `context` 并在抽取后改过 `config.json`，收据与现值不一致，`check` 仍然通过。 |

接手时：确定性步骤用当前代码；计分证据、清空 `context`、拒绝 fuzzy、复核失败不保留计分，按上表右列执行。加权数若出现，只能标成 2026-11-16 的展示公式。不要为贴近准确率、加权数或密度而改主张，也不要编造概率。

## 4. 原书、版本和分块

程序读 TXT。中文 TXT 直接使用。只有 PDF 时，先在仓库外转换：

```bash
pdftotext -enc UTF-8 book.pdf book.txt
```

保留默认版式和换页符。分别记录 PDF 与 TXT 的 sha256。阅读库 `catalog.json` 里的 sha256 对的是目录中的原文件，通常是 PDF 或原始 TXT，不要拿它和 `pdftotext` 产物比。扫描件先看文字层；`pdftotext` 几乎没有字母时，不要把空文本当原书。仓库不带 OCR。环境里若有 OCR，写明工具和版本；没有就停止这本书并报告。

`pipeline.py init` 写入 `book`、`author`、`cutoff`、`publication_year_proxy`、`rules_version=simple-v3-trend-four-class`。82 个已合并人工案例另外写了 `publication_date` 和 `execution_mode`。`check` 不强制这两个字段。新案例仍应写上，并写来源文件的仓库相对路径与 sha256。截止日沿用 `2026-11-15`，除非用户在指令里指定别的日期。

```bash
python3 toolkit/pipeline.py --case cases/<slug> init \
  --book "书名" --author "作者" --publication-year 1907 --cutoff 2026-11-15
python3 toolkit/prepare_book.py --case cases/<slug> txt /仓库外/book.txt --prepare-only
```

第二条只写计划和 `output/txt_import/manifest.json`。`cases/*/output/txt_import/` 与 `cases/*/input/` 已在 `.gitignore` 中。`batch_*.plan.json` 含分块全文，只用于阅读，不放入案例提交，也不放入验收包。

`split_text` 的默认参数是 `chunk_chars=3500`、`context_chars=600`。块在后半段回退到最近的换行、`。`、`！` 或 `？`。ID 从 `txt-00001` 起。每块带前后各 600 字，只用于消解指代，不重复计为另一块。

`matter_spans` 识别的标题是中文的序、前言、致谢、目录、参考文献、附录、后记等，以及 `Chapter N`、`第N章` 这类章节行。英文书经常识别不到前言。识别不到时，整段会留在计划里，必须阅读；需要排除时，用同一组字符区间调用后面的导入函数，并在验收里记录区间和标题。前言、致谢、后记、写作经过和感谢名单不是预测。`--include-front-matter` 会取消自动排除，只在有意保留这些部分时使用。

必须阅读的是 `manifest.json` 里 `ids` 列出的块，也就是计划里的块。被整段跳过的前置或后置块不在这份名单里。名单中的每一块都要有账本记录。账本一条的形式是：

```json
{"id":"txt-00001","predictions":[]}
```

`predictions` 可以是空数组，空数组表示这块已经读过且没有抽出预测。下一块未读时，断点写成下一个 ID。模型或助手说「已经读完全书」不是账本。账本保存抽取 JSON 和被拒原因，不保存块正文。含正文的计划文件留在仓库外或 git 忽略目录。

## 5. 抽取

每一块按 `DISCOVER_PROMPT_V5` 手写一项 `{"id":"txt-000NN","predictions":[...]}`。提示词要求覆盖计划中的每个块。字段以该常量为准，包括：

`quote`、`kind`（`prediction` 或 `unclear`）、`claim_type`（`forecast`、`aphorism`、`normative`、`trivial`、`historical`、`mechanism`、`hypothetical`、`unclear`）、`speaker`、`attribution`、`future_oriented`、`claim`、`changes`、`horizon`、`resolvable`、`confidence`、`expanded_claim`、`reference_resolutions`、`unresolved_references`、`time_text`、`condition_text`、`method`、`method_basis`、`reason`。

`attribution` 只有 `author`、`author_endorsed`、`reported`、`rebutted`。`confidence` 只有 `high`、`medium`、`low`、`unknown`，只反映作者语气。原文没有概率，就不写 70% 这类数字。

抽取范围是作者对出版之后、当时尚未确定、事后可以核验的结果。肯定、可能和真实条件句都算。引文必须说出什么会变化。没有日期的方向判断仍是预测，观察窗口是出版年到截止日，不能自编日期。比喻、规范建议、几乎必然的仪式、出版年之前的历史、没有未来结果的机制、过去反事实和假设战争情景不是预测。拿不准就用 `claim_type=unclear`，且 `kind=unclear`。

`quote` 是正文中的连续片段。可以省去换行、空格和页码行，不能改字、改标点或用省略号拼接。同一句里的独立预测分开记录。同一句里重叠的片段只留一段；这个重叠由 `claims_from_results` 判定，不另做「意思差不多」的人工删除。

英文引文的 `changes` 必须是对齐后原文的逐字子串。中文变化正则不会替英文句子证明它有变化方向。子串检查保留换行，所以跨过 `pdftotext` 换行的短语会对不上，候选会被收成不可核验。选择落在同一行里的短片段。`horizon` 和 `time_text` 同样只抄原文。2026-11-15 的 Kaplan 试抽记录过这个降级，本次没有重跑该书。

`reference_resolutions` 的 `expression` 和 `support_quote` 必须能在正文或所给上下文中逐字找到。找不到的指代写入 `unresolved_references`，并在 `expanded_claim` 中保留 `[指代待确认：…]`。

## 6. 确定性后处理

在仓库根目录调用现有函数。先把 `config.json` 里准备公开的字段写完。`ledger` 是第 4 节的逐块记录，键为块 ID。

```python
import hashlib
import sys
from pathlib import Path

sys.path.insert(0, "toolkit")
import prepare_book as pb
import run_parallel as rp

root = Path("cases/<slug>")
raw, text, codec = pb.decode_text(Path("/仓库外/book.txt"))
raw_sha = hashlib.sha256(raw).hexdigest()
config = rp.read_json(root / "config.json")
spans = pb.matter_spans(text)  # 手工排除英文附文时，换成已记录的区间
chunks = pb.split_text(text)
skipped = {
    c["id"]
    for c in chunks
    if any(a <= c["char_start"] and c["char_end"] <= b for a, b, _ in spans)
}
items = []
for chunk in chunks:
    if chunk["id"] in skipped:
        continue
    kept, rejected = pb.validate_chunk_predictions(ledger[chunk["id"]]["predictions"], chunk)
    if any((p.get("quote_alignment") or {}).get("method") == "fuzzy" for p in kept):
        raise SystemExit(f"fuzzy quote in {chunk['id']}")
    items.append({"id": chunk["id"], "predictions": kept, "rejected_predictions": rejected})
policy = {}
claims = pb.claims_from_results(items, chunks, text, raw_sha, config, spans, policy)
for claim in claims:
    claim["context"] = ""
    extra = claim.get("extraction_v2") or {}
    if "expanded_claim" in extra:
        pb.validate_expansion(extra, claim.get("quote", "") + "\n", normalized=True)
rp.save_jsonl(root / "data/claims.jsonl", claims)
```

这段做的事是：

- `validate_chunk_predictions` 把引文对齐回源文字区间。存进案例的 `quote` 是源文中的精确切片，并带 `source_verification`。精确匹配记 `txt_exact_match`；只折叠空白、页码行和全半角后对上的，记归一化方法。
- `claims_from_results` 排除前后附文、`rebutted`、正则判定的非预测，以及 `future_oriented=false`。`reported`、引号内却标成作者、缺少归属，会降为 `unclear`。重叠规则是较短一段的 80%，或同一句内任意重叠。ID 形如 `txt-<sha10>-<start:09d>-<end:09d>`，`extraction_version=v5`。
- 全部保留下来的候选都写入 `data/claims.jsonl`，包括 `unclear`。不要为了让分母好看而删掉它们。
- 清空 `context` 是人工批次的要求，不是 `claims_from_results` 的默认结果。清空后若 `validate_expansion` 报 `reference_support_not_in_source`，只允许把 `quote` 向前扩成一段更长的连续原文，让所指句子真正包含在引文里，然后重新运行上面的函数。ID 会随偏移变化，由函数重算。不能手改 ID，也不能改写原文。所指内容不在原文里时，留下失败，不要为了通过检查编一个依据。

`policy` 里的排除、降级和去重计数写入验收说明。被拒引文的原因留在块账本。主题接近只作为说明，不作为第二条去重规则，也不要在评估里把不重叠的预测标成 `duplicate`。

第 10 节的建议是：清空 `context` 且配置不再改动之后，用 `pb.extraction_provenance(claim, config, raw_sha)` 重算收据。已合并案例没有这一步。`check` 不检查收据是否匹配。

## 7. 检索、评估和语义复核

对每条 `resolvable=true` 的候选按 [toolkit/verify_prediction.py](../../toolkit/verify_prediction.py) 的阶段手写同等 JSON。[toolkit/decision_policy.py](../../toolkit/decision_policy.py) 的 `DECISION_CONTRACT` 会附加到计划和评估提示词，也附加到 [toolkit/semantic_review.py](../../toolkit/semantic_review.py) 的复核提示词。人工判断使用这些文本，不调用其中的模型客户端。

1. **PLAN。** 先固定 `scope`：对象、条件、可观察口径、可能的反证。初始第 1 轮恰好两条查询，一条 `support`，一条 `counter`。初始轮最多两轮；第 2 轮没有新的必要时，查询可以为空。结论仍是暂无法判断、且缺口写明了具体对象、指标、时期或来源时，最多再做 3 轮自适应检索。每一轮 1 到 5 条新查询，每条有 `strategy`，说明相对以往改变了措辞、指标、时间、来源类型或语言。不能重复已查语句和已读 URL。公开材料不可能补上该缺口时，查询为空，并写明原因。
2. **SELECT。** 最多 8 个 URL，且只能来自本轮搜索实际返回的 URL。保留不利来源。搜索摘要不是已读正文。
3. **ASSESS。** 字段至少包括 `id`、`inclusion`、`verdict`、`basis`、`scope`、`reason`、`limitation`、`evidence_ids`、`method`、`method_basis`、`observation_end`、`future_time_text`、`condition_state`、`trend_aligned`，以及 `evidence_notes` 和 `remaining_gap`。`reason` 与 `limitation` 各用 1 到 3 句具体中文。展示五类是：正确；趋势符合（存成 `verdict=部分符合` 且 `trend_aligned=true`）；部分符合；错误；暂无法判断。底层四类 verdict 只有正确、部分符合、错误、暂无法判断。
4. **SEMANTIC REVIEW。** 六项都要有 `pass`、`fail` 或 `unknown`：`object_match`、`condition_logic`、`time_alignment`、`evidence_support`、`counterevidence`、`verdict_logic`。`fail` 先修订评估一次。修订后仍失败，就把该条收成暂无法判断，`basis=evidence`，`trend_aligned=false`，并保留复核给出的具体缺口。不能带着失败项维持正确、趋势符合、部分符合或错误。

判定口径同时受 `DECISION_CONTRACT` 约束，这里只记下容易漏掉的执行点：

- 无日期的方向预测，窗口是 `publication_year_proxy` 到 `cutoff`。窗口内主要方向发生为正确，相反为错误。不因为缺日期改成暂无法判断，也不因此只给趋势符合。作者写了更晚终点时，阶段变化不是终局正确。
- 真正的 `if` 没有触发，不给正确或错误。前提未知但后果或分项已经可以观察时，用部分符合或趋势符合，`condition_state=unknown`。
- `claim_type` 不是 forecast，或句子被筛成非预测时，不能判正确。
- 趋势符合要有已存档材料明确支持方向。尚未被推翻、只有背景相关、或只看到一次波动，不够。
- 近期出版、窗口很短的书，更多保留暂无法判断。暂无法判断要指出一个决定性缺口。不要为了减少未定数改判。
- 事实只来自抓取后存档的公开材料。正确、部分符合和错误必须引用这些材料。不要用记忆补数字、日期、来源或概率。没有原始概率就不计算 Brier。

证据记录至少要能通过 `pipeline.py` 的 `verify_evidence`：

```json
{"id":"ev-…","url":"https://example.org/source","date":"2024-01-01","coverage":"观察时期","excerpt":"实际用于判断的短句","limitation":"口径或截断","local_archive":"data/sources/文件名","sha256":"该文件字节的 SHA256","verified":true}
```

`local_archive` 是相对案例目录的路径，不能是绝对路径，也不能跳出案例目录。`sha256` 必须等于该文件字节。`verified` 必须为 true。发布日期若是完整日，不能晚于截止日。`observation_end` 也不能晚于截止日。

[toolkit/exa_client.py](../../toolkit/exa_client.py) 抓取正文时使用 `maxCharacters: 12000`。`verify_prediction.py` 在文本长度达到 12000 时标记 `provider_text_may_be_truncated`。存档若达到此长度，或抓取工具说明已截断，只能引用已保存字符。未保存部分不是证据，取不到内容也不是反证。页眉日期和正文日期冲突时，以正文能支持的日期为准，并在 `limitation` 写明冲突。不稳定来源先重试，再因抓取失败记暂无法判断。

`inspect_assessment` 是不调用模型的引文和日期检查，输入是验证器内存里的候选，不是 `evidence.jsonl` 的最终形状。调用了就记录结果。没调用就写未跑。无论是否调用，计分案例仍要过 `pipeline.py check`。

评估文件必须精确覆盖当前全部主张 ID。然后：

```bash
python3 toolkit/pipeline.py --case cases/<slug> apply assess /仓库外/assess.jsonl
python3 toolkit/pipeline.py --case cases/<slug> check
python3 toolkit/pipeline.py --case cases/<slug> report
```

`check` 失败就不是完成。不要改写主张、手改 ID 或制造证据来换通过。`report` 成功会写出第 2.3 节列出的四份生成文件。`output/summary.json` 的 `display_verdicts` 是五类计数，`correct_share_of_decided` 是严格比例。可判定等于预测条数减去暂无法判断；趋势符合存在底层的「部分符合」里，同时在五类里单列。

## 8. 质量门

全部适用的门都要通过，才能在验收里写完成。任一失败都保持未完成。

1. 块账本的 ID 集合等于计划 `ids`，无缺号、无重复。每条都有 `predictions` 数组。没有「声称已读」的替代记录。
2. 主张由 `validate_chunk_predictions` 和 `claims_from_results` 生成。`context` 全空。fuzzy 引文已退回。去重只有代码里的重叠规则。
3. 每条可核验候选有 PLAN、SELECT、ASSESS、SEMANTIC REVIEW 记录。计分结论都有哈希相符的公开存档。截断和未读存档已标明，且未当作未保存部分的证据。
4. `apply assess`、`check`、`report` 按顺序通过。`check` 的退出码不为 0 时，不能写完成。
5. `python3 -m unittest discover -s toolkit/tests` 通过，并记录实际测试数。
6. 对密钥材料做字面检索，案例树、验收说明和日志中的真命中为 0。检索过程不打印密钥。公开 URL 里偶然出现的 `sk-` 样式要记成假阳性，不要删 URL 来逃避检查。
7. 案例和验收包里没有全书 TXT/PDF、`batch_*.plan.json`、模型 request/response、检查点全文或密钥。
8. 长片段重合检查见第 10 节。仓库没有现成命令。做了就报告最长重合和所在文件；没做就写「未跑」，不能写通过。
9. `manual_report.py` 不在仓库。未运行就写「工具不在仓库」。不要生成 `REPORT-manual-zh.md` 或 `output/manual-final/` 来模仿它。`pipeline.py report` 的四份文件是仓库内报告。

零条计分预测时，不要编造证据把 `evidence.jsonl` 凑成非空。验收写明计分条数为 0，第 3 条的「计分必须有存档」不适用。有计分条数时，空证据文件不能算完成。

统计口径：

- 严格比例 = 正确 / 可判定
- 错误率 = 错误 / 可判定
- 五类计数来自 `display_verdicts`
- 加权展示若写出，公式必须标为 2026-11-16 worker brief，并同时保留 `partial_numeric_weight=null` 的程序摘要

## 9. 带日期的状态，不是新队列

仓库没有 `queue.jsonl`、`claims/` 或 `done/`。阅读库有多份带 sha256 的全文，其中一些还没有 `cases/<id>-v5`。本文不把「目录减去已有案例」写成权威剩余名单。2026-11-16 16:35 的本地上传清单已经过时。本地 `done/` 也不能证明 `main` 已合并。

下面只记录 2026-11-19 核对过、且 `main` 上没有案例目录的项目。文件字节与对应 `catalog.json` 的 sha256 一致。文件还在，不等于可以开工。续作必须由用户按 `AGENTS.md` 点名这些 ID。

| ID | 2026-11-19 的 main | 阅读库文件与 sha256 | 当时停住的原因 |
|---|---|---|---|
| `adams-education-of-henry-adams` | 无目录。PR #30 的提交信息是因报告重跑会改写字节而抽出 | `reading-library/2026-11-15-未来判断扩展100本/03-文化与传播/046-the-education-of-henry-adams.txt`，`512eb06e74482bff4df27073501c0bca62a2ef49038999c3360a6b5553d3ca73` | 本地曾标 done。第 3 批未收入。不要重做或悄悄补交。 |
| `hudson-crystal-age` | 无目录，同一抽取原因 | `…/03-文化与传播/048-a-crystal-age.txt`，`b414056b098b7c75a59d7e3ca00300ea06d0ac7457d88ef02a494a2fa91a3139` | 同上。 |
| `lessig-code-version-2` | 无目录。已合并的是另一本 `lessig-future-of-ideas-v5` | `…/05-技术与科学/087-code-version-2-0.pdf`，`4fcc66d222cc986b9010110611a45afdf70d2cf9ed231d4f6a4979b3da6cf6f5` | 本地在 2026-11-16 晚些时候完成，没有进入 PR #27–#31。不要把它和 Future of Ideas 混为一本。 |
| `tocqueville-democracy-in-america` | 无目录 | `…/02-政治与治理/030-democracy-in-america.txt`，`603391572a4fab72a0382f2d35190595de85e2a6f8ad278b7d3c5863ce2cfeb6` | 本地记录为已读完，但 `check` 未通过，未标 done。记录中的缺口 ID `txt-603391572a-001333967-001334027` 与该文件 sha256 前 10 位相符。本次没有重跑 check，也没有改这条引文。 |
| `doctorow-makers` | 无目录。已合并的是 `doctorow-little-brother-v5` 与 `doctorow-down-and-out-in-the-magic-kingdom-v5` | `…/05-技术与科学/085-makers.txt`，`5cbea89a6bc6a25ad6066baf365170f82311bbc12d5aea97a8349699be54c993` | 本地完整性阻塞。记录为读到 246/305 块。本次没有续读。 |
| `unesco-reshaping-policies-for-creativity` | 无目录。已合并的是另一本 `unesco-reimagining-our-futures-together-v5` | `…/03-文化与传播/040-re-shaping-policies-for-creativity-addressing-culture-as-a-global-public-good.pdf`，`b54719f6ab5b32f2ef73a6869843227d1163354c82162659b68843a5af6a39ac` | 本地完整性阻塞。不要把它和已完成的 reimagining 混为一本。 |
| `wang-huiyao-china-next-global-order` | 无目录 | `…/02-政治与治理/015-china-and-the-next-global-order-coming-multipolar-world-and-great-power-coopetition.pdf`，`cc1c691c22ba255847491a249fe12d5dde31fdd247aabaf026735c5544a9a12d` | 本地记录为出版日窗口尚未审完，未标 done。 |
| `anderson-long-tail` | 无目录 | `reading-library/2026-11-15-未来判断书单/03-科技和AI/20-长尾理论.pdf`，`f327e1164ff616232409abee4f787a6daddc79f805233bca3377a12274b5c38a` | 本地记录为抽取未完成。 |
| `hughes-exploring-shaping-international-futures` | 无目录 | `…/02-政治与治理/017-exploring-and-shaping-international-futures.pdf`，`f462d1d296256c457eff07e676eead737f524c198174e7c9ca8da1e6f8169015` | 本地记录为分块已准备，答案尚未开始。 |
| `lin-jiedu-zhongguo-jingji` | 无目录 | `reading-library/2026-11-15-未来判断书单/04-经济和金融/33-解读中国经济.pdf`，`c55476987d898ebea6c56ec854bd00068f74474f81745291ccbc986f590184c4` | 本地记录为正文只读了一部分。 |

上表不是完整未做书单。队列文件不在仓库，所以这里不能列出「还剩多少本」或证明每本原书都齐。没有出现在表里的书，才可能按续作 Prompt 的资源条件新开；表里的书必须等用户写出 ID。

## 10. 建议

以下各项当前代码没有做成命令。做了要在验收里标成额外检查；没做不能写成已通过。

- 配置定稿并清空 `context` 后，重算 `extraction_provenance`。这样收据描述的是最终文件。不要为了重算成功而改主张。
- 打包前用源 TXT 做连续 300 字滑窗。保留源换行的精确重合，除主张引文及其在 `pipeline.py report` 中的转写外应为 0。只因为去掉换行才重合、且重合来自正常引文时，保留引文并披露，不要为了过门截短原文。不要把全书放进包里来制造或隐藏重合。
- 双栏 PDF 若被 `pdftotext` 交错，先按页恢复阅读顺序再抽取，并记录这一步。程序不会自动恢复栏序。
- 领取协议若要防两个人同时做同一本，唯一公共事实是默认分支上是否已有 `cases/<id>-v5`，加上用户是否已把 ID 分给某人。一台机器上的 `mkdir` 锁不会锁住另一台机器。仓库里没有共享锁目录。
- 验收包放在用户指定的目录。默认只交付验收包。用户另有发布授权时，才 `git push` 或开 PR。本手册的存在不是发布授权。

## 11. 验收包里写什么

每本书一份说明，至少包括：ID、源文件相对路径、PDF 与 TXT 的 sha256、与 catalog 是否一致、块数、账本覆盖、候选数、可核验数、五类计数、严格比例、错误率、证据与存档数、截断数、第 8 节每一道门的通过、失败、不适用或未跑、加权展示是否附带及其标签、偏离和未补上的缺口。

不把原书、分块计划、密钥、检索密钥或整本账本正文放进 git。短引文可以留在 `data/claims.jsonl`，这是案例本来就要保存的内容。
