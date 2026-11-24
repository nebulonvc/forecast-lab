"""Bounded Exa REST calls with an auditable, thread-safe per-run ledger.

Provider costs are estimates, not reconciled bills. An outer run lock must own
the directory across processes. Failed/ambiguous requests are never silently
replayed; the sole automatic retry is one explicitly rejected HTTP 429.
"""
from datetime import date, datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
import hashlib
import http.client
import json
import math
from pathlib import Path
import threading
import time
import urllib.error
import urllib.parse
import urllib.request


BASE_URL = 'https://api.exa.ai'
VERSION = 'exa-rest-v1'
MAX_RESPONSE_BYTES = 8_000_000
MAX_RETRY_WAIT = 30


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(',', ':')).encode('utf-8')


def save_bytes(path, value):
    temp = path.with_name(path.name + '.tmp')
    temp.write_bytes(value)
    temp.replace(path)


def now():
    return datetime.now(timezone.utc).isoformat()


def valid_cost(raw):
    costs = raw.get('costDollars') if isinstance(raw, dict) else None
    value = costs.get('total') if isinstance(costs, dict) else None
    return (float(value) if isinstance(value, (int, float)) and not isinstance(value, bool)
            and math.isfinite(value) and value >= 0 else None)


class ExaClient:
    def __init__(self, directory, api_key, budget_usd=0.1, timeout=30, search_qps=3, opener=None):
        keys = [api_key] if isinstance(api_key, str) else list(api_key or [])
        keys = [k for k in keys if isinstance(k, str) and k.strip()]
        if not keys or not (math.isfinite(budget_usd) and budget_usd > 0):
            raise ValueError('exa_missing_key_or_invalid_budget')
        if not (math.isfinite(timeout) and timeout > 0 and math.isfinite(search_qps) and 0 < search_qps <= 10):
            raise ValueError('exa_invalid_timeout_or_search_qps')
        self.directory = Path(directory)
        self.directory.mkdir(parents=True, exist_ok=True)
        # Several keys may be supplied; a key refused with 401/402/403 is retired and
        # the next one is used. The run stops only when every key has been refused.
        self.api_keys, self.key_index = keys, 0
        self.api_key, self.budget, self.timeout = keys[0], budget_usd, timeout
        self.retired_keys = 0
        self.search_qps = search_qps
        self.opener = opener or urllib.request.urlopen
        self.sleep, self.clock = time.sleep, time.monotonic
        self.lock = threading.RLock()
        self.changed = threading.Condition(self.lock)
        self.rate_lock = threading.Lock()
        self.next_search_at = 0.0
        self.request_locks = {}
        self.active = self.peak = self.cached = 0
        self.ledger_file = self.directory / 'ledger.json'
        self.ledger = (json.loads(self.ledger_file.read_text()) if self.ledger_file.exists() else
                       {'version': VERSION, 'endpoint': BASE_URL, 'created_at': now(), 'calls': {}})
        if self.ledger.get('version') != VERSION or self.ledger.get('endpoint') != BASE_URL:
            raise ValueError('exa_ledger_version_mismatch')
        self.fatal_error = self.ledger.get('fatal_error')

    def _redact(self, value):
        if isinstance(value, str):
            for key in self.api_keys:
                value = value.replace(key, '[REDACTED_API_KEY]')
            return value
        if isinstance(value, list):
            return [self._redact(x) for x in value]
        if isinstance(value, dict):
            return {self._redact(k): self._redact(v) for k, v in value.items()}
        return value

    def _redact_bytes(self, value):
        for key in self.api_keys:
            value = (value.replace(key.encode(), b'[REDACTED_API_KEY]')
                     .replace(json.dumps(key)[1:-1].encode(), b'[REDACTED_API_KEY]'))
        return value

    def totals(self):
        with self.lock:
            calls = list(self.ledger['calls'].values())
            attempts = [a for c in calls for a in c['attempts']]
            estimates = sum(a.get('estimated_cost_USD', 0) for a in attempts)
            retained = sum(a['reserved_USD'] for a in attempts if 'estimated_cost_USD' not in a)
            return {'estimated_cost_USD': round(estimates, 9),
                    'unknown_or_inflight_reserved_USD': round(retained, 9),
                    'budget_committed_USD': round(estimates + retained, 9),
                    'budget_limit_USD': self.budget, 'requests': len(calls), 'attempts': len(attempts),
                    'failed_attempts': sum(a['state'] not in {'in_flight', 'completed'} for a in attempts),
                    'unknown_requests': sum(c['state'] in {'in_flight', 'unknown'} for c in calls),
                    'missing_cost_attempts': sum(a['state'] != 'in_flight' and 'estimated_cost_USD' not in a
                                                 for a in attempts),
                    'cache_hits_this_run': self.cached, 'active_requests': self.active,
                    'peak_concurrency_this_run': self.peak,
                    'price_basis': 'costDollars estimates plus conservative unknown reservations; bill not reconciled'}

    def _persist(self):
        self.ledger['updated_at'] = now()
        self.ledger['totals'] = self.totals()
        save_bytes(self.ledger_file, canonical(self.ledger))

    def _throttle(self):
        with self.rate_lock:
            current = self.clock()
            scheduled = max(current, self.next_search_at)
            self.next_search_at = scheduled + 1 / self.search_qps
        self.sleep(max(0, scheduled - current))

    def _reserve(self, digest, kind, payload, reservation):
        with self.changed:
            while self.totals()['budget_committed_USD'] + reservation > self.budget + 1e-12:
                if self.fatal_error:
                    raise ValueError(self.fatal_error)
                if self.active == 0:
                    raise ValueError('exa_budget_reservation_exceeded')
                self.changed.wait()
            if self.fatal_error:
                raise ValueError(self.fatal_error)
            request_bytes = canonical(self._redact(payload))
            request_path = self.directory / (digest + '.request.json')
            if request_path.exists() and request_path.read_bytes() != request_bytes:
                raise ValueError('exa_request_archive_mismatch')
            save_bytes(request_path, request_bytes)
            call = self.ledger['calls'].setdefault(digest, {'kind': kind, 'state': 'in_flight', 'attempts': []})
            attempt = {'number': len(call['attempts']) + 1, 'state': 'in_flight',
                       'started_at': now(), 'reserved_USD': reservation}
            call['attempts'].append(attempt)
            call['state'] = 'in_flight'
            call['request_sha256'] = hashlib.sha256(request_bytes).hexdigest()
            self.active += 1
            self.peak = max(self.peak, self.active)
            try:
                self._persist()
            except Exception:
                self.active -= 1
                self.fatal_error = 'exa_ledger_write_failed_before_dispatch'
                attempt.update(state='not_sent', reserved_USD=0, estimated_cost_USD=0,
                               accounting_basis='local_failure_before_network')
                call['state'] = 'not_sent'
                self.changed.notify_all()
                raise
            return attempt

    def _retry_delay(self, header):
        try:
            if header is None:
                return 1.0
            try:
                delay = float(header)
            except ValueError:
                parsed = parsedate_to_datetime(header)
                if parsed.tzinfo is None:
                    parsed = parsed.replace(tzinfo=timezone.utc)
                delay = (parsed - datetime.now(timezone.utc)).total_seconds()
            return max(0, delay) if math.isfinite(delay) else MAX_RETRY_WAIT + 1
        except (TypeError, ValueError, OverflowError):
            return MAX_RETRY_WAIT + 1

    def _attempt(self, digest, kind, payload, reservation):
        attempt = self._reserve(digest, kind, payload, reservation)
        raw_bytes, raw, status, error, retry_after = None, None, None, None, None

        def read_response(response):
            try:
                return response.read(MAX_RESPONSE_BYTES + 1), False
            except http.client.IncompleteRead as exc:
                return exc.partial, True

        try:
            if kind == 'search':
                self._throttle()
            with self.lock:
                used_key, used_index = self.api_key, self.key_index
            attempt['key_slot'] = used_index + 1
            request = urllib.request.Request(BASE_URL + '/' + kind, data=canonical(payload), method='POST',
                                             headers={'Content-Type': 'application/json', 'x-api-key': used_key})
            try:
                with self.opener(request, timeout=self.timeout) as response:
                    status = 200
                    raw_bytes, incomplete = read_response(response)
                    if incomplete:
                        error = 'incomplete_response'
            except urllib.error.HTTPError as exc:
                status, retry_after = exc.code, exc.headers.get('Retry-After') if exc.headers else None
                try:
                    raw_bytes, incomplete = read_response(exc)
                finally:
                    exc.close()
                error = 'http_' + str(status)
            if raw_bytes is not None:
                archive = self._redact_bytes(raw_bytes)
                path = self.directory / f'{digest}.attempt-{attempt["number"]}.response.bin'
                save_bytes(path, archive)
                attempt.update(response_archive=path.name, response_sha256=hashlib.sha256(archive).hexdigest(),
                               archive_redacted=(archive != raw_bytes), response_bytes=len(raw_bytes))
                if incomplete:
                    attempt['response_truncated'] = True
                if len(raw_bytes) > MAX_RESPONSE_BYTES:
                    attempt['response_truncated'] = True
                    error = error or 'response_size_limit'
                else:
                    try:
                        raw = self._redact(json.loads(raw_bytes))
                    except (ValueError, UnicodeError):
                        error = error or 'invalid_json'
                if status == 200 and (not isinstance(raw, dict) or not isinstance(raw.get('results'), list)):
                    error = error or 'invalid_response_shape'
        except Exception as exc:
            error = type(exc).__name__
        finally:
            with self.changed:
                self.active -= 1
                attempt.update(finished_at=now(), http_status=status)
                cost = valid_cost(raw)
                if cost is not None:
                    attempt['estimated_cost_USD'] = cost
                    attempt['accounting_basis'] = 'provider_costDollars_estimate'
                else:
                    attempt['accounting_basis'] = 'reservation_retained_cost_unknown'
                if isinstance(raw, dict) and isinstance(raw.get('requestId'), str):
                    attempt['provider_request_id'] = raw['requestId']
                if error:
                    attempt['error'] = error
                    attempt['state'] = ('unknown' if error == 'incomplete_response' else
                                        'rejected' if status is not None and 400 <= status < 500 else
                                        'invalid_response' if status == 200 else 'unknown')
                else:
                    attempt['state'] = 'completed'
                call = self.ledger['calls'][digest]
                call['state'] = attempt['state']
                if status in (401, 402, 403):
                    slot = attempt.get('key_slot', 1) - 1
                    if slot == self.key_index and self.key_index + 1 < len(self.api_keys):
                        self.key_index += 1
                        self.api_key = self.api_keys[self.key_index]
                        self.retired_keys += 1
                        self.ledger.setdefault('key_rotations', []).append(
                            {'at': now(), 'retired_slot': slot + 1, 'http_status': status})
                        attempt['key_rotated'] = True
                    elif slot < self.key_index:
                        attempt['key_rotated'] = True  # another thread already moved on
                    else:
                        self.fatal_error = 'exa_provider_stopped_http_' + str(status)
                if self.totals()['budget_committed_USD'] > self.budget + 1e-12:
                    self.fatal_error = 'exa_provider_cost_exceeded_budget'
                if self.fatal_error:
                    self.ledger['fatal_error'] = self.fatal_error
                try:
                    self._persist()
                finally:
                    self.changed.notify_all()
        return raw, error, status, retry_after

    def _call(self, kind, payload, reservation):
        digest = hashlib.sha256(canonical({'version': VERSION, 'kind': kind, 'payload': payload})).hexdigest()
        with self.lock:
            request_lock = self.request_locks.setdefault(digest, threading.Lock())
        with request_lock:
            with self.lock:
                prior = self.ledger['calls'].get(digest)
                if prior:
                    if prior['state'] != 'completed':
                        raise ValueError('exa_request_previously_attempted_' + prior['state'] + '_' + digest[:12])
                    last = prior['attempts'][-1]
                    data = (self.directory / last['response_archive']).read_bytes()
                    if hashlib.sha256(data).hexdigest() != last['response_sha256']:
                        raise ValueError('exa_cached_response_hash_mismatch')
                    raw = json.loads(data)
                    self.cached += 1
                    self._persist()
                    return raw
            number = 0
            while True:
                raw, error, status, retry_after = self._attempt(digest, kind, payload, reservation)
                if not error:
                    return raw
                last = self.ledger['calls'][digest]['attempts'][-1]
                if status in (401, 402, 403) and last.get('key_rotated') and number < len(self.api_keys):
                    number += 1
                    continue  # refused key retired; same request on the next key
                if status != 429 or number >= len(self.api_keys):
                    raise ValueError('exa_request_failed_' + error)
                number += 1
                delay = self._retry_delay(retry_after)
                with self.lock:
                    self.ledger['calls'][digest]['retry_after_seconds'] = delay
                    self.ledger['calls'][digest]['retry_deferred'] = delay > MAX_RETRY_WAIT
                    self._persist()
                if delay > MAX_RETRY_WAIT:
                    raise ValueError('exa_retry_deferred_429')
                self.sleep(delay)

    def search(self, query, cutoff, num_results=10):
        if not isinstance(query, str) or not query.strip() or len(query) > 4000:
            raise ValueError('exa_invalid_query')
        if not isinstance(num_results, int) or isinstance(num_results, bool) or not 1 <= num_results <= 10:
            raise ValueError('exa_num_results_must_be_1_to_10')
        end = date.fromisoformat(cutoff) + timedelta(days=1)
        # More hits share one request. The reservation stays above the historical
        # five-result estimate; the ledger replaces it with costDollars when present.
        reservation = 0.007 if num_results <= 5 else 0.012
        return self._call('search', {'query': query.strip(), 'type': 'auto', 'numResults': num_results,
                                    'endPublishedDate': end.isoformat() + 'T00:00:00Z',
                                    'contents': {'highlights': True}}, reservation)

    def contents(self, urls):
        if (not isinstance(urls, list) or not 1 <= len(urls) <= 8
                or any(not isinstance(url, str) for url in urls) or len(set(urls)) != len(urls)):
            raise ValueError('exa_contents_requires_1_to_8_unique_urls')
        for url in urls:
            parsed = urllib.parse.urlsplit(url) if isinstance(url, str) else None
            if not parsed or parsed.scheme not in ('http', 'https') or not parsed.netloc or parsed.username:
                raise ValueError('exa_invalid_content_url')
        return self._call('contents', {'urls': urls, 'text': {'maxCharacters': 12000}}, len(urls) * 0.001)
