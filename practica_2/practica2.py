from functools import reduce

#1.-Escribe una función suma(a,b) que solo dependa de sus parámetros.
def suma(a,b):
    return(a + b)

#2.-Implementa una función recursiva factorial(n) que calcule el factorial.
def factorial(n):
    if n== 1:
        return 1
    else:
        f=n*(factorial(n-1))
        return f

#3.-Escribe una función recursiva que calcule el n-ésimo número de Fibonacci.
def Fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else: 
        f = Fibonacci(n-1)+ Fibonacci(n-2)
        return f

numeros =  [1,2,3,4,5,6,7,8,9,10]
#4.1.-Genera una nueva lista con los cuadrados de cada número usando map.
def cuadrado(x):
    return x*x
def nueva_lista():
    return(list( map(cuadrado, numeros)))
#4.2.-Filtra los números pares usando filter
def par(x):
    if x%2 == 0:
        return x
def lista_pares():
    return(list( filter(par, numeros)))

#4.3.-Usa reduce para calcular:
#4.3.1 La suma de [1..10]
def suma(x,y):
    return(x+y)
def suma_reduce():
    return(reduce(suma, numeros))

#4.3.2.- El producto [1..5]
def multiplicacion(x,y):
    return(x*y)
def multiplicacion_reduce():
    return(reduce(multiplicacion, numeros[:5]))

if __name__ == '__main__':
    #Ejercicio 1
    print(suma(4,1))
    #Ejercicio 2
    print(factorial(5))
    #Ejercicio 3
    print(Fibonacci(10))
    #Ejercicio 4.1
    print(nueva_lista())
    #Ejercicio 4.2
    print(lista_pares())
    #Ejercicio 4.3.1
    print(suma_reduce())
    #Ejercicio 4.3.1
    print(multiplicacion_reduce())
    