from pathlib import Path
import sys,re,json,zipfile,hashlib
sys.path.insert(0,'/tmp/ugreen-flagship-python')
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.units import inch
from pypdf import PdfReader
P=Path(__file__).resolve().parents[2];OUT=P/'submissions/round1-final-candidate-draft';S=P/'prototype/final-flagship';OUT.mkdir(parents=True,exist_ok=True)
qa=[
('1. What does the Skill do?', 'Before You Move previews evidence of what a proposed file change might affect.'),
('2. Who is the target user and problem?', 'NAS owners consolidate or reorganize long-lived files but may not know which projects use a particular copy.'),
('3. What is the solution?', 'A read-only investigation distinguishes direct references, ambiguous matches, different copy roles and unknown dependencies before the owner decides.'),
('4. What is the core user flow?', 'The owner identifies the target, proposed change and authorized folders. The Skill searches within those bounds, examines relevant references, optionally compares chosen copies, and presents evidence, limitations and a safe next step.'),
('5. How does it differ from existing tools or common AI?', 'It packages a focused pre-change procedure: a byte-identical copy is not assumed to have the same role, and unsearched or unverified dependencies remain visible. Generic AI can perform similar reasoning; we have not established superiority.'),
('6. Which UGREEN AI NAS capabilities does it use?', 'The file expert discovers and reads selected paths and optionally hashes copies. The document expert examines references. The knowledge expert may seek supporting and contrary evidence.'),
('7. What is the technical approach?', 'The Markdown Skill delegates only to registered experts using documented filesystem, document and knowledge operations. The owner authorizes the scope. The core makes no changes. Model and any external processing depend on device configuration.'),
('8. What is built and what needs testing?', 'The Skill instructions pass the official static checker. Independent local Codex tests on fictional files compared ordinary and Skill-guided requests; neither used UGREEN agents. Actual device execution, source propagation and coverage remain unverified.'),
('9. What will finalists test?', 'First, inspect an asset before a proposed move when two documents reference it. Second, compare identical copies with one referenced role and one unknown role. Edge case: an essential reference lies outside the authorized scope; request authorization and report uncertainty.'),
('10. What are the limitations and dependencies?', 'The Skill cannot observe all applications or prove a deletion safe. It does not move files, restore backups or maintain a dependency graph. Expert result formats, completeness and configured model behavior require hardware testing.')]
words=sum(len(re.findall(r"\b[\w]+(?:[-'][\w]+)*\b",a)) for _,a in qa)
source=['# Before You Move — Round 1 proposal draft','', 'Exactly ten substantive answers; word count: '+str(words), '']
for q,a in qa:source.extend(['## '+q,a,''])
source+=['## Disclosures','OpenAI Codex assisted with research, drafting, design and local testing. The Skill package contains no external libraries or executable components. It depends on the UGREEN Uliya platform and its registered experts; applicable UGREEN terms apply. The configured AI model/provider is not fixed by the Skill and may process authorized content externally.','ReportLab (BSD license; https://www.reportlab.com/) was used solely to generate this PDF, and pypdf (BSD-3-Clause; https://github.com/py-pdf/pypdf) to check its extracted text; neither is included in the Skill package. Entrant must review ownership, eligibility, development timing and disclosures before submission.']
(OUT/'proposal-source.md').write_text('\n'.join(source)+'\n')
styles=getSampleStyleSheet();title=ParagraphStyle('TitleX',parent=styles['Title'],fontSize=17,leading=20,spaceAfter=10);qh=ParagraphStyle('Q',parent=styles['BodyText'],fontName='Helvetica-Bold',fontSize=9.2,leading=11,spaceBefore=6,spaceAfter=2);body=ParagraphStyle('B',parent=styles['BodyText'],fontSize=9.2,leading=12,spaceAfter=3);note=ParagraphStyle('Note',parent=body,fontSize=7.8,leading=10,textColor=colors.HexColor('#555555'))
story=[Paragraph('Before You Move',title),Paragraph('Round 1 proposal — review draft',note)]
for q,a in qa:story += [Paragraph(q,qh),Paragraph(a,body)]
story += [Spacer(1,8),Paragraph('Disclosures',qh),Paragraph(source[-2],note),Paragraph(source[-1],note)]
pdf=OUT/'proposal-draft.pdf';SimpleDocTemplate(str(pdf),pagesize=(612,792),leftMargin=54,rightMargin=54,topMargin=42,bottomMargin=42,title='Before You Move - Round 1 proposal draft').build(story)
zip_path=OUT/'skill-draft.zip'
files=[S/'SKILL.md']+sorted((S/'references').glob('*.md'))
with zipfile.ZipFile(zip_path,'w',compression=zipfile.ZIP_DEFLATED) as z:
 for p in files:z.write(p,p.relative_to(S))
reader=PdfReader(pdf); extracted='\n'.join(p.extract_text() for p in reader.pages);(OUT/'proposal-extracted.txt').write_text(extracted)
with zipfile.ZipFile(zip_path) as z: contents=[{'path':x.filename,'bytes':x.file_size,'sha256':hashlib.sha256(z.read(x)).hexdigest()} for x in z.infolist()];bad=z.testzip()
checks={'word_count_10_answers':words,'pdf_bytes':pdf.stat().st_size,'pdf_pages':len(reader.pages),'pdf_extracts_all_questions':all(q in extracted for q,_ in qa),'zip_bytes':zip_path.stat().st_size,'zip_uncompressed_bytes':sum(x['bytes'] for x in contents),'files':contents,'zip_test_error':bad,'all_answers_within_500':words<=500,'skill_root_present':any(x['path']=='SKILL.md' for x in contents),'limits_ok':pdf.stat().st_size<=1000000 and zip_path.stat().st_size<=10000000 and sum(x['bytes'] for x in contents)<=10000000 and len(contents)<=100 and all(x['bytes']<=1000000 for x in contents),'static_check':json.loads((P/'experiments/final-flagship-tests/static-check.json').read_text())['status']}
(OUT/'package-verification.json').write_text(json.dumps(checks,indent=2)+'\n');print(json.dumps(checks,indent=2))
