# Escribe una función recursiva que calcule el n-ésimo número de Fibonacci.

def fibonacci(n, n1 = 0, n2 = 1, count = 1):
    if count == n:
        return n1
    else:
        return fibonacci(n, n2, n1+n2, count+1)

if __name__ == "__main__":
    print(fibonacci(4))