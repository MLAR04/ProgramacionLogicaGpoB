from universo import universo
# Lista con todos los síntomas únicos del universo
# opcion_sintomas = []
# for lista in universo.values():
#     for sintoma in lista:
#         if sintoma not in opcion_sintomas:
#             opcion_sintomas.append(sintoma)

opcion_sintomas = [
    "Tos",
    "Dolor de cabeza",
    "Fiebre",
    "Cansancio",
    "Perdida del olfato",
    "Nauseas",
    "Congestion nasal",
    "Ningun sintoma de los anteriores"
]

def diagnosticar():
    print("\nSelecciona los síntomas que tienes (ingresa los números separados por comas):\n")
    
    # Mostrar síntomas con índices
    for i, sintoma in enumerate(opcion_sintomas):
        print(f"{i+1}. {sintoma}")
    
    # Entrada del usuario
    eleccion = input("\nTus síntomas: ")
    entrada = eleccion.split(",")
    indices = []
    for x in entrada:               # recorre cada elemento de la lista
        numero = int(x.strip())     # quita espacios y lo convierte a entero
        indices.append(numero)

    # indices = [int(x.strip()) for x in eleccion.split(",")]

    # Convertir indices a síntomas seleccionados
    sintomas_usuario = [opcion_sintomas[i-1] for i in indices]
    
    # Revisar si coincide con alguna enfermedad
    for enfermedad, lista_sintomas in universo.items():
        if sorted(lista_sintomas) == sorted(sintomas_usuario):
            print(f"\nDiagnóstico: Tienes {enfermedad}.")
            return
    
    # Si no coincide con ninguna enfermedad exacta
    print("\nNo se puede diagnosticar.")

if __name__ == "__main__":
    diagnosticar()
