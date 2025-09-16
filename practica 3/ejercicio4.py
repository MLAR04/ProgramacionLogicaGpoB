#Dada la lista [1,2,3,4,5,6,7,8,9,10]:
#Genera una nueva lista con los cuadrados de cada número usando map.
#Filtra los números pares usando filter
#Usa reduce para calcular:
#La suma de [1..10]
#El producto [1..5]

from functools import reduce

numeros = [1,2,3,4,5,6,7,8,9,10]
cuadrados = list(map(lambda x: x**2, numeros))
print("Cuadrados:", cuadrados)

pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Numeros pares:", pares)

suma = reduce(lambda x, y: x + y, numeros)
print("Suma de [1..10]:", suma)

producto = reduce(lambda x, y: x * y, range(1, 6))
print("Producto de [1..5]:", producto)
