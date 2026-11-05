from pathlib import Path
import hashlib,json,os,shutil,subprocess,tempfile,time,concurrent.futures
R=Path(__file__).resolve().parents[1]; PROJECT=R.parents[2];WORK=R/'fixture/work';TOOL=R/'tools';HOME_CODEX=Path(os.environ['CODEX_HOME']);CODEX=Path(shutil.which('codex'));BWRAP=PROJECT/'experiments/15-finalist-candidate/local-tools/extracted/usr/bin/bwrap'
BASE=(R/'generic-prompt.md').read_text();SKILL=(R/'frozen-procedure.md').read_text()
def run(label,prompt):
 out=R/'runs'/label;out.mkdir(parents=True,exist_ok=False);(out/'prompt.md').write_text(prompt)
 with tempfile.TemporaryDirectory(prefix='nas-adaptive-agent-') as tmp:
  t=Path(tmp);tool=t/'tools';res=t/'out';fault=t/'faults';tool.mkdir();res.mkdir();fault.mkdir()
  for f in (CODEX,CODEX.parent/'codex-code-mode-host',TOOL/'adapter.py',TOOL/'adapter_core.py',R/'output-schema.json'):shutil.copy2(f,tool/f.name)
  shutil.copy2(R/'fixture/faults.json',fault/'config.json')
  cmd=[str(BWRAP),'--ro-bind','/','/','--dev-bind','/dev','/dev','--proc','/proc','--tmpfs','/tmp','--tmpfs',str(PROJECT),'--bind',str(HOME_CODEX),str(HOME_CODEX)]
  for parent in [Path('/home/martelaxe/.codex'),HOME_CODEX]:
   if not parent.exists():continue
   for sub in ['sessions','archived_sessions','attachments','history.jsonl']:
    p=parent/sub
    if p.is_dir():cmd+=['--tmpfs',str(p)]
    elif p.is_file():cmd+=['--ro-bind','/dev/null',str(p)]
  cmd+=['--dir','/tmp/work','--ro-bind',str(WORK),'/tmp/work','--dir','/tmp/out','--bind',str(res),'/tmp/out','--dir','/tmp/tools','--ro-bind',str(tool),'/tmp/tools','--dir','/tmp/faults','--ro-bind',str(fault),'/tmp/faults','--chdir','/tmp/work','--setenv','PATH','/tmp/tools:'+os.environ['PATH'],'--','/tmp/tools/codex','exec','--ignore-user-config','--ephemeral','--skip-git-repo-check','--sandbox','danger-full-access','-m','gpt-6.1-sol','-c','model_reasoning_effort="low"','-c','web_search="disabled"','--cd','/tmp/work','--output-schema','/tmp/tools/output-schema.json','--output-last-message','/tmp/out/response.json','--json','-']
  start=time.monotonic()
  try:
   p=subprocess.run(cmd,input=prompt,text=True,capture_output=True,timeout=900);rc=p.returncode;stdout=p.stdout;stderr=p.stderr
  except subprocess.TimeoutExpired as e:
   rc='timeout';stdout=e.stdout or '';stderr=e.stderr or '';stdout=stdout.decode() if isinstance(stdout,bytes) else stdout;stderr=stderr.decode() if isinstance(stderr,bytes) else stderr
  (out/'events.jsonl').write_text(stdout);(out/'stderr.txt').write_text(stderr)
  for f in res.iterdir():
   if f.is_file():shutil.copy2(f,out/f.name)
  cmds=[];usage=None
  for line in stdout.splitlines():
   try:
    e=json.loads(line)
    if e.get('type')=='item.completed' and e.get('item',{}).get('type')=='command_execution':cmds.append(e['item'])
    if e.get('type')=='turn.completed':usage=e.get('usage')
   except Exception:pass
  record={'condition':label,'exit_code':rc,'elapsed_seconds':round(time.monotonic()-start,3),'model_requested':'gpt-6.1-sol','reasoning':'low','fresh_codex_process':True,'shell_tool_calls':len(cmds),'usage':usage,'response_exists':(out/'response.json').exists(),'isolation':'outer bwrap root and fixture read-only; project, temporary and known history paths masked; writable /tmp/out. Host paths and adapter fault config remain visible; network isolation not independently verified. Inner codex danger-full-access only inside outer wrapper.','nas_runtime':False};(out/'execution.json').write_text(json.dumps(record,indent=2)+'\n');return record
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
 for f in concurrent.futures.as_completed([pool.submit(run,'G',BASE),pool.submit(run,'S',BASE+'\n\n'+SKILL)]):print(json.dumps(f.result()),flush=True)
