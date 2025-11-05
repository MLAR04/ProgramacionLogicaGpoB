from fastapi import FastAPI, Query, Body
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from typing import Optional, Dict, Any, List

from config import DEFAULT_DIST, PLACE_TYPE, HOTEL_TAGS
from data import Hoteles, Lugares
from logic import filtrar_hoteles, dist_km

app = FastAPI(title="Turismo")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"]
)

# hace carpeta "html" estatica
app.mount("/static", StaticFiles(directory="html"), name="static")

@app.get("/", include_in_schema=False)
def root():
    return FileResponse("html/index.html")

@app.get("/health")
def health():
    return {"status": "ok"}

# cargar info
@app.get("/catalogo")
def catalogo():
    return {
        "dist_default_km": DEFAULT_DIST,
        "place_type": [
            {"clave": k, "label": v["label"], "emoji": v["emoji"]}
            for k, v in PLACE_TYPE.items()
        ],
        "hotel_tags": [
            {"clave": k, "label": v}
            for k, v in HOTEL_TAGS.items()
        ],
    }

@app.get("/tipos")
def tipos_compat():
    return {
        "dist_default_km": DEFAULT_DIST,
        "tipos": [
            {"clave": k, "label": v["label"], "emoji": v["emoji"]}
            for k, v in PLACE_TYPE.items()
        ],
        "tags_sugeridos": HOTEL_TAGS,
    }

# para lista dinamica
@app.get("/ciudades")
def ciudades():
    return sorted({h.get("ciudad") for h in Hoteles if h.get("ciudad")})

@app.post("/hoteles/filtrados")
def hoteles_filtrados_endpoint(payload: Dict[str, Any] = Body(...)):
    presupuesto = payload.get("presupuesto")
    modo = payload.get("modo", "por_noche")
    noches = payload.get("noches")
    ciudad = payload.get("ciudad")
    tags_incluir = payload.get("tags_incluir", [])
    tags_excluir = payload.get("tags_excluir", [])

    res = filtrar_hoteles(
        Hoteles, presupuesto, modo, noches, ciudad, tags_incluir, tags_excluir
    )
    return JSONResponse(res)

@app.get("/hotel/{hotel_id}")
def get_hotel(hotel_id: str):
    h = next((x for x in Hoteles if x["id"] == hotel_id), None)
    if not h:
        return JSONResponse({"error": "not found"}, status_code=404)
    return h

# cosa para ver las actividades
@app.get("/actividades_cercanas")
def actividades_cercanas(
    hotel_id: str = Query(...),
    tipos_incluir: Optional[str] = Query(None),  # CSV de tags a incluir
    tipos_excluir: Optional[str] = Query(None),  # CSV de tags a excluir
):
    h = next((x for x in Hoteles if x["id"] == hotel_id), None)
    if not h:
        return JSONResponse([], status_code=404)

    inc = set(t.strip() for t in tipos_incluir.split(",")) if tipos_incluir else set()
    exc = set(t.strip() for t in tipos_excluir.split(",")) if tipos_excluir else set()

    found = []
    for l in Lugares:
        t = l.get("tipo")
        if inc and t not in inc:
            continue
        if exc and t in exc:
            continue
        d = dist_km(h, l)
        if d <= DEFAULT_DIST:
            found.append({
                "id": l["id"],
                "nom": l["nom"],
                "tipo": t,
                "dist_km": round(d, 3),
                "lat": l.get("lat"),
                "lon": l.get("lon"),
                "price_level": l.get("price_level"),
                "img": l.get("img"),
            })
    found.sort(key=lambda x: x["dist_km"])
    return JSONResponse(found)
