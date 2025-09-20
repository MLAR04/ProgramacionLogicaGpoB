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

def multiplo_de_6(R1, R2   ):
    return R1 and R2



if __name__ == "__main__":
    print(f"{'R1':<6}{'R2':<6}{'R1 AND R2':<10}")
    print("-" * 25)

    for R1 in [False, True]:
        for R2 in [False, True]:
            resultado = multiplo_de_6(R1, R2)
            print(f"{str(R1):<6}{str(R2):<6}{str(resultado):<10}")
