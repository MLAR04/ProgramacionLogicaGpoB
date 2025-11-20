Este proyecto entrena un modelo de árbol de decisión usando el dataset `Wine` incluido en Scikit-Learn.  
Se analizan las reglas generadas, la precisión del modelo y el impacto de limitar o no la profundidad del árbol.


El dataset contiene:
178 muestras
13 características químicas
  - alcohol
  - ácido málico
  - cenizas
  - magnesio
  - flavonoides
  - color_intensity
  - proline

Las clases posibles son 0, 1 y 2, que representan tres tipos de vino cultivados en la región italiana de Piamonte.

 Árbol con profundidad limitada (max_depth=2)
- Reglas simples y fáciles de interpretar  
- Precisión aproximada: 0.86 – 0.94

Árbol sin límite (max_depth=None)
- Más reglas y más detalle  
- Más riesgo de *overfitting*  
- Precisión similar o ligeramente mayor

 Opiniones sobre los resultados

- Cuando el árbol está limitado, genera reglas más claras y fáciles de explica
- Sin límite, el árbol memoriza demasiado los datos de entrenamiento.

El dataset Wine es adecuado para un modelo de árbol de decisión?

- Sus características son numéricas, ideales para un árbol.
- Las clases están bien separadas.
- Es pequeño y fácil de procesar.
- Las reglas generadas son interpretables.


Que pasaría si NO fuera adecuado?

Si un dataset:

- no tiene variables claras,
- tiene demasiados valores faltantes o no hay diferencia real entre clas

