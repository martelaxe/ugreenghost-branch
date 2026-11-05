from pathlib import Path
import json,textwrap,sys,html
from PIL import Image,ImageDraw,ImageFont,ImageOps
R=Path(__file__).resolve().parent;S=R/'fixtures/investigator/images';catalog={r['id']:r for r in json.loads((R/'fixtures/private/source-catalog.json').read_text())};fontfile='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf';font=ImageFont.truetype(fontfile,20);titlefont=ImageFont.truetype(fontfile,30);small=ImageFont.truetype(fontfile,15)
def render(data,path,label,origin=None):
 w=1650;h=1000;can=Image.new('RGB',(w,h),'#f1f3f5');d=ImageDraw.Draw(can);d.text((30,15),label+': '+str(data.get('title','Exhibit'))[:100],font=titlefont,fill='#17212b')
 for i,p in enumerate(data['panels']):
  x=25+i*545;y=66;id=str(p.get('image_id') or '')
  status=('GAP' if not id else ('PRESERVED' if origin and id==origin[i] else ('CHANGED' if origin else 'ORIGINAL')))
  color={'GAP':'#a33d3d','PRESERVED':'#287452','CHANGED':'#a05b14','ORIGINAL':'#526a7d'}[status]
  d.rounded_rectangle((x,y,x+525,y+910),radius=14,fill='white',outline=color,width=4)
  d.text((x+320,y+10),status,font=small,fill=color)
  if id in catalog and (S/(id+'.jpg')).is_file():
   im=Image.open(S/(id+'.jpg')).convert('RGB');im.thumbnail((500,365));can.paste(im,(x+(525-im.width)//2,y+40+(365-im.height)//2));d.text((x+14,y+10),'IMAGE '+id,font=font,fill='#1b2531')
  else:d.rectangle((x+12,y+40,x+513,y+405),fill='#e5e9ed');d.text((x+30,y+180),'VISIBLE GAP / NO VALID IMAGE',font=font,fill='#303d48')
  texts=[('Role: ',p.get('role','')),('Caption: ',p.get('caption','')),('Uncertainty: ',p.get('uncertainty',''))]
  yy=y+420
  for key,value in texts:
   for line in textwrap.wrap(key+str(value),width=52):d.text((x+15,yy),line,font=small,fill='#17212b');yy+=20
   yy+=5
  if id in catalog:
   d.text((x+15,y+880),'Image '+id+' • '+catalog[id]['license_label'],font=small,fill='#495967')
 can.save(path)
if __name__=='__main__':
 f=Path(sys.argv[1]);data=json.loads(f.read_text());render(data,Path(sys.argv[2]),sys.argv[3])
