# Caso 2. Saber si puede votar

def puedeVotar(mayorEdad: bool, tieneCredencial: bool, listaNominal: bool) -> bool:
    return mayorEdad and (tieneCredencial and listaNominal)

if __name__ == "__main__":
    print("Rg | R1 | R2 | R3 \n-----------------")
    for _ in range(2):
        for i in range(2):
            for j in range(2):
                print(f"{puedeVotar(_, i, j)}  | {_}  | {i}  | {j}")
                print("-----------------")