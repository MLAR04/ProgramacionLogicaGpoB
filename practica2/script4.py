"""
Dada la lista [1,2,3,4,5,6,7,8,9,10]
"""
from functools import reduce #Importamos la funcion reduce()
#Cuadrado de cada número en la lista
def cuadrados_numero(lista):
    cuadrados_lista = map(lambda numero: numero**2, lista)
    return list(cuadrados_lista)

#Los números pares de la lista
def pares(lista):
    pares_lista = filter(lambda numero: numero % 2 == 0, lista)
    return list(pares_lista)

# La suma de [1..10]
def suma_lista(lista):
    return reduce(lambda a,b: a+b, lista)

#El producto del [1,,5]
def producto_lista(lista):
    return reduce(lambda a,b: a*b, lista)
if __name__ == "__main__":
    lista = [1,2,3,4,5,6,7,8,9,10]
    print("Los cuadrados de cada numero en la lista son:",cuadrados_numero(lista))
    print("Los numeros pares son: ",pares(lista))
    print("La suma de la lista es: ",suma_lista(lista))
    print("El producto de la lista del 1 al 5 es: ",producto_lista(lista))
