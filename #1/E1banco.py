#hecho
clientes = ["juan"]
bancos = ["bancomer"]
cuentas = {"juan": ["bancomer"]}
prestamos = {"bancomer": ["hipotecario"]}
montos = {"juan": 5000}


# ley
def puede_solicitar(cliente, banco, tipo_prestamo):
    # El cliente debe existir
    if cliente not in clientes:
        return False
    # El banco debe existir
    if banco not in bancos:
        return False
    # El cliente debe tener una cuenta en ese banco
    if banco not in cuentas.get(cliente, []):
        return False
    # El banco debe ofrecer ese tipo de préstamo
    if tipo_prestamo not in prestamos.get(banco, []):
        return False
    return True

if __name__ == "__main__":
# consulta
    print("¿Juan puede solicitar un prestamo hipotecario en Bancomer?")
    print(puede_solicitar("juan", "bancomer", "hipotecario")) 

    print("¿Juan puede solicitar un prestamo automotriz en Bancomer?")
    print(puede_solicitar("juan", "bancomer", "automotriz"))   
