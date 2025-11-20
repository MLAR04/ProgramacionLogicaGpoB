# Clasificación de Vinos con Árbol de Decisión 

Este proyecto implementa un modelo de **Árbol de Decisión** en Python utilizando la librería `scikit-learn`. El objetivo es clasificar vinos en tres categorías diferentes basándose en sus características químicas (como alcohol, ácido málico, cenizas, etc.).

[cite_start]El proyecto utiliza el dataset **Wine** incluido en las bases de datos de prueba de scikit-learn[cite: 8].

## Requisitos

Para ejecutar este proyecto necesitas tener instalado Python y las siguientes librerías:

* **scikit-learn**: Para el modelo de Machine Learning y el dataset.
* **matplotlib**: Para la visualización gráfica del árbol.

### Instalación
Ejecuta el siguiente comando en tu terminal para instalar las dependencias:

```bash```
```pip install scikit-learn matplotlib```


## Opinión sobre los resultados 

Al realizar las pruebas con diferentes profundidades (max_depth), observé lo siguiente:


Precisión del modelo: El modelo consiguió una precisión muy alta (generalmente superior al 90%) en los datos de prueba. Esto indica que las características químicas son excelentes predictores para distinguir el tipo de vino.

Profundidad Limitada (max_depth=2 o 3): Las reglas generadas son cortas y comprensibles. Por ejemplo, el árbol suele preguntar primero por la "prolina" o los "flavonoides". Es fácil seguir la lógica humana.

Sin Límite de Profundidad (max_depth=None): El árbol crece mucho más. Aunque la precisión en entrenamiento puede ser perfecta, las reglas se vuelven complejas y difíciles de interpretar, corriendo el riesgo de "sobreajuste" (memorizar los datos en lugar de aprender patrones generales) .


##¿La base de conocimiento cumple con los requerimientos para utilizarse en un modelo de árbol de decisiones?

Respuesta: SÍ.
Justificación:El dataset cumple con los tres pilares necesarios para este algoritmo:
Datos Etiquetados: Contamos con la variable objetivo ya definida (la clase de vino), lo cual es indispensable para el aprendizaje supervisado.
Variables Informativas: Las características son numéricas y continuas, lo que permite al árbol establecer cortes lógicos (umbrales matemáticos como $\le$ o $>$) para separar las clases eficientemente.
Naturaleza del Problema: El problema es de clasificación (categorías discretas), que es la función natural de un DecisionTreeClassifier 6.
