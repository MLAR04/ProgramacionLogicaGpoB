# ------------------------------------------------------
# Ejercicio 4: Uso de map, filter y reduce
# ------------------------------------------------------
# Lista inicial: [1,2,3,4,5,6,7,8,9,10]
# 1. Generar una nueva lista con los cuadrados usando map
# 2. Filtrar los números pares usando filter
# 3. Usar reduce para:
#    a) Calcular la suma de [1..10]
#    b) Calcular el producto de [1..5]
# ------------------------------------------------------

from functools import reduce

# Lista base
lista = [1,2,3,4,5,6,7,8,9,10]

# 1. Lista con cuadrados usando map
cuadrados = list(map(lambda x: x**2, lista))
print("Cuadrados:", cuadrados)

# 2. Filtrar números pares usando filter
pares = list(filter(lambda x: x % 2 == 0, lista))
print("Números pares:", pares)

# 3a. Suma de [1..10] con reduce
suma = reduce(lambda a, b: a + b, lista)
print("Suma de [1..10]:", suma)

# 3b. Producto de [1..5] con reduce
producto = reduce(lambda a, b: a * b, range(1, 6))
print("Producto de [1..5]:", producto)
