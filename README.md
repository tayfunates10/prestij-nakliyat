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
- SSS “Daha Fazlası” bağlantısı `sss.html` sayfasına gider. Sayfa mevcut sorularla çalışır; ileride ek sorularla genişletilebilir.
- Galeri alt bantları fotoğraf alanının içindedir. Tekrarlanabilir tasarım ve başka görsel araçları için talimatlar `GALERI-TASARIM-REHBERI.md` içindedir.
- Footer sloganı `assets/footer-signature.svg` içinde yeniden oluşturulmuştur; düşük çözünürlüklü raster kırpımı kullanılmaz.
