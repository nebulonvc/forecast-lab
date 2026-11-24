import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import periodic_tracker as pt  # noqa: E402
import pipeline as pl  # noqa: E402
import verify_prediction as vp  # noqa: E402


class PeriodicTrackerTests(unittest.TestCase):
    def test_init_add_check_prepare_and_digest_roundtrip(self):
        with tempfile.TemporaryDirectory() as tmp:
            ledger = Path(tmp) / "my-forecasts"
            pt.main([
                "--case", str(ledger),
                "init",
                "--title", "个人定期预测账本测试",
                "--author", "Tester",
                "--cutoff", "2026-11-24",
            ])
            pt.main([
                "--case", str(ledger),
                "add",
                "--id", "my-2026-001",
                "--domain", "AI与电力基础设施",
                "--statement", "到2030年底，美国数据中心年耗电量占全美总发电量比重较2025年提高至少2个百分点。",
                "--horizon", "2026-2030",
                "--scope", "美国EIA或LBNL年度统计公报全美发电量口径",
                "--method", "约束账本法",
                "--counter-lens", "杰文斯悖论与电网审批排队延迟",
                "--indicators", "云厂商CapEx通电机架数、PJM并网排队周期",
                "--falsification", "2030年底占比增幅不足2个百分点",
            ])

            # 1. Must pass pipeline.py check & report cleanly
            pl.main(["--case", str(ledger), "check"])
            self.assertTrue((ledger / "cards/my-2026-001.md").is_file())
            self.assertTrue((ledger / "output/report.md").is_file())

            # 2. Must pass verify_prediction.py --prepare-only without API keys
            out_dir = ledger / "output/search_verify/test-run"
            rc = vp.main([
                "--case", str(ledger),
                "--unresolved",
                "--prepare-only",
                "--output-dir", str(out_dir),
            ])
            self.assertEqual(rc, 0)
            manifest = json.loads((out_dir / "manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["ids"], ["my-2026-001"])

            # 3. Simulate a periodic search run detecting trend progress and check digest shift detection
            fake_results = [{
                "claim_id": "my-2026-001",
                "task_state": "completed",
                "remaining_gap": "2030年终点尚未到达，但2026年在建负荷持续攀升。",
                "evidence_candidates": [{"url": "https://www.eia.gov/outlooks/steo/"}],
                "assessment": {
                    "id": "my-2026-001",
                    "inclusion": "forecast",
                    "verdict": "部分符合",
                    "trend_aligned": True,
                    "reason": "EIA短期能源展望显示数据中心负荷推动商业用电显著上修，方向持续符合。",
                },
            }]
            (out_dir / "results.jsonl").write_text(
                "\n".join(json.dumps(r, ensure_ascii=False) for r in fake_results) + "\n",
                encoding="utf-8",
            )
            digest_info = pt.generate_digest(ledger, search_run_dir=out_dir)
            self.assertEqual(digest_info["total_forecasts"], 1)
            self.assertEqual(digest_info["shift_count"], 1)
            self.assertEqual(digest_info["shifts"][0]["proposed"], "趋势符合")
            digest_md = (ledger / "output/periodic_digest.md").read_text(encoding="utf-8")
            self.assertIn("Signal Shifts", digest_md)
            self.assertIn("https://www.eia.gov/outlooks/steo/", digest_md)

    def test_bump_cutoff_rejects_backwards_date(self):
        with tempfile.TemporaryDirectory() as tmp:
            ledger = Path(tmp) / "ledger"
            pt.init_ledger(ledger, "Test", "User", "2026-11-24")
            updated = pt.bump_cutoff(ledger, "2026-12-01")
            self.assertEqual(updated, "2026-12-01")
            with self.assertRaises(ValueError):
                pt.bump_cutoff(ledger, "2026-10-01")


if __name__ == "__main__":
    unittest.main()
