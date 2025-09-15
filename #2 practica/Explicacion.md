
# ✨ Función Factorial en Python

Este programa implementa la función **factorial** utilizando **recursividad** en Python.

---

## 🔹 Objetivo
El objetivo del script es:
- Definir una función recursiva para calcular el factorial de un número entero.  
- Retornar el resultado de esa operación.  
- Ejecutar la función con un ejemplo (`factorial(5)`).  

---

## 🧾 Código completo

```python
def factorial(n):
    if n >= 1:
        return n * factorial(n-1)
    else:
        return 1


if __name__ == '__main__':
    print(factorial(5))



# ➕ Función de Suma en Python

Este programa implementa una función simple para **sumar dos números** en Python y muestra su resultado en pantalla.

---

## 🔹 Objetivo
El objetivo de este script es:
- Definir una función que reciba dos parámetros numéricos.  
- Retornar la suma de esos dos números.  
- Ejecutar la función con valores de ejemplo cuando se corre el archivo directamente.  

---

## 🧾 Código completo

```python
def suma(a, b):
    return a + b


if __name__ == '__main__':
    print(suma(10, 5))














# 📘 Operaciones con listas en Python

Este programa en Python muestra cómo usar las funciones **`map`**, **`filter`** y **`reduce`** para realizar diferentes operaciones sobre una lista de números.  

---

## 🔹 Objetivos del programa
1. Elevar todos los números de la lista al cuadrado.  
2. Filtrar únicamente los números pares.  
3. Sumar todos los elementos de la lista.  
4. Calcular el producto únicamente de los números del **1 al 5**.  

---

## 🧾 Código completo

```python
import functools

# Lista base del 1 al 10
lista = [1,2,3,4,5,6,7,8,9,10]

# Función que eleva un número al cuadrado
def elevar(num):
    return pow(num, 2)

# Función que valida si un número es par
def pares(pares):
    if (pares % 2 == 0):
        return True

# 1. Elevar cada número al cuadrado
cuadrado = list(map(elevar, lista))

# 2. Filtrar los números pares
num_pares = list(filter(pares, lista))

# 3. Sumar todos los elementos de la lista
suma = functools.reduce(lambda x, y: x + y, lista)

# 4. Calcular el producto de los números del 1 al 5
producto = functools.reduce(lambda x, y: x * y, lista[:5])

# Resultados
print(f"los cuadrados de los numeros de la lista son {cuadrado}")
print(f"los numeros pares de la lista son {num_pares}")
print(f"la suma de todos los numeros es {suma}")
print(f"el resultado del producto del 1 al 5 es {producto}")
