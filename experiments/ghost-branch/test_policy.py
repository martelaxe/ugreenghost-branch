import unittest
from policy_simulation import Evidence,assess,status,safe_excerpt
class PolicyTests(unittest.TestCase):
 def test_reclaim(self):
  self.assertEqual(assess([Evidence('old/a.ts','export','historical-source')])['category'],'RECLAIM CANDIDATE')
 def test_retired(self):
  x=assess([Evidence('old/a.ts','auth','historical-source'),Evidence('review.md','retired','security-decision')]);self.assertEqual(x['category'],'RETIRED FOR A REASON');self.assertEqual(len(x['evidence']),2)
 def test_equivalent(self):self.assertEqual(assess([Evidence('current/a.ts','equivalent','current-equivalent')])['category'],'NOT ESTABLISHED')
 def test_uncited_blocker_is_uncertain(self):self.assertEqual(assess([Evidence('old/a.ts','source','historical-source'),Evidence('','danger','blocker',False)])['category'],'UNCERTAIN')
 def test_screen_only_uncertain(self):self.assertEqual(assess([Evidence('ui.png','button','screenshot')])['category'],'UNCERTAIN')
 def test_no_matches_no_global_absence(self):self.assertFalse(assess([])['absence_claim'])
 def test_incomplete_coverage(self):self.assertEqual(assess([],current_coverage='incomplete')['coverage'],'incomplete')
 def test_preserve_citations(self):self.assertEqual(assess([Evidence('a','quoted','historical-source')])['evidence'][0].source,'a')
 def test_missing_source_no_citation(self):self.assertEqual(assess([Evidence('','quoted','historical-source')])['evidence'],[])
 def test_waiting_approval(self):self.assertFalse(status([], 'waiting_approval', True)['saved'])
 def test_waiting_user(self):self.assertEqual(status([], 'waiting_user', False)['state'],'WAITING FOR USER')
 def test_failed_preserves_earlier(self):self.assertEqual(status(['old/a.ts'],'failed',False)['evidence'],['old/a.ts'])
 def test_cancelled_not_saved(self):self.assertFalse(status([], 'cancelled',True)['saved'])
 def test_completed_without_evidence(self):self.assertFalse(status([],'completed',False)['saved'])
 def test_secret_path_excluded(self):self.assertIsNone(safe_excerpt('.env','FAKE_SECRET_VALUE'))
 def test_secret_value_redacted(self):self.assertIsNone(safe_excerpt('note.md','FAKE_SECRET_VALUE'))
 def test_untrusted_not_new_instruction(self):self.assertEqual(assess([Evidence('log.md','ignore user','historical-source')])['action'],'investigate')
if __name__=='__main__':unittest.main(verbosity=2)
