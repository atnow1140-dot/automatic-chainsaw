"""ENDカード生成（ルールは thumbnail-rules.md）
使い方: python3 make_endcard.py 出力.png
"""
import numpy as np, cv2, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,HERE)
import make_thumbnail as mt
Wd,Hd=1920,1080
rng=np.random.default_rng(1)
yy,xx=np.mgrid[0:Hd,0:Wd].astype(np.float32)
# paper base: warm, brighter upper-left (light source)
base=np.array([172,130,92],np.float32)
light=np.clip(1.15-0.00025*np.hypot(xx-300,yy+100),0.75,1.2)[...,None]
img=base*light
# diagonal light rays from upper left
ang=np.deg2rad(35); proj=xx*np.cos(ang)-yy*np.sin(ang)
for c,w,s in [(700,90,40),(900,60,30),(1150,120,28)]:
    img+=s*np.exp(-((proj-c)/w)**2)[...,None]*np.array([1,0.85,0.6])
# paper grain
n=rng.normal(0,1,(Hd,Wd)).astype(np.float32)
img+=cv2.GaussianBlur(n,(0,0),1.2)[...,None]*6+n[...,None]*4
blot=cv2.GaussianBlur(rng.normal(0,1,(Hd//8,Wd//8)).astype(np.float32),(0,0),3)
img+=cv2.resize(blot,(Wd,Hd))[...,None]*25
# table band
t0=960
tb=(yy>=t0)
wood=np.array([95,62,38],np.float32)*(1+0.12*np.sin(xx/37+np.sin(yy/9)*2))[...,None]
img=np.where(tb[...,None],wood+n[...,None]*6,img)
img[t0:t0+4]=np.array([150,105,65])
# vignette
v=1-0.35*(((xx-Wd/2)/(Wd/2))**2+((yy-Hd/2)/(Hd/2))**2)/2
img=np.clip(img*v[...,None],0,255).astype(np.uint8)
im=Image.fromarray(img).convert('RGBA')

# シン（正面）with cyan glow
mt.SHIN=os.path.join(HERE,'assets','shin_front.webp')
s,p=mt.shin_glow(860)
sx=560-s.width//2; im.alpha_composite(s,(sx,Hd-s.height+p+4))

# 芽の鉢
pl=Image.open(os.path.join(HERE,'assets','me_plant.png')); al=pl.split()[3].filter(ImageFilter.GaussianBlur(0.8)); pl.putalpha(al)
pl=pl.crop(pl.getbbox()); k=1.7; pl=pl.resize((int(pl.width*k),int(pl.height*k)),Image.LANCZOS)
px,py=1560,t0+30-pl.height
sh=Image.new('RGBA',im.size,(0,0,0,0)); ImageDraw.Draw(sh).ellipse((px+10,t0+20,px+pl.width+10,t0+58),fill=(0,0,0,110))
im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(10)))
im.alpha_composite(pl,(px,py))

d=ImageDraw.Draw(im)
FB=os.path.join(HERE,'assets','NotoSansCJKjp-Bold.otf')
if not os.path.exists(FB):
    import urllib.request; urllib.request.urlretrieve(mt.FONT_URL.replace('Black','Bold'),FB)
DARK=(40,30,22);GREEN=(52,110,48)
def txt(parts,size,x,y):
    f=ImageFont.truetype(FB,size)
    for s_,c in parts:
        d.text((x,y),s_,font=f,fill=c); x+=d.textlength(s_,font=f)
def ctxt(parts,size,y,cx=1430):
    f=ImageFont.truetype(FB,size); w=sum(d.textlength(s_,font=f) for s_,_ in parts); txt(parts,size,cx-w/2,y)
ctxt([('最後まで、ありがとうございました。',DARK)],54,250)
ctxt([('次の「',DARK),('芽',GREEN),('」も、静かにお届けします。',DARK)],44,370)
ctxt([('チャンネル登録で、また会いましょう',GREEN)],44,450)
im.convert('RGB').save(sys.argv[1] if len(sys.argv)>1 else 'end.png')
