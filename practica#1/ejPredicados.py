clients = {"person"}
banks = {"bank"}
accounts = {("person", "bank")}
loans = {("bank", "costco")}
receipts = {("person", 5000)}
accounts_per_bank = {
    "bank": {"person"}
}
loans_per_bank = {
    "bank": {"costco", "big cookie"}
}

# ver si X es un cliente
def is_client(x):
    if x in clients:  # ver si esta en lista de clientes
        return True
    for (person, bank) in accounts:  # si no, ver si su nombre esta en lista de cuentas
        if person == x:
            return True
    return False

# ver si Y es un banco
def is_bank(y):
    if y in banks:  # ver si esta en la lista de bancos
        return True
    if y in loans_per_bank and len(loans_per_bank[y]) > 0:  # ver si existe y puede generar un prestamo
        return True
    return False

# ver si X tiene una cuenta en el banco Y
def has_account(x, y):
    if (x, y) in accounts:  # ver si estan afiliados juntos
        return True
    if is_client(x) and is_bank(y):  # ver si existen individualmente (1/2)
        if y in accounts_per_bank:
            for account in accounts_per_bank[y]:  # y si estan afiliados (2/2)
                if account == x:
                    return True
    return False

# ver si banco Y puede generar prestamos para W
def generate_loan(y, w):
    if (y, w) in loans:  # ver si el banco tiene ese prestamo
        return True
    if is_bank(y):  # ver si existe el banco individualmente (1/2)
        if y in loans_per_bank:
            for loan_type in loans_per_bank[y]:  # y si existe el prestamo en el (2/2)
                if loan_type == w:
                    return True
    return False

# ver si cliente X recibio un monto Z de dinero
def received_money(x, z):
    for (person, amount) in receipts:  # ver si la persona aparece en los recibos
        if person == x and amount == z:
            return True
    return False

# mostrar resultados
def show_results(question, true, false):
    # si esta bien saldra "True? True", y "False? False"
    print(f"\n{question}\n\tTrue? {true}\n\tFalse? {false}")

# 1) "X" es un cliente
t1 = is_client("person")
f1 = is_client("pedro")
show_results(f"1) \"X\" es un cliente", t1, f1)

# 2) "Y" es un banco
t2 = is_bank("bank")
f2 = is_bank("home")
show_results(f"2) \"Y\" es un banco", t2, f2)

# 3) "X" tiene una cuenta en el banco "Y"
t3 = has_account("person", "bank")
f3 = has_account("person", "home")
show_results(f"3) \"X\" tiene una cuenta en el banco \"Y\"", t3, f3)

# 4) "Y" puede generar un préstamo de tipo "W"
t4 = generate_loan("bank", "costco")
f4 = generate_loan("bank", "office depot")
show_results(f"4) \"Y\" puede generar un préstamo de tipo \"W\"", t4, f4)

# 5) "X" recibió un monto "Z" de dinero
t5 = received_money("person", 5000)
f5 = received_money("person", 5)
show_results(f"5) \"X\" recibió un monto \"Z\" de dinero", t5, f5)
