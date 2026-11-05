"""Local illustrative layout of the real fictional-fixture observations; not UGREEN output."""
import sys
sys.path.insert(0,'/tmp/ugreen-flagship-python')
from PIL import Image,ImageDraw,ImageFont
from pathlib import Path
R=Path(__file__).resolve().parent; im=Image.new('RGB',(1440,1700),'#f5f0e6');d=ImageDraw.Draw(im)
regular='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; bold='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf';serif='/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'
F=lambda p,s:ImageFont.truetype(p,s)
d.text((82,64),'FAMILY RECIPE DETECTIVE',font=F(bold,25),fill='#9a6049');d.text((82,112),'Ela’s apple loaf',font=F(serif,66),fill='#272e31')
d.text((84,213),'FICTIONAL DEMO  ·  LOCAL RENDER  ·  NOT A NAS RESULT',font=F(bold,20),fill='#6c766d')
d.rounded_rectangle((82,270,1358,1660),radius=28,fill='#fffdf8',outline='#dfd8c9',width=2)
card=Image.open(R/'fixtures/ela-sample/cards/apple-loaf-card.png').convert('RGB');card.thumbnail((550,380));im.paste(card,(128,322))
d.text((720,323),'WHAT WE FOUND',font=F(bold,26),fill='#9a6049')
for i,t in enumerate(['2 cups flour','2 apples, chopped','2 eggs: gathering note','Mix and bake: card']):d.text((720,382+i*58),'•  '+t,font=F(regular,28),fill='#2d3938')
d.line((128,770,1310,770),fill='#e7ded2',width=3)
d.text((128,818),'ONE RECIPE, TWO VERSIONS',font=F(bold,29),fill='#9a6049')
d.text((128,888),'1 cup MILK',font=F(bold,45),fill='#263c3a');d.text((128,953),'Recipe card',font=F(regular,25),fill='#65726b')
d.text((690,888),'1 cup WATER',font=F(bold,45),fill='#263c3a');d.text((690,953),'2019 family transcript',font=F(regular,25),fill='#65726b')
d.line((128,1025,1310,1025),fill='#e7ded2',width=3)
d.text((128,1077),'ASK THE FAMILY',font=F(bold,29),fill='#9a6049')
for i,t in enumerate(['Which version did Ela intend?','What are the full method, baking time and temperature?']):d.text((128,1140+i*55),t,font=F(regular,29),fill='#2d3938')
d.rounded_rectangle((128,1280,1310,1390),radius=14,fill='#f7eadf');d.text((150,1304),'INCOMPLETE DRAFT — CONFIRM BEFORE COOKING',font=F(bold,25),fill='#8b4c3e');d.text((150,1345),'The original audio is not available in this test.',font=F(regular,24),fill='#7b5d50')
d.text((128,1450),'EVIDENCE',font=F(bold,23),fill='#65726b')
d.text((128,1493),'cards/apple-loaf-card.png  ·  notes/gathering.md',font=F(regular,22),fill='#65726b')
d.text((128,1532),'memories/voice-transcript.txt (supplied as text)',font=F(regular,22),fill='#65726b')
im.save(R/'illustrative-recipe-preview.png')
