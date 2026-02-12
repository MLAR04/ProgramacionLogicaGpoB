
def multiplo_6():
    print(f"{'R1':<2} {'^ R2':<5} {'RG':<20}")
    print("-"*30)
    valores = [True, False]
    
    for r1 in valores:
        for r2 in valores:
            regla_general = r1 and r2
            print(f"{str(r1):<5} {str(r2):<5} {str(regla_general):<20}")
    print("\n")

def puede_votar():
    print(f"{'R1':<10} {'^ R2':<10} {'^ R3':<10} {'RG':<30}")
    print("-"*60)
    valores = [True, False]
    
    for r1 in valores:
        for r2 in valores:
            for r3 in valores:
                regla_general = r1 and r2 and r3
                print(f"{str(r1):<10} {str(r2):<10} {str(r3):<10} {str(regla_general):<30}")
    print("\n")

def puede_tener_internet():
    print(f"{'(R1':<10} {'v R2)':<12} {'^ R3':<10} {'RG':<30}")
    print("-"*70)
    valores = [True, False]
    
    for r1 in valores:
        for r2 in valores:
            for r3 in valores:
                regla_general = (r1 or r2) and r3
                print(f"{str(r1):<10} {str(r2):<12} {str(r3):<10} {str(regla_general):<30}")



multiplo_6()
puede_votar()
puede_tener_internet()