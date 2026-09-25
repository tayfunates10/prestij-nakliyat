(() => {
  const dialog = document.querySelector('.service-dialog');
  const title = dialog.querySelector('#service-dialog-title');
  const description = dialog.querySelector('#service-dialog-description');
  const services = {
    home: ['Evden Eve Nakliyat', 'Eşyalarınız profesyonel ekibimizle güvenle yeni yuvanıza taşınır. Ev taşıma sürecinizi planlamak ve ihtiyaçlarınıza uygun hizmeti görüşmek için bizimle iletişime geçebilirsiniz.'],
    office: ['Ofis Taşımacılığı', 'İşinizi aksatmadan, hızlı ve planlı ofis taşıma hizmetleri. Ofisinizin eşya ve mobilya bilgilerini, yeni adresini ve tercih ettiğiniz taşıma tarihini birlikte değerlendirelim.'],
    furniture: ['Mobilya Montajı', 'Tüm mobilyalarınız uzman ekibimizce sökülür, taşınır ve montajı yapılır. Söküm ve kurulum ihtiyaçlarınızı görüşmek için mobilya türünü ve ölçülerini paylaşabilirsiniz.'],
    packing: ['Paketleme Hizmeti', 'Eşyalarınız özel ambalaj malzemeleri ile güvenle paketlenir. Paketlenmesini istediğiniz eşyaları ve hassas parçaları belirterek hizmet hakkında bilgi alabilirsiniz.'],
    lift: ['Asansörlü Taşıma', 'Yüksek katlarda bile hızlı, güvenli ve pratik taşıma çözümleri. Asansörlü taşımanın adresinize uygunluğunu değerlendirmek için kat ve bina çevresi bilgilerini paylaşabilirsiniz.']
  };
  document.querySelector('.service-grid').addEventListener('click', event => {
    const button = event.target.closest('[data-service]');
    if (!button) return;
    const service = services[button.dataset.service];
    if (!service) return;
    [title.textContent, description.textContent] = service;
    dialog.showModal();
  });
  dialog.querySelector('.dialog-close').addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', event => {
    if (event.target !== dialog) return;
    const bounds = dialog.getBoundingClientRect();
    if (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom) dialog.close();
  });
})();
