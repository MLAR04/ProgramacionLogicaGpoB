# ARBOL DE DESICIONES

En el archivo main.py se encuentra todo el codigo necesario para entrenar el modelo, exportar los resultados y analizarlos.

Los resultados se encuentran en resultados_wine.csv

## OPINIONES DE LOS RESULTADOS

### Uso de max_depth

Al aumentar el número en max_depth noté como el arbol generado en la terminal agregaba más reglas y se hacia cada vez más profundo, igualmente al hacer más pequeño el número.

Posteriormente al usar 'None' no existía un límite y se generaba el arbol completo.

### Resultados en la presición
en el metodo DecisionTreeClassifier() uso como semilla un valor aleatorio entre 1 y 99 por lo que el resultado siempre es diferente.

De todas las pruebas cambiando la profundidad del arbol y la semilla, la presición del modelo varia entre el 75.2% y el 99.8%


### MI base de conocimiento (Diagnostico en fresas)

Por la naturaleza y la estrucutura de la base de conocimiento opino que es ideal para utilizarse como modelo de arbol de desiciones, esto porque:

- Los hechos son los valores de entrada que utilizaría el arbol
- Cuenta con un apartado 'conclusión' que dicta al arbol que debe predecir en base a las entradas.
