def puede_votar(mayor_18, credencial, lista_nominal):
   
    return mayor_18 and credencial and lista_nominal

# Simulación de la regla:
print("--- Regla de Voto ---")
es_m18 = input("¿Tiene más de 18 años? (s/n): ").lower() == 's'
tiene_credencial = input("¿Tiene credencial de elector? (s/n): ").lower() == 's'
esta_nominal = input("¿Está en la lista nominal? (s/n): ").lower() == 's'

resultado = puede_votar(es_m18, tiene_credencial, esta_nominal)
print(f"\n¿La persona puede votar? {'Sí' if resultado else 'No'}")

# Tabla de Verdad (Conjunción Triple: P AND Q AND R)
print("\n--- Tabla de Verdad (Mayor 18 Y Credencial Y Lista Nominal) ---")
print("| P (+18) | Q (Credencial) | R (Nominal) | Votar (P ∧ Q ∧ R) |")
print("|---------|----------------|-------------|-------------------|")

# P = +18, Q = Credencial, R = Nominal. 2^3 = 8 combinaciones
combinaciones = [
    (True, True, True),
    (True, True, False),
    (True, False, True),
    (True, False, False),
    (False, True, True),
    (False, True, False),
    (False, False, True),
    (False, False, False)
]

for p, q, r_nom in combinaciones:
    r_voto = puede_votar(p, q, r_nom)
    # Formateo para la tabla
    p_str = "V" if p else "F"
    q_str = "V" if q else "F"
    r_nom_str = "V" if r_nom else "F"
    r_voto_str = "V" if r_voto else "F"
    print(f"| {p_str:<7} | {q_str:<14} | {r_nom_str:<11} | {r_voto_str:<17} |")
