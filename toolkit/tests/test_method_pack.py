import json
from pathlib import Path
import unittest

REPO_ROOT = Path(__file__).resolve().parents[2]


class MethodPackZeroCodeTrustTests(unittest.TestCase):
    def test_manifest_and_backtest_pack_are_valid_pure_data(self):
        manifest_path = REPO_ROOT / "method-pack/manifest.json"
        backtest_path = REPO_ROOT / "method-pack/curated_backtest_questions.json"
        self.assertTrue(manifest_path.is_file())
        self.assertTrue(backtest_path.is_file())

        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        for key in (
            "schema_version",
            "method_version",
            "onboarding_questions",
            "seven_step_protocol",
            "horizon_base_rates",
            "domain_catalog",
            "noise_linter_rules",
            "factcheck_protocol",
        ):
            self.assertIn(key, manifest)
        self.assertEqual(len(manifest["seven_step_protocol"]), 7)
        self.assertGreaterEqual(len(manifest["domain_catalog"]), 7)

        bt = json.loads(backtest_path.read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(bt["questions"]), 5)
        for q in bt["questions"]:
            self.assertIn("as_of", q)
            self.assertIn("pre_cutoff_context", q)
            self.assertIn(q["actual_outcome"], (0, 1))
            self.assertTrue(0.0 <= float(q["market_prob_at_cutoff"]) <= 1.0)

    def test_agent_onboarding_docs_never_instruct_executable_downloads(self):
        """Guardrail: onboarding docs must never ask users/agents to curl|bash or download .py/.sh scripts."""
        for rel in ("AGENT_SETUP.md", "README.md", "docs/05-quickstart-onboarding-and-polymarket.md"):
            content = (REPO_ROOT / rel).read_text(encoding="utf-8")
            self.assertNotIn("| bash", content, f"{rel} must not contain pipe-to-bash instructions")
            self.assertNotIn("| sh", content, f"{rel} must not contain pipe-to-sh instructions")
            self.assertNotIn("bootstrap.sh", content, f"{rel} must not reference executable bootstrap scripts")
            self.assertNotIn("forecast_kit.py", content, f"{rel} must not ask users to download Python scripts")


if __name__ == "__main__":
    unittest.main()
