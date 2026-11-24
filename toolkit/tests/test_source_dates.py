"""Availability is separate from publication precision and observation time."""
from copy import deepcopy
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import verify_prediction as vp
from test_verify_prediction import FakeLLM, FakeExa, packet, assessment, BODY


class SourceDateTests(unittest.TestCase):
    def source(self, published=None, *, kind='exa_contents', retrieved=None):
        return {'id': 's', 'text': BODY, 'published_date': published,
                'source_kind': kind, 'retrieved_at': retrieved}

    def inspect(self, source, note_date=None, relation='support'):
        item = assessment('a', 's')
        item['evidence_notes'][0].update(publication_date=note_date, relation=relation)
        return vp.inspect_assessment(item, [source], '2026-11-09')

    def test_capture_before_cutoff_proves_availability_without_publication_date(self):
        item, warnings = self.inspect(self.source(retrieved='2026-11-09T23:00:00+00:00'))
        self.assertEqual(item['verdict'], '正确')
        self.assertIsNone(item['evidence_notes'][0]['publication_date'])
        self.assertEqual(item['observation_end'], '2025-12-31')
        self.assertTrue(warnings)

    def test_late_or_untrusted_capture_is_a_warning_and_does_not_override_the_verdict(self):
        variants = [self.source(retrieved='2026-11-10T00:00:00+00:00'),
                    self.source(retrieved='2026-11-09'),
                    self.source(kind='previously_registered_excerpt', retrieved='2026-11-01T00:00:00+00:00')]
        for source in variants:
            with self.subTest(source=source):
                item, warnings = self.inspect(source)
                self.assertEqual(item['verdict'], '正确')
                self.assertEqual(item['evidence_notes'][0]['source_availability']['status'], 'unknown')
                self.assertTrue(warnings)
                self.assertTrue(all(warning.get('blocks_verdict') is False for warning in warnings))

    def test_capture_timestamp_is_compared_in_utc(self):
        item, _ = self.inspect(self.source(retrieved='2026-11-10T02:00:00+08:00'))
        self.assertEqual(item['verdict'], '正确')
        self.assertEqual(item['evidence_notes'][0]['source_availability']['status'], 'available')
        item, warnings = self.inspect(self.source(retrieved='2026-11-09T23:00:00-08:00'))
        self.assertEqual(item['verdict'], '正确')
        self.assertEqual(item['evidence_notes'][0]['source_availability']['status'], 'unknown')
        self.assertTrue(any(warning['code'] == 'source_availability_unconfirmed' and warning['blocks_verdict'] is False
                            for warning in warnings))

    def test_year_and_month_preserve_precision_and_prove_bounded_availability(self):
        for publication, expected in [('2025', ('2025-01-01', '2025-12-31')),
                                      ('2026-01', ('2026-01-01', '2026-01-31'))]:
            with self.subTest(publication=publication):
                p = packet('partial-date')
                p['existing_evidence'] = [{'id': 'old', 'url': 'https://source.example/old',
                    'date': publication, 'excerpt': BODY, 'verified': True, 'sha256': 'fixture', 'local_archive': 'fixture.txt'}]
                with tempfile.TemporaryDirectory() as directory:
                    result = vp.run_job(p, Path(directory), FakeLLM(note_publication_date=None), FakeExa())
                self.assertEqual(result['assessment']['verdict'], '正确')
                candidate = result['evidence_candidates'][0]
                self.assertEqual(candidate['published_date'], publication)
                self.assertEqual(tuple(candidate['publication_date_range'][k] for k in ('earliest', 'latest')), expected)

    def test_partial_interval_crossing_cutoff_warns_without_replacing_the_verdict(self):
        for publication in ('2026', '2026-11'):
            with self.subTest(publication=publication):
                item, warnings = self.inspect(self.source(publication), note_date=publication)
                self.assertEqual(item['verdict'], '正确')
                self.assertTrue(any(warning['code'] == 'publication_date_range_overlaps_cutoff'
                                    and warning['blocks_verdict'] is False for warning in warnings))
        item, _ = self.inspect(self.source('2026-11', retrieved='2026-11-08T00:00:00+00:00'), note_date='2026-11')
        self.assertEqual(item['verdict'], '正确')
        self.assertEqual(item['evidence_notes'][0]['source_availability']['status'], 'available')

    def test_unknown_background_alone_does_not_override_dated_material(self):
        item = assessment('a', 'dated')
        item['evidence_notes'][0]['publication_date'] = '2026-01-01'
        item['evidence_ids'].append('background')
        item['evidence_notes'].append({'evidence_id': 'background', 'relation': 'background',
            'quote': 'Background only.', 'publication_date': None, 'observation_end': None, 'limitation': 'Not relied upon.'})
        sources = [self.source('2026-01-01') | {'id': 'dated'},
                   self.source(kind='previously_registered_excerpt') | {'id': 'background', 'text': 'Background only.'}]
        accepted, warnings = vp.inspect_assessment(item, sources, '2026-11-09')
        self.assertEqual(accepted['verdict'], '正确')
        self.assertTrue(warnings)

    def test_undated_support_counter_and_boundary_keep_the_verdict_with_a_warning(self):
        for relation in ('support', 'counter', 'boundary'):
            with self.subTest(relation=relation):
                item, warnings = self.inspect(self.source(), relation=relation)
                self.assertEqual(item['verdict'], '正确')
                self.assertTrue(any(warning['code'] == 'publication_date_unconfirmed'
                                    and warning['blocks_verdict'] is False for warning in warnings))

    def test_explicit_future_publication_is_rejected_even_with_earlier_capture(self):
        for publication in ('2027', '2026-12', '2026-11-10'):
            with self.subTest(publication=publication), self.assertRaises(ValueError):
                self.inspect(self.source(publication, retrieved='2026-11-08T00:00:00+00:00'))

    def test_model_date_cannot_invent_precision_or_contradict_metadata(self):
        for publication, note in [('2026-01', '2026-01-01'), ('2025', '2025-05'), ('2026-01-02', '2026-01-01')]:
            with self.subTest(publication=publication, note=note), self.assertRaises(ValueError):
                self.inspect(self.source(publication), note_date=note)
        item, _ = self.inspect(self.source('2026-01-02'), note_date='2026-01')
        self.assertEqual(item['verdict'], '正确')

    def test_model_date_without_source_metadata_stays_a_warning(self):
        item, warnings = self.inspect(self.source(), note_date='2026-01-01')
        self.assertEqual(item['verdict'], '正确')
        self.assertEqual(item['evidence_notes'][0]['publication_date_status'], 'unconfirmed_by_source_metadata')
        self.assertTrue(any(warning['code'] == 'model_publication_date_not_verified'
                            and warning['blocks_verdict'] is False for warning in warnings))

    def test_capture_never_replaces_observation_or_publication_fields(self):
        item, _ = self.inspect(self.source(retrieved='2026-11-08T00:00:00+00:00'))
        self.assertIsNone(item['evidence_notes'][0]['publication_date'])
        self.assertEqual(item['evidence_notes'][0]['observation_end'], '2025-12-31')
        self.assertEqual(item['observation_end'], '2025-12-31')

    def test_future_observation_is_still_rejected(self):
        item = assessment('a', 's')
        item['evidence_notes'][0].update(publication_date=None, observation_end='2027-01-01')
        with self.assertRaisesRegex(ValueError, 'evidence_date_after_cutoff_or_invalid'):
            vp.inspect_assessment(item, [self.source(retrieved='2026-11-08T00:00:00+00:00')], '2026-11-09')


if __name__ == '__main__':
    unittest.main()
