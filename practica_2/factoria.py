# Implementa una función recursiva
# factorial(n) que calcule el factorial.

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)

if __name__ == "__main__":
    n: int = 5
    print(factorial(n))