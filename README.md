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
