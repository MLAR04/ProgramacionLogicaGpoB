# Ejercicio 1: Funcion suma que solo depende de sus parametros
def suma(a, b):
    return a + b

# Solicitar valores al usuario desde la terminal
num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))

# Llamar a la funcion y mostrar el resultado
resultado = suma(num1, num2)
print("Resultado de la suma:", resultado)
