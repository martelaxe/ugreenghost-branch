from pathlib import Path
import textwrap,zipfile,hashlib,json,re
R=Path(__file__).resolve().parent;P=R.parents[1]; O=P/'submission/experiment-16';O.mkdir(parents=True,exist_ok=True);S=P/'prototype/project-rescue-v2'
items=[
('What does your Skill do? (one sentence)','Project Rescue finds a context-supported candidate for a missing project file and proposes one approved copy that preserves the source.'),
('Who is your target user, and what is their problem?','Creators and small teams may have a missing project dependency while an existing usable copy has an opaque name, outdated alternatives, or another active use.'),
('What is your solution?','Compare the missing reference, review history and candidate records to identify a supported version; explain contradictions and stop when identity is ambiguous.'),
('What is the main user flow?','Authorize folders, investigate references and candidates, review one proposed source and destination, approve the exact operation, and independently verify the copy if the platform can safely execute it.'),
('How is your idea different from existing tools or common AI solutions?','The intended workflow combines cross-file identity evidence, shared-source preservation and approval-gated action across project types. Generic AI and application-specific relinking overlap; superior performance and uniqueness are not established.'),
('Which UGREEN AI NAS features does your Skill use, and at which step?','File-agent discovers, reads, checks paths and hashes, and conditionally copies; document-agent extracts and compares project references. All work stays within owner-authorized scopes.'),
('What is your technical approach?','A Markdown parent delegates to registered experts using actual completed results. The user supplies the goal and source and destination authorization. Separate owner and gateway approval are required; uncertain identity, collisions or unestablished atomic no-overwrite stop execution. Runtime model and data flows depend on UGREEN configuration.'),
('What have you built so far? What is not built yet? What still needs testing on a NAS?','A Markdown Skill passed static checking. Local Codex identified intended candidates in two fictional archives; generic Codex did too. A separate local adapter copied one file with simulated approvals. Real NAS execution, safe copy semantics, approval resumption and readback remain untested.'),
('How will you test your Skill if you become a Finalist? Name two core test cases and one edge case.','Test a creative asset and a business record with misleading names and supported identity; confirm the shared source remains. Edge case: an occupied target or unavailable atomic no-overwrite must block the copy.'),
('What are the known limits, risks, or outside dependencies of your Skill?','It finds existing accessible files, not deleted bytes; identity and archive coverage may remain uncertain. Byte equality does not prove application repair. UGREEN expert results, data handling, gateway approvals and collision guarantees remain unknown. Stop when safety is not established.')]
disclosure='Third-party and AI disclosure: No third-party executable components or open-source libraries are included in the Skill. UGREEN Uliya Skill Creation Tool and NAS runtime are supplied by UGREEN under its applicable terms (https://ai.ugreen.com/pages/hackathon-starter-kit). OpenAI Codex was used for research, drafting and local testing under OpenAI terms (https://openai.com/policies/terms-of-use/). The target runtime model and any external data flows depend on its configuration and require verification.'
words=sum(len(re.findall(r"\b[\w'-]+\b",a)) for q,a in items)
assert len(items)==10 and words<=500
md='# Project Rescue — Round 1 proposal (review draft)\n\n'+''.join(f'{i}. **{q}**\n\n   {a}\n\n' for i,(q,a) in enumerate(items,1))+f'## Third-party and AI disclosure\n\n{disclosure}\n'
(O/'proposal-source.md').write_text(md)
pages=[['PROJECT RESCUE - ROUND 1 PROPOSAL (REVIEW DRAFT)','']]
for i,(q,a) in enumerate(items,1):
 group=textwrap.wrap(f'{i}. {q}',width=86)+textwrap.wrap(a,width=86,initial_indent='   ',subsequent_indent='   ')+['']
 if len(pages[-1])+len(group)>48:pages.append([])
 pages[-1].extend(group)
group=['THIRD-PARTY AND AI DISCLOSURE']+textwrap.wrap(disclosure,width=86)
if len(pages[-1])+len(group)>48:pages.append([])
pages[-1].extend(group)
# Generate an uncompressed PDF using standard PDF objects; keep each answer together.
def esc(s):return s.replace('\\','\\\\').replace('(','\\(').replace(')','\\)')
objs=[]
def obj(s):objs.append(s.encode('latin1'));return len(objs)
obj('<< /Type /Catalog /Pages 2 0 R >>');obj('PLACEHOLDER');font=obj('<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>')
pageids=[]
for page in pages:
 stream='BT\n/F1 10 Tf\n13 TL\n40 760 Td\n'+'\n'.join('('+esc(line)+') Tj T*' for line in page)+'\nET\n'
 content=obj(f'<< /Length {len(stream.encode("latin1"))} >>\nstream\n{stream}endstream')
 pageids.append(obj(f'<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 {font} 0 R >> >> /Contents {content} 0 R >>'))
objs[1]=('<< /Type /Pages /Kids ['+' '.join(f'{p} 0 R' for p in pageids)+f'] /Count {len(pageids)} >>').encode('latin1')
out=bytearray(b'%PDF-1.4\n%\xe2\xe3\xcf\xd3\n');offset=[0]
for i,data in enumerate(objs,1):offset.append(len(out));out+=f'{i} 0 obj\n'.encode()+data+b'\nendobj\n'
xref=len(out);out+=f'xref\n0 {len(objs)+1}\n0000000000 65535 f \n'.encode()
for n in offset[1:]:out+=f'{n:010d} 00000 n \n'.encode()
out+=f'trailer\n<< /Size {len(objs)+1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n'.encode();pdf=O/'proposal-review.pdf';pdf.write_bytes(out)
z=O/'project-rescue-v2-review.zip'
with zipfile.ZipFile(z,'w',zipfile.ZIP_DEFLATED) as f:
 for p in [S/'SKILL.md',S/'references/disclosures.md']:f.write(p,p.relative_to(S))
with zipfile.ZipFile(z) as f:
 infos=f.infolist();assert len(infos)==2 and all(i.filename.endswith('.md') and i.file_size<=1048576 for i in infos) and sum(i.file_size for i in infos)<=10*1048576 and f.testzip() is None
 assert f.read('SKILL.md')==(S/'SKILL.md').read_bytes()
assert pdf.stat().st_size<=1048576 and z.stat().st_size<=10*1048576
record={'substantive_answer_word_count':words,'questions':len(items),'pdf_pages':len(pages),'pdf_bytes':pdf.stat().st_size,'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'zip_bytes':z.stat().st_size,'zip_sha256':hashlib.sha256(z.read_bytes()).hexdigest(),'zip_entries':[{ 'path':i.filename,'uncompressed_bytes':i.file_size} for i in infos],'skill_sha256':hashlib.sha256((S/'SKILL.md').read_bytes()).hexdigest(),'pdf_validation':'PDF header, object offsets and text generated locally; independent PDF renderer unavailable','status':'review only; not submitted or published'}
(O/'package-verification.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
