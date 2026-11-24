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

import pipeline as pl  # noqa: E402
import prepare_book as pb  # noqa: E402
import run_parallel as rp  # noqa: E402
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
    include_front_matter: bool = False,
    repo_root: Path = REPO_ROOT,
) -> dict:
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

    out_dir = case_dir / "output/txt_import"
    (out_dir / "chunk_proposals").mkdir(parents=True, exist_ok=True)
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
    if text.startswith("{"):
        obj = json.loads(text)
        if "items" in obj and isinstance(obj["items"], list):
            return obj["items"]
        if "id" in obj and "\n" not in text:
            return [obj]
    if text.startswith("["):
        return json.loads(text)
    return [json.loads(line) for line in text.splitlines() if line.strip()]


def import_agent_extractions(
    case_dir: Path,
    txt_path: Path,
    proposals_path: Path,
    *,
    encoding: str | None = None,
    include_front_matter: bool = False,
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
    for item in items:
        chunk = by_id[item["id"]]
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
    }


def export_verify_tasks(case_dir: Path, output_path: Path | None = None) -> dict:
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
    return {"tasks": len(tasks), "output": str(out), "total_claims": len(rows)}


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
        obj = json.loads(text)
        if "items" in obj and isinstance(obj["items"], list):
            return obj["items"]
        if "\n" not in text:
            return [obj]
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


def apply_agent_assessments(
    case_dir: Path,
    assessments_path: Path,
    *,
    evidence_raw_path: Path | None = None,
) -> dict:
    case_dir = case_dir.resolve()
    cfg = _read_json(case_dir / "config.json")
    ev_added = 0
    if evidence_raw_path is not None:
        raw_ev = _load_records_file_or_dir(evidence_raw_path)
        ev_added = _register_raw_evidence(case_dir, raw_ev, cfg["cutoff"])

    claims = _read_jsonl(case_dir / "data/claims.jsonl")
    proposals = _load_records_file_or_dir(assessments_path)
    by_id = {p["id"]: p for p in proposals}
    full_proposals = []
    for c in claims:
        if c["id"] in by_id:
            full_proposals.append(by_id[c["id"]])
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
    return {"evidence_registered": ev_added, "assessments_applied": len(full_proposals)}


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
    p_chunk.add_argument("--include-front-matter", action="store_true")

    p_trim = sub.add_parser("trim-contexts", help="Trim claim contexts to copyright-safe snippets")
    p_trim.add_argument("--case", type=Path, required=True)

    p_imp_ext = sub.add_parser("import-extractions", help="Validate, align, trim, and import Agent chunk extractions")
    p_imp_ext.add_argument("--case", type=Path, required=True)
    p_imp_ext.add_argument("--txt", type=Path, required=True)
    p_imp_ext.add_argument("--proposals", type=Path, required=True, help="JSON/JSONL file or directory of <chunk_id>.json")
    p_imp_ext.add_argument("--encoding", default=None)
    p_imp_ext.add_argument("--include-front-matter", action="store_true")

    p_exp = sub.add_parser("export-verify-tasks", help="Export extracted predictions for Agent web verification")
    p_exp.add_argument("--case", type=Path, required=True)
    p_exp.add_argument("--output", type=Path, default=None)

    p_app = sub.add_parser("apply-assessments", help="Register Agent-fetched evidence (SHA-256) and apply assessments")
    p_app.add_argument("--case", type=Path, required=True)
    p_app.add_argument("--assessments", type=Path, required=True)
    p_app.add_argument("--evidence-raw", type=Path, default=None)

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
        )
    elif args.command == "export-verify-tasks":
        res = export_verify_tasks(args.case, args.output)
    elif args.command == "apply-assessments":
        res = apply_agent_assessments(args.case, args.assessments, evidence_raw_path=args.evidence_raw)
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
