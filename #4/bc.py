# Base de conocimiento (hechos)
enfermedades = {
    "gripe": ["tos", "dolor de cabeza"],
    "covid": ["fiebre", "tos", "cansancio", "perdida del olfato"],
    "migraña": ["dolor de cabeza", "nauseas"],
    "resfriado": ["congestión nasal", "tos", "fiebre"],
}

# Motor de inferencia
def diagnosticar(sintomas_usuario):
    for enfermedad, sintomas in enfermedades.items():
        if all(s in sintomas_usuario for s in sintomas) and len(sintomas_usuario) == len(sintomas):
            return f"Posible diagnóstico: {enfermedad.capitalize()}"
    return "No te puedo diagnosticar con esos síntomas."

if __name__ == "__main__":
    print("------Bienvenido al sistema de diagnóstico------")
    print("-> Conozco estas enfermedades:", ", ".join(enfermedades.keys()))
    print("-> Los síntomas que manejo son:", ", ".join({s for lista in enfermedades.values() for s in lista}))
    print("-------------------------------------------------")

    # Pedir síntomas al usuario
    sintomas_usuario = []
    while True:
        sintoma = input("Ingresa un síntoma (o escribe 'fin' para terminar): ").strip().lower()
        if sintoma == "fin":
            break
        sintomas_usuario.append(sintoma)

    print("\nTus síntomas ingresados fueron:", sintomas_usuario)

    # Diagnóstico
    resultado = diagnosticar(sintomas_usuario)
    print(resultado)
