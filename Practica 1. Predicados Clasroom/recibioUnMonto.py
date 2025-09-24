# Hechos
dinero_recibido = {
    "Alexia": {"monto": "muy grande", "tipo": "general"}  # Alexia recibió  dinero, tipo general. Aqui hay un detalle con los tipos
#En la consulta falsa puse que recibio dolares, pero en los hechos y en las reglas nunca mencione tipo de moneda
#Pero ya lo tenia entregado en escrito
}

# Regla: alguien le dio dinero a Alexia
def le_dieron_dinero(nombre):
    #Retorna verdadero si si encuentra el nombre en el diccionario y si y solo si el monto que recibio no sea cero
    return nombre in dinero_recibido and dinero_recibido[nombre]["monto"] != 0

# Consultas
print("Alexia ya tiene dinero?", le_dieron_dinero("Alexia"))  # Verdadera
print("Alexia recibió dolares?", dinero_recibido["Alexia"]["tipo"] == "dolares")  # Falsa
