import itertools

def puede_votar():
    """
    Genera la tabla de verdad para el predicado:
    'Una persona puede votar si tiene más de 18 años, tiene credencial de elector y está en
    la lista nominal.'
    Se establece la Regla General RG: R1 and (R2 and R3)
    """
    print("  R1   |   R2   |   R3   |   S   ")
    print("-------|--------|--------|-------")
     # Primero genero todas las combinaciones posibles entre R1, R2 y R3
    for R1, R2, R3 in itertools.product([True, False], repeat=3):
        # Evaluo mi regla genenral
        S = R1 and (R2 and R3)
        #Imprimo la tabla de verdad
        print(f" {str(R1):<5} | {str(R2):<6} | {str(R3):<6} | {S} ") 

if __name__ == '__main__':
    puede_votar()
                