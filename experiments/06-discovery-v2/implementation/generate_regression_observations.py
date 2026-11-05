"""Replay three archived outputs through V2; later blocker review is mocked."""
from pathlib import Path
import json
from discovery_v2 import adapt_exp05, inventory, investigate

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'experiments/06-discovery-v2/results/regression-observations.json'
records = {}
for label, archive, stage in [('h-a1','a','a-h1/candidate-message.md'),('h-b1','b','b-h1/candidate-message.md'),('h-b2','b','b-h2/verifier-message.md')]:
    raw=json.loads((ROOT/'experiments/05-intelligence-multiplier/execution'/stage).read_text())['findings'][0]
    candidate=adapt_exp05(raw,1)
    sources,coverage=inventory(ROOT/'experiments/05-intelligence-multiplier/datasets'/archive)
    reviews=[]
    if label=='h-b2':
        reviews=[{'candidate_id':candidate['id'],'disposition':'SUPPORTED','explanation':'Illustrative positive review; uncited blocker must prevent promotion.',
                  'assessments':{e['id']:'supports' for e in candidate['evidence']},'blockers':[],'blocker_search_complete':True}]
    records[label]=investigate([candidate],sources,coverage,reviews)
    if label=='h-b1':
        excerpt='The cooperative prohibits sharing BX19 outside the organization without the garden committee’s separate written approval, including non-commercial samples.'
        review={'candidate_id':candidate['id'],'disposition':'BLOCKED','explanation':'Mock reviewer explicitly identified a sourced restriction.',
                'assessments':{'review-rights':'supports'},'blockers':[{'claim_id':'restriction','evidence_id':'review-rights','text':'External sharing requires written committee approval.'}],
                'additional_evidence':[{'id':'review-rights','claim_id':'restriction','path':'04-rights/lot-disposition.txt','excerpt':excerpt,'relation':'supports'}]}
        records['h-b1-later-mocked-review']=investigate([candidate],sources,coverage,[review])
assert records['h-a1']['candidates'][0]['state']=='NEEDS VERIFICATION'
assert records['h-b1']['candidates'][0]['state']=='NEEDS VERIFICATION'
assert records['h-b2']['candidates'][0]['state']=='NEEDS VERIFICATION'
assert records['h-b1-later-mocked-review']['candidates'][0]['state']=='BLOCKED'
OUT.write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print('Recorded H-A1, H-B1, H-B2, and one later mocked-review result.')
