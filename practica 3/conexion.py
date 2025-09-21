# enunciado = Una computadora puede conectarse a internet si tiene Wi-Fi activado
#             o cable Ethernet conectado, y ademas el modem funciona.

# Este programa evalua la regla logica de si una computadora puede conectarse a internet
# Reglas:
# r1: Wi-Fi activado
# r2: Cable Ethernet conectado
# r3: El modem funciona
# Regla General: Conexion a Internet si ( (r1 ∨ r2) ∧ r3 )

# TABLA DE VERDAD RESULTANTE:
#
# r1 (Wi-Fi) | r2 (Ethernet) | r3 (Modem) | (r1 ∨ r2) | ((r1 ∨ r2) ∧ r3) | Conexion
# ------------------------------------------------------------------------------
#    V       |       V       |     V      |     V     |        V          |   V
#    V       |       V       |     F      |     V     |        F          |   F
#    V       |       F       |     V      |     V     |        V          |   V
#    V       |       F       |     F      |     V     |        F          |   F
#    F       |       V       |     V      |     V     |        V          |   V
#    F       |       V       |     F      |     V     |        F          |   F
#    F       |       F       |     V      |     F     |        F          |   F
#    F       |       F       |     F      |     F     |        F          |   F
# ------------------------------------------------------------------------

# Mostrar reglas y expresion general
print("REGLAS:")
print("r1: Wi-Fi activado")
print("r2: Cable Ethernet conectado")
print("r3: El modem funciona")
print("\nRegla General: Conexion a Internet si ( (r1 ∨ r2) ∧ r3 )\n")

# Lista de posibles valores de verdad
valores = [True, False]

# Encabezado de la tabla de verdad
print("Tabla de Verdad:")
print("r1\t r2\t r3\t (r1 ∨ r2)\t ((r1 ∨ r2) ∧ r3)\t Conexion")

# Generar todas las combinaciones posibles de r1, r2 y r3
for r1 in valores:
    for r2 in valores:
        for r3 in valores:
            parcial = r1 or r2        # evaluacion de (r1 ∨ r2)
            resultado = parcial and r3  # evaluacion de ((r1 ∨ r2) ∧ r3)
            print(f"{r1}\t {r2}\t {r3}\t {parcial}\t\t {resultado}\t\t {resultado}")



