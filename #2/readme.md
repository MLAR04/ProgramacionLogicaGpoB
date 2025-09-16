# Ejercicios en Python

Este proyecto contiene varios ejercicios de funciones y operaciones básicas en Python.  
Cada ejercicio está en un archivo independiente y también existe un archivo `main.py` para ejecutar todo de una vez.

---

## 📂 Archivos

- `suma.py`: Contiene la función `suma(a, b)` que devuelve la suma de dos números.
- `factorial.py`: Contiene la función `factorial(n)` que calcula el factorial de un número de forma recursiva.
- `fibonacci.py`: Contiene la función `fibonacci(n)` que devuelve el n-ésimo número de Fibonacci de forma recursiva.  
  Además imprime los primeros 30 números de la serie si se ejecuta de manera individual.
- `lista.py`: Contiene ejemplos del uso de `map`, `filter` y `reduce`:
  - Lista de cuadrados con `map`.
  - Lista de números pares con `filter`.
  - Suma de los números del 1 al 10 con `reduce`.
  - Producto de los números del 1 al 5 con `reduce`.
- `main.py`: Ejecuta todos los ejercicios en conjunto importando los módulos anteriores.

---

## Ejecución

### Opción 1: Ejecutar cada archivo por separado
Abrir la terminal en la carpeta del proyecto y correr:

```bash
python suma.py
python factorial.py
python fibonacci.py
python lista.py

### Opción 2: Ejecutar todos los archivos de una vez

python main.py