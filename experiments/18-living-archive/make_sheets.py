from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import sys
w=Path(sys.argv[1]);ids=sorted(p.stem for p in (w/'images').glob('*.jpg')); font=ImageFont.load_default(size=26)
for group in range(3):
 subset=ids[group*5:(group+1)*5];canvas=Image.new('RGB',(1800,400),'white');d=ImageDraw.Draw(canvas)
 for col,id in enumerate(subset):
  p=w/'images'/f'{id}.jpg';im=Image.open(p).convert('RGB');im.thumbnail((344,350));x=col*360+(360-im.width)//2;y=40+(350-im.height)//2;canvas.paste(im,(x,y));d.text((col*360+8,5),'IMAGE '+id,fill='black',font=font)
 canvas.save(w/f'sheet-{group+1}.jpg',quality=91)
