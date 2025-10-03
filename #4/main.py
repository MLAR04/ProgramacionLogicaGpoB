enfermedades:dict = {
    "Gripe": {"Tos":0, "Dolor de cabeza":0},
    "COVID": {"Fiebre":0, "Tos":0, "Cansancio":0, "Perdida de olfato":0},
    "Migraña": {"Dolor de cabeza":0, "Nauseas":0},
    "Resfriado": {"Congestión Nasal":0, "Fiebre":0, "Tos":0},
}

def checar_sintomas(sintomas: list) -> None:
    for sintoma in sintomas:
        for enfermedad in enfermedades:
            if sintoma in enfermedades[enfermedad]:
                enfermedades[enfermedad][sintoma] = 1

def diagnostico() -> list:
    enfermedad_diagnosticada:list = []
    for enfermedad, sintomas in enfermedades.items():
        if all(valor == 1 for valor in sintomas.values()):
            enfermedad_diagnosticada.append(enfermedad)
    return enfermedad_diagnosticada


def cli(sintomas: list) -> None:
    sintomas_a_mantener = []
    for sintoma in sintomas:
        respuesta = input(f"¿Tienes {sintoma}? (s/n): ").lower()
        if respuesta not in ["n", "no"]:
            sintomas_a_mantener.append(sintoma)
    return sintomas_a_mantener

if __name__ == "__main__":
    sintomas: list = ["Tos", "Dolor de cabeza", "Fiebre", "Cansancio", "Perdida de olfato", "Nauseas", "Congestión Nasal"]

    sintomas = cli(sintomas)
    checar_sintomas(sintomas)

    enfermedad:list = diagnostico() 
    if len(enfermedad):
        print(f"Se ha diagnosticado: {enfermedad}")
    else:
        print("No se ha diagnosticado ninguna enfermedad")
