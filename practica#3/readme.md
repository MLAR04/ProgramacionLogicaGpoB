# Resumen de Códigos Python y Lógica Proposicional 🤓

Este documento describe la funcionalidad de tres programas Python diseñados para simular reglas lógicas y mostrar sus respectivas **Tablas de Verdad**.

---

## 1. Múltiplo de 6 (Conjunción: $P \land Q$)

**Regla Lógica:** Un número es múltiplo de 6 si es **divisible entre 2** ($P$) **Y** es **divisible entre 3** ($Q$).

**Función del Código:**
* Pide al usuario si se cumplen las dos condiciones ($P$ y $Q$).
* Aplica la operación lógica de **Conjunción** (`and` en Python).
* Imprime el resultado final y la **Tabla de Verdad** completa para la conjunción ($P \land Q$).
* **Resultado es Verdadero (V) solo si ambas premisas son Verdaderas.**

---

## 2. Voto (Conjunción Triple: $P \land Q \land R$)

**Regla Lógica:** Una persona puede votar si tiene **más de 18 años** ($P$) **Y** tiene **credencial de elector** ($Q$) **Y** está en la **lista nominal** ($R$).

**Función del Código:**
* Pide al usuario el estado de cumplimiento de las tres condiciones ($P$, $Q$ y $R$).
* Aplica la **Conjunción Triple** (`and` para las tres variables).
* Imprime el resultado final y la **Tabla de Verdad** con las 8 combinaciones posibles para una regla de tres variables ($P \land Q \land R$).
* **Resultado es Verdadero (V) solo si las tres premisas son Verdaderas.**

---

## 3. Conexión a Internet (Disyunción y Conjunción: $(P \lor Q) \land R$)

**Regla Lógica:** Una computadora conecta a internet si tiene **Wi-Fi** ($P$) **O** tiene **Ethernet** ($Q$), **Y** además, el **módem funciona** ($R$).

**Función del Código:**
* Pide el estado de las tres condiciones ($P$, $Q$ y $R$).
* Aplica una lógica compuesta:
    1.  **Disyunción** ($P \lor Q$) para la conectividad.
    2.  **Conjunción** de ese resultado con la condición del módem ($\dots \land R$).
* Imprime el resultado final y la **Tabla de Verdad** completa.
* **El resultado es Falso (F) si el módem no funciona, o si el módem funciona pero no hay ni Wi-Fi ni Ethernet.**
