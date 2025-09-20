# REGLAS
# R1: cuenta con wifi
# R2: cable ethernet
# R3: modem funciona
#
# REGLA GRAL
# puede conectarse a internet
#
# Rg -> (R1 Or R2) AND R3
#
# TABLA DE VERDAD
# R1 | R2 | R3 | puede conectarse a internet
# V  | V  | V  |    V
# V  | V  | F  |    F
# V  | F  | V  |    V
# V  | F  | F  |    F
# F  | V  | V  |    V
# F  | V  | F  |    F
# F  | F  | V  |    F  
# F  | F  | F  |    F  

def puede_conectarse(R1, R2, R3):
    return (R1 or R2) and R3


if __name__ == "__main__":
    print(f"{'R1':<6}{'R2':<6}{'R3':<6}{' (R1 OR R2) AND R3':<20}")
    print("-" * 38)

    for R1 in [False, True]:
        for R2 in [False, True]:
            for R3 in [False, True]:
                resultado = puede_conectarse(R1, R2, R3)
                print(f"{str(R1):<6}{str(R2):<6}{str(R3):<6}{str(resultado):<20}")
