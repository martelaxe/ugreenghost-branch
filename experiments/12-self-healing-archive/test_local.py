import unittest,tempfile,shutil
from pathlib import Path
from local_demo import R,SRC,DST,EXPECTED,run_copy,snapshot
class TestAdapter(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name)/'fixture';shutil.copytree(R/'archive',self.root)
 def tearDown(self):self.tmp.cleanup()
 def test_success_copy_and_preserve(self):
  b=snapshot(self.root); r=run_copy(self.root,user_approval=True,gateway_approval=True); a=snapshot(self.root)
  self.assertEqual(r['status'],'verified');self.assertEqual(set(a)-set(b),{DST});self.assertTrue(all(a[k]==v for k,v in b.items()))
 def test_no_user_approval(self):self.assertEqual(run_copy(self.root,gateway_approval=True)['status'],'stopped')
 def test_no_gateway_approval(self):self.assertEqual(run_copy(self.root,user_approval=True)['status'],'stopped')
 def test_both_denied(self):self.assertFalse((self.root/DST).exists());self.assertEqual(run_copy(self.root)['status'],'stopped')
 def test_collision_preserved(self):
  p=self.root/DST;p.write_text('existing target');r=run_copy(self.root,user_approval=True,gateway_approval=True);self.assertEqual(p.read_text(),'existing target');self.assertEqual(r['status'],'stopped')
 def test_changed_source(self):
  (self.root/SRC).write_text('changed');self.assertEqual(run_copy(self.root,user_approval=True,gateway_approval=True)['status'],'stopped')
 def test_missing_source(self):
  (self.root/SRC).unlink();self.assertEqual(run_copy(self.root,user_approval=True,gateway_approval=True)['status'],'stopped')
 def test_write_failure(self):
  r=run_copy(self.root,user_approval=True,gateway_approval=True,fail_write=True);self.assertEqual(r['status'],'stopped');self.assertFalse((self.root/DST).exists())
 def test_verification_failure(self):
  r=run_copy(self.root,user_approval=True,gateway_approval=True,fail_verify=True);self.assertEqual(r['status'],'unverified');self.assertTrue(r['action_reported_completed']);self.assertTrue((self.root/DST).exists())
 def test_destination_parent_missing(self):
  shutil.rmtree(self.root/'projects/harbor/assets');self.assertEqual(run_copy(self.root,user_approval=True,gateway_approval=True)['status'],'stopped')
if __name__=='__main__':unittest.main(verbosity=2)
