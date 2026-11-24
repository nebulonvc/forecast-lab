import concurrent.futures
import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
import threading
import time
import unittest
import urllib.error

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import run_parallel as rp


def extract_item(claim_id):
    return dict(id=claim_id, kind='prediction', claim='未来趋势', time_text='', condition_text='',
                method='趋势外推', method_basis='inferred', reason='原文包含未来判断')


def response_for(request):
    body = json.loads(request.data)
    data = json.loads(body['messages'][1]['content'])
    items = [extract_item(c['id']) for c in data['cases']]
    return {'choices': [{'finish_reason': 'stop', 'message': {'content': json.dumps({'items': items})}}],
            'usage': {'prompt_tokens': 100, 'completion_tokens': 100, 'total_tokens': 200}}


class Response:
    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def read(self, size=-1):
        data = json.dumps(self.obj).encode()
        return data[:size] if size >= 0 else data


def task(claim_id):
    cases = [{'id': claim_id, 'quote': '预测原文'}]
    return rp.payload('extract', {'cases': cases}, 8000), cases


class ParallelRunnerTests(unittest.TestCase):
    def test_review_envelope_can_exceed_old_limit_without_changing_default(self):
        request, cases = task('large-review')
        request['messages'][0]['content'] += 'x' * 50_000
        with tempfile.TemporaryDirectory() as folder, contextlib.redirect_stdout(io.StringIO()):
            default = rp.Runner(Path(folder) / 'default', 'test-secret',
                                opener=lambda *a, **kw: self.fail('oversized default request sent'))
            with self.assertRaisesRegex(ValueError, 'exceeds_48000'):
                default.call('extract', request, cases, 1)
            expanded = rp.Runner(Path(folder) / 'research', 'test-secret', max_request_bytes=96_000,
                                 opener=lambda request, timeout: Response(response_for(request)))
            self.assertEqual(expanded.call('extract', request, cases, 1)[0]['id'], 'large-review')
            self.assertGreater(expanded.totals()['estimated_cost_CNY'], 0)
            request['messages'][0]['content'] += 'x' * 50_000
            with self.assertRaisesRegex(ValueError, 'exceeds_96000'):
                expanded.call('extract', request, cases, 2)

    def test_actual_concurrency_and_cache_reuse(self):
        seen = []
        lock = threading.Lock()
        barrier = threading.Barrier(4)

        def opener(request, timeout):
            with lock:
                seen.append(request)
            barrier.wait(timeout=2)
            return Response(response_for(request))

        with tempfile.TemporaryDirectory() as folder, contextlib.redirect_stdout(io.StringIO()):
            runner = rp.Runner(folder, 'test-secret', opener=opener)
            with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
                fs = [pool.submit(runner.call, 'extract', *task(str(i)), i) for i in range(4)]
                results = [f.result() for f in fs]
            self.assertEqual(runner.peak, 4)
            self.assertEqual(len(results), 4)
            second = rp.Runner(folder, 'test-secret', opener=lambda *a, **kw: self.fail('cache made a network request'))
            self.assertEqual(second.call('extract', *task('0'), 0)[0]['id'], '0')
            self.assertEqual(second.cached, 1)
            self.assertEqual(len(seen), 4)
            persisted = '\n'.join(p.read_text() for p in Path(folder).glob('*.json'))
            self.assertNotIn('test-secret', persisted)
            self.assertNotIn('Authorization', persisted)

    def test_timeout_reserves_cost_and_never_silently_retries(self):
        calls = []

        def opener(*args, **kwargs):
            calls.append(1)
            raise TimeoutError('contains-sensitive-provider-details')

        with tempfile.TemporaryDirectory() as folder, contextlib.redirect_stdout(io.StringIO()) as output:
            runner = rp.Runner(folder, 'test-secret', opener=opener)
            with self.assertRaisesRegex(ValueError, 'request_failed_TimeoutError'):
                runner.call('extract', *task('a'), 1)
            self.assertGreater(runner.totals()['unknown_or_inflight_reserved_CNY'], 0)
            resumed = rp.Runner(folder, 'test-secret', opener=opener)
            with self.assertRaisesRegex(ValueError, 'previously_attempted'):
                resumed.call('extract', *task('a'), 1)
            self.assertEqual(len(calls), 1)
            self.assertNotIn('sensitive-provider', output.getvalue())

    def test_budget_reservation_waits_for_inflight_and_remains_atomic(self):
        entered = threading.Event()
        second_entered = threading.Event()
        release = threading.Event()
        calls = []

        def opener(request, timeout):
            calls.append(request)
            if len(calls) == 1:
                entered.set()
                release.wait(2)
            else:
                second_entered.set()
            return Response(response_for(request))

        request_a, cases_a = task('a')
        budget = rp.reserve_cost(request_a) * 1.5
        with tempfile.TemporaryDirectory() as folder, contextlib.redirect_stdout(io.StringIO()):
            runner = rp.Runner(folder, 'test-secret', budget=budget, opener=opener)
            with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
                first = pool.submit(runner.call, 'extract', request_a, cases_a, 1)
                self.assertTrue(entered.wait(2))
                second = pool.submit(runner.call, 'extract', *task('b'), 2)
                try:
                    self.assertFalse(second_entered.wait(0.05))
                    self.assertEqual(runner.active, 1)
                finally:
                    release.set()
                first.result(timeout=2)
                second.result(timeout=2)
            self.assertTrue(second_entered.is_set())
            self.assertEqual(runner.peak, 1)
            self.assertEqual(len(runner.ledger['calls']), 2)
            self.assertLessEqual(runner.totals()['budget_committed_CNY'], budget)

    def test_budget_waiter_wakes_after_unknown_and_rejects_without_deadlock(self):
        entered = threading.Event()
        release = threading.Event()

        def opener(request, timeout):
            entered.set()
            release.wait(2)
            raise TimeoutError()

        with tempfile.TemporaryDirectory() as folder, contextlib.redirect_stdout(io.StringIO()):
            runner = rp.Runner(folder, 'test-secret', budget=rp.reserve_cost(task('a')[0]) * 1.5, opener=opener)
            with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
                first = pool.submit(runner.call, 'extract', *task('a'), 1)
                self.assertTrue(entered.wait(2))
                second = pool.submit(runner.call, 'extract', *task('b'), 2)
                release.set()
                with self.assertRaisesRegex(ValueError, 'TimeoutError'):
                    first.result(timeout=2)
                with self.assertRaisesRegex(ValueError, 'budget_reservation_exceeded'):
                    second.result(timeout=2)
            self.assertEqual(len(runner.ledger['calls']), 1)
            self.assertGreater(runner.totals()['unknown_or_inflight_reserved_CNY'], 0)

    def test_budget_waiter_wakes_on_auth_failure(self):
        entered = threading.Event()
        release = threading.Event()

        def opener(request, timeout):
            entered.set()
            release.wait(2)
            raise urllib.error.HTTPError(rp.ENDPOINT, 401, 'unauthorized', {}, None)

        with tempfile.TemporaryDirectory() as folder, contextlib.redirect_stdout(io.StringIO()):
            runner = rp.Runner(folder, 'test-secret', budget=rp.reserve_cost(task('a')[0]) * 1.5, opener=opener)
            with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
                first = pool.submit(runner.call, 'extract', *task('a'), 1)
                self.assertTrue(entered.wait(2))
                second = pool.submit(runner.call, 'extract', *task('b'), 2)
                release.set()
                with self.assertRaisesRegex(ValueError, 'http_401'):
                    first.result(timeout=2)
                with self.assertRaisesRegex(ValueError, 'authentication_rejected'):
                    second.result(timeout=2)
            self.assertEqual(len(runner.ledger['calls']), 1)

    def test_invalid_response_retained_without_repeat_billing(self):
        calls = []

        def opener(request, timeout):
            calls.append(1)
            obj = response_for(request)
            obj['choices'][0]['message']['content'] = json.dumps({'items': [extract_item('wrong')]})
            return Response(obj)

        with tempfile.TemporaryDirectory() as folder, contextlib.redirect_stdout(io.StringIO()):
            runner = rp.Runner(folder, 'test-secret', opener=opener)
            with self.assertRaisesRegex(ValueError, 'cached_response_invalid'):
                runner.call('extract', *task('a'), 1)
            with self.assertRaisesRegex(ValueError, 'coverage_mismatch'):
                runner.call('extract', *task('a'), 1)
            self.assertEqual(len(calls), 1)
            self.assertEqual(len(list(Path(folder).glob('*.response.json'))), 1)
            self.assertGreater(runner.totals()['estimated_cost_CNY'], 0)

    def test_extract_is_evidence_blind_and_assess_links_are_scoped(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'data').mkdir()
            (root / 'output').mkdir()
            rp.save_json(root / 'config.json', {'book': 'test', 'cutoff': '2026-11-08'})
            rp.save_jsonl(root / 'data/claims.jsonl', [dict(id='a', page=1, quote='预测', context='语境', speaker='作者',
                legacy={'units': [{'evidence_ids': ['e1']}]}, source_verified=True, review={'outcome': 'SECRET_OUTCOME'})])
            rp.save_jsonl(root / 'data/evidence.jsonl', [dict(id='e1', verified=True, excerpt='结果事实', archive='/private/file',
                url='https://example.org'), dict(id='e2', verified=True, excerpt='别的事实')])
            _, batches = rp.prepare_batches(root)
            _, extract, assess = batches[0]
            self.assertNotIn('SECRET_OUTCOME', json.dumps(extract))
            self.assertNotIn('结果事实', json.dumps(extract, ensure_ascii=False))
            self.assertEqual(assess['cases'][0]['allowed_evidence_ids'], ['e1'])
            self.assertEqual([e['id'] for e in assess['evidence']], ['e1'])
            self.assertNotIn('/private/file', json.dumps(assess))

    def reuse_fixture(self, root):
        import prepare_book as pb
        (root / 'data').mkdir()
        (root / 'output').mkdir()
        config = {'book': 'test', 'cutoff': '2026-11-08', 'rules_version': 'test-v1'}
        claim = dict(id='a', page=None, quote='未来趋势', context='未来趋势的语境', speaker='作者',
                     source_verified=True, source_location={'type': 'txt', 'source_sha256': 'a' * 64},
                     source_verification={'method': 'txt_exact_match', 'sha256': 'a' * 64}, legacy={'units': []})
        claim['extraction_v2'] = dict(extract_item('a'), expanded_claim='未来趋势',
                                      reference_resolutions=[], unresolved_references=[])
        claim['extraction_v2']['provenance'] = pb.extraction_provenance(claim, config, 'a' * 64)
        rp.save_json(root / 'config.json', config)
        rp.save_jsonl(root / 'data/claims.jsonl', [claim])
        rp.save_jsonl(root / 'data/evidence.jsonl', [dict(id='e1', verified=True), dict(id='e2', verified=True)])
        rp.save_json(root / 'output/evidence_links.json', {'a': ['e1']})
        return claim, config

    def test_assess_only_reuses_extraction_and_keeps_evidence_scope(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            self.reuse_fixture(root)
            _, batches = rp.prepare_batches(root, assess_only=True)
            calls = []

            class StubRunner:
                def call(self, stage, request, cases, number):
                    calls.append((stage, request, cases))
                    return [{'id': 'a', 'evidence_ids': ['e1']}]

            extracted, assessed = rp.run_batch(StubRunner(), batches[0], 8000, assess_only=True)
            self.assertEqual([stage for stage, _, _ in calls], ['assess'])
            self.assertEqual(extracted[0]['claim'], '未来趋势')
            self.assertEqual(assessed[0]['id'], 'a')
            packet = json.loads(calls[0][1]['messages'][1]['content'])
            self.assertEqual(packet['cases'][0]['allowed_evidence_ids'], ['e1'])
            self.assertEqual([e['id'] for e in packet['evidence']], ['e1'])
            self.assertEqual(packet['cases'][0]['extraction']['id'], 'a')

    def test_assess_only_rejects_stale_inputs_and_incomplete_extraction(self):
        import copy
        import prepare_book as pb
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            original, config = self.reuse_fixture(root)
            for field, value in [('quote', '另一段原文'), ('context', '修改语境'), ('speaker', '另一人')]:
                claim = copy.deepcopy(original)
                claim[field] = value
                rp.save_jsonl(root / 'data/claims.jsonl', [claim])
                with self.assertRaises(ValueError):
                    rp.prepare_batches(root, assess_only=True)
            rp.save_jsonl(root / 'data/claims.jsonl', [original])
            rp.save_json(root / 'config.json', dict(config, rules_version='test-v2'))
            with self.assertRaises(ValueError):
                rp.prepare_batches(root, assess_only=True)
            rp.save_json(root / 'config.json', config)
            claim = copy.deepcopy(original)
            del claim['extraction_v2']['condition_text']
            claim['extraction_v2']['provenance'] = pb.extraction_provenance(claim, config, 'a' * 64)
            rp.save_jsonl(root / 'data/claims.jsonl', [claim])
            with self.assertRaises(ValueError):
                rp.prepare_batches(root, assess_only=True)

    def test_assess_only_cache_identity_changes_with_extraction(self):
        import prepare_book as pb
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            claim, config = self.reuse_fixture(root)
            _, before = rp.prepare_batches(root, assess_only=True)
            first = rp.canonical(rp.payload('assess', before[0][2], 8000))
            claim['extraction_v2']['claim'] = '修订后的趋势'
            claim['extraction_v2']['provenance'] = pb.extraction_provenance(claim, config, 'a' * 64)
            rp.save_jsonl(root / 'data/claims.jsonl', [claim])
            _, after = rp.prepare_batches(root, assess_only=True)
            second = rp.canonical(rp.payload('assess', after[0][2], 8000))
            self.assertNotEqual(rp.hashlib.sha256(first).hexdigest(), rp.hashlib.sha256(second).hexdigest())

    def test_shared_contexts_preserve_each_source_and_evidence_scope_with_smaller_packets(self):
        import copy
        import prepare_book as pb
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            original, config = self.reuse_fixture(root)
            claims = []
            links = {}
            for n in range(6):
                c = copy.deepcopy(original)
                c['id'] = c['extraction_v2']['id'] = str(n)
                c['context'] = ('A' if n < 4 else 'B') * 9000
                c['extraction_v2']['provenance'] = pb.extraction_provenance(c, config, 'a' * 64)
                claims.append(c)
                links[c['id']] = ['e1' if n < 4 else 'e2']
            rp.save_jsonl(root / 'data/claims.jsonl', claims)
            rp.save_json(root / 'output/evidence_links.json', links)
            _, old = rp.prepare_batches(root, assess_only=True)
            _, shared = rp.prepare_batches(root, assess_only=True, share_contexts=True)
            self.assertLess(len(shared), len(old))
            before = sum(len(rp.canonical(rp.payload('assess', a, 8000))) for _, _, a in old)
            after = sum(len(rp.canonical(rp.payload('assess', a, 8000))) for _, _, a in shared)
            self.assertLess(after, before)
            by_id = {c['id']: c for c in claims}
            seen = []
            for _, _, packet in shared:
                for c in packet['cases']:
                    recovered = packet['contexts'][c['context_ref']] if 'context_ref' in c else c['context']
                    self.assertEqual(recovered, by_id[c['id']]['context'])
                    self.assertEqual(c['quote'], by_id[c['id']]['quote'])
                    self.assertEqual(c['allowed_evidence_ids'], links[c['id']])
                    seen.append(c['id'])
                self.assertLessEqual(len(rp.canonical(rp.payload('assess', packet, 8000))), rp.PREPARED_REQUEST_BYTES)
            self.assertEqual(sorted(seen), sorted(by_id))
            self.assertTrue(all('context_ref' not in c and 'context' in c for _, _, p in old for c in p['cases']))

    def test_oversized_request_rejected_before_network_and_billing(self):
        request, cases = task('a')
        request['messages'][1]['content'] += 'x' * 48000
        with tempfile.TemporaryDirectory() as folder:
            runner = rp.Runner(folder, 'test-secret', opener=lambda *a, **kw: self.fail('network called'))
            with self.assertRaisesRegex(ValueError, '48000_bytes'):
                runner.call('extract', request, cases, 1)
            self.assertEqual(len(runner.ledger['calls']), 0)

    def test_missing_usage_keeps_conservative_charge(self):
        def opener(request, timeout):
            obj = response_for(request)
            del obj['usage']
            return Response(obj)

        with tempfile.TemporaryDirectory() as folder, contextlib.redirect_stdout(io.StringIO()):
            runner = rp.Runner(folder, 'test-secret', opener=opener)
            request, cases = task('a')
            runner.call('extract', request, cases, 1)
            self.assertAlmostEqual(runner.totals()['estimated_cost_CNY'], rp.reserve_cost(request), places=7)

    def test_peak_and_off_peak_costs(self):
        usage = {'prompt_tokens': 1500, 'prompt_cache_hit_tokens': 500,
                 'prompt_cache_miss_tokens': 1000, 'completion_tokens': 2000}
        self.assertAlmostEqual(rp.usage_cost(usage), 0.01802)
        self.assertAlmostEqual(rp.usage_cost(usage, rp.OFF_PEAK_PRICES), 0.00901)

    def test_authentication_failure_stops_queued_requests(self):
        calls = []

        def opener(request, timeout):
            calls.append(1)
            raise urllib.error.HTTPError(rp.ENDPOINT, 401, 'unauthorized', {}, None)

        with tempfile.TemporaryDirectory() as folder, contextlib.redirect_stdout(io.StringIO()):
            runner = rp.Runner(folder, 'test-secret', opener=opener)
            with self.assertRaisesRegex(ValueError, 'request_failed_http_401'):
                runner.call('extract', *task('a'), 1)
            with self.assertRaisesRegex(ValueError, 'authentication_rejected'):
                runner.call('extract', *task('b'), 2)
            self.assertEqual(len(calls), 1)

    def test_response_credential_echo_redacted_and_request_hash_matches(self):
        secret = 'test-secret'

        def opener(request, timeout):
            obj = response_for(request)
            obj['unexpected_metadata'] = [secret, {'echo': 'prefix ' + secret}]
            return Response(obj)

        with tempfile.TemporaryDirectory() as folder, contextlib.redirect_stdout(io.StringIO()):
            runner = rp.Runner(folder, secret, opener=opener)
            runner.call('extract', *task('a'), 1)
            files = list(Path(folder).glob('*.json'))
            self.assertTrue(files)
            for file in files:
                self.assertNotIn(secret, file.read_text())
            request_file = next(Path(folder).glob('*.request.json'))
            self.assertEqual(rp.hashlib.sha256(request_file.read_bytes()).hexdigest(), request_file.name.split('.')[0])

    def test_preflight_splits_large_batches_deterministically(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'data').mkdir()
            (root / 'output').mkdir()
            rp.save_json(root / 'config.json', {'book': 'test', 'cutoff': '2026-11-08'})
            claims = [dict(id=str(i), page=i, quote='预测', context='语境', speaker='作者',
                legacy={'units': [{'evidence_ids': ['e' + str(i)]}]}, source_verified=True) for i in range(4)]
            evidence = [dict(id='e' + str(i), verified=True, excerpt='x' * 10000) for i in range(4)]
            rp.save_jsonl(root / 'data/claims.jsonl', claims)
            rp.save_jsonl(root / 'data/evidence.jsonl', evidence)
            _, batches = rp.prepare_batches(root, batch_size=4)
            _, again = rp.prepare_batches(root, batch_size=4)
            self.assertEqual(batches, again)
            self.assertGreater(len(batches), 1)
            self.assertEqual([c['id'] for _, source, _ in batches for c in source['cases']], ['0', '1', '2', '3'])
            self.assertTrue(all(len(rp.canonical(rp.payload('assess', a, 8000))) <= 35000 for _, _, a in batches))
            evidence[0]['excerpt'] = 'x' * 50000
            rp.save_jsonl(root / 'data/evidence.jsonl', evidence)
            with self.assertRaisesRegex(ValueError, 'single_case_exceeds'):
                rp.prepare_batches(root, batch_size=4)

    def test_conditional_score_requires_satisfied_condition_and_future_is_unresolved(self):
        item = dict(id='a', inclusion='forecast', verdict='正确', basis='conditional', scope='条件已发生，观察2025年',
                    reason='证据符合', limitation='回顾性判断', evidence_ids=['e'], method='条件推理',
                    method_basis='inferred', observation_end='2025-12-31', future_time_text='', condition_state='satisfied')
        cases = [dict(id='a', allowed_evidence_ids=['e'], source_verified=True)]

        def wrap(i):
            return {'choices': [{'finish_reason': 'stop', 'message': {'content': json.dumps({'items': [i]})}}]}

        self.assertEqual(rp.validate_items('assess', wrap(item), cases), [item])
        item['condition_state'] = 'unknown'
        with self.assertRaises(ValueError):
            rp.validate_items('assess', wrap(item), cases)
        item['verdict'] = '部分符合'
        self.assertEqual(rp.validate_items('assess', wrap(item), cases)[0]['verdict'], '部分符合')
        item['verdict'] = '正确'
        item.update(basis='future', condition_state='unconditional', future_time_text='2030')
        with self.assertRaises(ValueError):
            rp.validate_items('assess', wrap(item), cases)
        item['verdict'] = '暂无法判断'
        self.assertEqual(rp.validate_items('assess', wrap(item), cases), [item])


if __name__ == '__main__':
    unittest.main()
