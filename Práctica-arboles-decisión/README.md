Equipo de turismo.

## Opinion  
Al realizar la ejecucion del codigo del arbol con profundidad limitada se mostro una precision ligeamente menor a la del arbol sin limite de profundidad.
## Mi base de conocimientos (Turismo) serviria para usarse como arbol de decisión?  
Por el momento no, cumple con caracteristicas que podrian utilizarse dentro de un modelo predictivo, sin embargo esta diseñada para filtrar resultados segun el cliente, no para realizar una predicción.  
### ¿Qué cambios realizar para que sea compatible con un árbol de decisión?  
Para que esta base de conocimientos pueda utilizarse con un árbol de decisión, sería necesario convertirla de un sistema de filtrado a un sistema de predicción.
Para esto se necesita crear una variable objetivo (como tipo de hotel, nivel de recomendacion), codificar las etiquetas con formato numerico, y tener suficientes ejemplos para que el modelo pueda aprender las reglas.
