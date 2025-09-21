# Un número es múltiplo de 6 si es divisible entre 2 y divisible entre 3.

def multiplo():
    print(" R1  R2  R ")

  
    numeros = [True, False]
    
    for r2 in numeros:
        for r in numeros:
              #S ↔ R1 ∧ R2
            r1 = r2 and r
            print(f"|  {str(r1)[0]}    |  {str(r2)[0]}    |  {str(r)[0]}    |")


if __name__ == "__main__":
    multiplo()
