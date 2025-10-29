# Programacion logica SLD

Este proyecto implementa un sistema de **validación de respuestas y subtemas** basado en **programación lógica**, usando **tuplas y recursión** en Python. Permite determinar si una respuesta es incorrecta o si un subtema pertenece a algún tema/categoría, devolviendo mensajes afirmativos.



## Estructura del proyecto




## Archivo Universo.py

Contiene la tupla `Respuestas_incorrectas`, que actúa como **universo de hechos**:

```python
Respuestas_incorrectas = (
    ("algoritmo", ("Un error de sintaxis", "Un lenguaje de programación", "Una estructura de datos")),
    ("representacion", ("Tablas de verdad", "Código binario", "Estructuras de control")),
    ("primer_paso", ("Codificarlo en C", "Probarlo directamente", "Hacer un diagrama UML")),
    ("funcion", ("Una variable que almacena datos", "Un error en tiempo de ejecución", "Una estructura de bucle")),
    ("programar", ("Jugar videojuegos", "Diseñar hardware", "Traducir textos")),
    ("caracteristica", ("Son ambiguos", "No requieren reglas", "Sólo funcionan en una computadora específica")),
    ("estructura", ("Inclusión de librerías", "Declaración de funciones", "Ejecución del main()")),
    ("literal", ("x", "int", "scanf")),
    ("compilador", ("Diseña interfaces gráficas", "Ejecuta directamente el programa", "Revisa el hardware del sistema")),
    ("secuencial", ("La repetición de bloques", "La toma de decisiones condicional", "La recursión")),
    ("selectiva", ("for", "while", "do-while")),
    ("iterativa", ("if", "switch", "return")),
    ("arreglo", ("Una variable que almacena un solo valor", "Una función matemática", "Un bucle infinito")),
    ("unidimensional", ("Tiene más de una fila y columna", "Es una función", "Solo acepta caracteres")),
    ("bidimensional", ("Almacenar un solo número", "Definir variables", "Controlar el flujo")),
    ("struct", ("Repetir instrucciones", "Traducir código", "Ejecutar bucles")),
    ("modulo", ("Un archivo de configuración del sistema", "Un ciclo infinito", "Una variable global")),
    ("parametros", ("Evitar errores de sintaxis", "Hacer que el programa se detenga", "Evitar el uso de funciones")),
    ("implementacion", ("Traducirlo a otro lenguaje", "Borrarlo del sistema", "Ejecutarlo sin definirlo"))
)


from Universo import Respuestas_incorrectas

# Función recursiva para buscar en los valores de una categoría
def buscar_valores(respuesta, valores, i=0):
    if i >= len(valores):
        return False
    if respuesta == valores[i]:
        return True
    return buscar_valores(respuesta, valores, i + 1)

# Determina si una respuesta es incorrecta
def es_incorrecta(respuesta, index=0):
    if index >= len(Respuestas_incorrectas):
        return False
    campo, valores = Respuestas_incorrectas[index]
    if buscar_valores(respuesta, valores):
        return True
    return es_incorrecta(respuesta, index + 1)

def respuesta_incorrecta(respuesta):
    if es_incorrecta(respuesta):
        return f"La respuesta '{respuesta}' es incorrecta"
    else:
        return f"La respuesta '{respuesta}' es correcta"

# Determina si un subtema pertenece a algún tema
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

Ejemplo de uso de las funciones:

from Funciones import respuesta_incorrecta, subtema_afirmativo

print(respuesta_incorrecta("Javascript"))
print(respuesta_incorrecta("Una variable que almacena datos"))

print(subtema_afirmativo("Una variable que almacena datos"))
print(subtema_afirmativo("algoritmo"))
print(subtema_afirmativo("Logaritmo"))
```
**Las respuestas esperadas son:**
```python
La respuesta 'Javascript' es incorrecta
La respuesta 'Una variable que almacena datos' es correcta
El subtema 'Una variable que almacena datos' pertenece a un tema
El subtema 'algoritmo' pertenece a un tema
El subtema 'Logaritmo' no pertenece a ningún tema


