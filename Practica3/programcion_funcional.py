#Programación Funcional 
from functools import reduce

#Escribe una función suma(a,b) que solo dependa de sus parámetros
def suma(a, b):
    resultado = a + b
    return resultado

print("p1:")
print("La suma de 3 + 5 es:", suma(4, 2))
print()

# 2. Implementa una función recursiva factorial(n) que calcule el factorial.
def factorial(n):
    if n == 0 or n == 1:  
        return 1
    else: 
        return n * factorial(n - 1)

print("p2:")
print("Factorial(5):", factorial(5))
print()

# Escribe una función recursiva que calcule el n-ésimo número de Fibonacci.
def fibonacci(n):
    if n == 1 or n == 2: ## El Fibonacci de 1 y 2 siempre es 1
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("p3:")
print("El número en la serie de Fibonacci es:", fibonacci(7))
print()

#ejercicio4
# Lista
numeros = [1,2,3,4,5,6,7,8,9,10]

#1 Genera una nueva lista con los cuadrados de cada número usando map
cuadrados = list(map(lambda x: x**2, numeros))
print("p4: ")
print("Cuadrados:", cuadrados)

#2 Filtra los números pares usando filter
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Números pares:", pares)

#3 Usa reduce para calcular
suma = reduce(lambda x, y: x + y, numeros)
print("Suma [1..10]:", suma) #La suma de [1..10]

producto = reduce(lambda x, y: x * y, [1,2,3,4,5])
print("Producto [1..5]:", producto) #El producto [1..5]
