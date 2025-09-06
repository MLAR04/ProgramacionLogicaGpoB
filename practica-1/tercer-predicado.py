instituciones_financieras = {"Santander": ["Felipe"]}

def realizar_transacciones(cliente):
    for banco in instituciones_financieras:
        print(cliente + " puede realizar transaciones?")
        if cliente in instituciones_financieras[banco]:
            return True
    return False

def tiene_cuenta(x):
    for banco in instituciones_financieras:
        print(x + " tiene cuenta?")
        if x in instituciones_financieras[banco]:
            return True
    return False

if __name__ == '__main__':
    print(realizar_transacciones("Felipe"))
    print(tiene_cuenta("Diego"))