(() => {
  const configs = [{id:'coverage-map',zoom:9,districts:true},{id:'contact-map',zoom:13}];
  const center = [41.4835594,31.8302742]; // Business pin from https://maps.app.goo.gl/j5zPko2Xv3FaQikd8
  // Approximate district centres; label direction keeps neighbouring names apart.
  const districts = [
    ['Zonguldak Merkez',41.4535,31.7894,'top'],
    ['Kilimli',41.4900,31.8350,'right'],
    ['Kozlu',41.4330,31.7430,'bottom'],
    ['Ereğli',41.2820,31.4190,'right'],
    ['Alaplı',41.1800,31.3880,'right'],
    ['Çaycuma',41.4260,32.0760,'right'],
    ['Devrek',41.2190,31.9560,'right'],
    ['Gökçebey',41.3060,32.1400,'right'],
  ];
  // Leaflet (~150 KB) ilk harita ekrana yaklaşınca yüklenir. CSS'i site.css'in önüne eklenir: haritayı özelleştiren
  // kurallarımız (refinements.css) eskisi gibi baskın kalır.
  const version = (document.querySelector('script[src*="maps.js"]')?.src.match(/\?v=[\w-]+/) || [''])[0];
  let leaflet;
  const loadLeaflet = () => leaflet || (leaflet = new Promise(resolve => {
    const css = document.createElement('link');
    css.rel = 'stylesheet';
    css.href = `assets/vendor/leaflet/leaflet.css${version}`;
    document.head.insertBefore(css, document.querySelector('link[href*="site.css"]'));
    const js = document.createElement('script');
    js.src = `assets/vendor/leaflet/leaflet.js${version}`;
    js.onload = js.onerror = () => resolve(window.L);
    document.head.append(js);
  }));
  const observer = new IntersectionObserver(entries => entries.forEach(async entry => {
    if (!entry.isIntersecting) return;
    observer.unobserve(entry.target);
    const element = entry.target;
    if (!await loadLeaflet()) { element.innerHTML=`<a class="map-fallback" href="https://www.openstreetmap.org/?mlat=${center[0]}&mlon=${center[1]}#map=14/${center[0]}/${center[1]}">Kilimli haritasını aç</a>`; return; }
    const map=L.map(element,{scrollWheelZoom:true,zoomControl:true,zoomSnap:element.dataset.districts?0.25:1});
    if (!element.dataset.districts) map.setView(center,Number(element.dataset.zoom));
    map.zoomControl.setPosition('topleft');
    const layer=L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png',{maxZoom:19,attribution:'© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'}).addTo(map);
    const marker=L.divIcon({className:'gold-map-pin',html:'<span></span>',iconSize:[24,30],iconAnchor:[12,27]});
    if (element.dataset.districts) {
      const dot=L.divIcon({className:'gold-map-dot',html:'<span></span>',iconSize:[14,14],iconAnchor:[7,7]});
      districts.forEach(([name,lat,lng,direction],i)=>{
        const central=i===0;
        L.marker([lat,lng],{icon:central?marker:dot,alt:`${name} — hizmet bölgesi`,zIndexOffset:central?1000:0}).addTo(map)
          .bindTooltip(name,{permanent:true,direction,offset:central?[0,-28]:direction==='bottom'?[0,6]:[8,0],className:central?'map-label map-label--central':'map-label'});
      });
      map.fitBounds(districts.map(([,lat,lng])=>[lat,lng]),{paddingTopLeft:[40,84],paddingBottomRight:[100,30]});
    } else {
      L.marker(center,{icon:marker,alt:'Prestij Nakliyat — Kilimli adresi'}).addTo(map).bindPopup('Prestij Nakliyat<br>Hisararkası Mah. Merkez Evler Sok. No:3/6<br>Kilimli / Zonguldak');
    }
    const zoomIn=element.querySelector('.leaflet-control-zoom-in'),zoomOut=element.querySelector('.leaflet-control-zoom-out');
    zoomIn.title='Yakınlaştır';zoomIn.setAttribute('aria-label','Yakınlaştır');zoomOut.title='Uzaklaştır';zoomOut.setAttribute('aria-label','Uzaklaştır');
    // Wheel zoom needs Ctrl/⌘ or a click on the map first, so page scrolling never gets stuck on the map.
    let wheelActive=false,hintTimer;
    const hint=document.createElement('p');
    hint.className='map-hint';hint.setAttribute('aria-hidden','true');
    hint.textContent=`Yakınlaştırmak için ${/Mac|iPhone|iPad/.test(navigator.platform)?'⌘':'Ctrl'} + fare tekerleğini kullanın veya haritaya tıklayın`;
    element.append(hint);
    element.addEventListener('wheel',event=>{
      if(wheelActive||event.ctrlKey||event.metaKey)return;
      event.stopPropagation();
      hint.classList.add('is-visible');clearTimeout(hintTimer);hintTimer=setTimeout(()=>hint.classList.remove('is-visible'),1400);
    },{capture:true});
    element.addEventListener('mousedown',()=>{wheelActive=true;hint.classList.remove('is-visible');});
    element.addEventListener('mouseleave',()=>{wheelActive=false;});
    new ResizeObserver(()=>map.invalidateSize()).observe(element);
    let notice;
    layer.on('tileerror',()=>{if(notice)return;notice=document.createElement('p');notice.className='map-note';notice.textContent='Harita yüklenemedi. Konumu harita bağlantısından açabilirsiniz.';element.after(notice);});
    layer.on('tileload',()=>{if(notice){notice.remove();notice=null;}});
  }),{rootMargin:'400px 0px'});
  configs.forEach(({id,zoom,districts})=>{const el=document.getElementById(id);if(el){el.dataset.zoom=zoom;if(districts)el.dataset.districts='1';observer.observe(el);}});
})();
