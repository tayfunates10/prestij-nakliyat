# Prestij Nakliyat

İlk bölüm: referans görsele göre siyah ve altın tonlarında duyarlı üst menü.

`index.html` dosyası statik bir sunucuyla veya doğrudan tarayıcıda açılabilir. Derleme gerektirmez.

## Kapsam

- Logo, kullanıcının referans görselinden SVG görüntü alanıyla gösterilir; orijinal kaynak değiştirilmemiştir. Ayrı şeffaf logo sağlanırsa bu kaynakla değiştirilebilir.
- Masaüstü menü, mobil açılır menü, telefon bağlantısı, altın ışık ve parlama efektleri.
- Animasyonlar sabit görsele göre yorumlanmıştır; birebir hareket eşleşmesi için video gerekir.
- Görseldeki tarayıcı adres çubuğu siteye dahil değildir.
- Telefon numarası referanstaki haliyle kullanılmıştır; yayına çıkmadan önce işletmenin numarasıyla doğrulanmalıdır.
- Menü bağlantıları sonraki bölümlerin kimliklerine hazırdır: `hakkimizda`, `hizmetlerimiz`, `tasinma-sureci`, `sss`, `galeri`, `iletisim`. Bu bölümlerin içeriği henüz verilmediğinden eklenmemiştir.
- Yazı tipi: Google Fonts üzerinden Roboto Condensed; bağlantı yoksa Arial Narrow / Arial.
- Hareket azaltma tercihi desteklenir.

Sonraki bölümler `#site-content` içine eklenir.

## Hero — ikinci bölüm

İki hero slaytı `hero.css` ve `hero.js` ile eklendi. Slaytlar 7 saniyede bir 1 saniyelik yumuşak geçiş yapar. Önceki/sonraki, doğrudan slayt seçimi ve duraklatma kontrolleri vardır. Fareyle üzerinde durunca, klavye odağı hero içindeyken ve sekme gizlendiğinde otomatik geçiş bekler. Hareket azaltma tercihi açıkken otomatik geçiş başlangıçta kapalıdır. Etkin olmayan slayt klavye ve ekran okuyucudan gizlenir.

Hero görsellerinde kullanıcının beyaz Fiat Ducato kamyoneti ve kasaya perspektifli Prestij kaplaması kullanıldı. Üretim yöntemi ve tam istemler `assets/hero-generation.md` içinde kayıtlıdır. Görselden bağımsız HTML başlıklar ve bağlantılar kullanılır. Teklif düğmeleri telefon aramasına; WhatsApp düğmeleri sohbet ekranına gider. Her iki bağlantı da ilk referanstaki örnek telefon numarasını kullanır.

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

Kullanıcının isteğiyle yalnızca Instagram ikonu gösterilir ve `https://instagram.com` adresine bağlanır; kullanıcı hesap adresini daha sonra değiştirecektir. Galeri bölümü henüz oluşturulmadığından footer'daki Galeri metni bağlantı değildir. El yazısı `assets/coverage-reference.png` içindeki footer görselinden alınır.
