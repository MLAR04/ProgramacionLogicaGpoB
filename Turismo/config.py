# distancia entre hotel y actividades (en km)
DEFAULT_DIST: float = 5

# tipos para las actividades
PLACE_TYPE = {
    "restaurante": {"label": "Restaurantes", "emoji": "🍔"},
    "playa": {"label": "Playas", "emoji": "🏖️"},
    "museo": {"label": "Museos", "emoji": "🏛️"},
    "parque": {"label": "Parques", "emoji": "🌳"},
    "caminata": {"label": "Caminatas", "emoji": "🚶"},
    "escenico": {"label": "Puntos escénicos", "emoji": "📸"},
    "bar": {"label": "Bares", "emoji": "🍺"},
    "compras": {"label": "Compras", "emoji": "🛍️"},
    "arte": {"label": "Arte & murales", "emoji": "🎨"},
    "interes": {"label": "Sitios de interés", "emoji": "⭐"},
}

# tags/etiquetas para describir el hotel
HOTEL_TAGS = {
    "familiar": "Familiar",
    "negocios": "Negocios",
    "pet": "Pet friendly",
    "naturaleza": "Naturaleza",
    "comida": "Comida",
    "popular": "Popular",
    "romantico": "Romántico",
}

# COMO SE CORRE:
# primero en terminal vas a escribir:
# pip install -r install.txt
# despues, en terminal escribir:
# uvicorn api:app --reload
# y luego entrar al url que te dice
