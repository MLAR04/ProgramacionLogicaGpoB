import functools


lista = [1,2,3,4,5,6,7,8,9,10]

def elevar (num):

    return pow(num,2)

def pares (pares):
    if (pares%2==0):
        return True
    

    

cuadrado=list(map(elevar,lista))

num_pares=list(filter (pares,lista))

suma = functools.reduce(lambda x,y: x+y,lista)

producto = functools.reduce(lambda x,y: x*y,lista[:5])

print(f"los cuadrados de los nuemros de las lista son {cuadrado}")

print(f"los numeros pares de la lista son {num_pares}")

print (f"la suma de todos los numeros da de resultado  {suma}")

print (f"el resultado del producto del 1 al 5 es {producto}")