# Nuestro universo son los bancos, cada banco tiene sus clientes y cada cliente tiene un saldo
Bancos = {
    "BBVA": {
        "Juan": 500,
        "Marta": 1500,
        "Pedro": 700,
        "Carlos": 1300
    },
    "Santander": {
        "Ana": 2500,
        "Luis": 3000,
        "Maria": 1200
    }
}


# 1. Consulta: En que banco tiene una cuenta un cliente? (En este caso, Juan)
# Esta consulta es la verdadera que tiene que devolver el banco BBVA
def en_que_banco_tiene_cuenta(cliente):
    for banco in Bancos:
        if cliente in Bancos[banco]:
            return banco
    return "No tiene cuenta en ningun banco"

# 2. Un cliente tiene mas de una cuenta? (En este caso, Juan)
# Esta consulta es falsa, ya que Juan solo tiene cuenta en el banco BBVA
def tiene_mas_de_una_cuenta(cliente):
    cuenta_count = 0
    for banco in Bancos:
        if cliente in Bancos[banco]:
            cuenta_count += 1
    return cuenta_count > 1

# 3. Cuantos clientes tiene un banco? (En este caso, BBVA)
# Esta consulta devuelve 4, ya que BBVA tiene 4 clientes: Juan, Marta, Pedro y Carlos
def cuantos_clientes_tiene_banco(banco):
    if banco in Bancos:
        return len(Bancos[banco])
    return 0

# 4. Un cliente tiene cuenta en un banco en especifico? (En este caso, Maria en BBVA)
# Esta consulta es falsa, ya que Maria tiene cuenta en Santander
def es_cliente_de_banco(cliente, banco="BBVA"):
    if banco in Bancos and cliente in Bancos[banco]:
        return True
    return False

# 5. Cuanto dinero tiene un cliente? (En este caso, Juan)
# Esta consulta devuelve 500, que es el saldo de Juan en BBVA
def cuanto_dinero_tiene_cliente(cliente):
    for banco in Bancos:
        if cliente in Bancos[banco]:
            return Bancos[banco][cliente]
    return 0

# 6. Puede un cliente mandar tanto dinero a otro cliente? (En este caso, Juan quiere mandar 10000)
# En este caso, la consulta es falsa, ya que Juan solo tiene 500
def puede_mandar_dinero(cliente_origen, cantidad):
    saldo_origen = cuanto_dinero_tiene_cliente(cliente_origen)
    if saldo_origen >= cantidad:
        return True
    return False

# 7. Juan puede pedir un prestamos? (En este caso, Juan quiere pedir un prestamos pero necesita minimo 1000)
# En este caso, la consulta es falsa, ya que Juan solo tiene 500
def puede_pedir_prestamo(cliente):
    saldo = cuanto_dinero_tiene_cliente(cliente)
    if saldo >= 1000:
        return True
    return False

# 8. Carlos puede pedir un prestamos? (En este caso, Carlos quiere pedir un prestamos pero necesita minimo 1000)
# En este caso, la consulta es verdadera, ya que Carlos tiene 1300
# Para eso reutilizamos la funcion anterior pero con Carlos

# 9. Cuanto dinero tiene juan ahora? (En este caso, Juan tiene 600 por que le llegaron 100 mas)
# Reutilizamos la funcion anterior del punto 5

# 10. Maria le puede mandar dinero a juan? (En este caso, Maria tiene 1200)
# En este caso, la consulta es verdadera, ya que Maria tiene 1200 y tiene una cuenta en Santander
# Parecida a la funcion del punto 6 pero solo confirmando que maria tenga una cuenta en algun banco
def es_cliente_de_algun_banco(cliente):
    for banco in Bancos:
        if cliente in Bancos[banco]:
            return True
    return False

def puede_mandar_dinero(cliente_origen, cliente_destino):
    if es_cliente_de_algun_banco(cliente_origen) and es_cliente_de_algun_banco(cliente_destino):
        return True
    return False


# Todas las consultas para verificar que funcionan correctamente
if __name__ == '__main__':
    print("CONSULTA: En que banco tiene cuenta Juan?", en_que_banco_tiene_cuenta("Juan"))
    print("CONSULTA: Juan tiene mas de una cuenta?", tiene_mas_de_una_cuenta("Juan"))
    print("CONSULTA: Cuantos clientes tiene el banco BBVA?", cuantos_clientes_tiene_banco("BBVA"))
    print("CONSULTA: Maria tiene cuenta en BBVA?", es_cliente_de_banco("Maria", "BBVA"))
    print("CONSULTA: Cuanto dinero tiene Juan?", cuanto_dinero_tiene_cliente("Juan"))
    print("CONSULTA: Juan puede mandar 10000?", puede_mandar_dinero("Juan", 10000))
    print("CONSULTA: Juan puede pedir un prestamo?", puede_pedir_prestamo("Juan"))
    print("CONSULTA: Carlos puede pedir un prestamo?", puede_pedir_prestamo("Carlos"))
    # Simulamos que le llego una transferencia de 100 a Juan
    Bancos["BBVA"]["Juan"] += 100
    print("CONSULTA: Cuanto dinero tiene Juan ahora?", cuanto_dinero_tiene_cliente("Juan"))
    print("CONSULTA: Maria le puede mandar dinero a Juan?", puede_mandar_dinero("Maria", "Juan"))
