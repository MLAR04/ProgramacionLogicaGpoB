from base_conocimiento import respuestas_usuarios, respuestas_correctas, tema_pregunta, existe_respuesta
# Clausula de Horn:
# respuesta_correcta(pregunta) <- existe_respuesta(pregunta, respuesta) ^ no_es_incorrecta(pregunta, respuesta)
def buscar_respuesta(numero_pregunta):

    for (pregunta, respuesta) in existe_respuesta:
        # atomo: existe_respuesta(pregunta, respuesta)
        # Unificacion: pregunta == numero_pregunta
        if pregunta == numero_pregunta:
            # atomo: es_correcta(pregunta, respuesta)
            if (pregunta, respuesta) in respuestas_correctas:
                return respuesta
    return None
def buscar_respuesta_recursiva(pregunta, indice=0):
    # Caso base: fin de lista
    if indice >= len(existe_respuesta):
        return None

    # atomo: existe_respuesta(pregunta, respuesta)
    p, r = existe_respuesta[indice]

    # Unificacion: pregunta == p
    if p == pregunta:
        # atomo: es_correcta(pregunta, respuesta)
        if (p, r) in respuestas_correctas:
            return r

    # Llamada recursiva: avanzar al siguiente hecho
    return buscar_respuesta_recursiva(pregunta, indice + 1)

def necesita_apoyo(usuario):
    """
    Cláusula de Horn:
    necesita_apoyo(Usuario, Pregunta) ← respuesta(Usuario, Pregunta, R) ^ ¬es_correcta(Pregunta, R)
    """

    temas_refuerzo = []

    # Átomo: respuesta(Usuario, Pregunta, Respuesta)
    for usr, pregunta, respuesta in respuestas_usuarios:
        if usr == usuario:
            # Unificación: se verifica que el usuario actual sea el mismo que el consultado

            # Negación: se comprueba que la respuesta NO esté en las respuestas correctas
            es_correcta = any(
                p_correcta == pregunta and r_correcta == respuesta
                for p_correcta, r_correcta in respuestas_correctas
            )

            # Sustitución: se asignan los valores específicos de la pregunta y su tema
            if not es_correcta:
                for p, tema in tema_pregunta:
                    if p == pregunta:
                        temas_refuerzo.append(tema)

    return temas_refuerzo
def necesita_apoyo_recursivo(usuario, indice=0, temas_refuerzo=None):
    """
    Cláusula de Horn:
    necesita_apoyo(Usuario, Pregunta) ← respuesta(Usuario, Pregunta, R) ^ ¬es_correcta(Pregunta, R)

    Comentarios:
    - Átomo: respuesta(Usuario, Pregunta, R)
    - Negación: la respuesta del usuario no coincide con las correctas
    - Unificación: coincidencia por número de pregunta y usuario
    - Sustitución: asignar valores específicos de usuario y pregunta
    """
    if temas_refuerzo is None:
        temas_refuerzo = []

    # Caso base: llegamos al final de la lista de respuestas de usuarios
    if indice >= len(respuestas_usuarios):
        return temas_refuerzo

    usr, pregunta, respuesta = respuestas_usuarios[indice]

    if usr == usuario:  # Unificación: usuario coincide
        # Negación: la respuesta no coincide con las correctas
        es_correcta = any(
            p_correcta == pregunta and r_correcta == respuesta
            for p_correcta, r_correcta in respuestas_correctas
        )

        # Sustitución: asignamos tema de refuerzo si la respuesta es incorrecta
        if not es_correcta:
            for p, tema in tema_pregunta:
                if p == pregunta:
                    temas_refuerzo.append(tema)

    # Llamada recursiva: procesamos la siguiente respuesta
    return necesita_apoyo_recursivo(usuario, indice + 1, temas_refuerzo)



if __name__ == "__main__":
    pregunta = 6 # Sustitucion: pregunta
    resultado = buscar_respuesta(pregunta)
    print(f"Consulta: Cual es la respuesta a la pregunta {pregunta}?")
    print(f"La respuesta correcta de la pregunta {pregunta} es: {resultado}")

    pregunta_recursiva = 12  # Sustitucion: pregunta
    resultado_recursiva = buscar_respuesta_recursiva(pregunta_recursiva)
    print(f"Consulta: Cual es la respuesta a la pregunta {pregunta_recursiva}?")
    print(f"La respuesta correcta de la pregunta {pregunta_recursiva} es: {resultado_recursiva}")

    usuario = "usuario1"  # Sustitución: Usuario = usuario1
    print("Consulta: Que temas necesita reforzar?")
    temas = necesita_apoyo(usuario)
    if temas:
        print(f"El {usuario} necesita apoyo en los temas: {', '.join(temas)}")
    else:
        print(f"El {usuario} no necesita apoyo en ningun tema.")

    usuario_recursivo = "usuario2"  # Sustitución: Usuario = usuario2
    print("Consulta: Que temas necesita reforzar?")
    temas = necesita_apoyo(usuario_recursivo)
    if temas:
        print(f"El {usuario_recursivo} necesita apoyo en los temas: {', '.join(temas)}")
    else:
        print(f"El {usuario_recursivo} no necesita apoyo en ningun tema.")