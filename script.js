const toggle = document.querySelector('.menu-toggle');
const menu = document.querySelector('#primary-menu');

function closeMenu() {
  toggle.setAttribute('aria-expanded', 'false');
  toggle.setAttribute('aria-label', 'Menüyü aç');
  menu.classList.remove('is-open');
}

toggle.addEventListener('click', () => {
  const open = toggle.getAttribute('aria-expanded') !== 'true';
  toggle.setAttribute('aria-expanded', String(open));
  toggle.setAttribute('aria-label', open ? 'Menüyü kapat' : 'Menüyü aç');
  menu.classList.toggle('is-open', open);
});

document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
    closeMenu();
    toggle.focus();
  }
});

menu.addEventListener('click', event => {
  if (event.target.closest('a')) closeMenu();
});

window.matchMedia('(min-width: 1241px)').addEventListener('change', event => {
  if (event.matches) closeMenu();
});

const header = document.querySelector('.site-header');

new ResizeObserver(() => {
  if (!menu.classList.contains('is-open')) {
    document.documentElement.style.setProperty('--header-height', `${header.offsetHeight}px`);
  }
}).observe(header);

// Header menüsü: sayfada hangi bölümdeyse onun linki altı çizili (.is-active). Yalnızca aynı sayfadaki (#...) bölümler.
// Header'ın altından ekranın ~%30'una kadarki çizgiyi geçen son bölüm seçilir; aynı satırdaki bölümlerde (masaüstünde
// SSS / İletişim yan yana) menüde önce geleni, sayfa sonunda son link seçilir. Menüde olmayan bölümlerde öncekinin linki kalır.
const spyLinks = [...menu.querySelectorAll('.nav-link[href^="#"]')]
  .map(link => ({ link, target: document.getElementById(link.getAttribute('href').slice(1)) }))
  .filter(item => item.target);
if (spyLinks.length > 1) {
  let spyFrame = 0;
  let clicked = null;   // aynı satırdaki bölümlerde (ör. İletişim'e tıklanınca) tıklanan link tercih edilir
  spyLinks.forEach(item => item.link.addEventListener('click', () => { clicked = item; }));
  const updateActiveLink = () => {
    spyFrame = 0;
    const line = header.offsetHeight + innerHeight * 0.3;
    const atBottom = innerHeight + scrollY >= document.documentElement.scrollHeight - 4;
    let active = spyLinks[0];
    let activeTop = -Infinity;
    spyLinks.forEach(item => {
      const top = item.target === document.body ? -Infinity : item.target.getBoundingClientRect().top;
      if (top <= line && (top > activeTop || (top === activeTop && item === clicked))) { active = item; activeTop = top; }
    });
    if (atBottom) active = spyLinks[spyLinks.length - 1];
    spyLinks.forEach(item => {
      item.link.classList.toggle('is-active', item === active);
      if (item === active) item.link.setAttribute('aria-current', 'location');
      else item.link.removeAttribute('aria-current');
    });
  };
  const scheduleActiveLink = () => { if (!spyFrame) spyFrame = requestAnimationFrame(updateActiveLink); };
  addEventListener('scroll', scheduleActiveLink, { passive: true });
  addEventListener('resize', scheduleActiveLink);
  updateActiveLink();
}

// Arka plan deseni hero bittikten sonra başlar (backdrop.css --hero-end).
const pageHero = document.querySelector('.hero');
const pageContent = document.querySelector('#site-content');

if (pageHero && pageContent) {
  new ResizeObserver(() => {
    pageContent.style.setProperty('--hero-end', `${pageHero.offsetTop + pageHero.offsetHeight}px`);
  }).observe(pageHero);
}

// Mobile quick actions: attention animations on a random button at random short intervals.
const quickActions = [...document.querySelectorAll('.mobile-action')];
const attentionEffects = ['is-pulse', 'is-shake', 'is-pop'];
const calmMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

function nudgeQuickAction() {
  if (!document.hidden && !calmMotion.matches && quickActions[0]?.offsetParent) {
    const action = quickActions[Math.floor(Math.random() * quickActions.length)];
    const effect = attentionEffects[Math.floor(Math.random() * attentionEffects.length)];
    action.classList.remove(...attentionEffects);
    void action.offsetWidth;
    action.classList.add(effect);
    action.addEventListener('animationend', () => action.classList.remove(...attentionEffects), { once: true });
  }
  setTimeout(nudgeQuickAction, 500 + Math.random() * 1300);
}

if (quickActions.length) setTimeout(nudgeQuickAction, 1200);

// Header logosu: tıklama/dokunmada seçim efekti (styles.css .is-tapped). Art arda basışlarda efekt baştan oynar.
const brandLink = document.querySelector('.site-header .brand');
if (brandLink) {
  let brandTimer;
  brandLink.addEventListener('click', () => {
    brandLink.classList.remove('is-tapped');
    void brandLink.offsetWidth;
    brandLink.classList.add('is-tapped');
    clearTimeout(brandTimer);
    brandTimer = setTimeout(() => brandLink.classList.remove('is-tapped'), 900);
  });
}
