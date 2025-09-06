bancos = {
    "santander" : {
        'clientes' : {
            'maria' : {'edad' : 27, 'cuenta' : 'ahorro', 'saldo': 15000},
            'carlos' : {'edad' : 38,'cuenta' : 'ahorro', 'saldo' : 8000}
        },
        'prestamos' : ['personal']
    }}

def es_cliente(cliente):
    return any(cliente in bancos[banco]['clientes'] for banco in bancos)

def es_banco(nbanco):
    return any(nbanco in bancos for banco in bancos)

def genera_prestamos(banco):
    return bool(bancos[banco].get('prestamos'))

def tiene_mas_clientes(banco, cliente):
    clientes = bancos[banco]['clientes']
    return len(clientes) > 1 and cliente in clientes

def tiene_cuenta(cliente):
    return any(cliente in bancos[banco]["clientes"] and "cuenta" in bancos[banco]["clientes"][cliente] for banco in bancos)

def puede_solicitar_prestamo(cliente):
    return any(cliente in bancos[banco]['clientes'] and genera_prestamos(banco) for banco in bancos)

def puede_recibir_monto(cliente, monto):
    for banco in bancos:
        if cliente in bancos[banco]["clientes"]:
            saldo = bancos[banco]["clientes"][cliente]["saldo"]
            return saldo > monto
    return False



if __name__ == '__main__':
    print('maria es cliente? ', es_cliente('maria'))
    print('maria es banco?', es_banco('maria'))

    print('santander genera prestamos?', genera_prestamos('santander'))
    print('santander es un cliente? ', es_cliente('santander'))

    print('santander tiene mas clientes ademas de maria?', tiene_mas_clientes('santander', 'maria'))
    print('pedro tine una cuenta?', tiene_cuenta('pedro'))

    print('maria puede pedir un prestamos?', puede_solicitar_prestamo('maria'))
    print('pedro puede pedir un prestamos?', puede_solicitar_prestamo('pedro'))
    
    print('maria puede recibir 10,000 pesos si tenia 15,000 en su cuenta? ', puede_recibir_monto('maria', 10000))
    bancos["santander"]["clientes"]["maria"]["saldo"] = 8000
    print('maria puede recibir 10,000 pesos si tenia 8,000 en su cuenta? ', puede_recibir_monto('maria', 10000))