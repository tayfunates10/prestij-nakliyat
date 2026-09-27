"""Arka plan için döşenebilir, evden eve nakliyat temalı ikon desenini üretir: assets/moving-pattern.svg

Kullanım (proje kökünden):  python tools/make_pattern.py

İkonlar tek renk ince çizgilerdir; kenardan taşan ikonlar karşı kenarda tekrar çizildiği için desen kesintisiz tekrarlanır.
Genel görünürlük backdrop.css içindeki --backdrop-strength ile ayarlanır.
"""
import math
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TILE = 720      # piksel, backdrop.css background-size ile orantılı
COUNT = 22      # desen karesindeki ikon sayısı
MIN_GAP = 128   # ikon merkezleri arasındaki en küçük uzaklık
SEED = 67       # Zonguldak plaka kodu; aynı tohum aynı deseni üretir

# 24 × 24 çizgi ikonları (yalnızca stroke)
ICONS = {
    "koli": '<path d="M3 8l9-5 9 5v8l-9 5-9-5zM3 8l9 5 9-5M12 13v8M7.5 5.5l9 5"/>',
    "kamyon": '<path d="M1 5h13v11H1zM14 9h4.5l3.5 4v3h-8"/><circle cx="5.5" cy="18" r="2"/><circle cx="17.5" cy="18" r="2"/>',
    "ev": '<path d="M3 11l9-8 9 8M5 9.5V21h14V9.5M10 21v-6h4v6"/>',
    "kanepe": '<path d="M4 10V7a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v3M2 12a2 2 0 0 1 4 0v2h12v-2a2 2 0 0 1 4 0v5H2zM4 17v2M20 17v2"/>',
    "tasima-arabasi": '<path d="M5 2h2.5l4 15h9M9.5 9.5l7-2 2 7-7 2"/><circle cx="11.5" cy="19.5" r="2"/>',
    "bant": '<circle cx="10" cy="12" r="7"/><circle cx="10" cy="12" r="2.5"/><path d="M17 12h5v3"/>',
    "anahtar": '<circle cx="7" cy="12" r="4"/><path d="M11 12h11M18 12v3M21 12v2"/>',
    "koliler": '<path d="M3 13h8v8H3zM13 13h8v8h-8zM8 4h8v9H8zM7 13v3M17 13v3M12 4v3"/>',
    "konum": '<path d="M12 21s7-6.5 7-12a7 7 0 0 0-14 0c0 5.5 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/>',
    "kirilacak": '<path d="M8 3h8l-.8 6.5a3.2 3.2 0 0 1-6.4 0zM12 13v7M9 21h6"/>',
    "bu-taraf-yukari": '<path d="M7 20V5M4 8l3-3 3 3M17 20V5M14 8l3-3 3 3M3 21h18"/>',
    "saksi": '<path d="M7 13h10l-1.5 8h-7zM12 13V8M12 10c-3 0-5-2-5-5 3 0 5 2 5 5M12 9c0-3 2-5 5-5 0 3-2 5-5 5"/>',
    "gardirop": '<path d="M5 2h14v18H5zM12 2v18M10 10v2M14 10v2M6 20v2M18 20v2"/>',
    "lamba": '<path d="M8 3h8l3 7H5zM12 10v9M8 21h8"/>',
}

random.seed(SEED)


def torus_distance(a, b):
    dx = abs(a[0] - b[0]); dy = abs(a[1] - b[1])
    return math.hypot(min(dx, TILE - dx), min(dy, TILE - dy))


points = []
attempts = 0
while len(points) < COUNT and attempts < 20000:
    attempts += 1
    candidate = (random.uniform(0, TILE), random.uniform(0, TILE))
    if all(torus_distance(candidate, p) >= MIN_GAP for p in points):
        points.append(candidate)

names = list(ICONS)
order = (names * (COUNT // len(names) + 1))[:COUNT]
random.shuffle(order)

uses = []
for (x, y), name in zip(points, order):
    size = random.uniform(38, 50)
    angle = random.uniform(-16, 16)
    scale = size / 24
    for ox in (-TILE, 0, TILE):
        for oy in (-TILE, 0, TILE):
            cx, cy = x + ox, y + oy
            if -size < cx < TILE + size and -size < cy < TILE + size:
                uses.append(f'<use href="#{name}" width="24" height="24" transform="translate({cx:.1f} {cy:.1f}) rotate({angle:.1f}) scale({scale:.3f}) translate(-12 -12)"/>')

# İkonlar arasında seyrek küçük noktalar (doku)
dots = []
for _ in range(90):
    p = (random.uniform(0, TILE), random.uniform(0, TILE))
    if all(torus_distance(p, q) > 40 for q in points):
        dots.append(f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="1.3"/>')

symbols = "".join(f'<symbol id="{n}" viewBox="0 0 24 24" overflow="visible">{body}</symbol>' for n, body in ICONS.items())
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{TILE}" height="{TILE}" viewBox="0 0 {TILE} {TILE}">'
       f'<defs>{symbols}</defs>'
       f'<g fill="none" stroke="#e2b24f" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round">{"".join(uses)}</g>'
       f'<g fill="#e2b24f" opacity=".6">{"".join(dots)}</g></svg>\n')
(ROOT / "assets" / "moving-pattern.svg").write_text(svg, encoding="utf-8", newline="\n")
print(f"assets/moving-pattern.svg: {len(points)} ikon, {len(svg) // 1024} KB")
