# Serie de fibonacci

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
if __name__ == "__main__":
    print("Los primeros 30 números de la serie de Fibonacci son:")
    for i in range(30):
        print(fibonacci(i), end=" ")
    print()
