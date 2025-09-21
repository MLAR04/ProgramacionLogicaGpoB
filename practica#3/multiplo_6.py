def es_multiplo_de_6(divisible_por_2, divisible_por_3):
  
    return divisible_por_2 and divisible_por_3

# Simulación de la regla:
print("--- Regla de Múltiplo de 6 ---")
es_d2 = input("¿El número es divisible entre 2? (s/n): ").lower() == 's'
es_d3 = input("¿El número es divisible entre 3? (s/n): ").lower() == 's'

resultado = es_multiplo_de_6(es_d2, es_d3)
print(f"\n¿El número es múltiplo de 6? {'Sí' if resultado else 'No'}")

# Tabla de Verdad (Conjunción: P AND Q)
print("\n--- Tabla de Verdad (Divisible por 2 Y Divisible por 3) ---")
print("| Divisible x 2 (P) | Divisible x 3 (Q) | Múltiplo de 6 (P ∧ Q) |")
print("|-------------------|-------------------|------------------------|")

# P = Divisible x 2, Q = Divisible x 3, P ∧ Q = Múltiplo de 6
combinaciones = [
    (True, True),
    (True, False),
    (False, True),
    (False, False)
]

for p, q in combinaciones:
    r = es_multiplo_de_6(p, q)
    # Formateo para la tabla
    p_str = "V" if p else "F"
    q_str = "V" if q else "F"
    r_str = "V" if r else "F"
    print(f"| {p_str:<17} | {q_str:<17} | {r_str:<22} |")
