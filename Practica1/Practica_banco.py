# --- Datos ---
hecho = {
    "bbva": {
        "juan": {"prestamo": 5000, "tipo": "vehicular"}
    },
    "banamex": {
        "manuel": {"prestamo": 100, "tipo": "hipotecario"}
    }
}

# --- Reglas ---

# "X" es un cliente
def es_cliente(x):
    for banco in hecho:
        if x in hecho[banco]:
            print(f'{x} es cliente de {banco}')
            return True
    print(f'{x} no es cliente en ningún banco del sistema')
    return False

# "Y" es un banco
def es_banco(y):
    if y in hecho:
        clientes = len(hecho[y])
        print(f'el banco {y} existe y tiene {clientes} cliente(s).')
        return True
    print(f'el banco {y} no está registrado en el sistema')
    return False

# "X" tiene una cuenta en el banco "Y"
def tiene_cuenta(x, y):
    if y in hecho and x in hecho[y]:
        print(f'el cliente {x} tiene una cuenta en el banco {y}')
        return True
    print(f'el cliente {x} no tiene cuenta en el banco {y}')
    return False

# "Y" puede generar un préstamo de tipo "W"
def tipo_prestamo(y, w):
    if y in hecho:
        for cliente in hecho[y]:
            if hecho[y][cliente]["tipo"] == w:
                print(f'el banco {y} maneja préstamos de tipo {w}')
                return True
        print(f'el banco {y} no maneja préstamos de tipo {w}')
        return False
    else:
        print(f'el banco {y} no existe en el sistema')
        return False

# "X" recibió un monto "Z" de dinero en el banco "Y"
def tiene_prestamo(x, y, z):
    if y in hecho and x in hecho[y]:
        if hecho[y][x]["prestamo"] == z:
            print(f'el cliente {x} recibió ${z} en el banco {y} (tipo {hecho[y][x]["tipo"]})')
            return True
        else:
            print(f'el cliente {x} tiene un préstamo en {y}, pero no por ${z}')
            return False
    print(f'el cliente {x} no tiene préstamo en el banco {y}')
    return False


# --- Consultas ---
if __name__ == '__main__':
    print("\n--- CONSULTAS ---\n")
    print(es_cliente("juan"))      # Verdadero
    print(es_cliente("roberto"))   # Falso

    print(es_banco("bbva"))        # Verdadero
    print(es_banco("hsbc"))        # Falso

    print(tiene_cuenta("juan", "bbva"))     # Verdadero
    print(tiene_cuenta("juan", "banamex"))  # Falso

    print(tipo_prestamo("banamex", "hipotecario")) # Verdadero
    print(tipo_prestamo("bbva", "hipotecario"))    # Falso

    print(tiene_prestamo("manuel", "banamex", 100))   # Verdadero
    print(tiene_prestamo("juan", "bbva", 2000))       # Falso

