from pathlib import Path
import hashlib,json,re,sys,zipfile
sys.path.insert(0,'/tmp/ghost-pdf-python')
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from pypdf import PdfReader
P=Path(__file__).resolve().parents[2]; S=P/'prototype/ghost-branch'; O=P/'submissions/round1-ghost-branch-draft';O.mkdir(parents=True,exist_ok=True)
qa=[
('1. What does the Skill do?', 'Ghost Branch investigates potentially forgotten software work in authorized NAS project archives and prepares an evidence-backed recovery handoff.'),
('2. Who is the target user and what is their problem?', 'Developers may have old experiments, source snapshots, screenshots and review notes scattered across backups, making useful unfinished work and reasons it was abandoned difficult to find together.'),
('3. What is the solution?', 'The Skill proposes candidates, checks available current-project evidence, searches for objections or replacements, and classifies work as worth investigating, retired, uncertain or not established.'),
('4. What is the main user flow?', 'The owner authorizes current and archived folders and asks for discovery, a specific feature investigation, or a recovery packet. The Skill requests bounded source analysis, presents evidence and gaps, and drafts a coding-agent handoff.'),
('5. How does it differ from existing tools or common AI?', 'It focuses on artifacts outside a repository and combines positive evidence with reasons not to revive a feature. Git history and generic AI can overlap; local generic agents also found the central synthetic examples.'),
('6. Which UGREEN AI NAS features does it use, and when?', 'File-agent discovers and reads authorized snapshots; document-agent compares selected notes and source evidence; photo-agent may inspect a screenshot; knowledge-agent may collect evidence or, with approval, save a reviewed packet.'),
('7. What is the technical approach?', 'Markdown instructions direct registered experts to documented ug-filesystem, ug-document, ug-photo and ug-knowledge operations. The user authorizes scope. Saving is optional and approval-gated. Model provider and any external processing depend on device configuration.'),
('8. What is built and what needs testing?', 'The Skill and linked references pass official static checking. Fresh local Codex trials on a fictional archive compare short, detailed and Skill-guided prompts. No UGREEN expert or NAS has run the workflow; source propagation and coverage remain unverified.'),
('9. How will finalists test the Skill?', 'Test a potentially useful old export and a deliberately retired login experiment. Edge case: a decisive review note lies outside the authorized scope; report uncertainty and request access only if useful.'),
('10. What are the known limitations?', 'Ghost Branch cannot execute Git or code, create branches, run tests, or prove repository-wide absence. Safe saving, expert output formats, large archives, screenshots, permissions and actual NAS behavior require validation.')]
words=sum(len(re.findall(r"\b[\w]+(?:[-'][\w]+)*\b",a)) for _,a in qa)
disclosure=('OpenAI Codex assisted with research, design, writing and local testing. The Skill ZIP includes no third-party libraries, executable code or service integration. UGREEN Uliya and its registered experts are platform dependencies. The entrant must verify ownership, competition eligibility, model/data handling and any other required AI or third-party disclosures.')
pdftools=('ReportLab (BSD license, https://www.reportlab.com/) generated this PDF; pypdf (BSD-3-Clause, https://github.com/py-pdf/pypdf) checked its text. Neither is included in the Skill package.')
lines=['# Ghost Branch — Round 1 proposal draft','',f'Ten substantive answers: {words} words.','']
for q,a in qa:lines.extend(['## '+q,a,''])
lines+=['## Disclosures',disclosure,pdftools,''];(O/'proposal-source.md').write_text('\n'.join(lines))
styles=getSampleStyleSheet();title=ParagraphStyle('GhostTitle',parent=styles['Title'],fontSize=17,leading=20,spaceAfter=8);head=ParagraphStyle('GhostQuestion',parent=styles['BodyText'],fontName='Helvetica-Bold',fontSize=9,leading=11,spaceBefore=5,spaceAfter=2);body=ParagraphStyle('GhostAnswer',parent=styles['BodyText'],fontSize=9,leading=11.6,spaceAfter=2);small=ParagraphStyle('GhostDisclosures',parent=body,fontSize=7.5,leading=9.2,textColor=colors.HexColor('#555555'))
story=[Paragraph('Ghost Branch',title),Paragraph('UGREEN AI NAS Hackathon — Round 1 proposal draft',small)]
for q,a in qa:story += [Paragraph(q,head),Paragraph(a,body)]
story += [Spacer(1,4),Paragraph('Disclosures',head),Paragraph(disclosure,small),Paragraph(pdftools,small)]
pdf=O/'ghost-branch-proposal.pdf';SimpleDocTemplate(str(pdf),pagesize=(612,792),leftMargin=54,rightMargin=54,topMargin=38,bottomMargin=38,title='Ghost Branch - Round 1 proposal').build(story)
files=[S/'SKILL.md']+sorted((S/'references').glob('*.md'));zip_path=O/'ghost-branch-skill.zip'
with zipfile.ZipFile(zip_path,'w',compression=zipfile.ZIP_DEFLATED) as z:
 for f in files:z.write(f,f.relative_to(S))
reader=PdfReader(pdf);extracted='\n'.join(page.extract_text() for page in reader.pages);(O/'proposal-extracted.txt').write_text(extracted)
with zipfile.ZipFile(zip_path) as z:
 entries=[{'path':e.filename,'bytes':e.file_size,'sha256':hashlib.sha256(z.read(e)).hexdigest()} for e in z.infolist()];bad=z.testzip()
static=json.loads((P/'experiments/ghost-branch/static-check.json').read_text());checks={'answer_word_count':words,'pdf_bytes':pdf.stat().st_size,'pdf_pages':len(reader.pages),'all_ten_questions_extracted':all(q in extracted for q,_ in qa),'zip_bytes':zip_path.stat().st_size,'uncompressed_bytes':sum(x['bytes'] for x in entries),'entries':entries,'zip_crc_error':bad,'static_status':static['status'],'static_errors':static['summary']['errors'],'static_warnings':static['summary']['warnings'],'zip_matches_checker_hashes':{x['path']:x['sha256'] for x in entries}=={x['path']:x['sha256'] for x in static['files']},'limits_ok':words<=500 and pdf.stat().st_size<=1000000 and zip_path.stat().st_size<=10000000 and sum(x['bytes'] for x in entries)<=10000000 and len(entries)<=100 and all(x['bytes']<=1000000 for x in entries)}
(O/'package-verification.json').write_text(json.dumps(checks,indent=2)+'\n');print(json.dumps(checks,indent=2));assert checks['limits_ok'] and checks['all_ten_questions_extracted'] and checks['zip_matches_checker_hashes'] and checks['static_status']=='static-pass' and not checks['static_errors'] and not checks['static_warnings'] and bad is None
