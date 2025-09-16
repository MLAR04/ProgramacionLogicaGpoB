#-------------------------------------------------------------------------------#
#   Escribe una función recursiva que calcule el n-ésimo número de Fibonacci.   #
#-------------------------------------------------------------------------------#

def fibonacci(param: int):
    return 0 if param == 1 else 1 if param == 2 else fibonacci(param - 2) + fibonacci(param - 1)# retornar el numero n-esimo de fibonacci


if __name__ == '__main__':
    print(fibonacci(6))