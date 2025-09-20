# Flores Hernandez Roberto David

# Un número es múltiplo de 6 si es divisible entre 2 y divisible entre 3.
# R1: divisible entre 2
# R2: divisible entre 3
# R3: múltiplo de 6
# Rg: R3 <-> (R1 and R2)
def F1(r1, r2):
    return r1 and r2

def tabla_F1():
    print("TABLA — Múltiplo de 6")
    print("R1 | R2 | R3")
    for r1 in [True, False]:
        for r2 in [True, False]:
            r3 = F1(r1, r2)
            print(r1, "|", r2, "|", r3)
    print()


# Una persona puede votar si tiene más de 18 años, tiene credencial de elector y está en la lista nominal.
# R1: >18 años
# R2: tiene credencial
# R3: en lista nominal
# R4: puede votar
# Rg: R4 <-> (R1 and R2 and R3)
def F2(r1, r2, r3):
    return r1 and r2 and r3

def tabla_F2():
    print("TABLA — Persona puede votar")
    print("R1 | R2 | R3 | R4")
    for r1 in [True, False]:
        for r2 in [True, False] :
            for r3 in [True, False]:
                r4 = F2(r1, r2, r3)
                print(r1, "|", r2, "|", r3, "|", r4)
    print()


# Una computadora puede conectarse a internet si tiene Wi-Fi activado o cable Ethernet conectado, y además el módem funciona.
# R1: Wi-Fi activado
# R2: Ethernet conectado
# R3: Módem funciona
# R4: puede conectarse
# Rg: R4 <-> ((R1 or R2) and R3)
def F3(r1, r2, r3):
    return (r1 or r2) and r3

def tabla_F3():
    print("TABLA F3 — Computadora conectada a internet")
    print("R1 | R2 | R3 | R4")
    for r1 in [True, False]:
        for r2 in [True, False] :
            for r3 in [True, False]:
                r4 = F3(r1, r2, r3)
                print(r1, "|", r2, "|", r3, "|", r4)
    print()


def main():
    tabla_F1()
    tabla_F2()
    tabla_F3()

if __name__ == "__main__":
    main()

"""
-------------------------
RESULTADOS
-------------------------



TABLA — Múltiplo de 6
R1 | R2 | R3
True | True | True
True | False | False
False | True | False
False | False | False

TABLA — Persona puede votar
R1 | R2 | R3 | R4
True | True | True | True
True | True | False | False
True | False | True | False
True | False | False | False
False | True | True | False
False | True | False | False
False | False | True | False
False | False | False | False

TABLA F3 — Computadora conectada a internet
R1 | R2 | R3 | R4
True | True | True | True
True | True | False | False
True | False | True | True
True | False | False | False
False | True | True | True
False | True | False | False
False | False | True | False
False | False | False | False 
"""