from base_conocimiento import hechos
#primer ley que dice cada subtema pertenece a un tema 
# como consulta entonces tenemos que 
# pertenece(diseno_funciones, diseno_algoritmico)


#----------------PRIMERA CLAUSULA SIN RECURSIVIDAD-------------------------------------
# ley: si existe un  subtema → pertenece a un tema 
"""
def pertenece(subtema, tema, hechos):
    print(f'UNIFICACIÓN Y SUSTITUCIÓN\nsubtema buscado = {subtema}\ntema buscado = {tema}\n')

    lista_temas = list(hechos["temas"].keys())
    encontrado_tema = False  # Para verificar si el tema existe en los hechos

    # Recorre todos los temas
    for i, tema_actual in enumerate(lista_temas):
        print(f"Revisando tema[{i}] = '{tema_actual}'")
        
        # Si encontramos el tema que buscamos
        if tema_actual.lower() == tema.lower():
            encontrado_tema = True
            subtemas_actuales = hechos["temas"][tema_actual]["subtemas"]
            
            # Recorremos cada subtema dentro del tema actual
            for j, candidato in enumerate(subtemas_actuales):
                print(f"Comparando con subtema[{j}] = '{candidato}' ...")
                
                # Comparación insensible a mayúsculas
                if candidato.lower() == subtema.lower():
                    print(f"✔ Coincidencia encontrada: '{subtema}' pertenece a '{tema}'\n")
                    return True
            
            # Si se revisaron todos los subtemas del tema y no hay coincidencia
            print(f"✖ Se revisaron todos los subtemas de '{tema}' y no se encontró '{subtema}'.\n")
            return False

    # Si no se encontró el tema
    if not encontrado_tema:
        print(f"✖ El tema '{tema}' no se encuentra en la base de hechos.\n")
    return False

"""
#----------------PRIMERA CLAUSULA CON RECURSIVIDAD-------------------------------------
def pertenece(subtema, tema, hechos, i=0, j=0):
    """
    Busca si 'subtema' pertenece a 'tema' recorriendo uno por uno.
    - hechos: diccionario con la estructura esperada.
    - i: índice del tema que estamos revisando.
    - j: índice del subtema dentro del tema actual.
    """
    print(f'UNIFICACIÓN Y SUSTITUCIÓN\nsubtema buscado = {subtema}\ntema buscado = {tema}\n')
    
    # Lista de todos los nombres de tema
    lista_temas = list(hechos["temas"].keys())

    # Si ya revisamos todos los temas -> no pertenece
    if i >= len(lista_temas):
        print("No se encontró el tema en la base de hechos.\n")
        return False

    tema_actual = lista_temas[i]
    subtemas_actuales = hechos["temas"][tema_actual]["subtemas"]

    # Si el tema actual es el tema que buscamos (comparación insensible a mayúsculas)
    if tema_actual.lower() == tema.lower():
        # Si ya revisamos todos los subtemas del tema actual -> no pertenece
        if j >= len(subtemas_actuales):
            print(f"Se revisaron todos los subtemas de '{tema}' y no se encontró '{subtema}'.\n")
            return False

        candidato = subtemas_actuales[j]
        print(f"Comparando con subtema[{j}] = '{candidato}' ...")

        # Comparación insensible a mayúsculas
        if candidato.lower() == subtema.lower():
            print(f"Coincidencia encontrada: '{subtema}' pertenece a '{tema}'\n")
            return True
        else:
            # Avanzamos al siguiente subtema del mismo tema
            return pertenece(subtema, tema, hechos, i, j + 1)
    else:
        # No es el tema buscado: avanzamos al siguiente tema y reiniciamos j a 0
        return pertenece(subtema, tema, hechos, i + 1, 0)


#--------------------SEGUNDA CLAUSULA SIN RECURSIVIDAD----------------------------------------------------------------
"""
def verificar_respuesta(usuario, pregunta, respuesta, tema, hechos):
    print(f"UNIFICACIÓN Y RESOLUCIÓN SLD\nUsuario = {usuario}\nTema = {tema}\n")
    print(f"Consulta: ¿La respuesta del usuario para '{pregunta}' es correcta?\n")

    respuestas_correctas = hechos["respuestas_correctas"]

    # Paso 1: Verificar si la pregunta existe en la base de conocimiento
    if pregunta not in respuestas_correctas:
        print(f"✖ La pregunta '{pregunta}' no existe en la base de conocimiento.\n")
        print(f"Por tanto, necesita_reforzar({usuario}, '{tema}')\n")
        return False

    # Paso 2: Unificación de la respuesta del usuario con la respuesta correcta
    respuesta_correcta = respuestas_correctas[pregunta]

    print(f"Comparando respuestas:")
    print(f"  → Usuario: '{respuesta}'")
    print(f"  → Correcta: '{respuesta_correcta}'")

    if respuesta.strip().lower() == respuesta_correcta.strip().lower():
        print("✔ Coincidencia encontrada.")
        print(f"Por tanto, ¬necesita_reforzar({usuario}, '{tema}')\n")
        return True
    else:
        print("✖ No coincide con la respuesta correcta.")
        print(f"Por tanto, necesita_reforzar({usuario}, '{tema}')\n")
        return False
"""
#---------------SEGUNDA CLAUSULA CON RECURSIVIDAD----------------------------------------------------
def verificar_respuesta(usuario, pregunta, respuesta, tema, hechos, i=0):
    """
    Verifica recursivamente si la respuesta del usuario coincide con la correcta.
    """
    respuestas_correctas = list(hechos["respuestas_correctas"].items())

    # Caso base: ya revisamos todas las preguntas y no hay coincidencia
    if i >= len(respuestas_correctas):
        print(f"✖ No se encontró la pregunta '{pregunta}' en la base de conocimiento.\n")
        print(f"Por tanto, necesita_reforzar({usuario}, '{tema}')\n")
        return False

    pregunta_actual, respuesta_correcta = respuestas_correctas[i]

    print(f"UNIFICACIÓN Y RESOLUCIÓN SLD - Paso {i+1}")
    print(f"Comparando pregunta actual: '{pregunta_actual}'")

    # Si la pregunta actual coincide con la buscada
    if pregunta_actual.lower() == pregunta.lower():
        print(f"  → Usuario: '{respuesta}'")
        print(f"  → Correcta: '{respuesta_correcta}'")

        # Unificación de respuesta
        if respuesta.strip().lower() == respuesta_correcta.strip().lower():
            print("Coincidencia encontrada.")
            print(f"  Por tanto, no necesita_reforzar({usuario}, '{tema}')\n")
            return True
        else:
            print("  ✖ No coincide con la respuesta correcta.")
            print(f"  Por tanto, necesita_reforzar({usuario}, '{tema}')\n")
            return False

    # Si no es la pregunta buscada, pasa a la siguiente (recursión)
    return verificar_respuesta(usuario, pregunta, respuesta, tema, hechos, i + 1)

#-------------------------------------------------------------------------------------------
if __name__ == '__main__':
    
    print(pertenece("Conceptos básicos", "diseño algoritmico", hechos),"\n")
    print(verificar_respuesta("usuario", "representacion", "Pseudocódigo", "Diseño de Algoritmos", hechos))