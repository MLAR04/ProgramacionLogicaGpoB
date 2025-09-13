# Importamos reduce de functools para operaciones acumulativas como suma o producto
from functools import reduce

# Lista de números del 1 al 10
lista = [1,2,3,4,5,6,7,8,9,10]

# ==========================
# Función suma
# ==========================
def suma(a, b):
    # Retorna la suma de los parámetros a y b
    return a + b

# ==========================
# Función factorial recursiva
# ==========================
def factorial(n):
    # Caso base: si n es 1, el factorial es 1
    if n == 1:
        return 1
    else:
        # Caso recursivo: n! = n * (n-1)!
        return n * factorial(n - 1)

# ==========================
# Función Fibonacci recursiva
# ==========================
def fibonacci(n):
    # Caso base: el primer número de Fibonacci es 0
    if n == 1:
        return 0
    # Caso base: el segundo número de Fibonacci es 1
    elif n == 2:
        return 1
    else:
        # Caso recursivo: Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)
        return fibonacci(n - 2) + fibonacci(n - 1)


# ==========================
# Bloque principal
# ==========================
if __name__ == '__main__':
    # Imprime la suma de 10 y 9 usando la función suma
    print(suma(10, 9)) # 19
    
    # Imprime el factorial de 4 usando la función factorial
    print(factorial(4)) # 24  -> 4*3*2*1 = 24
    
    # Imprime el sexto número de Fibonacci usando la función fibonacci
    print(fibonacci(6))  # 5   -> Fibonacci: 0,1,1,2,3,5
    
    # Genera y muestra una nueva lista con los cuadrados de cada número usando map
    print(list(map(lambda x: x*x, lista))) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    
    # Filtra y muestra los números pares de la lista usando filter
    print(list(filter(lambda x: (x % 2) == 0, lista)))  # [2, 4, 6, 8, 10]
    
    # Calcula y muestra la suma de todos los elementos de la lista usando reduce
    print(reduce(lambda x, y: x + y, lista))  # 55  -> 1+2+3+...+10
    
    # Calcula y muestra el producto de los primeros 5 elementos de la lista usando reduce
    print(reduce(lambda x, y: x * y, lista[:5])) # 120 -> 1*2*3*4*5