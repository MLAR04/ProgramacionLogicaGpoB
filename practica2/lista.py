# Dada la lista [1,2,3,4,5,6,7,8,9,10]:
# Genera una nueva lista con los cuadrados de cada número usando map.
# Filtra los números pares usando filter
# Usa reduce para calcular:
# La suma de [1..10]
# El producto [1..5]

from functools import reduce


def cuadrado(n):
    return n**2

def es_par(n):
    return True if n % 2 == 0 else False

def suma(a,b):
    return a+b

def producto(a, b):
    return a * b

if __name__ == '__main__':
    numeros = [1,2,3,4,5,6,7,8,9,10]

    cuadrados = map(cuadrado, numeros)
    print('Lista de cuadrados: ', list(cuadrados))

    pares = filter(es_par, numeros)
    print('Pares: ', list(pares))

    resultado_suma = reduce(suma, numeros)
    print('suma de todos los numeros: ', int(resultado_suma))

    resultado_m = reduce(producto, numeros[1:5])
    print('producto de los primeros 5 numeros:', int(resultado_m))
