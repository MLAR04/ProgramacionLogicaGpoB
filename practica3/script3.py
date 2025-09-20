"""
Una computadora puede conectarse a internet si tiene Wi-Fi activado o 
cable Ethernet conectado, y además el módem funciona

Rg → Una computadora puede conectarse a internet
R1 → tiene Wi-Fi activado
R2 → cable Ethernet conectado
R3 → el módem funciona
"""
def conectar_internet(r1, r2, r3):
    return ((r1 or r2) and r3)

if __name__ == "__main__":
    print("R1 | R2 | R3 | Rg")
    for i in reversed(range(2)):
        for j in reversed(range(2)):
            for h in reversed(range(2)):
                print(i, " | ", j, " | ", h, " | ", conectar_internet(i, j, h))
