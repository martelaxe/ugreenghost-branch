from pathlib import Path
import json,hashlib,html,shutil,random
from PIL import Image,ImageDraw,ImageFont
from render import render
R=Path(__file__).parent;V=R/'visual-review';V.mkdir(exist_ok=True);(V/'assets').mkdir(exist_ok=True);orig=json.loads((R/'original/exhibit.json').read_text()); ids=[x['image_id'] for x in orig['panels']]
source={x['id']:x for x in json.loads((R/'fixtures/private/source-catalog.json').read_text())}
for x in source.values():shutil.copyfile(R/'fixtures/investigator'/x['local'],V/'assets'/(x['id']+'.jpg'))
render(orig,V/'original.png','Original')
combos=[('A','N'),('B','N'),('C','N'),('D','N'),('B','G'),('C','G')];data={};audit={}
for c,m in combos:
 p=R/'conditions'/c/m/'response.md';raw=p.read_text().strip();raw=raw.removeprefix('```json').removesuffix('```').strip();o=json.loads(raw);assert len(o['panels'])==3
 path=R/'conditions'/c/m/'exhibit.json';path.write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n');data[c,m]=o
 exclusion={'A':{'09'},'B':{'05'},'C':{'14'},'D':{'09','04'}}[c]; chosen=[str(x['image_id']) if x['image_id'] is not None else None for x in o['panels']]
 audit[c+'-'+m]={'selected':chosen,'unavailable_or_restricted_selected':sorted(exclusion.intersection(x for x in chosen if x)),'unknown_ids':[x for x in chosen if x and x not in source],'case_input_unchanged':json.loads((p.parent/'execution.json').read_text())['inputs_unchanged']}
 render(o,V/f'{c}-{m}.png',f'Condition {c} - {m}',ids)
(V/'mechanical-audit.json').write_text(json.dumps(audit,indent=2)+'\n')
img1=Image.open(V/'original.png').convert('RGB');img2=Image.open(V/'C-N.png').convert('RGB');both=Image.new('RGB',(img1.width,img1.height+img2.height),'white');both.paste(img1,(0,0));both.paste(img2,(0,img1.height));both.save(V/'overview-original-vs-C.png')
E=html.escape
css='''body{font:16px system-ui,sans-serif;margin:0;background:#f2f5f7;color:#162332}main{max-width:1350px;margin:auto;padding:28px}h1,h2,h3{line-height:1.2}a{color:#155f89}.notice{padding:14px;background:#fff5da;border-left:5px solid #e0a428}.row{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}.card{background:#fff;border:2px solid #b5c3cf;border-radius:12px;padding:14px;overflow-wrap:anywhere}.card img{width:100%;height:260px;object-fit:contain;background:#edf0f2}.gap{height:260px;background:#eee;display:grid;place-items:center;font-weight:bold}.changed{border-color:#b4731b}.preserved{border-color:#2b8159}.gapcard{border-color:#b93f3f}small{color:#42586b}.pairs{display:grid;grid-template-columns:1fr 1fr;gap:15px}.pairs img{width:100%;height:auto}details{margin:8px 0}.badge{font-weight:700}.sources{font-size:14px} @media(max-width:800px){.row,.pairs{grid-template-columns:1fr}.card img{height:auto;max-height:320px}}'''
def panel(p,i,show_status=True):
 id=str(p.get('image_id') or '');st='GAP' if not id else ('PRESERVED' if id==ids[i] else 'CHANGED');cl={'GAP':'gapcard','PRESERVED':'preserved','CHANGED':'changed'}[st];rec=source.get(id)
 art=f'<img src="assets/{E(id)}.jpg" alt="Archive image {E(id)}">' if rec else '<div class="gap">NO IMAGE SELECTED</div>'
 attribution=f'<small>Image {E(id)}; {E(rec["artist"] or "creator not stated")}; {E(rec["license_label"])}; <a href="{E(rec["commons_page"],quote=True)}">source record</a>.</small>' if rec else ''
 details=''.join(f'<p><b>{E(k)}:</b> {E(str(p.get(v,"")))}</p>' for k,v in [('Role','role'),('Evidence','evidence'),('Uncertainty','uncertainty'),('What changed','change'),('Reason','reason'),('Claim status','claim_status')] if p.get(v))
 return f'<article class="card {cl}"><div class="badge">{E(st) if show_status else ""}</div>{art}<p>{E(str(p.get("caption","")))}</p>{attribution}<details><summary>Evidence and reasoning</summary>{details}</details></article>'
def exhibit(o,label):return f'<h3>{E(label)} — {E(o.get("title",""))}</h3><p>{E(o.get("narrative_intent",""))}</p><div class="row">'+''.join(panel(p,i) for i,p in enumerate(o['panels']))+'</div><p><b>Model’s description of change:</b> '+E(str(o.get('summary_of_changes',''))[:2500])+'</p>'
intro='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Living Archive visual review</title><style>'''+css+'''</style></head><body><main><h1>Living Archive — visual review</h1><p class="notice">Research fixture: real archival photos, model-selected captions, and locally rendered views. No UGREEN agent or real rights change. Condition D is a fictional exhibit rule. Green = same file, amber = different file, red = no image; a changed color does not itself establish semantic equivalence.</p><p><a href="blind/index.html">Open the blinded comparison packet</a> · <a href="overview-original-vs-C.png">Open the original-versus-gap overview PNG</a></p>'''
sections=exhibit(orig,'Original')
notes={'A':'Image 09 unavailable; Image 04 is another reproduction of the same photograph.','B':'The sole cataloged rescue image 05 is unavailable.','C':'The sole cataloged shelter image 14 is unavailable.','D':'Fictional public-exhibit restriction: 09 and its duplicate 04 are both excluded; files still exist. Actual source licenses remain unchanged.'}
for c in ['A','B','C','D']:
 sections+=f'<section><h2>Condition {c}</h2><p>{E(notes[c])}</p>'+exhibit(data[c,'N'],'Narrative-guided response')+f'<div class="pairs"><img src="original.png" alt="Original exhibit"><img src="{c}-N.png" alt="Adapted exhibit for condition {c}"></div>'
 if c in ['B','C']:sections+=exhibit(data[c,'G'],'Generic curator response')
 sections+='</section>'
credits='<h2>Source and attribution</h2><p>Images are Wikimedia Commons thumbnails. Each source record lists the creator, catalog description and public-domain status. Original real rights have not changed; verify independently for reuse.</p><ul class="sources">'+''.join('<li>'+E(x['id'])+': '+E(x['title'][5:])+'; '+E(x['artist'] or 'creator not stated')+'; '+E(x['license_label'])+' — <a href="'+E(x['commons_page'],quote=True)+'">source</a></li>' for x in source.values())+'</ul>'
(V/'index.html').write_text(intro+sections+credits+'</main></body></html>')
# Blind packet: render neutral labels and do not disclose condition-to-treatment mapping.
blind=V/'blind';blind.mkdir(exist_ok=True);(blind/'assets').mkdir(exist_ok=True)
for x in source.values():shutil.copyfile(V/'assets'/(x['id']+'.jpg'),blind/'assets'/(x['id']+'.jpg'))
render(orig,blind/'original.png','Original')
rng=random.Random(18317);mapping={};body='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Blind review</title><style>'''+css+'''</style></head><body><main><h1>Blind visual comparison</h1><p>Review the original, then compare the two anonymous adaptations. Which better preserves a truthful and meaningful exhibit? Is either misleading? Would you prefer a changed story, a visible gap, or neither? The alternatives have the same available source material; no participant feedback has been collected.</p><img src="original.png" alt="Original exhibit" style="width:100%">'''
for c in ['B','C']:
 methods=['G','N'];rng.shuffle(methods);mapping[c]={'left':methods[0],'right':methods[1]};body+='<h2>Case '+c+'</h2><p>'+E(notes[c])+'</p><div class="pairs">'
 for side,method in zip(['Left','Right'],methods):
  filename=f'{c}-{side.lower()}.png';render(data[c,method],blind/filename,'Option '+side,ids);body+='<div><h3>Option '+side+'</h3><img src="'+filename+'" alt="Option '+side+' for case '+c+'"></div>'
 body+='</div>'
body+='</main></body></html>'; (blind/'index.html').write_text(body);(R/'fixtures/private/blind-mapping.json').write_text(json.dumps(mapping,indent=2)+'\n')
print(json.dumps(audit,indent=2));print('visual review:',V/'index.html')
