"""Semantic gate shape and source binding; these are not factual-quality tests."""
from copy import deepcopy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import semantic_review as sr

ORIGINAL = 'If the regional shortage continues, it will become a major problem.\nThe speaker describes a local shortage.'
SOURCES = {'ev-one': 'The regional study measured the shortage in 2025.\nThe report was published in 2026.',
           'ev-two': 'The other region improved in 2025.'}


def review(decision='accept', check=None, value='fail', evidence_id=None, quote=None):
    result = {'id': 'claim-one', 'decision': decision,
              'checks': {name: 'pass' for name in sr.CHECKS}, 'issues': [], 'remaining_gap': ''}
    if check:
        result['checks'][check] = value
        result['issues'] = [{'check': check, 'reason': 'The proposed judgment substitutes another region for the stated region.',
                             'source_quote': quote or 'If the regional shortage continues', 'evidence_id': evidence_id,
                             'quote_origin': 'evidence' if evidence_id else 'book'}]
        result['remaining_gap'] = 'Bind the observed region to the original region, or retain the mismatch as unresolved.'
    return result


class SemanticReviewTests(unittest.TestCase):
    def test_quote_reference_resolves_only_to_provided_verbatim_text(self):
        options = sr.quote_options(ORIGINAL, '', [], SOURCES)
        item = review('revise', 'object_match')
        item['issues'][0] = {'check': 'object_match', 'reason': 'The region is mismatched.', 'quote_ref': 'q0'}
        result = sr.validate_review(item, 'claim-one', SOURCES, ORIGINAL, quote_options=options)
        issue = result['issues'][0]
        self.assertIn(issue['source_quote'], ORIGINAL)
        self.assertEqual(issue['quote_origin'], 'book')
        self.assertEqual(issue['quote_resolution'], 'program_supplied_verbatim_option')

    def test_unknown_or_conflicting_quote_reference_is_rejected(self):
        options = sr.quote_options(ORIGINAL, '', [], SOURCES)
        for reference in ('missing', 'q0'):
            item = review('revise', 'object_match')
            item['issues'][0]['quote_ref'] = reference
            item['issues'][0]['source_quote'] = 'Not the supplied quote.'
            with self.assertRaisesRegex(ValueError, 'quote_ref'):
                sr.validate_review(item, 'claim-one', SOURCES, ORIGINAL, quote_options=options)

    def test_proposal_quote_reference_does_not_bypass_fact_source_rule(self):
        item = review('revise', 'object_match')
        item['issues'][0] = {'check': 'object_match', 'reason': 'Mismatch.', 'quote_ref': 'q0'}
        options = {'q0': {'quote_origin': 'proposal', 'evidence_id': None, 'source_quote': 'Draft claim.'}}
        with self.assertRaisesRegex(ValueError, 'quote_not_in_supplied_text'):
            sr.validate_review(item, 'claim-one', SOURCES, ORIGINAL, 'Draft claim.', options)

    def validate(self, item, **kwargs):
        return sr.validate_review(item, kwargs.get('case_id', 'claim-one'),
                                  kwargs.get('source_texts', SOURCES), kwargs.get('original_text', ORIGINAL),
                                  kwargs.get('proposal_text', ''))

    def test_accept_requires_all_checks_and_returns_unchanged_object(self):
        item = review()
        self.assertIs(self.validate(item), item)

    def test_accept_cannot_hide_nonpass_issue_or_remaining_gap(self):
        variants = [review('accept', 'object_match'), review(), review()]
        variants[1]['issues'] = [{'check': 'object_match'}]
        variants[2]['remaining_gap'] = 'The object is not identified.'
        for item in variants:
            with self.subTest(item=item), self.assertRaises(ValueError):
                self.validate(item)

    def test_fixable_failure_can_request_one_revision(self):
        item = review('revise', 'condition_logic')
        before = deepcopy(item)
        self.assertEqual(self.validate(item), before)

    def test_unknown_object_can_end_as_unresolved_with_book_quote(self):
        item = review('unresolved', 'object_match', 'unknown')
        self.assertEqual(self.validate(item)['decision'], 'unresolved')

    def test_only_unknown_checks_cannot_request_an_unfounded_revision(self):
        with self.assertRaisesRegex(ValueError, 'unknown_requires_unresolved'):
            self.validate(review('revise', 'object_match', 'unknown'))

    def test_source_quote_binds_to_the_exact_selected_source(self):
        item = review('revise', 'time_alignment', evidence_id='ev-one',
                      quote='The regional study measured the shortage in 2025.')
        self.assertEqual(self.validate(item), item)
        item['issues'][0]['evidence_id'] = 'ev-two'
        with self.assertRaisesRegex(ValueError, 'quote_not_in_supplied_text'):
            self.validate(item)

    def test_foreign_source_and_fabricated_quote_rejected(self):
        foreign = review('revise', 'evidence_support', evidence_id='another-task-source', quote='A claim.')
        fabricated = review('revise', 'evidence_support', evidence_id='ev-one', quote='The shortage was zero in 2025.')
        for item in (foreign, fabricated):
            with self.subTest(item=item), self.assertRaises(ValueError):
                self.validate(item)

    def test_proposal_text_cannot_be_used_as_original_book_quote(self):
        item = review('revise', 'verdict_logic', quote='All indicators will deteriorate monotonically.')
        with self.assertRaisesRegex(ValueError, 'quote_not_in_supplied_text'):
            self.validate(item)

    def test_internal_verdict_and_time_critique_can_bind_to_supplied_proposal(self):
        proposal = 'Some premise indicators improved. Therefore the consequent was only partially realized.\nObservation end: 2026-01-01.'
        for check, quote in [('verdict_logic', 'Therefore the consequent was only partially realized.'),
                             ('time_alignment', 'Observation end: 2026-01-01.')]:
            with self.subTest(check=check):
                item = review('revise', check, quote=quote)
                item['issues'][0]['quote_origin'] = 'book'
                returned = self.validate(item, proposal_text=proposal)
                self.assertEqual(returned['issues'][0]['quote_origin'], 'proposal')
                self.assertEqual(item['issues'][0]['quote_origin'], 'book')

    def test_proposal_cannot_establish_object_conditions_or_external_evidence(self):
        proposal = 'The original region is the same as the observed region.'
        for check in ('object_match', 'condition_logic', 'evidence_support', 'counterevidence'):
            with self.subTest(check=check):
                item = review('revise', check, quote=proposal)
                item['issues'][0]['quote_origin'] = 'proposal'
                with self.assertRaisesRegex(ValueError, 'quote_not_in_supplied_text'):
                    self.validate(item, proposal_text=proposal)

    def test_proposal_quote_repair_is_bounded_and_origin_is_derived(self):
        proposal = 'Mixed indicators\ntherefore prove partial realization.'
        item = review('revise', 'verdict_logic', quote=proposal.replace('\n', ' '))
        returned = self.validate(item, proposal_text=proposal)
        note = returned['issues'][0]
        self.assertEqual(note['source_quote'], proposal)
        self.assertEqual(note['quote_origin'], 'proposal')
        self.assertEqual(note['quote_verification']['model_quote'], item['issues'][0]['source_quote'])
        item['issues'][0]['source_quote'] = 'Mixed indicators therefore prove full realization.'
        with self.assertRaisesRegex(ValueError, 'quote_not_in_supplied_text'):
            self.validate(item, proposal_text=proposal)
        item = review('revise', 'verdict_logic')
        item['issues'][0]['quote_origin'] = 'proposal'
        self.assertEqual(self.validate(item, proposal_text=ORIGINAL)['issues'][0]['quote_origin'], 'book')

    def test_exact_quotes_preserve_newlines_and_linewrap_restoration_is_recorded(self):
        item = review('revise', 'time_alignment', evidence_id='ev-one', quote=SOURCES['ev-one'])
        self.assertEqual(self.validate(item), item)
        item['issues'][0]['source_quote'] = SOURCES['ev-one'].replace('\n', ' ')
        before = deepcopy(item)
        returned = self.validate(item)
        restored = returned['issues'][0]
        self.assertEqual(restored['source_quote'], SOURCES['ev-one'])
        self.assertEqual(restored['quote_verification'], {
            'method': 'unique_whitespace_alignment', 'model_quote': before['issues'][0]['source_quote']})
        self.assertEqual(item, before)

    def test_quote_alignment_never_repairs_words_punctuation_or_ambiguous_matches(self):
        for quote, text in [('The count was 90.', 'The count was 9 1.'),
                            ('One, two.', 'One two.'),
                            ('A B A', 'A\nB\nA\nB\nA'),
                            ('alpha beta', 'alpha\nbeta and alpha\tbeta')]:
            with self.subTest(quote=quote, text=text), self.assertRaises(ValueError):
                sr.align_quote(quote, text)
        self.assertEqual(sr.align_quote('alpha beta', 'alpha beta; alpha beta'), 'alpha beta')
        self.assertEqual(sr.align_quote('alpha beta', 'prefix alpha\n beta suffix'), 'alpha\n beta')

    def test_checks_are_complete_and_values_are_enum_strings(self):
        variants = [review() for _ in range(4)]
        del variants[0]['checks']['time_alignment']
        variants[1]['checks']['new_check'] = 'pass'
        variants[2]['checks']['time_alignment'] = True
        variants[3]['checks']['time_alignment'] = 'probably'
        for item in variants:
            with self.subTest(item=item), self.assertRaises(ValueError):
                self.validate(item)

    def test_wrong_id_or_decision_rejected(self):
        variants = [review() for _ in range(3)]
        variants[0]['id'] = 'claim-two'
        variants[1]['decision'] = 'approved'
        variants[2]['decision'] = []
        for item in variants:
            with self.subTest(item=item), self.assertRaises(ValueError):
                self.validate(item)

    def test_nonaccept_must_explain_each_nonpass_check(self):
        item = review('unresolved', 'object_match', 'unknown')
        item['checks']['time_alignment'] = 'unknown'
        with self.assertRaisesRegex(ValueError, 'unexplained_nonpass'):
            self.validate(item)
        item['issues'].append({'check': 'time_alignment', 'reason': 'The time of the original shortage is missing.',
                               'source_quote': 'The speaker describes a local shortage.', 'evidence_id': None,
                               'quote_origin': 'book'})
        self.assertEqual(self.validate(item), item)

    def test_nonaccept_requires_issues_gap_and_nonpass(self):
        variants = [review('unresolved', 'object_match', 'unknown') for _ in range(3)]
        variants[0]['issues'] = []
        variants[1]['remaining_gap'] = ' '
        variants[2]['checks']['object_match'] = 'pass'
        for item in variants:
            with self.subTest(item=item), self.assertRaises(ValueError):
                self.validate(item)

    def test_issue_cannot_be_attached_to_a_passing_check(self):
        item = review('revise', 'object_match')
        item['issues'][0]['check'] = 'time_alignment'
        with self.assertRaisesRegex(ValueError, 'issue_check_mismatch'):
            self.validate(item)

    def test_incomplete_issue_or_wrong_source_identifier_type_rejected(self):
        variants = [review('revise', 'object_match') for _ in range(4)]
        del variants[0]['issues'][0]['evidence_id']
        variants[1]['issues'][0]['reason'] = ''
        variants[2]['issues'][0]['source_quote'] = '\n'
        variants[3]['issues'][0]['evidence_id'] = []
        for item in variants:
            with self.subTest(item=item), self.assertRaises(ValueError):
                self.validate(item)

    def test_immutable_inputs_and_secret_free_error_codes(self):
        item = review('revise', 'object_match')
        before = deepcopy(item)
        self.validate(item)
        self.assertEqual(item, before)
        item['issues'][0]['evidence_id'] = 'SECRET_PROVIDER_TOKEN'
        with self.assertRaises(ValueError) as error:
            self.validate(item)
        self.assertNotIn('SECRET_PROVIDER_TOKEN', str(error.exception))


if __name__ == '__main__':
    unittest.main()
