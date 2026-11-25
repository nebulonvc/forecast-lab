#!/usr/bin/env python3
"""Antigravity dynamic workflow (`run_workflow`) for parallel, zero-context-bloat, anti-laziness book processing.

Invoke via Antigravity's `run_workflow` tool:
    run_workflow(
        ScriptPath="/abs/path/to/toolkit/antigravity_book_workflow.py",
        Description="Parallel v5 book extraction and dual-evidence verification",
        Args={
            "case": "cases/author-book-v5",
            "txt": "cases/author-book-v5/input/book.txt",
            "chunk_batch_size": 4,
            "verify_batch_size": 3,
            "max_wave_concurrency": 6,
            "max_retries": 3,
            "model": "inherit"
        }
    )

Design Guarantees:
1. Parallelism (`parallel` in waves): Splits chunks and verification tasks into bounded shards and runs worker agents concurrently.
2. Zero Context Bloat: Workers read only their assigned shard file from disk (`batches/batch-XXXX.jsonl`) and write outputs to disk (`chunk_proposals/<chunk_id>.json`), returning only a tiny JSON receipt (<200 bytes) via `finish`.
3. Anti-Laziness (Zero-Trust):
   - Every chunk proposal must include `body_sha256_12` + `tail_anchor` (a verbatim >=8 char snippet from the last 45% of the chunk's `body`).
   - Orchestrator runs `contribute_book.py audit-progress` after every wave and automatically re-dispatches any incomplete or invalid shard up to `max_retries`.
   - Every decided forecast assessment must cite >=2 independent archived evidence items (`--require-dual-evidence`).
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
VERIFY_BATCH_SIZE = int(req_args.get("verify_batch_size", 3))
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
    },
    "required": ["batch_id", "verified_tasks", "evidence_archived"],
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


def make_verify_worker(batch: dict):
    bid = batch["batch_id"]
    bpath = CASE_DIR / batch["path"]
    cids = batch["claim_ids"]
    vprop_file = CASE_DIR / f"output/verify_proposals/{bid}.jsonl"
    eprop_file = CASE_DIR / f"output/evidence_proposals/{bid}.jsonl"
    method_path = REPO_ROOT / "toolkit/METHOD.md"

    prompt = f"""你是《信号与噪音》v5 正反双向搜证与六维复核专员（负责核验分片 {bid}）。
请严格对 `{bpath}` 中的全部 {len(cids)} 条预测（ID: {", ".join(cids)}）执行双向核查：

1. 阅读核验标准：`{method_path}` 与你的分片任务 `{bpath}`。
2. **强制双向搜证（Anti-Laziness 门禁强制检查）**：
   - 对每一条可判定预测（`verdict` 不为 `暂无法判断`），你必须利用联网搜索工具成对检索 **至少 2 条独立权威证据**（1 条支持/主口径证据 + 1 条反面/瓶颈/替代解释证据，优先官方统计局、央行、IEA/OECD/世行、财报、学术一手数据，且发布日期 `<= cutoff`）。
   - 每条证据的公开正文（`text`）长度不得少于 80 字，并写入 `{eprop_file}`（JSONL 格式，每行一条：`{{"id": "ev-{bid}-01", "url": "https://...", "date": "YYYY-MM-DD", "coverage": "...", "excerpt": "...", "limitation": "...", "text": "完整公开正文摘录（>=80字）"}}`）。
3. **六维语义复核与结论落盘**：
   - 将本分片所有预测的评估结果写入 `{vprop_file}`（JSONL 格式，每行对应一个 claim `id`）：
     `{{"id": "<claim_id>", "inclusion": "forecast", "verdict": "正确|部分符合|错误|暂无法判断", "basis": "endpoint|observed_window|conditional|future|definition|evidence|attribution", "scope": "...", "reason": "...", "limitation": "...", "evidence_ids": ["ev-{bid}-01", "ev-{bid}-02"], "method": "...", "method_basis": "explicit|inferred|unknown", "observation_end": "YYYY-MM-DD", "future_time_text": "", "condition_state": "unconditional|satisfied|not_met|unknown", "trend_aligned": false}}`
4. 写完磁盘文件后，通过 `finish` 返回简短回执：`{{"batch_id": "{bid}", "verified_tasks": {len(cids)}, "evidence_archived": <证据条数>}}`。
"""
    return agent(prompt=prompt, schema=VERIFY_RECEIPT_SCHEMA, role=f"Verify {bid}", model=WORKER_MODEL)


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
# Phase 3: Parallel Dual-Evidence Verification with Retry Loop
# ============================================================================
phase("3. Parallel Dual-Evidence Verification")
exp_res = run_cb("export-verify-tasks", "--case", str(CASE_DIR), "--batch-size", str(VERIFY_BATCH_SIZE))
vmanifest = json.loads((CASE_DIR / "output/verify_manifest.json").read_text(encoding="utf-8"))
vbatches_by_id = {b["batch_id"]: b for b in vmanifest["batches"]}
log(f"Exported {exp_res['tasks']} forecast tasks across {len(vbatches_by_id)} verification batches.")

for attempt in range(1, MAX_RETRIES + 1):
    vprog = run_cb("audit-progress", "--case", str(CASE_DIR))["verification"]
    pending_vids = vprog["pending_batches"]
    if not pending_vids and vprog["ready"]:
        log(f"All {vprog['total_tasks']} forecast verification tasks completed!")
        break
    log(f"Verification attempt {attempt}/{MAX_RETRIES}: {len(pending_vids)} pending batches ({vprog['done_tasks']}/{vprog['total_tasks']} done)")
    pending_vbatches = [vbatches_by_id[bid] for bid in pending_vids]
    for wave in slice_waves(pending_vbatches, MAX_WAVE_CONCURRENCY):
        vreceipts = await parallel(wave, make_verify_worker)
        for r in vreceipts:
            log(f"Verify receipt: {r}")

final_vprog = run_cb("audit-progress", "--case", str(CASE_DIR))["verification"]
if not final_vprog["ready"]:
    raise RuntimeError(f"Verification incomplete after {MAX_RETRIES} attempts: missing={final_vprog['missing_task_ids']}")

# ============================================================================
# Phase 4: Deterministic Aggregation, Dual-Evidence Gate & PR Check
# ============================================================================
phase("4. Apply Assessments & PR Gate")
app_res = run_cb(
    "apply-assessments",
    "--case", str(CASE_DIR),
    "--assessments", str(CASE_DIR / "output/verify_proposals"),
    "--evidence-raw", str(CASE_DIR / "output/evidence_proposals"),
    "--require-dual-evidence",
)
log(f"Applied assessments & verified dual evidence: {app_res}")

if not SKIP_SYNC:
    sync_res = run_cb("sync-database", "--case", str(CASE_DIR))
    log(f"Synced database: {sync_res}")
    pr_res = run_cb("pr-check", "--case", str(CASE_DIR))
    log(f"PR gate passed: {pr_res}")

print(json.dumps({"case": CASE_DIR.name, "status": "completed", "assessments": app_res}, ensure_ascii=False))
