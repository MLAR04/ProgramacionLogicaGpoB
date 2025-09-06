instituciones_financieras = {"Santander": ["Carla"], "Scotiabank": ["Pedro"]}

def es_cliente_santander(cliente):
    for banco in instituciones_financieras:
        print(cliente + " es cliente " + banco + "?")
        if cliente in instituciones_financieras[banco]:
            return True
    return False

def es_abarrotes(x):
    print(x + " es abarrotes?")
    if x in instituciones_financieras:
        return False
    return True



if __name__ == '__main__':
    print(es_cliente_santander("Carla"))
    print(es_abarrotes("Scotiabank"))