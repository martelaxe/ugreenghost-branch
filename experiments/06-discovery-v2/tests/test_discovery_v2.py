import json
import sys
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT / 'experiments/06-discovery-v2/implementation'))
from discovery_v2 import adapt_exp05, classify, investigate, inventory, match_evidence
from handoff_simulation import run_mock_handoffs


def sample():
    sources = {'need.txt': 'Residents asked for a small growing activity.',
               'asset.txt': 'The studio holds a reusable illustration.',
               'rights.txt': 'External sharing is prohibited without written consent.'}
    candidate = {'id': 'x', 'discovery': 'Explore an activity using the illustration.', 'why_matters': 'It may help residents.',
                 'claims': [{'id': 'need', 'text': 'Residents asked for an activity.', 'material': True},
                            {'id': 'asset', 'text': 'A reusable illustration exists.', 'material': True}],
                 'evidence': [{'id': 'e1', 'claim_id': 'need', 'path': 'need.txt', 'excerpt': sources['need.txt'], 'relation': 'supports'},
                              {'id': 'e2', 'claim_id': 'asset', 'path': 'asset.txt', 'excerpt': sources['asset.txt'], 'relation': 'supports'}],
                 'reported_blocker': '', 'original_next_action': 'Share the material.'}
    review = {'candidate_id': 'x', 'disposition': 'SUPPORTED', 'explanation': 'Both claims have matching sources.',
              'assessments': {'e1': 'supports', 'e2': 'supports'}, 'blockers': [], 'blocker_search_complete': True}
    return sources, candidate, review, {'critical_unknown': False}


class DiscoveryV2Tests(unittest.TestCase):
    def test_h_a1_empty_verifier_retains_real_candidate_and_evidence(self):
        raw = json.loads((PROJECT / 'experiments/05-intelligence-multiplier/execution/a-h1/candidate-message.md').read_text())['findings'][0]
        c = adapt_exp05(raw, 1)
        sources, coverage = inventory(PROJECT / 'experiments/05-intelligence-multiplier/datasets/a')
        result = investigate([c], sources, coverage, json.loads((PROJECT / 'experiments/05-intelligence-multiplier/execution/a-h1/verifier-message.md').read_text())['findings'])
        row = result['candidates'][0]
        self.assertEqual(row['state'], 'NEEDS VERIFICATION')
        self.assertEqual(row['candidate']['original_candidate'], raw)
        self.assertEqual(len(row['evidence']), len(raw['citations']))
        self.assertTrue(all(e['exact_match'] for e in row['evidence']))
        self.assertIn('No valid per-candidate verification', row['explanation'])

    def test_h_b1_empty_verifier_retains_uncited_blocker_and_never_recommends_distribution(self):
        raw = json.loads((PROJECT / 'experiments/05-intelligence-multiplier/execution/b-h1/candidate-message.md').read_text())['findings'][0]
        c = adapt_exp05(raw, 1)
        sources, coverage = inventory(PROJECT / 'experiments/05-intelligence-multiplier/datasets/b')
        row = investigate([c], sources, coverage, [], 'completed')['candidates'][0]
        self.assertEqual(row['state'], 'NEEDS VERIFICATION')
        self.assertIn('separate written', row['unverified_blocker'])
        self.assertEqual(row['candidate']['original_candidate'], raw)
        self.assertNotIn('distribute', row['safe_next_action'].lower())
        self.assertFalse(any(e.get('path') == '04-rights/lot-disposition.txt' for e in row['evidence']))

    def test_h_b2_uncited_decisive_blocker_cannot_be_supported(self):
        raw = json.loads((PROJECT / 'experiments/05-intelligence-multiplier/execution/b-h2/verifier-message.md').read_text())['findings'][0]
        c = adapt_exp05(raw, 1)
        sources, coverage = inventory(PROJECT / 'experiments/05-intelligence-multiplier/datasets/b')
        review = {'candidate_id': c['id'], 'disposition': 'SUPPORTED', 'explanation': 'Simulated positive review.', 'assessments': {e['id']: 'supports' for e in c['evidence']}, 'blockers': [], 'blocker_search_complete': True}
        row = investigate([c], sources, coverage, [review])['candidates'][0]
        self.assertEqual(row['state'], 'NEEDS VERIFICATION')
        self.assertIn('blocker', row['explanation'])
        self.assertIn('committee approval', row['unverified_blocker'])

    def test_h_b1_a_later_review_can_attach_real_rights_source_without_changing_candidate(self):
        raw = json.loads((PROJECT / 'experiments/05-intelligence-multiplier/execution/b-h1/candidate-message.md').read_text())['findings'][0]
        c=adapt_exp05(raw,1); sources,coverage=inventory(PROJECT / 'experiments/05-intelligence-multiplier/datasets/b')
        path='04-rights/lot-disposition.txt'
        excerpt='The cooperative prohibits sharing BX19 outside the organization without the garden committee’s separate written approval, including non-commercial samples.'
        review={'candidate_id':c['id'],'disposition':'BLOCKED','explanation':'The sharing restriction is documented.',
                'assessments':{'rights-proof':'supports'},'blockers':[{'claim_id':'sharing-restriction','evidence_id':'rights-proof','text':'External sharing requires written committee approval.'}],
                'additional_evidence':[{'id':'rights-proof','claim_id':'sharing-restriction','path':path,'excerpt':excerpt,'relation':'supports'}]}
        result=investigate([c],sources,coverage,[review])
        self.assertEqual(result['candidates'][0]['state'],'BLOCKED')
        self.assertEqual(result['candidates'][0]['blockers'][0]['path'],path)
        self.assertEqual(result['candidates'][0]['candidate']['original_candidate'],raw)
        added=[e for e in result['candidates'][0]['evidence'] if e.get('id')=='rights-proof'][0]
        self.assertTrue(added['exact_match'])
        self.assertEqual(added['origin'],'review')

    def test_unretrieved_review_evidence_cannot_prove_blocker(self):
        sources,c,review,coverage=sample()
        review['additional_evidence']=[{'id':'e3','claim_id':'restriction','path':'unknown.txt','excerpt':'No external sharing.','relation':'supports'}]
        review['assessments']['e3']='supports'
        review['blockers']=[{'claim_id':'restriction','evidence_id':'e3','text':'No external sharing.'}]
        row=investigate([c],sources,coverage,[review])['candidates'][0]
        self.assertEqual(row['state'],'NEEDS VERIFICATION')
        self.assertFalse(next(e for e in row['evidence'] if e['id']=='e3')['retrieved'])

    def test_supported_opportunity_requires_explicit_semantics_and_retrieved_sources(self):
        sources,c,review,coverage = sample()
        row = investigate([c],sources,coverage,[review])['candidates'][0]
        self.assertEqual(row['state'],'SUPPORTED')
        self.assertEqual(len(row['evidence']),2)
        self.assertTrue(all(e['retrieved'] and e['exact_match'] for e in row['evidence']))
        self.assertIn('authorize',row['safe_next_action'])

    def test_restriction_is_blocked_only_with_verified_source(self):
        sources,c,review,coverage=sample()
        c['evidence'].append({'id':'e3','claim_id':'restriction','path':'rights.txt','excerpt':sources['rights.txt'],'relation':'supports'})
        review['assessments']['e3']='supports'
        review['blockers']=[{'claim_id':'restriction','evidence_id':'e3','text':'External sharing requires written consent.'}]
        row=investigate([c],sources,coverage,[review])['candidates'][0]
        self.assertEqual(row['state'],'BLOCKED')
        self.assertEqual(row['blockers'][0]['path'],'rights.txt')
        self.assertEqual(row['blockers'][0]['excerpt'],sources['rights.txt'])
        self.assertIn('Do not take the blocked action',row['safe_next_action'])

    def test_sourced_blocker_is_reported_even_if_candidate_context_is_incomplete(self):
        sources,c,review,coverage=sample()
        c['evidence']=[{'id':'e3','claim_id':'restriction','path':'rights.txt','excerpt':sources['rights.txt'],'relation':'supports'}]
        review['assessments']={'e3':'supports'}
        review['blockers']=[{'claim_id':'restriction','evidence_id':'e3','text':'External sharing requires written consent.'}]
        row=investigate([c],sources,coverage,[review])['candidates'][0]
        self.assertEqual(row['state'],'BLOCKED')
        self.assertEqual(row['blockers'][0]['path'],'rights.txt')
        self.assertIn('Do not take the blocked action',row['safe_next_action'])

    def test_uncited_blocker_is_unverified_not_supported(self):
        sources,c,review,coverage=sample()
        review['blockers']=[{'claim_id':'restriction','evidence_id':'missing','text':'External sharing is restricted.'}]
        row=investigate([c],sources,coverage,[review])['candidates'][0]
        self.assertEqual(row['state'],'NEEDS VERIFICATION')
        self.assertIn('lacks retrieved source',row['explanation'])

    def test_negative_control_does_not_invent_candidate(self):
        sources,c,review,coverage=sample()
        out=investigate([],sources,coverage,[])
        self.assertEqual(out['candidates'],[])
        self.assertIn('No meaningful discovery',out['empty_message'])

    def test_missing_essential_source_is_not_supported(self):
        sources,c,review,coverage=sample();del sources['asset.txt']
        row=investigate([c],sources,coverage,[review])['candidates'][0]
        self.assertEqual(row['state'],'INSUFFICIENT EVIDENCE')
        self.assertFalse(row['evidence'][1]['retrieved'])
        self.assertEqual(row['candidate'],c)

    def test_truncated_or_unknown_coverage_prevents_supported(self):
        sources,c,review,coverage=sample();coverage['critical_unknown']=True
        row=investigate([c],sources,coverage,[review])['candidates'][0]
        self.assertEqual(row['state'],'NEEDS VERIFICATION')
        self.assertIn('Coverage',row['explanation'])

    def test_expert_failure_cancellation_and_approval_wait_are_not_success(self):
        sources,c,review,coverage=sample()
        for state in ('failed','cancelled','waiting_user','waiting_approval'):
            with self.subTest(state=state):
                row=investigate([c],sources,coverage,[review],state)['candidates'][0]
                self.assertEqual(row['state'],'NEEDS VERIFICATION')
                self.assertIn(state,row['explanation'])
                self.assertEqual(row['candidate'],c)

    def test_missing_blocker_review_cannot_be_supported(self):
        sources,c,review,coverage=sample();review.pop('blocker_search_complete')
        row=investigate([c],sources,coverage,[review])['candidates'][0]
        self.assertEqual(row['state'],'NEEDS VERIFICATION')
        self.assertIn('blocker review',row['explanation'])

    def test_duplicate_material_claim_ids_cannot_be_supported(self):
        sources,c,review,coverage=sample();c['claims'].append({'id':'need','text':'Another claim','material':True})
        row=investigate([c],sources,coverage,[review])['candidates'][0]
        self.assertEqual(row['state'],'NEEDS VERIFICATION')

    def test_review_missing_disposition_cannot_produce_supported(self):
        sources,c,review,coverage=sample();review.pop('disposition')
        row=investigate([c],sources,coverage,[review])['candidates'][0]
        self.assertEqual(row['state'],'NEEDS VERIFICATION')
        self.assertIn('structured disposition',row['explanation'])

    def test_duplicate_review_does_not_select_one_silently(self):
        sources,c,review,coverage=sample()
        row=investigate([c],sources,coverage,[review,deepcopy(review)])['candidates'][0]
        self.assertEqual(row['state'],'NEEDS VERIFICATION')

    def test_exact_match_is_not_semantic_verification(self):
        sources,c,review,coverage=sample();review['assessments']={}
        row=investigate([c],sources,coverage,[review])['candidates'][0]
        self.assertEqual(row['state'],'NEEDS VERIFICATION')
        self.assertTrue(all(e['exact_match'] for e in row['evidence']))

    def test_fabricated_quote_does_not_supply_context(self):
        sources,c,review,coverage=sample();c['evidence'][0]['excerpt']='An invented quote with grant funding.'
        row=investigate([c],sources,coverage,[review])['candidates'][0]
        self.assertEqual(row['state'],'INSUFFICIENT EVIDENCE')
        self.assertFalse(row['evidence'][0]['exact_match'])

    def test_related_evidence_does_not_prove_material_claim(self):
        sources,c,review,coverage=sample();c['evidence'][0]['relation']='related'
        row=investigate([c],sources,coverage,[review])['candidates'][0]
        self.assertEqual(row['state'],'NEEDS VERIFICATION')

    def test_rejected_requires_a_sourced_reviewed_contradiction(self):
        sources,c,review,coverage=sample()
        c['evidence'][0]['relation']='contradicts';review['assessments']['e1']='contradicts';review['disposition']='REJECTED'
        row=investigate([c],sources,coverage,[review])['candidates'][0]
        self.assertEqual(row['state'],'REJECTED')
        self.assertEqual(row['candidate'],c)
        review['assessments']['e1']='unknown'
        row=investigate([c],sources,coverage,[review])['candidates'][0]
        self.assertEqual(row['state'],'NEEDS VERIFICATION')

    def test_invalid_or_wrong_candidate_verification_does_not_discard(self):
        sources,c,review,coverage=sample();review['candidate_id']='someone-else'
        row=investigate([c],sources,coverage,[review])['candidates'][0]
        self.assertEqual(row['state'],'NEEDS VERIFICATION')
        self.assertEqual(row['candidate'],c)

    def test_inventory_measures_selection_and_referenced_missing_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/'a.txt').write_text('See plan-2025.pdf for figures.');(root/'b.md').write_text('A complete note.')
            docs,cov=inventory(root)
            self.assertEqual(cov['counts'],{'discovered':2,'selected':2,'read':2})
            self.assertEqual(cov['referenced_missing_names'],['plan-2025.pdf'])
            self.assertTrue(cov['critical_unknown'])
            self.assertEqual(len(docs),2)

    def test_inventory_truncation_and_unselected_file_are_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/'a.txt').write_text('abcdefghijk');(root/'b.txt').write_text('short')
            docs,cov=inventory(root,selected=['a.txt'],max_bytes=5)
            self.assertEqual(docs['a.txt'],'abcde')
            self.assertEqual(cov['truncated_paths'],['a.txt'])
            self.assertEqual(cov['counts'],{'discovered':2,'selected':1,'read':1})
            self.assertTrue(cov['critical_unknown'])

    def test_exp05_missing_reference_is_observed_not_fabricated(self):
        _,cov=inventory(PROJECT / 'experiments/05-intelligence-multiplier/datasets/a')
        self.assertEqual(cov['counts'],{'discovered':44,'selected':44,'read':44})
        self.assertIn('sleeve-sizes-2025.pdf',cov['referenced_missing_names'])
        self.assertTrue(cov['critical_unknown'])

    def test_mock_expert_handoffs_preserve_exact_source_references(self):
        sources,c,review,_=sample()
        file_result={'status':'completed','paths':['need.txt','asset.txt'],'coverage_complete':True}
        document_result={'status':'completed','documents':[{'path':'need.txt','text':sources['need.txt'],'complete':True},{'path':'asset.txt','text':sources['asset.txt'],'complete':True}],'coverage_complete':True}
        knowledge_result={'status':'completed','reviews':[review],'coverage_complete':True}
        result=run_mock_handoffs(file_result,document_result,knowledge_result,[c])
        self.assertEqual(result['calls'],['file-agent','document-agent','knowledge-agent'])
        self.assertEqual(result['candidates'][0]['state'],'SUPPORTED')
        self.assertEqual({e['path'] for e in result['candidates'][0]['evidence']},{'need.txt','asset.txt'})
        self.assertTrue(all(e['exact_match'] for e in result['candidates'][0]['evidence']))
        self.assertIn('not real UGREEN',result['handoff_notice'])

    def test_mock_handoff_stops_on_document_failure(self):
        sources,c,review,_=sample()
        result=run_mock_handoffs({'status':'completed','paths':['need.txt','asset.txt'],'coverage_complete':True},{'status':'failed'},{'status':'completed','reviews':[review],'coverage_complete':True},[c])
        self.assertEqual(result['calls'],['file-agent','document-agent'])
        self.assertEqual(result['candidates'][0]['state'],'INSUFFICIENT EVIDENCE')
        self.assertEqual(result['coverage']['failed'][0]['status'],'failed')

    def test_mock_handoff_incomplete_documents_stop_dependent_knowledge(self):
        sources,c,review,_=sample()
        file_result={'status':'completed','paths':['need.txt','asset.txt'],'coverage_complete':True}
        document_result={'status':'completed','documents':[{'path':'need.txt','text':sources['need.txt'],'complete':True},{'path':'asset.txt','text':sources['asset.txt'],'complete':False}],'coverage_complete':False}
        result=run_mock_handoffs(file_result,document_result,{'status':'completed','reviews':[review],'coverage_complete':True},[c])
        self.assertEqual(result['calls'],['file-agent','document-agent'])
        self.assertIn('asset.txt',result['coverage']['truncated_paths'])
        self.assertEqual(result['candidates'][0]['state'],'INSUFFICIENT EVIDENCE')

    def test_mock_handoff_pending_keeps_completed_document_sources(self):
        sources,c,review,_=sample()
        file_result={'status':'completed','paths':['need.txt','asset.txt'],'coverage_complete':True}
        document_result={'status':'completed','documents':[{'path':p,'text':sources[p],'complete':True} for p in ('need.txt','asset.txt')],'coverage_complete':True}
        result=run_mock_handoffs(file_result,document_result,{'status':'waiting_approval'},[c])
        self.assertEqual(result['candidates'][0]['state'],'NEEDS VERIFICATION')
        self.assertTrue(all(e['exact_match'] for e in result['candidates'][0]['evidence']))
        self.assertIn('waiting_approval',result['candidates'][0]['explanation'])

    def test_no_candidate_input_mutation(self):
        sources,c,review,coverage=sample();original=deepcopy(c)
        out=investigate([c],sources,coverage,[review]);out['candidates'][0]['candidate']['discovery']='changed'
        self.assertEqual(c,original)

    def test_blocked_report_does_not_expose_original_action_as_recommendation(self):
        sources,c,review,coverage=sample()
        c['original_next_action']='Immediately share the material without consent.'
        c['evidence'].append({'id':'e3','claim_id':'restriction','path':'rights.txt','excerpt':sources['rights.txt'],'relation':'supports'})
        review['assessments']['e3']='supports'
        review['blockers']=[{'claim_id':'restriction','evidence_id':'e3','text':'External sharing requires written consent.'}]
        out=investigate([c],sources,coverage,[review])
        self.assertEqual(out['user_facing'][0]['state'],'BLOCKED')
        self.assertNotIn('Immediately share',str(out['user_facing']))
        self.assertIn('Immediately share',out['candidates'][0]['candidate']['original_next_action'])

    def test_no_more_than_three_user_facing_candidates(self):
        sources,c,review,coverage=sample();items=[];reviews=[]
        for i in range(5):
            x=deepcopy(c);x['id']=str(i);items.append(x);y=deepcopy(review);y['candidate_id']=str(i);reviews.append(y)
        out=investigate(items,sources,coverage,reviews)
        self.assertEqual(len(out['candidates']),5)
        self.assertEqual(len(out['user_facing']),3)


if __name__ == '__main__': unittest.main(verbosity=2)
