# Árbol de Decisión con el Dataset Wine 🍷

Este proyecto entrena un modelo de **árbol de decisión** usando el dataset `Wine` incluido en Scikit-Learn.  
Se analizan las reglas generadas, la precisión del modelo y el impacto de limitar o no la profundidad del árbol.

---

## 📘 Dataset Wine
El dataset contiene:

- **178 muestras**
- **13 características químicas**, tales como:
  - alcohol
  - ácido málico
  - cenizas
  - magnesio
  - flavonoides
  - color_intensity
  - proline

Las clases posibles son **0, 1 y 2**, que representan tres tipos de vino cultivados en la región italiana de Piamonte.

---

## 📌 Código
El programa `arbol_decision.py`:

- Carga el dataset
- Divide datos en entrenamiento/prueba (80/20)
- Entrena dos modelos:
  - Uno con `max_depth=2`
  - Uno sin límite (`max_depth=None`)
- Imprime las reglas generadas
- Calcula la precisión del modelo

---

## 📊 Resultados

### ✔ Árbol con profundidad limitada (max_depth=2)
- Reglas simples y fáciles de interpretar  
- Precisión aproximada: **0.86 – 0.94**

### ✔ Árbol sin límite (max_depth=None)
- Más reglas y más detalle  
- Más riesgo de *overfitting*  
- Precisión similar o ligeramente mayor

---

## 🧠 Opiniones sobre los resultados

- Cuando el árbol está **limitado**, genera reglas más claras y fáciles de explicar.
- Sin límite, el árbol memoriza demasiado los datos de entrenamiento.
- La precisión no mejora demasiado al quitar el límite, lo cual indica que el dataset tiene buena estructura.

---

## 📌 ¿El dataset Wine es adecuado para un modelo de árbol de decisión?

### ✔ **Sí, cumple muy bien los requisitos.**

**Justificación:**

- Sus características son **numéricas**, ideales para un árbol.
- Las clases están bien separadas.
- Es pequeño y fácil de procesar.
- Las reglas generadas son interpretables.

---

## 🏷 Características y clases del modelo

### **Características (features):**
1. alcohol  
2. malic_acid  
3. ash  
4. alcalinity_of_ash  
5. magnesium  
6. total_phenols  
7. flavanoids  
8. nonflavanoid_phenols  
9. proanthocyanins  
10. color_intensity  
11. hue  
12. od280/od315_of_diluted_wines  
13. proline  

### **Clases del modelo:**
- **0** — Tipo de vino 1  
- **1** — Tipo de vino 2  
- **2** — Tipo de vino 3  

---

## 🛠 ¿Qué pasaría si NO fuera adecuado?

Si un dataset:

- no tiene variables claras,
- tiene demasiados valores faltantes,
- o no hay diferencia real entre clases,

entonces **no** sería útil para un árbol.  
En ese caso podría usarse **regresión** (si la salida fuera numérica) o un modelo como **SVM o KNN**.

---

## 📁 Estructura del proyecto

