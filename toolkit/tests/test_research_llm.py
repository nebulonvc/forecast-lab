"""Regression tests for the shared LLM transport used by search workers."""
import concurrent.futures
import contextlib
import hashlib
import http.client
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


class Response:
    def __init__(self, value):
        self.value = value if isinstance(value, bytes) else json.dumps(value).encode()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def read(self, size=-1):
        return self.value[:size] if size >= 0 else self.value


def task(ident='a'):
    return rp.payload('assess', {'id': ident}, 100), [{'id': ident}]


def response(usage=None):
    return {'items': [{'answer': 'proposal'}], 'usage': usage if usage is not None else
            {'prompt_tokens': 10, 'completion_tokens': 10, 'total_tokens': 20}}


def runner(folder, opener, budget=1):
    return rp.Runner(folder, 'secret-key', budget=budget, opener=opener,
                     validator=lambda stage, raw, cases: raw['items'])


def rejection(status, body=b'{"error":"secret-key must not appear"}'):
    return urllib.error.HTTPError('https://api.deepseek.com', status, 'SECRET ERROR DETAIL', {}, io.BytesIO(body))


class ResearchLLMTests(unittest.TestCase):
    def test_rejected_requests_keep_unknown_reservation_and_auth_payment_stop(self):
        for status in (400, 401, 402, 403):
            with self.subTest(status=status), tempfile.TemporaryDirectory() as folder, contextlib.redirect_stdout(io.StringIO()):
                calls = []

                def opener(*args, **kwargs):
                    calls.append(1)
                    raise rejection(status)

                client = runner(folder, opener)
                with self.assertRaisesRegex(ValueError, 'http_' + str(status)):
                    client.call('research', *task(), 1)
                reserve = rp.reserve_cost(task()[0])
                self.assertAlmostEqual(client.totals()['unknown_or_inflight_reserved_CNY'], reserve, places=7)
                self.assertAlmostEqual(client.totals()['budget_committed_CNY'], reserve, places=7)
                self.assertEqual(client.totals()['usage_unknown_requests'], 1)
                self.assertEqual(len(list(Path(folder).glob('*.response.bin'))), 1)
                for path in Path(folder).iterdir():
                    self.assertNotIn(b'secret-key', path.read_bytes())
                resumed = runner(folder, opener)
                if status in (401, 402, 403):
                    with self.assertRaisesRegex(ValueError, 'rejected_http_'):
                        resumed.call('research', *task('b'), 2)
                else:
                    with self.assertRaisesRegex(ValueError, 'previously_attempted'):
                        resumed.call('research', *task(), 1)
                self.assertEqual(len(calls), 1)

    def test_malformed_and_transport_partial_bytes_are_saved_before_parsing(self):
        class Partial(Response):
            def read(self, size=-1):
                raise http.client.IncompleteRead(b'{"secret-key":', 100)

        for obj in (Response(b'{"secret-key":'), Partial(b'')):
            with self.subTest(obj=obj), tempfile.TemporaryDirectory() as folder, contextlib.redirect_stdout(io.StringIO()):
                calls = []

                def opener(*args, **kwargs):
                    calls.append(1)
                    return obj

                client = runner(folder, opener)
                with self.assertRaises(ValueError):
                    client.call('research', *task(), 1)
                path = next(Path(folder).glob('*.response.bin'))
                self.assertEqual(path.read_bytes(), b'{"[REDACTED_API_KEY]":')
                record = next(iter(client.ledger['calls'].values()))
                self.assertEqual(record['response_sha256'], hashlib.sha256(path.read_bytes()).hexdigest())
                self.assertEqual(record['state'], 'unknown')
                self.assertEqual(record['response_truncated'], isinstance(obj, Partial))
                with self.assertRaisesRegex(ValueError, 'previously_attempted'):
                    runner(folder, opener).call('research', *task(), 1)
                self.assertEqual(len(calls), 1)

    def test_invalid_usage_never_reduces_committed_budget_or_adds_fake_tokens(self):
        invalid = [None, {}, {'prompt_tokens': -1, 'completion_tokens': 2},
                   {'prompt_tokens': True, 'completion_tokens': 2},
                   {'prompt_tokens': 10, 'completion_tokens': 2, 'total_tokens': 999},
                   {'prompt_tokens': 10, 'completion_tokens': 2, 'prompt_cache_hit_tokens': 11},
                   {'prompt_tokens': 10, 'completion_tokens': 2, 'prompt_cache_miss_tokens': -1},
                   {'prompt_tokens': 10 ** 1000, 'completion_tokens': 2}]
        for usage in invalid:
            with self.subTest(usage=usage), tempfile.TemporaryDirectory() as folder, contextlib.redirect_stdout(io.StringIO()):
                client = runner(folder, lambda *a, **kw: Response({'items': [], 'usage': usage}))
                client.call('research', *task(), 1)
                reserve = rp.reserve_cost(task()[0])
                self.assertAlmostEqual(client.totals()['estimated_cost_CNY'], reserve, places=7)
                self.assertAlmostEqual(client.totals()['budget_committed_CNY'], reserve, places=7)
                self.assertEqual(client.totals()['total_tokens'], 0)
                self.assertEqual(client.totals()['usage_unknown_requests'], 1)
                self.assertFalse(next(iter(client.ledger['calls'].values()))['usage_valid'])

    def test_budget_waiter_wakes_on_timeout_or_rejection_and_does_not_call(self):
        for status in (None, 400, 402):
            with self.subTest(status=status), tempfile.TemporaryDirectory() as folder, contextlib.redirect_stdout(io.StringIO()):
                entered, release = threading.Event(), threading.Event()
                calls = []

                def opener(*args, **kwargs):
                    calls.append(1)
                    entered.set()
                    release.wait(2)
                    if status is None:
                        raise TimeoutError('DETAIL')
                    raise rejection(status)

                client = runner(folder, opener, budget=rp.reserve_cost(task()[0]) * 1.5)
                with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
                    first = pool.submit(client.call, 'research', *task(), 1)
                    self.assertTrue(entered.wait(1))
                    second = pool.submit(client.call, 'research', *task('b'), 2)
                    time.sleep(0.02)
                    self.assertFalse(second.done())
                    release.set()
                    with self.assertRaises(ValueError):
                        first.result(timeout=2)
                    with self.assertRaisesRegex(ValueError, 'budget_reservation_exceeded|payment_rejected'):
                        second.result(timeout=2)
                self.assertEqual(len(calls), 1)
                self.assertEqual(client.active, 0)

    def test_budget_waiter_proceeds_when_valid_usage_releases_reservation(self):
        entered, release = threading.Event(), threading.Event()

        def opener(request, timeout):
            if '"a"' in json.loads(request.data)['messages'][1]['content']:
                entered.set()
                release.wait(2)
            return Response(response())

        with tempfile.TemporaryDirectory() as folder, contextlib.redirect_stdout(io.StringIO()):
            budget = rp.reserve_cost(task()[0]) * 1.5
            client = runner(folder, opener, budget=budget)
            with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
                first = pool.submit(client.call, 'research', *task(), 1)
                self.assertTrue(entered.wait(1))
                second = pool.submit(client.call, 'research', *task('b'), 2)
                time.sleep(0.02)
                self.assertFalse(second.done())
                release.set()
                first.result(timeout=2)
                second.result(timeout=2)
            self.assertEqual(client.peak, 1)
            self.assertEqual(len(client.ledger['calls']), 2)
            self.assertLessEqual(client.totals()['budget_committed_CNY'], budget)

    def test_nonfinite_or_invalid_budget_and_timeout_rejected(self):
        for value in (float('nan'), float('inf'), float('-inf'), 0, -1, True, '1', None):
            with self.subTest(value=value), tempfile.TemporaryDirectory() as folder:
                with self.assertRaises(ValueError):
                    rp.Runner(folder, 'key', budget=value)
                with self.assertRaises(ValueError):
                    rp.Runner(folder, 'key', timeout=value)

    def test_pre_dispatch_ledger_failure_does_not_leave_an_active_request(self):
        with tempfile.TemporaryDirectory() as folder:
            client = runner(folder, lambda *a, **kw: self.fail('network after ledger failure'))
            def broken_persist():
                raise OSError('storage unavailable')
            client.persist = broken_persist
            with self.assertRaises(OSError):
                client.call('research', *task(), 1)
            self.assertEqual(client.active, 0)
            self.assertEqual(client.totals()['budget_committed_CNY'], 0)
            with self.assertRaisesRegex(ValueError, 'ledger_write_failed_before_dispatch'):
                client.call('research', *task('b'), 2)

    def test_cached_raw_json_and_original_bytes_must_both_match_receipt(self):
        for changed_file in ('response.json', 'response.bin'):
            with self.subTest(changed_file=changed_file), tempfile.TemporaryDirectory() as folder, contextlib.redirect_stdout(io.StringIO()):
                client = runner(folder, lambda *a, **kw: Response(response()))
                client.call('research', *task(), 1)
                path = next(Path(folder).glob('*.' + changed_file))
                changed = response()
                changed['items'][0]['answer'] = 'tampered conclusion'
                path.write_bytes(json.dumps(changed).encode())
                resumed = runner(folder, lambda *a, **kw: self.fail('corrupted cache triggered network'))
                with self.assertRaisesRegex(ValueError, 'cached_response_integrity_failed'):
                    resumed.call('research', *task(), 1)
                self.assertEqual(next(iter(resumed.ledger['calls'].values()))['cache_integrity'], 'failed')

    def test_legacy_cache_without_receipt_is_flagged_and_refused(self):
        with tempfile.TemporaryDirectory() as folder, contextlib.redirect_stdout(io.StringIO()):
            request, cases = task()
            digest = hashlib.sha256(rp.canonical(request)).hexdigest()
            rp.save_json(Path(folder, digest + '.response.json'), response())
            client = runner(folder, lambda *a, **kw: self.fail('legacy cache triggered network'))
            with self.assertRaisesRegex(ValueError, 'missing_integrity_receipt'):
                client.call('research', request, cases, 1)
            self.assertEqual(client.ledger['calls'][digest]['cache_integrity'], 'legacy_unverified')
            self.assertEqual(client.totals()['cache_hits_this_run'], 0)

    def test_normalized_cache_reformatting_is_allowed_and_marked_verified(self):
        with tempfile.TemporaryDirectory() as folder, contextlib.redirect_stdout(io.StringIO()):
            client = runner(folder, lambda *a, **kw: Response(response()))
            expected = client.call('research', *task(), 1)
            path = next(Path(folder).glob('*.response.json'))
            path.write_text(json.dumps(json.loads(path.read_text()), separators=(',', ':'), sort_keys=True))
            resumed = runner(folder, lambda *a, **kw: self.fail('valid cache triggered network'))
            self.assertEqual(resumed.call('research', *task(), 1), expected)
            self.assertEqual(next(iter(resumed.ledger['calls'].values()))['cache_integrity'],
                             'verified_archive_hash_and_normalized_json')


if __name__ == '__main__':
    unittest.main()
