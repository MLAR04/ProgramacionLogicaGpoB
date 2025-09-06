hechos = {
    "clientes": ["Juan"],
    "bancos": ["Azteca"],
    "cuentas": [("Juan", "Azteca")],
    "prestamos": {
        "Juan": "Hipotecario"
    },
    "montos": {
        "Juan": 20000
    }
}
# Reglas
def puede_generar_prestamo(cliente):
    for c, b in hechos["cuentas"]:
        if c == cliente:
            return True
    return False

# Consultas
def tipo_prestamo(cliente):
    if cliente in hechos["prestamos"]:
        return hechos["prestamos"][cliente]
    else:
        return "No tiene préstamo registrado"

def monto_recibido(cliente):
    if cliente in hechos["montos"]:
        return hechos["montos"][cliente]
    else:
        return "No tiene monto registrado"

print("Hecho: Juan es un cliente del banco Azteca")
print("Regla: Juan puede generar un préstamo" if puede_generar_prestamo("Juan") else "Juan no puede generar un préstamo")

# Consultas
print(f"¿Qué tipo de préstamo tiene Juan? -> {tipo_prestamo('Juan')}")
print(f"¿Cuánto dinero recibió Juan del préstamo? -> {monto_recibido('Juan')}")
