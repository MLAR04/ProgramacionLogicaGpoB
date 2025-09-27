#Escribe una función recursiva que calcule el n-ésimo número de Fibonacci.

def fibonacci(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

posicion = int(input("Ingrese el numero de posicion de la serie de Fibonacci que desee conocer:"))

print(f"El numero de Fibonacci en la posicion {posicion} es: {fibonacci(posicion)}")
