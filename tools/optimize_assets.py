"""Görsel ve font optimizasyonu (PageSpeed): büyük referans PNG'ler yerine yalnızca gösterilen alanı içeren WebP'ler.

Kullanım (proje kökünden):  python tools/optimize_assets.py
Tekrar çalıştırmak güvenlidir: zaten dönüştürülmüş öğelere dokunmaz. Sonrasında python tools/build_districts.py çalıştırın.

1) SVG kırpıntıları: index.html / galeri.html içinde <svg viewBox="x y w h"> ... <image href="assets/X.png" width=W height=H>
   şeklinde büyük bir PNG'nin küçük bir alanını gösteren her öğe için o alan (+%6 pay) assets/opt/X-x-y.webp olarak kesilir
   ve <image> aynı koordinatlara x/y/width/height ile yerleştirilir: viewBox, clip-path ve düzen değişmez.
2) Hero görseli: assets/hero-coast-fiat.png → assets/opt/hero-coast-fiat-{960,1280,1672}.webp (srcset için).
3) Keşif bölümü fontları (TTF, ~1,1 MB) → Latin + Türkçe karakterlerle alt kümelenmiş WOFF2 (fontTools + brotli varsa).
"""
import re
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OPT = ROOT / "assets/opt"
PAGES = ["index.html", "galeri.html"]
MARGIN = 0.06
WEBP = dict(quality=82, method=6)
HERO_WIDTHS = [960, 1280, 1672]
FONTS = ["montserrat-variable", "roboto-condensed-variable"]
# Temel Latin + Latin-1 + Türkçe (ÇĞİıÖŞÜ çğöşü) + tipografik işaretler
UNICODES = "U+0020-007E,U+00A0-00FF,U+011E-011F,U+0130-0131,U+015E-015F,U+2013-2014,U+2018-201E,U+2022,U+2026,U+20BA,U+2192"

SVG_RE = re.compile(r'<svg\b[^>]*?viewBox="([\d.\s-]+)"[^>]*>.*?</svg>', re.S)
IMG_RE = re.compile(r'<image href="(assets/[\w-]+\.png)" width="(\d+)" height="(\d+)"')


def crop_box(viewbox, size):
    x, y, w, h = (float(v) for v in viewbox.split())
    mx, my = w * MARGIN, h * MARGIN
    x0, y0 = max(0, int(x - mx)), max(0, int(y - my))
    x1, y1 = min(size[0], int(x + w + mx + 0.999)), min(size[1], int(y + h + my + 0.999))
    return x0, y0, x1, y1


def convert_svg_crops():
    OPT.mkdir(exist_ok=True)
    made = {}
    for page in PAGES:
        path = ROOT / page
        text = path.read_text(encoding="utf-8")

        def fix_svg(svg_match):
            block = svg_match.group(0)
            viewbox = svg_match.group(1)

            def fix_image(m):
                src, width, height = m.group(1), int(m.group(2)), int(m.group(3))
                image = Image.open(ROOT / src)
                assert image.size == (width, height), (src, image.size)
                box = crop_box(viewbox, image.size)
                name = f"{Path(src).stem}-{box[0]}-{box[1]}.webp"
                if name not in made:
                    image.convert("RGB").crop(box).save(OPT / name, **WEBP)
                    made[name] = (OPT / name).stat().st_size
                x0, y0, x1, y1 = box
                return f'<image href="assets/opt/{name}" x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}"'

            return IMG_RE.sub(fix_image, block)

        new = SVG_RE.sub(fix_svg, text)
        if new != text:
            path.write_text(new, encoding="utf-8")
    for name, size in sorted(made.items()):
        print(f"  assets/opt/{name}  {size // 1024} KB")


def convert_hero():
    src = Image.open(ROOT / "assets/hero-coast-fiat.png").convert("RGB")
    for w in HERO_WIDTHS:
        out = OPT / f"hero-coast-fiat-{w}.webp"
        img = src if w >= src.width else src.resize((w, round(src.height * w / src.width)), Image.LANCZOS)
        img.save(out, quality=80, method=6)
        print(f"  {out.relative_to(ROOT)}  {out.stat().st_size // 1024} KB")


def convert_fonts():
    try:
        from fontTools import subset
    except ImportError:
        print("  fontTools yok: fontlar atlandı (pip install fonttools brotli)")
        return
    for name in FONTS:
        src = ROOT / f"assets/fonts/{name}.ttf"
        out = ROOT / f"assets/fonts/{name}.woff2"
        subset.main([str(src), f"--unicodes={UNICODES}", "--flavor=woff2", "--layout-features=*", f"--output-file={out}"])
        print(f"  {out.relative_to(ROOT)}  {out.stat().st_size // 1024} KB  (kaynak {src.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    print("SVG kırpıntıları:"); convert_svg_crops()
    print("Hero:"); convert_hero()
    print("Fontlar:"); convert_fonts()
