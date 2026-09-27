(() => {
  if (document.body.dataset.page === 'gallery') {
    // The gallery page always opens at the top, even after a reload.
    if ('scrollRestoration' in history) history.scrollRestoration = 'manual';
    if (!location.hash) window.scrollTo(0, 0);
  }
  const gallery = document.querySelector('.gallery');
  const dialog = gallery.querySelector('.gallery-dialog');
  const photos = [...gallery.querySelectorAll('.gallery-photo-button img')];
  const image = dialog.querySelector('.gallery-viewer-photo>img');
  const counter = dialog.querySelector('.gallery-counter');
  const caption = dialog.querySelector('.gallery-caption');
  const stage = dialog.querySelector('.gallery-viewer-image');
  const thumbList = dialog.querySelector('.gallery-thumbs');
  const pad = n => String(n).padStart(2, '0');
  const thumbs = photos.map((photo, i) => {
    const thumb = document.createElement('button');
    thumb.className = 'gallery-thumb';
    thumb.type = 'button';
    thumb.setAttribute('aria-label', `${i + 1}. fotoğraf`);
    thumb.innerHTML = `<img src="${photo.getAttribute('src')}" alt="" loading="lazy">`;
    thumb.addEventListener('click', () => show(i));
    thumbList.append(thumb);
    return thumb;
  });
  let current = 0;
  function show(index) {
    current = (index + photos.length) % photos.length;
    const src = photos[current].getAttribute('src');
    image.src = src;
    image.alt = photos[current].alt;
    caption.textContent = photos[current].alt.split(';')[0];
    stage.style.setProperty('--gallery-photo', `url("${src}")`);
    counter.innerHTML = `<strong>${pad(current + 1)}</strong> / ${pad(photos.length)}`;
    thumbs.forEach((thumb, i) => {
      if (i === current) thumb.setAttribute('aria-current', 'true');
      else thumb.removeAttribute('aria-current');
    });
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
