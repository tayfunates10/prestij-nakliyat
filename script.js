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
