#!/usr/bin/env python3
"""Research-only fixture generator. Not part of a UGREEN Skill."""
from pathlib import Path
import hashlib,json,difflib
R=Path(__file__).resolve().parents[1]
core={
'01-mail/2026-10-branch.txt':'From: Greenbank Community Room, Oct 12 2026\nSome households asked how children could try growing food on small apartment balconies. We have no instructor for a weekly class and no current purchase budget. Families would benefit from an inexpensive take-home activity with simple visual instructions. We are gathering ideas; nothing is commissioned.\n',
'01-mail/2024-partner.txt':'2024 note: a neighborhood harvest exchange took place once in May. It is closed and no current event is promised.\n',
'02-stock/stock-list.csv':'lot,botanical_name,harvest,quantity,origin\nBX19,Phaseolus vulgaris,2026,240,cooperative garden\nQ77,Cucurbita pepo,2024,75,private donation\n',
'02-stock/condition-log.txt':'Batch BX19 was dried and stored in sealed paper in September 2026. No germination test has been recorded. An older spring report was for a different batch and cannot establish BX19 viability.\n',
'02-stock/supplies.json':'{"stocktake_date":"2026-10-08","items":[{"item":"small paper envelopes","count":180,"status":"unallocated"},{"item":"adhesive labels","count":90,"status":"unallocated"}]}\n',
'03-research/species-lookup.csv':'botanical_name,plain_name,notes\nPhaseolus vulgaris,common bean,annual garden plant\nCucurbita pepo,squash,annual garden plant\n',
'03-research/old-test.txt':'Germination worksheet, April 2024: Q77 trial had eight sprouts from ten planted seeds. This records Q77 only; there is no later viability claim.\n',
'03-research/packet-notes.txt':'2019 note on planting activities: beans can be observed in clear cups using moist paper. These notes describe an activity, not a verified success rate or a guarantee suitable for every household.\n',
'04-rights/lot-disposition.txt':'Lot BX19 — signed committee minute, September 2026\nRIGHTS_CLAUSE\nExisting records contain no consent to share the Q77 donor lot. No document authorizes the use of personal household data.\n',
'04-rights/q77-donor.txt':'Q77 gift note: the donor permits preservation and private research only. No resale, external distribution or public copying is authorized.\n',
'05-equipment/desk-log.txt':'Office service note, 15 October 2026: the manual envelope label printer is working after maintenance. One trained volunteer can show staff its use. It is not a laboratory instrument.\n',
'05-equipment/format-guide.md':'# Label practice\nPrior workshops used large symbols and brief pictorial steps for mixed-language groups. A sample template can be adapted; user understanding has not been assessed.\n',
'06-design/template.json':'{"template":"T-12","source":"staff-created","license":"internal adaptation allowed","items":["sun symbol","water symbol","blank caption"]}\n',
'06-design/inventory.md':'Template T-12 was used for water-saving notices in 2022 and remains on the office drive. It is not a planting guide.\n',
'07-operations/schedule.csv':'week_start,unallocated_hours,condition\n2026-10-26,2,manager allocation required\n2026-11-02,4,manager allocation required\n2026-11-09,1,subject to client work\n',
'07-operations/limits.txt':'Manager note, 19 October 2026: up to four existing staff hours and unallocated office supplies may be assigned to one internal trial if approved. No outside funding, customer order or partner participation is committed.\n',
'07-operations/missing-register.txt':'Records index: an envelope size measurement sheet is listed as file sleeve-sizes-2025.pdf, but the file was not found during the last archive move. No measurements are available here.\n',
'08-admin/weekly.txt':'Week of October 26: settle the printer order, review supply shelf labels, and arrange the committee meeting.\n',
}
noise=[
('01-mail/vendor.txt','2023 vendor quote for paper expired 31 December 2023.'),('01-mail/meeting.txt','June 2025 meeting invite concerned the office door repair.'),('01-mail/receipt.txt','An earlier delivery of envelopes was received in 2022.'),('02-stock/labels.csv','code,count\nL1,25\nL2,31'),('02-stock/shelf.txt','Shelf B was repainted in 2021; contents were not counted in this note.'),('02-stock/pots.txt','Several plant pots were lent to a member in 2020; no current return record.'),('03-research/weather.txt','An August 2023 weather observation is not a forecast for 2026.'),('03-research/soil.md','# Soil lesson\nA past workshop compared dry and moist soil without measuring plant growth.'),('03-research/drafts.txt','A past office draft proposed a new noticeboard; the project was not funded.'),('04-rights/portrait.txt','A staff portrait belongs to the photographer; publication needs permission.'),('04-rights/logo.txt','The 2021 logo was retired. Its ownership is not established here.'),('04-rights/policy.md','# Information handling\nDo not disclose member contact information without permission.'),('05-equipment/desk.csv','item,status\nstapler,working\nscanner,unknown'),('05-equipment/printer.txt','A large printer had a paper jam repaired in 2025. Current availability is unknown.'),('05-equipment/ventilation.txt','A window latch was replaced in March 2026.'),('06-design/poster.txt','A 2022 poster used green type. The designer retained rights.'),('06-design/colours.csv','name,hex\ncream,FFF8E7\ngreen,335B40'),('06-design/paper.txt','The 2018 paper sample collection is in a cabinet. Its present condition is unknown.'),('07-operations/rota.txt','September 2026 roster records past shifts, not November reservations.'),('07-operations/room.txt','The meeting room was booked for committee review on October 29.'),('07-operations/cleaning.txt','Clean the work table at the end of each shift.'),('08-admin/tea.txt','Office tea and coffee go on the next shopping list.'),('08-admin/invoices.csv','id,amount,status\nI101,62,paid\nI102,80,paid'),('08-admin/keys.txt','The office manager holds the cupboard key.'),('08-admin/travel.txt','A bicycle repair appointment was pencilled in for November.'),('08-admin/print.txt','Keep one box of A4 paper for office correspondence.'),]
for p,t in noise:core[p]=t+'\n'
assert len(core)==44
positive='The cooperative permits staff to prepare and share small non-commercial community activity samples from BX19, subject to manager approval and a viability check.'
blocked='The cooperative prohibits sharing BX19 outside the organization without the garden committee’s separate written approval, including non-commercial samples.'
negative={
'01-mail/2026-10-branch.txt':'From: Greenbank Community Room, Oct 12 2026\nThe children’s balcony-growing activity was completed in August. The room has no current request, budget or available group session before April 2027. General comments may be sent to the committee.\n',
'02-stock/stock-list.csv':'lot,botanical_name,harvest,quantity,origin\nBX19,Phaseolus vulgaris,2022,240,private donation\nQ77,Cucurbita pepo,2024,75,private donation\n',
'02-stock/condition-log.txt':'Batch BX19 was found with torn packaging and unknown moisture exposure. No viable germination test is on file; disposal assessment is pending.\n',
'02-stock/supplies.json':'{"stocktake_date":"2026-10-08","items":[{"item":"small paper envelopes","count":180,"status":"reserved for paid orders"},{"item":"adhesive labels","count":90,"status":"reserved"}]}\n',
'04-rights/lot-disposition.txt':'Lot BX19 — signed committee minute, September 2026\nThe cooperative prohibits distributing or adapting BX19 outside the organization without the donor’s separate written approval, including non-commercial samples.\nNo document authorizes the use of personal household data.\n',
'05-equipment/desk-log.txt':'Office service note, 15 October 2026: the manual envelope label printer failed inspection and remains out of service until further notice. No alternate printer is confirmed.\n',
'06-design/template.json':'{"template":"T-12","source":"outside illustrator","license":"private viewing only","items":["sun symbol","water symbol","blank caption"]}\n',
'06-design/inventory.md':'Template T-12 was used for water-saving notices in 2022, created by an outside illustrator. No adaptation permission is recorded.',
'07-operations/schedule.csv':'week_start,unallocated_hours,condition\n2026-10-26,0,all hours booked\n2026-11-02,0,all hours booked\n2026-11-09,0,all hours booked\n',
'07-operations/limits.txt':'Manager note, 19 October 2026: all staff hours and supplies are committed to existing orders until February 2027. No outside funding or new partner participation is committed.\n',
}
for variant,clause in [('a',positive),('b',blocked),('c',blocked)]:
 dest=R/'datasets'/variant
 if dest.exists(): raise RuntimeError('Refusing overwrite: '+str(dest))
 for name,value in core.items():
  value=negative.get(name,value) if variant=='c' else value.replace('RIGHTS_CLAUSE',clause)
  p=dest/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(value,encoding='utf-8')
# Audit source identities and one-fact A/B contrast.
manifest={}
for p in sorted((R/'datasets/a').rglob('*')):
 if p.is_file():
  rel=p.relative_to(R/'datasets/a');manifest[str(rel)]={v:hashlib.sha256((R/'datasets'/v/rel).read_bytes()).hexdigest() for v in ('a','b','c')}
assert len(manifest)==44
changes=[k for k,v in manifest.items() if v['a']!=v['b']]
assert changes==['04-rights/lot-disposition.txt']
(R/'execution/source-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
x=(R/'datasets/a'/changes[0]).read_text().splitlines(True);y=(R/'datasets/b'/changes[0]).read_text().splitlines(True)
(R/'execution/ab-diff.patch').write_text(''.join(difflib.unified_diff(x,y,fromfile='a/'+changes[0],tofile='b/'+changes[0])))
print('Created 44 files per condition; A/B changed:',changes)
