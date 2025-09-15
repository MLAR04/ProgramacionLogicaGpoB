def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("El número no debe ser negativo")
    return 1 if n <= 1 else n * factorial(n - 1)


if __name__ == '__main__':
    try:
        n = int(input("Escribe un numero entero que no sea negativo: "))
        print(f"El factorial de {n} es: {factorial(n)}")
    except ValueError as e:
        print(f"Error: {e}")
