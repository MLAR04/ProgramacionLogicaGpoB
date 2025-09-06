bancos = {
    "hsbc": {
        "clientes" : {
            "pedro": {
                "saldo" : [20000, 30000]
            },
        },
        "prestamos" : ["hipotecario"]
    },
}

# 1. ¿Quienes son clientes?
def quienes_son_clientes():
    clientes_list = []
    for banco in bancos: 
        for cliente in bancos[banco]["clientes"]:
            print(cliente)
            clientes_list.append(cliente)


# 2. X es cliente: return True
def es_cliente(x):
    for banco in bancos:
        if x in bancos[banco]["clientes"]:
            return True
    return False

# 3. hay mas bancos: False
def mas_bancos(y):
    total_bancos = len(bancos)
    if y in bancos and total_bancos > 1:
        return True
    return False

# 4. Y es banco: return True
def es_banco(y):
    if y in bancos:
        return True
    return False

# 5. X tiene mas cuentas de banco? : return False
def mas_cuentas(x):
    cuentas = 0
    # Recorremos todos los bancos
    for banco, datos in bancos.items():
        if x in datos["clientes"]:
            cuentas += 1
    return cuentas > 1

# 6. De quien tiene registro Y: return ["pedro"]
def registros_banco(y):
    clientes_banco = []
    for banco in bancos:
        if banco == y:
            for key in bancos[banco]["clientes"]:
                clientes_banco.append(key)
            return(clientes_banco)
    return "No Existen registros"

# 7. "Y" genera prestamos del tipo "N": return True
def genera_prestamos(y, n):
    for banco in bancos:
        if banco == y:
            if n in bancos[banco]["prestamos"]:
                return True
        return False

# 8. Que tipo de prestamos genera Y: return ["hipotecario"]
def tipo_prestamos(y):
    tipo_prestamos = []
    for banco in bancos:
        if banco == y:
            for prestamo in bancos[banco]["prestamos"]:
                tipo_prestamos.append(prestamo)
            return tipo_prestamos
    return "no existe este banco"

# 9. X recibio más montos? : return false
def recibio_montos(x):
    for banco in bancos:
        for cliente in bancos[banco]["clientes"]:
            if cliente == x:
                return False if len(bancos[banco]["clientes"][cliente]["saldo"]) == 1 else True

# 10. ¿Quien recibio un monto de Z?
def quien_recibe(monto):
    usuarios = []
    for banco, datos in bancos.items():
        for cliente, info in datos["clientes"].items():
            if monto in info["saldo"]:
                usuarios.append(cliente)
    return list(set(usuarios))

if __name__ == "__main__":
    print(quien_recibe(20000))