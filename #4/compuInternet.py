# Pedir datos
R1 = input("¿Wi-Fi activado? (s/n): ").lower() == 's'
R2 = input("¿Cable Ethernet conectado? (s/n): ").lower() == 's'
R3 = input("¿El módem funciona? (s/n): ").lower() == 's'

# Regla general
RG = (R1 or R2) and R3

# Mostrar resultado de la computadora
print("\nPuede conectarse a internet:", "V" if RG else "F")

# Tabla de verdad
print("\nTabla de verdad")
print("R1  R2  R3  R1∨R2  (R1∨R2)∧R3")
for r1 in [True, False]:
    for r2 in [True, False]:
        for r3 in [True, False]:
            print(
                ("V" if r1 else "F"),
                ("V" if r2 else "F"),
                ("V" if r3 else "F"),
                ("V" if (r1 or r2) else "F"),
                ("V" if ((r1 or r2) and r3) else "F")
            )
