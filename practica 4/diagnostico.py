from base_conocimiento import enfermedades

def diagnosticar(sintomas):
    posibles_enfermedades = []
    for enfermedad in enfermedades:
        if all(sintoma in sintomas for sintoma in enfermedades[enfermedad]):
            posibles_enfermedades.append(enfermedad)
    return posibles_enfermedades

if __name__ == "__main__":
    sintomas_usuario = input("Ingrese sus síntomas separados por comas: ").split(",")
    sintomas_usuario = [sintoma.strip() for sintoma in sintomas_usuario]
    resultado = diagnosticar(sintomas_usuario)
    if resultado:
        print("Posibles enfermedades:", ", ".join(resultado))
    else:
        print("No se pudo determinar una enfermedad con los síntomas proporcionados.")

