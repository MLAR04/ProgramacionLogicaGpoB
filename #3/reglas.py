from itertools import product

# Función para imprimir tabla de verdad
def tabla_verdad(n, regla):
    # Genera el encabezado
    encabezado = [f"R{i+1}" for i in range(n)] + ["Rg (S)"]
    print(" | ".join(encabezado))
    print("-" * (5*n + 6))
    
    # Genera todas las combinaciones (0,1) de n proposiciones
    for valores in product([0,1], repeat=n):
        R = dict(zip([f"R{i+1}" for i in range(n)], valores))
        resultado = regla(*valores)  # evalúa la regla
        fila = list(valores) + [int(resultado)]
        print("  |  ".join(str(x) for x in fila))

#  Caso 1: múltiplo de 6 
print("\nCaso 1: Es múltiplo de 6")
tabla_verdad(2, lambda R1, R2: R1 and R2)

# Caso 2: persona puede votar 
print("\nCaso 2: Una persona puede votar")
tabla_verdad(3, lambda R1, R2, R3: R1 and R2 and R3)

#  Caso 3: conexión a internet 
print("\nCaso 3: Una computadora tine conexión a internet")
tabla_verdad(3, lambda R1, R2, R3: (R1 or R2) and R3)
