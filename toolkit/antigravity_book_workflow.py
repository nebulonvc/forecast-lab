#!/usr/bin/env python3
"""Antigravity dynamic workflow (`run_workflow`) for parallel, zero-context-bloat, anti-laziness book processing.

Aligned 100% with `verify_prediction.py` (`search-verifier-v3`) & `semantic_review.py`:
1. Parallelism (`parallel` in waves): Splits chunks and verification tasks into bounded shards and runs worker agents concurrently.
2. Zero Context Bloat: Workers read only their assigned shard file from disk (`batches/batch-XXXX.jsonl`) and write outputs to disk (`chunk_proposals/<chunk_id>.json`), returning only a tiny JSON receipt (<200 bytes) via `finish`.
3. Anti-Laziness & `search-verifier-v3` Multi-Round Parity:
   - Proof-of-Reading on Extraction: Every chunk proposal must include `body_sha256_12` + `tail_anchor` (a verbatim >=8 char snippet from the last 45% of the chunk's `body`).
   - Multi-Round Adaptive Search (`round_history`):
     * Initial rounds (1-2): Lock `research_scope` and execute paired `support` + `counter` queries.
     * Adaptive rounds (up to 3 rounds when verdict is still `暂无法判断`): Target the concrete `decisive_gap` (`gap_before`), declare a new `strategy_change` (shifting wording, proxy indicator, timeframe, source type, or language), and run non-duplicate queries (`<=5` per round). Single-round lazy `暂无法判断` is rejected unless `basis="future"` or an adaptive round proves public search cannot resolve the gap.
   - Verbatim `evidence_notes` Binding: Every cited `evidence_id` must have an `evidence_notes` entry whose `quote` is mechanically verified against the archived source text (`sr.align_quote`).
   - Independent 6-Check Semantic Review (`semantic_review.py`): A separate Independent Reviewer agent inspects `object_match`, `condition_logic`, `time_alignment`, `evidence_support`, `counterevidence`, and `verdict_logic` (`accept` / `revise` / `unresolved`), triggering 1 bounded revision + re-review when needed.
"""

import json
from pathlib import Path
import subprocess
import sys

REPO_ROOT = Path(WORKSPACES[0]).resolve() if WORKSPACES else Path.cwd().resolve()
TOOLKIT_SCRIPT = REPO_ROOT / "toolkit/contribute_book.py"

req_args = args if isinstance(args, dict) else {}
case_rel = req_args.get("case")
txt_rel = req_args.get("txt")
if not case_rel or not txt_rel:
    raise ValueError("Args must provide 'case' (e.g. 'cases/slug-v5') and 'txt' (e.g. 'cases/slug-v5/input/book.txt')")

CASE_DIR = (REPO_ROOT / case_rel).resolve()
TXT_PATH = (REPO_ROOT / txt_rel).resolve()
CHUNK_BATCH_SIZE = int(req_args.get("chunk_batch_size", 4))
CHUNK_CHARS = int(req_args.get("chunk_chars", 3500))
VERIFY_BATCH_SIZE = int(req_args.get("verify_batch_size", 2))
MAX_WAVE_CONCURRENCY = int(req_args.get("max_wave_concurrency", 6))
MAX_RETRIES = int(req_args.get("max_retries", 3))
WORKER_MODEL = req_args.get("model") or "inherit"
SKIP_SYNC = bool(req_args.get("skip_sync", False))


def run_cb(*cmd_args: str) -> dict:
    cmd = [sys.executable, str(TOOLKIT_SCRIPT), *cmd_args]
    proc = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(f"contribute_book.py {' '.join(cmd_args)} failed:\n{proc.stderr or proc.stdout}")
    out = proc.stdout.strip().splitlines()
    return json.loads(out[-1]) if out else {}


def slice_waves(items: list, width: int) -> list[list]:
    return [items[i : i + width] for i in range(0, len(items), width)]


EXTRACTION_RECEIPT_SCHEMA = {
    "type": "object",
    "properties": {
        "batch_id": {"type": "string"},
        "processed_chunks": {"type": "integer"},
        "extracted_forecasts": {"type": "integer"},
    },
    "required": ["batch_id", "processed_chunks", "extracted_forecasts"],
}

VERIFY_RECEIPT_SCHEMA = {
    "type": "object",
    "properties": {
        "batch_id": {"type": "string"},
        "verified_tasks": {"type": "integer"},
        "evidence_archived": {"type": "integer"},
        "total_adaptive_rounds": {"type": "integer"},
    },
    "required": ["batch_id", "verified_tasks", "evidence_archived", "total_adaptive_rounds"],
}

REVIEW_RECEIPT_SCHEMA = {
    "type": "object",
    "properties": {
        "batch_id": {"type": "string"},
        "reviewed_tasks": {"type": "integer"},
        "accepted": {"type": "integer"},
        "revise_requested": {"type": "integer"},
        "unresolved": {"type": "integer"},
    },
    "required": ["batch_id", "reviewed_tasks", "accepted", "revise_requested", "unresolved"],
}


def make_extract_worker(batch: dict):
    bid = batch["batch_id"]
    bpath = CASE_DIR / batch["path"]
    cids = batch["chunk_ids"]
    prop_dir = CASE_DIR / "output/txt_import/chunk_proposals"
    prompt_path = CASE_DIR / "output/txt_import/prompt_v5.txt"
    cfg_path = CASE_DIR / "config.json"

    prompt = f"""你是《信号与噪音》v5 书籍预测抽取分片专员（负责分片 {bid}）。
请严格按以下步骤在本地磁盘完成分片抽取，严禁跳读、严禁遗漏任何一个 chunk：

1. 阅读抽取规范与案例配置：
   - 案例配置：`{cfg_path}`
   - v5 抽取规范：`{prompt_path}`
   - 你唯一负责的分片文件：`{bpath}`（共 {len(cids)} 个 chunk：{", ".join(cids)}）

2. 对 `{bpath}` 中的**每一个** chunk（`{", ".join(cids)}`），完整通读其 `body`（从第一行读到最后一行），在 `{prop_dir}/<chunk_id>.json` 写入独立的 JSON 文件。
   **强制防偷懒与阅读证明要求（程序会自动做密码学校验，不通过直接打回）**：
   每个 `{prop_dir}/<chunk_id>.json` 必须满足如下顶层结构：
   ```json
   {{
     "id": "<chunk_id>",
     "body_sha256_12": "<直接照抄该 chunk 输入里的 body_sha256_12 字段>",
     "tail_anchor": "<从该 chunk 的 body 后 45% 区域（靠末尾段落）逐字复制一段 10~25 字的连续原文，证明你读到了块尾>",
     "predictions": [ ... ]
   }}
   ```
   - 如果某个 chunk 没有任何预测，也必须写出该文件并令 `"predictions": []`，同时附上真实的 `body_sha256_12` 与 `tail_anchor`！
   - 每条 prediction 必须包含 v5 标准字段：`quote`（必须从 `body` 逐字连续照抄，不得改字或用省略号拼接）、`kind`（`prediction` 或 `unclear`）、`claim_type`（`forecast`/`aphorism`/`normative`/`trivial`/`historical`/`mechanism`/`hypothetical`/`unclear`）、`speaker`、`attribution`（`author`/`author_endorsed`/`reported`/`rebutted`）、`future_oriented`（bool）、`claim`、`changes`、`horizon`、`resolvable`（bool）、`confidence`、`expanded_claim`、`reference_resolutions`、`unresolved_references`、`time_text`、`condition_text`、`method`、`method_basis`、`reason`。

3. 全部写完后，只通过 `finish` 返回简短回执：`{{"batch_id": "{bid}", "processed_chunks": {len(cids)}, "extracted_forecasts": <预测条数>}}`，不要在回复里粘贴长篇原文。
"""
    return agent(prompt=prompt, schema=EXTRACTION_RECEIPT_SCHEMA, role=f"Extract {bid}", model=WORKER_MODEL)


async def run_verify_and_review_shard(batch: dict):
    """Run multi-round adaptive researcher + independent 6-check semantic reviewer (+ 1 revision if needed) for one shard."""
    bid = batch["batch_id"]
    bpath = CASE_DIR / batch["path"]
    cids = batch["claim_ids"]
    vprop_file = CASE_DIR / f"output/verify_proposals/{bid}.jsonl"
    eprop_file = CASE_DIR / f"output/evidence_proposals/{bid}.jsonl"
    srev_file = CASE_DIR / f"output/semantic_reviews/{bid}.jsonl"
    v3_prompt_path = CASE_DIR / "output/search_verify/verify_prompt_v3.txt"

    researcher_prompt = f"""你是《信号与噪音》`search-verifier-v3` 多轮双向搜证与初判研究员（负责核验分片 {bid}）。
请严格按 `verify_prediction.py` 的多轮自适应搜证标准对 `{bpath}` 中的全部 {len(cids)} 条预测（ID: {", ".join(cids)}）执行研究：

1. 先阅读完整核验契约：`{v3_prompt_path}`（含 PLAN、ASSESS 与 DECISION_CONTRACT 七条统一判定口径）以及你的分片任务 `{bpath}`。
2. **多轮双向搜证与自适应变策补搜（`round_history` 强制门禁）**：
   - **初轮（Round 1-2，`kind: "initial"`）**：必须先确定 `research_scope`，并执行成对的 `support`（支持方向）与 `counter`（反面/瓶颈方向）检索。
   - **自适应变策补搜（Round 3..5，`kind: "adaptive"`，最多 3 轮）**：
     如果初轮检索后结论仍为 `"暂无法判断"`（且不是因为终点年份在 cutoff 之后的 `basis="future"`），你**绝不能单轮直接放弃**！必须针对具体缺失的 `gap_before`（决定性缺口），连续执行至少 2 轮（最多 3 轮）`kind="adaptive"` 变策补搜（或者在自适应轮次中明确证明公开检索不可能补上该缺口并填写 `stopped` 原因）：
     * 每一轮 adaptive 必须写明不同于前序轮次的 `strategy_change`（例如：切换中英文关键词、换用官方统计局/IEA/世行/行业协会代理指标、调整时间窗口）；
     * 每条 adaptive query 必须包含 `{{"role": "support|counter", "query": "不重复的新检索词", "strategy": "本条相比前轮改变了什么"}}`。
3. **归档公开证据正文（`{eprop_file}`）**：
   - 每条已判定预测（`verdict != "暂无法判断"`）必须绑定 **至少 2 条独立权威证据**（支持 + 反面/边界，且发表/观察期 `<= cutoff`）。
   - 将抓取到的证据写入 `{eprop_file}`（JSONL 格式，每行一条：`{{"id": "ev-{bid}-01", "url": "https://...", "date": "YYYY-MM-DD", "coverage": "...", "excerpt": "...", "limitation": "...", "text": "抓取的公开网页/报告正文（>=80字，必须包含你在 evidence_notes 中引用的连续原句）"}}`）。
4. **写出含 `round_history` 与 `evidence_notes` 的评估建议稿（`{vprop_file}`）**：
   - 将本分片每条预测的评估写入 `{vprop_file}`（JSONL 格式，每行一条），必须包含：
     * 标准评估字段：`id`, `inclusion` ("forecast"), `verdict` ("正确"|"部分符合"|"错误"|"暂无法判断"), `basis`, `scope`, `reason`, `limitation`, `evidence_ids`, `method`, `method_basis`, `observation_end`, `future_time_text`, `condition_state`, `trend_aligned`
     * `remaining_gap`：若为 `"暂无法判断"` 必须点名具体缺失的对象、指标或时期；已判定可为 `""`。
     * `evidence_notes`：与 `evidence_ids` 一一对应，每项含 `{{"evidence_id": "...", "relation": "support|counter|boundary|background", "quote": "<必须逐字存在于该证据 text 中的连续原句>", "publication_date": "YYYY-MM-DD或null", "observation_end": "YYYY-MM-DD或null", "limitation": "..."}}`。
     * `round_history`：数组，记录实际执行的初轮与自适应轮次：
       `[{{"index": 1, "round": 1, "kind": "initial", "strategy_change": null, "gap_before": null, "queries": [{{"role": "support", "query": "..."}}, {{"role": "counter", "query": "..."}}], "gap_after": "...", "verdict_after": "..."}}]`。
5. 写完磁盘文件后，通过 `finish` 返回回执。
"""
    r_receipt = await agent(prompt=researcher_prompt, schema=VERIFY_RECEIPT_SCHEMA, role=f"Research {bid}", model=WORKER_MODEL)

    # Step 2: Independent 6-check Semantic Reviewer Agent (does NOT re-search, strictly audits proposed_assessment)
    reviewer_prompt = f"""你是《信号与噪音》`search-verifier-v3` 独立六维语义复核员（负责独立复核分片 {bid}）。
你不得重新搜证，也不得使用训练记忆补充外部事实；你的职责是严格按照 `{v3_prompt_path}` 中的 **三、独立六维语义复核规则 (SEMANTIC REVIEW)** 与 **DECISION_CONTRACT**，审阅研究员刚刚生成的评估建议稿：

1. 读取以下磁盘文件：
   - 原书任务分片：`{bpath}`
   - 研究员评估建议稿：`{vprop_file}`
   - 研究员归档的证据正文：`{eprop_file}`
2. 对 `{bpath}` 中的每一条预测（ID: {", ".join(cids)}），独立检查以下六维逻辑门（每项只能填 `"pass"`、`"fail"` 或 `"unknown"`）：
   - `object_match`：取证对象是否与原书限定的人群、机构、地点或成果集合对应（已披露且指向同一对象的回顾性代理应判 `pass`）；
   - `condition_logic`：真实条件前提与后果关系是否成立；
   - `time_alignment`：原预测时间、证据发表日与 `observation_end`（`<= cutoff`）是否对齐；
   - `evidence_support`：`evidence_notes` 中的 `quote` 是否真实存在于 `{eprop_file}` 对应证据的 `text` 中并支持结论；
   - `counterevidence`：同对象、同口径的反向证据是否被恰当处理；
   - `verdict_logic`：五类结论（正确/趋势符合/部分符合/错误/暂无法判断）与 `round_history` 多轮检索是否符合统一判定口径。
3. 在 `{srev_file}` 写出复核结果（JSONL 格式，每行一条，严格遵守 `semantic_review.validate_review` 校验结构）：
   ```json
   {{
     "id": "<claim_id>",
     "decision": "accept|revise|unresolved",
     "checks": {{
       "object_match": "pass",
       "condition_logic": "pass",
       "time_alignment": "pass",
       "evidence_support": "pass",
       "counterevidence": "pass",
       "verdict_logic": "pass"
     }},
     "issues": [],
     "remaining_gap": ""
   }}
   ```
   - 当 `decision == "accept"` 时，六项 `checks` 必须全部为 `"pass"`，`issues` 必须为 `[]`，`remaining_gap` 必须为 `""`。
   - 当 `decision` 为 `"revise"` 或 `"unresolved"` 时，每一个非 `"pass"` 的 check 必须在 `issues` 中有至少一条记录：`{{"check": "<非pass项>", "reason": "...", "source_quote": "<逐字摘自原书quote/context或证据text的连续原句>", "evidence_id": "<证据ID或null>"}}`，且 `remaining_gap` 非空。
4. 写完 `{srev_file}` 后通过 `finish` 返回回执。
"""
    rev_receipt = await agent(prompt=reviewer_prompt, schema=REVIEW_RECEIPT_SCHEMA, role=f"Review {bid}", model=WORKER_MODEL)

    # Step 3: If reviewer requested 'revise' on any item in the shard, run bounded 1-time revision + round-2 review
    if rev_receipt.get("revise_requested", 0) > 0:
        revise_prompt = f"""你是《信号与噪音》`search-verifier-v3` 评估修订与二次复核专员（负责分片 {bid} 的唯一一次修订）。
独立语义复核员在 `{srev_file}` 中对 `{vprop_file}` 提出了 `decision="revise"` 的修订意见。
请严格按照 `{v3_prompt_path}` 中的 **四、唯一一次修订规则 (REVISION)**：
1. 读取 `{bpath}`、`{eprop_file}`、`{vprop_file}` 与 `{srev_file}`。
2. 针对 `{srev_file}` 中的具体 `issues` 修正 `{vprop_file}` 中对应预测的口径、结论、限制说明或 `evidence_notes`（若缺决定性事实则补充多轮自适应检索或按规程保守闭合为带具体 `remaining_gap` 的 `暂无法判断`）。
3. 同步更新 `{srev_file}` 中的二次复核结果（修复成立的项更新为 `decision="accept"`, 六项 `pass`, `issues=[]`, `remaining_gap=""`；若仍无法成立则按 `verify_prediction.py` 第 859-865 行保守闭合为 `verdict="暂无法判断"` 且 `decision="unresolved"`）。
4. 完成后通过 `finish` 返回更新后的复核回执。
"""
        rev_receipt = await agent(prompt=revise_prompt, schema=REVIEW_RECEIPT_SCHEMA, role=f"Revise {bid}", model=WORKER_MODEL)

    return {"batch_id": bid, "research": r_receipt, "review": rev_receipt}


# ============================================================================
# Phase 1: Deterministic Chunking & Sharding
# ============================================================================
phase("1. Chunk & Shard Book")
claims_file = CASE_DIR / "data/claims.jsonl"
existing_claims = [line for line in claims_file.read_text(encoding="utf-8").splitlines() if line.strip()] if claims_file.is_file() else []

if not existing_claims:
    manifest = run_cb(
        "chunk-txt",
        "--case", str(CASE_DIR),
        "--txt", str(TXT_PATH),
        "--chunk-chars", str(CHUNK_CHARS),
        "--batch-size", str(CHUNK_BATCH_SIZE),
    )
    log(f"Chunked book into {manifest['active_chunks']} active chunks across {len(manifest['batches'])} batches.")

    # ============================================================================
    # Phase 2: Parallel Map-Reduce Extraction with Anti-Laziness Retry Loop
    # ============================================================================
    phase("2. Parallel Extraction (Proof-of-Reading Enforced)")
    batches_by_id = {b["batch_id"]: b for b in manifest["batches"]}

    for attempt in range(1, MAX_RETRIES + 1):
        prog = run_cb("audit-progress", "--case", str(CASE_DIR))["extraction"]
        pending_ids = prog["pending_batches"]
        if not pending_ids and prog["ready"]:
            log(f"All {prog['active_chunks']} chunks verified with Proof-of-Reading!")
            break
        log(f"Extraction attempt {attempt}/{MAX_RETRIES}: {len(pending_ids)} pending batches ({prog['proof_verified_chunks']}/{prog['active_chunks']} proof-verified chunks)")
        pending_batches = [batches_by_id[bid] for bid in pending_ids]
        for wave in slice_waves(pending_batches, MAX_WAVE_CONCURRENCY):
            receipts = await parallel(wave, make_extract_worker)
            for r in receipts:
                log(f"Worker receipt: {r}")

    final_prog = run_cb("audit-progress", "--case", str(CASE_DIR))["extraction"]
    if not final_prog["ready"]:
        raise RuntimeError(f"Extraction incomplete after {MAX_RETRIES} attempts: missing={final_prog['missing_chunk_ids']} pending_batches={final_prog['pending_batches']}")

    imp_res = run_cb(
        "import-extractions",
        "--case", str(CASE_DIR),
        "--txt", str(TXT_PATH),
        "--proposals", str(CASE_DIR / "output/txt_import/chunk_proposals"),
        "--require-proof",
    )
    log(f"Imported extractions: {imp_res}")
else:
    log(f"Found {len(existing_claims)} existing claims in data/claims.jsonl; skipping extraction phase.")

# ============================================================================
# Phase 3: Parallel Multi-Round Verification + Independent 6-Check Semantic Review
# ============================================================================
phase("3. Multi-Round Adaptive Search & Independent 6-Check Review")
exp_res = run_cb("export-verify-tasks", "--case", str(CASE_DIR), "--batch-size", str(VERIFY_BATCH_SIZE))
vmanifest = json.loads((CASE_DIR / "output/verify_manifest.json").read_text(encoding="utf-8"))
vbatches_by_id = {b["batch_id"]: b for b in vmanifest["batches"]}
log(f"Exported {exp_res['tasks']} forecast tasks across {len(vbatches_by_id)} verification batches.")

for attempt in range(1, MAX_RETRIES + 1):
    vprog = run_cb("audit-progress", "--case", str(CASE_DIR))["verification"]
    # Re-run any batch that is missing tasks OR failed strict search-verifier-v3 multi-round / semantic review validation
    if vprog.get("strict_v3_ready"):
        log(f"All {vprog['total_tasks']} forecast tasks passed multi-round adaptive search & 6-check semantic review!")
        break
    pending_vids = vprog.get("strict_pending_batches") or vprog["pending_batches"] or list(vbatches_by_id.keys())
    log(
        f"Verification attempt {attempt}/{MAX_RETRIES}: {len(pending_vids)} batches to run "
        f"(done={vprog['done_tasks']}/{vprog['total_tasks']}, "
        f"adaptive_compliant={vprog.get('adaptive_compliant_tasks', 0)}, "
        f"semantic_reviewed={vprog.get('semantic_reviewed_tasks', 0)})"
    )
    pending_vbatches = [vbatches_by_id[bid] for bid in pending_vids]
    for wave in slice_waves(pending_vbatches, MAX_WAVE_CONCURRENCY):
        vreceipts = await parallel(wave, run_verify_and_review_shard)
        for r in vreceipts:
            log(f"Verify+Review shard receipt: {r}")

final_vprog = run_cb("audit-progress", "--case", str(CASE_DIR))["verification"]
if not final_vprog.get("strict_v3_ready"):
    raise RuntimeError(
        f"Verification failed strict search-verifier-v3 check after {MAX_RETRIES} attempts: "
        f"missing={final_vprog['missing_task_ids']}, strict_pending_batches={final_vprog.get('strict_pending_batches')}"
    )

# ============================================================================
# Phase 4: Deterministic Aggregation, V3 Multi-Round Gate & PR Check
# ============================================================================
phase("4. Apply Assessments & V3 Multi-Round Gate")
app_res = run_cb(
    "apply-assessments",
    "--case", str(CASE_DIR),
    "--assessments", str(CASE_DIR / "output/verify_proposals"),
    "--evidence-raw", str(CASE_DIR / "output/evidence_proposals"),
    "--semantic-reviews", str(CASE_DIR / "output/semantic_reviews"),
    "--require-dual-evidence",
    "--require-adaptive-rounds",
    "--require-semantic-review",
)
log(f"Applied assessments & verified V3 multi-round + 6-check review: {app_res}")

if not SKIP_SYNC:
    sync_res = run_cb("sync-database", "--case", str(CASE_DIR))
    log(f"Synced database: {sync_res}")
    pr_res = run_cb("pr-check", "--case", str(CASE_DIR))
    log(f"PR gate passed: {pr_res}")

print(json.dumps({"case": CASE_DIR.name, "status": "completed", "assessments": app_res}, ensure_ascii=False))
