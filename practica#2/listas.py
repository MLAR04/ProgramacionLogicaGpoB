from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def cuadrado(x):
    return x**2

def es_par(x):
    return x % 2 == 0

def suma(a, b):
    return a + b

def producto(a, b):
    return a * b

cuadrados = list(map(cuadrado, numeros))
pares = list(filter(es_par, numeros))
suma_total = reduce(suma, numeros)
producto_1_5 = reduce(producto, numeros[:5])

print("Cuadrados:", cuadrados)
print("Pares:", pares)
print("Suma total:", suma_total)
print("Producto:", producto_1_5)
