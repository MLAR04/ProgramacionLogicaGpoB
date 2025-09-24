# Hechos
cuentas_banco = {
    "Alexia": ["BBVA"]  # Alexia tiene cuenta en BBVA
}

edades = {
    "Alexia": 10  # Alexia es mayor de edad (Le puse 10 para comprobar el programa)
}

# Regla: verificar si Alexia es mayor de edad
def es_mayor(nombre):
    return edades.get(nombre, 0) >= 18

# Consultas
print("Alexia es mayor de edad?", es_mayor("Alexia")) # Verdadera
print("Alexia tiene una cuenta en Santander?", "Santander" in cuentas_banco.get("Alexia", []))  # Falsa
