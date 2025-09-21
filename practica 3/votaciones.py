# enunciado = Una persona puede votar si tiene mas de 18 anios,
#             tiene credencial de elector y esta en la lista nominal.

# Este programa evalua la regla logica de si una persona puede votar
# Reglas:
# r1: La persona tiene mas de 18 anios
# r2: Tiene credencial de elector
# r3: Esta en la lista nominal
# Regla General: Puede Votar si (r1 ∧ r2 ∧ r3)


# TABLA DE VERDAD RESULTANTE:
#
# r1 (Edad>18) | r2 (Credencial) | r3 (Lista Nominal) | (r1 ∧ r2 ∧ r3) | Puede Votar
# ------------------------------------------------------------------------------
#      V       |        V        |         V          |       V        |     V
#      V       |        V        |         F          |       F        |     F
#      V       |        F        |         V          |       F        |     F
#      V       |        F        |         F          |       F        |     F
#      F       |        V        |         V          |       F        |     F
#      F       |        V        |         F          |       F        |     F
#      F       |        F        |         V          |       F        |     F
#      F       |        F        |         F          |       F        |     F
# ------------------------------------------------------------------------



# Mostrar reglas y expresion general
print("REGLAS:")
print("r1: La persona tiene mas de 18 anios")
print("r2: Tiene credencial de elector")
print("r3: Esta en la lista nominal")
print("\nRegla General: Puede Votar si (r1 ∧ r2 ∧ r3)\n")

# Lista de posibles valores de verdad
valores = [True, False]

# Encabezado de la tabla de verdad
print("Tabla de Verdad:")
print("r1\t r2\t r3\t (r1 ∧ r2 ∧ r3)\t Puede Votar")

# Generar todas las combinaciones posibles de r1, r2 y r3
for r1 in valores:
    for r2 in valores:
        for r3 in valores:
            resultado = r1 and r2 and r3
            print(f"{r1}\t {r2}\t {r3}\t {resultado}\t\t {resultado}")

