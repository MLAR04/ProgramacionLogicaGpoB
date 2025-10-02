from typing import List

lista_sintomas: List[str] = ["tos", "dolor de cabeza", "fiebre", "cansansio", "perdida del olfato", "migrania", "nauseas", "congestion nasal"]
lista_enfermedades: List[str] = ["gripe", "covid", "migraña", "resfriado"]

lista_enfermedad_sintomas: List[List[int]] = [
    [1, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 0, 0, 1],
]

def escribir_lista_sintomas():
    for sintoma in lista_sintomas:
        print(sintoma, end=", ")
    print("\n")

def realizar_pregunta(enfermedades_posibles: List[int] , revision_sintomas: List[int]) -> int:
    #si solo queda una enfermedad posible y ya revise los sintomas que cuenta esta enfermedad
    if len(enfermedades_posibles) == 1:
        #obtener lista de indices de sintomas que tiene la enfermedad que NO has sido preguntados y que si cuenta la enfermedad con estos sintomas

        ind_enfermedad_detectada: int = enfermedades_posibles[0]

        for i in range(len(revision_sintomas)):

            if lista_enfermedad_sintomas[ind_enfermedad_detectada][i] == 1 and revision_sintomas[i] == -1:
                revision_sintomas[i] = preguntar_sintoma(lista_sintomas[i])

                if revision_sintomas[i] == 0:
                    print("El diagnóstico es: No se pudo determinar un diagnóstico con los síntomas proporcionados.")
                    return -1
            
                return realizar_pregunta(enfermedades_posibles, revision_sintomas)

    #si ya no hay enfermedades posibles
    if len(enfermedades_posibles) == 0:
        print("No se pudo determinar un diagnóstico con los síntomas proporcionados.")
        return -1

    #buscar un sintoma que preguntar
    # El sintoma seleccionado sera 1.Sabemos que es -1  2.Es distinto en almenos una enfermedad
    
    for i in range(len(revision_sintomas)):
        if revision_sintomas[i] == -1: #sintoma no revisado
            #verificar si es distinto en almenos una enfermedad
            distinto: bool = distincion_es_distinto(enfermedades_posibles, i)
            
            # si si es distinto, preguntar por el sintoma
            if distinto:
                #preguntar por el sintoma
                revision_sintomas[i] = preguntar_sintoma(lista_sintomas[i])

                #filtrar enfermedades posibles
                enfermedades_posibles: List[int] = filtrar_enfermedades(enfermedades_posibles, i, revision_sintomas[i])

                filtrar_enfermedades(enfermedades_posibles, i, revision_sintomas[i])
                return realizar_pregunta(enfermedades_posibles, revision_sintomas)


    return enfermedades_posibles[0]

#recibe un indice de sintoma y una lista de enfermedades posibles, revisa que el sintoma no es igual en todas las enfermedades
def distincion_es_distinto(enfermedades_posibles: List[int], indice_sintoma: int) -> bool:
    valor: int = lista_enfermedad_sintomas[enfermedades_posibles[0]][indice_sintoma]

    for enfermedad_posible in (enfermedades_posibles):
        if lista_enfermedad_sintomas[enfermedad_posible][indice_sintoma] != valor:
            return True
    return False

def preguntar_sintoma(sintoma: str) -> int:
    respuesta = input(f"¿Cuenta con el síntoma {sintoma}? (S/N): ").strip().upper()
    if respuesta == 'S':
        return 1
    elif respuesta == 'N':
        return 0
    else:
        print("Respuesta no válida. Por favor responda con S o N.")
        return preguntar_sintoma(sintoma)

# Filtra la lista de enfermedades posibles según la respuesta del usuario, 1 es las enfermedades, posibles, 2 es el indice del sintoma y 3 si tiene o no el sintoma
def filtrar_enfermedades(enfermedades_posibles: List[int], sintoma_index: int, tiene_sintoma: int) -> List[int]:
    nuevas_enfermedades_posibles: List[int] = []
    for enfermedad in enfermedades_posibles:
        if lista_enfermedad_sintomas[enfermedad][sintoma_index] == tiene_sintoma:
            nuevas_enfermedades_posibles.append(enfermedad)
    return nuevas_enfermedades_posibles

if __name__ == "__main__":
    print("Bienvenido al sistema de diagnóstico de enfermedades")
    print("Responda si cuenta con los siguientes síntomas, un S para si y un N para no")

    #lista que representa las enfermedades que puede tener el usuario
    enfermedades_posibles: List[int] = list(range(len(lista_enfermedades)))
    revision_sintomas: List[int] = [-1]*len(lista_sintomas)

    #Iniciar bucle
    enfermedad_detectada: int = realizar_pregunta(enfermedades_posibles, revision_sintomas)

    if enfermedad_detectada != -1:
        print(f"El diagnóstico es: {lista_enfermedades[enfermedad_detectada]}")

