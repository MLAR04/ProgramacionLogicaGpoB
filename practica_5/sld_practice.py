

from base_conocimiento import Hoteles, Actividades  

#  es la función que compara el patrón (consulta) con los hechos (base de conocimiento).
def unificar(patron, hecho):
    if patron[0] != hecho[0]:
        return None
    if hecho[2] > patron[2]:
        return None
    return {"X": hecho[1]}


def resolver_SLD(lista, patron, tipo, base_datos, resultados, paso=0):
    if paso >= len(lista):
        return

    elemento = lista[paso]
    costo = base_datos[elemento]["costo"]
    hecho = (tipo, elemento, costo)

    print(f"({paso+1}) : {patron}  ↔  {hecho}")
    sustitucion = unificar(patron, hecho)

    if sustitucion:
        print(f"resultado: {sustitucion}")
        resultados.append(sustitucion)
    else:
        print("error")

    resolver_SLD(lista, patron, tipo, base_datos, resultados, paso + 1)


# clausula 1 actividades_por_presupuesto
# "una actividad X se recomienda si se realiza en la Ciudad y cuesta menos o igual que el Presupuesto."
def actividades_por_presupuesto(ciudad, presupuesto):
    print(f"\n🔍 Consulta: actividades en {ciudad} con {presupuesto} pesos\n")

    actividades = [a for a, datos in Actividades.items() if datos["ciudad"].lower() == ciudad.lower()]
    patron = ("actividad", "X", presupuesto)
    resultados = []

    resolver_SLD(actividades, patron, "actividad", Actividades, resultados)

    if not resultados:
        print("\nNo se encontraron actividades dentro del presupuesto.\n")
    else:
        print("\nactividades recomendadas:")
        for r in resultados:
            act = r["X"]
            info = Actividades[act]
            print(f"- {act.replace('_', ' ')} ({info['tipo']}), ${info['costo']} pesos")


# xlausula 2
# "un hotel X se recomienda si está en la Ciudad y su costo no excede el Presupuesto."
def hoteles_por_presupuesto(ciudad, presupuesto):
    print(f"\nconsulta: hoteles en {ciudad} con {presupuesto} pesos\n")

    hoteles = [h for h, datos in Hoteles.items() if datos["ciudad"].lower() == ciudad.lower()]
    patron = ("hotel", "X", presupuesto)
    resultados = []

    resolver_SLD(hoteles, patron, "hotel", Hoteles, resultados)

    if not resultados:
        print("\nNo se encontraron hoteles.\n")
    else:
        print("\n Hoteles recomendados:")
        for r in resultados:
            hotel = r["X"]
            info = Hoteles[hotel]
            servicios = ", ".join(info["servicios"]) if info["servicios"] else "no hay servicios adicionales"
            print(f"- {hotel.replace('_', ' ')} ({info['tipo']}), ${info['costo']} pesos. Servicios: {servicios}")


if __name__ == "__main__":

    # Consultas 
    actividades_por_presupuesto("Cancún", 1000)
    actividades_por_presupuesto("Valle de Bravo", 800)
    actividades_por_presupuesto("Ciudad de México", 500)
    actividades_por_presupuesto("Los Cabos", 2500)

    hoteles_por_presupuesto("Cancún", 2500)
    hoteles_por_presupuesto("Valle de Bravo", 1500)
    hoteles_por_presupuesto("Los Cabos", 5000)
    hoteles_por_presupuesto("Los Cabos", 3000)
    hoteles_por_presupuesto("Cancún", 600)