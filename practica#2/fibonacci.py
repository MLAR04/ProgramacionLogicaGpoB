def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("El número debe ser no negativo")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    try:
        n = int(input("Escribe un número entero que no sea negativo para calcular su Fibonacci: "))
        print(f"El número de Fibonacci en la posición {n} es: {fibonacci(n)}")
    except ValueError as e:
        print(f"Error: {e}")
