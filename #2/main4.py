# Dada la lista [1,2,3,4,5,6,7,8,9,10]:
#   Genera una nueva lista con los cuadrados de cada número usando map.
#   Filtra los números pares usando filter
#   Usa reduce para calcular:
#       La suma de [1..10]
#       El producto [1..5]

from functools import reduce

def cuadrados(x):
    return x**2

def pares(lista):
    return list(filter(lambda x: x%2 == 0, lista))

def calculoReduce(lista):
    suma = reduce(lambda x, y: x + y, lista)
    producto = reduce(lambda x, y: x * y, lista[:5])
    
    return f"Suma: {suma}, Producto: {producto}"

if __name__ == "__main__":
    lista = [1,2,3,4,5,6,7,8,9,10]

    nueva_lista = list(map(cuadrados, lista))
    print(nueva_lista)

    print(pares(lista))
    print(calculoReduce(lista))