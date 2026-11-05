"""Run a fresh local Codex process in a narrowly mounted fixture. Not UGREEN."""
from pathlib import Path
import os,subprocess,tempfile,shutil,time,json,hashlib
R=Path(__file__).resolve().parent
BWRAP=Path('/tmp/ugreen-blind-01-r0oqy1ev/sandbox-tools/usr/bin/bwrap'); CODEX=Path(shutil.which('codex')); AUTH=Path(os.environ['CODEX_HOME'])/'auth.json'
TOOLS_TEMP=tempfile.TemporaryDirectory(prefix='handoff14-shared-tools-');TOOLS_PATH=Path(TOOLS_TEMP.name)
shutil.copy2(BWRAP,TOOLS_PATH/'bwrap');shutil.copy2(CODEX,TOOLS_PATH/'codex');shutil.copy2(CODEX.parent/'codex-code-mode-host',TOOLS_PATH/'codex-code-mode-host')
def digest(root):return {str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(root.rglob('*')) if p.is_file()}
def run(work,out,prompt,label,timeout=240):
 out.mkdir(parents=True,exist_ok=True);(out/'prompt.md').write_text(prompt);before=digest(work)
 assert not any(p.is_symlink() for p in work.rglob('*'))
 with tempfile.TemporaryDirectory(prefix='handoff14-run-') as t:
  t=Path(t);tool=TOOLS_PATH;res=t/'out';res.mkdir()
  # The strict throwaway CODEX_HOME failed workspace routing discovery; use the
  # configured runtime, while hiding project, /tmp, and known history folders.
  cmd=[str(BWRAP),'--ro-bind','/','/','--dev-bind','/dev','/dev','--proc','/proc','--tmpfs','/tmp','--tmpfs',str(R.parents[1]),'--bind','/home/martelaxe/.codex','/home/martelaxe/.codex','--bind',os.environ['CODEX_HOME'],os.environ['CODEX_HOME']]
  for parent in ['/home/martelaxe/.codex',os.environ['CODEX_HOME']]:
   for sub in ['sessions','archived_sessions','attachments','history.jsonl']:
    path=Path(parent)/sub
    if path.is_dir():cmd+=['--tmpfs',str(path)]
    elif path.is_file():cmd+=['--ro-bind','/dev/null',str(path)]
  cmd+=['--dir','/tmp/work','--ro-bind',str(work.resolve()),'/tmp/work','--dir','/tmp/out','--bind',str(res),'/tmp/out','--dir','/tmp/tools','--ro-bind',str(tool),'/tmp/tools','--chdir','/tmp/work','--setenv','PATH','/tmp/tools:'+os.environ['PATH'],'--','/tmp/tools/codex','exec','--ignore-user-config','--ephemeral','--skip-git-repo-check','--sandbox','read-only','-m','gpt-6.1-sol','-c','model_reasoning_effort="low"','-c','web_search="disabled"','--cd','/tmp/work','--output-last-message','/tmp/out/response.md','--json','-']
  start=time.monotonic()
  try:
   p=subprocess.run(cmd,input=prompt,text=True,capture_output=True,timeout=timeout);exitcode=p.returncode;so=p.stdout;se=p.stderr
  except subprocess.TimeoutExpired as e:exitcode='timeout';so=e.stdout or '';se=e.stderr or '';so=so.decode() if isinstance(so,bytes) else so;se=se.decode() if isinstance(se,bytes) else se
  (out/'events.jsonl').write_text(so);(out/'stderr.txt').write_text(se)
  if (res/'response.md').exists():shutil.copyfile(res/'response.md',out/'response.md')
  after=digest(work);n=0;usage=None
  for line in so.splitlines():
   try:
    ev=json.loads(line); item=ev.get('item',{});n+=item.get('type')=='command_execution' and ev.get('type')=='item.completed'
    if ev.get('type')=='turn.completed':usage=ev.get('usage')
   except (ValueError,TypeError):pass
  record={'label':label,'exit':exitcode,'elapsed_seconds':round(time.monotonic()-start,2),'has_final':(out/'response.md').exists(),'model_requested':'gpt-6.1-sol','reasoning_requested':'low','tool_commands_count':n,'usage_if_reported':usage,'fresh_process':True,'input_hashes':before,'inputs_unchanged':before==after,'no_symlinks':True,'isolation':'Outer bubblewrap hides project and host /tmp and masks known session, archive and attachment paths; mounts current fictional files and configured Codex runtime directories. Other host paths, configuration, metadata and auth remain visible, so isolation is incomplete; network isolation not independently proven. No UGREEN experts.'}
  (out/'execution.json').write_text(json.dumps(record,indent=2)+'\n');return record
