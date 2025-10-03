enfermedades = {
    "Gripa": ["Tos", "Dolor de garganta"],
    "Covid": ["Fiebre", "Tos", "Cansancio", "Perdida del olfato"],
    "Migraña": ["Dolor de cabeza", "Nauseas"],
    "Resfriado": ["Congestion nasal", "Fiebre", "Tos"]
}

def diagnosticar_enfermedad(sintomas):
    posible_enfermedad = []
    for enfermedad, sintomas_enfermedad in enfermedades.items():
        if all(sintoma in sintomas for sintoma in sintomas_enfermedad):
            posible_enfermedad.append(enfermedad)

    if not posible_enfermedad:
        return "No se pudo determinar una enfermedad con los sintomas proporcionados."
    return posible_enfermedad

if __name__ == "__main__":
    while True:
        print("Bienvenido al minisistema de diagnostico de enfermedades")
        print("A continuacion le preguntaré por sus sintomas")
        sintomas_usuario = []
        print("¿Tiene tos? (si/no)")
        input_tos = input().strip().lower()
        if input_tos == "si":
            sintomas_usuario.append("Tos")
        print("¿Tiene dolor de garganta? (si/no)")
        input_dolor_garganta = input().strip().lower()
        if input_dolor_garganta == "si":
            sintomas_usuario.append("Dolor de garganta")
        print("¿Tiene fiebre? (si/no)")
        input_fiebre = input().strip().lower()
        if input_fiebre == "si":
            sintomas_usuario.append("Fiebre")
        print("¿Tiene cansancio? (si/no)")
        input_cansancio = input().strip().lower()
        if input_cansancio == "si":
            sintomas_usuario.append("Cansancio")
        print("¿Tiene perdida del olfato? (si/no)")
        input_perdida_olfato = input().strip().lower()
        if input_perdida_olfato == "si":
            sintomas_usuario.append("Perdida del olfato")
        print("¿Tiene dolor de cabeza? (si/no)")
        input_dolor_cabeza = input().strip().lower()
        if input_dolor_cabeza == "si":
            sintomas_usuario.append("Dolor de cabeza")
        print("¿Tiene nauseas? (si/no)")
        input_nauseas = input().strip().lower()
        if input_nauseas == "si":
            sintomas_usuario.append("Nauseas")
        print("¿Tiene congestion nasal? (si/no)")
        input_congestion_nasal = input().strip().lower()
        if input_congestion_nasal == "si":
            sintomas_usuario.append("Congestion nasal")
        
        print("Con base en sus sintomas, usted podria tener:"+diagnosticar_enfermedad(sintomas_usuario).__str__())
        print("¿Desea realizar otro diagnostico? (si/no)")
        input_otro_diagnostico = input().strip().lower()
        if input_otro_diagnostico != "si":
            print("Gracias por usar el minisistema de diagnostico de enfermedades. ¡Hasta luego!")
            break