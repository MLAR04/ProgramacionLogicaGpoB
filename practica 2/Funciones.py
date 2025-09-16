from functools import reduce

def suma(a, b):
    return a + b

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Esta funcion si tiene prints por que pidio en el ejercicio que la misma lista
# se modifique de varias maneras 
def modificar_lista(lista):
    cuadrados = list(map(lambda x: x**2, lista))
    pares     = list(filter(lambda x: x % 2 == 0, lista))
    suma      = reduce(lambda a,b: a+b, lista)
    producto  = reduce(lambda a,b: a*b, lista[:5])

    print(cuadrados)
    print(pares)
    print(suma)
    print(producto)


# Aqui puede cambiar los valores para probar las funciones
def __main__():
    print(suma(3, 5))
    print(factorial(5))
    print(fibonacci(6))
    modificar_lista([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])