
# Definición de enfermedades y sus síntomas (hechos)
Gripe = {"tos", "dolor de cabeza"}
Covid = {"fiebre", "tos", "cansancio", "perdida del olfato"}
Migraña = {"dolor de cabeza", "nauseas"}
Resfriado = {"congestion nasal", "fiebre", "tos"}

# base de conocimiento
enfermedades = {
    "Gripe": Gripe,
    "Covid": Covid,
    "Migraña": Migraña,
    "Resfriado": Resfriado
}


def sintomas_diagnostico(sintomas_usuario):
    
    #se compara los síntomas del usuario con la base de conocimiento. y devuelve los diagnósticos posibles.
    diagnosticos = []

    for enfermedad, sintomas in enfermedades.items():
        if sintomas.issubset(sintomas_usuario):
            diagnosticos.append(enfermedad)

    return diagnosticos



if __name__ == "__main__":
    print("que sintomas tiene?:")
    print(" tos, dolor de cabeza, fiebre, cansancio, perdida del olfato, nauseas, congestion nasal")

    entrada = input("ingrese todos sus sintomas separados por comas ").lower()
    sintomas_usuario = {s.strip() for s in entrada.split(",")}

    # se ejecuta el motor 
    resultado = sintomas_diagnostico(sintomas_usuario)


    if resultado:
        print("tu diagnostico es:", ", ".join(resultado))
    else:
        print("no se puede responder")
