# Tabla de verdad para "Una persona puede votar
# si tiene más de 18 años, credencial y lista nominal"

def votaciones():
    print("| R1 | R2 | R3 | R |")
   

    numeros = [True, False]
    
    for r1 in numeros:
        for r2 in numeros:
            for r3 in numeros:
                    # R ↔ R1 ∧ R2 ∧ R3
                puede_votar = r1 and r2 and r3
                print(f"|{str(r1)[0]}     | {str(r2)[0]} | {str(r3)[0]} |{str(puede_votar)[0]}  |")


if __name__ == "__main__":
    votaciones()
