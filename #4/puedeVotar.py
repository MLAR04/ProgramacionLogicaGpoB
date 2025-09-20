#datos
R1 = input("¿Tiene mas de 18 años? (s/n): ").lower() == 's'
R2 = input("¿Tiene credencial de elector? (s/n): ").lower() == 's'
R3 = input("¿Esta en lista nominal? (s/n): ").lower() == 's'

# Regla general
RG = R1 and R2 and R3


print("\nPuede votar:", "V" if RG else "F")


print("\nTabla de verdad")
print("R1  R2  R3  R1∧R2∧R3")
for r1 in [True, False]:
    for r2 in [True, False]:
        for r3 in [True, False]:
            print(
                ("V" if r1 else "F"),
                ("V" if r2 else "F"),
                ("V" if r3 else "F"),
                ("V" if (r1 and r2 and r3) else "F")
            )
