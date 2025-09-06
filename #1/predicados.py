bancos = {
    "BBVA": {
        "clientes": {
            "Alicia": 700
        },
        "prestamos": ["hipotecario"]
    },
}

# X es un cliente
# consulta 1: ¿Es Alicia cliente? verdadero
# consulta 2: ¿Es Leticia cliente? falso
def es_cliente(nombre):
    for banco in bancos:
        if nombre in bancos[banco]["clientes"]:
            return True
    return False


# Y es un banco
# consulta 1: ¿Es BBVA un banco? verdadero
# consulta 2: ¿Es Banamex un banco? falso

def es_banco(nombre):
    for banco in bancos:
        if nombre == banco:
            return True
    return False


# X tiene una cuenta en el banco Y
# consulta 1: ¿Alicia tiene una cuenta en BBVA? verdadero
# consulta 2: ¿Maria tiene una cuenta en BBVA? falso

def tiene_cuenta_en_banco(cliente, banco):
    if es_cliente(cliente) and es_banco(banco):
        return cliente in bancos[banco]["clientes"]
    return False


# Y puede generar un préstamo de tipo W
# consulta 1: ¿BBVA puede generar un préstamo hipotecario? verdadero
# consulta 2: ¿Banamex puede generar un préstamo automotriz? falso

def puede_generar_prestamo(banco, tipo_prestamo):
    if es_banco(banco):
        return tipo_prestamo in bancos[banco]["prestamos"]
    return False

# X recibió un monto Z de dinero
# consulta 1: ¿tiene Alicia 700 pesos en su cuenta? verdadero
# consulta 2: ¿tiene Maria 200 pesos en su cuenta? falso

def tiene_dinero_en_cuenta(cliente, monto):
    for banco in bancos:
        if cliente in bancos[banco]["clientes"]:
            return bancos[banco]["clientes"][cliente] == monto
    return False

if __name__ == "__main__":
    print("¿Es Alicia cliente?", es_cliente("Alicia")) # True
    print("¿Es Leticia cliente?", es_cliente("Leticia")) # False
    print("¿Es BBVA un banco?", es_banco("BBVA")) # True
    print("¿Es Banamex un banco?", es_banco("Banamex")) # False
    print("¿Alicia tiene una cuenta en BBVA?", tiene_cuenta_en_banco("Alicia", "BBVA")) # True
    print("¿Maria tiene una cuenta en BBVA?", tiene_cuenta_en_banco("Maria", "BBVA")) # False
    print("¿BBVA puede generar un préstamo hipotecario?", puede_generar_prestamo("BBVA", "hipotecario")) # True
    print("¿Banamex puede generar un préstamo automotriz?", puede_generar_prestamo("Banamex", "automotriz")) # False
    print("¿tiene Alicia 700 pesos en su cuenta?", tiene_dinero_en_cuenta("Alicia", 700)) # True
    print("¿tiene Maria 200 pesos en su cuenta?", tiene_dinero_en_cuenta("Maria", 200)) # False