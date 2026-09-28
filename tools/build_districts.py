"""İlçe açılış sayfalarını, SEO etiketlerini, sitemap.xml, robots.txt ve llms.txt dosyalarını üretir.

Kullanım (proje kökünden):  python tools/build_districts.py

- Header, ikon kütüphanesi, hizmet penceresi, ücretsiz keşif bölümü, footer ve mobil hızlı işlem çubuğu
  index.html içinden alınır; bu alanlarda değişiklik yaptıktan sonra betiği yeniden çalıştırın.
- index.html ve galeri.html içindeki <!-- seo:start --> ... <!-- seo:end --> bloğu betik tarafından yazılır;
  elle düzenlemeyin, değişiklikleri buradan yapın.
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://prestijevdenevenakliyat.com"
LASTMOD = "2026-09-27"
PHONE_DISPLAY = "0552 475 01 67"
PHONE_TEL = "+905524750167"
PHONE_SCHEMA = "+90-552-475-01-67"
WHATSAPP = "https://wa.me/905524750167"
ORG_ID = f"{BASE}/#firma"
SITE_ID = f"{BASE}/#site"
# Paylaşım önizleme görseli; görsel değişince sürümü artırın (WhatsApp/Facebook önbelleği URL'ye bağlıdır).
OG_IMAGE = f"{BASE}/assets/og-image.jpg?v=20260928"
OG_IMAGE_ALT = "Prestij Nakliyat tanıtım görseli: kaplamalı beyaz Fiat Ducato nakliye aracı, Zonguldak hizmet bölgesi haritası, hizmetler ve 0552 475 01 67 telefon numarası"
SIGNATURE = "Her adımda güvenle taşıyoruz"
# index.html'deki ücretsiz keşif başlığı; ilçe sayfalarında ilçe adıyla değiştirilir.
DISCOVERY_TITLE = "Taşınma tarihiniz belli mi?<br><span>Planı birlikte yapalım.</span>"
# Firma adresi (Kilimli). Posta kodu ve koordinat doğrulanmadığı için şemaya yazılmıyor.
ADDRESS_STREET = "Hisararkası Mah. Merkez Evler Sok. No:3/6"
ADDRESS_DISTRICT = "Kilimli"
ADDRESS_FULL = f"{ADDRESS_STREET}, {ADDRESS_DISTRICT}/Zonguldak"
# Firmanın Google Maps kaydı (adres bağlantıları, yol tarifi ve şemadaki hasMap).
MAPS_URL = "https://maps.app.goo.gl/FkS2a55wqvdYeri78"
ALL_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
HOURS_24_7 = {"@type": "OpeningHoursSpecification", "dayOfWeek": ALL_WEEK, "opens": "00:00", "closes": "23:59"}

SERVICES = [
    ("Evden Eve Nakliyat", "Eşyalarınız profesyonel ekibimizle güvenle yeni yuvanıza taşınır."),
    ("Ofis Taşımacılığı", "İşinizi aksatmadan, hızlı ve planlı ofis taşıma hizmetleri."),
    ("Mobilya Montajı", "Tüm mobilyalarınız uzman ekibimizce sökülür, taşınır ve montajı yapılır."),
    ("Paketleme Hizmeti", "Eşyalarınız özel ambalaj malzemeleri ile güvenle paketlenir."),
    ("Asansörlü Taşıma", "Yüksek katlarda bile hızlı, güvenli ve pratik taşıma çözümleri."),
]

PRICE_ANSWER = ("Fiyat; eşya miktarına, iki adresin kat ve bina durumuna, asansör ve paketleme ihtiyacına "
                "ve adresler arasındaki mesafeye göre belirlenir. Ücretsiz keşifte eşyalarınızı yerinde görerek "
                "size net bir fiyat veriyoruz.")

COMMON_CHECKS = [
    "<strong>Paketleme:</strong> Beyaz eşya, cam ve hassas parçalar özel ambalaj malzemeleriyle korunur.",
    "<strong>Söküm ve kurulum:</strong> Söktüğümüz mobilyaları yeni adresinizde kurup yerleştiriyoruz.",
    "<strong>Sigorta:</strong> Eşyalarınız taşıma süresince sigorta güvencesi altındadır.",
]

# Her ilçe için özgün içerik. Yeni ilçe eklerken slug, ad ve metinleri doldurun.
DISTRICTS = [
    {
        "slug": "eregli", "name": "Ereğli", "upper": "EREĞLİ", "locative": "Ereğli’de", "ablative": "Ereğli’den",
        "place": "Karadeniz Ereğli, Zonguldak",
        "description": "Karadeniz Ereğli evden eve nakliyat: paketleme, mobilya montajı ve asansörlü taşıma. Ücretsiz keşif ve net fiyat için Prestij Nakliyat: 0552 475 01 67.",
        "hero": "Kdz. Ereğli’de ev ve ofis taşımalarınızı ücretsiz keşifle planlıyor, eşyalarınızı paketleyip yeni adresinize güvenle taşıyoruz.",
        "lead": "Prestij Nakliyat, Karadeniz Ereğli’de evden eve nakliyat, ofis taşımacılığı, paketleme, mobilya montajı ve asansörlü taşıma hizmeti veren Zonguldak merkezli bir nakliyat firmasıdır. Fiyat, ücretsiz keşifte eşyalarınız yerinde görülerek net olarak belirlenir.",
        "body": "Ereğli, sahil boyunca uzanan mahalleleri ve yamaçlara yayılan yerleşimiyle kat yüksekliği, sokak genişliği ve park imkânı adresten adrese değişen bir ilçedir. Bu yüzden her taşımadan önce bina girişini, kat sayısını ve aracın yanaşacağı noktayı keşifte birlikte netleştiriyoruz. Ereğli içindeki taşınmaların yanı sıra Ereğli’den Zonguldak merkeze, Alaplı’ya ya da diğer ilçelere taşınmalarda da aynı ekip ve planla çalışıyoruz.",
        "check": "<strong>Bina ve sokak durumu:</strong> Yüksek katlı apartmanlarda asansör ihtiyacını, eğimli sokaklarda aracın yanaşacağı noktayı keşifte belirliyoruz.",
        "faqs": [
            ("Ereğli’de evden eve nakliyat fiyatı nasıl belirlenir?", PRICE_ANSWER),
            ("Ereğli’den Zonguldak merkeze veya başka ilçeye taşınma yapıyor musunuz?", "Evet. Ereğli içindeki taşınmaların yanı sıra Zonguldak merkeze ve Alaplı, Çaycuma, Devrek gibi diğer ilçelere yapılan taşınmalarda da hizmet veriyoruz."),
            ("Ereğli’de keşif için adresime geliyor musunuz?", f"Evet. Ekibimiz adresinize gelip eşyalarınızı yerinde görür ve ücretsiz keşifle size özel taşıma planını çıkarır. Randevu için {PHONE_DISPLAY} numarasını arayabilir veya WhatsApp’tan yazabilirsiniz."),
        ],
    },
    {
        "slug": "kozlu", "name": "Kozlu", "upper": "KOZLU", "locative": "Kozlu’da", "ablative": "Kozlu’dan",
        "place": "Kozlu, Zonguldak",
        "description": "Kozlu evden eve nakliyat: yokuşlu sokaklara ve yüksek katlara uygun planla paketleme, montaj ve asansörlü taşıma. Ücretsiz keşif: 0552 475 01 67.",
        "hero": "Zonguldak merkeze komşu Kozlu’da yokuşlu sokaklara ve yüksek katlara uygun planla ev ve ofis taşıyoruz.",
        "lead": "Prestij Nakliyat, Kozlu’da evden eve nakliyat, ofis taşımacılığı, paketleme, mobilya montajı ve asansörlü taşıma hizmeti verir. Zonguldak merkeze komşu Kozlu’daki taşınmalarınızı ücretsiz keşifle planlar, net fiyatı keşifte veririz.",
        "body": "Kozlu, kıyıdan yamaçlara doğru yükselen mahalleleri ve eğimli sokaklarıyla bilinir; taşımada en çok zaman alan kısım çoğu zaman aracın bina önüne yanaşması ve merdivenli girişlerdir. Keşifte bu noktaları görüp ekibi ve ekipmanı buna göre hazırlıyoruz. Kozlu’dan Zonguldak merkeze, Kilimli’ye veya il içindeki başka bir adrese taşınmalarda da hizmet veriyoruz.",
        "check": "<strong>Yokuş ve merdivenli girişler:</strong> Aracın yanaşabileceği en yakın noktayı ve taşıma yolunu önceden planlıyoruz.",
        "faqs": [
            ("Kozlu’nun yokuşlu ve dar sokaklarında taşıma nasıl yapılıyor?", "Keşifte aracın yanaşabileceği en yakın noktayı ve bina girişini görüyoruz. Ekibi bu mesafeye göre planlıyor, yüksek katlarda asansörlü taşımayı değerlendiriyoruz."),
            ("Kozlu’da evden eve nakliyat fiyatı nasıl belirlenir?", PRICE_ANSWER),
            ("Kozlu’dan Zonguldak merkeze taşınma ne kadar sürer?", "Süre; eşya miktarına ve iki binanın kat ve giriş durumuna göre değişir. Keşif sırasında size uygun taşıma gününü ve saatini birlikte belirliyoruz."),
        ],
    },
    {
        "slug": "kilimli", "name": "Kilimli", "upper": "KİLİMLİ", "locative": "Kilimli’de", "ablative": "Kilimli’den",
        "place": "Kilimli, Zonguldak",
        "description": "Kilimli evden eve nakliyat: müstakil ev ve apartman taşımalarında paketleme, mobilya montajı ve asansörlü taşıma. Ücretsiz keşif: 0552 475 01 67.",
        "hero": "Kilimli’de müstakil evden apartman dairesine kadar her taşınmayı ücretsiz keşifle planlıyor, güvenle taşıyoruz.",
        "lead": "Prestij Nakliyat, Kilimli’de evden eve nakliyat, ofis taşımacılığı, paketleme, mobilya montajı ve asansörlü taşıma hizmeti verir. Kilimli’den Zonguldak merkeze ve diğer ilçelere yapılan taşınmalarda da aynı ekip ve planla çalışırız.",
        "body": "Zonguldak merkezin doğusunda, kıyı boyunca uzanan Kilimli’de müstakil evlerden apartman dairelerine kadar farklı konut tipleri bir arada bulunur. Müstakil evlerde bahçe ve depo eşyalarını, apartmanlarda kat ve asansör durumunu keşifte ayrı ayrı değerlendirip taşımayı buna göre planlıyoruz.",
        "check": "<strong>Konut tipi:</strong> Müstakil evlerde bahçe ve depo eşyalarını, apartmanlarda kat ve asansör durumunu ayrı ayrı planlıyoruz.",
        "faqs": [
            ("Kilimli’de evden eve nakliyat fiyatı nasıl belirlenir?", PRICE_ANSWER),
            ("Müstakil evden apartmana taşınırken nelere dikkat ediyorsunuz?", "Müstakil evdeki bahçe, depo ve büyük parçaları keşifte listeliyor; yeni adresin kat ve asansör durumuna göre paketleme, söküm ve taşıma sırasını belirliyoruz."),
            ("Kilimli’den Zonguldak merkeze taşınma yapıyor musunuz?", "Evet. Kilimli içindeki taşınmaların yanı sıra Zonguldak merkeze, Kozlu’ya ve il genelindeki diğer adreslere taşıma yapıyoruz."),
        ],
    },
    {
        "slug": "caycuma", "name": "Çaycuma", "upper": "ÇAYCUMA", "locative": "Çaycuma’da", "ablative": "Çaycuma’dan",
        "place": "Çaycuma, Zonguldak",
        "description": "Çaycuma evden eve nakliyat: Filyos ve çevre köyler dahil paketleme, mobilya montajı ve asansörlü taşıma. Ücretsiz keşif ve net fiyat: 0552 475 01 67.",
        "hero": "Çaycuma merkez, Filyos ve çevre köylerde ev ve ofis taşımalarınızı ücretsiz keşifle planlıyoruz.",
        "lead": "Prestij Nakliyat, Çaycuma’da ve Filyos başta olmak üzere ilçenin mahalle ve köylerinde evden eve nakliyat, ofis taşımacılığı, paketleme, mobilya montajı ve asansörlü taşıma hizmeti verir.",
        "body": "Filyos Çayı boyunca uzanan Çaycuma; ilçe merkezi, Filyos kıyısı ve çevre köyleriyle geniş bir alana yayılır. Adresler arası mesafe arttıkça planlama önem kazandığı için eşyaları güvenle taşıyacak araç ve ekip düzenini keşifte belirliyoruz. Çaycuma’dan Zonguldak merkeze, Gökçebey’e, Devrek’e veya Ereğli’ye taşınmalarda da hizmet veriyoruz.",
        "check": "<strong>Mesafe ve güzergâh:</strong> Merkez, Filyos ve köy adresleri arasında araç ve ekip düzenini mesafeye göre planlıyoruz.",
        "faqs": [
            ("Çaycuma’da evden eve nakliyat fiyatı nasıl belirlenir?", PRICE_ANSWER),
            ("Filyos ve Çaycuma köylerine taşıma yapıyor musunuz?", "Evet. Çaycuma merkezinin yanı sıra Filyos ve çevre köylerdeki adreslere de taşıma yapıyoruz. Adresinizi ve eşya bilgilerinizi paylaştığınızda uygun planı birlikte çıkarıyoruz."),
            ("Çaycuma’dan başka bir ilçeye taşınma yapıyor musunuz?", "Evet. Zonguldak merkeze, Gökçebey, Devrek, Ereğli ve diğer ilçelere taşınmalarda hizmet veriyoruz; fiyatı mesafe ve eşya miktarına göre keşifte netleştiriyoruz."),
        ],
    },
    {
        "slug": "devrek", "name": "Devrek", "upper": "DEVREK", "locative": "Devrek’te", "ablative": "Devrek’ten",
        "place": "Devrek, Zonguldak",
        "description": "Devrek evden eve nakliyat: uzun yola uygun paketleme, mobilya montajı ve asansörlü taşıma. Devrek’ten il geneline taşıma, ücretsiz keşif: 0552 475 01 67.",
        "hero": "Devrek içi ve Devrek’ten Zonguldak geneline taşınmalarda eşyalarınızı yola uygun paketliyor, güvenle taşıyoruz.",
        "lead": "Prestij Nakliyat, Devrek’te evden eve nakliyat, ofis taşımacılığı, paketleme, mobilya montajı ve asansörlü taşıma hizmeti verir. Devrek içi taşınmaların yanı sıra Zonguldak merkeze ve diğer ilçelere taşınmalarda da yanınızdayız.",
        "body": "Zonguldak’ın iç kesiminde yer alan Devrek, bastonuyla tanınan köklü bir ilçedir. Devrek’ten merkeze ya da sahil ilçelerine yapılan taşınmalar daha uzun bir yol gerektirdiği için eşyaların yola uygun paketlenmesine ve araca dengeli yerleştirilmesine özellikle dikkat ediyoruz. Kış aylarında yol ve hava durumunu da hesaba katarak taşıma gününü sizinle birlikte belirliyoruz.",
        "check": "<strong>Uzun yol hazırlığı:</strong> Eşyaları yola uygun paketliyor, araca sabitleyerek dengeli yerleştiriyoruz.",
        "faqs": [
            ("Devrek’te evden eve nakliyat fiyatı nasıl belirlenir?", PRICE_ANSWER),
            ("Devrek’ten Zonguldak merkeze veya Ereğli’ye taşınma yapıyor musunuz?", "Evet. Devrek içindeki taşınmaların yanı sıra Zonguldak merkeze, Ereğli’ye ve il içindeki diğer ilçelere taşıma yapıyoruz."),
            ("Uzun yolda eşyalarım nasıl korunuyor?", "Eşyalar özel ambalaj malzemeleriyle paketlenir, araca sabitlenerek dengeli yerleştirilir. Eşyalarınız taşıma süresince sigorta güvencesi altındadır; kapsam hakkında ekibimizden bilgi alabilirsiniz."),
        ],
    },
    {
        "slug": "gokcebey", "name": "Gökçebey", "upper": "GÖKÇEBEY", "locative": "Gökçebey’de", "ablative": "Gökçebey’den",
        "place": "Gökçebey, Zonguldak",
        "description": "Gökçebey evden eve nakliyat: ilçe merkezi ve köylerde paketleme, mobilya montajı ve asansörlü taşıma. Ücretsiz keşif ve net fiyat: 0552 475 01 67.",
        "hero": "Gökçebey merkez ve çevre köylerde ev ve ofis taşımalarınızı ücretsiz keşifle planlıyor, güvenle taşıyoruz.",
        "lead": "Prestij Nakliyat, Gökçebey’de evden eve nakliyat, ofis taşımacılığı, paketleme, mobilya montajı ve asansörlü taşıma hizmeti verir. Gökçebey içindeki ve Gökçebey’den il geneline yapılan taşınmalar için ücretsiz keşifle net fiyat sunar.",
        "body": "Çaycuma ile Devrek arasında yer alan Gökçebey’de ilçe merkezindeki apartmanlardan çevre köylerdeki müstakil evlere kadar farklı adreslere taşıma yapıyoruz. Küçük bir ilçede bile taşımanın sorunsuz geçmesi iyi plana bağlıdır: eşya listesini, paketlenecek parçaları ve taşıma saatini keşifte birlikte netleştiriyoruz.",
        "check": "<strong>Eşya listesi:</strong> Taşınacak ve paketlenecek eşyaları keşifte birlikte listeleyip taşıma saatini netleştiriyoruz.",
        "faqs": [
            ("Gökçebey’de evden eve nakliyat fiyatı nasıl belirlenir?", PRICE_ANSWER),
            ("Gökçebey’den Çaycuma, Devrek veya Zonguldak merkeze taşınma yapıyor musunuz?", "Evet. Gökçebey içindeki taşınmaların yanı sıra Çaycuma, Devrek, Zonguldak merkez ve il genelindeki diğer adreslere taşıma yapıyoruz."),
            ("Mobilya sökme ve kurulum hizmete dahil mi?", "Mobilya sökme ve montaj hizmetimiz bulunmaktadır. Taşınacak mobilyaları paylaştığınızda teklifinize dahil edilecek işlemleri birlikte netleştiriyoruz."),
        ],
    },
    {
        "slug": "alapli", "name": "Alaplı", "upper": "ALAPLI", "locative": "Alaplı’da", "ablative": "Alaplı’dan",
        "place": "Alaplı, Zonguldak",
        "description": "Alaplı evden eve nakliyat: sahil ve yazlık konut taşımalarında paketleme, mobilya montajı ve asansörlü taşıma. Ücretsiz keşif: 0552 475 01 67.",
        "hero": "Alaplı’da sahil ve iç kesimdeki ev, yazlık ve ofis taşımalarınızı ücretsiz keşifle planlıyoruz.",
        "lead": "Prestij Nakliyat, Alaplı’da evden eve nakliyat, ofis taşımacılığı, paketleme, mobilya montajı ve asansörlü taşıma hizmeti verir. Zonguldak’ın batı ucundaki Alaplı’dan Ereğli’ye, Zonguldak merkeze ve il içindeki diğer adreslere taşınmalarda da hizmet veriyoruz.",
        "body": "Karadeniz kıyısında, Ereğli ile Düzce sınırı arasında yer alan Alaplı’da sahil şeridindeki apartmanlar ile iç kesimdeki müstakil evler farklı taşıma planı gerektirir. Yazlık ve sahil konutlarındaki taşınmalarda da eşyaların paketlenmesini, sökülüp kurulmasını ve yeni adrese yerleştirilmesini tek plan içinde yürütüyoruz.",
        "check": "<strong>Sahil ve yazlık konutlar:</strong> Sezonluk kullanılan evlerdeki eşyaları da paketleme ve kurulum dahil tek planla taşıyoruz.",
        "faqs": [
            ("Alaplı’da evden eve nakliyat fiyatı nasıl belirlenir?", PRICE_ANSWER),
            ("Alaplı’dan Ereğli’ye veya Zonguldak merkeze taşınma yapıyor musunuz?", "Evet. Alaplı içindeki taşınmaların yanı sıra Ereğli’ye, Zonguldak merkeze ve il genelindeki diğer ilçelere taşıma yapıyoruz."),
            ("Yazlık evden eşya taşıma yapıyor musunuz?", "Evet. Yazlık ve sahil konutlarındaki eşyaları paketleyip il içindeki yeni adresinize taşıyor, gerekirse mobilyaların söküm ve kurulumunu da yapıyoruz."),
        ],
    },
]

ALL_AREAS = ["Zonguldak Merkez", "Ereğli", "Çaycuma", "Devrek", "Gökçebey", "Alaplı", "Kilimli", "Kozlu"]


def page_file(d):
    return f"{d['slug']}-evden-eve-nakliyat.html"


def page_url(d):
    return f"{BASE}/{page_file(d)}"


def esc(text):
    return html.escape(text, quote=True)


# Tüm sayfaların stilleri tek dosyada (PageSpeed: tek oluşturma engelleyici istek). Sıra = eski <link> sırası (cascade korunur);
# kaynak dosyalar düzenlenir, site.css bu betikle üretilir. Leaflet CSS'i haritayla birlikte maps.js yükler.
CSS_BUNDLE = ["fonts", "styles", "hero", "services", "trust", "about", "process", "coverage", "contact", "footer", "gallery",
              "layout", "refinements", "district", "backdrop", "reveal", "discovery"]


def bundle_css():
    parts = []
    for name in CSS_BUNDLE:
        css = re.sub(r"/\*.*?\*/", "", read(f"{name}.css"), flags=re.S)
        lines = [line.strip() for line in css.splitlines() if line.strip()]
        parts.append(f"/* {name}.css */\n" + "\n".join(lines))
    write("site.css", "/* Üretilen dosya: python tools/build_districts.py — kaynak CSS dosyalarını düzenleyin. */\n"
          + "\n".join(parts) + "\n")


def read(name):
    return (ROOT / name).read_text(encoding="utf-8")


def write(name, content):
    (ROOT / name).write_text(content, encoding="utf-8", newline="\n")


def between(source, start, end):
    i = source.index(start)
    j = source.index(end, i) + len(end)
    return source[i:j]


def link_to_home(fragment):
    fragment = fragment.replace('href="#ana-sayfa"', 'href="index.html"')
    fragment = re.sub(r'href="#(?!icon-)', 'href="index.html#', fragment)
    fragment = fragment.replace(' is-active', '').replace(' aria-current="page"', '')
    return fragment


def organization():
    return {
        "@type": "MovingCompany",
        "@id": ORG_ID,
        "name": "Prestij Nakliyat",
        "alternateName": ["Prestij Evden Eve Nakliyat", "Prestij Nakliyat Zonguldak"],
        "url": f"{BASE}/",
        "logo": {"@type": "ImageObject", "url": f"{BASE}/assets/logo.png", "width": 600, "height": 600},
        "image": f"{BASE}/assets/og-image.jpg",
        "description": "Zonguldak merkez ve tüm ilçelerinde evden eve nakliyat, ofis taşımacılığı, paketleme, mobilya montajı ve asansörlü taşıma hizmeti veren nakliyat firması.",
        "slogan": SIGNATURE,
        "telephone": PHONE_SCHEMA,
        "address": {"@type": "PostalAddress", "streetAddress": ADDRESS_STREET, "addressLocality": ADDRESS_DISTRICT,
                    "addressRegion": "Zonguldak", "addressCountry": "TR"},
        "hasMap": MAPS_URL,
        "openingHoursSpecification": [HOURS_24_7],
        "areaServed": [{"@type": "AdministrativeArea", "name": "Zonguldak"}]
        + [{"@type": "City", "name": d["place"], "url": page_url(d)} for d in DISTRICTS],
        "contactPoint": {
            "@type": "ContactPoint", "telephone": PHONE_SCHEMA, "contactType": "customer service",
            "areaServed": "TR", "availableLanguage": "Turkish",
            "hoursAvailable": HOURS_24_7,
        },
        "knowsAbout": ["Evden eve nakliyat", "Ofis taşımacılığı", "Mobilya montajı", "Eşya paketleme", "Asansörlü taşıma"],
        "hasOfferCatalog": {
            "@type": "OfferCatalog", "name": "Nakliyat hizmetleri",
            "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": n, "description": t}} for n, t in SERVICES],
        },
    }


def website():
    return {"@type": "WebSite", "@id": SITE_ID, "url": f"{BASE}/", "name": "Prestij Nakliyat", "inLanguage": "tr-TR", "publisher": {"@id": ORG_ID}}


def breadcrumb(url, items):
    return {"@type": "BreadcrumbList", "@id": f"{url}#breadcrumb", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": name, "item": item} for i, (name, item) in enumerate(items)]}


def faq_page(url, faqs):
    return {"@type": "FAQPage", "@id": f"{url}#sss", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}


def seo_head(title, description, url, nodes, og_type="website"):
    graph = json.dumps({"@context": "https://schema.org", "@graph": nodes}, ensure_ascii=False, separators=(",", ":"))
    graph = graph.replace("</", "<\\/")
    return f"""<!-- seo:start (tools/build_districts.py üretir) -->
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(description)}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="{url}">
  <meta name="geo.region" content="TR-67">
  <meta name="geo.placename" content="Zonguldak">
  <meta property="og:type" content="{og_type}">
  <meta property="og:locale" content="tr_TR">
  <meta property="og:site_name" content="Prestij Nakliyat">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(description)}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{OG_IMAGE}">
  <meta property="og:image:type" content="image/jpeg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="{esc(OG_IMAGE_ALT)}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc(title)}">
  <meta name="twitter:description" content="{esc(description)}">
  <meta name="twitter:image" content="{OG_IMAGE}">
  <meta name="twitter:image:alt" content="{esc(OG_IMAGE_ALT)}">
  <link rel="icon" href="favicon.ico?v=20260927-7" sizes="16x16 32x32 48x48">
  <link rel="icon" href="assets/favicon-16x16.png?v=20260927-7" type="image/png" sizes="16x16">
  <link rel="icon" href="assets/favicon-32x32.png?v=20260927-7" type="image/png" sizes="32x32">
  <link rel="icon" href="assets/favicon-48x48.png?v=20260927-7" type="image/png" sizes="48x48">
  <link rel="icon" href="favicon.png?v=20260927-7" type="image/png" sizes="512x512">
  <link rel="apple-touch-icon" href="assets/apple-touch-icon.png?v=20260927-7" sizes="180x180">
  <script type="application/ld+json">{graph}</script>
  <!-- seo:end -->"""


def inject_seo(name, block):
    source = read(name)
    if "<!-- seo:start" in source:
        source = re.sub(r"<!-- seo:start.*?<!-- seo:end -->", lambda _: block, source, count=1, flags=re.S)
    else:
        source = re.sub(r'<meta name="description".*?<link rel="icon"[^>]*>', lambda _: block, source, count=1, flags=re.S)
    write(name, source)


def visible_faqs(source):
    pairs = re.findall(r"<summary>(.*?)<span[^>]*></span></summary><p>(.*?)</p>", source, flags=re.S)
    return [(html.unescape(re.sub("<[^>]+>", "", q)).strip(), html.unescape(re.sub("<[^>]+>", "", a)).strip()) for q, a in pairs]


def home_seo(index):
    url = f"{BASE}/"
    title = "Zonguldak Evden Eve Nakliyat | Prestij Nakliyat"
    description = ("Zonguldak evden eve nakliyat: Merkez, Ereğli, Çaycuma, Devrek, Alaplı, Kilimli, Kozlu ve Gökçebey’de "
                   "paketlemeli, sigortalı, asansörlü taşıma. Ücretsiz keşif: 0552 475 01 67.")
    nodes = [organization(), website(),
             {"@type": "WebPage", "@id": f"{url}#sayfa", "url": url, "name": title, "description": description,
              "inLanguage": "tr-TR", "isPartOf": {"@id": SITE_ID}, "about": {"@id": ORG_ID},
              "primaryImageOfPage": f"{BASE}/assets/og-image.jpg"},
             faq_page(url, visible_faqs(index))]
    return seo_head(title, description, url, nodes)


# Google "Resim meta verisi": creator satır içi Organization olmalı (@id referansı "geçersiz nesne türü" sayılıyor);
# license galerideki görünür kullanım notunu (#gorsel-kullanim), acquireLicensePage iletişim bölümünü gösterir.
IMAGE_RIGHTS = {
    "creator": {"@type": "Organization", "name": "Prestij Nakliyat", "url": f"{BASE}/"},
    "creditText": "Prestij Nakliyat",
    "copyrightNotice": "© 2026 Prestij Nakliyat. Tüm hakları saklıdır.",
    "license": f"{BASE}/galeri.html#gorsel-kullanim",
    "acquireLicensePage": f"{BASE}/#iletisim",
}


def gallery_seo(gallery):
    url = f"{BASE}/galeri.html"
    title = "Galeri – Taşımalarımızdan Kareler | Prestij Nakliyat Zonguldak"
    description = "Prestij Nakliyat galerisi: Zonguldak’taki evden eve nakliyat, paketleme ve taşıma işlerimizden gerçek fotoğraflar."
    images = re.findall(r'<img src="(assets/gallery/[^"]+)" width="(\d+)" height="(\d+)" alt="([^"]+)"', gallery)
    assert 'id="gorsel-kullanim"' in gallery, "galeri.html'de license adresinin gösterdiği görsel kullanım notu yok"
    nodes = [organization(), website(),
             {"@type": ["CollectionPage", "ImageGallery"], "@id": f"{url}#sayfa", "url": url, "name": title,
              "description": description, "inLanguage": "tr-TR", "isPartOf": {"@id": SITE_ID}, "about": {"@id": ORG_ID},
              "breadcrumb": {"@id": f"{url}#breadcrumb"},
              "image": [{"@type": "ImageObject", "contentUrl": f"{BASE}/{src}", "width": int(w), "height": int(h),
                         "caption": html.unescape(alt), **IMAGE_RIGHTS} for src, w, h, alt in images]},
             breadcrumb(url, [("Ana Sayfa", f"{BASE}/"), ("Galeri", url)])]
    return seo_head(title, description, url, nodes), images


def district_seo(d):
    url = page_url(d)
    title = f"{d['name']} Evden Eve Nakliyat | Prestij Nakliyat Zonguldak"
    nodes = [organization(), website(),
             {"@type": "WebPage", "@id": f"{url}#sayfa", "url": url, "name": title, "description": d["description"],
              "inLanguage": "tr-TR", "isPartOf": {"@id": SITE_ID}, "about": {"@id": f"{url}#hizmet"},
              "breadcrumb": {"@id": f"{url}#breadcrumb"}, "primaryImageOfPage": f"{BASE}/assets/og-image.jpg"},
             {"@type": "Service", "@id": f"{url}#hizmet", "name": f"{d['name']} Evden Eve Nakliyat",
              "serviceType": "Evden eve nakliyat", "description": d["lead"], "provider": {"@id": ORG_ID},
              "areaServed": {"@type": "City", "name": d["place"]}, "url": url},
             breadcrumb(url, [("Ana Sayfa", f"{BASE}/"), ("Hizmet Bölgemiz", f"{BASE}/#hizmet-bolgemiz"), (d["name"], url)]),
             faq_page(url, d["faqs"])]
    return seo_head(title, d["description"], url, nodes)


def area_links(current=None):
    items = []
    for area in ALL_AREAS:
        d = next((x for x in DISTRICTS if x["name"] == area), None)
        href = page_file(d) if d else "index.html"
        if d is current:
            continue
        cls = ' class="coverage-district--central"' if d is None else ""
        items.append(f'<li{cls}><svg aria-hidden="true"><use href="#icon-pin"/></svg><a href="{href}">{area}</a></li>')
    return "\n          ".join(items)


def district_page(d, parts, version):
    css = ('  <link rel="preload" href="assets/fonts/roboto-condensed-variable.woff2" as="font" type="font/woff2" crossorigin>\n'
           '  <link rel="preload" href="assets/fonts/montserrat-variable.woff2" as="font" type="font/woff2" crossorigin>\n'
           f'  <link rel="stylesheet" href="site.css?v={version}">')
    services = "\n            ".join(
        f"<li><strong>{n}:</strong> {t}</li>" for n, t in [
            ("Evden Eve Nakliyat", f"{d['locative']} ve {d['ablative']} Zonguldak geneline ev taşıma."),
            ("Ofis Taşımacılığı", "İşinizi aksatmayacak şekilde planlanan ofis ve iş yeri taşıma."),
            ("Paketleme Hizmeti", "Eşyaların özel ambalaj malzemeleriyle korunarak paketlenmesi."),
            ("Mobilya Montajı", "Mobilyaların sökülmesi, taşınması ve yeni adreste kurulması."),
            ("Asansörlü Taşıma", "Yüksek katlarda hızlı, güvenli ve pratik taşıma."),
        ])
    checks = "\n            ".join(f"<li>{c}</li>" for c in [d["check"], *COMMON_CHECKS])
    faqs = "\n          ".join(
        f'<details name="district-faq"{" open" if i == 0 else ""}><summary>{esc(q)}<span aria-hidden="true"></span></summary><p>{esc(a)}</p></details>'
        for i, (q, a) in enumerate(d["faqs"]))
    discovery = parts["discovery"].replace(DISCOVERY_TITLE, f"{d['name']} taşınmanız için<br><span>planı birlikte yapalım.</span>")
    footer = parts["footer"].replace(f'<a href="{page_file(d)}">', f'<a href="{page_file(d)}" aria-current="page">')
    return f"""<!doctype html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#030303">
  {district_seo(d)}
{css}
  <link rel="preload" as="image" href="assets/opt/hero-coast-fiat-1280.webp" imagesrcset="assets/opt/hero-coast-fiat-960.webp 960w, assets/opt/hero-coast-fiat-1280.webp 1280w, assets/opt/hero-coast-fiat-1672.webp 1672w" imagesizes="(max-width: 650px) 176vw, 100vw" fetchpriority="high">
  <script src="script.js?v={version}" defer></script>
  <script src="reveal.js?v={version}" defer></script>
  <script src="services.js?v={version}" defer></script>
</head>
<body id="ana-sayfa" data-page="district">
  <!-- Bu dosya tools/build_districts.py ile üretilir; doğrudan düzenlemeyin. -->
  {parts["header"]}
  <main id="site-content" aria-label="Sayfa içeriği">
    {parts["icons"]}
    <section class="hero hero--district" aria-label="{d['name']} evden eve nakliyat">
      <div class="hero-slides">
        <article class="hero-slide is-current">
          <img class="hero-image" src="assets/opt/hero-coast-fiat-1280.webp" srcset="assets/opt/hero-coast-fiat-960.webp 960w, assets/opt/hero-coast-fiat-1280.webp 1280w, assets/opt/hero-coast-fiat-1672.webp 1672w" sizes="(max-width: 650px) 176vw, 100vw" alt="Gün batımında sahil yolunda, kasası siyah ve altın Prestij Nakliyat tasarımıyla kaplanmış beyaz Fiat Ducato kamyonet" fetchpriority="high" width="1672" height="941">
          <div class="hero-shade" aria-hidden="true"></div>
          <div class="hero-copy">
            <p class="hero-eyebrow"><svg aria-hidden="true"><use href="#icon-pin"/></svg>ZONGULDAK · {d['upper']}</p>
            <h1 class="hero-title"><span>{d['name']}</span><span class="gold-text hero-title-emphasis">Evden Eve</span><span>Nakliyat</span></h1>
            <p class="hero-description">{d['hero']}</p>
            <div class="hero-actions">
              <a class="hero-button hero-button--gold" href="tel:{PHONE_TEL}"><svg aria-hidden="true"><use href="#icon-quote"/></svg><span>Ücretsiz Fiyat Teklifi Al</span><svg class="button-arrow" aria-hidden="true"><use href="#icon-arrow"/></svg></a>
              <a class="hero-button hero-button--green" href="{WHATSAPP}" target="_blank" rel="noopener noreferrer"><svg aria-hidden="true"><use href="#icon-whatsapp"/></svg><span>WhatsApp’tan Yazın</span><svg class="button-arrow" aria-hidden="true"><use href="#icon-arrow"/></svg></a>
            </div>
            <ul class="hero-benefits hero-benefits--compact">
              <li><span class="benefit-icon"><svg aria-hidden="true"><use href="#icon-shield"/></svg></span><span><strong>%100</strong>Güvenli Taşıma</span></li>
              <li><span class="benefit-icon"><svg aria-hidden="true"><use href="#icon-team"/></svg></span><span><strong>Profesyonel</strong>Ekip</span></li>
              <li><span class="benefit-icon"><svg aria-hidden="true"><use href="#icon-bars"/></svg></span><span><strong>Ücretsiz</strong>Keşif</span></li>
              <li><span class="benefit-icon"><svg aria-hidden="true"><use href="#icon-diamond"/></svg></span><span><strong>Sigortalı</strong>Taşıma</span></li>
            </ul>
          </div>
        </article>
      </div>
    </section>
    <section class="district" aria-labelledby="district-title">
      <nav class="district-breadcrumb" aria-label="Sayfa konumu">
        <ol><li><a href="index.html">Ana Sayfa</a></li><li><a href="index.html#hizmet-bolgemiz">Hizmet Bölgemiz</a></li><li aria-current="page">{d['name']}</li></ol>
      </nav>
      <div class="district-intro">
        <p class="district-eyebrow">{d['upper']} EVDEN EVE NAKLİYAT</p>
        <h2 id="district-title">{d['locative']} planlı ve sigortalı evden eve nakliyat</h2>
        <p class="district-lead">{d['lead']}</p>
        <p>{d['body']}</p>
      </div>
      <div class="district-grid">
        <article class="district-card">
          <h3>{d['locative']} sunduğumuz hizmetler</h3>
          <ul class="district-list">
            {services}
          </ul>
        </article>
        <article class="district-card">
          <h3>{d['name']} taşımalarında dikkat ettiklerimiz</h3>
          <ul class="district-list">
            {checks}
          </ul>
        </article>
      </div>
      <div class="district-faq">
        <h2>{d['name']} evden eve nakliyat hakkında sık sorulanlar</h2>
        <div class="faq-list">
          {faqs}
        </div>
      </div>
      <div class="discovery-shell">
        {discovery}
      </div>
      <div class="district-others">
        <h2>Diğer hizmet bölgelerimiz</h2>
        <ul class="coverage-districts" aria-label="Zonguldak’ta hizmet verdiğimiz diğer bölgeler">
          {area_links(d)}
        </ul>
      </div>
    </section>
    {parts["dialog"]}
  </main>
  {footer}
  {parts["mobile"]}
</body>
</html>
"""


def sitemap(gallery_images):
    home_images = ["assets/og-image.jpg"]
    entries = [(f"{BASE}/", "1.0", home_images), (f"{BASE}/galeri.html", "0.6", [s for s, *_ in gallery_images])]
    entries += [(page_url(d), "0.8", []) for d in DISTRICTS]
    body = []
    for loc, priority, images in entries:
        imgs = "".join(f"\n    <image:image><image:loc>{BASE}/{src}</image:loc></image:image>" for src in images)
        body.append(f"  <url>\n    <loc>{loc}</loc>\n    <lastmod>{LASTMOD}</lastmod>\n    <priority>{priority}</priority>{imgs}\n  </url>")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n'
            + "\n".join(body) + "\n</urlset>\n")


def robots():
    ai_bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "Claude-User",
               "PerplexityBot", "Perplexity-User", "Google-Extended", "Applebot-Extended", "CCBot"]
    lines = ["# Arama motorları", "User-agent: *", "Allow: /", "Disallow: /tools/", "Disallow: /*.md$", "",
             "# Yapay zekâ arama ve yanıt motorları (GEO): içerik alıntılanabilir"]
    for bot in ai_bots:
        lines += [f"User-agent: {bot}", "Allow: /", "Disallow: /tools/", ""]
    lines.append(f"Sitemap: {BASE}/sitemap.xml")
    return "\n".join(lines) + "\n"


def llms(index):
    faqs = "\n".join(f"- **{q}** {a}" for q, a in visible_faqs(index))
    districts = "\n".join(f"- [{d['name']} evden eve nakliyat]({page_url(d)}): {d['lead']}" for d in DISTRICTS)
    services = "\n".join(f"- {n}: {t}" for n, t in SERVICES)
    return f"""# Prestij Nakliyat

> Prestij Nakliyat, Zonguldak merkez ve tüm ilçelerinde (Ereğli, Çaycuma, Devrek, Gökçebey, Alaplı, Kilimli, Kozlu) evden eve nakliyat, ofis taşımacılığı, paketleme, mobilya montajı ve asansörlü taşıma hizmeti veren bir nakliyat firmasıdır. Ücretsiz keşifle net fiyat verir. Telefon ve WhatsApp: {PHONE_DISPLAY}.

## Temel bilgiler

- Firma adı: Prestij Nakliyat
- Hizmet bölgesi: Zonguldak ili (Merkez, Ereğli, Çaycuma, Devrek, Gökçebey, Alaplı, Kilimli, Kozlu)
- Adres: {ADDRESS_FULL}
- Telefon / WhatsApp: {PHONE_DISPLAY} ({PHONE_TEL})
- Çalışma saatleri: 7/24 (haftanın her günü, günün her saati); telefonla veya WhatsApp üzerinden ulaşılabilir
- Fiyatlandırma: eşya miktarı, kat ve bina durumu, asansör ve paketleme ihtiyacı ile mesafeye göre; ücretsiz keşifte net fiyat verilir
- Web sitesi: {BASE}/

## Hizmetler

{services}

## İlçe sayfaları

- [Zonguldak evden eve nakliyat (ana sayfa)]({BASE}/): Zonguldak merkez ve tüm ilçeler.
{districts}

## Sık sorulan sorular

{faqs}

## Diğer sayfalar

- [Galeri]({BASE}/galeri.html): Taşımalarımızdan gerçek fotoğraflar.
"""


def main():
    index = read("index.html")
    version = re.search(r'site\.css\?v=([\w-]+)', index).group(1)
    bundle_css()
    parts = {
        "header": link_to_home(between(index, '<header class="site-header">', "</header>")),
        "icons": between(index, '<svg class="icon-library"', "</symbol>\n    </svg>"),
        "dialog": between(index, '<dialog class="service-dialog"', "</dialog>"),
        "footer": link_to_home(between(index, '<footer class="site-footer"', "</footer>")),
        "mobile": between(index, '<nav class="mobile-actions"', "</nav>"),
        "discovery": link_to_home(between(index, '<section class="discovery"', "</section>")),
    }
    assert DISCOVERY_TITLE in parts["discovery"], "index.html'deki keşif başlığı değişti: DISCOVERY_TITLE'ı güncelleyin"
    for d in DISTRICTS:
        write(page_file(d), district_page(d, parts, version))
    inject_seo("index.html", home_seo(read("index.html")))
    gallery_block, gallery_images = gallery_seo(read("galeri.html"))
    inject_seo("galeri.html", gallery_block)
    write("sitemap.xml", sitemap(gallery_images))
    write("robots.txt", robots())
    write("llms.txt", llms(read("index.html")))
    print(f"{len(DISTRICTS)} ilçe sayfası, sitemap.xml, robots.txt, llms.txt üretildi (v={version}).")


if __name__ == "__main__":
    main()
