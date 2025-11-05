let TIPOS = [];  // [{clave, label, emoji}, ...] (PLACE_TYPE)
let HOTEL_TAGS = [];  // [{clave, label}, ...]
let DIST_DEFAULT = 5;  // cambiar con config.py's DEFAULT_DIST, por si acaso

let selectedHotel = null;
let map, hotelLayer, activityLayer, hotelMarker;

function debounce(fn, ms=300){
    let t; return (...args)=>{ clearTimeout(t); t=setTimeout(()=>fn(...args), ms); };
}

function cycleState(el){
    // neutral -> include -> exclude -> neutral...
    if(el.classList.contains('include')) { el.classList.remove('include'); el.classList.add('exclude'); el.dataset.state='-1'; }
    else if(el.classList.contains('exclude')) { el.classList.remove('exclude'); el.dataset.state='0'; }
    else { el.classList.add('include'); el.dataset.state='1'; }
}
function currentIncludeExclude(containerSel){
    const inc=[], exc=[];
    document.querySelectorAll(containerSel+' .chip').forEach(ch=>{
        const key = ch.dataset.key;
        const st = ch.dataset.state || '0';
        if(st==='1') inc.push(key);
        if(st==='-1') exc.push(key);
    });
    return {inc, exc};
}
function emojiIcon(htmlEmoji){
    return L.divIcon({ html: `<div style="font-size:20px; line-height:20px">${htmlEmoji}</div>`, className: "emoji-icon", iconSize: [24,24], iconAnchor: [12,12] });
}

// tipos de lugares y ciudades
async function fetchTipos(){
    const res = await fetch('/tipos');
    const data = await res.json();
    TIPOS = data.tipos || [];
    if (Array.isArray(data.tags_sugeridos)) {
        HOTEL_TAGS = data.tags_sugeridos;
    } else {
        HOTEL_TAGS = Object.entries(data.tags_sugeridos || {}).map(([k,v])=>({clave:k,label:v}));
    }
    DIST_DEFAULT = data.dist_default_km || DIST_DEFAULT;
    renderHotelTagChips();
    renderTypeChips();
}
async function fetchCiudades(){
    try {
        const r = await fetch('/ciudades');
        if(r.ok){
            const cities = await r.json();
            renderCiudades(cities);
            return;
        }
    } catch {}
    // Fallback: infiere ciudades desde hoteles (sin filtros)
    const r2 = await fetch('/hoteles/filtrados', {
        method:'POST', headers:{'Content-Type':'application/json'},
        body: JSON.stringify({})
    });
    const hotels = await r2.json();
    const set = new Set(hotels.map(h=>h.ciudad).filter(Boolean));
    renderCiudades(Array.from(set).sort());
}
function renderCiudades(cities){
    const sel = document.getElementById('ciudad');
    sel.innerHTML = '<option value="">Todas</option>' + cities.map(c=>`<option>${c}</option>`).join('');
}
function renderHotelTagChips(){
    const c = document.getElementById('hotelTags');
    c.innerHTML = HOTEL_TAGS.map(t=>`<span class="chip" data-key="${t.clave}" data-state="0">${t.label}</span>`).join('');
    c.querySelectorAll('.chip').forEach(ch=> ch.addEventListener('click', ()=>{ cycleState(ch); aplicar(); }));
}
function renderTypeChips(){
    const c = document.getElementById('typeChips');
    c.innerHTML = TIPOS.map(t=>`<span class="chip" data-key="${t.clave}" data-state="0">${t.emoji} ${t.label}</span>`).join('');
    c.querySelectorAll('.chip').forEach(ch=> ch.addEventListener('click', ()=>{ cycleState(ch); updateActivities(); }));
}

// mapa
function initMap(){
    map = L.map('map').setView([32.52, -117.04], 12);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { maxZoom: 19 }).addTo(map);
    hotelLayer = L.layerGroup().addTo(map);
    activityLayer = L.layerGroup().addTo(map);
    // asegurar tamaño correcto
    setTimeout(()=> map.invalidateSize(), 0);
}
function clearHotels(){
    hotelLayer.clearLayers();
    if(hotelMarker){
        map.removeLayer(hotelMarker);
        hotelMarker=null;
    }
}
function clearActivities(){
    activityLayer.clearLayers();
}
function fitToMarkers(latlngs){
    if(!latlngs.length) return;
    if(latlngs.length===1){
        map.setView(latlngs[0], 13);
        return;
    }
    const bounds = L.latLngBounds(latlngs);
    map.fitBounds(bounds.pad(0.2));
}

// filtros dinamicos
const aplicarDebounced = debounce(aplicar, 300);

document.getElementById('aplicarFiltros').addEventListener('click', aplicar); // opcional
const modoSel = document.getElementById('modo');
const nochesInput = document.getElementById('noches');
const presupuestoInput = document.getElementById('presupuesto');
const ciudadSel = document.getElementById('ciudad');

modoSel.addEventListener('change', ()=> {
    nochesInput.style.display = modoSel.value==='total_viaje' ? 'inline-block' : 'none';
    aplicarDebounced();
});
nochesInput.addEventListener('input', aplicarDebounced);
presupuestoInput.addEventListener('input', aplicarDebounced);
ciudadSel.addEventListener('change', aplicarDebounced);

async function aplicar(){
    try {
        const presupuesto = presupuestoInput.value || null;
        const modo = modoSel.value;
        const noches = nochesInput.value ? parseInt(nochesInput.value,10) : null;
        const ciudad = ciudadSel.value || null;
        const {inc: tags_incluir, exc: tags_excluir} = currentIncludeExclude('#hotelTags');

        const res = await fetch('/hoteles/filtrados', {
            method:'POST', headers:{'Content-Type':'application/json'},
            body: JSON.stringify({ presupuesto: presupuesto? Number(presupuesto): null, modo, noches, ciudad, tags_incluir, tags_excluir })
        });
        const data = await res.json();
        renderHoteles(data);
        plotHotels(data);
    } catch (e) {
        console.error('Error al aplicar filtros:', e);
    }
}

function renderHoteles(list){
    const box = document.getElementById('listaHoteles');
    if(!list.length){
        box.innerHTML = '<p class="muted">No hay hospedajes que cumplan esos filtros.</p>';
        clearHotels(); clearActivities(); return;
    }
    box.innerHTML = list.map(h=>`
        <div class="hotel-item" data-id="${h.id}" data-lat="${h.lat||''}" data-lon="${h.lon||''}">
            <strong>${h.nom}</strong> — ${h.ciudad}<br/>
            <span class="muted">$${h.costo_calculado} MXN (${h.precio_noche}/noche)</span>
        </div>`).join('');
        box.querySelectorAll('.hotel-item').forEach(div=> div.addEventListener('click', ()=> selectHotel(div.dataset.id)));
        // mantener resaltado si ya habia uno seleccionado
        if (selectedHotel) highlightHotel(selectedHotel);
}

function plotHotels(hoteles){
    clearHotels(); clearActivities();
    const latlngs = [];
    for(const h of hoteles){
        if(h.lat!=null && h.lon!=null){
            const m = L.marker([h.lat, h.lon]);  // pin default
            // Tooltip (hover) con nombre, ciudad y precio/noche
            m.bindTooltip(`${h.nom} — ${h.ciudad} — $${h.precio_noche} / noche`, { direction: 'top' });
            // Popup simple (sin imagen)
            m.bindPopup(`<strong>${h.nom}</strong><br/><span class='muted'>${h.ciudad}</span><br/><span class='muted'>$${h.precio_noche} / noche</span>`);
            hotelLayer.addLayer(m);
            latlngs.push([h.lat, h.lon]);
        }
    }
    if(latlngs.length){ fitToMarkers(latlngs); setTimeout(()=> map.invalidateSize(), 0); }
}

function highlightHotel(hotelId) {
    document.querySelectorAll(".hotel-item").forEach(el => {
        el.classList.toggle("selected", hotelId && el.dataset.id === hotelId);
    });
}

async function selectHotel(hotelId){
    if (selectedHotel === hotelId) {
        selectedHotel = null;
        highlightHotel(null);
        document.getElementById("hotelSel").textContent = "Elige un hotel para ver actividades cercanas.";
        clearActivities();
        aplicar();
        return;
    }

    selectedHotel = hotelId;
    highlightHotel(hotelId);

    // borra TODOS los demas hoteles del mapa y mostrar solo el seleccionado
    clearHotels();
    // centra en el hotel seleccionado
    const hres = await fetch(`/hotel/${encodeURIComponent(selectedHotel)}`);
    const hotel = await hres.json();
    if(hotel && hotel.lat && hotel.lon){
        const htmlImg = hotel.img ? `<img class="popup-img" src="${hotel.img}" alt="${hotel.nom}" />` : "";
        hotelMarker = L.marker([hotel.lat, hotel.lon]).addTo(map);
        hotelMarker.bindTooltip(`${hotel.nom} — ${hotel.ciudad} — $${hotel.precio_noche} / noche`, { direction: 'top' });
        hotelMarker.bindPopup(`<strong>${hotel.nom}</strong><br/><span class='muted'>${hotel.ciudad}</span><br/><span class='muted'>$${hotel.precio_noche} / noche</span>${htmlImg}`);
        map.setView([hotel.lat, hotel.lon], 13);
        setTimeout(()=> map.invalidateSize(), 0);
    }
    await updateActivities();
}

// botones tri-estado de tipos
function computeTiposParam(){
    const incExc = currentIncludeExclude('#typeChips');
    let incluir = incExc.inc.slice();
    if(!incluir.length && incExc.exc.length){
        const all = TIPOS.map(t=>t.clave);
        incluir = all.filter(k=> !incExc.exc.includes(k));
    }
    return incluir;
}

async function updateActivities(){
    if(!selectedHotel) return;
    clearActivities();

    const incluirTipos = computeTiposParam();
    const q = new URLSearchParams({ hotel_id: selectedHotel });
    if(incluirTipos.length) q.set('tipos', incluirTipos.join(','));

    const res = await fetch('/actividades_cercanas?'+q.toString());
    const sitios = await res.json();

    const latlngs = [];
    for(const l of sitios){
        const t = TIPOS.find(x=>x.clave === l.tipo);
        const emoji = t ? t.emoji : "⭐";
        const label = t ? `${t.emoji} ${t.label}` : l.tipo;
        const price = l.price_level ? ` — ${l.price_level}` : "";
        const img = l.img ? `<img class="popup-img" src="${l.img}" alt="${l.nom}" />` : "";

        const m = L.marker([l.lat, l.lon], { icon: emojiIcon(emoji) });
        // Hover
        m.bindTooltip(`${l.nom} — ${label}${price} — ${l.dist_km} km`, { direction: 'top' });
        m.on('mouseover', e => e.target.openTooltip());
        m.on('mouseout', e => e.target.closeTooltip());
        // Click
        m.bindPopup(`<strong>${l.nom}</strong><br/>${label}${price}<br/><span class='muted'>${l.dist_km} km</span>${img}`);

        activityLayer.addLayer(m);
        latlngs.push([l.lat, l.lon]);
    }
    if(latlngs.length){ fitToMarkers(latlngs); setTimeout(()=> map.invalidateSize(), 0); }
}

// boot
(async function(){
    try {
        await fetchTipos();
        await fetchCiudades();
        initMap();
        await aplicar(); // muestra lista + pins al cargar
    } catch(e) {
        console.error('Error inicializando:', e);
    }
})();
