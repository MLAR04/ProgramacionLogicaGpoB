#-------------------------------------------------------------------------------#
#   Implementa una función recursiva factorial(n) que calcule el factorial.     #
#-------------------------------------------------------------------------------#

def factorial(param: int):
    return 1 if param <= 1 else param * factorial(param - 1) #retorno el factorial del numero

if __name__ == '__main__':
    print(factorial(10))