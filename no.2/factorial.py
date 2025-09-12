
# n es el numero al que se le quiere sacar el factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    

if __name__ == "__main__":
    print("factorial de 3",factorial(3))