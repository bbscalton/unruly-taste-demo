# Generates DEMO placeholder food illustrations (SVG) for the Unruly Taste demo site.
import os, math
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "images")
W, H = 640, 480

GLAZE = {"bbq": ("#8a2c10", "#c4511f"), "honey": ("#c9781a", "#f2b23a"), "jerk": ("#4a200c", "#8e3f14"),
         "lemon": ("#c9a032", "#f0d26a"), "thai": ("#b8321a", "#ee6a2c"), "fire": ("#a3170f", "#e8361c"),
         "mango": ("#d36a12", "#f7a531"), "strip": ("#b8732a", "#e2a554")}

def defs():
    s = ['<defs>',
         '<radialGradient id="bg" cx="50%" cy="38%" r="75%"><stop offset="0" stop-color="#3a1712"/><stop offset=".6" stop-color="#1c0f0c"/><stop offset="1" stop-color="#0d0908"/></radialGradient>',
         '<radialGradient id="plate" cx="50%" cy="45%" r="60%"><stop offset="0" stop-color="#2c2c2c"/><stop offset="1" stop-color="#151515"/></radialGradient>',
         '<linearGradient id="kraft" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d7ad72"/><stop offset="1" stop-color="#a8804a"/></linearGradient>',
         '<linearGradient id="bun" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f0b45a"/><stop offset="1" stop-color="#c47a26"/></linearGradient>',
         '<linearGradient id="fry" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffe08a"/><stop offset="1" stop-color="#e9b443"/></linearGradient>',
         '<filter id="sh" x="-20%" y="-20%" width="140%" height="160%"><feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#000" flood-opacity=".55"/></filter>']
    for k, (a, b) in GLAZE.items():
        s.append(f'<radialGradient id="g_{k}" cx="40%" cy="35%" r="70%"><stop offset="0" stop-color="{b}"/><stop offset="1" stop-color="{a}"/></radialGradient>')
    s.append('</defs>')
    return "".join(s)

def frame(body, title):
    title = title.replace("&", "&amp;")
    peppers = ''.join(f'<circle cx="{x}" cy="{y}" r="2.2" fill="{c}" opacity=".5"/>' for x, y, c in
                      [(40, 60, "#e63b2e"), (600, 80, "#f5c518"), (70, 420, "#2e9e4f"), (590, 400, "#e63b2e"), (320, 30, "#f5c518"), (560, 250, "#2e9e4f")])
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{title} (demo illustration)">'
            f'<title>{title} - DEMO placeholder illustration</title>{defs()}'
            f'<rect width="{W}" height="{H}" fill="url(#bg)"/>{peppers}{body}'
            f'<g transform="translate(14,14)"><rect width="118" height="26" rx="13" fill="#000" opacity=".55"/>'
            f'<text x="59" y="17.5" font-family="system-ui,Arial,sans-serif" font-size="12" font-weight="700" fill="#f5c518" text-anchor="middle" letter-spacing="1">DEMO IMAGE</text></g></svg>')

def wing(x, y, rot, glaze="bbq", sc=1.0, garnish=True):
    g = f'<g transform="translate({x},{y}) rotate({rot}) scale({sc})" filter="url(#sh)">'
    g += f'<path d="M-6,-20 C 26,-30 56,-14 58,0 C 56,14 26,30 -6,20 C -20,14 -20,-14 -6,-20Z" fill="url(#g_{glaze})"/>'
    g += '<rect x="56" y="-6" width="16" height="12" rx="6" fill="#f2e3c4"/>'
    g += '<ellipse cx="18" cy="-9" rx="18" ry="5" fill="#fff" opacity=".22"/>'
    if garnish:
        g += '<circle cx="8" cy="4" r="1.8" fill="#fff6dc"/><circle cx="26" cy="8" r="1.6" fill="#fff6dc"/><circle cx="34" cy="-4" r="1.6" fill="#2e9e4f"/>'
    return g + '</g>'

def strip(x, y, rot):
    return (f'<g transform="translate({x},{y}) rotate({rot})" filter="url(#sh)">'
            '<path d="M-40,-11 C -20,-17 20,-15 40,-9 C 46,-4 46,6 40,10 C 18,16 -20,16 -40,11 C -47,6 -47,-6 -40,-11Z" fill="url(#g_strip)"/>'
            '<path d="M-30,-6 l6,4 M-14,-8 l5,5 M4,-7 l6,5 M20,-6 l5,4 M-22,4 l6,3 M10,5 l5,3" stroke="#8a4f17" stroke-width="2" stroke-linecap="round"/></g>')

def sauce(x, y, color, r=30):
    return (f'<g transform="translate({x},{y})" filter="url(#sh)"><ellipse rx="{r}" ry="{r*0.72}" fill="#e9e9e9"/>'
            f'<ellipse rx="{r-5}" ry="{(r-5)*0.7}" fill="{color}"/><ellipse cx="-6" cy="-5" rx="{r*0.35}" ry="{r*0.12}" fill="#fff" opacity=".35"/></g>')

def fries(x, y, sc=1.0):
    g = f'<g transform="translate({x},{y}) scale({sc})" filter="url(#sh)">'
    for i, (fx, h, r) in enumerate([(-34, 70, -8), (-20, 84, -3), (-6, 92, 2), (8, 80, 6), (22, 88, 9), (-14, 66, 12), (16, 64, -10), (32, 70, 14)]):
        g += f'<rect x="{fx}" y="{-h}" width="11" height="{h}" rx="2" fill="url(#fry)" transform="rotate({r} {fx} 0)"/>'
    g += '<path d="M-48,-14 L48,-14 L38,62 L-38,62Z" fill="#d62828"/><path d="M-48,-14 C -20,6 20,6 48,-14" fill="#b71c1c"/>'
    g += '<text x="0" y="40" font-family="Impact,Arial Black,sans-serif" font-size="16" fill="#f5c518" text-anchor="middle">UT</text></g>'
    return g

def mac(x, y, sc=1.0):
    g = f'<g transform="translate({x},{y}) scale({sc})" filter="url(#sh)"><ellipse rx="62" ry="34" fill="#f2f2f2"/><ellipse rx="54" ry="27" fill="#f2b632"/>'
    import random
    rnd = random.Random(int(x * 7 + y))
    for _ in range(26):
        px, py = rnd.uniform(-44, 44), rnd.uniform(-18, 18)
        if (px / 46) ** 2 + (py / 21) ** 2 > 1: continue
        g += f'<path d="M{px-7:.0f},{py:.0f} q7,-8 14,0" stroke="#e08f12" stroke-width="5" fill="none" stroke-linecap="round"/>'
    g += '<circle cx="-14" cy="-6" r="3" fill="#2e9e4f"/><circle cx="18" cy="4" r="2.5" fill="#2e9e4f"/></g>'
    return g

def burger(x, y, sc=1.0):
    g = f'<g transform="translate({x},{y}) scale({sc})" filter="url(#sh)">'
    g += '<rect x="-74" y="30" width="148" height="26" rx="12" fill="url(#bun)"/>'
    g += '<path d="M-82,22 q10,-12 20,0 q10,-12 20,0 q10,-12 20,0 q10,-12 20,0 q10,-12 20,0 q10,-12 20,0 q10,-12 20,0 q10,-12 20,0 L82,32 L-82,32Z" fill="#3fae4f"/>'
    g += '<path d="M-80,6 C -70,-8 70,-8 80,6 C 84,18 76,28 66,30 L-66,30 C -76,28 -84,18 -80,6Z" fill="#c9802c"/>'
    g += '<path d="M-60,4 l8,6 M-30,0 l6,8 M0,2 l8,6 M30,0 l6,8 M56,4 l6,6" stroke="#8a4f17" stroke-width="3" stroke-linecap="round"/>'
    g += '<path d="M-72,10 L72,10 L60,22 L-60,22Z" fill="#f5c518" opacity=".85"/>'
    g += '<path d="M-76,2 C -76,-62 76,-62 76,2Z" fill="url(#bun)"/>'
    for sx, sy in [(-40, -30), (-14, -40), (12, -34), (38, -26), (-24, -16), (20, -14), (0, -22)]:
        g += f'<ellipse cx="{sx}" cy="{sy}" rx="4" ry="2" fill="#fff6dc" transform="rotate(20 {sx} {sy})"/>'
    return g + '</g>'

def wrap(x, y, rot=0, sc=1.0):
    g = f'<g transform="translate({x},{y}) rotate({rot}) scale({sc})" filter="url(#sh)">'
    g += '<path d="M-90,-30 L40,-30 L40,30 L-90,30 C -104,30 -104,-30 -90,-30Z" fill="#f1d9a6"/>'
    g += '<path d="M-80,-30 l10,60 M-50,-30 l10,60 M-20,-30 l10,60 M10,-30 l10,60" stroke="#d9b779" stroke-width="2"/>'
    g += '<ellipse cx="40" cy="0" rx="20" ry="30" fill="#f6e4ba"/><ellipse cx="40" cy="0" rx="15" ry="24" fill="#c9802c"/>'
    g += '<circle cx="36" cy="-10" r="5" fill="#3fae4f"/><circle cx="45" cy="6" r="5" fill="#e63b2e"/><circle cx="34" cy="10" r="4" fill="#f5a623"/><circle cx="46" cy="-8" r="3.5" fill="#f5c518"/>'
    return g + '</g>'

def waffle(x, y, sc=1.0):
    g = f'<g transform="translate({x},{y}) scale({sc})" filter="url(#sh)"><rect x="-70" y="-50" width="140" height="100" rx="18" fill="#dca04a"/>'
    for i in range(-50, 70, 24):
        g += f'<line x1="{i}" y1="-46" x2="{i}" y2="46" stroke="#b97a2a" stroke-width="5"/>'
    for j in range(-30, 50, 24):
        g += f'<line x1="-66" y1="{j}" x2="66" y2="{j}" stroke="#b97a2a" stroke-width="5"/>'
    g += '<path d="M-30,-30 C -10,-10 10,-34 30,-14 C 40,-4 20,10 30,24" stroke="#c9781a" stroke-width="8" fill="none" stroke-linecap="round" opacity=".9"/></g>'
    return g

def plantain(x, y):
    g = f'<g transform="translate({x},{y})" filter="url(#sh)">'
    for i, (px, py, r) in enumerate([(-40, 0, -20), (-10, -12, 10), (22, 2, -5), (-20, 22, 15), (14, 26, -15), (44, -14, 20)]):
        g += f'<ellipse cx="{px}" cy="{py}" rx="20" ry="12" fill="#8a4b12" transform="rotate({r} {px} {py})"/><ellipse cx="{px}" cy="{py}" rx="16" ry="9" fill="#efa63a" transform="rotate({r} {px} {py})"/>'
    return g + '</g>'

def box(x, y, w=230, h=120, label=""):
    g = f'<g transform="translate({x},{y})" filter="url(#sh)">'
    g += f'<path d="M{-w/2},0 L{w/2},0 L{w/2-14},{h} L{-w/2+14},{h}Z" fill="url(#kraft)"/>'
    g += f'<rect x="{-w/2}" y="-8" width="{w}" height="14" rx="4" fill="#c99a5e"/>'
    if label:
        g += f'<rect x="{-w/2+30}" y="{h/2-12}" width="{w-60}" height="34" rx="6" fill="#111"/>'
        g += f'<text x="0" y="{h/2+11}" font-family="Impact,Arial Black,sans-serif" font-size="20" fill="#f5c518" text-anchor="middle" letter-spacing="1">{label}</text>'
    return g + '</g>'

def cup(x, y, color, sc=1.0):
    return (f'<g transform="translate({x},{y}) scale({sc})" filter="url(#sh)"><rect x="6" y="-110" width="7" height="60" rx="3" fill="#f5c518" transform="rotate(12 9 -80)"/>'
            f'<path d="M-34,-60 L34,-60 L26,40 L-26,40Z" fill="#ffffff" opacity=".25"/><path d="M-31,-40 L31,-40 L26,36 L-26,36Z" fill="{color}"/>'
            f'<ellipse cx="0" cy="-60" rx="36" ry="9" fill="#fff" opacity=".35"/><circle cx="-10" cy="-20" r="5" fill="#fff" opacity=".35"/><circle cx="8" cy="0" r="3" fill="#fff" opacity=".35"/></g>')

def plate(x, y, rx=230, ry=130):
    return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="url(#plate)" stroke="#333" stroke-width="3"/>'

def banner(text, sub, color="#d62828"):
    return (f'<g transform="translate(320,410)"><rect x="-210" y="-30" width="420" height="58" rx="12" fill="{color}"/>'
            f'<text x="0" y="0" font-family="Impact,Arial Black,sans-serif" font-size="28" fill="#fff" text-anchor="middle" letter-spacing="1">{text}</text>'
            f'<text x="0" y="20" font-family="system-ui,Arial,sans-serif" font-size="13" font-weight="700" fill="#f5c518" text-anchor="middle">{sub}</text></g>')

imgs = {}
# Wings 12pc: plate of mixed glazes + sauce cups
b = plate(320, 260)
pos = [(200, 220, -20, "bbq"), (270, 190, 10, "honey"), (350, 200, -10, "jerk"), (420, 230, 20, "fire"), (230, 290, 30, "lemon"),
       (310, 270, -30, "mango"), (390, 300, 5, "thai"), (300, 330, 15, "bbq"), (240, 250, 60, "honey"), (360, 250, 40, "jerk")]
for px, py, r, gl in pos: b += wing(px - 25, py, r, gl)
b += sauce(500, 170, "#f2b23a", 30) + sauce(140, 170, "#8a2c10", 30) + sauce(520, 330, "#f7f1e1", 26)
imgs["wings-12pc.svg"] = frame(b, "Wings (12pc)")
# Wings combo: wings + fries + mac
b = plate(320, 270, 260, 140) + mac(410, 320, 0.95) + fries(450, 200, 0.95)
for px, py, r, gl in [(150, 230, -15, "bbq"), (210, 200, 15, "bbq"), (170, 290, 25, "honey"), (240, 270, -20, "honey"), (280, 320, 5, "bbq")]:
    b += wing(px, py, r, gl)
imgs["wings-combo.svg"] = frame(b, "Wings Combo")
# Wings with a side: chicken & waffles + plantain
b = plate(320, 270, 260, 140) + waffle(230, 270, 1.05)
for px, py, r, gl in [(330, 210, -10, "honey"), (360, 270, 20, "honey"), (300, 320, -30, "honey")]:
    b += wing(px, py, r, gl)
b += plantain(470, 300) + sauce(500, 190, "#f2b23a", 26)
imgs["wings-with-side.svg"] = frame(b, "Wings with a side")
# Burger & wings combo
b = plate(320, 280, 270, 140) + burger(230, 260, 1.0) + fries(470, 230, 0.85)
for px, py, r, gl in [(330, 320, -15, "fire"), (380, 340, 20, "fire"), (310, 360, 5, "bbq")]:
    b += wing(px, py, r, gl, 0.9)
b += sauce(160, 360, "#f7f1e1", 22) + sauce(530, 350, "#e8361c", 22)
imgs["burger-wings-combo.svg"] = frame(b, "Burger & Wings Combo")
# Hot box
b = box(320, 250, 400, 150, "HOT BOX") + burger(210, 200, 0.8) + fries(450, 180, 0.8) + mac(330, 230, 0.7)
b += wing(140, 300, -20, "fire", 0.8) + strip(500, 300, 15)
imgs["hot-box.svg"] = frame(b, "Hot Box")
# Wrap box
b = box(320, 250, 400, 150, "WRAP BOX") + wrap(250, 200, -8, 0.9) + fries(470, 180, 0.8) + mac(360, 235, 0.65)
b += strip(150, 300, -20) + wing(470, 300, 10, "mango", 0.8)
imgs["wrap-box.svg"] = frame(b, "Wrap Box")
# Thursday double bubble: two boxes
b = box(180, 200, 230, 120, "HOT BOX") + burger(150, 160, 0.55) + fries(230, 150, 0.55)
b += box(460, 200, 230, 120, "WRAP BOX") + wrap(440, 165, -6, 0.6) + fries(520, 150, 0.55)
b += '<text x="320" y="260" font-family="Impact,Arial Black,sans-serif" font-size="54" fill="#f5c518" text-anchor="middle">+</text>'
b += banner("DOUBLE BUBBLE", "ANY 2 BOXES · THURSDAYS")
imgs["deal-thursday-double-bubble.svg"] = frame(b, "Thursday Double Bubble")
# Friday mega meal
b = box(200, 190, 220, 110, "HOT BOX") + burger(170, 150, 0.5) + box(430, 190, 220, 110, "WRAP BOX") + wrap(410, 155, -6, 0.55)
b += cup(560, 300, "#e63b2e", 0.8) + cup(80, 300, "#f5a623", 0.8)
b += banner("FRIDAY MEGA MEAL", "HOT BOX + WRAP BOX + 2 REFRESHERS", "#0b7a3e")
imgs["deal-friday-mega-meal.svg"] = frame(b, "Friday Mega Meal")
# Hero: wide spread
b = plate(320, 270, 300, 150) + fries(150, 230, 0.85) + burger(320, 200, 0.75) + waffle(470, 300, 0.7)
for px, py, r, gl in [(220, 320, -15, "bbq"), (290, 340, 10, "honey"), (360, 330, -20, "fire"), (420, 220, 25, "jerk")]:
    b += wing(px, py, r, gl, 0.9)
b += sauce(540, 200, "#f2b23a", 24) + sauce(100, 340, "#e8361c", 24)
imgs["hero-spread.svg"] = frame(b, "Unruly Taste spread")

for n, s in imgs.items():
    open(os.path.join(OUT, n), "w").write(s)
print("\n".join(sorted(imgs)))
