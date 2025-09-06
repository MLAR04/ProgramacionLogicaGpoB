# Autor: Flores Hernandez Roberto David

# ------------------ Hechos ------------------
hechos = {
    "cuentas": {
        "Carlos": "bbva"   # Carlos tiene cuenta en bbva
    },
    "bancos": ["bbva"],
    "prestamos": {
        "bbva": ["hipotecario"],  # bbva puede dar préstamos hipotecarios
    },
    "dinero_prestado": {
        "Carlos": 10000000  # Carlos recibió 10,000,000
    },
    # Ley: Los clientes de bbva deben tener por lo menos 100 pesos en su cuenta
    "saldos" : {
    "Carlos": 100
    }
}

# ------------------ Leyes ------------------
leyes = {
    "cuenta_requiere_mayoria_edad": {"accion": "tener_cuenta", "condicion": "mayor_edad"},
    "prestamos_bbva": {"banco": "bbva", "condicion": "solo_clientes"},
    "prestamos_a_Carlos": {"persona": "Carlos", "prestamista": "solo_banco"}
}


# ------------------ Consultas ------------------

def carlos_mayor_edad():
    print("¿Carlos tiene por lo menos 18 años?")
    if "Carlos" in hechos["cuentas"] and leyes["cuenta_requiere_mayoria_edad"]["condicion"] == "mayor_edad":
        return True
    return False


def ricardo_tiene_cuenta():
    print("¿Ricardo tiene una cuenta de banco?")
    return "Ricardo" in hechos["cuentas"]


def bbva_tiene_clientes():
    print("¿bbva tiene clientes?")
    # revisamos si alguien tiene como banco "bbva"
    for persona, banco in hechos["cuentas"].items():
        if banco == "bbva":
            return True
    return False


def prestamas_es_banco():
    print("¿prestamas es un banco?")
    return "prestamas" in hechos["bancos"]


def tiene_100_pesos(persona):
    print(f"¿{persona} tiene 100 pesos?")
    if persona in hechos["cuentas"] and hechos["cuentas"][persona] == "bbva":
        return hechos["saldos"].get(persona, 0) >= 100
    return False


def felipe_cliente_bbva():
    print("¿Felipe es cliente de bbva?")
    return hechos["cuentas"].get("Felipe") == "bbva"


def bbva_prestamos_estudiantiles():
    print("¿bbva genera préstamos estudiantiles?")
    return "estudiantil" in hechos["prestamos"].get("bbva", [])


def bbva_presta_carlos():
    print("¿bbva le prestaría dinero a Carlos?")
    if (hechos["cuentas"].get("Carlos") == "bbva" and
        leyes["prestamos_bbva"]["condicion"] == "solo_clientes"):
        return True
    return False


def bbva_prestamo_hipotecario_carlos():
    print("¿bbva le dio un préstamo hipotecario a Carlos?")
    if ("hipotecario" in hechos["prestamos"].get("bbva", []) and
        "Carlos" in hechos["dinero_prestado"] and
        leyes["prestamos_a_Carlos"]["prestamista"] == "solo_banco"):
        return True
    return False


def carlos_pidio_a_juan():
    print("¿Carlos pidió prestado dinero a Juan?")
    if leyes["prestamos_a_Carlos"]["prestamista"] != "solo_banco":
        return True
    return False


# ------------------ Pruebas ------------------
if __name__ == "__main__":
    print(carlos_mayor_edad())              # True
    print(ricardo_tiene_cuenta())           # False
    print(bbva_tiene_clientes())            # True
    print(prestamas_es_banco())             # False
    print(tiene_100_pesos("Carlos"))  # True
    print(felipe_cliente_bbva())            # False
    print(bbva_prestamos_estudiantiles())   # False
    print(bbva_presta_carlos())             # True
    print(bbva_prestamo_hipotecario_carlos()) # True
    print(carlos_pidio_a_juan())            # False
