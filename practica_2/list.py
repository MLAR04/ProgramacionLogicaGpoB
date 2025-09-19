# Dada la lista [1,2,3,4,5,6,7,8,9,10]:
# Genera una nueva lista con los cuadrados de cada número usando map.
# Filtra los números pares usando filter
# Usa reduce para calcular:
#   La suma de [1..10]
#   El producto [1..5]

from functools import reduce

# 1. lista de cuadrados
def cuadrado(x):
    return x**2

# 2. Lista de pares
def pares(x):
    if x % 2 == 0:
        return True
    else:
        return False

# 3. Lista de sumas
def suma(a, b):
    return a + b

# 4. Lista de productos
def producto(x, y):
    return x * y


if __name__ == "__main__":
    main_list = [1,2,3,4,5,6,7,8,9,10] # Lista Principal

    # 1. Cuadrado de cada número
    list_cuadrados = map(cuadrado, main_list)
    print(f"Lista de cuadrados: {list(list_cuadrados)}")

    # 2. Filtro de numeros pares
    list_pares = filter(pares, main_list)
    print(f"Lista de pares: {list(list_pares)}")

    # 3.1 La suma de [1..10]
    list_suma = reduce(suma, main_list)
    print(f"La suma de todos los elementos es: {list_suma}")

    # 3.2 El producto [1..5]
    list_producto = reduce(producto, main_list[1:5])
    print(f"El producto de los primeros 5 elementos es: {list_producto}")