# Implementa una función recursiva factorial(n) que calcule el factorial. 

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) # Aqui se aplica la recursividad 
    
print("Factorial de 5:", factorial(5))
  