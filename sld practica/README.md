#  Sistema Experto de Turismo en México
**Proyecto de Programación Lógica (Resolución SLD en Python)**  
Instituto Tecnológico de Ensenada  

---

##  Descripción General

Este proyecto implementa un **sistema experto sobre turismo en México** utilizando conceptos de **programación lógica**, **unificación de términos** y **resolución SLD (Selective Linear Definite clause resolution)**.  

El objetivo es simular el funcionamiento de un motor lógico (como Prolog) que sea capaz de responder consultas sobre **hoteles, destinos turísticos y actividades** con base en una **base de conocimiento** estructurada en forma de **cláusulas de Horn**.

El sistema es **interactivo**: muestra al usuario los lugares registrados y permite realizar consultas personalizadas, tales como:
- Verificar si un lugar es turístico.  
- Buscar hospedajes accesibles según el presupuesto disponible.  

---

## 📁 Estructura del Proyecto

proyecto_sld/
│
├── base_conocimiento.pl # Representación de hechos y reglas
├── sld_practice.py # Script principal con unificación y resolución SLD



---

##  Base de Conocimiento

La **base de conocimiento** se encuentra dentro del archivo **`sld_practice.py`**, en la parte superior del código, en una lista llamada `base_conocimiento`.

Esta base contiene **hechos** sobre hoteles y actividades, expresados en forma de **tuplas**:

python
base_conocimiento = [
    ("hotel", ["Hotel_Sol", "Cancún", "lujo", 2000]),
    ("hotel", ["Hostal_Playa", "Cancún", "económico", 500]),
    ("hotel", ["Cabaña_Bosque", "Valle_de_Bravo", "rural", 1200]),
    ("actividad", ["Snorkel", "Cancún", "acuática", 700]),
    ("actividad", ["Kayak", "Valle_de_Bravo", "acuática", 600])
]

Cada hecho representa información del dominio turístico:

hotel(Nombre, Lugar, Tipo, Precio)

actividad(Nombre, Lugar, Tipo, Costo)

Cláusulas de Horn

Las cláusulas de Horn se encuentran en la lista reglas dentro del mismo archivo.
Estas reglas definen relaciones lógicas que permiten al sistema derivar nuevos conocimiento

Ejemplo:

reglas = [
    # Un lugar es turístico si existe al menos una actividad registrada
    ("turistico", ["Lugar"],
     [("actividad", ["_", "Lugar", "_", "_"])]),

    # Un hotel es accesible si su precio es menor o igual al presupuesto
    ("accesible", ["Hotel", "Lugar", "Presupuesto"],
     [("hotel", ["Hotel", "Lugar", "_", "Precio"]),
      ("<=", ["Precio", "Presupuesto"])])
]


Estas dos cláusulas de Horn permiten ejecutar consultas del tipo:

turistico('Cancún')

accesible(Hotel, 'Valle_de_Bravo', 1500)

Unificación

La unificación es el proceso mediante el cual el sistema compara dos términos lógicos (por ejemplo, un hecho y una consulta) para determinar si pueden hacerse iguales mediante sustitución de variables.

En este proyecto, la función de unificación se encuentra en:

def unificar(patron, hecho, sustituciones):


Ubicación: línea 60 - 80 del archivo sld_practice.py.

Función:

Compara elemento por elemento entre un patrón (consulta o regla) y un hecho.

Si encuentra una variable (nombre que inicia con mayúscula), la sustituye por el valor correspondiente.

Si hay conflicto (la variable ya tiene otro valor asignado), devuelve None.

Ejemplo de uso interno:

unificar(["Hotel", "Cancún"], ["Hotel_Sol", "Cancún"], {})
# Retorna: {'Hotel': 'Hotel_Sol'}

 Resolución SLD

La resolución SLD (Selective Linear Definite clause resolution) es el corazón del sistema.
Se implementa en la función:

def resolver(query):


Ubicación: línea 83 - 160 del archivo sld_practice.py.

Funcionamiento:

Recibe una consulta (query), como por ejemplo:
("accesible", ["Hotel", "Valle_de_Bravo", 1500])

Busca una regla o hecho que tenga el mismo predicado (accesible, turistico, etc.).

Aplica unificación entre el objetivo y la cabeza de la regla.

Si hay coincidencia, agrega los sub-objetivos de la regla a una pila de trabajo.

Evalúa comparaciones numéricas (como Precio <= Presupuesto).

Imprime la ruta de derivación paso a paso mostrando cómo se llegó a la solución.

Ejemplo de salida:

➡️ Objetivo actual: accesible('Hotel', 'Valle_de_Bravo', 1500)
📘 Aplicando regla: accesible('Hotel', 'Lugar', 'Presupuesto') :- [('hotel', ['Hotel', 'Lugar', '_', 'Precio']), ('<=', ['Precio', 'Presupuesto'])]
✅ Unificado con hecho: ('hotel', ['Cabaña_Bosque', 'Valle_de_Bravo', 'rural', 1200])
✅ Comparación verdadera: 1200 <= 1500
Resultado final: {'Hotel': 'Cabaña_Bosque', 'Lugar': 'Valle_de_Bravo', 'Presupuesto': 1500, 'Precio': 1200}


