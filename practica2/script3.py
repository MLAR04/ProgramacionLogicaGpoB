"""
Función que calcula el n-ésimo número de la serie de Fibonacci
"""
def serie_fibonacci(posicion):
    contador = 1
    if contador == posicion:
        return 0
    else:
        a, b = 0, 1
        while contador < posicion - 1:
            a, b = b, a + b
            contador += 1
        return b 

if __name__ == "__main__":
    print(serie_fibonacci(2))