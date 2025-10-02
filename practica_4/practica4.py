from universo import enfermedades

def diagnostico():
    sintomas = {
        'a': 'fiebre',
        'b': 'tos',
        'c': 'dolor de cabeza',
        'd': 'cansancio',
        'e': 'perdida del olfato',
        'f': 'náuseas',
        'g': 'congestión nasal'
    }

    print("Selecciona los síntomas que presentas: ")
    print("a. Fiebre")
    print("b. Tos") 
    print("c. Dolor de cabeza") 
    print("d. Cansancio") 
    print("e. Pérdida del olfato") 
    print("f. Náuseas") 
    print("g. Congestión nasal")
    entrada = input("Escribe las letras de los síntomas separados por comas: ").lower()
    entrada = entrada.replace(" ", "").split(",")

    invalidas = []
    for letra in entrada:
        if letra not in sintomas:
            invalidas.append(letra)

    if invalidas:
        print("Opciones no disponibles:", ", ".join(invalidas))
        print("favor de ingresar opciones válidas")
        return diagnostico()
    
    
    seleccion = []
    for letra in entrada:
        seleccion.append(sintomas[letra])

    enfermedad_encontrada = []
    for enfermedad, lista_sintomas in enfermedades.items():
        if set(seleccion) == set(lista_sintomas):
            enfermedad_encontrada.append(enfermedad)

    if enfermedad_encontrada:
        print("Tienes la siguiente enfermedad:", ", ".join(enfermedad_encontrada))
    else:
        print("No se puede diagnosticar")

if __name__ == '__main__':
    diagnostico()
