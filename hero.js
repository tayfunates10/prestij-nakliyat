(() => {
  const hero = document.querySelector('.hero');
  const slides = [...hero.querySelectorAll('.hero-slide')];
  const dots = [...hero.querySelectorAll('.hero-dot')];
  const motionPreference = window.matchMedia('(prefers-reduced-motion: reduce)');
  const interval = 7000;
  let current = 0;
  let timer;
  let paused = motionPreference.matches;

  let focused = false;

  function schedule() {
    clearTimeout(timer);
    if (!paused && !focused && !document.hidden) {
      timer = setTimeout(() => show(current + 1), interval);
    }
  }

  function show(index) {
    current = (index + slides.length) % slides.length;
    slides.forEach((slide, i) => {
      const active = i === current;
      slide.classList.toggle('is-current', active);
      slide.setAttribute('aria-hidden', String(!active));
      slide.inert = !active;
    });
    dots.forEach((dot, i) => {
      const active = i === current;
      dot.classList.toggle('is-selected', active);
      if (active) dot.setAttribute('aria-current', 'true');
      else dot.removeAttribute('aria-current');
    });
    schedule();
  }

  dots.forEach(dot => {
    dot.addEventListener('click', () => show(Number(dot.dataset.slide)));
  });
  // Dokunmatik ekranda parmakla sola kaydırma sonraki, sağa kaydırma önceki slayta geçer.
  // Yalnızca belirgin yatay hareket sayılır; dikey sayfa kaydırması etkilenmez (dinleyiciler pasif).
  const slideArea = hero.querySelector('.hero-slides');
  let touchX = null;
  let touchY = 0;
  slideArea.addEventListener('touchstart', event => {
    if (event.touches.length !== 1) { touchX = null; return; }
    touchX = event.touches[0].clientX;
    touchY = event.touches[0].clientY;
  }, { passive: true });
  slideArea.addEventListener('touchend', event => {
    if (touchX === null) return;
    const dx = event.changedTouches[0].clientX - touchX;
    const dy = event.changedTouches[0].clientY - touchY;
    touchX = null;
    if (Math.abs(dx) > 45 && Math.abs(dx) > Math.abs(dy) * 1.5) show(current + (dx < 0 ? 1 : -1));
  }, { passive: true });
  slideArea.addEventListener('touchcancel', () => { touchX = null; }, { passive: true });

  hero.addEventListener('focusin', () => { focused = true; schedule(); });
  hero.addEventListener('focusout', () => {
    queueMicrotask(() => { focused = hero.contains(document.activeElement); schedule(); });
  });
  hero.querySelector('.hero-controls').addEventListener('keydown', event => {
    if (event.key === 'ArrowRight' || event.key === 'ArrowLeft') {
      event.preventDefault();
      show(current + (event.key === 'ArrowRight' ? 1 : -1));
      dots[current].focus();
    }
  });
  document.addEventListener('visibilitychange', schedule);
  motionPreference.addEventListener('change', event => {
    paused = event.matches;
    schedule();
  });
  if (document.readyState === 'complete') schedule();
  else window.addEventListener('load', schedule, { once: true });
})();
