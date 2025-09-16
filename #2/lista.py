# Lista con map, filter y reduce

from functools import reduce

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usamos map para elevar al cuadrado
cuadrados = list(map(lambda x: x**2, lista))

# Usamos filter para obtener solo los números pares
pares = list(filter(lambda x: x % 2 == 0, lista))

# Usamos reduce para obtener la suma y el factorial
suma_total = reduce(lambda x, y: x + y, lista)
factorial = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])

if __name__ == "__main__":
    print("Cuadrados:", cuadrados)
    print("Pares:", pares)
    print("Suma de [1-10]:", suma_total)
    print("Factorial de 5:", factorial)