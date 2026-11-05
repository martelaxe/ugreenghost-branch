import copy
import unittest

from mock_workflow import FILES, FAILED_LASER, SCOPE, fake_scenario, run


class EvidenceWorkflowTests(unittest.TestCase):
    def test_supported_discovery_cites_only_exact_fixture_evidence(self):
        result = run(fake_scenario('supported_discovery'))
        self.assertEqual(result['disposition'], 'hypothesis')
        self.assertEqual(len(result['evidence']), 5)
        for citation in result['evidence']:
            self.assertIn(citation['quote'], FILES[citation['path']])
        self.assertIn('untested', result['uncertainty'][0])
        self.assertIn('manager', result['safe_next_action'])
        self.assertEqual(result['critical_blockers'], [])
        self.assertIn('mock_scope', result['coverage']['status'])

    def test_blocker_changes_action_and_quotes_source(self):
        result = run(fake_scenario('critical_blocker'))
        self.assertEqual(result['disposition'], 'blocked')
        self.assertEqual(result['critical_blockers'][0]['quote'], FAILED_LASER)
        self.assertEqual(result['critical_blockers'][0]['path'], f'{SCOPE}/equipment.txt')
        self.assertIn('Do not operate L-2', result['safe_next_action'])
        self.assertIn('repair and clearance', result['safe_next_action'])

    def test_missing_essential_source_never_becomes_hypothesis(self):
        result = run(fake_scenario('missing_source'))
        self.assertEqual(result['disposition'], 'incomplete')
        self.assertIsNone(result['discovery'])
        self.assertIn('asset_rights', result['missing_roles'])
        self.assertNotIn(f'{SCOPE}/archive.txt', [e['path'] for e in result['evidence']])
        self.assertNotIn('bounded internal prototype', result['safe_next_action'])

    def test_truncated_content_stops_dependent_expert_and_preserves_partial_sources(self):
        result = run(fake_scenario('truncated_evidence'))
        self.assertEqual(result['disposition'], 'incomplete')
        self.assertIn('content incomplete', result['coverage']['details'])
        self.assertIn(f'{SCOPE}/archive.txt', result['coverage']['details'])
        self.assertNotIn('knowledge-agent', result['expert_states'])
        self.assertTrue(result['evidence'])
        self.assertNotIn(f'{SCOPE}/archive.txt', [e['path'] for e in result['evidence']])

    def test_failed_expert_stops_processing_and_reports_failure(self):
        result = run(fake_scenario('expert_failure'))
        self.assertEqual(result['disposition'], 'incomplete')
        self.assertIn('document-agent: failed', result['coverage']['details'])
        self.assertEqual(result['expert_states'], ['file-agent', 'document-agent'])
        self.assertIsNone(result['discovery'])

    def test_pending_approval_is_not_treated_as_completed(self):
        result = run(fake_scenario('approval_pending'))
        self.assertEqual(result['disposition'], 'incomplete')
        self.assertIn('waiting_approval', result['coverage']['details'])
        self.assertTrue(result['evidence'])
        self.assertIsNone(result['discovery'])

    def test_pending_stage_preserves_blocker_from_completed_document(self):
        f = fake_scenario('critical_blocker')
        f['knowledge-agent'] = {'status': 'waiting_approval', 'result': None}
        result = run(f)
        self.assertEqual(result['disposition'], 'incomplete')
        self.assertEqual(result['critical_blockers'][0]['quote'], FAILED_LASER)
        self.assertIn('waiting_approval', result['coverage']['details'])

    def test_incomplete_result_does_not_assert_no_blockers(self):
        result = run(fake_scenario('expert_failure'))
        self.assertIsNone(result['critical_blockers'])
        self.assertIn('not been comprehensively assessed', result['uncertainty'][1])

    def test_unknown_inventory_coverage_cannot_produce_a_hypothesis(self):
        f = fake_scenario('supported_discovery')
        del f['file-agent']['result']['data']['coverage']['complete']
        result = run(f)
        self.assertEqual(result['disposition'], 'incomplete')
        self.assertEqual(result['expert_states'], ['file-agent'])

    def test_null_coverage_remains_unknown(self):
        f = fake_scenario('supported_discovery')
        f['document-agent']['result']['data']['coverage'] = None
        result = run(f)
        self.assertEqual(result['disposition'], 'incomplete')
        self.assertIn('incomplete or unknown coverage', result['coverage']['details'])

    def test_path_traversal_is_outside_scope(self):
        f = fake_scenario('supported_discovery')
        f['file-agent']['result']['data']['paths'].append(SCOPE + '/../secret.txt')
        result = run(f)
        self.assertEqual(result['disposition'], 'incomplete')
        self.assertEqual(result['expert_states'], ['file-agent'])

    def test_cancelled_expert_stops_processing(self):
        f = fake_scenario('supported_discovery')
        f['document-agent'] = {'status': 'cancelled', 'result': None}
        result = run(f)
        self.assertEqual(result['disposition'], 'incomplete')
        self.assertIn('document-agent: cancelled', result['coverage']['details'])
        self.assertEqual(result['expert_states'], ['file-agent', 'document-agent'])

    def test_fabricated_citation_is_rejected(self):
        f = fake_scenario('supported_discovery')
        f['knowledge-agent']['result']['data']['evidence'][0]['quote'] = 'The studio has already received a grant.'
        result = run(f)
        self.assertEqual(result['disposition'], 'incomplete')
        self.assertIn('unverified', result['coverage']['details'])
        self.assertIsNone(result['discovery'])

    def test_discovered_but_unread_file_cannot_be_silently_skipped(self):
        f = fake_scenario('supported_discovery')
        f['document-agent']['result']['data']['documents'].pop()
        result = run(f)
        self.assertEqual(result['disposition'], 'incomplete')
        self.assertIn('incomplete or unknown coverage', result['coverage']['details'])
        self.assertNotIn('knowledge-agent', result['expert_states'])

    def test_unreported_but_obvious_blocker_stops_safe_recommendation(self):
        f = fake_scenario('critical_blocker')
        f['knowledge-agent']['result']['data']['blocker'] = None
        result = run(f)
        self.assertEqual(result['disposition'], 'incomplete')
        self.assertIn('contradicts', result['coverage']['details'])
        self.assertIsNone(result['discovery'])

    def test_out_of_scope_inventory_is_rejected(self):
        f = fake_scenario('supported_discovery')
        f['file-agent']['result']['data']['paths'].append('/outside/private.txt')
        result = run(f)
        self.assertEqual(result['disposition'], 'incomplete')
        self.assertEqual(result['expert_states'], ['file-agent'])

    def test_completed_status_without_successful_envelope_stops(self):
        f = fake_scenario('supported_discovery')
        f['document-agent']['result'] = {'ok': False, 'error': {'code': 'MOCK_FAILURE'}}
        result = run(f)
        self.assertEqual(result['disposition'], 'incomplete')
        self.assertIn('completed without a valid', result['coverage']['details'])
        self.assertNotIn('knowledge-agent', result['expert_states'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
