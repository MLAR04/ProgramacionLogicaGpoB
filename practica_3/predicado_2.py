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

# Una persona puede votar si tiene más de 18 años, 
# tiene credencial de elector y está en la lista nominal.
def puede_votar(r1, r2, r3):
    return r1 and r2 and r3

if __name__ == "__main__":
    # Se inicializa un objeto tabla con los headers
    reglas = Table(headers=headers)

    # Para cada fila se hace una iteración
    for i in values:
        # Se agrega una fila para cada valor posible
        s = puede_votar(i[0], i[1], i[2])
        reglas.add_row([i[0], i[1], i[2], s])
    print(reglas) # se imprime la tabla