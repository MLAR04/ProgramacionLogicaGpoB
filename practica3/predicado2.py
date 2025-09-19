# Una persona puede votar si tiene más de 18 años, tiene credencial de elector y está en la lista nominal.

def puede_votar(R1:bool, R2:bool, R3:bool)->bool:
    '''
    R1 = Tiene mas de 18 años
    R2 = Tiene credencial
    R3 = Esta en la lista nominal
    '''
    return R1 and R2 and R3

if __name__ == '__main__':
    print('S R1 ^ R2 ^ R3')
    print("------------------")
    print(" R1 | R2 | R3 | S")
    for r1 in range(2):
        for r2 in range(2):
            for r3 in range(2):
                print("------------------")
                print(f"  {r1} |  {r2} |  {r3} | {puede_votar(r1,r2,r3)}")
