#####################################################################################################
#   Con la base de conocimiento generada en clase, sobre enfermedades, los síntomas y las reglas.   #
#   Desarrolla el motor de inferencia en código en Python  que diagnostique la enfermedad con       #
#   base en los síntomas.                                                                           #
#####################################################################################################

# Definir primero el universo del motor de inferencia
enfermedades = {"Gripe": ["dolor de cabeza", "tos"],
                "Covid-19": ["fiebre", "tos", "cansancio"],
                "Migraña": ["dolor de cabeza", "nauseas"],
                "Resfriado": ["congestion nasal", "fiebre", "tos"]
                }

def definir_enfermedad(sintomas: list, base: dict):
    # definir primero si es posible encontrar una enfermedad
    if len(sintomas) < 2:
        return "No hay suficientes sintomas para diagnosticarte"
    
    # asigno los sintomas
    sintomas_paciente = set(sintomas)

    for enfermedad, sintoma_en_base in base.items():
        # comparar los sintomas del paciente con los de las enfermedades de la base
        if sintomas_paciente == set(sintoma_en_base):
            return enfermedad # mando la enfermedad disgnosticada
    
    # de lo contrario, puedo diagnosticar
    return "No se puede diagnosticar. Los síntomas no coinciden con ninguna enfermedad conocida."

    
if __name__ == '__main__':

    sintomas = []
    print("######################################################################")
    print("DETECTOR DE ENFERMEDADES (NOMAS TENEMOS 4 ESTABLECIDAS POR EL MOMENTO)")
    print("----------------------------------------------------------------------")
    print(" Nota: para salir del menu o si no tienes mas síntomas ingresa salir  ")
    while True:
        # pido ingresar los síntomas
        sintoma = input("Que síntoma que tienes: ")

        if sintoma.lower() == 'salir':
            break #continuo con el diagnostico
        else:
            sintomas.append(sintoma.lower())

    lista_de_sintomas = ", ".join(sintomas)
    print(f"Tus sintomas ingresados son {lista_de_sintomas} por ende: ")
    diagnostico = definir_enfermedad(sintomas, enfermedades)
    print(f"Tu resultado es: {diagnostico}")