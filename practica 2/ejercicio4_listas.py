# Ejercicio 4: Operaciones con listas usando map, filter y reduce
from functools import reduce

# Lista de numeros dada en las instrucciones 
lista = [1,2,3,4,5,6,7,8,9,10]

# a) Generar una nueva lista con los cuadrados de cada numero usando map

# map aplica la funcion lambda a cada elemento de la lista
cuadrados = list(map(lambda x: x**2, lista))
print("Cuadrados de la lista:", cuadrados)

# b) Filtrar los numeros pares usando filter
# filter selecciona los elementos que cumplen la condicion lambda
pares = list(filter(lambda x: x % 2 == 0, lista))
print("Numeros pares en la lista:", pares)

# c) Usar reduce para calcular la suma de todos los elementos de la lista
# reduce acumula los resultados de aplicar la funcion lambda entre los elementos
suma_lista = reduce(lambda x, y: x + y, lista)
print("Suma de los elementos de la lista:", suma_lista)

# d) Usar reduce para calcular el producto de los primeros 5 elementos
# Se toma una sublista con los primeros 5 elementos y se aplica reduce con multiplicacion
producto_lista = reduce(lambda x, y: x * y, lista[:5])
print("Producto de los primeros 5 elementos:", producto_lista)
