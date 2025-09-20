import itertools

def es_multiplo_seis(param: int):
    """
    Genera la tabla de verdad para el predicado:
    'Un número es múltiplo de 6 ↔ (divisible entre 2 y divisible entre 3)'
    con el número n.
    Se establece la Regla General RG: R1 and R2
    """

    R1 = (param % 2 == 0)
    R2 = (param % 3 == 0)

    print("  R1   |   R2   |   S   ")
    print("-------|--------|-------")
    # Primero genero las conbinaciones posibles con itertools
    for R1, R2 in itertools.product([True, False], repeat=2):
        # Evaluo con mi regla general
        S = R1 and R2 
        # Imprimo la tabla de verdad
        print(f" {str(R1):<5} | {str(R2):<6} | {S}")




if __name__ == '__main__':
    es_multiplo_seis(12)