from pathlib import Path
import json, shutil
P=Path(__file__).parent; r=P/'disposable';
if r.exists():shutil.rmtree(r)
r.mkdir();(r/'memory.txt').write_text('Fictional private memory: family planted a pear tree.\n')
policy={'read_story':True};events=[]
def ask():
 if not policy['read_story']:events.append({'request':'read_story','decision':'DENY'});return 'DENIED BY TOY BROKER'
 events.append({'request':'read_story','decision':'ALLOW'});return (r/'memory.txt').read_text().strip()
before=ask();policy['read_story']=False;after=ask();direct=(r/'memory.txt').read_text().strip()
output={'before_broker':before,'after_broker':after,'direct_read_bypasses_broker':direct,'record':events,'limitations':'A same-user process can read the file directly; no security, privacy, cryptography, secure deletion, remote revocation, or recall of previously seen data. A fictional broker, not UGREEN.'}
(P/'output.json').write_text(json.dumps(output,indent=2)+'\n');print(json.dumps(output,indent=2))
