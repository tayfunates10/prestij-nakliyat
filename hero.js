(() => {
  const hero = document.querySelector('.hero');
  const slides = [...hero.querySelectorAll('.hero-slide')];
  const dots = [...hero.querySelectorAll('.hero-dot')];
  const pauseButton = hero.querySelector('.hero-pause');
  const motionPreference = window.matchMedia('(prefers-reduced-motion: reduce)');
  const interval = 7000;
  let current = 0;
  let timer;
  let paused = motionPreference.matches;
  let hovered = false;
  let focused = false;

  function schedule() {
    clearTimeout(timer);
    if (!paused && !hovered && !focused && !document.hidden) {
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
      dots[i].classList.toggle('is-selected', active);
      dots[i].setAttribute('aria-pressed', String(active));
    });
    schedule();
  }

  function renderPause() {
    pauseButton.setAttribute('aria-pressed', String(paused));
    pauseButton.setAttribute('aria-label', paused ? 'Otomatik geçişi başlat' : 'Otomatik geçişi duraklat');
    pauseButton.firstElementChild.textContent = paused ? '▶' : 'Ⅱ';
    schedule();
  }

  dots.forEach((dot, i) => dot.addEventListener('click', () => show(i)));
  hero.querySelectorAll('[data-step]').forEach(button => {
    button.addEventListener('click', () => show(current + Number(button.dataset.step)));
  });
  pauseButton.addEventListener('click', () => {
    paused = !paused;
    renderPause();
  });
  hero.addEventListener('pointerenter', event => {
    if (event.pointerType === 'mouse') { hovered = true; schedule(); }
  });
  hero.addEventListener('pointerleave', () => { hovered = false; schedule(); });
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
    renderPause();
  });
  renderPause();
})();
