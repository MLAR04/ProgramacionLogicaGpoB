#############################################################################
#                                                                           # 
#   Resolución SLD (Selective Linear Definite-clause resolution) en Python  #
#                                                                           #
#############################################################################

#############################################################################
#                                                                           #
#   Una pregunta X es del tema Y SI existe un subtema Z tal que la pregunta #  
#   X pertenece al subtema Z Y el subtema Z pertenece al tema Y             #
#                                                                           #
#       pregunta_es_del_tema(X, Y) -> pregunta(Z, X) subtema(Y, Z)          #
#                                                                           #
#############################################################################

from hechos import PREGUNTAS, SUBTEMAS, RESPUESTAS_CORRECTAS

def pregunta_es_del_tema(p:str, t:str, i = 0):

    #           SIN RECURSIVIDAD
    # for subtema, _pregunta in PREGUNTAS:
    #     if _pregunta == pregunta:                     
    #         for _tema, sub in SUBTEMAS:
    #             if _tema == tema and sub == subtema:
    #                 return True
    # return False

    if i >= len(PREGUNTAS):
        return False
    
    subtema, pregunta = PREGUNTAS[i]
    if p == pregunta:
        if checar_subtemas(t, subtema):
            return True
    return pregunta_es_del_tema(p, t, i + 1)

def checar_subtemas(t: str, sub_buscar: str, i=0):
    if i >= len(SUBTEMAS):
        return False
    
    tema, s = SUBTEMAS[i]

    if t == tema and sub_buscar == s:
        return True
    return checar_subtemas(t, sub_buscar, i + 1)

def unificacion(pregunta: str, t: str, i = 0):
    #           SIN RECURSIVIDAD
    # for subtema, _pregunta in PREGUNTAS:
    #     if _pregunta == pregunta:
    #         Z = subtema
    #         for _tema, sub in SUBTEMAS:
    #             if _tema == tema and sub == Z:
    #                 return {"X": pregunta, "Y": tema, "Z": Z}
    # return None

    if i >= len(PREGUNTAS):
        return None
    
    subtema, p = PREGUNTAS[i]
    
    if pregunta == p:
        Z = subtema
        resultado = buscar_unificacion_subtemas(pregunta, t, Z, 0)
        if resultado:
            return resultado
    
    return buscar_unificacion_preguntas(pregunta, t, i + 1)

def buscar_unificacion_subtemas(pregunta: str, t: str, Z: str, i=0):
    if i >= len(SUBTEMAS):
        return None
    
    tema, sub = SUBTEMAS[i]
    
    if t == tema and sub == Z:
        return {"X": pregunta, "Y": t, "Z": Z}
    
    # Caso recursivo: siguiente subtema
    return buscar_unificacion_subtemas(pregunta, tema, Z, i + 1)


#############################################################################
#                                                                           #
#  Verifica si la respuesta es igual a respuesta correcta                   #
#  para la pregunta dada                                                    #
#       pregunta_es_correcta(P, R) :- respuesta_correcta(P, RC), R = RC     #
#                                                                           #
#############################################################################

def pregunta_es_correcta(pregunta: str, respuesta: str, i = 0) -> bool:
    if i >= len(RESPUESTAS_CORRECTAS):
        return False

    p, r_correcta = RESPUESTAS_CORRECTAS[i]

    if p == pregunta:
        return r_correcta == respuesta
    return pregunta_es_correcta(pregunta, respuesta, i + 1)

def obtener_respuesta_correcta(pregunta: str, i = 0) -> str:
    if i >= len(RESPUESTAS_CORRECTAS):
        return None
    
    p, r_correcta = RESPUESTAS_CORRECTAS[i]
    
    if p == pregunta:
        return r_correcta
    
    return obtener_respuesta_correcta(pregunta, i + 1)

def unificacion_respuesta(pregunta: str, respuesta: str, i=0):
    if i >= len(RESPUESTAS_CORRECTAS):
        return None
    
    p, r_correcta = RESPUESTAS_CORRECTAS[i]
    
    # Unificar: P = pregunta, RC = r_correcta, R = respuesta
    if p == pregunta:
        if r_correcta == respuesta:
            return {
                'P': pregunta,
                'R': respuesta,
                'RC': r_correcta
            }
        else:
            return None
    
    return unificacion_respuesta(pregunta, respuesta, i + 1)

if __name__ == '__main__':
    print(pregunta_es_del_tema("¿Qué es un algoritmo?", "Diseño algoritmico"))
    print(unificacion("¿Qué es un algoritmo?", "Diseño algoritmico"))
    print(pregunta_es_correcta("¿Qué es un algoritmo?", "Una receta paso a paso para resolver un problema"))
    print(unificacion_respuesta("¿Qué es un algoritmo?", "Una receta paso a paso para resolver un problema"))

