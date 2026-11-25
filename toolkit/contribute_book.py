#!/usr/bin/env python3
"""Community book contribution toolkit: Agent-native & BYOK API workflows, PR checks, and database sync.

Uses only the Python 3.11+ standard library.
"""
from __future__ import annotations

import argparse
import csv
from datetime import date
import hashlib
import json
from pathlib import Path
import re
import statistics
import subprocess
import sys
import tempfile

TOOLKIT_DIR = Path(__file__).resolve().parent
REPO_ROOT = TOOLKIT_DIR.parent
sys.path.insert(0, str(TOOLKIT_DIR))

from decision_policy import DECISION_CONTRACT  # noqa: E402
import pipeline as pl  # noqa: E402
import prepare_book as pb  # noqa: E402
import run_parallel as rp  # noqa: E402
import semantic_review as sr  # noqa: E402
import verify_prediction as vp  # noqa: E402

DOMAINS = (
    "地缘政治与国际秩序",
    "宏观经济、金融与市场",
    "科技、商业与产业颠覆",
    "AI与奇点前沿",
    "人口、能源、资源与生态",
    "社会结构、制度、文化与教育",
    "科幻推演与乌托邦/反乌托邦",
)

DOMAIN_ALIASES = {
    "地缘政治": "地缘政治与国际秩序",
    "国际秩序": "地缘政治与国际秩序",
    "政治与治理": "地缘政治与国际秩序",
    "宏观金融": "宏观经济、金融与市场",
    "宏观经济": "宏观经济、金融与市场",
    "金融与市场": "宏观经济、金融与市场",
    "科技商业": "科技、商业与产业颠覆",
    "商业与产业": "科技、商业与产业颠覆",
    "ai": "AI与奇点前沿",
    "ai与奇点": "AI与奇点前沿",
    "人工智能": "AI与奇点前沿",
    "人口能源资源": "人口、能源、资源与生态",
    "能源与人口": "人口、能源、资源与生态",
    "能源": "人口、能源、资源与生态",
    "社会制度教育": "社会结构、制度、文化与教育",
    "社会制度": "社会结构、制度、文化与教育",
    "科幻乌托邦": "科幻推演与乌托邦/反乌托邦",
    "科幻推演": "科幻推演与乌托邦/反乌托邦",
}

AUTHOR_TYPES = (
    "国际机构与政府智库",
    "政治家与战略实务者",
    "地缘与社科政治学者",
    "经济学家与金融投资人",
    "科技商业思想家与产业实践者",
    "古典思想家与科幻/乌托邦作家",
)

AUTHOR_TYPE_ALIASES = {
    "国际机构": "国际机构与政府智库",
    "智库": "国际机构与政府智库",
    "政府智库": "国际机构与政府智库",
    "政治家": "政治家与战略实务者",
    "战略实务者": "政治家与战略实务者",
    "地缘与社科学者": "地缘与社科政治学者",
    "学者": "地缘与社科政治学者",
    "经济学家": "经济学家与金融投资人",
    "投资人": "经济学家与金融投资人",
    "科技商业思想家": "科技商业思想家与产业实践者",
    "产业实践者": "科技商业思想家与产业实践者",
    "古典思想家": "古典思想家与科幻/乌托邦作家",
    "科幻作家": "古典思想家与科幻/乌托邦作家",
}

SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]{2,80}$")
FORBIDDEN_BOOK_EXTS = {".txt", ".pdf", ".epub", ".mobi", ".azw3", ".docx", ".doc"}
SECRET_PATTERNS = (
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"AIzaSy[A-Za-z0-9_-]{30,}"),
    re.compile(r"tvly-[A-Za-z0-9_-]{16,}"),
    re.compile(r"Bearer\s+[A-Za-z0-9._-]{20,}"),
)
PRIVACY_PATH_PATTERNS = (
    re.compile(r"/Users/[^/\s\"']+"),
    re.compile(r"/home/[^/\s\"']+"),
    re.compile(r"[A-Za-z]:\\\\Users\\\\[^\\\s\"']+"),
)
MAX_QUOTE_CHARS = 1200
MAX_CONTEXT_CHARS = 1600
IGNORED_SUBDIRS_FOR_BOOK_SCAN = {"input", "sources"}


def normalize_domain(raw: str) -> str:
    val = (raw or "").strip()
    if val in DOMAINS:
        return val
    mapped = DOMAIN_ALIASES.get(val.lower()) or DOMAIN_ALIASES.get(val)
    if mapped:
        return mapped
    raise ValueError(f"Unsupported domain '{raw}'. Choose one of: {', '.join(DOMAINS)}")


def normalize_author_type(raw: str) -> str:
    val = (raw or "").strip()
    if val in AUTHOR_TYPES:
        return val
    mapped = AUTHOR_TYPE_ALIASES.get(val.lower()) or AUTHOR_TYPE_ALIASES.get(val)
    if mapped:
        return mapped
    raise ValueError(f"Unsupported author_type '{raw}'. Choose one of: {', '.join(AUTHOR_TYPES)}")


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _save_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)


def _read_jsonl(path: Path) -> list[dict]:
    if not path.is_file():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _save_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
    tmp.replace(path)


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _sha256_file(path: Path) -> str:
    with path.open("rb") as f:
        return hashlib.file_digest(f, "sha256").hexdigest()


def _check_txt_location(txt_path: Path, repo_root: Path) -> None:
    resolved = txt_path.resolve()
    if not resolved.is_file():
        raise ValueError(f"Source TXT file not found: {txt_path}")
    repo_resolved = repo_root.resolve()
    if resolved.is_relative_to(repo_resolved):
        rel = resolved.relative_to(repo_resolved)
        parts = rel.parts
        allowed = (
            parts[0] in {"books", "reading-library"}
            or (len(parts) >= 3 and parts[0] == "cases" and parts[2] == "input")
            or ("output" in parts)
        )
        if not allowed:
            raise ValueError(
                f"Copyright guard: {rel} is inside the repository but not in an ignored input/ directory. "
                "Move the source TXT into cases/<slug>/input/ or outside the repository."
            )


def init_case(
    case_dir: Path,
    *,
    book: str,
    author: str,
    publication_year: int,
    domain: str,
    author_type: str,
    cutoff: str | None = None,
    execution_mode: str = "agent-native-v5",
    source_note: str = "",
) -> dict:
    case_dir = case_dir.resolve()
    slug = case_dir.name
    if not SLUG_RE.fullmatch(slug):
        raise ValueError(f"Invalid case slug '{slug}'. Must match {SLUG_RE.pattern} (e.g. author-book-v5)")
    cutoff_val = cutoff or date.today().isoformat()
    date.fromisoformat(cutoff_val)
    if not (1 <= publication_year <= 9999):
        raise ValueError(f"Invalid publication year: {publication_year}")
    norm_domain = normalize_domain(domain)
    norm_author_type = normalize_author_type(author_type)
    if (case_dir / "config.json").exists() or (case_dir / "data/claims.jsonl").exists():
        raise ValueError(f"Case already exists at {case_dir}")

    (case_dir / "data/sources").mkdir(parents=True, exist_ok=True)
    (case_dir / "input").mkdir(parents=True, exist_ok=True)
    (case_dir / "output").mkdir(parents=True, exist_ok=True)

    cfg = {
        "book": book.strip(),
        "author": author.strip(),
        "cutoff": cutoff_val,
        "publication_year_proxy": publication_year,
        "rules_version": "simple-v3-trend-four-class",
        "domain": norm_domain,
        "author_type": norm_author_type,
        "execution_mode": execution_mode,
        "community_contribution": True,
    }
    if source_note.strip():
        cfg["publication_year_note"] = source_note.strip()
    _save_json(case_dir / "config.json", cfg)
    _save_jsonl(case_dir / "data/claims.jsonl", [])
    _save_jsonl(case_dir / "data/evidence.jsonl", [])
    return cfg


def chunk_txt_for_agent(
    case_dir: Path,
    txt_path: Path,
    *,
    encoding: str | None = None,
    chunk_chars: int = 3500,
    context_chars: int = 600,
    batch_size: int = 5,
    include_front_matter: bool = False,
    repo_root: Path = REPO_ROOT,
) -> dict:
    if batch_size < 1:
        raise ValueError("batch_size must be >= 1")
    case_dir = case_dir.resolve()
    cfg_path = case_dir / "config.json"
    if not cfg_path.is_file():
        raise ValueError(f"Missing config.json in {case_dir}")
    _check_txt_location(txt_path, repo_root)

    raw, text, codec = pb.decode_text(txt_path, encoding)
    raw_sha = _sha256_bytes(raw)
    spans = [] if include_front_matter else pb.matter_spans(text)
    chunks = pb.split_text(text, chunk_chars=chunk_chars, context_chars=context_chars)
    skipped = [c["id"] for c in chunks if any(a <= c["char_start"] and c["char_end"] <= b for a, b, _ in spans)]
    active_chunks = [c for c in chunks if c["id"] not in skipped]
    for c in active_chunks:
        c["body_sha256_12"] = _sha256_bytes((c.get("body") or "").encode("utf-8"))[:12]

    out_dir = case_dir / "output/txt_import"
    (out_dir / "chunk_proposals").mkdir(parents=True, exist_ok=True)
    batches_dir = out_dir / "batches"
    if batches_dir.exists():
        for old in batches_dir.glob("*.jsonl"):
            old.unlink()
    batches_dir.mkdir(parents=True, exist_ok=True)
    batch_meta: list[dict] = []
    for idx in range(0, len(active_chunks), batch_size):
        slice_chunks = active_chunks[idx : idx + batch_size]
        bid = f"batch-{(idx // batch_size) + 1:04d}"
        bfile = batches_dir / f"{bid}.jsonl"
        _save_jsonl(bfile, slice_chunks)
        batch_meta.append({
            "batch_id": bid,
            "path": f"output/txt_import/batches/{bid}.jsonl",
            "chunk_ids": [c["id"] for c in slice_chunks],
            "count": len(slice_chunks),
        })

    _save_jsonl(out_dir / "chunks.jsonl", active_chunks)
    (out_dir / "prompt_v5.txt").write_text(pb.DISCOVER_PROMPT_V5 + "\n", encoding="utf-8")

    manifest = {
        "source_sha256": raw_sha,
        "encoding": codec,
        "characters": len(text),
        "lines": text.count("\n") + 1,
        "total_chunks": len(chunks),
        "active_chunks": len(active_chunks),
        "skipped_matter_chunks": skipped,
        "active_chunk_ids": [c["id"] for c in active_chunks],
        "chunk_chars": chunk_chars,
        "context_chars": context_chars,
        "batch_size": batch_size,
        "batches": batch_meta,
        "extraction_version": pb.EXTRACTION_VERSION,
    }
    _save_json(out_dir / "manifest.json", manifest)

    cfg = _read_json(cfg_path)
    cfg["source_sha256"] = raw_sha
    cfg["source_txt_sha256"] = raw_sha
    cfg["source_txt_bytes"] = len(raw)
    _save_json(cfg_path, cfg)
    return manifest


def _find_span(haystack: str, needle: str) -> tuple[int, int] | None:
    if not needle:
        return None
    pos = haystack.find(needle)
    if pos >= 0:
        return (pos, pos + len(needle))
    # Fallback via normalized_index if whitespace/punctuation folded
    norm_h, idx_h = pb.normalized_index(haystack)
    norm_n = pb.normalize_for_match(needle)
    if not norm_n:
        return None
    n_pos = norm_h.find(norm_n)
    if n_pos >= 0:
        return (idx_h[n_pos], idx_h[n_pos + len(norm_n) - 1] + 1)
    return None


def _merge_spans(spans: list[tuple[int, int]], length: int, radius: int) -> list[tuple[int, int]]:
    expanded = [(max(0, a - radius), min(length, b + radius)) for a, b in spans]
    expanded.sort()
    merged: list[tuple[int, int]] = []
    for a, b in expanded:
        if merged and a <= merged[-1][1] + 20:
            merged[-1] = (merged[-1][0], max(merged[-1][1], b))
        else:
            merged.append((a, b))
    return merged


def trim_claim_context(claim: dict, cfg: dict, *, max_context_chars: int = 1200) -> dict:
    """Trim claim['context'] so copyright-protected full text is never committed,
    while preserving 100% of reference_resolutions support spans and updating provenance.
    """
    ctx = claim.get("context") or ""
    quote = claim.get("quote") or ""
    extra = claim.get("extraction_v2") or {}
    refs = extra.get("reference_resolutions") or []

    if not ctx:
        return claim

    needed_needles: list[str] = []
    for ref in refs:
        if isinstance(ref, dict):
            for k in ("expression", "support_quote"):
                val = ref.get(k) or ""
                if val and val not in quote and not pb.norm_contains(val, quote):
                    needed_needles.append(val)

    if not needed_needles:
        # Keep only a tiny local window around quote, or empty string
        q_span = _find_span(ctx, quote)
        if q_span:
            a = max(0, q_span[0] - 120)
            b = min(len(ctx), q_span[1] + 120)
            trimmed = ctx[a:b]
        else:
            trimmed = ""
    else:
        spans: list[tuple[int, int]] = []
        for needle in needed_needles:
            sp = _find_span(ctx, needle)
            if sp:
                spans.append(sp)
        q_span = _find_span(ctx, quote)
        if q_span:
            spans.append(q_span)
        if not spans:
            trimmed = ctx[:max_context_chars]
        else:
            radius = 80
            while radius >= 0:
                merged = _merge_spans(spans, len(ctx), radius)
                candidate = "\n…\n".join(ctx[a:b] for a, b in merged)
                if len(candidate) <= max_context_chars or radius == 0:
                    trimmed = candidate[:max_context_chars] if len(candidate) > max_context_chars else candidate
                    break
                radius //= 2
            # Verify expansion still passes; if over-trimmed, fall back to exact minimal slices
            try:
                pb.validate_expansion(extra, quote + "\n" + trimmed, normalized=True)
            except ValueError:
                minimal = "\n…\n".join(ctx[a:b] for a, b in _merge_spans(spans, len(ctx), 10))
                trimmed = minimal

    claim["context"] = trimmed
    raw_sha = (claim.get("source_location") or {}).get("source_sha256")
    if isinstance(extra, dict) and isinstance(raw_sha, str) and len(raw_sha) == 64 and extra.get("provenance"):
        extra["provenance"] = pb.extraction_provenance(claim, cfg, raw_sha)
    return claim


def trim_case_contexts(case_dir: Path) -> dict:
    case_dir = case_dir.resolve()
    cfg = _read_json(case_dir / "config.json")
    claims_path = case_dir / "data/claims.jsonl"
    rows = _read_jsonl(claims_path)
    trimmed_count = 0
    for c in rows:
        before = len(c.get("context") or "")
        trim_claim_context(c, cfg)
        if len(c.get("context") or "") != before:
            trimmed_count += 1
        if "expanded_claim" in (c.get("extraction_v2") or {}):
            pb.validate_expansion(c["extraction_v2"], (c.get("quote") or "") + "\n" + (c.get("context") or ""), normalized=True)
    _save_jsonl(claims_path, rows)
    return {"claims": len(rows), "trimmed": trimmed_count}


def _load_chunk_proposals(proposals_path: Path) -> list[dict]:
    if proposals_path.is_dir():
        items = []
        for p in sorted(proposals_path.glob("*.json")):
            obj = _read_json(p)
            if isinstance(obj, dict) and "items" in obj and isinstance(obj["items"], list):
                items.extend(obj["items"])
            elif isinstance(obj, list):
                items.extend(obj)
            elif isinstance(obj, dict) and "id" in obj:
                items.append(obj)
            else:
                raise ValueError(f"Unrecognized chunk proposal format in {p}")
        return items
    text = proposals_path.read_text(encoding="utf-8").strip()
    if not text:
        return []
    if text.startswith("["):
        return json.loads(text)
    if text.startswith("{"):
        try:
            obj = json.loads(text)
            if isinstance(obj, dict) and "items" in obj and isinstance(obj["items"], list):
                return obj["items"]
            if isinstance(obj, dict) and "id" in obj:
                return [obj]
        except json.JSONDecodeError:
            pass
    return [json.loads(line) for line in text.splitlines() if line.strip()]


def _verify_proof_of_reading(item: dict, chunk: dict, *, require_proof: bool = False) -> dict:
    """Anti-laziness check: validate that the worker agent actually read the chunk body.
    Verifies body_sha256_12 and tail_anchor (a verbatim >=8 char snippet from the last 35% of body).
    """
    body = chunk.get("body") or ""
    expected_sha12 = chunk.get("body_sha256_12") or _sha256_bytes(body.encode("utf-8"))[:12]
    provided_sha12 = (item.get("body_sha256_12") or "").strip()
    tail_anchor = (item.get("tail_anchor") or "").strip()

    if require_proof and not provided_sha12:
        raise ValueError(f"Lazy agent guard: chunk {chunk['id']} missing body_sha256_12 proof of reading")
    if provided_sha12 and provided_sha12 != expected_sha12:
        raise ValueError(
            f"Lazy agent guard: chunk {chunk['id']} body_sha256_12 mismatch "
            f"(got '{provided_sha12}', expected '{expected_sha12}')"
        )

    if require_proof and not tail_anchor:
        raise ValueError(f"Lazy agent guard: chunk {chunk['id']} missing tail_anchor proof of reading")
    if tail_anchor:
        norm_anchor = pb.normalize_for_match(tail_anchor)
        if len(norm_anchor) < 6:
            raise ValueError(f"Lazy agent guard: chunk {chunk['id']} tail_anchor too short (<6 normalized chars)")
        tail_start = max(0, int(len(body) * 0.55))
        tail_region = body[tail_start:]
        if tail_anchor not in tail_region and not pb.norm_contains(tail_anchor, tail_region):
            if tail_anchor in body or pb.norm_contains(tail_anchor, body):
                raise ValueError(
                    f"Lazy agent guard: chunk {chunk['id']} tail_anchor found in early text, not in the last 45% of body"
                )
            raise ValueError(f"Lazy agent guard: chunk {chunk['id']} tail_anchor not found in chunk body")
    return {
        "chunk_id": chunk["id"],
        "sha12_verified": bool(provided_sha12),
        "tail_anchor_verified": bool(tail_anchor),
    }


def import_agent_extractions(
    case_dir: Path,
    txt_path: Path,
    proposals_path: Path,
    *,
    encoding: str | None = None,
    include_front_matter: bool = False,
    require_proof: bool = False,
    repo_root: Path = REPO_ROOT,
) -> dict:
    case_dir = case_dir.resolve()
    cfg = _read_json(case_dir / "config.json")
    claims_path = case_dir / "data/claims.jsonl"
    if _read_jsonl(claims_path):
        raise ValueError("data/claims.jsonl is non-empty; refusing to overwrite existing claims")
    _check_txt_location(txt_path, repo_root)

    manifest_path = case_dir / "output/txt_import/manifest.json"
    chunks_path = case_dir / "output/txt_import/chunks.jsonl"
    if not manifest_path.is_file() or not chunks_path.is_file():
        raise ValueError("Run 'chunk-txt' before 'import-extractions'")
    manifest = _read_json(manifest_path)
    chunks = _read_jsonl(chunks_path)

    raw, text, _ = pb.decode_text(txt_path, encoding)
    raw_sha = _sha256_bytes(raw)
    if raw_sha != manifest["source_sha256"]:
        raise ValueError("Source TXT SHA-256 does not match chunk-txt manifest")

    items = _load_chunk_proposals(proposals_path)
    by_id = {c["id"]: c for c in chunks}
    seen_ids = [item.get("id") for item in items]
    if len(seen_ids) != len(set(seen_ids)):
        raise ValueError("Duplicate chunk IDs in proposals")
    if set(seen_ids) != set(by_id):
        missing = sorted(set(by_id) - set(seen_ids))
        extra = sorted(set(seen_ids) - set(by_id))
        raise ValueError(f"Chunk coverage mismatch: missing={missing[:5]} extra={extra[:5]}")

    all_rejected = []
    proof_verified = 0
    for item in items:
        chunk = by_id[item["id"]]
        proof = _verify_proof_of_reading(item, chunk, require_proof=require_proof)
        if proof["sha12_verified"] and proof["tail_anchor_verified"]:
            proof_verified += 1
        preds = item.get("predictions")
        if not isinstance(preds, list):
            raise ValueError(f"predictions must be a list for chunk {item['id']}")
        kept, rejected = pb.validate_chunk_predictions(preds, chunk)
        item["predictions"] = kept
        for r in rejected:
            all_rejected.append({"chunk": item["id"], **r})

    spans = [] if include_front_matter else pb.matter_spans(text)
    policy: dict = {}
    claims = pb.claims_from_results(items, chunks, text, raw_sha, cfg, spans=spans, report=policy)
    for c in claims:
        trim_claim_context(c, cfg)

    _save_jsonl(claims_path, claims)
    _save_json(case_dir / "output/txt_import/policy_report.json", policy)
    _save_jsonl(case_dir / "output/txt_import/rejected_predictions.jsonl", all_rejected)
    return {
        "imported_claims": len(claims),
        "rejected_quotes": len(all_rejected),
        "excluded_non_predictions": len(policy.get("excluded") or []),
        "overlap_duplicates_dropped": policy.get("duplicates", 0),
        "proof_of_reading_verified_chunks": proof_verified,
    }


def _build_verify_prompt_v3() -> str:
    return (
        "# Forecast Lab: search-verifier-v3 多轮双向搜证 + 自适应变策补搜 + 独立六维语义复核规范\n\n"
        "## 一、检索规划与多轮自适应变策规则 (PLAN)\n"
        f"{vp.PLAN}\n\n"
        "## 二、初判评估、逐证据原句绑定与决定性缺口规则 (ASSESS)\n"
        f"{vp.ASSESS}\n\n"
        "## 三、独立六维语义复核规则 (SEMANTIC REVIEW)\n"
        f"{sr.REVIEW_PROMPT}\n\n"
        "## 四、唯一一次修订规则 (REVISION)\n"
        f"{sr.REVISION_PROMPT}\n"
    )


def export_verify_tasks(case_dir: Path, output_path: Path | None = None, *, batch_size: int = 4) -> dict:
    if batch_size < 1:
        raise ValueError("batch_size must be >= 1")
    case_dir = case_dir.resolve()
    cfg = _read_json(case_dir / "config.json")
    rows = _read_jsonl(case_dir / "data/claims.jsonl")
    tasks = []
    for c in rows:
        if c.get("duplicate_of"):
            continue
        if c.get("kind") != "prediction":
            continue
        ext = c.get("extraction_v2") or {}
        tasks.append({
            "id": c["id"],
            "book": cfg["book"],
            "author": cfg.get("author", ""),
            "publication_year_proxy": cfg.get("publication_year_proxy"),
            "cutoff": cfg["cutoff"],
            "quote": c.get("quote", ""),
            "context": c.get("context", ""),
            "expanded_claim": ext.get("expanded_claim") or c.get("claim", ""),
            "time_text": c.get("time_text", ""),
            "horizon": ext.get("horizon", ""),
            "horizon_source": ext.get("horizon_source", ""),
            "condition_text": c.get("condition_text", ""),
            "method": c.get("method", ""),
            "method_basis": c.get("method_basis", "unknown"),
        })
    out = output_path or (case_dir / "output/verify_tasks.jsonl")
    _save_jsonl(out, tasks)
    sverify_dir = case_dir / "output/search_verify"
    sverify_dir.mkdir(parents=True, exist_ok=True)
    (sverify_dir / "verify_prompt_v3.txt").write_text(_build_verify_prompt_v3(), encoding="utf-8")

    vbatches_dir = case_dir / "output/verify_batches"
    if vbatches_dir.exists():
        for old in vbatches_dir.glob("*.jsonl"):
            old.unlink()
    vbatches_dir.mkdir(parents=True, exist_ok=True)
    (case_dir / "output/verify_proposals").mkdir(parents=True, exist_ok=True)
    (case_dir / "output/evidence_proposals").mkdir(parents=True, exist_ok=True)
    (case_dir / "output/semantic_reviews").mkdir(parents=True, exist_ok=True)

    batch_meta: list[dict] = []
    for idx in range(0, len(tasks), batch_size):
        slice_tasks = tasks[idx : idx + batch_size]
        bid = f"vbatch-{(idx // batch_size) + 1:04d}"
        bfile = vbatches_dir / f"{bid}.jsonl"
        _save_jsonl(bfile, slice_tasks)
        batch_meta.append({
            "batch_id": bid,
            "path": f"output/verify_batches/{bid}.jsonl",
            "claim_ids": [t["id"] for t in slice_tasks],
            "count": len(slice_tasks),
        })
    vmanifest = {
        "version": vp.VERSION,
        "adaptive_rounds_limit": vp.ADAPTIVE_ROUNDS,
        "adaptive_searches_per_round": vp.ADAPTIVE_SEARCHES,
        "tasks": len(tasks),
        "total_claims": len(rows),
        "batch_size": batch_size,
        "batches": batch_meta,
    }
    _save_json(case_dir / "output/verify_manifest.json", vmanifest)
    return {"tasks": len(tasks), "output": str(out), "total_claims": len(rows), "batches": len(batch_meta)}


def _load_records_file_or_dir(path: Path) -> list[dict]:
    if path.is_dir():
        rows = []
        for p in sorted(list(path.glob("*.json")) + list(path.glob("*.jsonl"))):
            if p.suffix == ".jsonl":
                rows.extend(_read_jsonl(p))
            else:
                obj = _read_json(p)
                if isinstance(obj, list):
                    rows.extend(obj)
                elif isinstance(obj, dict) and "items" in obj and isinstance(obj["items"], list):
                    rows.extend(obj["items"])
                elif isinstance(obj, dict):
                    rows.append(obj)
        return rows
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        return []
    if text.startswith("["):
        return json.loads(text)
    if text.startswith("{"):
        try:
            obj = json.loads(text)
            if isinstance(obj, dict) and "items" in obj and isinstance(obj["items"], list):
                return obj["items"]
            if isinstance(obj, dict):
                return [obj]
        except json.JSONDecodeError:
            pass
    return [json.loads(line) for line in text.splitlines() if line.strip()]


def _register_raw_evidence(case_dir: Path, raw_records: list[dict], cutoff: str) -> int:
    ev_path = case_dir / "data/evidence.jsonl"
    existing = {e["id"]: e for e in _read_jsonl(ev_path)}
    cutoff_date = date.fromisoformat(cutoff)
    added = 0
    for rec in raw_records:
        eid = rec.get("id")
        url = rec.get("url")
        text = rec.get("text") or rec.get("content") or ""
        if not isinstance(eid, str) or not eid.strip():
            raise ValueError("Evidence record missing id")
        if not vp.public_url(url):
            raise ValueError(f"Evidence {eid} has invalid or non-public URL: {url}")
        if not isinstance(text, str) or not text.strip():
            raise ValueError(f"Evidence {eid} missing full archived text")
        pub_date = rec.get("date")
        if isinstance(pub_date, str) and len(pub_date) >= 10 and pub_date[4:5] == "-" and pub_date[7:8] == "-":
            if date.fromisoformat(pub_date[:10]) > cutoff_date:
                raise ValueError(f"Evidence {eid} date {pub_date} is after cutoff {cutoff}")
        archive_rel = Path("data/sources") / f"{eid}.txt"
        archive_abs = case_dir / archive_rel
        archive_abs.parent.mkdir(parents=True, exist_ok=True)
        archive_abs.write_text(text, encoding="utf-8")
        digest = _sha256_file(archive_abs)
        existing[eid] = {
            "id": eid,
            "url": url,
            "date": pub_date or None,
            "coverage": rec.get("coverage") or "",
            "excerpt": rec.get("excerpt") or text[:400],
            "limitation": rec.get("limitation") or "公开权威网页/文献存档，仅支持所引事实。",
            "local_archive": archive_rel.as_posix(),
            "sha256": digest,
            "verified": True,
        }
        added += 1
    _save_jsonl(ev_path, [existing[k] for k in sorted(existing)])
    return added


def _default_excluded_assessment(claim: dict) -> dict:
    inclusion = "duplicate" if claim.get("duplicate_of") else "nonforecast"
    return {
        "id": claim["id"],
        "inclusion": inclusion,
        "verdict": None,
        "basis": "excluded",
        "scope": "按 v5 规则归类为非可评分预测或重复条目，不计入命中率分母。",
        "reason": "抽取阶段识别为非预测、不可解或重复候选，依 METHOD.md 保留审计记录并排除。",
        "limitation": "排除条目不参与准确度计分。",
        "evidence_ids": [],
        "method": claim.get("method") or "unknown",
        "method_basis": claim.get("method_basis") or "unknown",
        "observation_end": None,
        "future_time_text": "",
        "condition_state": "unconditional",
        "trend_aligned": False,
    }


def _run_pipeline(case_dir: Path, *args: str) -> None:
    pl.main(["--case", str(case_dir), *args])


def _validate_search_Verifier_v3_proposal(
    prop: dict,
    claim: dict,
    raw_ev_by_id: dict[str, dict],
    cutoff: str,
    *,
    require_dual_evidence: bool = False,
    require_adaptive_rounds: bool = False,
    review_item: dict | None = None,
) -> dict:
    """Validate an agent verification proposal against search-verifier-v3 multi-round & semantic-review rules."""
    cid = claim["id"]
    verdict = prop.get("verdict")
    eids = prop.get("evidence_ids") or []
    notes = prop.get("evidence_notes")
    round_history = prop.get("round_history")

    # 1. Dual-evidence & archive depth check for decided forecasts
    if require_dual_evidence and prop.get("inclusion") == "forecast" and verdict != "暂无法判断":
        if len(eids) < 2:
            raise ValueError(
                f"Lazy agent guard: decided forecast {cid} must cite at least 2 independent evidence items "
                f"(supporting + counter/context), got {len(eids)}"
            )
        for eid in eids:
            rec = raw_ev_by_id.get(eid)
            if rec is not None and len((rec.get("text") or rec.get("content") or "").strip()) < 60:
                raise ValueError(
                    f"Lazy agent guard: evidence {eid} for {cid} has archived text < 60 chars (too shallow)"
                )

    # 2. Verbatim evidence_notes alignment check (mirrors verify_prediction.inspect_assessment)
    if isinstance(notes, list) and notes:
        notes_by_eid = {}
        for note in notes:
            if not isinstance(note, dict) or not isinstance(note.get("evidence_id"), str):
                raise ValueError(f"Invalid evidence_note in {cid}")
            neid = note["evidence_id"]
            if note.get("relation") not in {"support", "counter", "boundary", "background"}:
                raise ValueError(f"Invalid evidence_note relation '{note.get('relation')}' for {cid}")
            rec = raw_ev_by_id.get(neid)
            if rec is not None:
                src_text = rec.get("text") or rec.get("content") or ""
                nquote = (note.get("quote") or "").strip()
                if not nquote:
                    raise ValueError(f"Empty quote in evidence_note {neid} for {cid}")
                if nquote not in src_text:
                    try:
                        note["quote"] = sr.align_quote(nquote, src_text)
                    except ValueError as exc:
                        raise ValueError(
                            f"Lazy agent guard: evidence_note quote for {neid} in {cid} not found in archived source text"
                        ) from exc
            notes_by_eid[neid] = note
        if require_adaptive_rounds and any(eid not in notes_by_eid for eid in eids):
            raise ValueError(f"Lazy agent guard: {cid} missing evidence_notes entry for cited evidence_ids")
    elif require_adaptive_rounds and eids:
        raise ValueError(f"Lazy agent guard: {cid} must provide evidence_notes with verbatim quotes for cited evidence_ids")

    # 3. Multi-round initial + adaptive search check (mirrors verify_prediction.py search-verifier-v3)
    adaptive_count = 0
    if isinstance(round_history, list) and round_history:
        seen_q_norms: set[str] = set()
        seen_strategies: set[str] = set()
        initial_rounds = [r for r in round_history if isinstance(r, dict) and r.get("kind") == "initial"]
        adaptive_rounds = [r for r in round_history if isinstance(r, dict) and r.get("kind") == "adaptive"]
        adaptive_count = len(adaptive_rounds)

        if not initial_rounds:
            raise ValueError(f"Multi-round guard: {cid} round_history must start with at least 1 initial round")
        first_queries = initial_rounds[0].get("queries") or []
        first_roles = {q.get("role") for q in first_queries if isinstance(q, dict)}
        if first_roles != {"support", "counter"}:
            raise ValueError(
                f"Multi-round guard: {cid} initial round 1 must include both 'support' and 'counter' queries"
            )
        for r in initial_rounds:
            for q in (r.get("queries") or []):
                if isinstance(q, dict) and isinstance(q.get("query"), str) and q["query"].strip():
                    seen_q_norms.add(vp.normalize_query(q["query"]))

        if adaptive_count > vp.ADAPTIVE_ROUNDS:
            raise ValueError(f"Multi-round guard: {cid} exceeded ADAPTIVE_ROUNDS={vp.ADAPTIVE_ROUNDS}")

        for idx, ar in enumerate(adaptive_rounds, start=1):
            gap_before = (ar.get("gap_before") or "").strip()
            strat_change = (ar.get("strategy_change") or "").strip()
            if not gap_before:
                raise ValueError(f"Multi-round guard: {cid} adaptive round {idx} missing gap_before (decisive_gap)")
            if not strat_change:
                raise ValueError(f"Multi-round guard: {cid} adaptive round {idx} missing strategy_change")
            if strat_change in seen_strategies:
                raise ValueError(f"Multi-round guard: {cid} adaptive round {idx} repeated strategy_change")
            seen_strategies.add(strat_change)

            aqueries = ar.get("queries") or []
            if not aqueries:
                if not ar.get("stopped"):
                    raise ValueError(
                        f"Multi-round guard: {cid} adaptive round {idx} has empty queries without stopped reason"
                    )
                continue
            if len(aqueries) > vp.ADAPTIVE_SEARCHES:
                raise ValueError(f"Multi-round guard: {cid} adaptive round {idx} > {vp.ADAPTIVE_SEARCHES} queries")
            for q in aqueries:
                if not isinstance(q, dict) or q.get("role") not in {"support", "counter"}:
                    raise ValueError(f"Multi-round guard: {cid} adaptive query missing valid role")
                qtext = (q.get("query") or "").strip()
                qstrat = (q.get("strategy") or "").strip()
                if not qtext or not qstrat:
                    raise ValueError(f"Multi-round guard: {cid} adaptive query must specify both query and strategy")
                qnorm = vp.normalize_query(qtext)
                if qnorm in seen_q_norms:
                    raise ValueError(
                        f"Multi-round guard: {cid} adaptive round {idx} repeated prior query '{qtext}'"
                    )
                seen_q_norms.add(qnorm)
    elif require_adaptive_rounds and prop.get("inclusion") == "forecast":
        raise ValueError(f"Multi-round guard: forecast {cid} missing round_history trace")

    # If verdict is still '暂无法判断', enforce specific remaining_gap AND multi-round adaptive search
    if prop.get("inclusion") == "forecast" and verdict == "暂无法判断":
        rem_gap = (prop.get("remaining_gap") or "").strip()
        if require_adaptive_rounds and not rem_gap:
            raise ValueError(f"Multi-round guard: unresolved forecast {cid} must specify a concrete remaining_gap")
        if require_adaptive_rounds and prop.get("basis") != "future":
            # Must have executed at least 2 adaptive rounds (or 1+ adaptive round with explicit stopped reason)
            has_stopped = any(
                isinstance(r, dict) and r.get("kind") == "adaptive" and bool(r.get("stopped"))
                for r in (round_history or [])
            )
            if adaptive_count < 2 and not (adaptive_count >= 1 and has_stopped):
                raise ValueError(
                    f"Multi-round guard: unresolved forecast {cid} (verdict='暂无法判断', basis='{prop.get('basis')}') "
                    f"only ran {adaptive_count} adaptive round(s). Must run at least 2 adaptive rounds with new "
                    f"strategy_change & non-duplicate queries (up to {vp.ADAPTIVE_ROUNDS} adaptive rounds) before concluding '暂无法判断'."
                )

    # 4. Independent 6-check semantic review validation (mirrors semantic_review.validate_review)
    rev_validated = False
    if review_item is not None:
        source_texts = {
            eid: (raw_ev_by_id[eid].get("text") or raw_ev_by_id[eid].get("content") or "")
            for eid in eids
            if eid in raw_ev_by_id
        }
        orig_text = (claim.get("quote") or "") + "\n" + (claim.get("context") or "")
        prop_text = "\n".join(str(prop.get(k) or "") for k in ("scope", "reason", "limitation", "observation_end"))
        validated_rev = sr.validate_review(review_item, cid, source_texts, orig_text, prop_text)
        if validated_rev["decision"] == "revise":
            raise ValueError(
                f"Semantic review guard: {cid} has unaddressed review decision='revise'; run revision + round-2 review"
            )
        if validated_rev["decision"] == "unresolved" and verdict != "暂无法判断":
            raise ValueError(
                f"Semantic review guard: {cid} reviewer decision='unresolved' but assessment verdict='{verdict}'"
            )
        rev_validated = True

    return {"adaptive_rounds": adaptive_count, "semantic_review_verified": rev_validated}


def apply_agent_assessments(
    case_dir: Path,
    assessments_path: Path,
    *,
    evidence_raw_path: Path | None = None,
    semantic_reviews_path: Path | None = None,
    require_dual_evidence: bool = False,
    require_adaptive_rounds: bool = False,
    require_semantic_review: bool = False,
) -> dict:
    case_dir = case_dir.resolve()
    cfg = _read_json(case_dir / "config.json")
    ev_added = 0
    raw_ev_by_id: dict[str, dict] = {}
    if evidence_raw_path is not None:
        raw_ev = _load_records_file_or_dir(evidence_raw_path)
        for r in raw_ev:
            if isinstance(r.get("id"), str):
                raw_ev_by_id[r["id"]] = r
        ev_added = _register_raw_evidence(case_dir, raw_ev, cfg["cutoff"])

    for e in _read_jsonl(case_dir / "data/evidence.jsonl"):
        eid = e["id"]
        if eid not in raw_ev_by_id:
            arch = case_dir / (e.get("local_archive") or "")
            txt = arch.read_text(encoding="utf-8") if arch.is_file() else (e.get("excerpt") or "")
            raw_ev_by_id[eid] = {**e, "text": txt}

    reviews_by_id: dict[str, dict] = {}
    rev_path = semantic_reviews_path or (case_dir / "output/semantic_reviews")
    if rev_path and rev_path.exists():
        for rev in _load_records_file_or_dir(rev_path):
            if isinstance(rev, dict) and isinstance(rev.get("id"), str):
                reviews_by_id[rev["id"]] = rev

    claims = _read_jsonl(case_dir / "data/claims.jsonl")
    proposals = _load_records_file_or_dir(assessments_path)
    by_id = {p["id"]: p for p in proposals}
    full_proposals = []
    dual_verified = 0
    adaptive_verified = 0
    review_verified = 0
    for c in claims:
        if c["id"] in by_id:
            prop = by_id[c["id"]]
            rev_item = reviews_by_id.get(c["id"]) or (prop.get("semantic_review") if isinstance(prop.get("semantic_review"), dict) else None)
            if require_semantic_review and prop.get("inclusion") == "forecast" and rev_item is None:
                raise ValueError(f"Semantic review guard: missing 6-check semantic review for forecast {c['id']}")
            vstat = _validate_search_Verifier_v3_proposal(
                prop,
                c,
                raw_ev_by_id,
                cfg["cutoff"],
                require_dual_evidence=require_dual_evidence,
                require_adaptive_rounds=require_adaptive_rounds,
                review_item=rev_item if (require_semantic_review or rev_item is not None) else None,
            )
            if require_dual_evidence and prop.get("inclusion") == "forecast" and prop.get("verdict") != "暂无法判断":
                dual_verified += 1
            if isinstance(prop.get("round_history"), list) and prop.get("round_history"):
                adaptive_verified += 1
            if vstat["semantic_review_verified"]:
                review_verified += 1
            full_proposals.append(prop)
        elif c.get("duplicate_of") or c.get("kind") != "prediction":
            full_proposals.append(_default_excluded_assessment(c))
        else:
            raise ValueError(f"Missing assessment for forecast claim {c['id']}")

    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".jsonl", delete=False) as tmp:
        tmp_path = Path(tmp.name)
        tmp.write("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in full_proposals))
    try:
        _run_pipeline(case_dir, "apply", "assess", str(tmp_path))
        _run_pipeline(case_dir, "report")
        _run_pipeline(case_dir, "check")
    finally:
        tmp_path.unlink(missing_ok=True)
    return {
        "evidence_registered": ev_added,
        "assessments_applied": len(full_proposals),
        "dual_evidence_verified": dual_verified,
        "multi_round_traces_verified": adaptive_verified,
        "semantic_reviews_verified": review_verified,
    }


def import_verify_run(case_dir: Path, search_run_dir: Path | None = None) -> dict:
    case_dir = case_dir.resolve()
    cfg = _read_json(case_dir / "config.json")
    run_dir = (search_run_dir or (case_dir / "output/search_verify")).resolve()
    results_file = run_dir / "results.jsonl"
    if not results_file.is_file():
        raise ValueError(f"results.jsonl not found in {run_dir}")
    results = _read_jsonl(results_file)
    incomplete = [r.get("claim_id") for r in results if r.get("task_state") != "completed" or not r.get("assessment")]
    if incomplete:
        raise ValueError(f"Verify run has incomplete tasks ({len(incomplete)}), e.g. {incomplete[:3]}. Resume before importing.")

    ev_path = case_dir / "data/evidence.jsonl"
    ev_map = {e["id"]: e for e in _read_jsonl(ev_path)}
    new_ev_count = 0
    proposals_by_id: dict[str, dict] = {}

    for res in results:
        asm = dict(res["assessment"])
        cand_map = {c["id"]: c for c in (res.get("evidence_candidates") or [])}
        notes_map = {n["evidence_id"]: n for n in (asm.get("evidence_notes") or []) if isinstance(n, dict) and n.get("evidence_id")}
        mapped_ids: list[str] = []
        for eid in asm.get("evidence_ids") or []:
            if eid in ev_map and ev_map[eid].get("verified"):
                mapped_ids.append(eid)
                continue
            cand = cand_map.get(eid)
            if not cand:
                raise ValueError(f"Referenced evidence {eid} not found in candidates or evidence.jsonl")
            prior_id = cand.get("prior_evidence_id")
            if prior_id and prior_id in ev_map and ev_map[prior_id].get("verified"):
                mapped_ids.append(prior_id)
                continue
            arch_rel = cand.get("archive_path")
            if not arch_rel or not (run_dir / arch_rel).is_file():
                raise ValueError(f"Missing archived source body for {eid} at {arch_rel}")
            raw_bytes = (run_dir / arch_rel).read_bytes()
            if cand.get("archive_sha256") and _sha256_bytes(raw_bytes) != cand["archive_sha256"]:
                raise ValueError(f"Archive SHA-256 mismatch for {eid}")
            dest_rel = Path("data/sources") / f"{eid}.txt"
            dest_abs = case_dir / dest_rel
            dest_abs.parent.mkdir(parents=True, exist_ok=True)
            dest_abs.write_bytes(raw_bytes)
            note = notes_map.get(eid) or {}
            pub_date = note.get("publication_date") or cand.get("published_date")
            if isinstance(pub_date, str) and len(pub_date) >= 10 and pub_date[4:5] == "-" and pub_date[7:8] == "-":
                if date.fromisoformat(pub_date[:10]) > date.fromisoformat(cfg["cutoff"]):
                    pub_date = None
            ev_map[eid] = {
                "id": eid,
                "url": cand["url"],
                "date": pub_date,
                "coverage": note.get("observation_end") or cfg["cutoff"],
                "excerpt": note.get("quote") or (cand.get("text") or "")[:400],
                "limitation": note.get("limitation") or "自动联网搜证与独立复核归档来源，仅作所引事实参考。",
                "local_archive": dest_rel.as_posix(),
                "sha256": _sha256_bytes(raw_bytes),
                "verified": True,
            }
            mapped_ids.append(eid)
            new_ev_count += 1
        asm["evidence_ids"] = list(dict.fromkeys(mapped_ids))
        proposals_by_id[asm["id"]] = asm

    _save_jsonl(ev_path, [ev_map[k] for k in sorted(ev_map)])

    claims = _read_jsonl(case_dir / "data/claims.jsonl")
    full_proposals = []
    for c in claims:
        if c["id"] in proposals_by_id:
            full_proposals.append(proposals_by_id[c["id"]])
        elif c.get("duplicate_of") or c.get("kind") != "prediction":
            full_proposals.append(_default_excluded_assessment(c))
        else:
            raise ValueError(f"Missing verify result for forecast claim {c['id']}")

    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".jsonl", delete=False) as tmp:
        tmp_path = Path(tmp.name)
        tmp.write("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in full_proposals))
    try:
        _run_pipeline(case_dir, "apply", "assess", str(tmp_path))
        _run_pipeline(case_dir, "report")
        _run_pipeline(case_dir, "check")
    finally:
        tmp_path.unlink(missing_ok=True)
    return {"new_evidence": new_ev_count, "assessments_applied": len(full_proposals)}


def _horizon_tier(window_years: int) -> str:
    if window_years <= 3:
        return "0–3年(超短窗)"
    if window_years <= 9:
        return "4–9年(中短窗)"
    if window_years <= 19:
        return "10–19年(中长窗)"
    if window_years <= 39:
        return "20–39年(长周期)"
    if window_years <= 99:
        return "40–99年(跨代)"
    return ">=100年(跨世纪)"


def _fmt_pct(num: int, den: int) -> str:
    if den <= 0:
        return ""
    return f"{(num / den) * 100:.1f}%"


def _fmt_weighted(correct: int, trend: int, partial: int, den: int) -> str:
    if den <= 0:
        return ""
    score = (correct + 0.75 * trend + 0.5 * partial) / den
    return f"{score * 100:.1f}%"


def _median_explicit_span(claims: list[dict], pub_year: int) -> str:
    spans: list[float] = []
    for c in claims:
        ext = c.get("extraction_v2") or {}
        if ext.get("horizon_source") != "explicit":
            continue
        text = (ext.get("horizon") or c.get("time_text") or "").strip()
        years = [int(y) for y in re.findall(r"(?<!\d)(1[5-9]\d\d|20\d\d|21\d\d)(?!\d)", text)]
        valid = [y - pub_year for y in years if y >= pub_year]
        if valid:
            spans.append(float(max(valid)))
            continue
        rel = re.search(r"(\d+)\s*(?:年|years?)", text, re.IGNORECASE)
        if rel:
            spans.append(float(int(rel.group(1))))
    if not spans:
        return ""
    med = statistics.median(spans)
    return str(int(med)) if med == int(med) else f"{med:.1f}"


def _subset_metrics(claims: list[dict], explicit: bool) -> tuple[int, str, str]:
    decided = correct = error = 0
    for c in claims:
        asm = c.get("assessment") or {}
        if asm.get("inclusion") != "forecast":
            continue
        v = pl.display_verdict(asm)
        if v == "暂无法判断" or v not in pl.DISPLAY_VERDICTS:
            continue
        ext = c.get("extraction_v2") or {}
        hs = ext.get("horizon_source")
        is_exp = (hs == "explicit") if hs else bool((c.get("time_text") or "").strip())
        if is_exp != explicit:
            continue
        decided += 1
        if v == "正确":
            correct += 1
        elif v == "错误":
            error += 1
    return decided, _fmt_pct(correct, decided), _fmt_pct(error, decided)


def _parse_pct(val: str) -> float | None:
    s = (val or "").replace("%", "").strip()
    return float(s) / 100.0 if s else None


def sync_database(case_dir: Path, *, repo_root: Path = REPO_ROOT, run_ranking: bool = True) -> dict:
    case_dir = case_dir.resolve()
    _run_pipeline(case_dir, "check")
    _run_pipeline(case_dir, "report")

    cfg = _read_json(case_dir / "config.json")
    claims = _read_jsonl(case_dir / "data/claims.jsonl")
    summary = _read_json(case_dir / "output/summary.json")

    slug = case_dir.name
    domain = normalize_domain(cfg.get("domain", ""))
    author_type = normalize_author_type(cfg.get("author_type", ""))
    pub_year = int(cfg["publication_year_proxy"])
    cutoff = cfg["cutoff"]
    window_years = max(0, int(cutoff[:4]) - pub_year)
    tier = _horizon_tier(window_years)

    dv = summary["display_verdicts"]
    forecast_n = int(summary["forecast_n"])
    decided_n = int(summary["decided_n"])
    correct = int(dv["正确"])
    trend = int(dv["趋势符合"])
    partial = int(dv["部分符合"])
    error = int(dv["错误"])
    unresolved = int(dv["暂无法判断"])
    nonforecast = int((summary.get("excluded") or {}).get("nonforecast", 0))

    mode = cfg.get("execution_mode", "")
    batch_tag = "v5_community_api" if "api" in mode.lower() else "v5_community_agent"

    exp_dec, exp_strict, exp_err = _subset_metrics(claims, explicit=True)
    imp_dec, imp_strict, imp_err = _subset_metrics(claims, explicit=False)

    new_row = {
        "slug": slug,
        "领域": domain,
        "作者类型": author_type,
        "作者": cfg.get("author", ""),
        "书名": cfg["book"],
        "出版年": str(pub_year),
        "截止日": cutoff,
        "观察窗口年数": str(window_years),
        "时间跨度分档": tier,
        "写明期限中位目标跨度年": _median_explicit_span(claims, pub_year),
        "批次口径": batch_tag,
        "预测数": str(forecast_n),
        "可判定数": str(decided_n),
        "正确": str(correct),
        "趋势符合": str(trend),
        "部分符合": str(partial),
        "错误": str(error),
        "暂无法判断": str(unresolved),
        "剔除非预测数": str(nonforecast),
        "严格胜率": _fmt_pct(correct, decided_n),
        "方向命中率": _fmt_pct(correct + trend, decided_n),
        "错误率": _fmt_pct(error, decided_n),
        "未定率": _fmt_pct(unresolved, forecast_n),
        "展示加权分_20261116口径": _fmt_weighted(correct, trend, partial, decided_n),
        "写明时间可判定数": str(exp_dec),
        "写明时间严格胜率": exp_strict,
        "写明时间错误率": exp_err,
        "隐含窗口可判定数": str(imp_dec),
        "隐含窗口严格胜率": imp_strict,
        "隐含窗口错误率": imp_err,
        "说明": cfg.get("publication_year_note", f"community PR ({batch_tag})"),
        "同档基准严格胜率": "",
        "同档超额严格胜率_pp": "",
        "同档基准方向命中率": "",
        "同档超额方向命中率_pp": "",
        "同档基准错误率": "",
        "同档低错优势_pp": "",
    }

    csv_path = repo_root / "datasets/all_cases_summary.csv"
    with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames or [])
        rows = list(reader)

    replaced = False
    for i, r in enumerate(rows):
        if r["slug"] == slug:
            rows[i] = new_row
            replaced = True
            break
    if not replaced:
        rows.append(new_row)

    # Recompute pooled baseline and excesses for the affected tier
    tier_rows = [r for r in rows if r["时间跨度分档"] == tier and int(r["可判定数"] or 0) > 0]
    if tier_rows:
        tot_dec = sum(int(r["可判定数"]) for r in tier_rows)
        tot_cor = sum(int(r["正确"]) for r in tier_rows)
        tot_dir = sum(int(r["正确"]) + int(r["趋势符合"]) for r in tier_rows)
        tot_err = sum(int(r["错误"]) for r in tier_rows)
        b_strict = tot_cor / tot_dec
        b_dir = tot_dir / tot_dec
        b_err = tot_err / tot_dec
        for r in rows:
            if r["时间跨度分档"] != tier:
                continue
            if int(r["可判定数"] or 0) <= 0:
                continue
            r["同档基准严格胜率"] = f"{b_strict * 100:.1f}%"
            r["同档基准方向命中率"] = f"{b_dir * 100:.1f}%"
            r["同档基准错误率"] = f"{b_err * 100:.1f}%"
            rs = _parse_pct(r["严格胜率"])
            rd = _parse_pct(r["方向命中率"])
            re_ = _parse_pct(r["错误率"])
            if rs is not None:
                r["同档超额严格胜率_pp"] = f"{(rs - b_strict) * 100:+.1f}pp"
            if rd is not None:
                r["同档超额方向命中率_pp"] = f"{(rd - b_dir) * 100:+.1f}pp"
            if re_ is not None:
                r["同档低错优势_pp"] = f"{(b_err - re_) * 100:+.1f}pp"

    tmp_csv = csv_path.with_suffix(".csv.tmp")
    with tmp_csv.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    tmp_csv.replace(csv_path)

    if run_ranking and (repo_root / "docs/make_ranking.py").is_file():
        subprocess.run([sys.executable, str(repo_root / "docs/make_ranking.py")], cwd=repo_root, check=True)

    return {"slug": slug, "tier": tier, "total_works": len(rows), "forecast_n": forecast_n, "decided_n": decided_n}


def pr_check(case_dir: Path, *, repo_root: Path = REPO_ROOT) -> dict:
    case_dir = case_dir.resolve()
    slug = case_dir.name
    if not SLUG_RE.fullmatch(slug):
        raise ValueError(f"Invalid case slug '{slug}'")
    cfg = _read_json(case_dir / "config.json")
    for req_key in ("book", "author", "publication_year_proxy", "cutoff", "domain", "author_type"):
        if not cfg.get(req_key):
            raise ValueError(f"config.json missing required field: {req_key}")
    normalize_domain(cfg["domain"])
    normalize_author_type(cfg["author_type"])
    src_sha = cfg.get("source_sha256") or cfg.get("source_txt_sha256") or ""
    if not re.fullmatch(r"[0-9a-f]{64}", src_sha):
        raise ValueError("config.json must record a valid 64-hex source_sha256")

    # 1. Pipeline check + report idempotency
    _run_pipeline(case_dir, "check")
    summary = _read_json(case_dir / "output/summary.json")
    if not summary.get("whole_candidate_pass_complete") or summary.get("unreviewed", 1) != 0:
        raise ValueError("All extracted candidates must be assessed (whole_candidate_pass_complete=true, unreviewed=0)")
    if int(summary.get("forecast_n") or 0) <= 0:
        raise ValueError("Case must contain at least 1 forecast")

    report_files = [case_dir / "output/report.md", case_dir / "output/claims.csv", case_dir / "output/summary.json"]
    before_hashes = {p.name: _sha256_file(p) for p in report_files if p.is_file()}
    if len(before_hashes) != 3:
        raise ValueError("Missing output/report.md, output/claims.csv, or output/summary.json; run pipeline.py report")
    _run_pipeline(case_dir, "report")
    after_hashes = {p.name: _sha256_file(p) for p in report_files}
    if before_hashes != after_hashes:
        raise ValueError("output/report.md, claims.csv, or summary.json is out of sync; commit freshly generated reports")

    # 2. Copyright & context length guard
    for path in case_dir.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(case_dir)
        if rel.parts[0] in IGNORED_SUBDIRS_FOR_BOOK_SCAN:
            continue
        if len(rel.parts) >= 2 and rel.parts[0] == "output" and rel.parts[1] in {"txt_import", "search_verify", "parallel_run"}:
            continue
        if len(rel.parts) >= 2 and rel.parts[0] == "data" and rel.parts[1] == "sources":
            continue
        if path.suffix.lower() in FORBIDDEN_BOOK_EXTS:
            raise ValueError(f"Copyright guard: forbidden raw book file inside tracked case path: {rel}")

    claims = _read_jsonl(case_dir / "data/claims.jsonl")
    for c in claims:
        if len(c.get("quote") or "") > MAX_QUOTE_CHARS:
            raise ValueError(f"Quote exceeds {MAX_QUOTE_CHARS} chars in claim {c['id']}")
        if len(c.get("context") or "") > MAX_CONTEXT_CHARS:
            raise ValueError(
                f"Context exceeds {MAX_CONTEXT_CHARS} chars in claim {c['id']}. "
                "Run 'contribute_book.py trim-contexts' to protect book copyright."
            )

    # 3. Secret & personal path leak scan across tracked files
    for path in case_dir.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(case_dir)
        if rel.parts[0] == "input" or (len(rel.parts) >= 2 and rel.parts[0] == "output" and rel.parts[1] in {"txt_import", "search_verify", "parallel_run"}):
            continue
        if path.suffix.lower() not in {".json", ".jsonl", ".md", ".csv", ".txt"}:
            continue
        content = path.read_text(encoding="utf-8", errors="ignore")
        for pat in SECRET_PATTERNS:
            if pat.search(content):
                raise ValueError(f"Potential API secret detected in {rel}")
        for pat in PRIVACY_PATH_PATTERNS:
            if pat.search(content):
                raise ValueError(f"Local machine privacy path detected in {rel}")

    # 4. Database CSV parity check
    csv_path = repo_root / "datasets/all_cases_summary.csv"
    with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
        csv_rows = {r["slug"]: r for r in csv.DictReader(f)}
    if slug not in csv_rows:
        raise ValueError(f"Case '{slug}' missing from datasets/all_cases_summary.csv; run 'contribute_book.py sync-database'")
    row = csv_rows[slug]
    dv = summary["display_verdicts"]
    checks = [
        ("预测数", summary["forecast_n"]),
        ("可判定数", summary["decided_n"]),
        ("正确", dv["正确"]),
        ("趋势符合", dv["趋势符合"]),
        ("部分符合", dv["部分符合"]),
        ("错误", dv["错误"]),
        ("暂无法判断", dv["暂无法判断"]),
    ]
    for col, expected in checks:
        if int(row[col]) != int(expected):
            raise ValueError(f"datasets/all_cases_summary.csv mismatch for {slug} column '{col}': {row[col]} != {expected}")

    return {"slug": slug, "pr_check": "passed", "claims": len(claims), "forecast_n": summary["forecast_n"]}


def audit_progress(case_dir: Path) -> dict:
    """Return deterministic, zero-trust completion status across extraction and verification."""
    case_dir = case_dir.resolve()
    manifest_path = case_dir / "output/txt_import/manifest.json"
    chunks_path = case_dir / "output/txt_import/chunks.jsonl"
    prop_dir = case_dir / "output/txt_import/chunk_proposals"

    ext_status: dict = {"ready": False, "active_chunks": 0, "done_chunks": 0, "proof_verified_chunks": 0, "missing_chunk_ids": [], "pending_batches": []}
    if manifest_path.is_file() and chunks_path.is_file():
        manifest = _read_json(manifest_path)
        chunks = {c["id"]: c for c in _read_jsonl(chunks_path)}
        done_ids: set[str] = set()
        proof_ok: set[str] = set()
        if prop_dir.is_dir():
            for item in _load_chunk_proposals(prop_dir):
                cid = item.get("id")
                if cid in chunks and isinstance(item.get("predictions"), list):
                    done_ids.add(cid)
                    try:
                        pr = _verify_proof_of_reading(item, chunks[cid], require_proof=True)
                        if pr["sha12_verified"] and pr["tail_anchor_verified"]:
                            proof_ok.add(cid)
                    except ValueError:
                        pass
        missing = sorted(set(chunks) - done_ids)
        pending_batches = [
            b["batch_id"]
            for b in (manifest.get("batches") or [])
            if any(cid not in done_ids or cid not in proof_ok for cid in (b.get("chunk_ids") or []))
        ]
        ext_status = {
            "ready": len(missing) == 0 and len(proof_ok) == len(chunks),
            "active_chunks": len(chunks),
            "done_chunks": len(done_ids),
            "proof_verified_chunks": len(proof_ok),
            "missing_chunk_ids": missing,
            "pending_batches": pending_batches,
        }

    vmanifest_path = case_dir / "output/verify_manifest.json"
    vtasks_path = case_dir / "output/verify_tasks.jsonl"
    vprop_dir = case_dir / "output/verify_proposals"
    eprop_dir = case_dir / "output/evidence_proposals"
    srev_dir = case_dir / "output/semantic_reviews"
    ver_status: dict = {
        "ready": False,
        "total_tasks": 0,
        "done_tasks": 0,
        "adaptive_compliant_tasks": 0,
        "semantic_reviewed_tasks": 0,
        "missing_task_ids": [],
        "pending_batches": [],
    }
    if vtasks_path.is_file():
        cfg = _read_json(case_dir / "config.json")
        cutoff = cfg.get("cutoff", "9999-12-31")
        vtasks = {t["id"]: t for t in _read_jsonl(vtasks_path)}
        raw_ev_by_id: dict[str, dict] = {}
        if eprop_dir.is_dir():
            for r in _load_records_file_or_dir(eprop_dir):
                if isinstance(r, dict) and isinstance(r.get("id"), str):
                    raw_ev_by_id[r["id"]] = r
        ev_raw_file = case_dir / "output/evidence_raw.jsonl"
        if ev_raw_file.is_file():
            for r in _load_records_file_or_dir(ev_raw_file):
                if isinstance(r, dict) and isinstance(r.get("id"), str):
                    raw_ev_by_id[r["id"]] = r

        reviews_by_id: dict[str, dict] = {}
        if srev_dir.is_dir():
            for rev in _load_records_file_or_dir(srev_dir):
                if isinstance(rev, dict) and isinstance(rev.get("id"), str):
                    reviews_by_id[rev["id"]] = rev

        vdone: set[str] = set()
        vcompliant: set[str] = set()
        vreviewed: set[str] = set()
        all_props: list[dict] = []
        if vprop_dir.is_dir():
            all_props.extend(_load_records_file_or_dir(vprop_dir))
        asm_file = case_dir / "output/assessments.jsonl"
        if asm_file.is_file():
            all_props.extend(_load_records_file_or_dir(asm_file))

        for p in all_props:
            if not isinstance(p, dict) or p.get("id") not in vtasks:
                continue
            cid = p["id"]
            vdone.add(cid)
            rev_item = reviews_by_id.get(cid) or (p.get("semantic_review") if isinstance(p.get("semantic_review"), dict) else None)
            try:
                _validate_search_Verifier_v3_proposal(
                    p,
                    vtasks[cid],
                    raw_ev_by_id,
                    cutoff,
                    require_dual_evidence=True,
                    require_adaptive_rounds=True,
                    review_item=rev_item,
                )
                vcompliant.add(cid)
                if rev_item is not None:
                    vreviewed.add(cid)
            except ValueError:
                pass

        vmissing = sorted(set(vtasks) - vdone)
        vbatches = (_read_json(vmanifest_path).get("batches") or []) if vmanifest_path.is_file() else []
        vpending = [
            b["batch_id"]
            for b in vbatches
            if any(cid not in vdone for cid in (b.get("claim_ids") or []))
        ]
        strict_pending = [
            b["batch_id"]
            for b in vbatches
            if any(
                cid not in vdone or cid not in vcompliant or cid not in vreviewed
                for cid in (b.get("claim_ids") or [])
            )
        ]
        ver_status = {
            "ready": len(vmissing) == 0,
            "strict_v3_ready": len(vmissing) == 0 and len(vcompliant) == len(vtasks) and len(vreviewed) == len(vtasks),
            "total_tasks": len(vtasks),
            "done_tasks": len(vdone),
            "adaptive_compliant_tasks": len(vcompliant),
            "semantic_reviewed_tasks": len(vreviewed),
            "missing_task_ids": vmissing,
            "pending_batches": vpending,
            "strict_pending_batches": strict_pending,
        }

    return {"case": case_dir.name, "extraction": ext_status, "verification": ver_status}


def ci_audit(*, repo_root: Path = REPO_ROOT) -> dict:
    cases_dir = repo_root / "cases"
    audited: list[str] = []
    for cfg_path in sorted(cases_dir.glob("*/config.json")):
        cfg = _read_json(cfg_path)
        if cfg.get("community_contribution"):
            res = pr_check(cfg_path.parent, repo_root=repo_root)
            audited.append(res["slug"])

    csv_path = repo_root / "datasets/all_cases_summary.csv"
    with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            if str(r.get("批次口径") or "").startswith("v5_community"):
                cdir = cases_dir / r["slug"]
                if not (cdir / "config.json").is_file():
                    raise ValueError(f"Community CSV row '{r['slug']}' missing case directory")
                if r["slug"] not in audited:
                    res = pr_check(cdir, repo_root=repo_root)
                    audited.append(res["slug"])

    return {"community_cases_audited": len(audited), "slugs": audited}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    p_init = sub.add_parser("init", help="Initialize a new community book case")
    p_init.add_argument("--case", type=Path, required=True)
    p_init.add_argument("--book", required=True)
    p_init.add_argument("--author", required=True)
    p_init.add_argument("--publication-year", type=int, required=True)
    p_init.add_argument("--domain", required=True)
    p_init.add_argument("--author-type", required=True)
    p_init.add_argument("--cutoff", default=None)
    p_init.add_argument("--execution-mode", choices=["agent-native-v5", "api-pipeline-v5"], default="agent-native-v5")
    p_init.add_argument("--source-note", default="")

    p_chunk = sub.add_parser("chunk-txt", help="Split source TXT into v5 chunks for Agent-native extraction")
    p_chunk.add_argument("--case", type=Path, required=True)
    p_chunk.add_argument("--txt", type=Path, required=True)
    p_chunk.add_argument("--encoding", default=None)
    p_chunk.add_argument("--chunk-chars", type=int, default=3500)
    p_chunk.add_argument("--context-chars", type=int, default=600)
    p_chunk.add_argument("--batch-size", type=int, default=5, help="Chunks per worker shard to prevent context bloat")
    p_chunk.add_argument("--include-front-matter", action="store_true")

    p_trim = sub.add_parser("trim-contexts", help="Trim claim contexts to copyright-safe snippets")
    p_trim.add_argument("--case", type=Path, required=True)

    p_imp_ext = sub.add_parser("import-extractions", help="Validate, align, trim, and import Agent chunk extractions")
    p_imp_ext.add_argument("--case", type=Path, required=True)
    p_imp_ext.add_argument("--txt", type=Path, required=True)
    p_imp_ext.add_argument("--proposals", type=Path, required=True, help="JSON/JSONL file or directory of <chunk_id>.json")
    p_imp_ext.add_argument("--encoding", default=None)
    p_imp_ext.add_argument("--include-front-matter", action="store_true")
    p_imp_ext.add_argument("--require-proof", action="store_true", help="Enforce proof-of-reading (body_sha256_12 + tail_anchor) on every chunk")

    p_exp = sub.add_parser("export-verify-tasks", help="Export extracted predictions for Agent web verification")
    p_exp.add_argument("--case", type=Path, required=True)
    p_exp.add_argument("--output", type=Path, default=None)
    p_exp.add_argument("--batch-size", type=int, default=4, help="Predictions per verification worker shard")

    p_app = sub.add_parser("apply-assessments", help="Register Agent-fetched evidence (SHA-256) and apply assessments")
    p_app.add_argument("--case", type=Path, required=True)
    p_app.add_argument("--assessments", type=Path, required=True)
    p_app.add_argument("--evidence-raw", type=Path, default=None)
    p_app.add_argument("--semantic-reviews", type=Path, default=None, help="File or directory of independent 6-check semantic reviews")
    p_app.add_argument("--require-dual-evidence", action="store_true", help="Enforce >=2 independent archived evidence items per decided forecast")
    p_app.add_argument("--require-adaptive-rounds", action="store_true", help="Enforce search-verifier-v3 multi-round initial + adaptive search trace & verbatim evidence_notes")
    p_app.add_argument("--require-semantic-review", action="store_true", help="Enforce independent 6-check semantic review validation on every forecast")

    p_prog = sub.add_parser("audit-progress", help="Audit extraction and verification completion without trusting agent claims")
    p_prog.add_argument("--case", type=Path, required=True)

    p_iv = sub.add_parser("import-verify", help="Import verify_prediction.py run results and verify evidence hashes")
    p_iv.add_argument("--case", type=Path, required=True)
    p_iv.add_argument("--search-run-dir", type=Path, default=None)

    p_sync = sub.add_parser("sync-database", help="Sync case summary to datasets/all_cases_summary.csv and ranking")
    p_sync.add_argument("--case", type=Path, required=True)
    p_sync.add_argument("--repo-root", type=Path, default=REPO_ROOT)

    p_pr = sub.add_parser("pr-check", help="Run all PR readiness gates (hashes, copyright, secrets, DB parity)")
    p_pr.add_argument("--case", type=Path, required=True)
    p_pr.add_argument("--repo-root", type=Path, default=REPO_ROOT)

    p_ci = sub.add_parser("ci-audit", help="Audit all community-contributed cases in CI")
    p_ci.add_argument("--repo-root", type=Path, default=REPO_ROOT)

    args = parser.parse_args(argv)
    if args.command == "init":
        res = init_case(
            args.case,
            book=args.book,
            author=args.author,
            publication_year=args.publication_year,
            domain=args.domain,
            author_type=args.author_type,
            cutoff=args.cutoff,
            execution_mode=args.execution_mode,
            source_note=args.source_note,
        )
    elif args.command == "chunk-txt":
        res = chunk_txt_for_agent(
            args.case,
            args.txt,
            encoding=args.encoding,
            chunk_chars=args.chunk_chars,
            context_chars=args.context_chars,
            batch_size=args.batch_size,
            include_front_matter=args.include_front_matter,
        )
    elif args.command == "trim-contexts":
        res = trim_case_contexts(args.case)
    elif args.command == "import-extractions":
        res = import_agent_extractions(
            args.case,
            args.txt,
            args.proposals,
            encoding=args.encoding,
            include_front_matter=args.include_front_matter,
            require_proof=args.require_proof,
        )
    elif args.command == "export-verify-tasks":
        res = export_verify_tasks(args.case, args.output, batch_size=args.batch_size)
    elif args.command == "apply-assessments":
        res = apply_agent_assessments(
            args.case,
            args.assessments,
            evidence_raw_path=args.evidence_raw,
            semantic_reviews_path=args.semantic_reviews,
            require_dual_evidence=args.require_dual_evidence,
            require_adaptive_rounds=args.require_adaptive_rounds,
            require_semantic_review=args.require_semantic_review,
        )
    elif args.command == "audit-progress":
        res = audit_progress(args.case)
    elif args.command == "import-verify":
        res = import_verify_run(args.case, args.search_run_dir)
    elif args.command == "sync-database":
        res = sync_database(args.case, repo_root=args.repo_root)
    elif args.command == "pr-check":
        res = pr_check(args.case, repo_root=args.repo_root)
    elif args.command == "ci-audit":
        res = ci_audit(repo_root=args.repo_root)
    else:
        return 1

    print(json.dumps(res, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValueError, KeyError, OSError, subprocess.CalledProcessError) as exc:
        print(f"Contribute-book stopped: {exc}", file=sys.stderr)
        sys.exit(2)
