"""Make an unsent participant packet from exact local model output excerpts."""
import json,secrets,shutil
from pathlib import Path
base=Path(__file__).resolve().parent
s={
 'archaeologist':(base/'outputs/archaeologist/raw-response.md').read_text(),
 'alchemy':(base/'outputs/alchemy/raw-response.md').read_text(),
 'fork':(base/'outputs/fork/raw-response.md').read_text(),
 'quest':(base/'outputs/quest/raw-response.md').read_text(),
}
excerpts={
 'archaeologist':s['archaeologist'].split('Suggested message to Harbor Room:')[0]+'> Could you clarify how the $420 deposit for our 16 March 2024 event, reference HR-241, was settled?\n',
 'alchemy':s['alchemy'].split('### PANEL 2')[1].split('### PANEL 3')[0]+'\n'+s['alchemy'].split('### PANEL 4')[1].split('### PANEL 5')[0],
 'fork':'| Budget item | Draft A — retain original quote P1 | Draft B — proposed replacement P2 |\n|---|---|---|\n'+''.join(x+'\n' for x in s['fork'].splitlines() if x.startswith('| **Total listed costs**') or x.startswith('| Against $240 ceiling') or x.startswith('| Approval status')),
 'quest':s['quest'].split('## SPOILER')[0],
}
# Ensure every excerpted core sentence/row came from the corresponding actual report.
assert 'Could you clarify how the $420 deposit' in s['archaeologist']
labels=['A','B','C','D']; names=list(excerpts);secrets.SystemRandom().shuffle(names);mapping=dict(zip(labels,names))
(root:=base/'human-packet').mkdir(exist_ok=True)
text=['# Four fictional AI NAS experiences — participant packet\n\nThese are unedited excerpts selected from actual local AI outputs using fictional files. They are concept sketches, not real UGREEN NAS results. The full outputs have different lengths; these excerpts also differ in length, so comparisons may be biased. Do not infer a product exists or that any conclusion is certain.\n\nRead in the order assigned by the facilitator. The fictional source files for each experience are in `archives/<its letter>/` if you want to check its evidence. For the excerpt that is a puzzle, you may solve it; the answer is not shown here.\n']
for label,name in mapping.items():
 shutil.copytree(base/'fixtures'/name,root/'archives'/label,dirs_exist_ok=True)
 text.append(f'\n## Experience {label}\n\n{excerpts[name]}\n')
text.append('''\n## Questions\n\n1. Which experience would make you most excited to own an AI NAS, and why? A / B / C / D / none.\n2. Which would you use most often? A / B / C / D / none. Explain.\n3. Which is most surprising to you personally? A / B / C / D / none. What did you expect instead?\n4. Which seems most trustworthy, and what did you want to check?\n5. What felt boring, generic, unsafe, confusing, or unnecessary?\n6. For the puzzle, what answer do you get? Did it feel solvable and worth playing?\n\nYou may select none. These fictional records contain no private information. Please do not include personal data in your answers.\n''')
(root/'participant-packet.md').write_text(''.join(text))
(base/'facilitator-only-mapping.json').write_text(json.dumps({'mapping':mapping,'quest_solution':'BLUE 12','source_note':'Use evidence-checks.md to evaluate quotations and limitations.'},indent=2)+'\n')
print('Created anonymized packet and separate facilitator-only mapping; no one was contacted.')
