from prettyTables import Table

#definimos las filas
values = [[True, True, True],
          [True, True, False],
          [True, False, True],
          [True, False, False],
          [False, True, True],
          [False, True, False],
          [False, False, True],
          [False, False, False]]

# Inicializamos las columnas variables
headers = ["R1", "R2", "R3", "S"]

# Una computadora puede conectarse a internet si tiene Wi-Fi 
# activado o cable Ethernet conectado, y además el módem funciona.
def puede_conectarse_internet(r1, r2, r3):
    return (r1 or r2) and r3

if __name__ == "__main__":
    # Se inicializa un objeto tabla con los headers
    reglas = Table(headers=headers)

    # Para cada fila se hace una iteración
    for i in values:
        # Se agrega una fila para cada valor posible
        s = puede_conectarse_internet(i[0], i[1], i[2])
        reglas.add_row([i[0], i[1], i[2], s])
    print(reglas) # se imprime la tabla