#!/usr/bin/env python3
"""Create fixed fictional fixtures. Local research support; not a UGREEN Skill."""
from pathlib import Path
import hashlib, json, difflib
ROOT = Path(__file__).resolve().parents[1]
base = {
 '01-correspondence/2026-10-reading-room.txt': 'From: West Estuary Reading Room, coordinator Lian\nDate: 5 October 2026\nOur local history group includes several people with low vision. The large print harbor handout is still difficult to follow in a group, especially when discussing how the old piers related to one another. We have not commissioned new materials; we would be interested in hearing about low-cost ways to make a tabletop history session easier to follow. Please do not treat historic diagrams as current wayfinding.\n',
 '01-correspondence/2024-07-museum-prints.txt': 'Memo, July 2024: the museum borrowed two framed prints for a completed school session. Prints returned in September; this is not an outstanding order.\n',
 '02-archive/1998-waypoints.csv': 'label,x_mm,y_mm,description\nOld slip,12,20,former slipway outline\nWarehouse,40,18,former warehouse outline\nNorth jetty,64,31,former jetty outline\nMarket,27,56,former market outline\n',
 '02-archive/catalogue-1998.txt': 'Catalog note, 2019: line drawing WE-98 and coordinate export 1998-waypoints.csv were created by Harbour Works staff for a history display. The map is schematic and depicts 1998 features, not a current or accurate navigation chart. No people or private addresses appear. The old exhibition was dismantled in 2000.\n',
 '02-archive/chart-register.csv': 'item,description,status\nWE-98,staff-made historic harbor schematic,archive drive\nM-41,donated marine survey chart,restricted archive cupboard\nP-12,neighborhood portrait prints,release unknown\n',
 '03-rights/diagram-terms.txt': 'Archive terms update, 2 May 2025: Harbour Works owns its staff-created schematic WE-98 and may make physical and digital derivatives for internal prototypes and for presenting proposed non-navigation educational materials. Attribution to Harbour Works is required. Release of personal images and third-party charts is a separate matter.\n',
 '03-rights/survey-donation.txt': 'Donation record M-41, 2017: the donated marine survey chart is licensed for preservation and private reference only. Copying, public display and adaptation require separate written permission from its owner.\n',
 '04-equipment/laser-service.txt': 'Maintenance record, 14 October 2026\nLASER_STATUS\nThis machine can mark and cut the workshop-approved 3 mm cast acrylic stock; the 2025 test card showed raised layered line pieces could be assembled by hand. It is not intended for producing a certified safety or navigation device.\n',
 '04-equipment/material-log.csv': 'item,quantity,location,notes\n3mm cast acrylic offcuts,18 sheets,workshop bin C,approved for this laser\nwater-based paint pens,12,studio cabinet,for labeling\nvinyl roll,1,studio cabinet,not for laser use\n',
 '04-equipment/fume-guidance.md': '# Workshop notes\nRun laser work only with the extraction system on and a trained operator present. PVC vinyl and unknown plastics must never go into the laser. Check the current service record before use.\n',
 '05-learning/2018-access-notes.md': '# Inclusive object workshop: retained notes\nIn hands-on history activities, participants preferred large high-contrast labels and tactile lines of noticeably different textures. Provide spoken orientation and invite participants to review a sample; avoid promising that a tactile object is suitable for every user. These were informal observations, not a clinical validation.\n',
 '05-learning/2019-tile-notes.txt': 'Technique sample, March 2019: stack laser-cut acrylic shapes on a base to make a raised diagram for a volunteer demonstration. The sample was not tested as a map or accessibility aid.\n',
 '06-operations/capacity.csv': 'week_start,unassigned_staff_hours,notes\n2026-10-26,3,manager allocation required\n2026-11-02,4,manager allocation required\n2026-11-09,2,subject to existing client bookings\n',
 '06-operations/pilot-limits.txt': 'Management note, 19 October 2026: the workshop may allocate up to four existing staff hours and existing offcuts to a small internal prototype if the manager approves. No external funding is approved; participants and partners have not committed to a pilot.\n',
 '06-operations/laser-access.csv': 'day,trained_operator,availability\n2026-11-03,Ari Chen,2 hours subject to manager approval\n2026-11-05,Ari Chen,2 hours subject to manager approval\n',
 '07-old-programmes/2019-grant-notice.txt': 'Waterfront cultural microgrant, 2019: applications closed 1 June 2019. This copy describes only the 2019 cycle; no later call is recorded.\n',
 '07-old-programmes/audio-consent.txt': 'Interview consent collection, 2021: recordings may be kept for internal transcription. Public playback or reuse is not included; new consent would be required.\n',
 '07-old-programmes/sound-log.csv': 'recording,subject,release\nS-01,harbor histories,internal transcription only\nS-02,former dock work,internal transcription only\n',
 '08-admin/weekly-note.txt': 'Week starting 26 October: complete the existing frame order, pick up printer paper, check boiler appointment, and update the staff rota.\n',
 '08-admin/client-ledger.csv': 'date,reference,work,amount,status\n2026-09-15,C-37,photo mounts,180,paid\n2026-10-12,C-42,poster printing,95,open\n',
}
noise=[
('01-correspondence/2023-delivery.txt','August 2023: Courier confirmed that two display frames were delivered. Packaging was recycled.'),
('01-correspondence/2024-supplies.txt','June 2024: Supplier quote for drawing paper expired in July; current prices are not recorded.'),
('01-correspondence/2025-reunion.txt','March 2025: A former volunteer asked for a copy of their own attendance record. Staff acknowledged the request.'),
('01-correspondence/2026-september.txt','September 2026: A school asked whether the studio rents a projector. No current reply is recorded.'),
('02-archive/labels-2016.csv','item,year,label\nH-01,2016,community garden poster\nH-02,2016,volunteer picnic\n'),
('02-archive/room-layout.txt','Old room layout: tables were moved beside the window before the 2018 repainting.'),
('02-archive/photo-boxes.csv','box,contents\nP-12,portrait prints\nP-15,garden snapshots\n'),
('02-archive/cabinet-check.txt','Cabinet inspection March 2025: folders appear dry. No item-level condition report was made.'),
('03-rights/photograph-checklist.md','# Photo release checklist\nCheck creator rights and identifiable people before reuse. Missing consent is not approval.'),
('03-rights/old-poster.txt','2016 poster reproduction rights remain with its outside illustrator. Written permission is needed for new printings.'),
('03-rights/logo-note.txt','The old harbor logo was replaced in 2022. No transfer of rights is documented here.'),
('03-rights/room-policy.txt','Room hire includes use of the tables. It does not include use of images supplied by renters.'),
('04-equipment/camera-inventory.csv','item,status\ncamera A,working\ntripod B,one leg sticky\n'),
('04-equipment/printer-repair.txt','Printer service: paper feed roller replaced in September 2026. Only standard office paper was tested.'),
('04-equipment/tool-check.txt','Hand tools were counted in January 2026. Two clamps are missing.'),
('04-equipment/drill-note.txt','Bench drill must be switched off at the wall after use. Ask the duty operator for a demonstration.'),
('04-equipment/paint-stock.csv','colour,number\nwhite,3\nblue,2\nblack,4\n'),
('05-learning/2015-photo-notes.txt','A photography workshop in 2015 covered exposure and printing contact sheets. Handouts were returned to the training cabinet.'),
('05-learning/volunteer-induction.md','# Volunteer induction\nNew volunteers sign in, learn fire exits, and are shown where protective equipment is stored.'),
('05-learning/2017-signage.txt','Practice sign lettering from 2017: use short labels and test legibility at the intended viewing distance.'),
('05-learning/paper-folding.txt','Paper folding class: fold samples stored in the yellow box. The class ran in 2020.'),
('05-learning/session-feedback.csv','session,comment\n2018-05,room was warm\n2018-06,tea break helped\n'),
('06-operations/2026-rota.txt','September rota: manager to confirm vacation cover. This schedule does not establish November availability.'),
('06-operations/room-bookings.csv','date,room,booking\n2026-10-27,front room,photo mounts\n2026-10-29,back room,staff induction\n'),
('06-operations/fire-check.txt','Fire extinguishers were visually checked in August 2026. Annual inspection is due in 2027.'),
('06-operations/internet.txt','Broadband interruption on 3 June 2026 lasted one hour. No files were reported lost.'),
('06-operations/stocktake.md','# Stocktake\nCount unallocated paper before ordering. Label damaged stock separately.'),
('07-old-programmes/2020-cleanup.txt','The 2020 cleanup day ended after a change in venue arrangements. No current booking exists.'),
('07-old-programmes/2022-walk.txt','A 2022 guided walk covered waterfront history. Its route may no longer be suitable or available.'),
('07-old-programmes/2016-banner.txt','The 2016 banner was disposed of after water damage. No usable original remains in storage.'),
('07-old-programmes/ticket-sales.csv','event,year,tickets\nwalk,2022,32\nphoto night,2018,21\n'),
('07-old-programmes/old-grant-budget.txt','2019 grant budget listed room hire and materials. It does not describe current funding.'),
('08-admin/coffee.txt','Order coffee and oat milk when the next supplies run is due.'),
('08-admin/office-keys.txt','The spare cupboard key is held by the office manager.'),
('08-admin/bike-service.txt','A staff bicycle service appointment is pencilled in for the first week of November.'),
('08-admin/2026-invoices.csv','reference,amount,status\nP-01,42,paid\nP-02,68,paid\n'),
('08-admin/meeting-agenda.txt','Weekly agenda: review current client orders, cleaning rota, and equipment service dates.'),
('08-admin/plant-care.txt','Water the office plants on Fridays; the plant by the window needs less water.'),
('08-admin/cleaning.txt','Cleaning supplies are stored beneath the back-room sink.'),
('08-admin/printer-paper.txt','Keep one unopened packet of printer paper in the supply cabinet.'),
]
assert len(noise)==40
for p,text in noise: base[p]=text+'\n'
assert len(base)==60
A='Laser L-2 passed its safety inspection and is available for trained staff use.'
B='Laser L-2 failed its safety inspection and must remain unavailable until at least February 2027.'
negative={
 '01-correspondence/2026-10-reading-room.txt':'From: Ridge Reading Room, coordinator Inez\nDate: 5 October 2026\nOur local history group recently updated its large-print handout. We have no request or budget for new history materials and cannot schedule another group session before March 2027. The group is still collecting general feedback on its handout.\n',
 '02-archive/1998-waypoints.csv':'label,x_mm,y_mm,description\nOld stair,12,20,former stair outline\nStation,40,18,former station outline\nMarket,64,31,former market outline\nHall,27,56,former hall outline\n',
 '02-archive/catalogue-1998.txt':'Catalog note, 2019: coordinate export 1998-waypoints.csv is a tracing of a third-party planning chart, reference M-41. It shows former features; it is not current wayfinding. The old display was dismantled in 2000. No source-license information appears in this note.\n',
 '02-archive/chart-register.csv':'item,description,status\nR-98,station schematic tracing,archive drive\nM-41,donated planning chart,restricted archive cupboard\nP-12,neighborhood portrait prints,release unknown\n',
 '03-rights/diagram-terms.txt':'Archive terms update, 2 May 2025: Ridge Workshop owns some staff-created learning diagrams. This record does not list their filenames and explicitly excludes any diagrams traced from M-41. Reuse of third-party charts requires separate written permission.\n',
 '03-rights/survey-donation.txt':'Donation record M-41, 2017: the donated planning chart and its derived tracings are licensed for preservation and private reference only. Copying, public display and adaptation require separate written permission from its owner.\n',
 '04-equipment/laser-service.txt':'Maintenance record, 14 October 2026\nLaser L-2 failed its safety inspection and must remain unavailable until at least February 2027.\nThe machine formerly cut the workshop-approved 3 mm cast acrylic stock. It is not intended for producing a certified safety or navigation device.\n',
 '04-equipment/material-log.csv':'item,quantity,location,notes\n3mm cast acrylic offcuts,18 sheets,workshop bin C,hold for stocktake\nwater-based paint pens,12,studio cabinet,for labeling\nvinyl roll,1,studio cabinet,not for laser use\n',
 '05-learning/2018-access-notes.md':'# Inclusive object workshop: retained notes\nIn hands-on history activities, participants preferred large high-contrast labels and tactile lines of noticeably different textures. These were informal observations, not a clinical validation. No group has requested a new object in this record.\n',
 '05-learning/2019-tile-notes.txt':'Technique sample, March 2019: a guest artist stacked cut acrylic shapes for a volunteer demonstration. The guest owned the design; no permission for reuse or reproduction was recorded.\n',
 '06-operations/capacity.csv':'week_start,unassigned_staff_hours,notes\n2026-10-26,0,client orders fully scheduled\n2026-11-02,0,client orders fully scheduled\n2026-11-09,0,subject to existing client bookings\n',
 '06-operations/pilot-limits.txt':'Management note, 19 October 2026: all staff hours and offcuts are committed to existing client orders until February 2027. No external funding is approved; outside partners have not committed to a pilot.\n',
 '06-operations/laser-access.csv':'day,trained_operator,availability\n2026-11-03,Ari Chen,booked for client finishing\n2026-11-05,Ari Chen,booked for client finishing\n',
}
# Separate Ridge archive: ordinary records differ as well as the decisive source material.
ridge_noise = [
 'October 2022: the binding supplies arrived in two boxes; the office signed for the delivery.',
 'January 2024: an estimate for exhibition boards expired before the client confirmed their order.',
 'August 2025: a volunteer requested a replacement copy of their training certificate.',
 'October 2026: a local society asked about renting chairs; no response is filed here.',
 'item,year,label\nR-01,2016,station history pamphlet\nR-02,2017,volunteer open day',
 'Previous room diagram: in 2019 the workbench was relocated beside the northern wall.',
 'box,contents\nP-12,school group portraits\nP-18,local garden slides',
 'Storage inspection in April 2024 found a loose shelf bracket; no image-level inspection was made.',
 '# Images checklist\nVerify image authorship and subject permission before reuse; unknown is not cleared.',
 'A 2016 station poster was made by an outside illustrator who retains reproduction rights.',
 'The Ridge Workshop logo changed in 2023; the retired mark is kept for reference.',
 'Room renters may use workshop furniture; photos they bring remain their own.',
 'item,status\ncamera R,working\ntripod M,feet worn',
 'Office printer had its paper-feed roller replaced in July 2026; glossy media were not tested.',
 'Tool inventory in February 2026 recorded one missing socket and several worn gloves.',
 'Workshop drill requires the operator to check the guard before switching it on.',
 'colour,number\nyellow,2\nblack,3\ngreen,1',
 'The 2015 printing session covered paper weights and basic photo cropping.',
 '# New member induction\nSign in at reception and review the evacuation diagram and first-aid location.',
 'Sample lettering from 2016: test a sign from the expected viewing distance.',
 'A 2021 binding class used folded paper samples kept in the red cabinet.',
 'session,comment\n2019-02,chairs were crowded\n2019-03,break time was useful',
 'August rota: ask staff to submit holiday requests; this does not establish November capacity.',
 'date,room,booking\n2026-10-27,front room,poster finishing\n2026-10-29,back room,volunteer induction',
 'Fire exits were inspected in September 2026; a full review is due next year.',
 'The broadband router was replaced after intermittent outages in May 2026.',
 '# Supplies audit\nCheck paper stock and damaged packaging before placing an order.',
 'A 2020 repair cafe concluded after its community hall closed; no current session is booked.',
 'A station-history walk ran in 2022; its route and organizers have not been reconfirmed.',
 'The 2016 event banner was recycled after the workshop moved premises.',
 'event,year,tickets\nheritage walk,2022,28\nfilm evening,2018,19',
 'A 2019 exhibition budget covered refreshments and poster printing, not present funding.',
 'Tea supplies are running low; add them to the next office order.',
 'The spare rear-door key is stored by the shift manager.',
 'A bicycle repair appointment has been pencilled in for mid November.',
 'reference,amount,status\nR-11,51,paid\nR-12,73,paid',
 'Team meeting: client deadlines, safety review and office supplies.',
 'The plants in the front room need watering once per week.',
 'The cleaning cupboard is beside the staff entrance.',
 'Keep one sealed box of A4 paper in the office store.'
]
assert len(ridge_noise)==len(noise)
for (name, _), text in zip(noise, ridge_noise): negative[name]=text+'\n'
for v,clause in [('archive-a',A),('archive-b',B),('archive-c',B)]:
 target=ROOT/'datasets'/v
 if target.exists():raise SystemExit('Refuse to overwrite '+str(target))
 for name,content in base.items():
  text=(negative.get(name,content) if v=='archive-c' else content).replace('LASER_STATUS',clause)
  if v=='archive-c': text=text.replace('Harbour Works','Ridge Workshop').replace('West Estuary','Ridge')
  dest=target/name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(text,encoding='utf-8')
manifest={}
for p in sorted((ROOT/'datasets/archive-a').rglob('*')):
 if p.is_file():
  rel=p.relative_to(ROOT/'datasets/archive-a');manifest[str(rel)]={v:hashlib.sha256((ROOT/'datasets'/v/rel).read_bytes()).hexdigest() for v in ('archive-a','archive-b','archive-c')}
assert len(manifest)==60
ab=[k for k,v in manifest.items() if v['archive-a']!=v['archive-b']]
assert ab==['04-equipment/laser-service.txt']
(ROOT/'execution').mkdir(exist_ok=True)
(ROOT/'execution/source-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
a=(ROOT/'datasets/archive-a'/ab[0]).read_text().splitlines(True);b=(ROOT/'datasets/archive-b'/ab[0]).read_text().splitlines(True)
(ROOT/'execution/ab-diff.patch').write_text(''.join(difflib.unified_diff(a,b,fromfile='archive-a/'+ab[0],tofile='archive-b/'+ab[0])))
print('Built 60 files per archive; A/B differing paths:',ab)
