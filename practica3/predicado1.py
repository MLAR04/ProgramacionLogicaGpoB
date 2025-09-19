# Un número es múltiplo de 6 si es divisible entre 2 y divisible entre 3.

def es_multiplo_de_6(R1:bool, R2:bool)->bool:
    '''
    R1 = Es divisible entre 2
    R2 = Es divisible entre 3
    '''
    return R1 and R2

if __name__ == '__main__':
    print('S R1 ^ R2')
    print("-------------")
    print(" R1 | R2 | S")
    for r1 in range(2):
        for r2 in range(2):
            print("-------------")
            print(f"  {r1} |  {r2} | {es_multiplo_de_6(r1,r2)}")
