import unittest,tempfile,os,hashlib
from pathlib import Path

def copy(src,dst,*,owner,gateway,expected,fail_readback=False):
 if not owner or not gateway:return 'awaiting approval'
 if not src.is_file() or not dst.parent.is_dir():return 'blocked'
 if hashlib.sha256(src.read_bytes()).hexdigest()!=expected:return 'source changed'
 try:
  fd=os.open(dst,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600)
 except FileExistsError:return 'collision'
 with os.fdopen(fd,'wb') as f:f.write(src.read_bytes())
 if fail_readback:return 'unverified'
 return 'verified' if hashlib.sha256(dst.read_bytes()).hexdigest()==expected and hashlib.sha256(src.read_bytes()).hexdigest()==expected else 'unverified'
class Cases(unittest.TestCase):
 def setUp(self):
  self.t=tempfile.TemporaryDirectory();self.p=Path(self.t.name);self.src=self.p/'source';self.dst=self.p/'dest';self.src.write_text('test source');self.h=hashlib.sha256(self.src.read_bytes()).hexdigest()
 def tearDown(self):self.t.cleanup()
 def c(self,**kw):
  d={'owner':True,'gateway':True,'expected':self.h};d.update(kw);return copy(self.src,self.dst,**d)
 def test_success_and_preservation(self):self.assertEqual(self.c(),'verified');self.assertEqual(self.src.read_text(),'test source');self.assertEqual(self.dst.read_text(),'test source')
 def test_owner_pending(self):self.assertEqual(self.c(owner=False),'awaiting approval');self.assertFalse(self.dst.exists())
 def test_gateway_pending(self):self.assertEqual(self.c(gateway=False),'awaiting approval');self.assertFalse(self.dst.exists())
 def test_collision(self):self.dst.write_text('existing');self.assertEqual(self.c(),'collision');self.assertEqual(self.dst.read_text(),'existing')
 def test_changed_source(self):self.src.write_text('changed');self.assertEqual(self.c(),'source changed');self.assertFalse(self.dst.exists())
 def test_failed_verification(self):self.assertEqual(self.c(fail_readback=True),'unverified');self.assertTrue(self.dst.exists())
 def test_missing_parent(self):self.dst=self.p/'missing'/'dest';self.assertEqual(self.c(),'blocked');self.assertFalse(self.dst.exists())
if __name__=='__main__':unittest.main(verbosity=2)
