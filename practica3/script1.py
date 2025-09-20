"""
Un numero es multiplo de 6 si es divisible entre 2 y divisible entre 3

Rg → Un número es múltiplo de 6
R1 → es divisible entre 2
R2 → divisible entre 3

"""
def multiplo_de_6(r1, r2):
    return (r1 and r2)

if __name__ == "__main__":
    print("R1 | R2 | Rg")
    for i in reversed(range(2)):    
        for j in reversed(range(2)):
            print(i, " | ", j, " | ", multiplo_de_6(i, j))