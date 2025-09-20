import itertools

def computadora_conectarse_internet():
    """
    Genera la tabla de verdad para el predicado:
    'Una computadora puede conectarse a internet si tiene Wi-Fi activado o cable Ethernet
    conectado, y además el módem funciona.'
    Se establece la Regla General RG: (R1 or R2) and R3
    """

    print("  R1   |   R2   |   R3   |   S   ")
    print("-------|--------|--------|-------")
    # Primero genero todas las combinaciones posibles entre R1, R2 y R3
    for R1, R2, R3 in itertools.product([True, False], repeat=3):
        # Establezco  y evaluo la regla general
        S = (R1 or R2) and R3
        #Imprimo la tabla de verdad
        print(f" {str(R1):<5} | {str(R2):<6} | {str(R3):<6} | {S} ")


if __name__ == '__main__':
    computadora_conectarse_internet()