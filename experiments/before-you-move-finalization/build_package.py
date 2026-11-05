from pathlib import Path
import hashlib,json,re,sys,zipfile
sys.path.insert(0,'/tmp/ugreen-flagship-python')
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from pypdf import PdfReader
P=Path(__file__).resolve().parents[2]; S=P/'prototype/before-you-move'; OUT=P/'submissions/round1-before-you-move-final'
qa=[
('1. What does the Skill do?', 'Before You Move is designed to show what a proposed file change might affect before the owner acts.'),
('2. Who is the target user, and what is their problem?', 'NAS owners reorganizing long-lived projects may not know which documents refer to a file or why identical copies are kept.'),
('3. What is the solution?', 'A read-only review links a proposed move, rename or deletion to returned references, possible copy roles and unresolved evidence.'),
('4. What is the main user flow?', 'The owner supplies the target, intended change and authorized folders. The Skill requests a bounded search, examines returned references, optionally compares selected copies, and presents source evidence, unknowns and a specific next step.'),
('5. How does it differ from existing tools or common AI?', 'UGREEN offers file search and deduplication. This proposed review combines path references and documented file roles with a pre-change decision. Generic AI can perform similar checks; our local tests did not establish superiority.'),
('6. Which UGREEN AI NAS features does it use, and when?', 'For authorized paths, file-agent discovers and inspects files and may compare hashes. Document-agent examines relevant references. Knowledge-agent may seek supporting and contrary evidence.'),
('7. What is the technical approach?', 'Markdown instructions direct registered experts to use documented ug-filesystem, ug-document and ug-knowledge operations. The owner authorizes the scope. The workflow requests no file changes. The configured Uliya model and any external processing depend on the device setup.'),
('8. What is built, and what still needs testing?', 'The Skill and linked references pass the official static checker. Fictional local tests compared ordinary, detailed and Skill-guided requests. No UGREEN experts or NAS hardware were used; expert results and coverage remain unverified.'),
('9. How will you test the Skill as a finalist?', 'Test a file referenced by two project notes, then two identical copies with different recorded roles. Edge case: relevant folders are outside the authorized scope; request permission and report the gap.'),
('10. What are the known limits, risks or dependencies?', 'The Skill cannot establish a complete dependency graph or guarantee that a change is safe. It does not perform file changes. Expert output formats, source attribution, model configuration and actual NAS behavior require validation.')]
words=sum(len(re.findall(r"\b[\w]+(?:[-'][\w]+)*\b",answer)) for _,answer in qa)
disc=('OpenAI Codex assisted with research, design, drafting and local tests. The Skill package contains no third-party libraries or executables. UGREEN Uliya and its registered experts are platform dependencies. The configured model provider may process authorized content externally; the entrant should verify that configuration and add any other applicable AI or third-party disclosures.')
tools=('ReportLab (BSD license, https://www.reportlab.com/) generated this PDF; pypdf (BSD-3-Clause, https://github.com/py-pdf/pypdf) checked its text. Neither is included in the Skill package.')
lines=['# Before You Move — Round 1 project proposal','',f'Ten substantive answers: {words} words.','']
for q,a in qa:lines.extend(['## '+q,a,''])
lines.extend(['## Disclosures',disc,tools,'']);(OUT/'proposal-source.md').write_text('\n'.join(lines))
styles=getSampleStyleSheet();title=ParagraphStyle('FinalTitle',parent=styles['Title'],fontSize=17,leading=20,spaceAfter=8); h=ParagraphStyle('FinalQuestion',parent=styles['BodyText'],fontName='Helvetica-Bold',fontSize=9.2,leading=11,spaceBefore=5,spaceAfter=2); b=ParagraphStyle('FinalBody',parent=styles['BodyText'],fontSize=9.2,leading=12,spaceAfter=2); n=ParagraphStyle('FinalNote',parent=b,fontSize=7.7,leading=9.5,textColor=colors.HexColor('#555555'))
story=[Paragraph('Before You Move',title),Paragraph('UGREEN AI NAS Hackathon — Round 1 proposal',n)]
for q,a in qa:story += [Paragraph(q,h),Paragraph(a,b)]
story += [Spacer(1,5),Paragraph('Disclosures',h),Paragraph(disc,n),Paragraph(tools,n)]
pdf=OUT/'before-you-move-proposal.pdf';SimpleDocTemplate(str(pdf),pagesize=(612,792),leftMargin=54,rightMargin=54,topMargin=38,bottomMargin=38,title='Before You Move - Round 1 proposal').build(story)
files=[S/'SKILL.md']+sorted((S/'references').glob('*.md'));zpath=OUT/'before-you-move-skill.zip'
with zipfile.ZipFile(zpath,'w',compression=zipfile.ZIP_DEFLATED) as z:
 for p in files:z.write(p,p.relative_to(S))
reader=PdfReader(pdf);extracted='\n'.join(page.extract_text() for page in reader.pages);(OUT/'proposal-extracted.txt').write_text(extracted)
with zipfile.ZipFile(zpath) as z:
 details=[{'path':i.filename,'bytes':i.file_size,'sha256':hashlib.sha256(z.read(i)).hexdigest()} for i in z.infolist()];bad=z.testzip()
check=json.loads((P/'experiments/before-you-move-finalization/static-check.json').read_text());chkhash={x['path']:x['sha256'] for x in check['files']};zhash={x['path']:x['sha256'] for x in details}
result={'answer_word_count':words,'pdf_bytes':pdf.stat().st_size,'pdf_pages':len(reader.pages),'all_ten_questions_extracted':all(q in extracted for q,_ in qa),'zip_bytes':zpath.stat().st_size,'zip_uncompressed_bytes':sum(x['bytes'] for x in details),'zip_entries':details,'zip_crc_error':bad,'static_checker_status':check['status'],'static_errors':check['summary']['errors'],'static_warnings':check['summary']['warnings'],'zip_matches_static_checked_files':chkhash==zhash,'size_limits_met':words<=500 and pdf.stat().st_size<=1000000 and zpath.stat().st_size<=10000000 and sum(x['bytes'] for x in details)<=10000000 and len(details)<=100 and all(x['bytes']<=1000000 for x in details)}
(OUT/'verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2));assert result['all_ten_questions_extracted'] and result['size_limits_met'] and result['zip_matches_static_checked_files'] and result['static_checker_status']=='static-pass' and not result['static_errors'] and not result['static_warnings'] and bad is None
