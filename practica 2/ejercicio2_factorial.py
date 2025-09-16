# Ejercicio 2: Funcion recursiva que calcule el factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Solicitar valor al usuario desde la terminal
num = int(input("Ingresa un numero para calcular su factorial: "))

# Llamar a la funcion pasando el parametro (ese valor se pasa como parametro n)
resultado = factorial(num)

# Mostrar el resultado
print("Factorial de", num, ":", resultado)
