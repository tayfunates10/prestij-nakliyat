"""Galeri fotoğraflarına Prestij Nakliyat alt bandını (logo, telefon, konum) basar.

Kullanım (proje kökünden):  python tools/make_gallery_bands.py

- Kaynak: assets/gallery/<ad>.jpeg (orijinal fotoğraf, değiştirilmez)
- Çıktı:  assets/gallery/<ad>-bantli.jpg
- Fotoğraflar kırpılmaz; çıktı kaynağın tamamıdır (en fazla MAX_WIDTH genişliğe küçültülür).
- Bant 720 x 756 px bir kart üzerinde ölçülmüştür. Ölçek fotoğrafın kısa kenarına göre seçilir; logo sol alta,
  telefon ve konum sağ alta sabitlenir, böylece dikey ve yatay fotoğraflarda aynı görünür.
- Telefon değişirse PHONE değerini güncelleyip betiği yeniden çalıştırın.
Gereksinim: Pillow, numpy.
"""
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
GALLERY = ROOT / "assets" / "gallery"
FONT = ROOT / "assets" / "fonts" / "roboto-condensed-variable.ttf"
LOGO = ROOT / "assets" / "header-reference.png"
LOGO_BOX = (55, 447, 488, 555)  # Sitedeki logo görüntü alanı (viewBox="55 447 433 108")

PHONE = "0552 475 01 67"
LOCATION = "Merkez / Zonguldak"

# Galeri sırası; kaynak assets/gallery/<ad>.jpeg
PHOTOS = [
    "arac-ici-paketleme",
    "fiat-nakliye-araci",
    "fiat-nakliye-araci-istasyon",
    "korumali-esyalar",
    "paketli-esyalar-ekip",
    "paketli-esyalar-koli",
    "paketli-esyalar-kose",
    "paketli-esyalar-yatak",
]
MAX_WIDTH = 1200

# 720 x 756 tasarım ölçüleri (px)
W, H = 720, 756
GRADIENT = [(530, 0.0), (645, 0.72), (756, 0.93)]  # (y, opaklık)
BAND_COLOR = np.array([7, 9, 7], float)
LOGO_X, LOGO_Y, LOGO_W = 31.3, 645.0, 296.2
PHONE_RIGHT, PHONE_TOP, PHONE_INK_H, PHONE_COLOR, PHONE_WEIGHT, PHONE_TRACK = 682, 647, 29, (253, 228, 147), 850, 0.78
LOC_RIGHT, LOC_TOP, LOC_INK_H, LOC_COLOR, LOC_WEIGHT, LOC_TRACK = 686, 697, 29, (232, 229, 221), 500, 0
PIN_X, PIN_Y, PIN_W, PIN_H, PIN_COLOR = 415, 697, 20, 25, (214, 184, 112)
SS = 4  # kenar yumuşatma için süper örnekleme


def font(size, weight):
    f = ImageFont.truetype(str(FONT), size)
    f.set_variation_by_axes([weight])
    return f


def fit_font(text, ink_h, weight, scale):
    """Mürekkep yüksekliği ink_h * scale olacak yazı boyutunu bulur (SS ölçeğinde)."""
    target = ink_h * scale * SS
    size = target
    for _ in range(6):
        l, t, r, b = font(round(size), weight).getbbox(text)
        size *= target / (b - t)
    return font(round(size), weight)


def draw_text(text, f, track):
    """Harf aralıklı metni kendi mürekkep kutusuna kırpılmış maske olarak çizer."""
    size = f.size
    mask = Image.new("L", (round(len(text) * (size + track) + size * 2), size * 3), 0)
    d = ImageDraw.Draw(mask)
    x = size
    for ch in text:
        d.text((x, size), ch, font=f, fill=255)
        x += f.getlength(ch) + track
    return mask.crop(mask.getbbox())


def fit(photo):
    """Kaynağı kırpmadan, en fazla MAX_WIDTH genişliğe küçültür."""
    w, h = photo.size
    if w <= MAX_WIDTH:
        return photo
    return photo.resize((MAX_WIDTH, round(h * MAX_WIDTH / w)), Image.LANCZOS)


def band(img):
    out_w, out_h = img.size
    k = min(out_w / W, out_h / H)
    a = np.asarray(img).astype(float)
    # Tasarım koordinatları: soldaki öğeler sola, sağdakiler sağa, hepsi alta sabitlenir.
    left = lambda x: x * k
    right_ = lambda x: out_w - (W - x) * k
    bottom = lambda y: out_h - (H - y) * k

    # Alt geçiş
    ys = H - (out_h - np.arange(out_h)) / k
    alpha = np.interp(ys, [y for y, _ in GRADIENT], [o for _, o in GRADIENT])[:, None, None]
    a = a * (1 - alpha) + BAND_COLOR * alpha

    # Logo (siyah zemin, koyu banda "lighten" ile oturur)
    logo = Image.open(LOGO).convert("RGB").crop(LOGO_BOX)
    lw = round(LOGO_W * k)
    lh = round(lw * logo.height / logo.width)
    logo = np.asarray(logo.resize((lw, lh), Image.LANCZOS)).astype(float)
    x0, y0 = round(left(LOGO_X)), round(bottom(LOGO_Y))
    region = a[y0:y0 + lh, x0:x0 + lw]
    a[y0:y0 + lh, x0:x0 + lw] = np.maximum(region, logo[:region.shape[0], :region.shape[1]])

    # Yazılar ve konum simgesi süper örneklenmiş maskeye çizilir
    layers = []
    for text, right, top, ink_h, color, weight, track in (
        (PHONE, PHONE_RIGHT, PHONE_TOP, PHONE_INK_H, PHONE_COLOR, PHONE_WEIGHT, PHONE_TRACK),
        (LOCATION, LOC_RIGHT, LOC_TOP, LOC_INK_H, LOC_COLOR, LOC_WEIGHT, LOC_TRACK),
    ):
        f = fit_font(text, ink_h, weight, k)
        ink = draw_text(text, f, track * k * SS)
        mask = Image.new("L", (out_w * SS, out_h * SS), 0)
        mask.paste(ink, (round(right_(right + 1) * SS) - ink.width, round(bottom(top) * SS)))
        layers.append((mask, color))

    pin = Image.new("L", (out_w * SS, out_h * SS), 0)
    d = ImageDraw.Draw(pin)
    px, py, pw, ph = right_(PIN_X) * SS, bottom(PIN_Y) * SS, PIN_W * k * SS, PIN_H * k * SS
    stroke = max(1, round(2.2 * k * SS))
    cx, r = px + pw / 2, pw / 2 - stroke / 2
    cy = py + r + stroke / 2
    tip = (cx, py + ph - stroke / 2)
    # Damla biçimli iğne: üst yay + uca inen iki kenar
    d.arc((cx - r, cy - r, cx + r, cy + r), 150, 30, fill=255, width=stroke)
    for ang in (150, 30):
        rad = np.radians(ang)
        d.line(((cx + r * np.cos(rad), cy + r * np.sin(rad)), tip), fill=255, width=stroke)
    ir = pw * 0.2
    d.ellipse((cx - ir, cy - ir, cx + ir, cy + ir), outline=255, width=stroke)
    layers.append((pin, PIN_COLOR))

    for mask, color in layers:
        m = np.asarray(mask.resize((out_w, out_h), Image.LANCZOS)).astype(float)[..., None] / 255
        a = a * (1 - m) + np.array(color, float) * m

    return Image.fromarray(np.clip(a, 0, 255).round().astype(np.uint8))


def main():
    for name in PHOTOS:
        src = Image.open(GALLERY / f"{name}.jpeg").convert("RGB")
        out = band(fit(src))
        out.save(GALLERY / f"{name}-bantli.jpg", quality=88, optimize=True, progressive=True)
        print(f"{name}-bantli.jpg {out.size[0]}x{out.size[1]}")


if __name__ == "__main__":
    main()
