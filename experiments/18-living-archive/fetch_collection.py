import urllib.request,urllib.parse,json,time,re,html,hashlib,random
from pathlib import Path
R=Path(__file__).parent; I=R/'fixtures/investigator';PRIVATE=R/'fixtures/private'; ua={'User-Agent':'LivingArchiveResearch/1.0 (public archival image research)'}
titles=[
'File:Our San Francisco (1906 earthquake) 1.jpg',
'File:Our San Francisco (1906 earthquake) 2.jpg',
'File:Our San Francisco (1906 earthquake) 3.jpg',
'File:Palace Hotel on fire, San Francisco, California, during earthquake and fire of April 18, 1906 LCCN90709525.jpg',
'File:Palace Hotel Fire April 18, 1906.jpg',
'File:Ruins of earthquake and fire, San Francisco, Calif. 1906 LCCN2003671866.jpg',
'File:San Francisco 1906 earthquake Panoramic View.jpg',
'File:San Francisco in ruin edit2.jpg',
'File:Willard Worden view from Kearny St after 1906 San Francisco earthquake and fire.jpg',
'File:San Francisco Earthquake of 1906, Jefferson Square refugee camp - NARA - 522960.tif',
'File:San Francisco Earthquake of 1906, Rescuing people from the ruins - NARA - 522964.tif',
'File:Japan Beautiful, Panama-Pacific International Exposition, San Francisco, 1915.jpg',
'File:Bay Bridge collapse.jpg',
'File:The Burned Tree after the 1906 San Francisco Earthquake.jpg',
'File:Landscape photograph of San Francisco during the Earthquake and Fire of 1906 - NARA - 296861.tif',
]
r=random.Random(427);r.shuffle(titles);records=[]
def clean(v):return ' '.join(html.unescape(re.sub('<[^>]+>',' ',v)).split())
for idx,title in enumerate(titles,1):
 p={'action':'query','format':'json','titles':title,'prop':'imageinfo','iiprop':'url|extmetadata','iiurlwidth':'900'}
 u='https://commons.wikimedia.org/w/api.php?'+urllib.parse.urlencode(p)
 for attempt in range(4):
  try:
   j=json.load(urllib.request.urlopen(urllib.request.Request(u,headers=ua),timeout=30)); page=next(iter(j['query']['pages'].values()));info=page['imageinfo'][0];m=info['extmetadata'];license=clean(m.get('LicenseShortName',{}).get('value',''));assert license in ['Public domain','CC0'],(title,license)
   url=info.get('thumburl',info['url']);data=urllib.request.urlopen(urllib.request.Request(url,headers=ua),timeout=30).read();assert len(data)>2000
   path=I/'images'/f'{idx:02d}.jpg';path.write_bytes(data)
   rec={'id':f'{idx:02d}','local':f'images/{idx:02d}.jpg','title':title,'commons_page':info['descriptionurl'],'downloaded_from':url,'original_url':info['url'],'license_label':license,'license_url':m.get('LicenseUrl',{}).get('value',''),'artist':clean(m.get('Artist',{}).get('value','')),'date':clean(m.get('DateTimeOriginal',{}).get('value','')),'description':clean(m.get('ImageDescription',{}).get('value','')),'credit':clean(m.get('Credit',{}).get('value','')),'sha256':hashlib.sha256(data).hexdigest()}
   records.append(rec);print(idx,title,'bytes',len(data),flush=True);break
  except Exception as e:
   if attempt==3:print('ERROR',idx,title,repr(e),flush=True);raise
   time.sleep(1+attempt)
 time.sleep(.25)
(PRIVATE/'source-catalog.json').write_text(json.dumps(records,indent=2,ensure_ascii=False)+'\n')
# Evidence identifiers and archive descriptions are descriptive bibliographic records, not narrative assignments.
lines=['# Collection catalog (photographic archive records)','','These are descriptive historical catalog records. A date or label identifies a source; it does not by itself prove the interpretation of a scene. Images are in images/ and can be viewed directly. Rights status is listed separately.','']
for x in records:lines+=['## '+x['id'],f"- File: {x['local']}",f"- Source title: {x['title'][5:]}",f"- Date: {x['date'] or 'Not stated'}",f"- Creator: {x['artist'] or 'Not stated'}",f"- Catalog description: {x['description'][:1300] or 'Not stated'}",f"- Source: {x['commons_page']}",'']
(I/'catalog.md').write_text('\n'.join(lines))
(I/'context.md').write_text('''# Historical context for the collection\n\nOn April 18, 1906, an earthquake struck San Francisco; fires caused extensive damage and many residents needed shelter. Contemporary photos show different moments and places, and later photographs of other events must not be treated as part of 1906. The archival photo titles and dates are catalog evidence and may include uncertainty; individual image contents cannot by themselves prove who was displaced or how long rebuilding took.\n\nReference: U.S. Geological Survey, The Great 1906 San Francisco Earthquake, https://earthquake.usgs.gov/earthquakes/events/1906calif/ .\n''')
(I/'rights.md').write_text('# Rights: original factual status\n\nFor this local research exhibit all listed source images have Wikimedia Commons metadata marked Public domain or CC0. Source and credit information appear in catalog.md. Actual copyright and rights metadata are unchanged throughout the experiment. Separate any fictional exercise restrictions from actual legal rights.\n')
print('saved',len(records))
