# Una computadora puede conectarse a internet si tiene Wi-Fi activado o cable Ethernet conectado, y además el módem funciona.

def puede_acceder_a_internet(R1:bool, R2:bool, R3:bool)->bool:
    '''
    R1 = Tiene Wi-Fi activado
    R2 = Tiene cable Ethernet conectado
    R3 = El modem funciona
    '''
    return (R1 or R2) and R3

if __name__ == '__main__':
    print('S (R1 v R2) ^ R3')
    print("------------------")
    print(" R1 | R2 | R3 | S")
    for r1 in range(2):
        for r2 in range(2):
            for r3 in range(2):
                print("------------------")
                print(f"  {r1} |  {r2} |  {r3} | {puede_acceder_a_internet(r1,r2,r3)}")
