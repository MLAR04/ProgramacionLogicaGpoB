from typing import List, Dict, Any

# id, nombre, ciudad, latitud, longitud, precio por noche, etiquetas del hotel
# para las img, agregar URL con al final: ?q=80&w=1200&auto=format&fit=crop
Hoteles: List[Dict[str, Any]] = [
    {"id": "h_001", "nom": "Hotel Bahía Azul", "ciudad": "Tijuana", "lat": 32.5149, "lon": -117.0382, "precio_noche": 1200.0, "tags": ["familiar", "playa", "pet"], "img": ""},
    {"id": "h_002", "nom": "Hotel Centro Histórico", "ciudad": "Tijuana", "lat": 32.5280, "lon": -117.0430, "precio_noche": 900.0, "tags": ["negocios", "popular"], "img": "https://i.scdn.co/image/ab67616d00001e024fb2717cb8c109535a59aea9?q=80&w=1200&auto=format&fit=crop"},
    {"id": "h_003", "nom": "Eco Lodge Sierra", "ciudad": "Tecate", "lat": 32.5660, "lon": -116.6290, "precio_noche": 1600.0, "tags": ["naturaleza", "romantico"], "img": ""},
]

# id, nombre, tipo de actividad (tiene su icono/emoji asignado en config.py), latitud, longitud, precio
# para las img, agregar URL con al final: ?q=80&w=1200&auto=format&fit=crop
Lugares: List[Dict[str, Any]] = [
    {"id": "p_001", "nom": "Mercado Gastronómico", "tipo": "restaurante", "lat": 32.5240, "lon": -117.0435, "price_level": "$$", "img": "https://i.scdn.co/image/ab67616d00001e024fb2717cb8c109535a59aea9?q=80&w=1200&auto=format&fit=crop"},
    {"id": "p_002", "nom": "Parque Lineal", "tipo": "parque", "lat": 32.5220, "lon": -117.0500, "price_level": "gratis", "img": ""},
    {"id": "p_003", "nom": "Playa Hermosa", "tipo": "playa", "lat": 32.4860, "lon": -117.1280, "price_level": "gratis", "img": ""},
    {"id": "p_004", "nom": "Museo de Historia", "tipo": "museo", "lat": 32.5250, "lon": -117.0330, "price_level": "$", "img": ""},
    {"id": "p_005", "nom": "Sendero La Rumorosa", "tipo": "caminata", "lat": 32.6350, "lon": -116.0450, "price_level": "gratis", "img": ""},
    {"id": "p_006", "nom": "Mirador Panorámico", "tipo": "escenico", "lat": 32.5010, "lon": -116.9900, "price_level": "gratis", "img": ""},
    {"id": "p_007", "nom": "Zona de Bares", "tipo": "bar", "lat": 32.5255, "lon": -117.0200, "price_level": "$$", "img": ""},
    {"id": "p_008", "nom": "Plaza Comercial Centro", "tipo": "compras", "lat": 32.5300, "lon": -117.0450, "price_level": "$$", "img": ""},
    {"id": "p_009", "nom": "Murales Urbanos", "tipo": "arte", "lat": 32.5310, "lon": -117.0470, "price_level": "gratis", "img": ""},
    {"id": "p_010", "nom": "Atractivo Local", "tipo": "interes", "lat": 32.5200, "lon": -117.0400, "price_level": "$", "img": ""},
]
