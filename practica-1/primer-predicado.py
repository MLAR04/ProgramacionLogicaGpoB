entidad_finaciera = {"banco":["Felipe"]}

def es_cliente(persona):
    for banco in entidad_finaciera:
        print(persona + " es cliente registrado?")
        if persona in entidad_finaciera[banco]:
            return True
    return False



if __name__ == '__main__':
    print(es_cliente("Felipe"))
    print(es_cliente("David"))