from functools import reduce

# funcion suma(a,b)
def suma(a, b):
    return a+b

# funcion recursiva factorial(n)
def factorial(n):
    return 1 if n <= 1 else n * factorial(n-1)

# funcion recursiva n-esimo numero de Fibonacci: 1,1,3,5,8,...
def fibonacci(n):
    return n if n < 2 else fibonacci(n-1) + fibonacci(n-2)

# Dada la lista del 1 al 10
lista = list(range(1, 11))

# Generar nueva lista con cuadrados usando "map"
lista_cuadrados = list(map(lambda x: x**2, lista))

# Filtrar numeros pares usando "filter"
lista_pares = list(filter(lambda x: x%2==0, lista))

# Usar "reduce" para calcular suma del 1 al 10
suma_1_10 = reduce(lambda x, y: x+y, lista)

# Usar "reduce" para calcular producto del 1 al 5
producto_1_5 = reduce(lambda x, y: x*y, range(1,6))

def show_results():
    print("suma(7,8) =", suma(7,8),
          "\nfactorial(5) =", factorial(5),
          "\nfibonacci(7) =", fibonacci(7),
          "\nDe la lista:", lista,
          "\n\tnueva lista con cuadrados =", lista_cuadrados,
          "\n\tfiltrar los pares =", lista_pares,
          "\n\tusar reduce para sumar del 1 al 10 =", suma_1_10,
          "\n\tusar reduce para multiplicar del 1 al 5 =", producto_1_5)

show_results()
