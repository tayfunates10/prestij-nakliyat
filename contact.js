(() => {
  const form = document.querySelector('.quote-form');
  const result = form.querySelector('.quote-result');
  const status = result.querySelector('[role="status"]');
  const continueLink = result.querySelector('a');
  const phone = form.elements.phone;
  form.addEventListener('input', event => {
    if (typeof event.target.setCustomValidity === 'function') event.target.setCustomValidity('');
    result.hidden = true;
    continueLink.removeAttribute('href');
  });
  form.addEventListener('submit', event => {
    event.preventDefault();
    for (const field of ['fullName', 'origin', 'destination']) {
      const input = form.elements[field];
      input.setCustomValidity(input.value.trim() ? '' : 'Lütfen bu alanı doldurun.');
    }
    const digits = phone.value.replace(/\D/g, '');
    const national = digits.startsWith('90') && digits.length === 12 ? digits.slice(2) : digits.startsWith('0') && digits.length === 11 ? digits.slice(1) : digits;
    phone.setCustomValidity(/^[2-5]\d{9}$/.test(national) ? '' : 'Lütfen geçerli bir Türkiye telefon numarası girin. Örnek: 0532 123 45 67');
    if (!form.reportValidity()) return;
    const message = [
      'Merhaba, Prestij Nakliyat için fiyat teklifi almak istiyorum.',
      '',
      `Ad Soyad: ${form.elements.fullName.value.trim()}`,
      `Telefon: +90${national}`,
      `Taşınacak Adres (Nereden): ${form.elements.origin.value.trim()}`,
      `Yeni Adres (Nereye): ${form.elements.destination.value.trim()}`,
      ...(form.elements.notes.value.trim() ? [`Notlar: ${form.elements.notes.value.trim()}`] : [])
    ].join('\n');
    const url = `https://wa.me/905321234567?text=${encodeURIComponent(message)}`;
    continueLink.href = url;
    status.textContent = 'Talebiniz hazır. Gönderimi WhatsApp’ta tamamlayın. Pencere açılmadıysa aşağıdaki bağlantıyı kullanabilirsiniz.';
    result.hidden = false;
    window.open(url, '_blank', 'noopener,noreferrer');
  });
  document.querySelectorAll('.faq-list details').forEach(item => {
    item.addEventListener('toggle', () => {
      if (!item.open) return;
      document.querySelectorAll('.faq-list details').forEach(other => { if (other !== item) other.open = false; });
    });
  });
  document.querySelectorAll('.hero-actions .hero-button--gold').forEach(link => link.setAttribute('href', '#teklif-al'));
  form.querySelector('.quote-submit').disabled = false;
})();
