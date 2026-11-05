from pathlib import Path
import shutil,hashlib,json,concurrent.futures
from run_process import run
R=Path(__file__).resolve().parent;F=R/'fixtures';W=R/'workspaces';W.mkdir(exist_ok=True)
for name,base in [('THEN',F/'then'),('NOW-P',F/'archive'),('NOW-G',F/'archive'),('NOW-P-IRRELEVANT',F/'archive')]:
 dest=W/name
 if dest.exists():shutil.rmtree(dest)
 shutil.copytree(base,dest)
(W/'NOW-P-IRRELEVANT'/'99_art_poster.md').write_text('''# Art poster update\n\n**Claimed event date:** 2024-10-10\n**Available to this fictional board archive:** 2024-10-10 10:00 UTC\n**Provenance:** Sent to the board archive Oct 10.\n\nA volunteer replaced a yellow craft-club poster with a blue one for an October art activity. This does not discuss either Alder Street building or the safety order.\n''')
def digest(p):return {str(q.relative_to(p)):hashlib.sha256(q.read_bytes()).hexdigest() for q in sorted(p.rglob('*')) if q.is_file()}
now=digest(W/'NOW-P');aug=digest(W/'NOW-P-IRRELEVANT');assert {k for k in aug if k not in now}=={'99_art_poster.md'} and all(aug[k]==v for k,v in now.items())
assert digest(W/'NOW-P')==digest(W/'NOW-G')
snapshot='''You are an independent investigator examining a fictional local archive. The decision cutoff is 2024-09-12 23:59 UTC. Work only within this workspace, read the actual available records, cite exact filenames and evidence, do not modify files, do not use web, outside files or external services, and distinguish observed records from speculation. A file's availability in this archive is not proof that a particular person read or believed it.\n\n'''
then=snapshot+'''Given only the evidence available at this date, explain the situation, the board's decision options, the recorded decision, and what remains uncertain. Do not predict later developments. State what evidence is within your scope and what it does and does not establish.\n'''
generic=snapshot+'''Explain the historical decision and what changed later. Distinguish evidence available to the board archive at the cutoff from later or uncertain records. Account for when evidence entered the archive, not just the date described; cite supporting records, note uncertainty and avoid judging earlier decisions using later information as if it were then available. Explain whether later information changes the interpretation and which conclusions remain unchanged.\n'''
procedure=generic+'''\nProcedure: First reconstruct the THEN claims and alternatives using only sources with documented availability by the cutoff. Separately classify later and unknown-availability records, noting that an old event date is not proof of receipt or access. For each material later record, identify whether it changes, supports or is irrelevant to a specific THEN inference and explain why, with citations. Treat unknown availability as unknown, not automatically before or after the cutoff. Present a short THEN / REVEAL / NOW account grounded in these independent classifications. Never claim that an earlier decision-maker knew or should have known an unavailable later record.\n'''
case=[('THEN',then),('NOW-P',procedure),('NOW-G',generic),('NOW-P-IRRELEVANT',procedure)]
(F/'private'/'preflight-hashes.json').write_text(json.dumps({n:digest(W/n) for n,_ in case},indent=2)+'\n')
(R/'pre-registered-test.md').write_text('''# Frozen test plan\n\nFictional cutoff 2024-09-12 23:59 UTC. Four fresh Codex processes: THEN has the attested-only snapshot and no later archive files; NOW-P and NOW-G get byte-identical full archives, same core objective and safety requirements; P receives additional temporal classification and reveal steps. NOW-P-IRRELEVANT gets exactly the same P prompt and archive plus one unrelated later poster; no prior output is provided. Controlled input hashes and hidden key are in fixtures/private and physically excluded from investigators. The poster and key were designed before any investigator output; model inputs remain read-only. Outputs will be judged by traceable claims, not aesthetic quality; a single run per condition cannot support statistical claims.\n''')
def job(case):
 name,prompt=case;r=run(W/name,R/'runs'/name,prompt,name,timeout=240);print(name,'exit',r['exit'],'tool commands',r['tool_commands_count'],'seconds',r['elapsed_seconds'],flush=True);return r
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:list(pool.map(job,case))
