// Kaydırınca içerik giriş animasyonu. Görünüm (masaüstü / mobil) reveal.css'teki medya sorgularıyla belirlenir;
// bu dosya öğeleri işaretler ve görünür olduklarında .is-revealed ekler.
// JS yoksa veya "hareketi azalt" açıksa hiçbir şey gizlenmez.
(() => {
  if (!('IntersectionObserver' in window) || matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const mobile = matchMedia('(max-width: 900px)').matches;
  const maxStagger = 5;
  const found = [];
  const mark = (el, type, index) => {
    el.dataset.reveal = type;
    el.style.setProperty('--reveal-i', Math.min(index, maxStagger));
    found.push(el);
  };
  const skip = el => el.closest('.hero, dialog') || el.hasAttribute('data-reveal');

  // 1) Bütün olarak gelen bloklar: [seçici, tür]. Aynı ebeveyn altındaki eşleşmeler kademeli gelir.
  const blocks = [
    ['.service-card, .trust-item, .process-step, .district-card, .about-features > li', 'card'],
    ['.about-photo-wrap', 'from-start'],
    ['.coverage-map-panel', 'from-end'],
    ['.gallery-card', 'photo'],
    ['.gallery-more', 'rise'],
  ];
  blocks.forEach(([selector, type]) => {
    document.querySelectorAll(selector).forEach(el => {
      if (skip(el)) return;
      mark(el, type, [...el.parentElement.children].filter(child => child.matches(selector)).indexOf(el));
    });
  });

  // 2) Metin grupları parçalarına ayrılır: üst etiket, başlık, açıklama… her biri ayrı yönden ve sırayla gelir.
  //    Masaüstü: sol → sağ → alt döngüsü. Mobil: sol ↔ sağ.
  //    İç içe grup olan veya içinde zaten animasyonlu öğe bulunan çocuklar atlanır (kendi başlarına işlenir).
  const textGroups = '.services-heading, .trust-heading, .process-heading, .gallery-heading, .about-copy, .about-cta, .about-cta-copy, .coverage-copy, .contact-column, .district-intro, .district-faq, .district-others';
  const sides = mobile ? ['start', 'end'] : ['start', 'end', 'up'];
  document.querySelectorAll(textGroups).forEach(group => {
    if (group.closest('.hero, dialog')) return;
    [...group.children]
      .filter(child => !skip(child) && !child.matches(textGroups) && !child.querySelector('[data-reveal]') && child.getClientRects().length)
      .forEach((child, i) => {
        child.dataset.revealSide = sides[i % sides.length];
        mark(child, 'part', i);
      });
  });
  if (!found.length) return;

  // Mobil: bloklar da soldan ya da sağdan gelir. Yan yana duranlar bulundukları taraftan,
  // tam genişlikteki (alt alta) bloklar sayfa sırasına göre dönüşümlü olarak gelir.
  if (mobile) {
    const vw = document.documentElement.clientWidth;
    let alternate = 0;
    found.filter(el => !el.dataset.revealSide)
      .sort((a, b) => a.compareDocumentPosition(b) & Node.DOCUMENT_POSITION_FOLLOWING ? -1 : 1)
      .forEach(el => {
        const box = el.getBoundingClientRect();
        el.dataset.revealSide = box.width < vw * .6 ? (box.left + box.width / 2 < vw / 2 ? 'start' : 'end') : (alternate++ % 2 ? 'end' : 'start');
      });
  }

  // Animasyon bitince işaretler kaldırılır; kartların kendi hover geçişleri geri gelir.
  const finish = el => {
    el.removeAttribute('data-reveal');
    el.removeAttribute('data-reveal-side');
    el.classList.remove('is-revealed');
    el.style.removeProperty('--reveal-i');
  };
  const reveal = el => {
    observer.unobserve(el);
    el.classList.add('is-revealed');
    const { transitionDuration, transitionDelay } = getComputedStyle(el);
    const total = (parseFloat(transitionDuration) + parseFloat(transitionDelay)) * 1000;
    setTimeout(() => finish(el), total + 100);
  };
  // Tetikleme çizgisi (tüm sayfalar, iki görünüm): ekran 4 satıra bölündüğünde alttan 1. satırın üst çizgisi (üstten %75).
  const observer = new IntersectionObserver(entries => entries.forEach(entry => {
    if (entry.isIntersecting) reveal(entry.target);
  }), { rootMargin: '0px 0px -25% 0px' });

  // Sayfanın sonundaki öğeler tetikleme çizgisine hiç ulaşamayabilir: sona gelince kalanlar da gelir.
  const revealAtEnd = () => {
    if (innerHeight + scrollY < document.documentElement.scrollHeight - 4) return;
    found.forEach(el => { if (el.dataset.reveal && !el.classList.contains('is-revealed')) reveal(el); });
  };
  addEventListener('scroll', revealAtEnd, { passive: true });

  document.documentElement.classList.add('reveal-ready');
  found.forEach(el => observer.observe(el));
})();
