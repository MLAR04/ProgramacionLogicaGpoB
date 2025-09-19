# Caso 3. Saber si una computadora puede conectarse a internet

def tenerInternet(wiki: bool, ethernet: bool, modem: bool) -> bool:
    return (wiki or ethernet) and modem

if __name__ == "__main__":
    print("Rg | R1 | R2 | R3 \n-----------------")
    for _ in range(2):
        for i in range(2):
            for j in range(2):
                print(f"{tenerInternet(_, i, j)}  | {_}  | {i}  | {j}")
                print("-----------------")
