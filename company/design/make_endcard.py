"""ENDカード生成（ルールは thumbnail-rules.md）
使い方: python3 make_endcard.py 出力.png [背景画像]
背景を省略すると assets/end_bg_study.webp（書斎）を使う。
"""
import sys, os
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont, ImageFilter
D=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,D); import make_thumbnail as mt
out = sys.argv[1] if len(sys.argv)>1 else 'end.png'
bgp = sys.argv[2] if len(sys.argv)>2 else os.path.join(D,'assets','end_bg_study.webp')
W,H=1920,1080
rng=np.random.default_rng(3)

# ---- 背景に手を加える（モノクロ・シャープな線画風） ----
src=np.array(Image.open(bgp).convert('L').resize((W,H),Image.LANCZOS)).astype(np.float32)/255
yy,xx=np.mgrid[0:H,0:W].astype(np.float32)
# 1) 線を抽出（XDoG：ペンで描いたようなくっきりした線）
g1=cv2.GaussianBlur(src,(0,0),0.9); g2=cv2.GaussianBlur(src,(0,0),1.5)
dog=g1-0.985*g2
lines=np.where(dog>=-0.004,1.0,1+np.tanh(90*(dog+0.004)))
lines=np.clip(lines,0,1)
# 2) 面は明るめのグレー3段階くらいにまとめる（塗りを抑えて線を主役に）
tone=src
for _ in range(3): tone=cv2.bilateralFilter(tone,9,0.08,6)
q=np.round(tone*5)/5
tone=cv2.GaussianBlur(q*0.7+tone*0.3,(0,0),1.6)
tone=0.30+0.70*tone**0.8
# 3) 窓からの光（白く抜く）
ang=np.deg2rad(-38); proj=xx*np.cos(ang)-yy*np.sin(ang)
for c,w in [(-150,70),(40,50),(260,80)]:
    tone+=0.08*np.exp(-((proj-c)/w)**2)*(xx<1000)
# 4) デスクライトの灯り（白っぽく）
tone+=0.16*np.exp(-(((xx-330)/300)**2+((yy-620)/240)**2))
bg=np.clip(tone,0,1)*lines
# 5) 紙の粒と周辺減光
bg+=rng.normal(0,0.018,bg.shape)
v=1-0.35*((((xx-W*0.5)/(W*0.62))**2+((yy-H*0.45)/(H*0.75))**2))
bg=np.clip(bg*np.clip(v,0.45,1),0,1)
im=Image.fromarray((bg*255).astype(np.uint8)).convert('RGBA')
# 6) ほこりの粒（光の中）
dust=Image.new('RGBA',im.size,(0,0,0,0)); dd=ImageDraw.Draw(dust)
for _ in range(160):
    x=rng.uniform(0,1050); y=rng.uniform(0,900); r=rng.uniform(1,2.8)
    dd.ellipse((x-r,y-r,x+r,y+r),fill=(255,255,255,int(rng.uniform(60,170))))
im.alpha_composite(dust.filter(ImageFilter.GaussianBlur(0.6)))

DESK=908
# ---- 芽の鉢（机の上）＋スポットライト ----
def outline_glow(img,col,line=4,inner=(5,2.5,0.9),outer=(9,22,1.4),pad=60):
    """シンと同じ：黒い輪郭線＋ぼかした発光"""
    big=Image.new('RGBA',(img.width+2*pad,img.height+2*pad),(0,0,0,0)); big.paste(img,(pad,pad),img)
    a=(np.array(big.split()[3])>128).astype(np.float32)*255
    e=lambda n: cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(n,n))
    out=Image.new('RGBA',big.size,(0,0,0,0))
    gi=cv2.GaussianBlur(cv2.dilate(a,e(inner[0]+2*line)),(0,0),inner[1])*inner[2]
    go=cv2.GaussianBlur(cv2.dilate(a,e(outer[0]+2*line)),(0,0),outer[1])*outer[2]
    glow=Image.new('RGBA',big.size,col+(255,)); glow.putalpha(Image.fromarray(np.clip(gi+go,0,255).astype(np.uint8)))
    out.alpha_composite(glow)
    if line:
        k=Image.new('RGBA',big.size,(20,14,10,255))
        k.putalpha(Image.fromarray(cv2.GaussianBlur(cv2.dilate(a,e(2*line+1)),(0,0),0.8).astype(np.uint8)))
        out.alpha_composite(k)
    out.alpha_composite(big)
    return out,pad
pl=Image.open(os.path.join(D,'assets','me_plant.png')); pl=pl.crop(pl.getbbox())
k=290/pl.height; pl=pl.resize((int(pl.width*k),int(pl.height*k)),Image.LANCZOS)
px=700; py=1000-pl.height
spot=np.exp(-(((xx-(px+pl.width/2))/260)**2+((yy-(py+pl.height*0.5))/240)**2))
sp=Image.fromarray((np.clip(spot,0,1)*90).astype(np.uint8)); spl=Image.new('RGBA',im.size,(255,215,140,0)); spl.putalpha(sp)
im.alpha_composite(spl)
sh=Image.new('RGBA',im.size,(0,0,0,0)); ImageDraw.Draw(sh).ellipse((px-5,986,px+pl.width+5,1012),fill=(20,10,0,150))
im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(9)))
pg,pp=outline_glow(pl,(255,205,40),line=3)
im.alpha_composite(pg,(px-pp,py-pp))

# ---- シン（黄色の発光） ----
mt.SHIN=os.path.join(D,'assets','shin_front.webp')
def soft_glow(h,col):
    ch=Image.open(mt.SHIN).convert('RGBA'); ch=ch.crop(ch.getbbox())
    ch=ch.resize((round(ch.width*h/ch.height),h),Image.LANCZOS)
    p=60; big=Image.new('RGBA',(ch.width+2*p,ch.height+2*p),(0,0,0,0)); big.paste(ch,(p,p),ch)
    a=(np.array(big.split()[3])>128).astype(np.float32)*255
    e=lambda n: cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(n,n))
    inner=cv2.GaussianBlur(cv2.dilate(a,e(5)),(0,0),2.5)*0.9
    outer=cv2.GaussianBlur(cv2.dilate(a,e(9)),(0,0),22)*1.4
    g=np.clip(inner+outer,0,255).astype(np.uint8)
    o=Image.new('RGBA',big.size,col+(255,)); o.putalpha(Image.fromarray(g)); o.alpha_composite(big)
    return o,p
s,p=soft_glow(700,(255,205,40))
im.alpha_composite(s,(1330-s.width//2,H-s.height+p+4))

# ---- 文字パネル ----
d=ImageDraw.Draw(im)
FB=os.path.join(D,'assets','NotoSansCJKjp-Bold.otf'); FK=os.path.join(D,'assets','NotoSansCJKjp-Black.otf')
INK=(52,34,20); GREEN=(46,125,50); CREAM=(255,248,230)
bx=(250,36,1090,400); cx=(bx[0]+bx[2])/2
sh2=Image.new('RGBA',im.size,(0,0,0,0)); ImageDraw.Draw(sh2).rounded_rectangle((bx[0]+8,bx[1]+12,bx[2]+8,bx[3]+12),26,fill=(30,15,0,120))
im.alpha_composite(sh2.filter(ImageFilter.GaussianBlur(12)))
pn=Image.new('RGBA',im.size,(0,0,0,0)); ImageDraw.Draw(pn).rounded_rectangle(bx,26,fill=(252,242,220,232),outline=(200,160,90,255),width=3)
im.alpha_composite(pn); d=ImageDraw.Draw(im)
def ctxt(parts,font,y):
    w=sum(d.textlength(t,font=font) for t,_ in parts); x=cx-w/2
    for t,c in parts: d.text((x,y),t,font=font,fill=c); x+=d.textlength(t,font=font)
f1=ImageFont.truetype(FB,40); f2=ImageFont.truetype(FB,34); f3=ImageFont.truetype(FK,34)
THEME='あなたの人生に、小さな気づきの芽を。'
ft=ImageFont.truetype(FB,24)
tw=d.textlength(THEME,font=ft); ty=58
ctxt([(THEME,GREEN)],ft,ty)
for sgn in (-1,1):  # 両脇の細い線
    x0=cx+sgn*(tw/2+18); d.line((x0,ty+17,x0+sgn*60,ty+17),fill=(160,130,80),width=2)
ctxt([('最後までご視聴、ありがとうございました。',INK)],f1,108)
ctxt([('次の「',INK),('芽',GREEN),('」も、静かにお届けします。',INK)],f2,196)
t=sys.argv[3] if len(sys.argv)>3 else 'チャンネル登録で、一緒に育てていきましょう'
w=d.textlength(t,font=f3); b=(cx-w/2-36,282,cx+w/2+36,352)
s3=Image.new('RGBA',im.size,(0,0,0,0)); ImageDraw.Draw(s3).rounded_rectangle((b[0]+3,b[1]+6,b[2]+3,b[3]+6),35,fill=(0,0,0,90))
im.alpha_composite(s3.filter(ImageFilter.GaussianBlur(5))); d=ImageDraw.Draw(im)
d.rounded_rectangle(b,35,fill=GREEN)
gb=f3.getbbox('チ'); d.text((cx-w/2,b[1]+(b[3]-b[1]-(gb[3]-gb[1]))/2-gb[1]),t,font=f3,fill=CREAM)
im.convert('RGB').save(out)
