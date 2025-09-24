# Hechos
bancos = {
    "Banamex": {"tiene_dinero": True}  # Banamex es un banco y tiene dinero y esa es regla para que sea un banco
}

# Regla: todos los bancos deben tener dinero
def banco_tiene_dinero(nombre_banco):
    if nombre_banco in bancos and bancos[nombre_banco]["tiene_dinero"]:
        return True
    return False

# Consultas
print("¿Banamex tiene dinero?", banco_tiene_dinero("Banamex")) # Verdadera
print("¿Los bancos solo manejan dinero?", False) # Falsa
