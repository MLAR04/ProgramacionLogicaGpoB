# REGLAS
# R1: tiene mas de 18 años
# R2: tiene credencial de elector
# R3: esta en lista nominal
#
# REGLA GRAL
# puede votar
#
# Rg -> R1 AND R2 AND R3
#
# TABLA DE VERDAD
# R1 | R2 | R3 | puede votar
# V  | V  | V  |    V
# V  | V  | F  |    F
# V  | F  | V  |    F
# V  | F  | F  |    F
# F  | V  | V  |    F
# F  | V  | F  |    F
# F  | F  | V  |    F
# F  | F  | F  |    F  

def puede_votar(R1, R2, R3):
    return R1 and R2 and R3

if __name__ == "__main__":
    print(f"{'R1':<6}{'R2':<6}{'R3':<6}{'R1 AND R2 AND R3':<20}")
    print("-" * 38)

    for R1 in [False, True]:
        for R2 in [False, True]:
            for R3 in [False, True]:
                resultado = puede_votar(R1, R2, R3)
                print(f"{str(R1):<6}{str(R2):<6}{str(R3):<6}{str(resultado):<20}")
