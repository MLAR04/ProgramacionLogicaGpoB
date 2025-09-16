from functools import reduce


# Escribe una función suma(a,b) que solo dependa de sus parámetros.
def suma(a, b):
    return a + b


print("Funcion de Suma:", suma(9, 3))


# Función recursiva factorial(n)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print("Funcion Factorial", factorial(5))


# Función recursiva de Fibonacci.
def fibonacci(n):
    # La serie comienza con 0 y n0 = 0, n1=1.
    if n < 0:
        return "El numero no debe ser menor que 0"
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print("Funcion n-esimo numero fibonnaci:", fibonacci(6))

# Ultimo ejercicio
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Genera una nueva lista con los cuadrados de cada número usando map.
listaResultados = map(lambda x: x ** 2, lista)
print("EL cuadrado de cada numero usando Map:", list(listaResultados))

# Filtra los números pares usando filter
listaResultados = filter(lambda x: x % 2 == 0, lista)
print("Obtener numeros pares usando Filter:", list(listaResultados))

# Reduce: La suma de [1..10]
Resultado = reduce(lambda x, y: x + y, lista)
print("Suma 1..10 usando Reduce:", Resultado)

# El producto [1..5]
Resultado = reduce(lambda x, y: x * y, lista[0:5])
print("Producto de 1..5 usando Reduce:", Resultado)
