# Escribe una función recursiva que calcule
# el n-ésimo número de Fibonacci.

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    n = 80
    print(fibonacci(n))