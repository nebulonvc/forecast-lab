import concurrent.futures
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
from exa_client import ExaClient


class Response:
    def __init__(self, value):
        self.value = value if isinstance(value, bytes) else json.dumps(value).encode()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def read(self, size=-1):
        return self.value[:size] if size >= 0 else self.value


def success(cost=0.001):
    return {'requestId': 'request-1', 'results': [], 'costDollars': {'total': cost}}


def http_error(code, retry_after=None, body=b'{}'):
    headers = {'Retry-After': retry_after} if retry_after is not None else {}
    return urllib.error.HTTPError('https://api.exa.ai/search', code, 'details must not leak', headers, io.BytesIO(body))


class ExaClientTests(unittest.TestCase):
    def test_search_request_cutoff_cost_and_redacted_archive(self):
        seen = []

        def opener(request, timeout):
            seen.append(request)
            return Response({**success(0.007), 'results': [{'title': 'test-secret', 'url': 'https://example.org'}]})

        with tempfile.TemporaryDirectory() as folder:
            client = ExaClient(folder, 'test-secret', opener=opener)
            result = client.search('counter evidence', '2026-11-09')
            body = json.loads(seen[0].data)
            self.assertEqual(body['endPublishedDate'], '2026-11-10T00:00:00Z')
            self.assertEqual(body['contents'], {'highlights': True})
            self.assertEqual(body['numResults'], 10)
            self.assertEqual(seen[0].get_header('X-api-key'), 'test-secret')
            self.assertEqual(result['results'][0]['title'], '[REDACTED_API_KEY]')
            self.assertEqual(client.totals()['estimated_cost_USD'], 0.007)
            self.assertEqual(client.totals()['unknown_or_inflight_reserved_USD'], 0)
            for path in Path(folder).iterdir():
                self.assertNotIn(b'test-secret', path.read_bytes())
            call = next(iter(client.ledger['calls'].values()))
            attempt = call['attempts'][0]
            self.assertTrue(attempt['archive_redacted'])
            data = Path(folder, attempt['response_archive']).read_bytes()
            self.assertEqual(hashlib.sha256(data).hexdigest(), attempt['response_sha256'])

    def test_search_accepts_ten_results_and_rejects_eleven(self):
        seen = []

        def opener(request, timeout):
            seen.append(json.loads(request.data))
            return Response(success(0.012))

        with tempfile.TemporaryDirectory() as folder:
            client = ExaClient(folder, 'key', opener=opener)
            client.search('official statistics', '2026-11-09', num_results=10)
            self.assertEqual(seen[0]['numResults'], 10)
            with self.assertRaisesRegex(ValueError, 'exa_num_results_must_be_1_to_10'):
                client.search('official statistics', '2026-11-09', num_results=11)
            with self.assertRaisesRegex(ValueError, 'exa_num_results_must_be_1_to_10'):
                client.search('official statistics', '2026-11-09', num_results=0)

    def test_contents_keeps_per_url_failures_and_single_content_type(self):
        received = []
        obj = {**success(0.002), 'results': [{'url': 'https://a.org', 'text': 'actual evidence'}],
               'statuses': [{'id': 'https://a.org', 'status': 'success'},
                            {'id': 'https://b.org', 'status': 'error', 'error': {'tag': 'CRAWL_NOT_FOUND'}}]}

        def opener(request, timeout):
            received.append(json.loads(request.data))
            return Response(obj)

        with tempfile.TemporaryDirectory() as folder:
            client = ExaClient(folder, 'key', opener=opener)
            self.assertEqual(client.contents(['https://a.org', 'https://b.org']), obj)
            self.assertEqual(received[0], {'urls': ['https://a.org', 'https://b.org'], 'text': {'maxCharacters': 12000}})

    def test_independent_calls_really_overlap(self):
        barrier = threading.Barrier(3)

        def opener(request, timeout):
            barrier.wait(2)
            return Response(success())

        with tempfile.TemporaryDirectory() as folder:
            client = ExaClient(folder, 'key', opener=opener)
            with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
                futures = [pool.submit(client.contents, [f'https://example.org/{i}']) for i in range(3)]
                self.assertEqual(len([f.result() for f in futures]), 3)
            self.assertEqual(client.totals()['peak_concurrency_this_run'], 3)

    def test_identical_inflight_request_is_coalesced_then_cached_on_resume(self):
        entered, release = threading.Event(), threading.Event()
        calls = []

        def opener(request, timeout):
            calls.append(1)
            entered.set()
            release.wait(2)
            return Response(success())

        with tempfile.TemporaryDirectory() as folder:
            client = ExaClient(folder, 'key', opener=opener)
            with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
                first = pool.submit(client.contents, ['https://example.org'])
                self.assertTrue(entered.wait(1))
                second = pool.submit(client.contents, ['https://example.org'])
                release.set()
                self.assertEqual(first.result(), second.result())
            self.assertEqual(len(calls), 1)
            self.assertEqual(client.totals()['cache_hits_this_run'], 1)
            resumed = ExaClient(folder, 'key', opener=lambda *a, **kw: self.fail('cache repeated network'))
            self.assertEqual(resumed.contents(['https://example.org']), success())
            self.assertEqual(resumed.totals()['attempts'], 1)

    def test_budget_waits_for_inflight_then_rejects_without_overspending(self):
        entered, release = threading.Event(), threading.Event()
        calls = []

        def opener(request, timeout):
            calls.append(1)
            entered.set()
            release.wait(2)
            return Response(success())

        with tempfile.TemporaryDirectory() as folder:
            client = ExaClient(folder, 'key', budget_usd=0.001, opener=opener)
            with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
                first = pool.submit(client.contents, ['https://first.org'])
                self.assertTrue(entered.wait(1))
                second = pool.submit(client.contents, ['https://second.org'])
                time.sleep(0.02)
                self.assertFalse(second.done())
                release.set()
                first.result()
                with self.assertRaisesRegex(ValueError, 'budget_reservation_exceeded'):
                    second.result(timeout=2)
            self.assertEqual(len(calls), 1)
            self.assertEqual(client.totals()['budget_committed_USD'], 0.001)

    def test_reported_zero_releases_reservation_for_waiter(self):
        entered, release = threading.Event(), threading.Event()

        def opener(request, timeout):
            if 'first' in request.data.decode():
                entered.set()
                release.wait(2)
            return Response(success(0))

        with tempfile.TemporaryDirectory() as folder:
            client = ExaClient(folder, 'key', budget_usd=0.001, opener=opener)
            with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
                first = pool.submit(client.contents, ['https://first.org'])
                self.assertTrue(entered.wait(1))
                second = pool.submit(client.contents, ['https://second.org'])
                release.set()
                first.result(); second.result(timeout=2)
            self.assertEqual(client.totals()['budget_committed_USD'], 0)
            self.assertEqual(client.totals()['attempts'], 2)

    def test_timeout_is_unknown_reserved_and_never_retried(self):
        count = []

        def opener(*args, **kwargs):
            count.append(1)
            raise TimeoutError('SECRET DETAILS')

        with tempfile.TemporaryDirectory() as folder:
            client = ExaClient(folder, 'key', opener=opener)
            with self.assertRaisesRegex(ValueError, 'exa_request_failed_TimeoutError'):
                client.contents(['https://example.org'])
            self.assertEqual(client.totals()['unknown_or_inflight_reserved_USD'], 0.001)
            self.assertEqual(client.totals()['unknown_requests'], 1)
            resumed = ExaClient(folder, 'key', opener=opener)
            with self.assertRaisesRegex(ValueError, 'previously_attempted_unknown'):
                resumed.contents(['https://example.org'])
            self.assertEqual(len(count), 1)
            self.assertNotIn('SECRET DETAILS', Path(folder, 'ledger.json').read_text())

    def test_malformed_response_archived_without_repeat(self):
        calls = []

        def opener(*args, **kwargs):
            calls.append(1)
            return Response(b'{"results": [')

        with tempfile.TemporaryDirectory() as folder:
            client = ExaClient(folder, 'key', opener=opener)
            with self.assertRaisesRegex(ValueError, 'invalid_json'):
                client.contents(['https://example.org'])
            self.assertEqual(next(Path(folder).glob('*.response.bin')).read_bytes(), b'{"results": [')
            with self.assertRaisesRegex(ValueError, 'previously_attempted_invalid_response'):
                client.contents(['https://example.org'])
            self.assertEqual(len(calls), 1)
            self.assertEqual(client.totals()['missing_cost_attempts'], 1)

    def test_transport_truncation_retains_partial_bytes_as_unknown(self):
        class TruncatedResponse(Response):
            def read(self, size=-1):
                raise http.client.IncompleteRead(b'{"results": [', 100)

        with tempfile.TemporaryDirectory() as folder:
            client = ExaClient(folder, 'key', opener=lambda *a, **kw: TruncatedResponse(b''))
            with self.assertRaisesRegex(ValueError, 'incomplete_response'):
                client.contents(['https://example.org'])
            self.assertEqual(next(Path(folder).glob('*.response.bin')).read_bytes(), b'{"results": [')
            self.assertEqual(client.totals()['unknown_requests'], 1)
            attempt = next(iter(client.ledger['calls'].values()))['attempts'][0]
            self.assertTrue(attempt['response_truncated'])

    def test_429_retries_once_and_preserves_missing_cost_of_rejection(self):
        calls, sleeps = [], []

        def opener(*args, **kwargs):
            calls.append(1)
            if len(calls) == 1:
                raise http_error(429, '0.01')
            return Response(success())

        with tempfile.TemporaryDirectory() as folder:
            client = ExaClient(folder, 'key', opener=opener)
            client.sleep = sleeps.append
            client.contents(['https://example.org'])
            self.assertEqual(sleeps, [0.01])
            self.assertEqual(len(calls), 2)
            self.assertEqual(client.totals()['unknown_or_inflight_reserved_USD'], 0.001)
            self.assertEqual(client.totals()['estimated_cost_USD'], 0.001)
            self.assertEqual(client.totals()['failed_attempts'], 1)

    def test_429_long_wait_deferred_and_repeated_429_stops(self):
        for header, expected_calls in [('120', 1), ('0', 2)]:
            with self.subTest(header=header), tempfile.TemporaryDirectory() as folder:
                calls = []

                def opener(*args, **kwargs):
                    calls.append(1)
                    raise http_error(429, header)

                client = ExaClient(folder, 'key', opener=opener)
                client.sleep = lambda _: None
                with self.assertRaises(ValueError):
                    client.contents(['https://example.org'])
                with self.assertRaisesRegex(ValueError, 'previously_attempted'):
                    client.contents(['https://example.org'])
                self.assertEqual(len(calls), expected_calls)

    def test_auth_payment_stop_future_requests_and_reserve_failure(self):
        for status in (401, 402, 403):
            with self.subTest(status=status), tempfile.TemporaryDirectory() as folder:
                calls = []

                def opener(*args, **kwargs):
                    calls.append(1)
                    raise http_error(status, body=b'{"error":"key"}')

                client = ExaClient(folder, 'key', opener=opener)
                with self.assertRaisesRegex(ValueError, f'http_{status}'):
                    client.contents(['https://first.org'])
                with self.assertRaisesRegex(ValueError, 'provider_stopped'):
                    client.contents(['https://second.org'])
                self.assertEqual(len(calls), 1)
                self.assertEqual(client.totals()['unknown_or_inflight_reserved_USD'], 0.001)

    def test_refused_key_rotates_to_next_key_then_stops_when_all_refused(self):
        for status in (401, 402, 403):
            with self.subTest(status=status), tempfile.TemporaryDirectory() as folder:
                used = []

                def opener(request, timeout):
                    key = request.get_header('X-api-key')
                    used.append(key)
                    if key in ('key-one', 'key-two'):
                        raise http_error(status, body=b'{"error":"NO_MORE_CREDITS"}')
                    return Response(success())

                client = ExaClient(folder, ['key-one', 'key-two', 'key-three'], opener=opener)
                client.contents(['https://first.org'])
                self.assertEqual(used, ['key-one', 'key-two', 'key-three'])
                client.contents(['https://second.org'])
                self.assertEqual(used[-1], 'key-three')
                self.assertEqual(len(client.ledger['key_rotations']), 2)
                self.assertIsNone(client.fatal_error)
                for path in Path(folder).iterdir():
                    for key in (b'key-one', b'key-two', b'key-three'):
                        self.assertNotIn(key, path.read_bytes())

        with tempfile.TemporaryDirectory() as folder:
            calls = []

            def refuse(*args, **kwargs):
                calls.append(1)
                raise http_error(402)

            client = ExaClient(folder, ['a-key', 'b-key'], opener=refuse)
            with self.assertRaisesRegex(ValueError, 'http_402'):
                client.contents(['https://first.org'])
            self.assertEqual(len(calls), 2)
            self.assertEqual(client.fatal_error, 'exa_provider_stopped_http_402')
            with self.assertRaisesRegex(ValueError, 'provider_stopped'):
                client.contents(['https://second.org'])
            self.assertEqual(len(calls), 2)

    def test_missing_or_invalid_cost_remains_reserved(self):
        for costs in (None, 'bad', {'total': -1}, {'total': True}, {'total': float('nan')}):
            with self.subTest(costs=costs), tempfile.TemporaryDirectory() as folder:
                client = ExaClient(folder, 'key', opener=lambda *a, **kw: Response({'results': [], 'costDollars': costs}))
                client.contents(['https://example.org'])
                self.assertEqual(client.totals()['missing_cost_attempts'], 1)
                self.assertEqual(client.totals()['unknown_or_inflight_reserved_USD'], 0.001)

    def test_cache_integrity_and_bad_input_are_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            client = ExaClient(folder, 'key', opener=lambda *a, **kw: Response(success()))
            for urls in ([], ['file:///secret'], ['https://u:p@example.org'], ['https://a.org'] * 2, [{}]):
                with self.assertRaises(ValueError):
                    client.contents(urls)
            client.contents(['https://example.org'])
            next(Path(folder).glob('*.response.bin')).write_bytes(b'{}')
            with self.assertRaisesRegex(ValueError, 'hash_mismatch'):
                client.contents(['https://example.org'])

    def test_search_rate_slots_are_global_across_threads(self):
        with tempfile.TemporaryDirectory() as folder:
            client = ExaClient(folder, 'key', opener=lambda *a, **kw: Response(success(0.007)), search_qps=2)
            client.clock = lambda: 10.0
            sleeps = []
            client.sleep = sleeps.append
            with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
                futures = [pool.submit(client.search, str(i), '2026-11-09') for i in range(3)]
                [f.result() for f in futures]
            self.assertEqual(sorted(sleeps), [0, 0.5, 1.0])

    def test_ledger_failure_before_dispatch_releases_active_count(self):
        with tempfile.TemporaryDirectory() as folder:
            client = ExaClient(folder, 'key', opener=lambda *a, **kw: self.fail('network after ledger failure'))
            def broken_persist():
                raise OSError('storage unavailable')
            client._persist = broken_persist
            with self.assertRaises(OSError):
                client.contents(['https://example.org'])
            self.assertEqual(client.active, 0)
            self.assertEqual(client.totals()['budget_committed_USD'], 0)
            with self.assertRaisesRegex(ValueError, 'ledger_write_failed_before_dispatch'):
                client.contents(['https://second.org'])


if __name__ == '__main__':
    unittest.main()
