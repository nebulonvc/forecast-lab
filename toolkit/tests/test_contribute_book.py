import csv
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import contribute_book as cb  # noqa: E402
import pipeline as pl  # noqa: E402
import prepare_book as pb  # noqa: E402
import run_parallel as rp  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[2]


class ContributeBookTests(unittest.TestCase):
    def _make_temp_repo(self, tmp: Path) -> Path:
        repo = tmp / "repo"
        (repo / "datasets").mkdir(parents=True)
        (repo / "cases").mkdir(parents=True)
        (repo / "docs").mkdir(parents=True)
        shutil.copy2(REPO_ROOT / "datasets/all_cases_summary.csv", repo / "datasets/all_cases_summary.csv")
        shutil.copy2(REPO_ROOT / "docs/make_ranking.py", repo / "docs/make_ranking.py")
        return repo

    def test_openai_compatible_endpoint_and_payload(self):
        self.assertEqual(rp.resolve_endpoint(None), rp.DEFAULT_ENDPOINT)
        self.assertEqual(rp.resolve_endpoint("https://api.openai.com/v1"), "https://api.openai.com/v1/chat/completions")
        self.assertEqual(
            rp.resolve_endpoint("https://openrouter.ai/api/v1/chat/completions"),
            "https://openrouter.ai/api/v1/chat/completions",
        )
        ds_req = rp.payload("extract", {"cases": []}, 1000, model="deepseek-flash")
        self.assertIn("thinking", ds_req)
        oai_req = rp.payload("extract", {"cases": []}, 1000, model="gpt-4.1-mini", endpoint="https://api.openai.com/v1/chat/completions")
        self.assertNotIn("thinking", oai_req)

        pb_ds = pb.make_request("discover", [], {"book": "T", "publication_year_proxy": 2020}, 1000, "deepseek-flash")
        self.assertIn("thinking", pb_ds)
        pb_oai = pb.make_request(
            "discover", [], {"book": "T", "publication_year_proxy": 2020}, 1000, "gpt-4.1-mini",
            endpoint="https://api.openai.com/v1/chat/completions",
        )
        self.assertNotIn("thinking", pb_oai)

    def test_agent_native_end_to_end_and_pr_gates(self):
        with tempfile.TemporaryDirectory() as d:
            repo = self._make_temp_repo(Path(d))
            case_dir = repo / "cases/test-author-future-v5"
            cb.init_case(
                case_dir,
                book="测试未来之书",
                author="测试作者",
                publication_year=2020,
                domain="AI",
                author_type="学者",
                cutoff="2026-11-24",
                execution_mode="agent-native-v5",
            )

            # Copyright guard rejects TXT placed directly inside tracked case root
            bad_txt = case_dir / "book.txt"
            bad_txt.write_text("序言\n这是序言。\n第一章 未来\n人工智能将在2025年普及。\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Copyright guard"):
                cb.chunk_txt_for_agent(case_dir, bad_txt, repo_root=repo)
            bad_txt.unlink()

            # Valid TXT inside ignored input/ directory
            txt_path = case_dir / "input/book.txt"
            filler = "这是一段用于测试上下文裁剪长度的背景文字，不包含任何预测结论。" * 50
            book_text = (
                "序言\n感谢所有编辑。\n\n"
                "第一章 算力与制度\n"
                f"{filler}\n"
                "该国政府在2021年宣布了新的算力补贴计划。因此，到2025年底，该国的公共算力中心数量将会翻倍。\n"
                f"{filler}\n"
                "我们要努力建设更美好的数字社会。\n"
            )
            txt_path.write_text(book_text, encoding="utf-8")

            manifest = cb.chunk_txt_for_agent(case_dir, txt_path, chunk_chars=1500, context_chars=300, repo_root=repo)
            self.assertGreaterEqual(manifest["active_chunks"], 1)
            self.assertTrue((case_dir / "output/txt_import/prompt_v5.txt").is_file())

            chunks = cb._read_jsonl(case_dir / "output/txt_import/chunks.jsonl")
            prop_dir = case_dir / "output/txt_import/chunk_proposals"
            for ch in chunks:
                preds = []
                if "该国的公共算力中心数量将会翻倍" in ch["body"]:
                    preds.append({
                        "quote": "到2025年底，该国的公共算力中心数量将会翻倍。",
                        "kind": "prediction",
                        "claim_type": "forecast",
                        "speaker": "测试作者",
                        "attribution": "author",
                        "future_oriented": True,
                        "claim": "到2025年底，该国的公共算力中心数量将翻倍",
                        "changes": "公共算力中心数量将会翻倍",
                        "horizon": "到2025年底",
                        "resolvable": True,
                        "confidence": "medium",
                        "expanded_claim": "到2025年底，该国（实施算力补贴计划的国家）的公共算力中心数量将会翻倍。",
                        "reference_resolutions": [{
                            "expression": "该国",
                            "referent": "实施2021年算力补贴计划的国家",
                            "support_quote": "该国政府在2021年宣布了新的算力补贴计划。",
                        }],
                        "unresolved_references": [],
                        "time_text": "到2025年底",
                        "condition_text": "",
                        "method": "约束账本法",
                        "method_basis": "explicit",
                        "reason": "明确给出时间与数量变化方向",
                    })
                if "我们要努力建设更美好的数字社会" in ch["body"]:
                    preds.append({
                        "quote": "我们要努力建设更美好的数字社会。",
                        "kind": "prediction",
                        "claim_type": "normative",
                        "speaker": "测试作者",
                        "attribution": "author",
                        "future_oriented": True,
                        "claim": "建设更美好的数字社会",
                        "changes": "",
                        "horizon": "",
                        "resolvable": False,
                        "confidence": "unknown",
                        "expanded_claim": "我们要努力建设更美好的数字社会。",
                        "reference_resolutions": [],
                        "unresolved_references": [],
                        "time_text": "",
                        "condition_text": "",
                        "method": "unknown",
                        "method_basis": "unknown",
                        "reason": "规范倡议",
                    })
                (prop_dir / f"{ch['id']}.json").write_text(
                    json.dumps({"id": ch["id"], "predictions": preds}, ensure_ascii=False),
                    encoding="utf-8",
                )

            imp_res = cb.import_agent_extractions(case_dir, txt_path, prop_dir, repo_root=repo)
            self.assertEqual(imp_res["imported_claims"], 1)
            self.assertEqual(imp_res["excluded_non_predictions"], 1)

            claims = cb._read_jsonl(case_dir / "data/claims.jsonl")
            self.assertLessEqual(len(claims[0]["context"]), 1200)
            pb.validate_extraction_provenance(claims[0], cb._read_json(case_dir / "config.json"))

            tasks_res = cb.export_verify_tasks(case_dir)
            self.assertEqual(tasks_res["tasks"], 1)
            tasks = cb._read_jsonl(case_dir / "output/verify_tasks.jsonl")
            cid = tasks[0]["id"]

            ev_raw = case_dir / "output/evidence_raw.jsonl"
            ev_raw.write_text(json.dumps({
                "id": "ev-001",
                "url": "https://stats.example.org/compute-2025",
                "date": "2026-01-15",
                "coverage": "2020-2025",
                "excerpt": "2025年底全国公共算力中心数量较2020年增长2.1倍。",
                "limitation": "官方统计公报摘录",
                "text": "2026年1月官方公报显示：2025年底全国公共算力中心数量较2020年增长2.1倍，超过翻倍目标。",
            }, ensure_ascii=False) + "\n", encoding="utf-8")

            asm_path = case_dir / "output/assessments.jsonl"
            asm_path.write_text(json.dumps({
                "id": cid,
                "inclusion": "forecast",
                "verdict": "正确",
                "basis": "endpoint",
                "scope": "核验2025年底公共算力中心数量较2020年是否翻倍",
                "reason": "2026年1月官方统计公报显示2025年底数量增长2.1倍，已达标。",
                "limitation": "仅依赖单一统计口径。",
                "evidence_ids": ["ev-001"],
                "method": "约束账本法",
                "method_basis": "explicit",
                "observation_end": "2025-12-31",
                "future_time_text": "",
                "condition_state": "unconditional",
                "trend_aligned": False,
            }, ensure_ascii=False) + "\n", encoding="utf-8")

            app_res = cb.apply_agent_assessments(case_dir, asm_path, evidence_raw_path=ev_raw)
            self.assertEqual(app_res["evidence_registered"], 1)
            self.assertEqual(app_res["assessments_applied"], 1)

            sync_res = cb.sync_database(case_dir, repo_root=repo)
            self.assertEqual(sync_res["slug"], "test-author-future-v5")
            self.assertEqual(sync_res["total_works"], 133)

            with (repo / "datasets/all_cases_summary.csv").open(encoding="utf-8-sig") as f:
                csv_rows = {r["slug"]: r for r in csv.DictReader(f)}
            self.assertIn("test-author-future-v5", csv_rows)
            self.assertEqual(csv_rows["test-author-future-v5"]["批次口径"], "v5_community_agent")
            self.assertEqual(csv_rows["test-author-future-v5"]["写明期限中位目标跨度年"], "5")

            pr_res = cb.pr_check(case_dir, repo_root=repo)
            self.assertEqual(pr_res["pr_check"], "passed")
            ci_res = cb.ci_audit(repo_root=repo)
            self.assertEqual(ci_res["community_cases_audited"], 1)

            # Security checks: secret leak & over-long context must fail pr_check
            leak_file = case_dir / "REPORT-manual-zh.md"
            leak_file.write_text("API key sk-1234567890abcdefghijklmnop\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Potential API secret"):
                cb.pr_check(case_dir, repo_root=repo)
            leak_file.unlink()

            claims = cb._read_jsonl(case_dir / "data/claims.jsonl")
            claims[0]["context"] = (claims[0].get("context") or "") + ("x" * 2000)
            cb._save_jsonl(case_dir / "data/claims.jsonl", claims)
            cb._run_pipeline(case_dir, "report")
            with self.assertRaisesRegex(ValueError, "Context exceeds"):
                cb.pr_check(case_dir, repo_root=repo)

    def test_import_verify_from_api_run(self):
        with tempfile.TemporaryDirectory() as d:
            repo = self._make_temp_repo(Path(d))
            case_dir = repo / "cases/api-book-v5"
            cb.init_case(
                case_dir,
                book="API测试书",
                author="API作者",
                publication_year=2021,
                domain="宏观金融",
                author_type="经济学家",
                cutoff="2026-11-24",
                execution_mode="api-pipeline-v5",
            )
            txt_path = case_dir / "input/book.txt"
            txt_path.write_text("到2025年通胀率将回落至3%以下。\n", encoding="utf-8")
            raw_sha = hashlib.sha256(txt_path.read_bytes()).hexdigest()
            cfg = cb._read_json(case_dir / "config.json")
            cfg["source_sha256"] = raw_sha
            cb._save_json(case_dir / "config.json", cfg)

            cid = f"txt-{raw_sha[:10]}-000000000-000000018"
            cb._save_jsonl(case_dir / "data/claims.jsonl", [{
                "id": cid,
                "family": cid,
                "duplicate_of": None,
                "page": None,
                "quote": "到2025年通胀率将回落至3%以下。",
                "context": "",
                "speaker": "API作者",
                "source_verified": True,
                "source_verification": {"method": "txt_exact_match", "sha256": raw_sha},
                "source_location": {"type": "txt", "line_start": 1, "line_end": 1, "char_start": 0, "char_end": 18, "source_sha256": raw_sha},
                "kind": "prediction",
                "claim": "到2025年通胀率将回落至3%以下",
                "time_text": "到2025年",
                "condition_text": "",
                "method": "约束账本法",
                "method_basis": "explicit",
                "extraction_v2": {
                    "id": cid,
                    "extraction_version": "v5",
                    "kind": "prediction",
                    "claim_type": "forecast",
                    "horizon": "到2025年",
                    "horizon_source": "explicit",
                    "resolvable": True,
                    "expanded_claim": "到2025年通胀率将回落至3%以下。",
                    "reference_resolutions": [],
                    "unresolved_references": [],
                },
            }])

            run_dir = case_dir / "output/search_verify"
            arch_rel = "jobs/abc/ev1.txt"
            (run_dir / arch_rel).parent.mkdir(parents=True, exist_ok=True)
            body = "2025年全年CPI同比上涨2.4%，回落至3%以下。"
            (run_dir / arch_rel).write_text(body, encoding="utf-8")
            body_sha = hashlib.sha256(body.encode("utf-8")).hexdigest()
            cb._save_jsonl(run_dir / "results.jsonl", [{
                "claim_id": cid,
                "task_state": "completed",
                "evidence_candidates": [{
                    "id": "ev-api-1",
                    "url": "https://bls.gov/cpi-2025",
                    "published_date": "2026-01-10",
                    "text": body,
                    "archive_path": arch_rel,
                    "archive_sha256": body_sha,
                }],
                "assessment": {
                    "id": cid,
                    "inclusion": "forecast",
                    "verdict": "正确",
                    "basis": "endpoint",
                    "scope": "2025年CPI同比",
                    "reason": "2025年CPI为2.4%，低于3%。",
                    "limitation": "仅看年度均值。",
                    "evidence_ids": ["ev-api-1"],
                    "evidence_notes": [{
                        "evidence_id": "ev-api-1",
                        "relation": "support",
                        "quote": body,
                        "publication_date": "2026-01-10",
                        "observation_end": "2025-12-31",
                        "limitation": "官方CPI公报",
                    }],
                    "method": "约束账本法",
                    "method_basis": "explicit",
                    "observation_end": "2025-12-31",
                    "future_time_text": "",
                    "condition_state": "unconditional",
                    "trend_aligned": False,
                },
            }])

            res = cb.import_verify_run(case_dir, run_dir)
            self.assertEqual(res["new_evidence"], 1)
            cb.sync_database(case_dir, repo_root=repo)
            pr = cb.pr_check(case_dir, repo_root=repo)
            self.assertEqual(pr["pr_check"], "passed")


if __name__ == "__main__":
    unittest.main()
