
# n es el numero fibonacci ques e queire calcular
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
if __name__ == "__main__":
    print("10mo numero fibonacci", fibonacci(10))