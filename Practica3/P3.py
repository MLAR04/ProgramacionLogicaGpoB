# 1) Un número es múltiplo de 6 si es divisible entre 2 y 3
def multiploDe6(div2: bool, div3: bool) -> bool:
    return div2 and div3


# 2) Una persona puede votar si tiene más de 18 años, tiene credencial de elector y está en la lista nominal
def puedeVotar(edad: bool, credencial: bool, lista: bool) -> bool:
    return edad and credencial and lista


# 3) Una computadora puede conectarse a internet si, tiene Wi-Fi activado o cable Ethernet conectado, y además el módem funciona
def tenerInternet(wifi: bool, ethernet: bool, modem: bool) -> bool:
    return (wifi or ethernet) and modem


# Tablas de verdad
if __name__ == "__main__":

    # 1. Tabla de verdad múltiplo de 6

    print("1) Múltiplo de 6")
    print("Rg | R1 | R2")
    print("---------------")
    for d2 in range(2):
        for d3 in range(2):
            print(f"{int(multiploDe6(d2, d3))}  | {d2}  | {d3}")
            print("---------------")
    print("\n")

    # 2. Tabla de verdad votar
    print("2) Puede votar")
    print("Rg | R1 | R2 | R3")
    print("-----------------")
    for a in range(2):
        for c in range(2):
            for l in range(2):
                print(f"{int(puedeVotar(a, c, l))}  | {a}  | {c}  | {l}")
                print("-----------------")
    print("\n")


    # 3. Tabla de verdad internet
    print("3) Conexión a internet")
    print("Rg | R1 | R2 | R3")
    print("-----------------")
    for w in range(2):
        for e in range(2):
            for m in range(2):
                print(f"{int(tenerInternet(w, e, m))}  | {w}  | {e}  | {m}")
                print("-----------------")
