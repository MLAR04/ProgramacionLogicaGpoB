from functools import reduce

#---------------------------------------------------------------------------#
#   Dada la lista [1,2,3,4,5,6,7,8,9,10]:                                   #
#   Genera una nueva lista con los cuadrados de cada número usando map.     #
#---------------------------------------------------------------------------#

def map_lista():
    lista = [1,2,3,4,5,6,7,8,9,10] # declarar la lista local
    return list(map(lambda item: item * item, lista)) # retorna el valor elevado al cuadrado de cada elemento.

#---------------------------------------------------------------------------#
# Filtra los números pares usando filter                                    #
#---------------------------------------------------------------------------#

def filter_lista():
    lista = [1,2,3,4,5,6,7,8,9,10] # declarar la lista local
    return list(filter(lambda item: item % 2 == 0, lista)) #retorna la lista de numeros pares basandose en el residuo.

#---------------------------------------------------------------------------#
#   Usa reduce para calcular:                                               #
#   La suma de [1..10]                                                      #
#---------------------------------------------------------------------------#

def reduce_suma():
    lista = [1,2,3,4,5,6,7,8,9,10] # declarar la lista local
    return reduce(lambda item1, item2: item1 + item2, lista) # retorna la suma de los valores de la lista

#---------------------------------------------------------------------------#
#   Usa reduce para calcular:                                               #
#   El producto [1..5]                                                      #
#---------------------------------------------------------------------------#

def reduce_producto():
    lista = [1,2,3,4,5,6,7,8,9,10] # declarar la lista local
    return reduce(lambda item1, item2: item1 * item2, lista[:5]) # retorna el producto de los valores de la lista






if __name__ == '__main__':
    print(f'Los cuadrados son {map_lista()}')
    print(f'La lista de pares es {filter_lista()}')
    print(f'La suma es {reduce_suma()}')
    print(f'El producto es {reduce_producto()}')