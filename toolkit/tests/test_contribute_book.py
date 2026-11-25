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

    def test_anti_laziness_proof_of_reading_and_dual_evidence_gates(self):
        with tempfile.TemporaryDirectory() as d:
            repo = self._make_temp_repo(Path(d))
            case_dir = repo / "cases/anti-lazy-book-v5"
            cb.init_case(
                case_dir,
                book="防偷懒压测之书",
                author="严格审计员",
                publication_year=2021,
                domain="科技商业",
                author_type="科技商业思想家",
                cutoff="2026-11-24",
                execution_mode="agent-native-v5",
            )
            txt_path = case_dir / "input/book.txt"
            head_part = "第一章 导论\n" + ("这是前半部分的论述文字，探讨产业链的早期演进背景。" * 18)
            tail_part = "在章节结尾处，到2025年底全球电动重卡渗透率将突破10%。这是本章末尾的终局锚点句子。\n"
            chap2 = "第二章 尾声\n" + ("第二章前半段讨论基础设施布局与电网改造进度。" * 18) + "本章末尾总结：电网储能成本还将继续下降。\n"
            txt_path.write_text(head_part + "\n" + tail_part + "\n" + chap2, encoding="utf-8")

            manifest = cb.chunk_txt_for_agent(case_dir, txt_path, chunk_chars=550, context_chars=100, batch_size=1, repo_root=repo)
            self.assertGreaterEqual(manifest["active_chunks"], 2)
            self.assertEqual(len(manifest["batches"]), manifest["active_chunks"])

            # 1. Initial audit-progress reports 0 proof_verified_chunks and all batches pending
            prog0 = cb.audit_progress(case_dir)
            self.assertFalse(prog0["extraction"]["ready"])
            self.assertEqual(prog0["extraction"]["proof_verified_chunks"], 0)
            self.assertEqual(len(prog0["extraction"]["pending_batches"]), manifest["active_chunks"])

            chunks = cb._read_jsonl(case_dir / "output/txt_import/chunks.jsonl")
            prop_dir = case_dir / "output/txt_import/chunk_proposals"

            # 2. Simulate a lazy agent that only read the beginning of chunk 1 (tail_anchor from head, not last 45%)
            for ch in chunks:
                (prop_dir / f"{ch['id']}.json").write_text(
                    json.dumps({
                        "id": ch["id"],
                        "body_sha256_12": ch["body_sha256_12"],
                        "tail_anchor": ch["body"][:16].strip(),
                        "predictions": [],
                    }, ensure_ascii=False),
                    encoding="utf-8",
                )
            with self.assertRaisesRegex(ValueError, "Lazy agent guard.*not in the last 45%"):
                cb.import_agent_extractions(case_dir, txt_path, prop_dir, require_proof=True, repo_root=repo)

            # 3. Simulate a lazy agent with fabricated/wrong body_sha256_12
            (prop_dir / f"{chunks[0]['id']}.json").write_text(
                json.dumps({
                    "id": chunks[0]["id"],
                    "body_sha256_12": "000000000000",
                    "tail_anchor": chunks[0]["body"][-20:].strip(),
                    "predictions": [],
                }, ensure_ascii=False),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "Lazy agent guard.*body_sha256_12 mismatch"):
                cb.import_agent_extractions(case_dir, txt_path, prop_dir, require_proof=True, repo_root=repo)

            # 4. Write valid proof-of-reading for all chunks
            for ch in chunks:
                preds = []
                if "全球电动重卡渗透率将突破10%" in ch["body"]:
                    preds.append({
                        "quote": "到2025年底全球电动重卡渗透率将突破10%。",
                        "kind": "prediction",
                        "claim_type": "forecast",
                        "speaker": "严格审计员",
                        "attribution": "author",
                        "future_oriented": True,
                        "claim": "到2025年底全球电动重卡渗透率将突破10%",
                        "changes": "全球电动重卡渗透率突破10%",
                        "horizon": "到2025年底",
                        "resolvable": True,
                        "confidence": "high",
                        "expanded_claim": "到2025年底全球电动重卡渗透率将突破10%。",
                        "reference_resolutions": [],
                        "unresolved_references": [],
                        "time_text": "到2025年底",
                        "condition_text": "",
                        "method": "S曲线外推",
                        "method_basis": "explicit",
                        "reason": "明确量化预测",
                    })
                (prop_dir / f"{ch['id']}.json").write_text(
                    json.dumps({
                        "id": ch["id"],
                        "body_sha256_12": ch["body_sha256_12"],
                        "tail_anchor": ch["body"][-18:].strip(),
                        "predictions": preds,
                    }, ensure_ascii=False),
                    encoding="utf-8",
                )

            prog1 = cb.audit_progress(case_dir)
            self.assertTrue(prog1["extraction"]["ready"])
            self.assertEqual(prog1["extraction"]["pending_batches"], [])

            imp_res = cb.import_agent_extractions(case_dir, txt_path, prop_dir, require_proof=True, repo_root=repo)
            self.assertEqual(imp_res["proof_of_reading_verified_chunks"], len(chunks))
            self.assertEqual(imp_res["imported_claims"], 1)

            # 5. Verification sharding & Dual-evidence anti-laziness gate
            exp_res = cb.export_verify_tasks(case_dir, batch_size=2)
            self.assertEqual(exp_res["tasks"], 1)
            self.assertEqual(exp_res["batches"], 1)
            cid = cb._read_jsonl(case_dir / "output/verify_tasks.jsonl")[0]["id"]

            ev_raw = case_dir / "output/evidence_raw.jsonl"
            ev_raw.write_text(
                json.dumps({
                    "id": "ev-01",
                    "url": "https://iea.org/reports/global-ev-outlook-2026",
                    "date": "2026-04-10",
                    "coverage": "2021-2025",
                    "excerpt": "2025年全球电动重卡销量占比约为3.8%，主要集中在中国与欧洲。",
                    "limitation": "IEA全球口径",
                    "text": "国际能源署（IEA）《2026全球电动汽车展望》官方统计数据显示：截至2025年底，全球重型卡车电动化渗透率达到3.8%，虽较2021年显著增长，但受限于长途干线充电兆瓦级快充网络建设滞后，未达到10%门槛。",
                }, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
            asm_path = case_dir / "output/assessments.jsonl"
            asm_obj = {
                "id": cid,
                "inclusion": "forecast",
                "verdict": "错误",
                "basis": "endpoint",
                "scope": "2025年底全球电动重卡销量渗透率",
                "reason": "2025年底全球电动重卡实际渗透率约3.8%，未突破10%。",
                "limitation": "各国重卡吨位定义存在差异。",
                "evidence_ids": ["ev-01"],
                "method": "S曲线外推",
                "method_basis": "explicit",
                "observation_end": "2025-12-31",
                "future_time_text": "",
                "condition_state": "unconditional",
                "trend_aligned": False,
            }
            asm_path.write_text(json.dumps(asm_obj, ensure_ascii=False) + "\n", encoding="utf-8")

            # Lazy single-evidence submission is rejected when require_dual_evidence=True
            with self.assertRaisesRegex(ValueError, "Lazy agent guard.*at least 2 independent evidence"):
                cb.apply_agent_assessments(case_dir, asm_path, evidence_raw_path=ev_raw, require_dual_evidence=True)

            # Adding second independent evidence item passes dual-evidence check
            with ev_raw.open("a", encoding="utf-8") as f:
                f.write(json.dumps({
                    "id": "ev-02",
                    "url": "https://icct.org/publication/heavy-duty-zevs-2025",
                    "date": "2026-03-18",
                    "coverage": "2025",
                    "excerpt": "中国2025年新能源重卡渗透率突破12%，但北美与拉美市场仍低于1.5%，拉低全球均值。",
                    "limitation": "ICCT区域对比报告",
                    "text": "国际清洁交通委员会（ICCT）2026年3月发布的《全球零排放重型商用车市场追踪》指出：2025年中国新能源重卡销量占比已突破12%（支持局部市场破10%的趋势），然而美国、印度及拉美市场受制于兆瓦充电桩与购置成本，渗透率不足1.5%，导致全球汇总渗透率停留在3.8%~4.1%区间。",
                }, ensure_ascii=False) + "\n")
            asm_obj["evidence_ids"] = ["ev-01", "ev-02"]
            asm_path.write_text(json.dumps(asm_obj, ensure_ascii=False) + "\n", encoding="utf-8")

            app_res = cb.apply_agent_assessments(case_dir, asm_path, evidence_raw_path=ev_raw, require_dual_evidence=True)
            self.assertEqual(app_res["dual_evidence_verified"], 1)
            self.assertEqual(app_res["evidence_registered"], 2)

            # 6. Multi-round adaptive search (search-verifier-v3 parity) & independent 6-check semantic review tests
            # 6a. Unresolved forecast ('暂无法判断') with only 1 initial round and 0 adaptive rounds must be rejected
            unresolved_lazy = {
                **asm_obj,
                "verdict": "暂无法判断",
                "basis": "evidence",
                "evidence_ids": ["ev-01"],
                "remaining_gap": "缺少2025年底拉美与非洲重卡保有量分母统计",
                "evidence_notes": [{
                    "evidence_id": "ev-01",
                    "relation": "support",
                    "quote": "截至2025年底，全球重型卡车电动化渗透率达到3.8%",
                    "publication_date": "2026-04-10",
                    "observation_end": "2025-12-31",
                    "limitation": "IEA口径",
                }],
                "round_history": [{
                    "index": 1,
                    "round": 1,
                    "kind": "initial",
                    "strategy_change": None,
                    "gap_before": None,
                    "queries": [
                        {"role": "support", "query": "global electric heavy duty truck sales share 2025"},
                        {"role": "counter", "query": "electric heavy truck adoption bottleneck 2025"},
                    ],
                }],
            }
            asm_path.write_text(json.dumps(unresolved_lazy, ensure_ascii=False) + "\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Multi-round guard.*only ran 0 adaptive round"):
                cb.apply_agent_assessments(
                    case_dir, asm_path, evidence_raw_path=ev_raw, require_adaptive_rounds=True
                )

            # 6b. Adaptive round repeating a previous query must be rejected
            unresolved_dup_q = {
                **unresolved_lazy,
                "round_history": [
                    unresolved_lazy["round_history"][0],
                    {
                        "index": 2,
                        "round": 2,
                        "kind": "adaptive",
                        "gap_before": "缺少拉美与非洲电动重卡官方销量分母",
                        "strategy_change": "切换至区域清洁交通统计数据库",
                        "queries": [{
                            "role": "support",
                            "query": "Global Electric Heavy Duty Truck Sales Share 2025",
                            "strategy": "重复上一轮英文查询",
                        }],
                    },
                ],
            }
            asm_path.write_text(json.dumps(unresolved_dup_q, ensure_ascii=False) + "\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Multi-round guard.*repeated prior query"):
                cb.apply_agent_assessments(
                    case_dir, asm_path, evidence_raw_path=ev_raw, require_adaptive_rounds=True
                )

            # 6c. Valid 2 adaptive rounds with distinct strategy_change & non-duplicate queries passes unresolved check
            unresolved_valid = {
                **unresolved_lazy,
                "round_history": [
                    unresolved_lazy["round_history"][0],
                    {
                        "index": 2,
                        "round": 2,
                        "kind": "adaptive",
                        "gap_before": "缺少拉美与非洲电动重卡官方销量分母",
                        "strategy_change": "改查ICCT与OICA各国商用车注册分类统计表",
                        "queries": [{
                            "role": "support",
                            "query": "OICA heavy commercial vehicle registration electric 2025",
                            "strategy": "改用国际汽车制造商协会OICA官方注册量口径",
                        }],
                    },
                    {
                        "index": 3,
                        "round": 3,
                        "kind": "adaptive",
                        "gap_before": "OICA尚未发布2025第四季度发展中国家分动力类型重卡细项",
                        "strategy_change": "检索各国交通部年鉴与彭博新能源财经BNEF公开摘要",
                        "queries": [{
                            "role": "counter",
                            "query": "BNEF zero emission commercial truck fleet share 2025 report",
                            "strategy": "补充BNEF全球商用车电动化年度追踪口径",
                        }],
                    },
                ],
            }
            asm_path.write_text(json.dumps(unresolved_valid, ensure_ascii=False) + "\n", encoding="utf-8")
            res_unres = cb.apply_agent_assessments(
                case_dir, asm_path, evidence_raw_path=ev_raw, require_adaptive_rounds=True
            )
            self.assertEqual(res_unres["multi_round_traces_verified"], 1)

            # 6d. Decided forecast with verbatim evidence_notes + independent 6-check semantic review
            decided_v3 = {
                **asm_obj,
                "evidence_ids": ["ev-01", "ev-02"],
                "remaining_gap": "",
                "evidence_notes": [
                    {
                        "evidence_id": "ev-01",
                        "relation": "counter",
                        "quote": "截至2025年底，全球重型卡车电动化渗透率达到3.8%",
                        "publication_date": "2026-04-10",
                        "observation_end": "2025-12-31",
                        "limitation": "IEA全球口径",
                    },
                    {
                        "evidence_id": "ev-02",
                        "relation": "support",
                        "quote": "2025年中国新能源重卡销量占比已突破12%",
                        "publication_date": "2026-03-18",
                        "observation_end": "2025-12-31",
                        "limitation": "ICCT区域对比口径",
                    },
                ],
                "round_history": [unresolved_lazy["round_history"][0]],
            }
            asm_path.write_text(json.dumps(decided_v3, ensure_ascii=False) + "\n", encoding="utf-8")

            srev_path = case_dir / "output/semantic_reviews/vbatch-0001.jsonl"
            # First test: unaddressed decision='revise' is blocked by semantic review guard
            srev_revise = {
                "id": cid,
                "decision": "revise",
                "checks": {
                    "object_match": "pass",
                    "condition_logic": "pass",
                    "time_alignment": "pass",
                    "evidence_support": "pass",
                    "counterevidence": "pass",
                    "verdict_logic": "fail",
                },
                "issues": [{
                    "check": "verdict_logic",
                    "reason": "需在reason中补充说明中国市场虽突破12%但全球总口径为3.8%",
                    "source_quote": "2025年底全球电动重卡实际渗透率约3.8%，未突破10%。",
                    "evidence_id": None,
                }],
                "remaining_gap": "补充区域分化说明",
            }
            srev_path.write_text(json.dumps(srev_revise, ensure_ascii=False) + "\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Semantic review guard.*unaddressed review decision='revise'"):
                cb.apply_agent_assessments(
                    case_dir,
                    asm_path,
                    evidence_raw_path=ev_raw,
                    semantic_reviews_path=srev_path,
                    require_dual_evidence=True,
                    require_adaptive_rounds=True,
                    require_semantic_review=True,
                )

            # Second test: accepted 6-check semantic review passes all v3 gates
            srev_accept = {
                "id": cid,
                "decision": "accept",
                "checks": {
                    "object_match": "pass",
                    "condition_logic": "pass",
                    "time_alignment": "pass",
                    "evidence_support": "pass",
                    "counterevidence": "pass",
                    "verdict_logic": "pass",
                },
                "issues": [],
                "remaining_gap": "",
            }
            srev_path.write_text(json.dumps(srev_accept, ensure_ascii=False) + "\n", encoding="utf-8")
            res_v3 = cb.apply_agent_assessments(
                case_dir,
                asm_path,
                evidence_raw_path=ev_raw,
                semantic_reviews_path=srev_path,
                require_dual_evidence=True,
                require_adaptive_rounds=True,
                require_semantic_review=True,
            )
            self.assertEqual(res_v3["dual_evidence_verified"], 1)
            self.assertEqual(res_v3["multi_round_traces_verified"], 1)
            self.assertEqual(res_v3["semantic_reviews_verified"], 1)

            # 6e. Security & cheating edge cases: path traversal eid, coarse YYYY-MM after cutoff, and duplicate-URL cloning
            bad_ev = case_dir / "output/bad_ev.jsonl"
            bad_ev.write_text(
                json.dumps({
                    "id": "../escape",
                    "url": "https://iea.org/ok",
                    "date": "2025-01-01",
                    "text": "合法长度的正文内容，用于测试路径穿越证据ID是否会被直接拒绝。" * 3,
                }, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "Invalid or unsafe evidence id"):
                cb.apply_agent_assessments(case_dir, asm_path, evidence_raw_path=bad_ev)

            bad_ev.write_text(
                json.dumps({
                    "id": "ev-future-month",
                    "url": "https://iea.org/future",
                    "date": "2026-12",
                    "text": "合法长度的正文内容，但发表年月2026-12晚于cutoff 2026-11-24。" * 3,
                }, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "invalid or after cutoff"):
                cb.apply_agent_assessments(case_dir, asm_path, evidence_raw_path=bad_ev)

            cloned_url_ev = case_dir / "output/cloned_url_ev.jsonl"
            cloned_url_ev.write_text(
                json.dumps({
                    "id": "ev-dup-1",
                    "url": "https://iea.org/same-page",
                    "date": "2026-04-10",
                    "text": "国际能源署（IEA）官方统计数据显示：截至2025年底，全球重型卡车电动化渗透率达到3.8%，未达10%。" * 2,
                }, ensure_ascii=False) + "\n"
                + json.dumps({
                    "id": "ev-dup-2",
                    "url": "https://iea.org/same-page",
                    "date": "2026-04-10",
                    "text": "同一网页的第二段摘录：2025年中国新能源重卡销量占比已突破12%，但欧美市场较低。" * 2,
                }, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
            cloned_asm = case_dir / "output/cloned_asm.jsonl"
            cloned_asm.write_text(
                json.dumps({**decided_v3, "evidence_ids": ["ev-dup-1", "ev-dup-2"]}, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "Lazy agent guard.*only 1 distinct URL"):
                cb.apply_agent_assessments(
                    case_dir, cloned_asm, evidence_raw_path=cloned_url_ev, require_dual_evidence=True
                )
            bad_ev.unlink()
            cloned_url_ev.unlink()
            cloned_asm.unlink()

            # Verify audit_progress confirms strict_v3_ready == True on the clean v3 state
            prog_v3 = cb.audit_progress(case_dir)
            self.assertTrue(prog_v3["verification"]["strict_v3_ready"])


if __name__ == "__main__":
    unittest.main()
