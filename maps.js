(() => {
  const configs = [{id:'coverage-map',zoom:9},{id:'contact-map',zoom:13}];
  const center = [41.4535,31.7894]; // City centre, not a verified business address.
  const observer = new IntersectionObserver(entries => entries.forEach(entry => {
    if (!entry.isIntersecting) return;
    observer.unobserve(entry.target);
    const element = entry.target;
    if (!window.L) { element.innerHTML='<a class="map-fallback" href="https://www.openstreetmap.org/#map=13/41.4535/31.7894">Zonguldak haritasını aç</a>'; return; }
    const map=L.map(element,{scrollWheelZoom:false,zoomControl:true}).setView(center,Number(element.dataset.zoom));
    map.zoomControl.setPosition('topleft');
    const layer=L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png',{maxZoom:19,attribution:'© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'}).addTo(map);
    const marker=L.divIcon({className:'gold-map-pin',html:'<span></span>',iconSize:[24,30],iconAnchor:[12,27]});
    L.marker(center,{icon:marker,alt:'Zonguldak Merkez — hizmet bölgesi'}).addTo(map).bindPopup('Zonguldak Merkez<br>Prestij Nakliyat hizmet bölgesi');
    const zoomIn=element.querySelector('.leaflet-control-zoom-in'),zoomOut=element.querySelector('.leaflet-control-zoom-out');
    zoomIn.title='Yakınlaştır';zoomIn.setAttribute('aria-label','Yakınlaştır');zoomOut.title='Uzaklaştır';zoomOut.setAttribute('aria-label','Uzaklaştır');
    new ResizeObserver(()=>map.invalidateSize()).observe(element);
    let notice;
    layer.on('tileerror',()=>{if(notice)return;notice=document.createElement('p');notice.className='map-note';notice.textContent='Harita yüklenemedi. Konumu harita bağlantısından açabilirsiniz.';element.after(notice);});
    layer.on('tileload',()=>{if(notice){notice.remove();notice=null;}});
  }),{rootMargin:'0px'});
  configs.forEach(({id,zoom})=>{const el=document.getElementById(id);if(el){el.dataset.zoom=zoom;observer.observe(el);}});
})();
