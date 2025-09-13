def fact(n):
    if n == 0 or n == 1 or n<0:
        return 1
    else:
        res= n * fact(n-1)
        return res

if __name__ == '__main__':
    print(fact(3))
