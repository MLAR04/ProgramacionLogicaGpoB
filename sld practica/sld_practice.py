"""
sld_practice.py
Sistema experto sobre turismo en México
"""

from copy import deepcopy

# ===== BASE DE CONOCIMIENTO =====
base_conocimiento = [
    ("hotel", ["Hotel_Sol", "Cancún", "lujo", 2000]),
    ("hotel", ["Hostal_Playa", "Cancún", "económico", 500]),
    ("hotel", ["Hotel_Lujo", "Los_Cabos", "lujo", 5000]),
    ("hotel", ["Cabaña_Bosque", "Valle_de_Bravo", "rural", 1200]),
    ("actividad", ["Snorkel", "Cancún", "acuática", 700]),
    ("actividad", ["Paracaidismo", "Los_Cabos", "extrema", 3000]),
    ("actividad", ["Museo_Frida_Kahlo", "Ciudad_de_México", "cultural", 200]),
    ("actividad", ["Kayak", "Valle_de_Bravo", "acuática", 600]),
    ("actividad", ["Senderismo", "Valle_de_Bravo", "aventura", 0]),
    ("actividad", ["Tour_Tequila", "Guadalajara", "gastronómica", 350])
]

# ===== REGLAS =====
reglas = [
    ("turistico", ["Lugar"],
     [("actividad", ["_", "Lugar", "_", "_"])]),

    ("accesible", ["Hotel", "Lugar", "Presupuesto"],
     [("hotel", ["Hotel", "Lugar", "_", "Precio"]),
      ("<=", ["Precio", "Presupuesto"])])
]


# ===== UNIFICACIÓN =====
def unificar(patron, hecho, sustituciones):
    s = deepcopy(sustituciones)
    for p, h in zip(patron, hecho):
        if p == "_":
            continue
        if isinstance(p, str) and p[0].isupper():
            if p in s:
                if s[p] != h:
                    return None
            else:
                s[p] = h
        elif p != h:
            return None
    return s


# ===== RESOLUCIÓN SLD =====
def resolver(query):
    print(f"\n Resolviendo consulta: {query}")
    pila = [(query, {})]

    while pila:
        objetivo, sustituciones = pila.pop()
        predicado, argumentos = objetivo
        print(f"\n Objetivo actual: {predicado}{tuple(argumentos)}")

        # Comparaciones numéricas
        if predicado == "<=":
            var1, var2 = argumentos
            val1 = sustituciones.get(var1, var1)
            val2 = sustituciones.get(var2, var2)
            try:
                if float(val1) <= float(val2):
                    print(f" Comparación verdadera: {val1} <= {val2}")
                    continue
                else:
                    print(f" Comparación falsa: {val1} <= {val2}")
                    return None
            except ValueError:
                print(f" No se pudo evaluar comparación: {val1} <= {val2}")
                return None

        # Hechos
        for hecho in base_conocimiento:
            if hecho[0] == predicado:
                unif = unificar(argumentos, hecho[1], sustituciones)
                if unif is not None:
                    print(f" Unificado con hecho: {hecho}")
                    print(f"Sustituciones: {unif}")
                    return unif

        # Reglas
        for regla in reglas:
            cabeza_pred, cabeza_args, cuerpo = regla
            if cabeza_pred == predicado:
                unif = unificar(argumentos, cabeza_args, sustituciones)
                if unif is not None:
                    print(f" Aplicando regla: {cabeza_pred}{tuple(cabeza_args)} :- {cuerpo}")
                    for subobjetivo in reversed(cuerpo):
                        pila.append((subobjetivo, unif))
                    break
    print("❌ No se encontró solución.")
    return None


# ===== INTERFAZ DE USUARIO =====
def mostrar_conocimiento():
    print("\n====================================")
    print("SISTEMA EXPERTO TURISMO EN MÉXICO")
    print("====================================")
    print("\n📋 Lugares y actividades registradas:\n")

    lugares = set([h[1][1] for h in base_conocimiento if h[0] == "hotel"])
    for lugar in lugares:
        print(f"  {lugar}")
        print("  Hoteles:")
        for h in base_conocimiento:
            if h[0] == "hotel" and h[1][1] == lugar:
                print(f"   • {h[1][0]} ({h[1][2]}) - ${h[1][3]} por noche")
        print("  Actividades:")
        for a in base_conocimiento:
            if a[0] == "actividad" and a[1][1] == lugar:
                print(f"   • {a[1][0]} ({a[1][2]}) - ${a[1][3]}")
        print()


def menu_interactivo():
    print("====================================")
    print("¿Qué deseas consultar?")
    print("1️⃣  Verificar si un lugar es turístico.")
    print("2️⃣  Buscar hospedajes accesibles según tu presupuesto.")
    print("3️⃣  Salir.")
    print("====================================")

    while True:
        opcion = input("\nSelecciona una opción (1-3): ")

        if opcion == "1":
            lugar = input(" Ingresa el nombre del lugar: ").strip()
            resultado = resolver(("turistico", [lugar]))
            if resultado:
                print(f"\n {lugar} es un lugar turístico.")
            else:
                print(f"\n No se encontraron actividades en {lugar}.")

        elif opcion == "2":
            lugar = input(" Ingresa el nombre del lugar: ").strip()
            presupuesto = float(input(" Ingresa tu presupuesto (MXN): "))
            resultado = resolver(("accesible", ["Hotel", lugar, presupuesto]))
            if resultado:
                print(f"\n Puedes hospedarte en {resultado['Hotel']} en {resultado['Lugar']} por ${resultado['Precio']} por noche.")
            else:
                print(f"\n No se encontraron hospedajes en {lugar} dentro del presupuesto de ${presupuesto}.")

        elif opcion == "3":
            print("\n Gracias por usar el sistema experto de turismo.")
            break

        else:
            print(" Opción inválida. Intenta de nuevo.")


# ===== PROGRAMA PRINCIPAL =====
if __name__ == "__main__":
    mostrar_conocimiento()
    menu_interactivo()
