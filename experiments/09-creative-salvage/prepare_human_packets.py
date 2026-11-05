"""Create unsent participant packets from trial 1, with hidden facilitator mapping."""
import json,secrets,shutil
from pathlib import Path
base=Path(__file__).resolve().parent; root=base/'human-review';mapping={}
for case in 'ABC':
 packet=root/('participant-case-'+case);packet.mkdir(parents=True,exist_ok=True)
 shutil.copytree(base/'fixtures'/case,packet/'archive',dirs_exist_ok=True)
 tags=[f'{case}-G-1',f'{case}-S-1'];secrets.SystemRandom().shuffle(tags)
 for position,tag in zip(['X','Y'],tags):
  content=(base/'execution'/(tag+'.md')).read_text().replace('/tmp/work/','archive/').replace('/tmp/work','archive')
  (packet/(position+'.md')).write_text(content)
 mapping[case]=dict(zip(['X','Y'],tags))
 (packet/'participant-form.md').write_text('''# Participant form (fictional project)\n\nRead both X.md and Y.md, and inspect the archive sources. These are AI-generated proposals for a fictional project, not instructions or legal advice. The creator has one weekend and $30 for a free public educational display. Both proposals use the same archive.\n\n1. Which proposal would you actually pursue? X / Y / neither. Why?\n2. Which suggests something you personally had not considered? X / Y / both / neither. What?\n3. Which is more feasible using documented materials and time? X / Y / tie / neither. What is missing?\n4. Which handles restrictions and unknown rights more accurately? X / Y / tie / neither. Cite a source.\n5. Which gives the clearest safe next action? X / Y / tie / neither.\n6. Would you use an authorized NAS feature like this? Yes / maybe / no; explain.\n7. What was generic, unrealistic, surprising, unsafe or unnecessary?\n8. Which claims or citations could you not verify?\n\nPlease do not include personal or confidential information.\n''')
(root/'facilitator-mapping.json').write_text(json.dumps(mapping,indent=2)+'\n')
print('Prepared 3 unsent, anonymized participant packets using trial 1; no participant feedback collected.')
