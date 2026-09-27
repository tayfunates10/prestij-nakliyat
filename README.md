# Prestij Nakliyat

İlk bölüm: referans görsele göre siyah ve altın tonlarında duyarlı üst menü.

`index.html` dosyası statik bir sunucuyla veya doğrudan tarayıcıda açılabilir. Derleme gerektirmez.

## Kapsam

- Logo, kullanıcının referans görselinden SVG görüntü alanıyla gösterilir; orijinal kaynak değiştirilmemiştir. Ayrı şeffaf logo sağlanırsa bu kaynakla değiştirilebilir.
- Masaüstü menü, mobil açılır menü, telefon bağlantısı, altın ışık ve parlama efektleri.
- Animasyonlar sabit görsele göre yorumlanmıştır; birebir hareket eşleşmesi için video gerekir.
- Görseldeki tarayıcı adres çubuğu siteye dahil değildir.
- Telefon numarası referanstaki haliyle kullanılmıştır; yayına çıkmadan önce işletmenin numarasıyla doğrulanmalıdır.
- Menü bağlantıları sonraki bölümlerin kimliklerine hazırdır: `hakkimizda`, `hizmetlerimiz`, `tasinma-sureci`, `sss`, `galeri`, `iletisim`. Tüm bölümler sayfaya eklenmiştir.
- Yazı tipi: Google Fonts üzerinden Roboto Condensed; bağlantı yoksa Arial Narrow / Arial.
- Hareket azaltma tercihi desteklenir.

Sonraki bölümler `#site-content` içine eklenir.

## Hero — ikinci bölüm

İki hero slaytı `hero.css` ve `hero.js` ile eklendi. Slaytlar 7 saniyede bir 1 saniyelik yumuşak geçiş yapar. Önceki, duraklat/başlat ve sonraki olmak üzere üç eşit dairesel kontrol vardır. İlk geçiş sayfa yüklendikten 7 saniye sonradır. Klavye odağı hero içindeyken ve sekme gizlendiğinde otomatik geçiş bekler; fareyle üzerinde durmak geçişi durdurmaz. Hareket azaltma tercihi açıkken otomatik geçiş başlangıçta kapalıdır. Etkin olmayan slayt klavye ve ekran okuyucudan gizlenir.

Hero görsellerinde kullanıcının beyaz Fiat Ducato kamyoneti ve kasaya perspektifli Prestij kaplaması kullanıldı. Üretim yöntemi ve tam istemler `assets/hero-generation.md` içinde kayıtlıdır. Görselden bağımsız HTML başlıklar ve bağlantılar kullanılır. Teklif düğmeleri sayfadaki teklif formuna; WhatsApp düğmeleri sohbet ekranına gider. Her iki bağlantı da ilk referanstaki örnek telefon numarasını kullanır.

Kullanıcının örneğindeki pazarlama metinleri korunmuştur; bunlar bağımsız olarak doğrulanmış hizmet beyanları değildir. Görseller referans kompozisyonuna göre oluşturulmuş temsili sahnelerdir.

## Hizmetlerimiz — üçüncü bölüm

`#hizmetlerimiz` bölümü beş hizmet kartını içerir. Fotoğraflar sağlanan `assets/services-reference.png` dosyasından SVG görüntü alanlarıyla gösterilir; orijinal görsel dosyası değiştirilmemiştir. Başlıklar, açıklamalar, ikonlar ve düğmeler bağımsız arayüz öğeleridir.

Geniş ekranda beş sütun; daha dar ekranlarda üç, iki ve tek sütun kullanılır. Altın çerçeve ışıkları ve kart üzerine gelindiğinde hafif yükselme efekti vardır. Hareket azaltma tercihi desteklenir.

Her Detayları İncele düğmesi hizmet açıklamasını yerel bir dialog içinde açar. Kapat düğmesi, Escape ve pencere dışına tıklama desteklenir. Kapanışta klavye odağı açan düğmeye döner. Bilgi ve fiyat teklifi bağlantısı mevcut telefon numarasını kullanır.

## Neden Prestij — dördüncü bölüm

`#neden-prestij` bölümünde referanstaki büyük logo ve altı avantaj bulunur: %100 Güvenli Taşıma, Profesyonel Ekip, Zamanında Teslimat, Uygun Fiyat, Sigortalı Taşıma, 7/24 İletişim. Logo ve ikonlar sağlanan `assets/trust-reference.png` görselinden SVG görüntü alanlarıyla gösterilir. Metinler HTML olarak yazılmıştır. Referanstaki hizmet beyanları kullanıcı tarafından sağlanan içerik olarak korunmuştur.

Altın ayırıcı çizgiler ve ışık efektleri CSS ile oluşturulmuştur. Yerleşim masaüstünde altı, tablette üç, telefonda iki sütundur. Hareket azaltma tercihi desteklenir. 7/24 İletişim başlığı mevcut telefon bağlantısını kullanır.

## Hakkımızda — beşinci bölüm

`#hakkimizda` bölümünde kullanıcı referansındaki ekip fotoğrafı, açıklama, dört özellik, altın dalga, dört istatistik ve el yazısı slogan yer alır. Fotoğraf, ikonlar ve slogan `assets/about-reference.png` kaynağından SVG görüntü alanlarıyla gösterilir; metinler ve istatistikler HTML'dir. 500+ müşteri, 1.000+ taşıma ve 10+ yıl değerleri kullanıcı referansından alınmıştır; bağımsız doğrulama yapılmamıştır.

Masaüstünde fotoğraf solda ve açıklama sağda; mobilde üst üste yerleşir. Özellikler mobilde tek, istatistikler iki sütundur. Hakkımızda menü bağlantısı bu bölüme gider. Görselin dalga çizgisi basit SVG geometriyle yeniden oluşturulmuştur. Hareket azaltma tercihi desteklenir.

## Taşıma Süreci — altıncı bölüm

`#tasinma-sureci` bölümünde kullanıcının referansındaki başlık, ekip sahnesi ve numaralı beş adım yer alır: İletişim, Keşif & Planlama, Paketleme, Taşıma, Montaj & Teslimat. Fotoğraflar ve içlerindeki hizmet ikonları `assets/process-reference.png` kaynağından SVG görüntü alanlarıyla gösterilir. Kart metinleri ve numaralar bağımsız HTML öğeleridir. Beş adım semantik sıralı liste olarak düzenlenmiştir.

Masaüstünde beş sütun, daha dar ekranlarda üç ve iki sütun, telefonda tek sütun kullanılır. Telefonda bağlantı okları aşağıya döner. Hareket azaltma tercihi desteklenir. Üst menüdeki Taşınma Süreci bağlantısı bu bölüme gider.

## Hizmet Bölgemiz — yedinci bölüm

`#hizmet-bolgemiz` bölümü, sağlanan tam sayfa tasarımından yalnızca hizmet bölgesi alanını uygular. Zonguldak Merkez, Ereğli, Çaycuma, Devrek, Gökçebey, Alaplı, Kilimli ve Kozlu etiketleri semantik bir listedir; filtre veya seçim düğmesi değildir. Merkez etiketi altın dolguludur.

Sağdaki temsili harita, `assets/coverage-reference.png` içindeki ilgili SVG görüntü alanından gösterilir; etkileşimli coğrafi harita değildir. Mobilde harita metin ve etiketlerin altına geçer. Diğer referans bölümleri bu değişikliğe dahil edilmemiştir.

## SSS, teklif ve iletişim — sekizinci bölüm

Üç sütunlu `contact-strip` alanında beş açılır soru, teklif formu, telefon/WhatsApp/e-posta bağlantıları ve referans harita bulunur. `#sss`, `#teklif-al`, `#iletisim` bağlantıları desteklenir. Harita Zonguldak Merkez aramasını açar; gösterilen işaretin gerçek işletme adresi olduğu doğrulanmamıştır. İletişim bilgileri kullanıcı referansından alınmıştır.

Form ad, Türkiye telefon numarası, çıkış/varış adresi ve isteğe bağlı not toplar. Gönderim, bu bilgileri kodlanmış metin olarak WhatsApp sohbetine hazırlar; ziyaretçi orada kendisi gönderir. Sunucuya kayıt, otomatik mesaj, e-posta gönderimi veya tarayıcıda kalıcı saklama yoktur. Arayüz bu davranışı açıklar. Açılır pencere engellenirse devam bağlantısı gösterilir. Telefon numarası diğer bölümlerdeki örnek `0532 123 45 67` numarasıdır. Yayına almadan önce gerçek iletişim bilgileri teyit edilmelidir.

İlk SSS açık başlar; başka soru açıldığında önceki kapanır. Yerleşim geniş ekranda üç sütun, tablette iki sütun ve altta iletişim, telefonda tek sütundur. Form doğrulaması ve klavye erişimi desteklenir.

## Footer — dokuzuncu bölüm

Referans düzenine göre logo, hizmet bağlantıları, kurumsal alan, hizmet bölgeleri, sosyal medya ikonları ve el yazısı slogan eklendi. Hizmet düğmeleri mevcut detay pencerelerini açar; kurumsal bağlantılar hazır bölümlere gider. Bölge bağlantıları hizmet bölgesi alanını açar. Logo sayfa başına döner. Alt satırda 2026 telif bilgisi ve hizmet sloganları yer alır.

Kullanıcının isteğiyle yalnızca Instagram ikonu gösterilir ve `https://instagram.com` adresine bağlanır; kullanıcı hesap adresini daha sonra değiştirecektir. Galeri bağlantısı `#galeri` bölümüne gider. El yazısı `assets/coverage-reference.png` içindeki footer görselinden alınır.

## Galeri

Hizmet Bölgemiz ile SSS/teklif/iletişim alanları arasına dört kullanıcı fotoğrafından oluşan `#galeri` bölümü eklendi. `assets/gallery/` altındaki kaynak JPEG'ler değiştirilmeden kopyalandı. Her kartın altındaki HTML bandında Prestij Nakliyat, mevcut iletişim numarası ve Zonguldak Merkez bulunur; bu bant fotoğraf dosyasına işlenmemiştir.

Önizlemeler eşit boyda alanlara yerleşir; tıklandığında fotoğrafın tamamı kırpılmadan dialog içinde gösterilir. Önceki/sonraki, yön tuşları, Escape, kapatma düğmesi ve dışarı tıklama desteklenir. Telefon linkleri ayrı tıklanabilir öğelerdir. Masaüstünde dört, tablette iki ve mobilde tek sütundur. Üst menü ve footer galeriye bağlanmıştır.

## 26 Eylül — ölçü ve arayüz düzeltmeleri

Son yüklenen `layout.css`, bölümleri ortak 1600 piksel üst genişlikte toplar; başlık, kart, ikon ve boşluk ölçeklerini ekran boyutuna göre dengeler. Header arama kutusu grid içinde tutulur; tüm menü alt çizgileri 42 pikseldir. İki hero slaytı aynı ilk görseli, logoyu, butonları ve yerleşimi kullanır; sadece başlık, açıklama ve rozetler değişir. Rozet çemberleri sabit kare ölçüde, net 2 piksel kenarlıklıdır. Hizmet başlığının dekoratif çizgileri kaldırıldı. Hizmet fotoğrafları gömülü yuvarlak ikonlar görünmeyecek şekilde gösterilir; bağımsız kare ikonlar 60 × 60 pikseldir.

Doğrulama: 320–1983 piksel arasında 13 ekran genişliğinde taşma, header kutusu, eşit menü çizgileri ve kare ikon ölçüleri; 7 saniyelik otomatik geçiş, önceki/sonraki ve klavye kontrolleri; hizmet/galeri pencereleri, SSS ve form doğrulaması. WhatsApp form testi bağlantıyı yakalayarak yapıldı, mesaj gönderilmedi.

## İkinci düzeltme turu

- Header/hero kenarlara tam oturur, hero içindeki ikinci logo kaldırılmıştır.
- Neden Prestij bölümü altı sade kart ve aynı çizgi sistemindeki vektör ikonlarla yeniden tasarlanmıştır. Hakkımızda etiketi eşit yan çizgilerin merkezindedir. Özellik ikonları SVG'dir; alt rozetler Planlı, Özenli, Eksiksiz ve Zonguldak olarak güncellenmiştir.
- Taşıma süreci görseli kendi sınırları içindedir; fotoğrafa gömülü eski ikonlar görünümden çıkarılmış, simetrik yeni ikonlar ve dolu oklar eklenmiştir.
- Hizmet bölgesi ve iletişim haritaları Leaflet 1.9.4 ile gerçek OpenStreetMap verisi kullanır. Haritalar görünür olduklarında yüklenir; sürükleme, +/−, dokunmatik yakınlaştırma desteklenir. Sayfa kaydırmasını engellememesi için fare tekerleğiyle yakınlaştırma kapalıdır. Siyah/altın görünüm CSS ile uygulanır, atıf ayrı ve okunaklıdır.
- İşaret 41.4535, 31.7894 koordinatındaki Zonguldak merkezini gösterir; doğrulanmış işletme adresi değildir. İşletmenin konumu geldiğinde `maps.js` içindeki merkez/işaret bilgileri ve haritada aç bağlantısı güncellenmelidir.
- OpenStreetMap standart karo sunucusu: https://tile.openstreetmap.org/{z}/{x}/{y}.png. Normal tarayıcı önbelleği korunur, önceden indirme/offline paketleme yapılmaz. Kullanım politikası: https://operations.osmfoundation.org/policies/tiles/ . Testlerde harita karoları taklit edilmiştir; gerçek görünüm uygulama tarayıcısında kontrol edilmiştir. Leaflet: https://leafletjs.com/examples/quick-start/ . Yerel kütüphane lisansı `assets/vendor/leaflet/LICENSE` içindedir.
- `galeri.html` tüm galeri fotoğraflarını gösterir; ana sayfadaki “Tüm Galeriyi Gör” butonu bu sayfaya gider. Header, hero, footer ve mobil hızlı işlem çubuğu `index.html` ile birebir aynıdır (bölüm bağlantıları `index.html#…` biçimindedir); bu alanlarda yapılan her değişiklik iki dosyaya da uygulanmalıdır. Sayfa her açılışta en üstten başlar. Yeni fotoğraf eklerken kartı `galeri.html` içine sıradaki `data-photo` numarasıyla ekleyin; ana sayfada ilk 4 fotoğraf kalır.
- Galeri alt bantları fotoğraf alanının içindedir. Tekrarlanabilir tasarım ve başka görsel araçları için talimatlar `GALERI-TASARIM-REHBERI.md` içindedir.
- Footer sloganı `assets/footer-signature.svg` içinde yeniden oluşturulmuştur; düşük çözünürlüklü raster kırpımı kullanılmaz.

## SEO / GEO — 27 Eylül

Hedef anahtar kelime: **zonguldak evden eve nakliyat**. İlçe aramaları için her ilçenin kendi açılış sayfası vardır. Alan adı: `https://prestijevdenevenakliyat.com`.

- İlçe sayfaları: `eregli-`, `kozlu-`, `kilimli-`, `caycuma-`, `devrek-`, `gokcebey-`, `alapli-evden-eve-nakliyat.html`. Zonguldak Merkez ana sayfadır. Her sayfada ilçeye özgü H1, özet paragraf, hizmetler, dikkat edilen noktalar, 3 soruluk SSS, ücretsiz keşif alanı ve diğer ilçelere bağlantılar bulunur.
- Hizmet Bölgemiz etiketleri ve footer bölge bağlantıları ilçe sayfalarına gider (iç bağlantı).
- **Tek kaynak:** `python tools/build_districts.py` ilçe sayfalarını, `index.html` / `galeri.html` içindeki `<!-- seo:start -->…<!-- seo:end -->` bloğunu (title, description, canonical, Open Graph, JSON-LD), `sitemap.xml`, `robots.txt` ve `llms.txt` dosyalarını yeniden üretir. Header, footer veya SSS değiştikten sonra betiği çalıştırın; ilçe sayfalarını ve SEO bloğunu elle düzenlemeyin.
- JSON-LD: `MovingCompany` (telefon, Zonguldak adresi, hizmet bölgeleri, 7/24 iletişim, hizmet kataloğu), `WebSite`, `WebPage`, `FAQPage` (sayfadaki görünür sorularla birebir), ilçe sayfalarında `Service` + `BreadcrumbList`, galeride `ImageGallery`.
- E-posta gerçek olmadığı için yapısal veriye eklenmedi. Instagram hesabı gelince `organization()` içine `sameAs` olarak eklenmeli. Açık sokak adresi yoktur; Google İşletme Profili'nde hizmet bölgesi işletmesi olarak aynı telefon ve bölgeler kullanılmalıdır.
- `robots.txt` arama motorlarına ve yapay zekâ tarayıcılarına (GPTBot, ClaudeBot, PerplexityBot, Google-Extended vb.) izin verir; `tools/` ve `.md` dosyalarını kapatır. `llms.txt` firmanın özetini, hizmetleri, ilçe sayfalarını ve SSS'yi yapay zekâ motorları için sade metinle sunar.
- Paylaşım görseli `assets/og-image.jpg` (1200×630), logo `assets/logo.png` (600×600), `favicon.svg` ve `assets/apple-touch-icon.png` eklendi.
- Galeri sayfasında H1 artık "Tüm Galerimiz" başlığıdır; hero başlığı H2'ye çevrildi (görünüm değişmedi). Ana sayfa hero üst etiketi "ZONGULDAK EVDEN EVE NAKLİYAT" oldu.
- Yayından sonra: Google Search Console ve Bing Webmaster Tools'a `sitemap.xml` gönderin, Google İşletme Profili açın/doğrulayın ve web sitesi alanına bu alan adını yazın.

## Arka plan deseni

Tüm sayfalarda hero'nun altından footer'a kadar silik, altın çizgili taşınma ikonlarından oluşan bir desen vardır (koli, kamyon, ev, kanepe, taşıma arabası, bant, anahtar, gardırop, "bu taraf yukarı" okları, konum işareti vb.). Desen `assets/moving-pattern.svg` dosyasındadır, kesintisiz tekrarlanır ve `python tools/make_pattern.py` ile yeniden üretilir. Stiller `backdrop.css` dosyasındadır; görünürlük `--backdrop-strength` değişkeniyle ayarlanır (masaüstü .13, telefon .11). Desenin görünmesi için bölümlerin düz siyah zeminleri `backdrop.css` içinde şeffaf yapılmıştır; kartlar ve dekoratif ışımalar korunmuştur. Yeni bir bölüm eklerken düz siyah zemin vermeyin.

Hero ile altındaki alan arasındaki geçiş yumuşaktır: hero görselinin alt kısmı sayfa zeminine erir (`.hero-slide:after`), desen ve sıcak ışıma hero bittikten sonra 150 piksel boyunca yavaşça belirir. Hero'nun bittiği nokta `script.js` tarafından ölçülüp `--hero-end` değişkenine yazılır; JavaScript yoksa desen hero'nun arkasında kalır. İlçe sayfalarındaki üst altın çizgi ve köşe ışıması bu geçiş için kaldırıldı.

## Ücretsiz keşif — duyarlı referans tasarımı

Ana sayfadaki `#ucretsiz-kesif`, masaüstünde metin/avantajlar, keşif fotoğrafı ve iletişim düğmelerinden oluşur. 900 piksel ve altında içerik dikey sıralanır; fotoğraf düğmelerin altına geçer. Tasarım `discovery.css` içinde diğer sayfalardaki keşif alanlarından bağımsızdır.

Fotoğraf, kullanıcı tarafından verilen masaüstü/mobil kaynaklarından SVG görüntü alanlarıyla gösterilir; kaynak PNG dosyaları değiştirilmemiştir. Ev ve avantaj ikonları eşit ölçülü, ortalanmış SVG vektörlerdir. Teklif düğmesi hover ve klavye odağında altın dolguya geçer; çerçeve dışındaki dekoratif çizgiler ve parlamalar kaldırılmıştır. Başlıklar, açıklamalar, avantaj metinleri ve düğmeler gerçek HTML'dir. Montserrat ve Roboto Condensed fontları lisanslarıyla birlikte yerel olarak saklanır. Telefon, WhatsApp ve mevcut teklif formu bağlantıları korunur.

Yerel çalıştırma: depo klasöründe `python -m http.server 4173 --bind 127.0.0.1`, ardından `http://127.0.0.1:4173/#ucretsiz-kesif`.

## Favicon

Sekme simgesi logodaki altın çatı, yol kıvrımı ve beyaz nakliye kamyonundan oluşan sade bir vektör işarettir. Küçük boyutta okunamayan marka yazıları simgeye dahil edilmez; ana logo değiştirilmemiştir.

Kaynak `favicon.svg`; uyumluluk dosyaları 16/32/48 piksel PNG, üç boyutu içeren `favicon.ico` ve 180×180 `assets/apple-touch-icon.png` dosyasıdır. Raster sürümler SVG'den doğrudan ilgili boyuta çizilmiştir. Tüm HTML sayfaları ve `tools/build_districts.py` aynı sürümlü bağlantıları içerir.
