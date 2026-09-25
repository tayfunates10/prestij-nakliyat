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

