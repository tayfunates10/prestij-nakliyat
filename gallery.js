(() => {
  const gallery = document.querySelector('.gallery');
  const dialog = gallery.querySelector('.gallery-dialog');
  const photos = [...gallery.querySelectorAll('.gallery-photo-button img')];
  const image = dialog.querySelector('.gallery-viewer-image>img');
  const counter = dialog.querySelector('.gallery-counter');
  let current = 0;
  function show(index) {
    current = (index + photos.length) % photos.length;
    image.src = photos[current].getAttribute('src');
    image.alt = photos[current].alt;
    counter.textContent = `${current + 1} / ${photos.length}`;
  }
  gallery.querySelector('.gallery-grid').addEventListener('click', event => {
    const button = event.target.closest('[data-photo]');
    if (!button) return;
    show(Number(button.dataset.photo));
    dialog.showModal();
  });
  dialog.querySelector('.gallery-close').addEventListener('click', () => dialog.close());
  dialog.querySelector('.gallery-previous').addEventListener('click', () => show(current - 1));
  dialog.querySelector('.gallery-next').addEventListener('click', () => show(current + 1));
  dialog.addEventListener('keydown', event => {
    if (event.key === 'ArrowLeft' || event.key === 'ArrowRight') {
      event.preventDefault();
      show(current + (event.key === 'ArrowRight' ? 1 : -1));
    }
  });
  dialog.addEventListener('click', event => {
    if (event.target !== dialog) return;
    const rect = dialog.getBoundingClientRect();
    if (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom) dialog.close();
  });
})();
