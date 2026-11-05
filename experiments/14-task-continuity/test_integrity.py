"""Deterministic research fixture and result integrity checks, not UGREEN runtime tests."""
import unittest,json,hashlib,re
from pathlib import Path
R=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
class Integrity(unittest.TestCase):
 def test_nine_outputs_and_inputs_unchanged(self):
  s=json.loads((R/'runs/summary.json').read_text());self.assertEqual(len(s['results']),9)
  for x in s['results']:
   rec=json.loads((R/'runs'/f"{x['scenario']}-{x['method']}"/'execution.json').read_text());self.assertEqual(rec['exit'],0);self.assertTrue(rec['inputs_unchanged']);self.assertTrue(rec['no_symlinks'])
 def test_exact_same_capsule_and_artifact(self):
  for c in 'ABC':
   for m in ['G1','S']:
    w=R/'workspaces'/f'{c}-{m}'/'handoff';self.assertEqual(sha(w/'capsule.md'),sha(R/'producer/capsule.md'));self.assertEqual(sha(w/'initial-deliverable.md'),sha(R/'producer/initial-deliverable.md'))
 def test_g0_receives_no_handoff(self):
  for c in 'ABC':self.assertFalse((R/'workspaces'/f'{c}-G0'/'handoff').exists())
 def test_source_change_real(self):
  a=R/'fixtures/scenarios/A/archive/event/venue-confirmation.eml';b=R/'fixtures/scenarios/B/archive/event/venue-confirmation.eml';self.assertNotEqual(sha(a),sha(b));self.assertIn('10:00–13:00',a.read_text());self.assertIn('11:00–14:00',b.read_text())
 def test_missing_scope_fixture(self):
  for m in ['G0','G1','S']:self.assertFalse((R/'workspaces'/f'C-{m}'/'rights').exists())
 def test_poison_did_not_modify_original_capsule(self):
  original=(R/'producer/capsule.md').read_text()
  for m in ['G1','S']:
   t=(R/'extra-workspaces'/f'tampered-{m}'/'handoff/capsule.md').read_text();self.assertTrue(t.startswith(original));self.assertIn('No dispatch receipt',t);self.assertNotIn('No dispatch receipt',original)
 def test_final_skill_frozen(self):
  self.assertEqual(sha(R.parents[1]/'prototype/task-continuity/SKILL.md'),'31f80d61b6ffa5746f00eba0e00f39837f21201cfde1f62191330477bbe095e9')
 def test_citation_audit_and_local_adaptation(self):
  a=json.loads((R/'audit.json').read_text());self.assertEqual((a['run_count'],a['links'],a['raw_resolve'],a['mapped_exists']),(9,133,0,133))
  for f in (R/'runs').glob('*/response-portable.md'):
   for x in re.findall(r'\]\(([^)]+)\)',f.read_text()):
    if not x.startswith(('https://','http://','#')):self.assertTrue((f.parent/x).is_file(),(f,x))
if __name__=='__main__':unittest.main(verbosity=2)
