from universo import Respuestas_incorrectas

def buscar_valores(respuesta, valores, i=0):
    if i >= len(valores):
        return False
    if respuesta == valores[i]:
        return True
    return buscar_valores(respuesta, valores, i + 1)


def es_incorrecta(respuesta, index=0):
    if index >= len(Respuestas_incorrectas):
        return False
    _, valores = Respuestas_incorrectas[index]
    if buscar_valores(respuesta, valores):
        return True
    return es_incorrecta(respuesta, index + 1)

def respuesta_incorrecta(respuesta):
    if es_incorrecta(respuesta):
        return f"La respuesta '{respuesta}' es incorrecta"
    else:
        return f"La respuesta '{respuesta}' es correcta"

def pertenece_a_tema(subtema, index=0):
    if index >= len(Respuestas_incorrectas):
        return False
    campo, valores = Respuestas_incorrectas[index]
    if subtema == campo or buscar_valores(subtema, valores):
        return True
    return pertenece_a_tema(subtema, index + 1)

def subtema_afirmativo(subtema):
    if pertenece_a_tema(subtema):
        return f"El subtema '{subtema}' pertenece a un tema"
    else:
        return f"El subtema '{subtema}' no pertenece a ningún tema"
