"""Same-material prompt/hint experiment. Audit arms never select a verdict."""
from copy import deepcopy
from concurrent.futures import ThreadPoolExecutor
from datetime import date
import hashlib
import json
from pathlib import Path

ARMS = ('legacy_hint', 'legacy_nohint', 'shared_hint')
AUDIT_RULE = 'post-production-three-arm-no-repair-v1'


def legacy_prompt():
    policy = json.loads((Path(__file__).parent / 'validation/review_policy_v1.json').read_text())
    prompt = policy['review_prompt']
    if hashlib.sha256(prompt.encode()).hexdigest() != policy['sha256']:
        raise ValueError('legacy_review_policy_hash_mismatch')
    return prompt


def legacy_hint(proposed, candidates):
    """Reproduce the old missing-day hint only, not the new date policy."""
    missing = []
    referenced = set(proposed['evidence_ids'])
    for source in candidates:
        if source['id'] not in referenced:
            continue
        try:
            date.fromisoformat((source.get('published_date') or '')[:10])
        except ValueError:
            missing.append(source['id'])
    candidate = deepcopy(proposed)
    warnings = []
    if missing and proposed['inclusion'] == 'forecast' and proposed['verdict'] != '暂无法判断':
        warnings = [{'code': 'publication_date_unconfirmed', 'evidence_ids': sorted(set(missing))}]
        candidate.update(verdict='暂无法判断', basis='evidence',
            reason='引用材料的发表时间尚未确认，无法确认其属于证据截止日前；原模型建议保留待复核。',
            remaining_gap='核对被引用材料的可证实发表版本及日期。' + proposed['remaining_gap'])
    return {'mechanical_candidate': {k: candidate[k] for k in ('verdict', 'basis', 'reason', 'remaining_gap')},
            'mechanical_warnings': warnings}


def arm_order(ident):
    return sorted(ARMS, key=lambda arm: hashlib.sha256((ident + arm).encode()).hexdigest())


def sample_ids(ids, count=12):
    return sorted(ids, key=lambda ident: hashlib.sha256(ident.encode()).hexdigest())[:count]


def run_audits(packets, run_dir, llm):
    """Run shadows after production; preserve formal outcomes and use remaining funds."""
    import verify_prediction as vp
    import run_parallel as rp
    import semantic_review as sr

    root = Path(run_dir)

    def evaluate(packet):
        ident = packet['id']
        directory = vp.job_directory(root, ident)
        result_path = directory / 'result.json'
        snapshot_path = directory / 'review-audit-input.json'
        try:
            manifest = rp.read_json(directory / 'input.json')
            result = vp.cached_result(root, directory, manifest)
            if result is None:
                return {'claim_id': ident, 'status': 'missing_result'}
        except (ValueError, OSError, KeyError) as exc:
            return {'claim_id': ident, 'status': 'invalid_result', 'error': vp.safe_error(exc)}
        audit = result.setdefault('review_audit', {'selected': True, 'arms': {}})
        arms = audit.setdefault('arms', {})
        primary = arms.get('shared_nohint', {})

        def persist():
            rp.save_json(result_path, result)
            receipt = rp.read_json(directory / 'receipt.json')
            receipt['sha256'] = hashlib.sha256(result_path.read_bytes()).hexdigest()
            rp.save_json(directory / 'receipt.json', receipt)

        def unavailable(status, error):
            for arm in ARMS:
                if arms.get(arm, {}).get('status') not in {'completed', 'failed'}:
                    arms[arm] = {'status': status, 'error': error, 'schema_repaired': False}
            persist()
            return {'claim_id': ident, 'status': status, 'error': error}

        if primary.get('status') != 'completed':
            return unavailable('missing', 'formal_first_review_not_completed')
        if not snapshot_path.is_file():
            return unavailable('missing', 'review_audit_input_missing')
        try:
            snapshot = rp.read_json(snapshot_path)
            data, context, original_request = snapshot['data'], snapshot['context'], snapshot['request']
            material_hash = vp.digest(data)
            if material_hash != snapshot['common_input_sha256'] or material_hash != primary['common_input_sha256']:
                raise ValueError('review_audit_input_hash_mismatch')
            if len(original_request['messages']) != 2 or json.loads(original_request['messages'][1]['content']) != data:
                raise ValueError('review_audit_request_input_mismatch')
            # Bind validation texts to the hashed model input; a modified context
            # must not make a fabricated quotation pass the source validator.
            case = data['cases'][0]
            expected = {'id': ident, 'cutoff': data['cutoff'],
                'original_text': (case.get('quote') or '') + '\n' + (case.get('context') or ''),
                'proposal_text': '\n'.join(str(data['proposed_assessment'].get(k) or '')
                    for k in ('scope', 'reason', 'limitation', 'observation_end')),
                'source_texts': {c['id']: c['text'] for c in data['evidence_candidates']},
                'review_quote_options': data.get('review_quote_options', {})}
            if case['id'] != ident or any(context.get(k) != value for k, value in expected.items()):
                raise ValueError('review_audit_context_input_mismatch')
        except (ValueError, OSError, KeyError, TypeError) as exc:
            return unavailable('failed', vp.safe_error(exc))
        for arm in arm_order(ident):
            previous = arms.get(arm, {})
            if previous.get('status') in {'completed', 'failed'}:
                continue
            arm_data = deepcopy(data)
            if arm.endswith('_hint'):
                arm_data.update(legacy_hint(data['proposed_assessment'], data['evidence_candidates']))
            request = deepcopy(original_request)
            prompt = legacy_prompt() if arm.startswith('legacy_') else sr.REVIEW_PROMPT
            request['messages'][0]['content'] = prompt
            request['messages'][1]['content'] = json.dumps(arm_data, ensure_ascii=False)
            request_hash = vp.digest(request)
            if previous.get('status') == 'started' and previous.get('request_sha256') != request_hash:
                arms[arm] = previous | {'status': 'failed', 'error': 'review_audit_resume_request_mismatch'}
                persist()
                continue
            if previous.get('status') != 'started':
                if result.get('diagnostic_llm_calls', 0) >= len(ARMS):
                    arms[arm] = {'status': 'failed', 'error': 'review_audit_call_limit', 'schema_repaired': False}
                    persist()
                    continue
                result['diagnostic_llm_calls'] = result.get('diagnostic_llm_calls', 0) + 1
                result.setdefault('request_receipts', []).append({'provider': 'deepseek', 'stage': 'semantic_review',
                    'purpose': arm, 'request_sha256': request_hash})
            arms[arm] = {'status': 'started', 'schema_repaired': False,
                'common_input_sha256': material_hash, 'primary_material_sha256': material_hash,
                'request_sha256': request_hash, 'prompt_sha256': hashlib.sha256(prompt.encode()).hexdigest(),
                'primary_schema_repaired': bool(primary.get('schema_repaired')),
                'same_protocol_as_primary': not bool(primary.get('schema_repaired'))}
            persist()
            try:
                items = llm.call('semantic_review', request, [context], 1)
                review = vp.validate_stage('semantic_review', items, [context])[0]
                arms[arm].update(status='completed', review=deepcopy(review))
            except Exception as exc:
                arms[arm].update(status='failed', error=vp.safe_error(exc))
            persist()
        return {'claim_id': ident, 'status': 'processed',
                'arms': {arm: arms[arm]['status'] for arm in ARMS}}

    selected = [p for p in packets if p.get('review_audit')]
    with ThreadPoolExecutor(max_workers=4) as pool:
        return list(pool.map(evaluate, selected))
