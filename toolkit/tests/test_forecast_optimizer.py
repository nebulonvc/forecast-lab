import collections
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import forecast_mcp as fmcp  # noqa: E402
import forecast_optimizer as fo  # noqa: E402
import periodic_tracker as pt  # noqa: E402
import pipeline as pl  # noqa: E402


class ForecastOptimizerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = fo.ForecastOptimizerEngine.load()

    def test_corpus_loader_exact_8130_parity(self):
        forecasts, nonforecasts, curated = fo.load_training_corpus()
        self.assertEqual(len(forecasts), 8130)
        self.assertEqual(len(nonforecasts), 2553)
        self.assertEqual(len(curated), 330)
        vc = collections.Counter(r["verdict"] for r in forecasts)
        self.assertEqual(vc["正确"], 1686)
        self.assertEqual(vc["趋势符合"], 971)
        self.assertEqual(vc["部分符合"], 1714)
        self.assertEqual(vc["错误"], 689)
        self.assertEqual(vc["暂无法判断"], 3070)

    def test_saved_model_artifact_and_out_of_book_cv_dominance(self):
        self.assertTrue(fo.DEFAULT_MODEL_PATH.is_file())
        self.assertTrue(fo.DEFAULT_BENCHMARK_PATH.is_file())

        bundle = json.loads(fo.DEFAULT_MODEL_PATH.read_text(encoding="utf-8"))
        saved_sha = bundle.pop("artifact_sha256")
        calc_sha = hashlib.sha256(json.dumps(bundle, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
        self.assertEqual(saved_sha, calc_sha)

        bench = json.loads(fo.DEFAULT_BENCHMARK_PATH.read_text(encoding="utf-8"))
        m0 = bench["models"]["M0_Uniform_Marginal_Prior"]
        m1 = bench["models"]["M1_Static_Horizon_Explicit_Table"]
        m3 = bench["models"]["M3_Regularized_GLMM_NoHist_Ablation"]
        m4 = bench["models"]["M4_Regularized_GLMM_Full_Hist_Lenses"]
        m7 = bench["models"]["M7_Calibrated_LogLinear_SuperLearner"]

        # Adding t0 historical regimes & method lenses strictly improves out-of-book GLMM fit
        self.assertLess(m4["brier_5class"], m3["brier_5class"])
        self.assertLess(m4["logloss_5class"], m3["logloss_5class"])

        # Production Super-Learner strictly beats both Marginal and Static Horizon Table across proper scoring rules
        self.assertLess(m7["brier_5class"], m0["brier_5class"])
        self.assertLess(m7["brier_5class"], m1["brier_5class"])
        self.assertLess(m7["logloss_5class"], m1["logloss_5class"])
        self.assertLess(m7["decided_brier_4class"], m1["decided_brier_4class"])
        self.assertLess(m7["decided_logloss_4class"], m1["decided_logloss_4class"])
        self.assertLess(m7["decided_ordinal_rps"], m1["decided_ordinal_rps"])
        self.assertLess(m7["decided_ece_directional"], 0.03)

    def test_point_in_time_priors_prevent_lookahead_leakage(self):
        past_train = [
            {"pub_year": 1970, "domain": "地缘政治与国际秩序", "verdict": "正确"},
            {"pub_year": 1980, "domain": "地缘政治与国际秩序", "verdict": "错误"},
        ]
        future_shock = [
            {"pub_year": 2024, "domain": "地缘政治与国际秩序", "verdict": "正确"}
            for _ in range(50)
        ]
        target = [{"pub_year": 2000, "domain": "地缘政治与国际秩序"}]
        p_without_future = fo.compute_pit_priors_fast(past_train, target)[0]
        p_with_future = fo.compute_pit_priors_fast(past_train + future_shock, target)[0]
        self.assertEqual(p_without_future, p_with_future)

    def test_optimize_forecast_detects_traps_and_validates_rewrite(self):
        noisy = self.engine.optimize_forecast(
            statement="到2028年底，AI将彻底取代50%以上的软件工程师工作，代码编写成本每年减半。",
            domain="AI",
        )
        trap_ids = {t["trap_id"] for t in noisy["operationalizability_audit"]["traps_detected"]}
        self.assertIn("unanchored_hard_number", trap_ids)
        self.assertIn("surpass_explicit_no_ledger", trap_ids)
        self.assertIn("linear_rate_extrapolation", trap_ids)
        self.assertGreater(noisy["expected_uplift"]["delta_strict_win_prob_pp"], 5.0)
        self.assertLess(noisy["expected_uplift"]["delta_error_prob_pp"], -2.0)

        refined = self.engine.optimize_forecast(
            statement="到2030年底，美国数据中心年耗电量占全美总发电量的比例较2025年提高至少2.0个百分点。",
            domain="人口、能源、资源与生态",
            horizon="2026-2030",
            scope="以美国EIA或LBNL年度正式电力统计公报全美总发电量为分母；基于存量机架与在建变电站排期核算。",
            method="约束账本法",
            counter_lens="杰文斯效率反弹与区域电网并网排队延迟",
            leading_indicators="四大云厂商季度CapEx指引、PJM大负荷并网排队时长",
            falsification="2030年底占比增幅低于2.0个百分点",
            forecaster_stance="国际机构与政府智库",
        )
        self.assertEqual(refined["operationalizability_audit"]["score_out_of_6"], 6)
        self.assertEqual(len(refined["operationalizability_audit"]["traps_detected"]), 0)
        p5 = refined["baseline_evaluation"]["probs_5class"]
        self.assertAlmostEqual(sum(p5.values()), 1.0, places=3)

    def test_domain_and_horizon_adaptive_method_selection(self):
        energy_short = self.engine.optimize_forecast(
            statement="未来四年电网级储能新增装机占比提升",
            domain="能源",
            target_years=4,
        )["recommended_optimization"]
        self.assertEqual(energy_short["method_key"], "constraint_ledger")
        self.assertEqual(energy_short["commitment_regime"], "explicit_interval_with_ledger")

        geo_long = self.engine.optimize_forecast(
            statement="未来二十五年欧亚大陆边缘海道战略竞争持续",
            domain="地缘政治",
            target_years=25,
        )["recommended_optimization"]
        self.assertEqual(geo_long["method_key"], "geopolitical_chassis")
        self.assertEqual(geo_long["commitment_regime"], "directional_structural_window")

    def test_three_axis_bayesian_update_and_confirmation_bias_guard(self):
        prior = {"正确": 0.35, "趋势符合": 0.25, "部分符合": 0.25, "错误": 0.15}
        one_sided = self.engine.bayesian_update(
            prior_decided_probs=prior,
            evidence_items=[
                {"relation": "support", "source_tier": "official_stats", "axis": "event", "summary": "EIA最新统计占比已升0.9pp"},
            ],
        )
        self.assertIsNotNone(one_sided["confirmation_bias_warning"])
        self.assertGreater(one_sided["posterior_decided_4class"]["正确"], prior["正确"])
        self.assertLess(one_sided["posterior_decided_4class"]["错误"], prior["错误"])

        balanced = self.engine.bayesian_update(
            prior_decided_probs=prior,
            evidence_items=[
                {"relation": "support", "source_tier": "official_stats", "axis": "event", "summary": "机架用电增长符合方向"},
                {"relation": "counter", "source_tier": "institutional", "axis": "time", "summary": "变压器交付周期拉长至36个月"},
            ],
        )
        self.assertIsNone(balanced["confirmation_bias_warning"])
        self.assertAlmostEqual(sum(balanced["posterior_decided_4class"].values()), 1.0, places=3)

    def test_mcp_server_protocol_and_register_roundtrip(self):
        with tempfile.TemporaryDirectory() as tmp:
            ledger = Path(tmp) / "test-ledger"
            pt.init_ledger(ledger, title="MCP测试账本", author="AgentTester", cutoff="2026-11-24")

            srv = fmcp.ForecastMCPServer()
            # Notification returns None
            self.assertIsNone(srv.handle_request({"jsonrpc": "2.0", "method": "notifications/initialized"}))

            # Register optimized forecast via MCP tool
            reg_resp = srv.handle_request({
                "jsonrpc": "2.0",
                "id": 10,
                "method": "tools/call",
                "params": {
                    "name": "register_optimized_forecast",
                    "arguments": {
                        "claim_id": "mcp-opt-001",
                        "domain": "人口、能源、资源与生态",
                        "statement": "到2030年底，全球公用事业级新型储能新增装机中无镍钴路线占比达到35%以上。",
                        "horizon": "2026-2030",
                        "scope": "以IEA年度储能统计公报新增并网GWh为分母",
                        "method": "约束账本法",
                        "counter_lens": "碳酸锂价格长期低位抑制钠电替代经济性",
                        "leading_indicators": "磷酸铁锂与钠离子电芯价差、电网侧招标中标份额",
                        "falsification": "2030年新增装机占比低于35%",
                        "ledger_path": str(ledger),
                    },
                },
            })
            self.assertFalse(reg_resp["result"]["isError"])
            pl.main(["--case", str(ledger), "check"])

            audit_resp = srv.handle_request({
                "jsonrpc": "2.0",
                "id": 11,
                "method": "tools/call",
                "params": {"name": "audit_forecast_ledger", "arguments": {"ledger_path": str(ledger)}},
            })
            audit_data = json.loads(audit_resp["result"]["content"][0]["text"])
            self.assertEqual(audit_data["forecast_count"], 1)
            self.assertEqual(audit_data["items"][0]["operationalizability_score"], 6)

        # End-to-end stdio subprocess test (newline-delimited JSON-RPC 2.0)
        mcp_script = Path(__file__).resolve().parents[1] / "forecast_mcp.py"
        requests = "\n".join([
            json.dumps({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2025-03-26"}}),
            json.dumps({"jsonrpc": "2.0", "method": "notifications/initialized"}),
            json.dumps({"jsonrpc": "2.0", "id": 2, "method": "resources/list", "params": {}}),
            json.dumps({"jsonrpc": "2.0", "id": 3, "method": "prompts/get", "params": {"name": "optimize-my-prediction", "arguments": {"draft_idea": "AI取代程序员"}}}),
        ]) + "\n"
        proc = subprocess.run(
            [sys.executable, str(mcp_script)],
            input=requests.encode("utf-8"),
            capture_output=True,
            timeout=15,
            check=True,
        )
        lines = [json.loads(line) for line in proc.stdout.decode("utf-8").splitlines() if line.strip()]
        self.assertEqual(len(lines), 3)  # notification produced no response
        self.assertEqual(lines[0]["id"], 1)
        self.assertEqual(len(lines[1]["result"]["resources"]), 3)
        self.assertIn("optimize_forecast", lines[2]["result"]["messages"][0]["content"]["text"])


if __name__ == "__main__":
    unittest.main()
