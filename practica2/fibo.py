def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        res= fibonacci(n-2) + fibonacci(n-1)
        return res

if __name__ == '__main__':
    print(fibonacci(4))
