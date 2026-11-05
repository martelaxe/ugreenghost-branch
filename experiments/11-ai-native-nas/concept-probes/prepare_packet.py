"""Produce an unsent, blinded label packet from actual local probe outputs."""
import json,random,shutil
from pathlib import Path
base=Path(__file__).resolve().parent
out=base/'human-packet';out.mkdir(exist_ok=True)
names=['impact','rebuild'];random.Random(1101).shuffle(names);mapping=dict(zip(['X','Y'],names))
parts=['# Two fictional NAS experiences\n\nEach excerpt is an actual local AI response to a different fictional task; neither was tested on a UGREEN NAS. Read the assigned order. The source archive for each is under `archives/X/` or `archives/Y/`. The tasks and output lengths differ, so this is an exploratory concept comparison, not an experiment measuring model quality.\n']
for label,name in mapping.items():
 shutil.copytree(base/'fixtures'/name,out/'archives'/label,dirs_exist_ok=True)
 prompt=(base/'outputs'/name/'prompt.txt').read_text().split('\n')[0]
 result=(base/'outputs'/name/'raw-response.md').read_text()
 parts += [f'\n## Experience {label}\n\n**User request:** {prompt}\n\n{result}\n']
parts.append('''\n## Questions\n\n1. Which experience would you actually want to use on your NAS? X / Y / neither. Why?\n2. Which result would change what you would do next? X / Y / both / neither. How?\n3. Which felt surprising or memorable? X / Y / both / neither. Why?\n4. What was generic, confusing, incorrect, unsafe or missing?\n5. What would you need to verify before acting on the result?\n6. Would either make you more excited about an AI NAS? Yes / maybe / no. Explain.\n\nChoose neither if appropriate; please do not include personal data.\n''')
(out/'participant-packet.md').write_text(''.join(parts))
(base/'facilitator-mapping.json').write_text(json.dumps({'seed':1101,'mapping':mapping},indent=2)+'\n')
print('Created anonymized packet; no participants contacted.')
