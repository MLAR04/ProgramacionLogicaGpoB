def sistema_experto():
    print("=== Sistema de Detección de Enfermedades Comunes ===\n")
 


    sintomas = {}
    sintomas["tos"] = input("¿Tienes tos? ").strip().lower() == "si"
    sintomas["dolor_cabeza"] = input("¿Tienes dolor de cabeza? ").strip().lower() == "si"
    sintomas["fiebre"] = input("¿Tienes fiebre? ").strip().lower() == "si"
    sintomas["cansancio"] = input("¿Tienes cansancio? ").strip().lower() == "si"
    sintomas["perdida_olfato"] = input("¿Has perdido el olfato? ").strip().lower() == "si"
    sintomas["nauseas"] = input("¿Tienes náuseas? ").strip().lower() == "si"
    sintomas["congestion_nasal"] = input("¿Tienes congestión nasal? ").strip().lower() == "si"

    # Reglas de inferencia
    enfermedad = None

    if sintomas["tos"] and sintomas["dolor_cabeza"]:
        enfermedad = "Gripe"
    elif sintomas["fiebre"] and sintomas["tos"] and sintomas["cansancio"] and sintomas["perdida_olfato"]:
        enfermedad = "Covid"
    elif sintomas["dolor_cabeza"] and sintomas["nauseas"]:
        enfermedad = "Migraña"
    elif sintomas["congestion_nasal"] and sintomas["fiebre"] and sintomas["tos"]:
        enfermedad = "Resfriado"


    if enfermedad:
        print(f"\n Segun los síntomas, Tienes la siguiente enfermedad: {enfermedad}")
    else:
        print("\n No se pudo determinar la enfermedad con los sintomas dados.")



if __name__ == "__main__":
    sistema_experto()
