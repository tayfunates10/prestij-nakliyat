(() => {
  const hero = document.querySelector('.hero');
  const slides = [...hero.querySelectorAll('.hero-slide')];
  const pauseButton = hero.querySelector('.hero-pause');
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
    schedule();
  }

  function renderPause() {
    pauseButton.setAttribute('aria-pressed', String(paused));
    pauseButton.setAttribute('aria-label', paused ? 'Otomatik geçişi başlat' : 'Otomatik geçişi duraklat');
    pauseButton.firstElementChild.textContent = paused ? '▶' : 'Ⅱ';
    schedule();
  }

  hero.querySelectorAll('[data-step]').forEach(button => {
    button.addEventListener('click', () => show(current + Number(button.dataset.step)));
  });
  pauseButton.addEventListener('click', () => {
    paused = !paused;
    renderPause();
  });
  hero.addEventListener('focusin', () => { focused = true; schedule(); });
  hero.addEventListener('focusout', () => {
    queueMicrotask(() => { focused = hero.contains(document.activeElement); schedule(); });
  });
  hero.querySelector('.hero-controls').addEventListener('keydown', event => {
    if (event.key === 'ArrowRight' || event.key === 'ArrowLeft') {
      event.preventDefault();
      show(current + (event.key === 'ArrowRight' ? 1 : -1));

    }
  });
  document.addEventListener('visibilitychange', schedule);
  motionPreference.addEventListener('change', event => {
    paused = event.matches;
    renderPause();
  });
  if (document.readyState === 'complete') renderPause();
  else window.addEventListener('load', renderPause, { once: true });
})();
