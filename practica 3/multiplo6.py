#enunciado = Un número es múltiplo de 6 si es divisible entre 2 y divisible entre 3.

# Este programa evalua la regla logica de si un numero es multiplo de 6
# Reglas:
# r1: El numero es divisible entre 2
# r2: El numero es divisible entre 3
# Regla General: Multiplo de 6 si (r1 Aand r2)


# ------------------------------------------------------------------------
# TABLA DE VERDAD RESULTANTE:
#
# r1 (Divisible entre 2) | r2 (Divisible entre 3) | (r1 ∧ r2) | Multiplo de 6
# ----------------------------------------------------------------------------
#          V              |           V            |     V     |      V
#          V              |           F            |     F     |      F
#          F              |           V            |     F     |      F
#          F              |           F            |     F     |      F
# ------------------------------------------------------------------------

# Mostrar reglas y expresion general
print("REGLAS:")
print("r1: El numero es divisible entre 2")
print("r2: El numero es divisible entre 3")
print("\nRegla General: Multiplo de 6 si (r1 ∧ r2)\n")

# Lista de posibles valores de verdad
valores = [True, False]

# Encabezado de la tabla de verdad
print("Tabla de Verdad:")
print("r1\t r2\t (r1 ∧ r2)\t Multiplo de 6")

# Generar todas las combinaciones posibles de r1 y r2
for r1 in valores:
    for r2 in valores:
        resultado = r1 and r2
        print(f"{r1}\t {r2}\t {resultado}\t\t {resultado}")
