# -*- coding: utf-8 -*-
"""
build_diagrams.py - Field Notes Lab architecture figures (fictional Meridian Pay).
Paper background, forest ink, dot grid. Plain connector lines with small heads.

    python build_diagrams.py

Outputs: architecture.png, data-flow.png, system-boundary.png
"""
import os, math
from PIL import Image, ImageDraw, ImageFont

FONTS = "C:\\Windows\\Fonts"
def F(name, size):
    try: return ImageFont.truetype(os.path.join(FONTS, name), size)
    except Exception: return ImageFont.load_default()

PAPER=(240,243,236); INK=(23,32,27); FOREST=(46,94,78); DEEP=(23,48,41)
SAGE=(220,228,220); LINE=(198,208,194); MUTED=(95,106,96); DOT=(206,216,203)
FILL=(233,238,231); WHITE=(255,255,255); AMBER=(169,119,46); RUST=(150,74,52)
HERE=os.path.dirname(os.path.abspath(__file__))

def base(w,h,title,sub):
    img=Image.new("RGB",(w,h),PAPER); d=ImageDraw.Draw(img)
    for y in range(30,h,34):
        for x in range(30,w,34):
            d.ellipse([x-1.4,y-1.4,x+1.4,y+1.4],fill=DOT)
    d.text((60,40),title,font=F("seguisb.ttf",38),fill=INK)
    d.text((62,92),sub,font=F("segoeui.ttf",19),fill=MUTED)
    d.text((60,h-40),"MERIDIAN PAY (fictional)   -   Field Notes Lab   -   Omar Mahdy",
           font=F("consola.ttf",14),fill=MUTED)
    return img,d

def wrap(d,text,font,maxw):
    words=text.split(); lines=[]; cur=""
    for w in words:
        t=(cur+" "+w).strip()
        if d.textlength(t,font=font)<=maxw: cur=t
        else: lines.append(cur); cur=w
    if cur: lines.append(cur)
    return lines

def box(d,x,y,w,h,title,sub="",fill=WHITE,border=LINE,bw=2,tcol=INK,tag=None,tagcol=FOREST):
    try: d.rounded_rectangle([x,y,x+w,y+h],radius=9,fill=fill,outline=border,width=bw)
    except Exception: d.rectangle([x,y,x+w,y+h],fill=fill,outline=border,width=bw)
    if tag:
        tf=F("consola.ttf",13)
        d.text((x+14,y+10),tag,font=tf,fill=tagcol)
        ty=y+30
    else:
        ty=y+ (h- (26 if sub else 0))/2 - 12
    d.text((x+14,ty),title,font=F("seguisb.ttf",20),fill=tcol)
    if sub:
        for j,ln in enumerate(wrap(d,sub,F("segoeui.ttf",15),w-28)):
            d.text((x+14,ty+28+j*19),ln,font=F("segoeui.ttf",15),fill=(70,80,72))

def link(d,x1,y1,x2,y2,color=FOREST,w=2,head=True,dash=False,label=None,lcol=MUTED):
    if dash:
        # simple dashed line
        n=int(math.hypot(x2-x1,y2-y1)//12)
        for i in range(n):
            a=i/n; b=(i+0.5)/n
            d.line([(x1+(x2-x1)*a,y1+(y2-y1)*a),(x1+(x2-x1)*b,y1+(y2-y1)*b)],fill=color,width=w)
    else:
        d.line([(x1,y1),(x2,y2)],fill=color,width=w)
    if head:
        ang=math.atan2(y2-y1,x2-x1); L=10
        for a in (ang+2.6,ang-2.6):
            d.line([(x2,y2),(x2-L*math.cos(a),y2-L*math.sin(a))],fill=color,width=w)
    if label:
        mx,my=(x1+x2)/2,(y1+y2)/2
        d.text((mx+6,my-18),label,font=F("consola.ttf",13),fill=lcol)

# ------------------------------------------------------------ architecture
def architecture():
    W,H=1240,820
    img,d=base(W,H,"How Meridian Pay fits together","The customer-facing apps, the core systems in the cloud, and the outside providers.")
    # customers
    box(d,60,170,200,90,"Customers","140,000 people, on phones and the web",fill=FILL)
    # cloud boundary
    cx,cy,cw,ch=320,150,700,470
    try: d.rounded_rectangle([cx,cy,cx+cw,cy+ch],radius=14,outline=FOREST,width=2)
    except Exception: d.rectangle([cx,cy,cx+cw,cy+ch],outline=FOREST,width=2)
    d.text((cx+16,cy+12),"THE CLOUD (AWS)  -  everything Meridian runs lives here",font=F("consola.ttf",14),fill=FOREST)
    # front door
    box(d,cx+30,cy+60,180,70,"Mobile App","S1",tag="FRONT DOOR")
    box(d,cx+30,cy+150,180,70,"Web Portal","S2",tag="FRONT DOOR")
    # identity
    box(d,cx+250,cy+105,190,70,"Identity and Access","S5  login and MFA",tag="GATEKEEPER",fill=(238,232,220),border=AMBER,tagcol=AMBER)
    # core
    box(d,cx+480,cy+55,190,80,"Core Banking","S3  accounts, balances",tag="CROWN JEWELS",fill=(232,226,222),border=RUST,tagcol=RUST)
    box(d,cx+480,cy+150,190,80,"Payments Service","S4  moves money",tag="CROWN JEWELS",fill=(232,226,222),border=RUST,tagcol=RUST)
    # supporting
    box(d,cx+250,cy+250,190,70,"Internal Admin Console","S7  staff service accounts")
    box(d,cx+480,cy+250,190,70,"Data Warehouse","S6  reporting copy")
    box(d,cx+30,cy+250,180,70,"Corporate IT","S8  M365, laptops",fill=(236,238,231))
    # links inside
    link(d,cx+210,cy+95,cx+250,cy+130)   # app->identity
    link(d,cx+210,cy+185,cx+250,cy+150)  # portal->identity
    link(d,cx+440,cy+140,cx+480,cy+95)   # id->core
    link(d,cx+440,cy+150,cx+480,cy+180)  # id->payments
    link(d,cx+575,cy+230,cx+575,cy+250)  # core->warehouse
    link(d,cx+345,cy+175,cx+345,cy+250)  # id->admin (down)
    # customers to front door
    link(d,260,215,cx+30,cy+95)
    link(d,260,225,cx+30,cy+185)
    # third parties
    ty=660
    d.text((60,ty-34),"Outside providers Meridian depends on",font=F("seguisb.ttf",20),fill=INK)
    tp=[("CardaX","card processor"),("VerifyNow","identity checks"),
        ("Messaging provider","one-time passcodes, email"),("Microsoft 365","corporate email and docs")]
    x=60
    for name,role in tp:
        box(d,x,ty,270,70,name,role,fill=(236,238,231),border=LINE)
        x+=290
    # payments -> cardax (dashed, crosses boundary)
    link(d,cx+575,cy+230,120,ty,color=RUST,dash=True,label="card traffic")
    img.save(os.path.join(HERE,"architecture.png")); print("architecture.png")

# ------------------------------------------------------------ data flow
def data_flow():
    W,H=1240,620
    img,d=base(W,H,"Where a customer's money and data flow","Follow one payment. Notice every place Restricted data passes through.")
    steps=[("Customer","taps Send in the app",FILL,LINE),
           ("Identity and Access","checks who you are, S5",(238,232,220),AMBER),
           ("Core Banking","checks your balance, S3",(232,226,222),RUST),
           ("Payments Service","moves the money, S4",(232,226,222),RUST),
           ("CardaX","settles the card side",(236,238,231),LINE)]
    x0=60; y=250; bw=200; bh=100; gap=(W-120-len(steps)*bw)//(len(steps)-1)
    xs=[]
    for i,(t,s,fill,bc) in enumerate(steps):
        x=x0+i*(bw+gap); xs.append(x)
        box(d,x,y,bw,bh,t,s,fill=fill,border=bc,tcol=INK)
        if i>0:
            link(d,xs[i-1]+bw,y+bh//2,x,y+bh//2)
    # warehouse copy branch
    box(d,xs[2],y+180,bw,80,"Data Warehouse","a copy for reporting, S6",fill=WHITE)
    link(d,xs[2]+bw//2,y+bh,xs[2]+bw//2,y+180,dash=True,label="copied")
    d.text((60,y+bh+22),"Every box above handles Restricted data. That is why the whole path, not just the ends, has to be protected.",
           font=F("segoeui.ttf",17),fill=MUTED)
    img.save(os.path.join(HERE,"data-flow.png")); print("data-flow.png")

# ------------------------------------------------------------ system boundary
def system_boundary():
    W,H=1240,700
    img,d=base(W,H,"The authorisation boundary: Customer Web Portal (S2)",
               "For the RMF walkthrough. What is inside the line is what you are signing off.")
    bx,by,bw,bh=90,160,720,420
    try: d.rounded_rectangle([bx,by,bx+bw,by+bh],radius=16,outline=FOREST,width=3)
    except Exception: d.rectangle([bx,by,bx+bw,by+bh],outline=FOREST,width=3)
    d.text((bx+18,by+14),"INSIDE THE BOUNDARY  -  what this authorisation covers",font=F("consola.ttf",14),fill=FOREST)
    box(d,bx+40,by+60,300,90,"Web front end","the pages customers see",fill=FILL)
    box(d,bx+40,by+180,300,90,"Portal API","the logic behind the pages")
    box(d,bx+400,by+60,280,90,"Session store","who is logged in right now")
    box(d,bx+400,by+180,280,90,"Portal database","portal-specific data")
    box(d,bx+220,by+310,280,80,"Load balancer and web firewall","the doorway from the internet",fill=(236,238,231))
    link(d,bx+190,by+150,bx+190,by+180)
    link(d,bx+340,by+105,bx+400,by+105)
    link(d,bx+340,by+225,bx+400,by+225)
    link(d,bx+360,by+310,bx+300,by+270)
    # outside connections
    d.text((870,150),"OUTSIDE the boundary",font=F("consola.ttf",14),fill=MUTED)
    ext=[("Customers","reach the portal from the internet"),
         ("Identity service (S5)","a shared service it relies on"),
         ("Core Banking (S3)","the real data lives here"),
         ("Monitoring","collects the portal's logs")]
    ey=190
    for name,role in ext:
        box(d,870,ey,300,80,name,role,fill=(236,238,231),border=LINE)
        link(d,bx+bw,ey+40,870,ey+40,dash=True,head=True)
        ey+=100
    d.text((90,600),"Rule of thumb: if you are responsible for it and it is part of this system, it is inside. Shared services it merely uses are outside, but you still record the dependency.",
           font=F("segoeui.ttf",16),fill=MUTED)
    img.save(os.path.join(HERE,"system-boundary.png")); print("system-boundary.png")

if __name__=="__main__":
    architecture(); data_flow(); system_boundary()
