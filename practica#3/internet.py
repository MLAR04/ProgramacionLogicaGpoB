def puede_conectar_internet(wifi, ethernet, modem):
  
    conectividad = wifi or ethernet # P OR Q
    return conectividad and modem      # (P OR Q) AND R

# Simulación de la regla:
print("--- Regla de Conexión a Internet ---")
hay_wifi = input("¿Tiene Wi-Fi activado? (s/n): ").lower() == 's'
hay_ethernet = input("¿Tiene cable Ethernet conectado? (s/n): ").lower() == 's'
modem_ok = input("¿El módem funciona? (s/n): ").lower() == 's'

resultado = puede_conectar_internet(hay_wifi, hay_ethernet, modem_ok)
print(f"\n¿La computadora puede conectarse a internet? {'Sí' if resultado else 'No'}")

# Tabla de Verdad (Disyunción y Conjunción: (P OR Q) AND R)
print("\n--- Tabla de Verdad ((Wi-Fi O Ethernet) Y Módem) ---")
print("| P (Wi-Fi) | Q (Ethernet) | P ∨ Q | R (Módem) | Conecta ((P ∨ Q) ∧ R) |")
print("|-----------|--------------|-------|-----------|-----------------------|")

# P = Wi-Fi, Q = Ethernet, R = Módem. 2^3 = 8 combinaciones
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

for p, q, r_modem in combinaciones:
    p_o_q = p or q
    r_conecta = puede_conectar_internet(p, q, r_modem)
    # Formateo para la tabla
    p_str = "V" if p else "F"
    q_str = "V" if q else "F"
    p_o_q_str = "V" if p_o_q else "F"
    r_modem_str = "V" if r_modem else "F"
    r_conecta_str = "V" if r_conecta else "F"
    print(f"| {p_str:<9} | {q_str:<12} | {p_o_q_str:<5} | {r_modem_str:<9} | {r_conecta_str:<21} |")
