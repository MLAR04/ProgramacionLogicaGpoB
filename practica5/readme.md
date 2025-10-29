# EQUIPO EDUCACION

## Leyes utilizadas en esta práctica

1. Si el usuario envía una respuesta incorrecta de un **subtema**, requiere apoyo en el **tema**.  
2. Si existe un **subtema**, pertenece a un **tema**.  

## Primera cláusula de Horn

Usaremos la ley de nuestro proyecto:  
**Todo subtema pertenece a un tema.**

Esto significa que nuestra consulta será:  
> ¿El subtema “diseño de funciones” pertenece al tema “diseño algorítmico”?

## Segunda cláusula de Horn

En esta parte usaremos las dos leyes:

1. Si el usuario envía una respuesta incorrecta de un **subtema**, requiere apoyo en el **tema**.  
2. Si existe un **subtema**, pertenece a un **tema**.  

## Hechos utilizados

Los hechos definidos en la base de conocimiento son los siguientes:

```python
hechos = [
    ("subtema", "conceptos_basicos", "diseno_algoritmico"),
    ("subtema", "estructuras_de_control", "diseno_algoritmico"),
    ("subtema", "diseno_de_funciones", "diseno_algoritmico"),
    ("respuesta_incorrecta", "usuario1", "diseno_de_funciones")
]
