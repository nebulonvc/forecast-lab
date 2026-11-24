"""End-to-end worker tests use synthetic APIs; no external calls are made."""
import contextlib
import copy
import io
import json
from pathlib import Path
import sys
import tempfile
import threading
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import verify_prediction as vp


BODY = "In 2025 the population was 1000. The comparable 1991 population was 1200."


def packet(ident="a"):
    return {
        "id": ident, "book": "Synthetic book", "cutoff": "2026-11-09",
        "publication_year_proxy": 1991,
        "claim": {
            "id": ident, "quote": "The population will decline.",
            "context": "This concerns the example region after 1991.",
            "speaker": "Author", "source_verified": True, "duplicate_of": None,
            "extraction_v2": {
                "id": ident, "kind": "prediction", "claim": "The population will decline.",
                "expanded_claim": "The example region population will decline after 1991.",
                "reference_resolutions": [], "unresolved_references": [],
                "time_text": "after 1991", "condition_text": "",
                "method": "Trend extrapolation", "method_basis": "explicit",
                "reason": "Original text points to a future result.",
            },
            "assessment": {"verdict": "暂无法判断", "evidence_ids": []},
        },
        "existing_evidence": [],
    }


def assessment(ident, evidence_id=None, **changes):
    item = {
        "id": ident, "inclusion": "forecast", "verdict": "正确",
        "basis": "observed_window", "scope": "Example region, 1991 to 2025.",
        "reason": "The comparable reported population declined.",
        "limitation": "Only this region and observed window are assessed.",
        "evidence_ids": [evidence_id] if evidence_id else [],
        "method": "Trend extrapolation", "method_basis": "explicit",
        "observation_end": "2025-12-31", "future_time_text": "",
        "condition_state": "unconditional", "trend_aligned": False,
        "evidence_notes": [{
            "evidence_id": evidence_id, "relation": "support", "quote": BODY,
            "publication_date": "2026-01-01", "observation_end": "2025-12-31",
            "limitation": "Synthetic source for a deterministic test.",
        }] if evidence_id else [],
        "remaining_gap": "",
    }
    item.update(changes)
    return item


class FakeExa:
    def __init__(self, *, date="2026-01-01T00:00:00Z", failed_role=None, no_text=False, body=BODY):
        self.date = date
        self.failed_role = failed_role
        self.no_text = no_text
        self.body = body
        self.search_calls = []
        self.content_calls = []
        self.lock = threading.Lock()

    def search(self, query, cutoff, num_results=5):
        ident, role = query.split()[:2]
        url = "https://source.example/" + ident + "/" + role
        with self.lock:
            self.search_calls.append((query, cutoff, num_results))
        result = {"id": url, "url": url, "title": ident + " " + role,
                  "highlights": ["A search snippet is not the source body."]}
        if self.date is not None:
            result["publishedDate"] = self.date
        return {"requestId": ident + "-" + role, "results": [result]}

    def contents(self, urls):
        with self.lock:
            self.content_calls.append(list(urls))
        results, statuses = [], []
        for url in urls:
            if self.failed_role and url.endswith("/" + self.failed_role):
                statuses.append({"id": url, "status": "error",
                                 "error": {"tag": "CRAWL_NOT_FOUND"}})
                continue
            row = {"id": url, "url": url, "title": "Actual source page",
                   "text": "" if self.no_text else self.body}
            if self.date is not None:
                row["publishedDate"] = self.date
            results.append(row)
            statuses.append({"id": url, "status": "success", "source": "live"})
        return {"requestId": "read", "results": results, "statuses": statuses}

    def totals(self):
        return {"search_requests": len(self.search_calls),
                "contents_requests": len(self.content_calls)}


class FakeLLM:
    def __init__(self, *, failed_id=None, barrier=None, selected_url=None,
                 forged_quote=False, foreign_evidence=False, final_overrides=None,
                 second_round=False, note_publication_date="2026-01-01", second_scope=None, note_quote=None,
                 review_script=None, revision_overrides=None):

        self.failed_id = failed_id
        self.barrier = barrier
        self.selected_url = selected_url
        self.forged_quote = forged_quote
        self.foreign_evidence = foreign_evidence
        self.final_overrides = final_overrides or {}
        self.second_round = second_round
        self.note_publication_date = note_publication_date
        self.second_scope = second_scope
        self.note_quote = note_quote
        self.review_script = review_script or ["accept"]
        self.revision_overrides = revision_overrides or {}
        self.review_counts = {}
        self.calls = []
        self.requests = []
        self.plan_counts = {}
        self.lock = threading.Lock()

    def call(self, stage, request, cases, batch_number):
        data = json.loads(request["messages"][-1]["content"])
        ident = cases[0]["id"]
        with self.lock:
            self.calls.append((ident, stage, data))
            self.requests.append((stage, copy.deepcopy(request)))
            if stage == "search_plan":
                self.plan_counts[ident] = self.plan_counts.get(ident, 0) + 1
            round_number = self.plan_counts.get(ident, 0)
        if stage == "search_plan":
            if round_number == 1 and self.barrier:
                self.barrier.wait(timeout=3)
            if ident == self.failed_id:
                raise TimeoutError("synthetic transport interruption")
            queries = [] if round_number > 1 and not self.second_round else [
                {"role": "support", "query": ident + " support"},
                {"role": "counter", "query": ident + " counter"},
            ]
            scope = self.second_scope if round_number > 1 and self.second_scope else "Example region after 1991."
            item = {"id": ident, "scope": scope, "queries": queries}
            if data.get("round_kind") == "adaptive":
                item["strategy_change"] = "Public search cannot add a series beyond the sources already read."
                item["queries"] = [{**query, "query": query["query"] + " adaptive " + str(round_number),
                                    "strategy": "different phrasing, source type, or language"} for query in queries]
            return [item]
        if stage == "select_sources":
            allowed = list(data.get("allowed_urls") or [])
            urls = ["https://source.example/" + ident + "/support",
                    "https://source.example/" + ident + "/counter"]
            urls = [url for url in urls if not allowed or url in allowed] or allowed[:2]
            if self.selected_url:
                urls = [self.selected_url]
            return [{"id": ident, "urls": urls, "reason": "Read both search directions."}]
        if stage == "semantic_review":
            with self.lock:
                review_number = self.review_counts.get(ident, 0)
                self.review_counts[ident] = review_number + 1
            scripted = self.review_script[min(review_number, len(self.review_script) - 1)]
            if isinstance(scripted, dict):
                return [{"id": ident, **copy.deepcopy(scripted)}]
            checks = {name: "pass" for name in (
                "object_match", "condition_logic", "time_alignment", "evidence_support",
                "counterevidence", "verdict_logic",
            )}
            issues, gap = [], ""
            if scripted != "accept":
                checks["object_match"] = "fail" if scripted == "revise" else "unknown"
                gap = "The original region must be matched to the observed population series."
                issues = [{"check": "object_match", "reason": gap,
                           "source_quote": data["cases"][0]["quote"], "evidence_id": None}]
            return [{"id": ident, "decision": scripted, "checks": checks,
                     "issues": issues, "remaining_gap": gap}]
        if stage not in {"assess", "revise_assessment"}:
            raise AssertionError("Unexpected LLM stage " + stage)
        refs = cases[0].get("allowed_evidence_ids", [])
        evidence_id = refs[0] if refs else None
        overrides = dict(self.final_overrides)
        if stage == "revise_assessment":
            overrides.update(self.revision_overrides)
        item = assessment(ident, evidence_id, **copy.deepcopy(overrides))
        if item["evidence_notes"]:
            item["evidence_notes"][0]["publication_date"] = self.note_publication_date
            if self.note_quote is not None:
                item["evidence_notes"][0]["quote"] = self.note_quote
        if self.foreign_evidence:
            item["evidence_ids"] = ["another-job-evidence"]
            item["evidence_notes"] = [dict(item["evidence_notes"][0], evidence_id="another-job-evidence")]
        if self.forged_quote:
            item["evidence_notes"][0]["quote"] = "Fabricated: the population was 99."
        return [item]

    def totals(self):
        return {"mock_calls": len(self.calls)}


class VerifyPredictionTests(unittest.TestCase):
    def test_audit_budget_cannot_interrupt_formal_revision(self):
        class LimitedLLM(FakeLLM):
            def __init__(self):
                super().__init__(review_script=['revise', 'accept'])
                self.attempts = 0

            def call(self, *args):
                self.attempts += 1
                if self.attempts > 7:
                    raise ValueError('estimated_budget_reservation_exceeded')
                return super().call(*args)

        with tempfile.TemporaryDirectory() as directory:
            item = packet()
            item['review_audit'] = True
            llm = LimitedLLM()
            result = vp.run_job(item, Path(directory), llm, FakeExa())
            self.assertEqual(result['task_state'], 'completed')
            self.assertEqual(llm.attempts, 7)
            vp.ra.run_audits([item], Path(directory), llm)
            resumed = vp.run_job(item, Path(directory), llm, FakeExa())
            self.assertEqual(resumed['task_state'], 'completed')
            self.assertEqual(resumed['assessment'], result['assessment'])

    def test_resume_recipe_is_checked_before_any_calibration_calls(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            case = self.setup_case(directory)
            key = root / 'key'
            key.write_text('synthetic-key')
            args = ['--case', str(case), '--all-forecasts', '--review-audit',
                    '--key-file', str(key), '--exa-key-file', str(key), '--output-dir', str(root / 'run')]
            with mock.patch.object(vp.rp, 'Runner', side_effect=lambda *a, **kw: FakeLLM()), \
                 mock.patch.object(vp, 'ExaClient', side_effect=lambda *a, **kw: FakeExa()), \
                 mock.patch('calibrate_review_policy.run_calibration') as calibration, \
                 contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(vp.main(args), 0)
                calibration.reset_mock()
                with mock.patch.object(vp.sr, 'REVIEW_PROMPT', vp.sr.REVIEW_PROMPT + ' Changed rules.'):
                    with self.assertRaisesRegex(ValueError, 'run_configuration_changed'):
                        vp.main(args)
                calibration.assert_not_called()

    def test_primary_review_is_not_given_a_mechanical_verdict(self):
        llm = FakeLLM()
        result = self.run_one(llm=llm)
        review_data = [data for _, stage, data in llm.calls if stage == 'semantic_review'][0]
        self.assertNotIn('mechanical_candidate', review_data)
        self.assertNotIn('mechanical_warnings', review_data)
        self.assertEqual(result['decision_trace'][0]['draft_verdict'], '正确')
        self.assertEqual(result['decision_trace'][0]['mechanical_verdict'], '正确')

    def test_shadow_audit_holds_material_fixed_and_cannot_override_production(self):
        class AuditLLM(FakeLLM):
            def call(self, stage, request, cases, batch_number):
                if request['messages'][0]['content'] == vp.ra.legacy_prompt():
                    raise TimeoutError('synthetic shadow failure')
                return super().call(stage, request, cases, batch_number)

        with tempfile.TemporaryDirectory() as directory:
            item = packet()
            item['review_audit'] = True
            llm = AuditLLM()
            result = vp.run_job(item, Path(directory), llm, FakeExa())
            self.assertEqual(result['diagnostic_llm_calls'], 0)
            vp.ra.run_audits([item], Path(directory), llm)
            result = vp.run_job(item, Path(directory), llm, FakeExa())
        self.assertEqual(result['task_state'], 'completed')
        self.assertEqual(result['assessment']['verdict'], '正确')
        self.assertEqual(result['diagnostic_llm_calls'], 3)
        arms = result['review_audit']['arms']
        self.assertEqual(len({arm['common_input_sha256'] for arm in arms.values()}), 1)
        self.assertEqual(arms['legacy_hint']['status'], 'failed')
        self.assertEqual(arms['legacy_nohint']['status'], 'failed')
        self.assertEqual(arms['shared_nohint']['status'], 'completed')
        self.assertFalse(result['errors'])

    def test_validation_failure_gets_one_api_repair_then_normal_review(self):
        class RepairLLM(FakeLLM):
            attempts = 0

            def call(self, stage, request, cases, batch_number):
                if stage == 'assess':
                    self.attempts += 1
                    if self.attempts == 1:
                        raise vp.rp.ResponseValidationError('a' * 64, ValueError('cited_source_missing_exact_quote'))
                adapted = copy.deepcopy(request)
                adapted['messages'] = adapted['messages'][:2]
                return super().call(stage, adapted, cases, batch_number)

        llm = RepairLLM()
        result = self.run_one(llm=llm)
        self.assertEqual(result['task_state'], 'completed')
        self.assertEqual(llm.attempts, 2)
        self.assertEqual(len(result['schema_repairs']), 1)
        self.assertEqual(len(result['semantic_reviews']), 1)
        self.assertEqual(result['schema_repairs'][0]['validation_error'], 'cited_source_missing_exact_quote')

    def test_failed_validation_repair_stays_partial_and_stops(self):
        class InvalidLLM(FakeLLM):
            attempts = 0

            def call(self, stage, request, cases, batch_number):
                if stage == 'assess':
                    self.attempts += 1
                    raise vp.rp.ResponseValidationError('b' * 64, ValueError('evidence_quote_not_in_shown_source'))
                return super().call(stage, request, cases, batch_number)

        llm = InvalidLLM()
        result = self.run_one(llm=llm)
        self.assertEqual(result['task_state'], 'partial')
        self.assertEqual(llm.attempts, 2)
        self.assertIsNone(result['assessment'])
        self.assertFalse(result['autonomous_decision'])
        self.assertEqual(len(result['schema_repairs']), 1)

    def run_one(self, *, llm=None, exa=None, ident="a"):
        with tempfile.TemporaryDirectory() as folder:
            return vp.run_job(packet(ident), Path(folder), llm or FakeLLM(), exa or FakeExa())

    def test_stopped_search_provider_spends_no_llm_calls(self):
        exa = FakeExa()
        exa.fatal_error = 'exa_provider_stopped_http_402'
        llm = FakeLLM()
        result = self.run_one(llm=llm, exa=exa)
        self.assertEqual(result['task_state'], 'not_started')
        self.assertEqual(llm.calls, [])
        self.assertEqual(exa.search_calls, [])
        self.assertIn('search_provider_stopped', result['errors'][0]['error'])

    def test_provider_stopping_mid_job_aborts_before_assessment(self):
        class StoppingExa(FakeExa):
            def search(self, query, cutoff, num_results=5):
                self.fatal_error = 'exa_provider_stopped_http_402'
                raise ValueError('exa_provider_stopped_http_402')
        exa = StoppingExa()
        llm = FakeLLM()
        result = self.run_one(llm=llm, exa=exa)
        self.assertNotEqual(result['task_state'], 'completed')
        self.assertEqual([stage for _, stage, _ in llm.calls], ['search_plan'])
        self.assertIsNone(result['assessment'])

    def test_single_task_reads_sources_and_returns_unverified_candidates(self):
        exa = FakeExa()
        llm = FakeLLM()
        result = self.run_one(llm=llm, exa=exa)
        self.assertEqual(result["claim_id"], "a")
        self.assertEqual(result["task_state"], "completed")
        self.assertEqual(result["assessment"]["verdict"], "正确")
        self.assertEqual(len(exa.search_calls), 2)
        self.assertTrue(all(count == 10 for _, _, count in exa.search_calls))
        self.assertEqual({q.split()[1] for q, _, _ in exa.search_calls}, {"support", "counter"})
        self.assertTrue(result["evidence_candidates"])
        self.assertTrue(all(c["verified"] is False for c in result["evidence_candidates"]))
        final_packet = [data for _, stage, data in llm.calls if stage == "assess"][0]
        self.assertIn(BODY, json.dumps(final_packet))
        self.assertLessEqual(len(llm.calls), 8)

    def test_actual_concurrency_failure_isolation_and_completion_callbacks(self):
        barrier = threading.Barrier(2)
        llm = FakeLLM(failed_id="a", barrier=barrier)
        completed = []
        with tempfile.TemporaryDirectory() as folder:
            results = vp.run_jobs([packet("a"), packet("b")], Path(folder), llm, FakeExa(),
                                  workers=2, on_complete=completed.append)
        self.assertEqual([r["claim_id"] for r in results], ["a", "b"])
        self.assertEqual({r["claim_id"] for r in completed}, {"a", "b"})
        self.assertNotEqual(results[0]["task_state"], "completed")
        self.assertIsNone(results[0]["assessment"])
        self.assertEqual(results[1]["task_state"], "completed")

    def test_unseen_selected_url_is_rejected_before_contents(self):
        exa = FakeExa()
        result = self.run_one(llm=FakeLLM(selected_url="https://invented.example/page"), exa=exa)
        self.assertNotEqual(result["task_state"], "completed")
        self.assertIsNone(result["assessment"])
        self.assertEqual(exa.content_calls, [])

    def test_fabricated_quote_cannot_be_a_scored_suggestion(self):
        result = self.run_one(llm=FakeLLM(forged_quote=True))
        self.assertNotEqual(result["task_state"], "completed")
        self.assertIsNone(result["assessment"])

    def test_pdf_wrapped_quote_restores_source_text_without_changing_raw_proposal(self):
        wrapped = BODY.replace("was 1000", "was\n1000").replace("population was 1200", "population\nwas 1200")
        result = self.run_one(exa=FakeExa(body="Report heading\n" + wrapped + "\nEnd of table."))
        self.assertEqual(result["task_state"], "completed")
        note = result["assessment"]["evidence_notes"][0]
        self.assertEqual(note["quote"], wrapped)
        self.assertEqual(note["quote_verification"], {
            "method": "unique_whitespace_alignment", "model_quote": BODY,
        })
        raw_note = result["raw_assessment"]["evidence_notes"][0]
        self.assertEqual(raw_note["quote"], BODY)
        self.assertNotIn("quote_verification", raw_note)

    def test_whitespace_alignment_cannot_change_numbers_or_punctuation(self):
        wrapped = BODY.replace("was 1000", "was\n1000")
        for quote in (BODY.replace("1000", "1001"), BODY.replace("1000.", "1000,")):
            with self.subTest(quote=quote):
                result = self.run_one(exa=FakeExa(body=wrapped), llm=FakeLLM(note_quote=quote))
                self.assertIsNone(result["assessment"])
                self.assertNotEqual(result["task_state"], "completed")
                self.assertEqual(result["raw_assessment"]["evidence_notes"][0]["quote"], quote)

    def test_ambiguous_whitespace_quote_is_rejected(self):
        wrapped = BODY.replace("was 1000", "was\n1000")
        result = self.run_one(exa=FakeExa(body=wrapped + "\nRepeated section:\n" + wrapped))
        self.assertIsNone(result["assessment"])
        self.assertNotEqual(result["task_state"], "completed")

    def test_overlapping_whitespace_matches_are_ambiguous(self):
        # str.count would return one non-overlapping match for ABCABC in ABCABCABC.
        result = self.run_one(exa=FakeExa(body="ABC\nABC\nABC"),
                              llm=FakeLLM(note_quote="ABCABC"))
        self.assertIsNone(result["assessment"])
        self.assertNotEqual(result["task_state"], "completed")

    def test_evidence_from_another_job_cannot_be_cited(self):
        result = self.run_one(llm=FakeLLM(foreign_evidence=True))
        self.assertNotEqual(result["task_state"], "completed")
        self.assertIsNone(result["assessment"])

    def test_future_observation_end_cannot_be_scored(self):
        result = self.run_one(llm=FakeLLM(final_overrides={"observation_end": "2027-01-01"}))
        self.assertNotEqual(result["task_state"], "completed")
        self.assertIsNone(result["assessment"])

    def test_source_published_after_cutoff_cannot_support_a_score(self):
        result = self.run_one(exa=FakeExa(date="2027-01-01T00:00:00Z"),
                              llm=FakeLLM(note_publication_date="2027-01-01"))
        self.assertNotEqual(result["task_state"], "completed")
        self.assertIsNone(result["assessment"])

    def test_unknown_real_condition_cannot_be_scored(self):
        result = self.run_one(llm=FakeLLM(final_overrides={"condition_state": "unknown"}))
        self.assertNotEqual(result["task_state"], "completed")
        self.assertIsNone(result["assessment"])

    def test_missing_publication_date_warns_without_overriding_an_accepted_verdict(self):
        # A later capture cannot prove that an undated page existed by the cutoff.
        # The warning remains; it does not replace a verdict the reviewer accepted.
        with mock.patch.object(vp.rp, 'now', return_value='2026-11-10T00:00:00+00:00'):
            result = self.run_one(exa=FakeExa(date=None), llm=FakeLLM(note_publication_date=None))
        self.assertEqual(result["task_state"], "completed")
        self.assertEqual(result["assessment"]["verdict"], "正确")
        self.assertEqual(result["semantic_validation"], "accepted")
        self.assertEqual(result["raw_assessment"]["verdict"], "正确")
        self.assertTrue(any(warning["code"] == "publication_date_unconfirmed" and warning["blocks_verdict"] is False
                            for warning in result["validation_warnings"]))
        self.assertTrue(all(warning.get("blocks_verdict") is False for warning in result["validation_warnings"]))

    def test_completed_unresolved_research_is_distinct_from_execution_failure(self):
        unresolved = {
            "verdict": "暂无法判断", "basis": "conditional",
            "condition_state": "unknown", "observation_end": None,
            "evidence_ids": [], "evidence_notes": [],
            "reason": "The original trigger has not been established.",
            "remaining_gap": "A dated record establishing the original trigger is missing.",
        }
        result = self.run_one(llm=FakeLLM(final_overrides=unresolved))
        self.assertEqual(result["task_state"], "completed")
        self.assertEqual(result["assessment"]["verdict"], "暂无法判断")
        self.assertEqual(result["assessment"]["condition_state"], "unknown")
        self.assertTrue(result["remaining_gap"])

    def test_raw_webpage_is_not_replaced_by_search_snippet(self):
        result = self.run_one(exa=FakeExa(no_text=True))
        self.assertFalse(result["assessment"] and result["assessment"]["verdict"] == "正确")
        self.assertFalse(result["evidence_candidates"])

    def test_source_failures_are_preserved_even_if_other_page_succeeds(self):
        result = self.run_one(exa=FakeExa(failed_role="counter"))
        self.assertEqual(result["task_state"], "completed")
        self.assertEqual(result["errors"], [])
        self.assertTrue(result["source_errors"])
        self.assertIn("CRAWL_NOT_FOUND", json.dumps(result["source_errors"]))
        self.assertIn("CRAWL_NOT_FOUND", json.dumps(result["source_statuses"]))
        self.assertTrue(result["evidence_candidates"])

    def test_all_selected_sources_failing_keeps_task_partial(self):
        unresolved = {
            "verdict": "暂无法判断", "basis": "evidence",
            "observation_end": None, "evidence_ids": [], "evidence_notes": [],
            "reason": "No selected page returned usable text.",
            "remaining_gap": "Readable evidence pages are missing.",
        }
        result = self.run_one(exa=FakeExa(no_text=True), llm=FakeLLM(final_overrides=unresolved))
        self.assertEqual(result["task_state"], "partial")
        self.assertTrue(result["source_errors"])
        self.assertTrue(any(err.get("error") == "all_selected_pages_unavailable" for err in result["errors"]))

    def test_successful_resume_makes_no_new_model_or_search_calls(self):
        llm = FakeLLM()
        exa = FakeExa()
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            first = vp.run_job(packet(), root, llm, exa)
            calls = (len(llm.calls), len(exa.search_calls), len(exa.content_calls))
            again = vp.run_job(packet(), root, llm, exa)
            self.assertEqual(first["assessment"], again["assessment"])
            self.assertEqual(calls, (len(llm.calls), len(exa.search_calls), len(exa.content_calls)))

    def test_modified_completed_result_is_rejected_without_new_requests(self):
        llm, exa = FakeLLM(), FakeExa()
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            vp.run_job(packet(), root, llm, exa)
            calls = (len(llm.calls), len(exa.search_calls), len(exa.content_calls))
            result_path = vp.job_directory(root, "a") / "result.json"
            saved = json.loads(result_path.read_text())
            saved["claim_id"] = "a different prediction"
            result_path.write_text(json.dumps(saved))
            with self.assertRaises(ValueError):
                vp.run_job(packet(), root, llm, exa)
            self.assertEqual(calls, (len(llm.calls), len(exa.search_calls), len(exa.content_calls)))

    def test_modified_archived_source_is_rejected_without_new_requests(self):
        llm, exa = FakeLLM(), FakeExa()
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            result = vp.run_job(packet(), root, llm, exa)
            calls = (len(llm.calls), len(exa.search_calls), len(exa.content_calls))
            source = root / result["evidence_candidates"][0]["archive_path"]
            source.write_text("The stored evidence was changed after the judgment.")
            with self.assertRaises(ValueError):
                vp.run_job(packet(), root, llm, exa)
            self.assertEqual(calls, (len(llm.calls), len(exa.search_calls), len(exa.content_calls)))

    def test_contents_canonical_url_keeps_requested_url_provenance(self):
        class RedirectingExa(FakeExa):
            def contents(self, urls):
                response = super().contents(urls)
                for row in response["results"]:
                    row["url"] += "/canonical"
                return response

        result = self.run_one(exa=RedirectingExa())
        self.assertEqual(result["task_state"], "completed")
        self.assertEqual({c["url"] for c in result["evidence_candidates"]},
                         {"https://source.example/a/support", "https://source.example/a/counter"})
        self.assertTrue(all(c["resolved_url"] == c["url"] + "/canonical"
                            for c in result["evidence_candidates"]))

    def test_proposal_prompt_does_not_require_candidates_to_be_already_verified(self):
        llm = FakeLLM()
        result = self.run_one(llm=llm)
        self.assertEqual(result["task_state"], "completed")
        prompt = [request["messages"][0]["content"] for stage, request in llm.requests
                  if stage == "assess"][0]
        # The shared import rubric requires verified evidence. Reusing that rule
        # unchanged would force every new, deliberately unverified candidate to UNKNOWN.
        self.assertNotIn("已判定三类必须引用verified来源", prompt)
        self.assertIn("候选verified=false本身不强制判未知", prompt)
        self.assertIn("正式导入仍须另行语义复核", prompt)

    def test_changed_rubric_cannot_reuse_old_completed_result(self):
        llm, exa = FakeLLM(), FakeExa()
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            vp.run_job(packet(), root, llm, exa)
            calls = len(llm.calls)
            with mock.patch.object(vp, "ASSESS", vp.ASSESS + " A changed research rubric."):
                with self.assertRaises(ValueError):
                    vp.run_job(packet(), root, llm, exa)
            self.assertEqual(len(llm.calls), calls)

    def test_modified_input_cannot_reuse_a_previous_result(self):
        llm = FakeLLM()
        exa = FakeExa()
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            vp.run_job(packet(), root, llm, exa)
            changed = packet()
            changed["claim"]["quote"] = "A different original claim."
            with self.assertRaises(ValueError):
                vp.run_job(changed, root, llm, exa)

    def setup_case(self, folder):
        root = Path(folder) / "case"
        (root / "data").mkdir(parents=True)
        (root / "config.json").write_text(json.dumps({
            "book": "Synthetic book", "publication_year_proxy": 1991,
            "cutoff": "2026-11-09",
        }))
        (root / "data/claims.jsonl").write_text("".join(
            json.dumps(packet(ident)["claim"]) + "\n" for ident in ("a", "b")))
        (root / "data/evidence.jsonl").write_text("")
        return root

    def test_explicit_selection_preserves_order_and_source_files(self):
        with tempfile.TemporaryDirectory() as folder:
            root = self.setup_case(folder)
            before = {p.name: p.read_bytes() for p in (root / "data").iterdir()}
            selected = vp.load_packets(root, ["b", "a"])
            self.assertEqual([p["id"] for p in selected], ["b", "a"])
            self.assertEqual({p.name: p.read_bytes() for p in (root / "data").iterdir()}, before)
            with self.assertRaises(ValueError):
                vp.load_packets(root, ["does-not-exist"])
            with self.assertRaises(ValueError):
                vp.load_packets(root, ["a", "a"])

    def test_prepare_only_requires_ids_and_never_calls_apis(self):
        with tempfile.TemporaryDirectory() as folder:
            root = self.setup_case(folder)
            before = {p.name: p.read_bytes() for p in (root / "data").iterdir()}
            args = ["--case", str(root), "--prepare-only", "--output-dir", str(Path(folder) / "run")]
            with contextlib.redirect_stderr(io.StringIO()):
                with self.assertRaises(SystemExit) as error:
                    vp.main(args)
            self.assertEqual(error.exception.code, 2)
            with mock.patch.object(vp.rp.Runner, "call", side_effect=AssertionError("LLM called")), \
                    contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(vp.main(args + ["--claim-id", "a"]), 0)
            self.assertEqual({p.name: p.read_bytes() for p in (root / "data").iterdir()}, before)

    def setup_selector_case(self, folder):
        root = self.setup_case(folder)
        rows = [packet(ident)["claim"] for ident in ("a", "b", "c", "d", "e", "f")]
        rows[0]["assessment"].update(inclusion="forecast", verdict="暂无法判断")
        rows[1]["assessment"].update(inclusion="forecast", verdict="正确")
        rows[2]["assessment"].update(inclusion="nonforecast", verdict=None)
        rows[2]["extraction_v2"]["kind"] = "nonforecast"
        rows[3]["assessment"].update(inclusion="duplicate", verdict=None)
        rows[3]["extraction_v2"]["kind"] = "duplicate"
        rows[3]["duplicate_of"] = "a"
        rows[4].pop("assessment")
        rows[5].pop("assessment")
        rows[5]["extraction_v2"]["kind"] = "nonforecast"
        (root / "data/claims.jsonl").write_text("".join(json.dumps(row) + "\n" for row in rows))
        return root

    def test_unresolved_selector_freezes_only_current_unresolved_forecasts_without_apis(self):
        with tempfile.TemporaryDirectory() as folder:
            root = self.setup_selector_case(folder)
            output = Path(folder) / "unresolved-run"
            before = {p.relative_to(root): p.read_bytes() for p in root.rglob("*") if p.is_file()}
            with mock.patch.object(vp.rp.Runner, "call", side_effect=AssertionError("LLM called")), \
                    mock.patch.object(vp.ExaClient, "search", side_effect=AssertionError("Exa search called")), \
                    mock.patch.object(vp.ExaClient, "contents", side_effect=AssertionError("Exa read called")), \
                    contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(vp.main(["--case", str(root), "--unresolved", "--prepare-only",
                                          "--output-dir", str(output)]), 0)
            self.assertEqual(json.loads((output / "manifest.json").read_text())["ids"], ["a"])
            tasks = [json.loads(line) for line in (output / "tasks.jsonl").read_text().splitlines()]
            self.assertEqual([task["id"] for task in tasks], ["a"])
            self.assertEqual({p.relative_to(root): p.read_bytes() for p in root.rglob("*") if p.is_file()}, before)

    def test_all_forecasts_selector_excludes_duplicates_and_nonforecasts_without_apis(self):
        with tempfile.TemporaryDirectory() as folder:
            root = self.setup_selector_case(folder)
            output = Path(folder) / "all-forecasts-run"
            before = {p.relative_to(root): p.read_bytes() for p in root.rglob("*") if p.is_file()}
            with mock.patch.object(vp.rp.Runner, "call", side_effect=AssertionError("LLM called")), \
                    mock.patch.object(vp.ExaClient, "search", side_effect=AssertionError("Exa search called")), \
                    mock.patch.object(vp.ExaClient, "contents", side_effect=AssertionError("Exa read called")), \
                    contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(vp.main(["--case", str(root), "--all-forecasts", "--prepare-only",
                                          "--output-dir", str(output)]), 0)
            self.assertEqual(json.loads((output / "manifest.json").read_text())["ids"], ["a", "b", "e"])
            tasks = [json.loads(line) for line in (output / "tasks.jsonl").read_text().splitlines()]
            self.assertEqual([task["id"] for task in tasks], ["a", "b", "e"])
            self.assertEqual({p.relative_to(root): p.read_bytes() for p in root.rglob("*") if p.is_file()}, before)

    def test_nonfinite_budget_is_rejected_even_during_prepare(self):
        with tempfile.TemporaryDirectory() as folder:
            root = self.setup_case(folder)
            for flag in ("--budget-cny", "--exa-budget-usd"):
                for value in ("nan", "inf"):
                    with self.subTest(flag=flag, value=value), contextlib.redirect_stderr(io.StringIO()):
                        with self.assertRaises(SystemExit) as error:
                            vp.main(["--case", str(root), "--claim-id", "a", "--prepare-only",
                                     "--output-dir", str(Path(folder) / (flag + value)), flag, value])
                        self.assertEqual(error.exception.code, 2)

    def test_initial_judgment_scope_reaches_final_assessment_unchanged(self):
        llm = FakeLLM(second_round=True, second_scope="A different criterion chosen after reading results.")
        result = self.run_one(llm=llm)
        self.assertEqual(result["task_state"], "completed")
        final_packet = [data for _, stage, data in llm.calls if stage == "assess"][0]
        self.assertEqual(final_packet["research_scope"], "Example region after 1991.")
        self.assertEqual(result["scope"], "Example region after 1991.")

    def test_semantic_scope_rejection_is_repaired_then_accepted(self):
        llm = FakeLLM(
            review_script=["revise", "accept"],
            final_overrides={"scope": "Worldwide population instead of the original region."},
            revision_overrides={"scope": "Example region, 1991 to 2025."},
        )
        result = self.run_one(llm=llm)
        self.assertEqual(result["task_state"], "completed")
        self.assertEqual(result["assessment"]["scope"], "Example region, 1991 to 2025.")
        self.assertEqual(result["semantic_validation"], "accepted")
        self.assertEqual(result["revision_count"], 1)
        self.assertEqual(len(result["semantic_reviews"]), 2)
        self.assertTrue(result["autonomous_decision"])
        self.assertFalse(result["needs_review"])
        self.assertGreaterEqual(len(result["draft_history"]), 2)
        self.assertIn("Worldwide population", json.dumps(result["draft_history"]))
        repair_packet = [data for _, stage, data in llm.calls if stage == "revise_assessment"][0]
        self.assertEqual(repair_packet["proposed_assessment"]["scope"],
                         "Worldwide population instead of the original region.")
        self.assertIn("object_match", json.dumps(repair_packet))

    def test_persistent_semantic_rejection_returns_concrete_unknown_without_looping(self):
        llm = FakeLLM(review_script=["revise", "revise"], second_round=True)
        result = self.run_one(llm=llm)
        self.assertEqual(result["task_state"], "completed")
        self.assertEqual(result["assessment"]["verdict"], "暂无法判断")
        self.assertEqual(result["semantic_validation"], "unresolved")
        self.assertEqual(result["revision_count"], 1)
        self.assertEqual(len(result["semantic_reviews"]), 2)
        self.assertTrue(result["autonomous_decision"])
        self.assertFalse(result["needs_review"])
        self.assertIn("original region", result["remaining_gap"])
        stages = [stage for _, stage, _ in llm.calls]
        self.assertEqual(stages.count("revise_assessment"), 1)
        self.assertEqual(stages.count("semantic_review"), 2)
        self.assertLessEqual(len(llm.calls), 8)

    def test_unresolved_semantic_review_returns_unknown_without_repair(self):
        llm = FakeLLM(review_script=["unresolved"])
        result = self.run_one(llm=llm)
        self.assertEqual(result["task_state"], "completed")
        self.assertEqual(result["assessment"]["verdict"], "暂无法判断")
        self.assertEqual(result["semantic_validation"], "unresolved")
        self.assertEqual(result["revision_count"], 0)
        self.assertEqual(len(result["semantic_reviews"]), 1)
        self.assertTrue(result["autonomous_decision"])
        self.assertFalse(result["needs_review"])
        self.assertIn("original region", result["remaining_gap"])
        self.assertFalse(any(stage == "revise_assessment" for _, stage, _ in llm.calls))

    def test_fabricated_reviewer_quote_cannot_accept_a_judgment(self):
        checks = {name: "pass" for name in (
            "object_match", "condition_logic", "time_alignment", "evidence_support",
            "counterevidence", "verdict_logic",
        )}
        checks["object_match"] = "fail"
        review = {"decision": "revise", "checks": checks,
                  "issues": [{"check": "object_match", "reason": "Supposed source mismatch.",
                              "source_quote": "This sentence is not in the original book.",
                              "evidence_id": None}],
                  "remaining_gap": "The original scope remains uncertain."}
        result = self.run_one(llm=FakeLLM(review_script=[review]))
        self.assertNotEqual(result["task_state"], "completed")
        self.assertIsNone(result["assessment"])
        self.assertTrue(result["errors"])

    def test_reviewer_cannot_cite_evidence_from_another_task(self):
        checks = {name: "pass" for name in (
            "object_match", "condition_logic", "time_alignment", "evidence_support",
            "counterevidence", "verdict_logic",
        )}
        checks["evidence_support"] = "fail"
        review = {"decision": "revise", "checks": checks,
                  "issues": [{"check": "evidence_support", "reason": "Supposed source mismatch.",
                              "source_quote": BODY, "evidence_id": "another-task-source"}],
                  "remaining_gap": "The supporting source is unresolved."}
        result = self.run_one(llm=FakeLLM(review_script=[review]))
        self.assertNotEqual(result["task_state"], "completed")
        self.assertIsNone(result["assessment"])
        self.assertTrue(result["errors"])

    def test_round_and_model_call_limits_are_enforced(self):
        llm = FakeLLM(second_round=True)
        exa = FakeExa()
        result = self.run_one(llm=llm, exa=exa)
        self.assertEqual(result["task_state"], "completed")
        # The second round repeats the same queries, so those searches are not sent again.
        self.assertEqual(len(exa.search_calls), 2)
        self.assertEqual(sum(query["state"] == "skipped_duplicate" for query in result["queries"]), 2)
        self.assertLessEqual(len(llm.calls), vp.LLM_CALL_LIMIT)
        self.assertLessEqual(sum(len(urls) for urls in exa.content_calls), vp.SELECT_LIMIT * 2)

    def test_context_budget_prefers_statistical_pages_and_highlight_passages(self):
        long_text = ("intro " * 800) + "HIGHLIGHT_SENTENCE population was 1000." + ("tail " * 800)
        sources = [
            {"id": "news", "url": "https://news.example/story", "title": "A commentary",
             "text": "short news item", "highlights": []},
            {"id": "stat", "url": "https://www.census.gov/data/table", "title": "Census statistics",
             "text": long_text, "highlights": ["HIGHLIGHT_SENTENCE population was 1000."]},
        ]
        shown = {row["id"]: row for row in vp.bounded_evidence(sources, budget=2500)}
        self.assertIn("HIGHLIGHT_SENTENCE", shown["stat"]["text"])
        self.assertGreater(shown["stat"]["shown_bytes"], shown["news"]["shown_bytes"])
        self.assertEqual(shown["stat"]["context_focus"], "highlight_window")
        self.assertTrue(shown["stat"]["context_truncated"])
        self.assertFalse(shown["news"]["context_truncated"])

    def test_adaptive_plan_must_change_query_and_strategy(self):
        case = {"id": "a", "round": 3, "round_kind": "adaptive",
                "prior_query_norms": ["a support"], "prior_strategy_changes": ["old approach"]}
        repeated = {"id": "a", "scope": "Example region after 1991.", "strategy_change": "try a dataset",
                    "queries": [{"role": "support", "query": "A   support", "strategy": "rephrase"}]}
        with self.assertRaisesRegex(ValueError, "adaptive_query_repeats_previous"):
            vp.validate_stage("search_plan", [repeated], [case])
        same_strategy = dict(repeated, strategy_change="old approach", queries=[
            {"role": "support", "query": "a census", "strategy": "official statistics"}])
        with self.assertRaisesRegex(ValueError, "adaptive_strategy_not_changed"):
            vp.validate_stage("search_plan", [same_strategy], [case])
        fresh = dict(repeated, queries=[{"role": "counter", "query": "a census bulletin",
                                         "strategy": "official statistics, English"}])
        accepted = vp.validate_stage("search_plan", [fresh], [case])
        self.assertEqual(accepted[0]["queries"][0]["query"], "a census bulletin")

    def test_adaptive_search_changes_strategy_and_stops_when_a_verdict_is_reachable(self):
        class AdaptiveLLM(FakeLLM):
            def __init__(self):
                super().__init__()
                self.assessments = 0

            def call(self, stage, request, cases, batch_number):
                data = json.loads(request["messages"][-1]["content"])
                ident = cases[0]["id"]
                if stage == "search_plan" and data.get("round_kind") == "adaptive":
                    with self.lock:
                        self.calls.append((ident, stage, data))
                        self.requests.append((stage, copy.deepcopy(request)))
                        self.plan_counts[ident] = self.plan_counts.get(ident, 0) + 1
                        number = self.plan_counts[ident]
                    return [{"id": ident, "scope": "Example region after 1991.",
                             "strategy_change": "Round %s uses an official statistical table in another language." % number,
                             "queries": [
                                 {"role": "support", "query": "%s census table %s" % (ident, number),
                                  "strategy": "English official statistics for a later decade"},
                                 {"role": "counter", "query": "%s population bulletin %s" % (ident, number),
                                  "strategy": "statistical bulletin, different source type"},
                             ]}]
                if stage == "assess":
                    self.assessments += 1
                    item = super().call(stage, request, cases, batch_number)
                    if self.assessments == 1:
                        item[0].update(verdict="暂无法判断", basis="evidence", trend_aligned=False,
                                       observation_end=None, evidence_ids=[], evidence_notes=[],
                                       reason="The first pages do not contain the series.",
                                       remaining_gap="Need an official population count for the example region after 1991.")
                    return item
                return super().call(stage, request, cases, batch_number)

        llm, exa = AdaptiveLLM(), FakeExa()
        result = self.run_one(llm=llm, exa=exa)
        self.assertEqual(result["task_state"], "completed", result["errors"])
        self.assertEqual(result["assessment"]["verdict"], "正确")
        adaptive = [entry for entry in result["round_history"] if entry["kind"] == "adaptive"]
        self.assertEqual(len(adaptive), 1)
        self.assertIn("official statistical", adaptive[0]["strategy_change"])
        self.assertIn("official population count", adaptive[0]["gap_before"])
        self.assertEqual(adaptive[0]["verdict_after"], "正确")
        self.assertTrue(all(query["state"] == "completed" for query in adaptive[0]["queries"]))
        self.assertEqual(result["adaptive_rounds"], 1)
        self.assertTrue(all(count == 10 for _, _, count in exa.search_calls))
        self.assertLessEqual(len(llm.calls), vp.LLM_CALL_LIMIT)
        self.assertLess(len(adaptive), vp.ADAPTIVE_ROUNDS)

    def test_unresolved_adaptive_search_stops_after_three_rounds_and_dedupes_urls(self):
        class StuckLLM(FakeLLM):
            def call(self, stage, request, cases, batch_number):
                data = json.loads(request["messages"][-1]["content"])
                ident = cases[0]["id"]
                if stage == "search_plan" and data.get("round_kind") == "adaptive":
                    with self.lock:
                        self.calls.append((ident, stage, data))
                        self.requests.append((stage, copy.deepcopy(request)))
                        self.plan_counts[ident] = self.plan_counts.get(ident, 0) + 1
                        number = self.plan_counts[ident]
                    return [{"id": ident, "scope": "Example region after 1991.",
                             "strategy_change": "Adaptive strategy %s switches language and source type." % number,
                             "queries": [
                                 {"role": "support", "query": "%s census table %s" % (ident, number),
                                  "strategy": "official statistics"},
                                 {"role": "counter", "query": "%s gazetteer count %s" % (ident, number),
                                  "strategy": "different dataset"},
                             ]}]
                if stage == "assess":
                    item = super().call(stage, request, cases, batch_number)
                    item[0].update(verdict="暂无法判断", basis="evidence", trend_aligned=False,
                                   observation_end=None,
                                   reason="The official count is still absent.",
                                   remaining_gap="The example region official population count after 1991 is still absent.")
                    return item
                return super().call(stage, request, cases, batch_number)

        llm, exa = StuckLLM(), FakeExa()
        result = self.run_one(llm=llm, exa=exa)
        self.assertEqual(result["task_state"], "completed", result["errors"])
        self.assertEqual(result["assessment"]["verdict"], "暂无法判断")
        adaptive = [entry for entry in result["round_history"] if entry["kind"] == "adaptive"]
        self.assertEqual(len(adaptive), 3)
        self.assertEqual(result["adaptive_rounds"], 3)
        self.assertTrue(adaptive[-1]["gap_after"])
        self.assertTrue(adaptive[1]["skipped_duplicate_urls"])
        self.assertEqual(adaptive[1]["new_urls"], [])
        self.assertEqual(len(exa.content_calls), 2)
        self.assertEqual(len({url for urls in exa.content_calls for url in urls}),
                         len([url for urls in exa.content_calls for url in urls]))


if __name__ == "__main__":
    unittest.main()
