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


# Clausula Horn 1: Qué actividades puedo hacer con cierto presupuesto
def actividades_ciudad(ciudad, presupuesto):
    print(f"\nConsulta: actividades en {ciudad} con {presupuesto} pesos\n")
    patron = ("actividad", "X", presupuesto) # query
    resultados = []

    for actividad in Ciudades[ciudad]["Actividades"]:
        hecho = ("actividad", actividad, Actividades[actividad]["Costo"])
        print("Intentando unificar:", patron, "con", hecho)

        # Unificación (si tipo coincide y el costo cumple)
        if patron[0] == hecho[0] and hecho[2] <= patron[2]:
            sustitucion = {"X": hecho[1]}
            resultados.append(sustitucion)

    if not resultados:
        return print("No se encontraron actividades disponibles")

    return print(resultados)


# Clausula Horn 2: En qué hoteles puedo hospedarme con cierto presupuesto
def hoteles_presupuesto(ciudad, presupuesto):
    print(f"\nConsulta: hoteles en {ciudad} con {presupuesto} pesos\n")
    patron = ("hotel", "X", presupuesto) # query
    resultados = []

    for hotel in Ciudades[ciudad]["Hoteles"]:
        hecho = ("hotel", hotel, Hoteles[hotel]["costo"])
        print("Intentando unificar:", patron, "con", hecho)
        # Unificación (si hecho coincide y el costo cumple)
        if patron[0] == hecho[0] and hecho[2] <= patron[2]:
            sustitucion = {"X": hecho[1]}
            resultados.append(sustitucion)

    if not resultados:
        return print("No se encontraron Hoteles disponibles")

    return print(resultados)


# Consultas
actividades_ciudad("cancun", 900)

hoteles_presupuesto("cancun", 2000)
