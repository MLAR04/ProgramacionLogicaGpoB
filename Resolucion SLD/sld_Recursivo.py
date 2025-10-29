Hoteles = {
    "Hotel_Xcaret_Mexico": {"costo": 1900},
    "Hotel_Riu_Palace": {"costo": 2800}
}

Actividades = {
    "Tour_de_Snorkel_en_Isla_Mujeres": {"Costo": 800},
    "Playa_Delfines": {"Costo": 0}
}

Ciudades = {
    "cancun": {
        "Hoteles": ["Hotel_Xcaret_Mexico"],
        "Actividades": ["Tour_de_Snorkel_en_Isla_Mujeres", "Playa_Delfines"]
    },
    "los_cabos": {
        "Hoteles": ["Hotel_Riu_Palace"]
    }
}


# Función recursiva para buscar coincidencias
def buscar_recursivo(lista, patron, tipo, base_datos, resultados, i=0):
    if i >= len(lista):
        return

    elemento = lista[i]
    costo = base_datos[elemento]["costo"] if tipo == "hotel" else base_datos[elemento]["Costo"]
    hecho = (tipo, elemento, costo)
    print("Intentando unificar:", patron, "con", hecho)

    # Unificacion:
    if patron[0] == hecho[0] and hecho[2] <= patron[2]:
        sustitucion = {"X": hecho[1]}
        resultados.append(sustitucion)

    # Recursividad
    buscar_recursivo(lista, patron, tipo, base_datos, resultados, i + 1)


# Clausula Horn 1: Qué actividades puedo hacer con cierto presupuesto
def actividades_ciudad(ciudad, presupuesto):
    print(f"\nConsulta: actividades en {ciudad} con {presupuesto} pesos\n")
    actividades = Ciudades[ciudad].get("Actividades", [])
    patron = ("actividad", "X", presupuesto)
    resultados = []

    buscar_recursivo(actividades, patron, "actividad", Actividades, resultados)

    if not resultados:
        return print("No se encontraron actividades disponibles")
    return print(resultados)


# Clausula Horn 2: En qué hoteles puedo hospedarme con cierto presupuesto
def hoteles_presupuesto(ciudad, presupuesto):
    print(f"\nConsulta: hoteles en {ciudad} con {presupuesto} pesos\n")
    hoteles = Ciudades[ciudad].get("Hoteles", [])
    patron = ("hotel", "X", presupuesto)
    resultados = []

    buscar_recursivo(hoteles, patron, "hotel", Hoteles, resultados)

    if not resultados:
        return print("No se encontraron Hoteles disponibles")
    return print(resultados)


# Consultas
actividades_ciudad("cancun", 1000)
hoteles_presupuesto("cancun", 2000)
