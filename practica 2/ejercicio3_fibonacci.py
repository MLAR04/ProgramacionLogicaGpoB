# Ejercicio 3: Funcion recursiva que calcule la secuencia de Fibonacci hasta n
def fibonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        secuencia = fibonacci(n - 1)  # Obtener la secuencia hasta n-1
        secuencia.append(secuencia[-1] + secuencia[-2])  # Agregar el siguiente numero
        return secuencia  # Devolver la secuencia completa hasta n

# Solicitar valor al usuario desde la terminal y asignarlo a n
n = int(input("Ingresa la posicion hasta la que quieres ver Fibonacci: "))

# Llamar a la funcion pasando el parametro n
resultado = fibonacci(n)

# Mostrar la secuencia completa
print("Secuencia de Fibonacci hasta la posicion", n, ":", resultado)
