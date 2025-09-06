# Objetivo:
Pensando en un contexto financiero, utiliza la siguiente lista de predicados, por cada uno genera un Hecho, una Regla y 2 Consultas (una que resulte verdadera y una que resulte falsa).

## Predicados   

- "X" es un cliente.
- "Y" e un banco.
- "X" tiene una cuenta en el banco "Y".
- "Y" puede generar un préstamo de tipo "W".
- "X" recibió un monto "Z" de dinero.

## Estructura de la practica

- **data.py** alberga todos los diccionarios y conjuntos (hechos) los cuales seran consultados.
- **consultas.py** alberga todas las funciones necesarias para realizar las consultas propuestas en el ejercicio de predicados.
- **utils.py** alberga una funcion auxiliar para formatear los resultados a una tabla esteticamente mejorada con el uso de la libreria **rich**.
- **main.py** es el archivo encargado de ejecutar las consultas y presentar los resultados.