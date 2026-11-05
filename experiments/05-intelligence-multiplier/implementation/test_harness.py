import tempfile, unittest
from pathlib import Path
from harness import retrieve, verify_candidate, parse_model, PER_FILE

class HarnessTests(unittest.TestCase):
    def setUp(self):
        self.finding={'title':'candidate','hypothesis':'test','status':'investigate','citations':[{'path':'a.txt','quote':'long enough quote A'},{'path':'b.txt','quote':'long enough quote B'}],'uncertainty':'unknown','blocker':'unknown','next_action':'ask first'}
        self.sources={'a.txt':'prefix long enough quote A suffix','b.txt':'prefix long enough quote B suffix'}
    def test_valid_quotes(self):self.assertTrue(verify_candidate(self.finding,self.sources)[0])
    def test_invented_quotes_rejected(self):
        self.finding['citations'][0]['quote']='invented evidence';self.assertFalse(verify_candidate(self.finding,self.sources)[0])
    def test_unknown_path_rejected(self):
        self.finding['citations'][0]['path']='../outside';self.assertFalse(verify_candidate(self.finding,self.sources)[0])
    def test_one_source_is_insufficient(self):
        self.finding['citations'].pop();self.assertFalse(verify_candidate(self.finding,self.sources)[0])
    def test_malformed_json_abstention(self):self.assertIsNone(parse_model('I cannot produce JSON'))
    def test_bounded_retrieval_reports_truncation_and_omission(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);(p/'long.txt').write_text('a'*(PER_FILE+50));(p/'unreadable.pdf').write_bytes(b'%PDF')
            sources,coverage=retrieve(p)
            self.assertEqual(len(sources['long.txt']),PER_FILE)
            self.assertEqual(coverage['truncated'],['long.txt'])
            self.assertEqual(coverage['omitted'][0]['path'],'unreadable.pdf')

if __name__=='__main__':unittest.main(verbosity=2)
