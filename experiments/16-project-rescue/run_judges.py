from pathlib import Path
import shutil,concurrent.futures
from run_process import run
R=Path(__file__).resolve().parent;P=R.parents[1];W=R/'judge-material';W.mkdir(exist_ok=True)
for folder in ['archive','results']:(W/folder).mkdir(exist_ok=True)
for rel in ['projects/cedar/layout.txt','projects/cedar/review.md','catalog/design-codes.txt','catalog/production-register.csv','shared/q7.svg','shared/banner-final.svg','shared/lantern.svg','projects/winter/board.md','projects/cedar/notes.txt']:
 dest=W/'archive'/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(R/'fixtures/creative'/rel,dest)
shutil.copyfile(R/'runs/creative-S/response.md',W/'results/report-A.md');shutil.copyfile(R/'runs/creative-G/response.md',W/'results/report-B.md')
shutil.copyfile(R/'demo/copy-record.json',W/'results/local-copy.json')
(W/'request.txt').write_text('My old Cedar folder is missing something important. Can you find the intended asset and propose how to recover it without changing originals? The workspace is my authorized search scope; projects/cedar/assets is the authorized existing destination directory.\n')
(W/'context.txt').write_text('The two reports were independently produced by fresh local Codex processes using the same fictional archive and ordinary safety prompt. One also received a specialized Markdown Skill. They are anonymized; no real NAS agent or user approval was involved. The local copy record was created afterward on a disposable clone with synthetic approval flags and local OS exclusive creation. Real UGREEN copy destination semantics, atomic no-overwrite, gateway approval, resumption, parent result propagation and post-copy readback remain unverified. Adobe Premiere Link Media locates and automatically relinks media using paths and file properties; Windows File History, Time Machine and Synology snapshots recover backed-up versions; UGREEN advertises semantic search and file chat. Project Rescue locates an existing copy, does not undelete bytes or prove application functionality.\n')
base='''Act as a skeptical independent mock hackathon reviewer. Inspect every provided document, including archive evidence, the actual user request, both anonymized reports and local copy record. Do not use outside material or assume real UGREEN behavior or real human validation. Evaluate User Value, Innovation & Differentiation, Technical Quality, and AI NAS Fit & Validation on 0–25 each; scores are subjective simulated judgments, not winning probabilities. Identify: most valuable feature; most original behavior; closest competitor; weakest technical assumption; strongest reason to reject; whether demonstration is compelling; and one improvement possible within a Markdown-only Skill. Compare the two reports, withhold credit for capabilities common to both, and state limitations and whether Round 1 submission is defensible. Provide concrete evidence.\n'''
def job(perspective):
 prompt=base+'\nReview from the perspective of '+perspective+'.\n'
 return run(W,R/'judge-runs'/perspective.replace(' ','-'),prompt,perspective,240)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as x:
 for r in x.map(job,['NAS owner','skeptical engineer','creativity focused judge']):print(r['label'],r['exit'],r['tool_commands_count'],flush=True)
