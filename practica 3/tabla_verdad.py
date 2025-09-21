casos_2 = [
    (False, False),
    (False, True),
    (True, False),
    (True, True)
]

casos_3 = [
    (False, False, False),
    (False, False, True),
    (False, True, False),
    (False, True, True),
    (True, False, False),
    (True, False, True),
    (True, True, False),
    (True, True, True)
]

def tabla_verdad_2(f):
    print("R1\tR2\tRg")
    for a, b in casos_2:
        print(f"{a}\t{b}\t{f(a, b)}")

def tabla_verdad_3(f):
    print("R1\tR2\tR3\tRg")
    for a, b, c in casos_3:
        print(f"{a}\t{b}\t{c}\t{f(a, b, c)}")

# -----------------------------
# Caso 1: múltiplo de 6
def caso_multiplo_6():
    print("\nCaso 1: Es múltiplo de 6")
    tabla_verdad_2(lambda R1, R2: R1 and R2)

# Caso 2: persona puede votar
def caso_puede_votar():
    print("\nCaso 2: Una persona puede votar")
    tabla_verdad_3(lambda R1, R2, R3: R1 and R2 and R3)

# Caso 3: conexión a internet
def caso_conexion_internet():
    print("\nCaso 3: Una computadora tiene conexión a internet")
    tabla_verdad_3(lambda R1, R2, R3: (R1 or R2) and R3)

# -----------------------------

if __name__ == "__main__":
    caso_multiplo_6()
    caso_puede_votar()
    caso_conexion_internet()
