# Esta es una libreria que ayuda a realizar tablas de una manera mas presentable
# En este caso se utilizo para las tablas de verdad 
from prettytable import PrettyTable


# --- 1. Un número es múltiplo de 6 si es divisible entre 2 y divisible entre 3 ---
def tabla_multiplo_seis():
    tabla = PrettyTable()
    tabla.field_names = ["Divisible_2", "Divisible_3", "Multiplo_6"]

    for d2 in [True, False]:
        for d3 in [True, False]:
            multiplo = d2 and d3
            tabla.add_row([d2, d3, multiplo])

    print("Tabla de verdad: Multiplo de 6")
    print(tabla, "\n")


# --- 2. Una persona puede votar si tiene más de 18, credencial y está en lista nominal ---
def tabla_votar():
    tabla = PrettyTable()
    tabla.field_names = ["Mayor_18", "Credencial", "Lista", "Puede_Votar"]

    for m18 in [True, False]:
        for cred in [True, False]:
            for lista in [True, False]:
                votar = m18 and cred and lista
                tabla.add_row([m18, cred, lista, votar])

    print("Tabla de verdad: Puede Votar")
    print(tabla, "\n")


# --- 3. Una computadora puede conectarse a internet si (wifi o ethernet) y modem funciona ---
def tabla_internet():
    tabla = PrettyTable()
    tabla.field_names = ["WiFi", "Ethernet", "Modem", "Internet"]

    for wifi in [True, False]:
        for eth in [True, False]:
            for modem in [True, False]:
                internet = (wifi or eth) and modem
                tabla.add_row([wifi, eth, modem, internet])

    print("Tabla de verdad: Internet")
    print(tabla, "\n")


if __name__ == "__main__":
    tabla_multiplo_seis()
    tabla_votar()
    tabla_internet()