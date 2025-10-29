# Proyecto: Sistema de Evaluación de Conocimientos

## Equipo
**Nombre del equipo:** Educación

## Descripción
Este proyecto tiene como objetivo implementar un sistema de conocimiento basado en reglas (cláusulas de Horn) para evaluar si un usuario necesita reforzar ciertos temas en función de sus respuestas a preguntas específicas.

---

## Hechos
Se definen los temas, subtemas y las respuestas correctas para las preguntas correspondientes:

```python
hechos = {
    "temas": {
        "diseño algoritmico": {
            "subtemas": ["Conceptos básicos", "Diseño de algoritmos"]
        },
        "Introducción a la Programación": {
            "subtemas": ["Conceptos básicos de programación", "Estructura básica de un programa"]
        }
    },
    "respuestas_correctas": {
        "algoritmo": "Una receta paso a paso para resolver un problema",
        "representacion": "Diagramas de flujo",
        "estructura": "Uso de condicionales y ciclos"
    }
}
reglas = [
    # Regla 1: Para todo tema existe al menos un subtema
    "subtema(X, T) -> tema(T)",

    # Regla 2: Si existe un subtema, entonces pertenece a un tema
    "subtema(X, T) -> pertenece(X, T)",

    # Regla 3: Existe una sola respuesta correcta para cada pregunta
    "respuesta_correcta(P, R) -> unica_respuesta(P)",

    # Regla 4: Si la respuesta del usuario no coincide con la correcta, entonces es incorrecta
    "respuesta(usuario, P, R1) ∧ respuesta_correcta(P, R2) ∧ R1 ≠ R2 -> incorrecta(usuario, P)",

    # Regla 5: Si una respuesta es incorrecta, entonces el usuario necesita reforzar el tema correspondiente
    "incorrecta(usuario, P) -> necesita_reforzar(usuario, T)",

    # Regla 6: Si el usuario responde correctamente todas las preguntas, entonces no necesita refuerzo en el tema
    "respuesta(usuario, P, R) ∧ respuesta_correcta(P, R) -> ¬necesita_reforzar(usuario, T)"
]
