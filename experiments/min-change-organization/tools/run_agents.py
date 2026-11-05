from pathlib import Path
import hashlib,json,os,shutil,subprocess,tempfile,time,concurrent.futures
R=Path(__file__).resolve().parents[1];PROJECT=R.parents[1];HOME_CODEX=Path(os.environ['CODEX_HOME']);CODEX=Path(shutil.which('codex'));BWRAP=PROJECT/'experiments/15-finalist-candidate/local-tools/extracted/usr/bin/bwrap'
BASE=(R/'prompts/generic.md').read_text();GUIDE=(R/'prompts/specialized-procedure.md').read_text();COMMON=(R/'prompts/policy-common.md').read_text();EXTRA=(R/'prompts/policy-C-extra.md').read_text()
def hashes(p):
 return {x.relative_to(p).as_posix():hashlib.sha256(x.read_bytes()).hexdigest() for x in p.rglob('*') if x.is_file()}
def run(dataset,condition,rep):
 out=R/'runs'/dataset/f'{condition}{rep}';out.mkdir(parents=True,exist_ok=False);prompt=BASE+('\n\n'+GUIDE if condition=='S' else '');(out/'prompt.md').write_text(prompt);(out/'policy.md').write_text(COMMON+('\n\n'+EXTRA if dataset=='C' else ''))
 with tempfile.TemporaryDirectory(prefix='min-change-') as tmp:
  t=Path(tmp);tool=t/'tools';res=t/'out';work=t/'work';tool.mkdir();res.mkdir();shutil.copytree(R/'fixtures'/dataset,work);before=hashes(work)
  for f in (CODEX,CODEX.parent/'codex-code-mode-host',R/'tools/adapter.py'):shutil.copy2(f,tool/f.name)
  policy=t/'policy.txt';policy.write_text((out/'policy.md').read_text())
  cmd=[str(BWRAP),'--ro-bind','/','/','--dev-bind','/dev','/dev','--proc','/proc','--tmpfs','/tmp','--tmpfs',str(PROJECT),'--bind',str(HOME_CODEX),str(HOME_CODEX)]
  for parent in [Path('/home/martelaxe/.codex'),HOME_CODEX]:
   if not parent.exists():continue
   for sub in ['sessions','archived_sessions','attachments','history.jsonl']:
    p=parent/sub
    if p.is_dir():cmd+=['--tmpfs',str(p)]
    elif p.is_file():cmd+=['--ro-bind','/dev/null',str(p)]
  cmd+=['--dir','/tmp/work','--ro-bind',str(work),'/tmp/work','--dir','/tmp/out','--bind',str(res),'/tmp/out','--dir','/tmp/tools','--ro-bind',str(tool),'/tmp/tools','--ro-bind',str(policy),'/tmp/policy.txt','--chdir','/tmp/work','--setenv','PATH','/tmp/tools:'+os.environ['PATH'],'--','/tmp/tools/codex','exec','--ignore-user-config','--ephemeral','--skip-git-repo-check','--sandbox','danger-full-access','-m','gpt-6.1-sol','-c','model_reasoning_effort="low"','-c','web_search="disabled"','--cd','/tmp/work','--output-last-message','/tmp/out/final.txt','--json','-']
  start=time.monotonic()
  try:
   p=subprocess.run(cmd,input=prompt,text=True,capture_output=True,timeout=600);rc=p.returncode;stdout=p.stdout;stderr=p.stderr
  except subprocess.TimeoutExpired as e:
   rc='timeout';stdout=e.stdout or '';stderr=e.stderr or '';stdout=stdout.decode() if isinstance(stdout,bytes) else stdout;stderr=stderr.decode() if isinstance(stderr,bytes) else stderr
  (out/'events.jsonl').write_text(stdout);(out/'stderr.txt').write_text(stderr)
  for f in res.iterdir():
   if f.is_file():shutil.copy2(f,out/f.name)
  usage=None;commands=[]
  for line in stdout.splitlines():
   try:
    e=json.loads(line)
    if e.get('type')=='item.completed' and e.get('item',{}).get('type')=='command_execution':commands.append(e['item'])
    if e.get('type')=='turn.completed':usage=e.get('usage')
   except Exception:pass
  after=hashes(work)
  record={'dataset':dataset,'condition':condition,'rep':rep,'exit':rc,'elapsed_seconds':round(time.monotonic()-start,3),'model':'gpt-6.1-sol','effort':'low','usage':usage,'shell_calls':len(commands),'plan_exists':(out/'plan.json').exists(),'input_bytes_unchanged':before==after,'isolation':'Outer bubblewrap read-only host root, isolated fixture and masked project/known history; temporary /tmp/out writable; some host paths visible, network isolation unverified. No UGREEN runtime.','approval':'none; plan-only'};(out/'execution.json').write_text(json.dumps(record,indent=2)+'\n');return record
jobs=[(d,c,i) for d in ['A','B','C','D'] for i in (1,2) for c in ('G','S')]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 for f in concurrent.futures.as_completed([pool.submit(run,*job) for job in jobs]):print(json.dumps(f.result()),flush=True)
