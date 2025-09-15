def fibonacci(num):
    if num in {0, 1}: 
        return num
    return fibonacci(num - 1) + fibonacci(num - 2) 

resul = [fibonacci(n) for n in range(8)]
print(resul)