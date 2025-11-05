from typing import Dict, List, Any, Optional
import math
from config import PLACE_TYPE, DEFAULT_DIST


def _rad(x: float) -> float:
    # grados a radianes, para distancias?
    return x * math.pi / 180.0

def dist_km(a: Dict[str, float], b: Dict[str, float]) -> float:
    # distancia "Haversine" en km entre dos puntos
    R = 6371.0
    if a.get("lat") is None or a.get("lon") is None or b.get("lat") is None or b.get("lon") is None:
        return float("inf")
    dlat = _rad(b["lat"] - a["lat"])
    dlon = _rad(b["lon"] - a["lon"])
    lat1 = _rad(a["lat"])
    lat2 = _rad(b["lat"])
    h = math.sin(dlat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
    return 2 * R * math.asin(math.sqrt(h))

def calc_cost(precio_noche: float, modo: str, noches: Optional[int]) -> float:
    # calcula el costo segun las noches seleccionadas
    if modo == "por_noche":
        return precio_noche
    if modo == "por_semana":
        return precio_noche * 7
    n = noches if (noches and noches > 0) else 3
    return precio_noche * n

def lugar_cumple_tags(lista: Dict[str, Any], include: List[str], exclude: List[str]) -> bool:
    tags = lista.get("tags", [])
    # utiliza "all" (AND) para ver si todos los tags estan incluidos
    if include and not all(t in tags for t in include):
        return False
    # utiliza "any" (OR) para ver que no este ni un solo tag excluido
    if exclude and any(t in tags for t in exclude):
        return False
    return True

# algo que quedo de antes, honestamente no se si se usa
def min_dist_por_tipo(hotel: Dict[str, Any], tipo: str, lugares: List[Dict[str, Any]]) -> Optional[float]:
    if tipo not in PLACE_TYPE:
        return None
    dmin: Optional[float] = None
    for l in lugares:
        if l.get("tipo") != tipo:
            continue
        d = dist_km(hotel, l)
        if dmin is None or d < dmin:
            dmin = d
    return dmin

def filtrar_hoteles(
    hoteles: List[Dict[str, Any]],
    presupuesto: Optional[float] = None,
    modo: str = "por_noche",
    noches: Optional[int] = None,
    ciudad: Optional[str] = None,
    tags_incluir: Optional[List[str]] = None,
    tags_excluir: Optional[List[str]] = None,
) -> List[Dict[str, Any]]:
    # filtra hoteles por: ciudad, presupuesto, tags
    tags_incluir = tags_incluir or []
    tags_excluir = tags_excluir or []
    resultados: List[Dict[str, Any]] = []

    for h in hoteles:
        # 1) Ciudad (si se pide)
        if ciudad and h.get("ciudad") != ciudad:
            continue

        # 2) Costo vs presupuesto
        costo = calc_cost(h.get("precio_noche", 0.0), modo, noches)
        if presupuesto is not None and costo > float(presupuesto):
            continue

        # 3) Tags del hotel
        if not lugar_cumple_tags(h, tags_incluir, tags_excluir):
            continue

        # Resultado (incluye lat/lon para marcar en el mapa)
        resultados.append({
            "id": h["id"],
            "nom": h["nom"],
            "ciudad": h["ciudad"],
            "precio_noche": h["precio_noche"],
            "costo_calculado": round(costo, 2),
            "tags": h.get("tags", []),
            "lat": h.get("lat"),
            "lon": h.get("lon"),
        })

    # Ordenar por costo calculado (barato primero)
    resultados.sort(key=lambda x: x["costo_calculado"])
    return resultados
