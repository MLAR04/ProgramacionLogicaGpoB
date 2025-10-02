def verificar_multiplo_6(numero: int):
    R1 = (numero % 2 == 0)   
    R2 = (numero % 3 == 0)   
    RG = R1 and R2           

    print("\nRESULTADOS PARA EL NUMERO INGRESADO:")
    print(f"R1 (divisible entre 2): {R1}")
    print(f"R2 (divisible entre 3): {R2}")
    print(f"Regla General (R1 ∧ R2): {RG}")

    print("\nTABLA DE VERDAD")
    print(f"{'R1':<6}{'R2':<6}{'R1 ∧ R2':<8}")
    print("-" * 20)
    for r1 in [True, False]:
        for r2 in [True, False]:
            print(f"{str(r1):<6}{str(r2):<6}{str(r1 and r2):<8}")

def main():
    numero = int(input("Ingresa un numero: "))
    verificar_multiplo_6(numero)

if __name__ == "__main__":
    main()