from functools import reduce

lista = [1,2,3,4,5]


def elevar_al_cuadrado(lista):
    return list(map(lambda x: x**2, lista))


def filtrar_numeros(lista):
    return list(filter(lambda x: x % 2 == 0, lista))


def sumar_numeros(lista):
    return reduce(lambda x, y: x + y, lista)


def multiplicar_numeros(lista, cantidad):
    return reduce(lambda x, y: x * y, lista[:cantidad])



if __name__ == "__main__":
    print("Elevar al cuadrado:", elevar_al_cuadrado(lista))
    print("Filtrar números pares:", filtrar_numeros(lista))
    print("Sumar números:", sumar_numeros(lista))
    print("Multiplicar los primeros 5 numeros:", multiplicar_numeros(lista, 5))