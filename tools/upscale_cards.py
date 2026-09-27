"""Hizmetlerimiz ve Taşıma Süreci kart görsellerinin yüksek çözünürlüklü (HD) sürümleri: yapay zekâ süper çözünürlük (EDSR ×4).

Kullanım (proje kökünden):  python tools/upscale_cards.py <EDSR_x4.pb yolu>
Gereksinim: pip install opencv-contrib-python-headless numpy pillow
Model: https://github.com/Saafke/EDSR_Tensorflow/raw/master/models/EDSR_x4.pb (~38 MB, repoya eklenmez)

Kaynaklardaki kırpıntılar çok küçük (hizmet ~300 px, süreç 211 px) ve mobil kartta ~1000 fiziksel piksele büyütülüyordu.
EDSR üretken değildir: yüz/logo uydurmaz, var olan kenar ve dokuyu netleştirir. Çıktılar *-hd.webp olarak yazılır ve
index.html'deki <image> doğrudan onlara bağlanır (toplam ~230 KB; eski küçük kırpıntılardan yalnızca ~75 KB fazla).
Kart düzeni değişmez: <image> x/y/width/height aynı kalır. Kaynak kırpıntıya bağlı <image>'lar yoksa betik bir şey yapmaz.
"""
import re
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
SERVICE_WIDTH = 1000   # mobil kart ~348 css px × ~2,6–3 DPR
WEBP = dict(quality=78, method=6)
SHARPEN = ImageFilter.UnsharpMask(radius=1.2, percent=45, threshold=2)
# Süreç adımları: process-reference.png içindeki 211×132 alanlar
STEPS = {"surec-iletisim": (195, 428), "surec-kesif": (562, 428), "surec-paketleme": (940, 428),
         "surec-tasima": (1308, 428), "surec-montaj": (1680, 428)}
SERVICE_IMG = re.compile(r'<image href="(assets/opt/(services-reference-\d+-\d+)\.webp)" x="(\d+)" y="(\d+)" width="(\d+)" height="(\d+)"')
PROCESS_IMG = re.compile(r'<image href="(assets/process/(surec-[a-z]+)\.webp)" width="211" height="132"')


def main(model_path):
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    sr.readModel(model_path)
    sr.setModel("edsr", 4)

    def upscale(pil):
        out = sr.upsample(cv2.cvtColor(np.array(pil), cv2.COLOR_RGB2BGR))
        return Image.fromarray(cv2.cvtColor(out, cv2.COLOR_BGR2RGB)).filter(SHARPEN)

    page = ROOT / "index.html"
    html = page.read_text(encoding="utf-8")
    services = Image.open(ROOT / "assets/services-reference.png").convert("RGB")
    process = Image.open(ROOT / "assets/process-reference.png").convert("RGB")

    def service(m):
        src, stem, x, y, w, h = m.group(1), m.group(2), *map(int, m.groups()[2:])
        out = ROOT / f"assets/opt/{stem}-hd.webp"
        big = upscale(services.crop((x, y, x + w, y + h)))
        big.resize((SERVICE_WIDTH, round(SERVICE_WIDTH * h / w)), Image.LANCZOS).save(out, **WEBP)
        print(f"  {out.relative_to(ROOT)}  {out.stat().st_size // 1024} KB")
        return f'<image href="assets/opt/{stem}-hd.webp" x="{x}" y="{y}" width="{w}" height="{h}"'

    def step(m):
        src, stem = m.group(1), m.group(2)
        x, y = STEPS[stem]
        out = ROOT / f"assets/process/{stem}-hd.webp"
        upscale(process.crop((x, y, x + 211, y + 132))).save(out, **WEBP)
        print(f"  {out.relative_to(ROOT)}  {out.stat().st_size // 1024} KB")
        return f'<image href="assets/process/{stem}-hd.webp" width="211" height="132"'

    html = SERVICE_IMG.sub(service, html)
    html = PROCESS_IMG.sub(step, html)
    page.write_text(html, encoding="utf-8")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
