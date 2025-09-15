from functools import reduce

def cuadrado(arr):
    return list(map(lambda x: x**2, arr))

def filtrar_pares(arr):
    return list(filter(lambda x: x % 2 == 0, arr))

def suma(arr):
    return reduce(lambda x, y: x + y, arr)

def producto(arr):
    return reduce(lambda x, y: x * y, arr[:5])


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Cuadrados:", cuadrado(arr))
    print("Números pares:", filtrar_pares(arr))
    print("Suma total:", suma(arr))
    print("Producto de los primeros 5:", producto(arr))
