# función recursiva que calcule el n-ésimo número de Fibonacci.

def fibonacci(n):
    if (n < 2):
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)
    


if __name__ == '__main__':
    print(fibonacci(18))