# ================================================
#  base_conocimiento.py
#  Base de conocimiento para resolución SLD
# ================================================

# --- Hechos: Hoteles (cláusulas unitarias) ---
# Clausula de Horn (hecho):
# hotel(Nombre, Ciudad, Tipo, Costo, Servicios)
# Significa: "El hotel Nombre se encuentra en Ciudad, es de Tipo, cuesta Costo, y ofrece Servicios."

Hoteles = {
    "Hotel_Sol_Cancun": {
        "ciudad": "Cancún",
        "tipo": "lujo",
        "costo": 2000,
        "servicios": ["desayuno", "spa", "transporte"]
    },
    "Hostal_Playa_Cancun": {
        "ciudad": "Cancún",
        "tipo": "económico",
        "costo": 500,
        "servicios": []
    },
    "Hotel_Lujo_Los_Cabos": {
        "ciudad": "Los Cabos",
        "tipo": "lujo",
        "costo": 5000,
        "servicios": ["spa", "transporte"]
    },
    "Cabana_Bosque_Valle": {
        "ciudad": "Valle de Bravo",
        "tipo": "rústico",
        "costo": 1200,
        "servicios": ["desayuno"]
    }
}

# --- Hechos: Actividades (cláusulas unitarias) ---
# Clausula de Horn (hecho):
# actividad(Nombre, Ciudad, Tipo, Costo)
# Significa: "La actividad Nombre se realiza en Ciudad, es de Tipo, y cuesta Costo pesos."

Actividades = {
    "Snorkel_Cancun": {
        "ciudad": "Cancún",
        "tipo": "acuática",
        "costo": 700
    },
    "Paracaidismo_Los_Cabos": {
        "ciudad": "Los Cabos",
        "tipo": "extrema",
        "costo": 3000
    },
    "Museo_Frida_CDMX": {
        "ciudad": "Ciudad de México",
        "tipo": "cultural",
        "costo": 200
    },
    "Kayak_Valle": {
        "ciudad": "Valle de Bravo",
        "tipo": "acuática",
        "costo": 600
    },
    "Senderismo_Valle": {
        "ciudad": "Valle de Bravo",
        "tipo": "aventura",
        "costo": 0
    }
}
