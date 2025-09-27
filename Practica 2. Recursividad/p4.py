#Dada la lista [1,2,3,4,5,6,7,8,9,10]:
#Genera una nueva lista con los cuadrados de cada número usando map.
#Filtra los números pares usando filter
#Usa reduce para calcular:
#La suma de [1..10]
#El producto [1..5]
#

from functools import reduce

# lista original
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Genera una nueva lista con los cuadrados de cada número usando map
cuadrados = list(map(lambda x: x**2, numeros)) #Lambda ayuda a crear una funcion pequeña sin necesidad de que usemos def
print("Cuadrados:", cuadrados)                 #MAP ayuda a transfprmar cada elemento de la lista
                                                # Se usa list para que se vayan guardando los resultados

# 2. Filtra los números pares usando filter
pares = list(filter(lambda x: x % 2 == 0, numeros)) #FILTER solo secciona algunos elementos 
print("Numeros pares:", pares)

# 3. Usa reduce para calcular la suma de [1..10]
suma = reduce(lambda a, b: a + b, numeros) # REDUCE junta todo, en un solo valor 
print("Suma de 1..10:", suma)

# 4. Usa reduce para calcular el producto de [1..5]
producto = reduce(lambda a, b: a * b, [1, 2, 3, 4, 5])
print("Producto de 1..5:", producto)
