# Practica 3 - Descomposición de Reglas Lógicas

Utiliza la descomposición de reglas lógicas para descomponer los siguientes predicados:

- Un número es múltiplo de 6 si es divisible entre 2 y divisible entre 3.
- Una persona puede votar si tiene más de 18 años, tiene credencial de elector y está en la lista nominal.
- Una computadora puede conectarse a internet si tiene Wi-Fi activado o cable Ethernet conectado, y además el módem funciona.

---

## Predicado 1

- Un número es múltiplo de 6 si es divisible entre 2 y divisible entre 3.
  - R<sub>1</sub> = es divisible entre 2
  - R<sub>2</sub> = es divisible entre 3

Es múltiplo de 6 ↔ R<sub>1</sub> ^ R<sub>2</sub>

## Predicado 2

- Una persona puede votar si tiene más de 18 años, tiene credencial de elector y está en la lista nominal.
  - R<sub>1</sub> = tiene mas de 18 años
  - R<sub>2</sub> = tiene credencial
  - R<sub>3</sub> = esta en la lista nominal

Puede votar ↔ R<sub>1</sub> ^ R<sub>2</sub> ^ R<sub>3</sub>

## Predicado 3

- Una computadora puede conectarse a internet si tiene Wi-Fi activado o cable Ethernet conectado, y además el módem funciona.
  - R<sub>1</sub> = tiene Wi-Fi activado
  - R<sub>2</sub> = tiene cable Ethernet conectado
  - R<sub>3</sub> = el modem funciona

Puede acceder a internet ↔ (R<sub>1</sub> <sup>v</sup> R<sub>2</sub>) ^ R<sub>3</sub>
