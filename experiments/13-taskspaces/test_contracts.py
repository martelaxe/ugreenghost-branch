"""Local, deterministic test fixtures, not UGREEN response handling."""
import unittest,json,hashlib,re
from pathlib import Path
R=Path(__file__).resolve().parent
# Local event vocabulary, not a UGREEN expert envelope.
def save_disposition(user_approved,platform_approved,operation,readback):
 if not user_approved or not platform_approved:return 'not-authorized'
 if operation=='pending':return 'pending'
 if operation in {'failed','cancelled'}:return operation
 if operation!='completed':return 'unknown'
 return 'verified' if readback=='match' else 'unverified'
def coverage(limited,inaccessible):return 'incomplete' if limited or inaccessible else 'unknown-unless-proven'
def grouping(candidates):return candidates[0] if len(candidates)==1 else 'ask-or-preserve-ambiguity'
class Tests(unittest.TestCase):
 def test_limited_is_incomplete(self):self.assertEqual(coverage(True,False),'incomplete')
 def test_access_failure_is_incomplete(self):self.assertEqual(coverage(False,True),'incomplete')
 def test_no_false_coverage_complete(self):self.assertEqual(coverage(False,False),'unknown-unless-proven')
 def test_multiple_categories_are_ambiguous(self):self.assertEqual(grouping(['personal','business']),'ask-or-preserve-ambiguity')
 def test_no_user_approval(self):self.assertEqual(save_disposition(False,True,'completed','match'),'not-authorized')
 def test_no_platform_approval(self):self.assertEqual(save_disposition(True,False,'completed','match'),'not-authorized')
 def test_pending_not_complete(self):self.assertEqual(save_disposition(True,True,'pending','match'),'pending')
 def test_completed_without_readback_is_unverified(self):self.assertEqual(save_disposition(True,True,'completed','failed'),'unverified')
 def test_failed_never_verified(self):self.assertEqual(save_disposition(True,True,'failed','match'),'failed')
 def test_completed_with_readback(self):self.assertEqual(save_disposition(True,True,'completed','match'),'verified')
 def test_links_resolve(self):
  j=json.loads((R/'citation-audit.json').read_text());self.assertEqual(len(j),15);self.assertTrue(all(not x['broken_links'] for x in j))
 def test_sources_unchanged(self):
  j=json.loads((R/'citation-audit.json').read_text());self.assertTrue(all(x['source_fixture_unchanged'] for x in j))
if __name__=='__main__':unittest.main(verbosity=2)
