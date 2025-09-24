# Hechos
clientes_banco = {
    "Brandon": {"edad": 21}  
}

# Regla: un cliente de banco debe ser mayor de edad
def es_mayor_de_edad_banco(nombre):
    if nombre in clientes_banco and clientes_banco[nombre]["edad"] >= 18:
        return True
    return False

# Consultas
print("Brandon es mayor de edad?", es_mayor_de_edad_banco("Brandon"))  # Verdadera
print("Brandon es cliente de un mercado?", False) # Falsa 
