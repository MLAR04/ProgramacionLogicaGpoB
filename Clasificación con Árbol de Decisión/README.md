# README 

##  resultados

Los resultados del modelo fueron buenos.\
Con un arbol pequeño (por ejemplo, `max_depth=2`), las reglas son
fáciles de entender y la precisión sigue siendo preciso.\
Cuando se deja que el árbol crezca sin límite (`max_depth=None`), el
modelo mejora su precision porque puede aprender  más detalles del
dataset.
el comportamiento del modelo es el esperado y los resultados
son coherentes.

## ¿El dataset sirve para usar un árbol de decisión?

 el dataset del vino funciona bien con un árbol de decisión.

### ¿Por que?

-   Todas las características son numéricas y fáciles de dividir con
    reglas.
-   La variable objetivo tiene clases claras: 0, 1 y 2.
-   El modelo alcanza buenas precisiones, lo que significa que los datos
    sí contienen patrones distinguibles.
-   No tiene problemas grandes de datos faltantes o ruido.


### Características

El modelo utiliza mediciones del vino como:

-   alcohol
-   malic_acid
-   ash
-   alcalinity_of_ash
-   magnesium
-   total_phenols
-   flavanoids
-   nonflavanoid_phenols
-   proanthocyanins
-   color_intensity
-   hue
-   od280/od315_of_diluted_wines
-   proline

### Clases

-   Clase 0
-   Clase 1
-   Clase 2


