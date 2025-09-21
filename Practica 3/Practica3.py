n = 12  # n numero a comprobar
r1 = n % 2 == 0  # Es divisible entre 2
r2 = n % 3 == 0  # Es divisible entre 3


# Un numero es multipo de 2 si R1 y R2 son verdaderos
def EsMultiplo(R1, R2):
    if R1 and R2:
        S = True
    else:
        S = False
    print("R1", R1, ",R2", R2, "Resultado", S)


print(n, "Es multiplo de 6?")
EsMultiplo(r1, r2)


class Persona:
    # Datos para saber si la persona puede votar
    def __init__(self, nombre, edad, ine, lista):
        self.nombre = nombre
        self.R1 = edad
        self.R2 = ine
        self.R3 = lista

    # Una persona puede votar si R1, R2 y R3 son verdaderas
    def PuedeVotar(self):
        if self.R1 > 18 and self.R2 and self.R3:
            S = True
        else:
            S = False
        print("R1:", self.R1 > 18, "R2:", self.R2, "R3:", self.R3, "Resultado", S)


juan = Persona("Juan", 21, True, True)
print(juan.nombre, "Puede votar?")
juan.PuedeVotar()


# Una computadora puede conectarse a internet si R1 o R2 son verdaderas, y si R3 es verdadero.
def Computadora_Internet(R1, R2, R3):
    if (R1 or R2) and R3:
        S = True
    else:
        S = False

    print("R1:", R1, "R2:", R2, "R3:", R3, "Resultado", S)


print("La computadora puede conectarse a internet?")
Computadora_Internet(True, False, True)
