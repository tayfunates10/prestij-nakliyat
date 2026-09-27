"""Taşıma Süreci adım kartlarının görsellerini üretir: assets/process/surec-*.webp

Kullanım (proje kökünden):  python tools/make_process_steps.py

Kartlar önceden assets/process-reference.png içinden 211×132 piksellik alanları doğrudan gösteriyordu; mobilde bu alan
~3,3 kat büyütüldüğü için bulanıktı. Burada her alan 3 kat (633×396) Lanczos ile büyütülüp ölçülü keskinleştirilir
(UnsharpMask r=1.2, %80 — daha güçlüsü kenarlarda hale bırakıyor). HTML'de SVG viewBox 0 0 211 132 kalır, yerleşim değişmez.
"""
from pathlib import Path

from PIL import Image, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
SIZE = (211, 132)
SCALE = 3
# process-reference.png içindeki sol üst köşeler (index.html'deki eski viewBox değerleri)
STEPS = {
    "surec-iletisim": (195, 428),
    "surec-kesif": (562, 428),
    "surec-paketleme": (940, 428),
    "surec-tasima": (1308, 428),
    "surec-montaj": (1680, 428),
}


def main():
    source = Image.open(ROOT / "assets/process-reference.png").convert("RGB")
    out_dir = ROOT / "assets/process"
    out_dir.mkdir(exist_ok=True)
    for name, (x, y) in STEPS.items():
        crop = source.crop((x, y, x + SIZE[0], y + SIZE[1]))
        big = crop.resize((SIZE[0] * SCALE, SIZE[1] * SCALE), Image.LANCZOS)
        big.filter(ImageFilter.UnsharpMask(radius=1.2, percent=80, threshold=3)).save(out_dir / f"{name}.webp", quality=88, method=6)
    print(f"{len(STEPS)} adım görseli üretildi: assets/process/")


if __name__ == "__main__":
    main()
