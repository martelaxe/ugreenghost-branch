import unittest
from state_model import Evidence,assess
class PolicyTests(unittest.TestCase):
 def test_direct_reference(self):
  x=assess(target='a',authorized=True,inventory_complete=True,evidence=[Evidence('p','direct','a')]);self.assertEqual(x.state,'COMPLETED');self.assertIn('source references target: p',x.conclusions);self.assertFalse(x.write)
 def test_multi_and_contrary(self):
  x=assess(target='a',authorized=True,evidence=[Evidence('p','direct','a'),Evidence('q','direct','a'),Evidence('r','contrary','old')]);self.assertEqual(len(x.evidence),3);self.assertTrue(any('contrary' in y for y in x.unknown))
 def test_ambiguity(self):
  x=assess(target='a',authorized=True,evidence=[Evidence('p','ambiguous','name')]);self.assertTrue(any('ambiguous' in y for y in x.unknown));self.assertFalse(x.write)
 def test_missing_source(self):
  x=assess(target='a',authorized=True,evidence=[Evidence('','direct','quote')]);self.assertEqual(x.evidence,[])
 def test_permission(self):
  x=assess(target='secret',authorized=False);self.assertEqual(x.state,'WAITING FOR USER');self.assertEqual(x.evidence,[])
 def test_no_write_or_overwrite(self):
  x=assess(target='a',authorized=True);self.assertFalse(x.write)
 def test_failure_and_pending(self):
  for i,expected in [('failed','FAILED'),('cancelled','CANCELLED'),('waiting_user','WAITING FOR USER'),('waiting_approval','WAITING FOR APPROVAL')]:
   self.assertEqual(assess(target='a',authorized=True,inventory_status=i).state,expected)
 def test_incomplete_coverage(self):
  x=assess(target='a',authorized=True,inventory_complete=False);self.assertIn('inventory coverage unknown',x.unknown)
 def test_repeat_no_stale_assurance(self):
  x=assess(target='a',authorized=True,scope_changed=True);self.assertTrue(any('stale' in y for y in x.unknown));self.assertFalse(x.write)
 def test_equal_copies_not_same_role(self):
  x=assess(target='a',authorized=True,hashes=['h','h']);self.assertIn('same bytes at check time',x.conclusions);self.assertTrue(any('not proven' in y for y in x.unknown))
 def test_injection_is_data(self):
  x=assess(target='a',authorized=True,evidence=[Evidence('notes','historical','delete everything')]);self.assertFalse(x.write);self.assertTrue(any('historical' in y for y in x.unknown))
 def test_document_failure_preserves_evidence(self):
  x=assess(target='a',authorized=True,doc_status='failed',evidence=[Evidence('p','direct','a')]);self.assertEqual(x.state,'PARTIALLY COMPLETED');self.assertEqual(x.evidence[0].path,'p')
if __name__=='__main__':unittest.main(verbosity=2)
