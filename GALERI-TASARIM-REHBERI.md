# Galeri görseli ve alt bant uygulama rehberi

Bu dosya, farklı yapay zekâ araçlarının yeni fotoğraflara aynı tasarımı uygulayabilmesi için hazırlanmıştır.

## Sitede kullanılan yöntem (öncelikli)

Orijinal fotoğraflar değiştirilmez. Kart `figure.gallery-card`, fotoğraf `button.gallery-photo-button > img`, görselin içinde görünen alt bant ise aynı figure içindeki `figcaption.gallery-band` bileşenidir. Bant `position:absolute; bottom:0` ile fotoğrafın altına oturur. Böylece logo ve telefon her çözünürlükte net kalır, telefon bağlantısı kullanılabilir ve bilgi tek yerden değiştirilebilir.

1. Yeni orijinal fotoğrafı `assets/gallery/` içine açıklayıcı bir dosya adıyla koy. Fotoğraftaki mevcut filigranları kaldırma.
2. `index.html` içindeki son `gallery-card` bileşenini kopyala. `img src`, gerçek width/height, Türkçe alt açıklaması, düğme aria-label ve sıralı `data-photo` numarasını güncelle.
3. Bantta mevcut logo SVG görüntü alanını aynen kullan: viewBox="55 447 433 108", kaynak `assets/header-reference.png`, kaynak boyutu 1672 × 941. Logoyu yeniden çizme veya yapay zekâ ile tekrar üretme.
4. Telefon: `0532 123 45 67`, bağlantı: `tel:+905321234567`. Bu, mevcut sitedeki örnek numaradır; kullanıcı gerçek numarayı verdiğinde tüm siteyle birlikte değiştir.
5. Konum: `Merkez / Zonguldak`.
6. `refinements.css` içindeki `.gallery-card`, `.gallery-photo-button`, `.gallery-band`, `.gallery-band-logo`, `.gallery-location` kurallarını kullan. Yeni karta ayrı renk, yazı tipi veya rastgele bant yüksekliği ekleme.
7. `.gallery-enlarge` ve önceki/sonraki düğmelerinde aynı dolu SVG okunu kullan: viewBox="0 0 24 24", path="M3 9h10V4l9 8-9 8v-5H3Z". Emoji veya font karakteri kullanma.
8. Galeri JavaScript’i görselleri DOM’dan okur; yeni kart için ayrı olay dinleyicisi yazma. Fotoğrafı büyütme, önceki/sonraki, Escape, klavye odağı ve 320/390/768/1440 ekran ölçülerini kontrol et.

## Başka bir görsel aracına verilecek açıklama

“Ekli taşıma fotoğrafını ve orijinal Prestij Nakliyat logosunu kullan. Fotoğrafın en altına, fotoğrafın içinde kalan siyah/füme bir marka bandı yerleştir. Üst sınırına ince, düz altın çizgi ekle. Bandın üst satırında orijinal logo, altında okunaklı ‘0532 123 45 67’, son satırda konum simgesi ve ‘Merkez / Zonguldak’ yazsın. Palet: #070907, #16150d, #d1ac56, #ffe5a0. Metinler ve logo kusursuz netlikte, hizalı, gölgesiz ve gürültüsüz olsun. Logoyu veya harfleri yeniden yorumlama. Bandın fotoğraftaki ana konuyu kapatmasını önle. Telefonu veya konumu uydurma. Fotoğrafın içeriğini ve filigranlarını koru. Çıktı sRGB, yüksek çözünürlüklü PNG olsun.”

Siteye eklerken bantlı çıktıyı tekrar HTML bantla üst üste kullanma. Web sitesi için yukarıdaki bağımsız HTML/SVG katman yöntemi tercih edilir. Sosyal medya için tek parça çıktı istenirse aynı bileşeni tarayıcıda oluşturup kartı dışa aktar; bu, logonun ve metnin üretilmiş görüntüye göre daha güvenilir ve net kalmasını sağlar.
