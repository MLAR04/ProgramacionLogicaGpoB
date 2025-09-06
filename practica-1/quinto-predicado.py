monto_cuenta = {"Paco": 10000}

def es_exacto(monto_a_buscar):
    for persona in monto_cuenta:
        if monto_a_buscar == monto_cuenta[persona]:
            print(f"El monto de la cuenta de {persona} es de ${monto_a_buscar} exactos?")
            return True
        elif monto_a_buscar < monto_cuenta[persona]:
            print(f"El monto en la cuenta de {persona} es menor a ${monto_a_buscar}?")
            return False
        else: 
            return False

if __name__ == '__main__':
    print(es_exacto(10000))
    print(es_exacto(5000))


