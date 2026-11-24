#!/usr/bin/env python3
"""Manage a personal forward-looking forecast ledger and generate periodic review digests.

Uses only the Python 3.11+ standard library and stays 100% compatible with
toolkit/pipeline.py (check/report) and toolkit/verify_prediction.py (--all-forecasts / --unresolved).
"""
from __future__ import annotations

import argparse
from datetime import date
import hashlib
import json
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import pipeline as pl  # noqa: E402


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _save_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _read_jsonl(path: Path) -> list[dict]:
    if not path.is_file():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _save_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    tmp.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
    tmp.replace(path)


def _slugify(value: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9\u4e00-\u9fff_-]+", "-", value.strip()).strip("-")
    return cleaned[:48] or "forecast"


def init_ledger(case_dir: Path, title: str, author: str, cutoff: str | None = None) -> dict:
    case_dir = case_dir.resolve()
    today = cutoff or date.today().isoformat()
    year = date.fromisoformat(today).year
    if (case_dir / "config.json").exists():
        raise ValueError(f"Ledger already exists at {case_dir}")
    (case_dir / "cards").mkdir(parents=True, exist_ok=True)
    (case_dir / "data/sources").mkdir(parents=True, exist_ok=True)
    (case_dir / "output").mkdir(parents=True, exist_ok=True)
    cfg = {
        "book": title,
        "author": author,
        "cutoff": today,
        "publication_year_proxy": year,
        "rules_version": "simple-v3-trend-four-class",
        "ledger_mode": "prospective_periodic_tracker",
    }
    _save_json(case_dir / "config.json", cfg)
    _save_jsonl(case_dir / "data/claims.jsonl", [])
    _save_jsonl(case_dir / "data/evidence.jsonl", [])
    return cfg


def add_forecast(
    case_dir: Path,
    *,
    claim_id: str,
    domain: str,
    statement: str,
    horizon: str,
    scope: str,
    method: str,
    counter_lens: str,
    leading_indicators: str,
    falsification: str,
    condition_text: str = "",
    base_rate: str = "基准率待补充",
    review_cadence: str = "每季度巡检",
    created_date: str | None = None,
) -> dict:
    case_dir = case_dir.resolve()
    cfg = _read_json(case_dir / "config.json")
    today = created_date or cfg["cutoff"]
    date.fromisoformat(today)
    if date.fromisoformat(today) > date.fromisoformat(cfg["cutoff"]):
        cfg["cutoff"] = today
        _save_json(case_dir / "config.json", cfg)

    rows = _read_jsonl(case_dir / "data/claims.jsonl")
    if any(r["id"] == claim_id for r in rows):
        raise ValueError(f"Duplicate forecast ID: {claim_id}")
    if not statement.strip() or not horizon.strip() or not scope.strip() or not method.strip():
        raise ValueError("statement, horizon, scope, and method must be non-empty")

    cards_dir = case_dir / "cards"
    cards_dir.mkdir(parents=True, exist_ok=True)
    card_rel = Path("cards") / f"{_slugify(claim_id)}.md"
    card_path = case_dir / card_rel
    card_lines = [
        f"# 预测卡：{claim_id}（{domain}）",
        "",
        f"- **编号**：`{claim_id}`",
        f"- **创建与冻结日期**：{today}",
        f"- **预测人 / 团队**：{cfg.get('author') or 'Personal Forecast Lab'}",
        f"- **所属领域**：{domain}",
        f"- **目标期限**：{horizon}",
        f"- **建议巡检频率**：{review_cadence}",
        "",
        "## 1. 可核验核心承诺（事前冻结原文）",
        "",
        statement.strip(),
        "",
        "## 2. 统计口径、范围与排除边界",
        "",
        f"- **核验口径与范围**：{scope.strip()}",
        f"- **前提条件**：{condition_text.strip() or '无附加前置条件（按当前公开基线直接观测）'}",
        f"- **历史/同档基准率参考**：{base_rate.strip()}",
        "",
        "## 3. 方法透镜与反校验视角",
        "",
        f"- **主推理方法（Signal Lens）**：{method.strip()}",
        f"- **反校验透镜（Counter-Lens）**：{counter_lens.strip() or '检查替代供给、政策反制与跨层跳跃风险'}",
        "",
        "## 4. 定期追踪领先指标与证伪阈值",
        "",
        f"- **领先观测指标**：{leading_indicators.strip()}",
        f"- **明确证伪 / 推翻条件**：{falsification.strip()}",
        "",
        "## 5. 三轴复盘记录（事件 × 机制 × 时间）",
        "",
        "| 巡检日期 | 事件轴状态 | 机制轴验证 | 时间轴进度 | 新证据摘要与改判说明 |",
        "| :--- | :--- | :--- | :--- | :--- |",
        f"| {today} | 初始登记（暂无法判断） | 待观测 | 窗口期内 | 事前冻结基线承诺 |",
        "",
    ]
    card_content = "\n".join(card_lines)
    card_path.write_text(card_content, encoding="utf-8")
    card_bytes = card_path.read_bytes()
    card_sha = hashlib.sha256(card_bytes).hexdigest()

    # Locate exact line/char span of statement inside the frozen card
    char_start = card_content.index(statement.strip())
    char_end = char_start + len(statement.strip())
    line_start = card_content[:char_start].count("\n") + 1
    line_end = line_start + statement.strip().count("\n")

    condition_state = "unknown" if condition_text.strip() else "unconditional"
    basis = "conditional" if condition_text.strip() else "future"
    full_method = f"{method.strip()}｜反校验：{counter_lens.strip()}" if counter_lens.strip() else method.strip()
    full_scope = f"【领域：{domain}】{scope.strip()}｜领先指标：{leading_indicators.strip()}"
    full_limitation = f"证伪条件：{falsification.strip()}；基准率参考：{base_rate.strip()}"

    record = {
        "id": claim_id,
        "page": None,
        "quote": statement.strip(),
        "context": f"目标期限：{horizon.strip()}。核验口径：{scope.strip()}。领先指标：{leading_indicators.strip()}",
        "speaker": cfg.get("author") or "作者",
        "source_verified": True,
        "source_location": {
            "type": "txt",
            "path": card_rel.as_posix(),
            "line_start": line_start,
            "line_end": line_end,
            "char_start": char_start,
            "char_end": char_end,
            "source_sha256": card_sha,
        },
        "source_verification": {
            "method": "txt_exact_match",
            "source_sha256": card_sha,
            "created_at": today,
        },
        "duplicate_of": None,
        "family": domain,
        "kind": "prediction",
        "claim": statement.strip(),
        "time_text": horizon.strip(),
        "condition_text": condition_text.strip(),
        "method": full_method,
        "method_basis": "explicit",
        "extraction": None,
        "extraction_v2": {
            "id": claim_id,
            "extraction_version": "v5",
            "kind": "prediction",
            "claim_type": "forecast",
            "speaker": cfg.get("author") or "作者",
            "attribution": "author",
            "future_oriented": True,
            "claim": statement.strip(),
            "expanded_claim": statement.strip(),
            "reference_resolutions": [],
            "unresolved_references": [],
            "changes": statement.strip(),
            "horizon": horizon.strip(),
            "horizon_source": "explicit",
            "resolvable": True,
            "confidence": "medium",
            "time_text": horizon.strip(),
            "condition_text": condition_text.strip(),
            "method": full_method,
            "method_basis": "explicit",
            "reason": f"事前登记前瞻预测卡（{card_rel.as_posix()}），明确定义了目标期限与可核验指标。",
        },
        "assessment": {
            "id": claim_id,
            "inclusion": "forecast",
            "verdict": "暂无法判断",
            "basis": basis,
            "scope": full_scope,
            "reason": f"于 {today} 事前冻结登记，目标窗口（{horizon.strip()}）尚未到期，等待定期检索领先指标更新。",
            "limitation": full_limitation,
            "evidence_ids": [],
            "method": full_method,
            "method_basis": "explicit",
            "observation_end": None,
            "future_time_text": horizon.strip(),
            "condition_state": condition_state,
            "trend_aligned": False,
        },
        "review_metadata": {
            "domain": domain,
            "created_date": today,
            "review_cadence": review_cadence,
            "leading_indicators": leading_indicators.strip(),
            "falsification": falsification.strip(),
            "card_path": card_rel.as_posix(),
        },
    }
    rows.append(record)
    _save_jsonl(case_dir / "data/claims.jsonl", rows)
    return record


def bump_cutoff(case_dir: Path, new_cutoff: str | None = None) -> str:
    case_dir = case_dir.resolve()
    target = new_cutoff or date.today().isoformat()
    date.fromisoformat(target)
    cfg_path = case_dir / "config.json"
    cfg = _read_json(cfg_path)
    if date.fromisoformat(target) < date.fromisoformat(cfg["cutoff"]):
        raise ValueError(f"New cutoff {target} cannot be earlier than current cutoff {cfg['cutoff']}")
    cfg["cutoff"] = target
    _save_json(cfg_path, cfg)
    return target


def generate_digest(
    case_dir: Path,
    *,
    search_run_dir: Path | None = None,
    output_file: Path | None = None,
) -> dict:
    case_dir = case_dir.resolve()
    cfg = _read_json(case_dir / "config.json")
    claims = _read_jsonl(case_dir / "data/claims.jsonl")

    proposals_by_id: dict[str, dict] = {}
    run_summary: dict = {}
    if search_run_dir and (search_run_dir / "results.jsonl").is_file():
        for item in _read_jsonl(search_run_dir / "results.jsonl"):
            cid = item.get("claim_id") or item.get("id")
            if cid:
                proposals_by_id[cid] = item
        if (search_run_dir / "summary.json").is_file():
            run_summary = _read_json(search_run_dir / "summary.json")

    counts = {v: 0 for v in pl.DISPLAY_VERDICTS}
    shifts: list[dict] = []
    table_rows: list[str] = []
    detail_blocks: list[str] = []

    for c in claims:
        asm = c.get("assessment") or {}
        if asm.get("inclusion") != "forecast":
            continue
        cur_verdict = pl.display_verdict(asm) or "暂无法判断"
        counts[cur_verdict] = counts.get(cur_verdict, 0) + 1

        meta = c.get("review_metadata") or {}
        domain = meta.get("domain") or c.get("family") or "未分类"
        horizon = (c.get("extraction_v2") or {}).get("horizon") or c.get("time_text") or "未注明"
        indicators = meta.get("leading_indicators") or "见口径说明"

        prop = proposals_by_id.get(c["id"])
        prop_verdict = "未运行联网巡检"
        gap_or_note = asm.get("reason", "")
        new_urls: list[str] = []

        if prop:
            p_asm = prop.get("assessment") or {}
            if p_asm:
                prop_verdict = "趋势符合" if p_asm.get("trend_aligned") else (p_asm.get("verdict") or "无有效建议")
            else:
                prop_verdict = f"运行异常({prop.get('task_state', 'unknown')})"
            gap_or_note = prop.get("remaining_gap") or p_asm.get("reason") or gap_or_note
            for cand in prop.get("evidence_candidates") or []:
                if cand.get("url"):
                    new_urls.append(cand["url"])
            if p_asm and prop_verdict != cur_verdict:
                shifts.append({
                    "id": c["id"],
                    "previous": cur_verdict,
                    "proposed": prop_verdict,
                    "reason": p_asm.get("reason", ""),
                })

        safe_stmt = c["quote"].replace("|", "／").replace("\n", " ")
        if len(safe_stmt) > 64:
            safe_stmt = safe_stmt[:61] + "..."
        table_rows.append(
            f"| `{c['id']}` | {domain} | {horizon} | **{cur_verdict}** | {prop_verdict} | {safe_stmt} |"
        )

        detail_blocks.extend([
            f"### `{c['id']}` · {domain}（目标窗口：{horizon}）",
            f"- **冻结承诺**：{c['quote']}",
            f"- **当前账本状态**：`{cur_verdict}` ｜ **本期联网建议**：`{prop_verdict}`",
            f"- **重点盯盘领先指标**：{indicators}",
            f"- **本期摘要 / 待补缺口**：{gap_or_note}",
        ])
        if new_urls:
            preview_links = " · ".join(f"[来源{idx}]({u})" for idx, u in enumerate(new_urls[:5], 1))
            detail_blocks.append(f"- **本期捕获外部线索**：{preview_links}")
        card_rel = meta.get("card_path")
        if card_rel:
            detail_blocks.append(f"- **原始预测卡**：[`{card_rel}`](../{card_rel})")
        detail_blocks.append("")

    total_forecasts = sum(counts.values())
    lines = [
        f"# {cfg['book']} · 定期预测追踪简报",
        "",
        f"- **账本截止日（Cutoff）**：`{cfg['cutoff']}`",
        f"- **在册可追踪预测数**：**{total_forecasts}** 条（"
        + "，".join(f"{k} {v}" for k, v in counts.items())
        + "）",
        f"- **本期检测到状态异动建议**：**{len(shifts)}** 条",
    ]
    if run_summary:
        llm_cost = (run_summary.get("deepseek") or {}).get("estimated_cost_CNY", 0.0)
        exa_cost = (run_summary.get("exa") or {}).get("estimated_cost_USD", 0.0)
        lines.append(
            f"- **本期自动搜证任务完成度**：`{run_summary.get('task_states', {}).get('completed', 0)}/{run_summary.get('requested', 0)}` "
            f"（估计成本：LLM ¥{llm_cost:.4f} / Exa ${exa_cost:.4f}）"
        )
    lines.extend([
        "",
        "> **贝叶斯更新提醒**：自动联网巡检给出的仅是候选建议稿，不会静默覆盖你已冻结的主账本。请对照事件轴、机制轴、时间轴核实证据后，再决定是否通过 `pipeline.py apply assess` 正式更新状态。",
        "",
        "## 一、全部预测状态总览",
        "",
        "| 预测编号 | 领域 | 目标窗口 | 当前账本结论 | 本期联网建议 | 核心承诺摘要 |",
        "| :--- | :--- | :--- | :--- | :--- | :--- |",
        *table_rows,
        "",
    ])

    if shifts:
        lines.extend([
            "## 二、本期重点关注：状态变化建议（Signal Shifts）",
            "",
        ])
        for s in shifts:
            lines.append(f"- **`{s['id']}`**：`{s['previous']}` → **`{s['proposed']}`** — {s['reason']}")
        lines.append("")

    lines.extend([
        "## 三、逐条追踪详情与领先指标核对",
        "",
        *detail_blocks,
    ])

    target_out = output_file or (case_dir / "output/periodic_digest.md")
    target_out.parent.mkdir(parents=True, exist_ok=True)
    target_out.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    rel_digest = (
        target_out.resolve().relative_to(case_dir).as_posix()
        if target_out.resolve().is_relative_to(case_dir)
        else target_out.name
    )
    digest_summary = {
        "book": cfg["book"],
        "cutoff": cfg["cutoff"],
        "total_forecasts": total_forecasts,
        "current_counts": counts,
        "shift_count": len(shifts),
        "shifts": shifts,
        "digest_path": rel_digest,
    }
    _save_json(target_out.with_suffix(".json"), digest_summary)
    return digest_summary


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", type=Path, default=Path("my-forecasts"), help="Path to forecast ledger directory")
    sub = parser.add_subparsers(dest="command", required=True)

    p_init = sub.add_parser("init", help="Initialize a new personal forecast ledger")
    p_init.add_argument("--title", default="我的定期预测实验室 (My Forecast Lab)")
    p_init.add_argument("--author", default="Forecast Lab User")
    p_init.add_argument("--cutoff", default=None, help="ISO date YYYY-MM-DD (defaults to today)")

    p_add = sub.add_parser("add", help="Register a new pre-frozen forecast card and JSONL claim")
    p_add.add_argument("--id", required=True, dest="claim_id", help="Unique forecast ID, e.g. my-2026-001")
    p_add.add_argument("--domain", required=True, help="Domain label, e.g. AI与能源基础设施")
    p_add.add_argument("--statement", required=True, help="Falsifiable forecast commitment")
    p_add.add_argument("--horizon", required=True, help="Target window or deadline, e.g. 2026-2030")
    p_add.add_argument("--scope", required=True, help="Exact metric, denominator, data source, and exclusions")
    p_add.add_argument("--method", required=True, help="Primary reasoning lens (e.g. 约束账本法)")
    p_add.add_argument("--counter-lens", default="", help="Counter-calibration lens")
    p_add.add_argument("--indicators", required=True, help="Leading indicators to monitor periodically")
    p_add.add_argument("--falsification", required=True, help="Observation that would falsify this forecast")
    p_add.add_argument("--condition", default="", help="Optional trigger condition A")
    p_add.add_argument("--base-rate", default="参考同时间跨度历史基准率")
    p_add.add_argument("--cadence", default="每季度巡检")
    p_add.add_argument("--created-date", default=None)

    p_bump = sub.add_parser("bump-cutoff", help="Advance ledger cutoff date to today (or --date) before periodic search")
    p_bump.add_argument("--date", default=None, help="ISO date YYYY-MM-DD (defaults to today)")

    p_digest = sub.add_parser("digest", help="Generate Markdown periodic tracking digest")
    p_digest.add_argument("--search-run-dir", type=Path, default=None, help="Optional verify_prediction output dir")
    p_digest.add_argument("--output", type=Path, default=None, help="Optional output markdown path")

    args = parser.parse_args(argv)
    if args.command == "init":
        cfg = init_ledger(args.case, args.title, args.author, args.cutoff)
        print(json.dumps({"initialized": str(args.case.resolve()), "cutoff": cfg["cutoff"]}, ensure_ascii=False))
        return 0

    if args.command == "add":
        rec = add_forecast(
            args.case,
            claim_id=args.claim_id,
            domain=args.domain,
            statement=args.statement,
            horizon=args.horizon,
            scope=args.scope,
            method=args.method,
            counter_lens=args.counter_lens,
            leading_indicators=args.indicators,
            falsification=args.falsification,
            condition_text=args.condition,
            base_rate=args.base_rate,
            review_cadence=args.cadence,
            created_date=args.created_date,
        )
        pl.main(["--case", str(args.case), "report"])
        print(json.dumps({"added": rec["id"], "card": rec["review_metadata"]["card_path"]}, ensure_ascii=False))
        return 0

    if args.command == "bump-cutoff":
        updated = bump_cutoff(args.case, args.date)
        print(json.dumps({"case": str(args.case), "cutoff": updated}, ensure_ascii=False))
        return 0

    if args.command == "digest":
        summary = generate_digest(args.case, search_run_dir=args.search_run_dir, output_file=args.output)
        print(json.dumps(summary, ensure_ascii=False))
        return 0

    return 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValueError, KeyError, OSError) as exc:
        print(f"Periodic tracker error: {exc}", file=sys.stderr)
        sys.exit(2)
