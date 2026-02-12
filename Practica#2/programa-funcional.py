# Practica 2
from functools import reduce
lista = [1,2,3,4,5,6,7,8,9,10]

# 1 Función suma
def suma (a, b):
   return a + b

#2 Funcion factorial
def factorial(n):
   if n == 0 or n == 1:
      return 1
   return n * factorial(n-1)

#3 Fibonacci
def fibonacci(n):
   if n == 0:
      return 0
   if n == 1:
      return 1
   return fibonacci(n-1) + fibonacci(n-2)

#4 map
cuadrados = list(map(lambda x: x**2, lista))

#5 filter
pares = list(filter(lambda x: x% 2 == 0, lista))

#6 reduce
suma_lista = reduce(lambda x, y: x + y, lista) 
producto = reduce(lambda x, y: x * y, [1,2,3,4,5])

print("Suma:", suma(1,2))
print("Factorial:", factorial(5))
print("Fibonacci:", fibonacci(6))
print("Cuadrados:", cuadrados)
print("Pares:", pares)
print("Suma de 1 al 10:", suma_lista)
print("Producto de 1 al 5:", producto)

