# REGLAS
# R1: es dibilivle entre 2
# R1: es dibilivle entre 3
#
# REGLA GRAL
# es multiplo de 6
#
# Rg -> R1 AND R2
#
# TABLA DE VERDAD
# R1 | R2 | es multiplo de 6
# V  | V  |    V
# V  | F  |    F
# F  | V  |    F
# F  | F  |    F

def es_multiplo_de_2(n):
    return n % 2 == 0

def es_multiplo_de_3(n):
    return n % 3 == 0



if __name__ == "__main__":
    print(" R1: es multiplo de 2")
    print(" R2: es multiplo de 3")

    print("Resultado: es múltiplo de 6 (R1 AND R2)\n")

    # Encabezado
    print(f"{'n':<5}{'R1':<10}{'R2':<10}{'R1 AND R2':<12}")
    print("-" * 40)

    # Probamos con números del 1 al 12
    for n in range(1, 13):
        r1 = es_multiplo_de_2(n)
        r2 = es_multiplo_de_3(n)
        r3 = r1 and r2
        print(f"{n:<5}{str(r1):<10}{str(r2):<10}{str(r3):<12}")
