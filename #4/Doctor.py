# Proyecto: Sistema de detección de enfermedades comunes
def main():
    enfermedades = {
        "gripe": ["tos","dolor de cabeza"], 
        "covid": ["fiebre","tos","cansancio","perdida del olfato"], 
        "migraña": ["dolor de cabeza","nauseas"],   
        "resfriado" : ["congestion nasal","fiebre","tos"]
    }

    # Solicitar sintomas
    usuario_sintomas = input("Ingrese sus sintomas separados por comas: ").lower().split(",")
    usuario_sintomas = [sintoma.strip() for sintoma in usuario_sintomas]
    diagnostico = []
    # Comparar 
    for enfermedad, sintomas in enfermedades.items():
        if all(sintoma in usuario_sintomas for sintoma in sintomas):
            diagnostico.append(enfermedad)
    #  resultado
    if diagnostico:
        print("Usted tiene esta enfermedad: " + ", ".join(diagnostico))
    else:
        print("No se pudo determinar una enfermedad con los sintomas proporcionados.")

if __name__ == "__main__":
    main()
