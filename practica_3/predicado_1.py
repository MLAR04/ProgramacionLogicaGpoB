from prettyTables import Table

#definimos las filas
values = [[True, True],
          [True, False], 
          [False, True],
          [False, False]]
# Inicializamos las columnas variables
headers = ["R1", "R2", "S"]

# Un número es múltiplo de 6 si es divisible entre 2 y divisible entre 3.
def multiplo_de_seis(r1, r2):
    return r1 and r2

if __name__ == "__main__":
    # Se inicializa un objeto tabla con los headers
    reglas = Table(headers=headers)

    # Para cada fila se hace una iteración
    for i in values:
        # Se agrega una fila para cada valor posible
        s = multiplo_de_seis(i[0], i[1])
        reglas.add_row([i[0], i[1], s])
    print(reglas) # se imprime la tabla