from universo import Bancos

def esCliente(banco, persona): # Deuelve si una persona es cliente de una empresa
    if persona in Bancos[banco]["clientes"]:
        return True
    return False

def tipoEmpresa(banco): # Devuelve el tipo de institución que es una empresa
    return Bancos[banco]["Tipo"]

def bancosDeCliente(persona): # Devuelve una lista de en que bancos se encuentra una persona
    listaBancos = []
    for banco in Bancos:
        if persona in Bancos[banco]["clientes"]:
            listaBancos.append(banco)
    return listaBancos

def tiposPrestamos(banco): # Devuelve los tipos de prestamos que cuenta una empresa (Si aplica)
    return Bancos[banco]["tipos_prestamos"]

def montoCliente(persona): # Devuelve el monto que recibio un cliente
    for banco in Bancos:
        if persona in Bancos[banco]["clientes"]:
            return Bancos[banco]["clientes"][persona]["monto"]

def edadCliente(persona): # Devuelve la edad de una persona
    for banco in Bancos:
        if persona in Bancos[banco]["clientes"]:
            return Bancos[banco]["clientes"][persona]["edad"]

if __name__ == "__main__":
    persona = "Pedro"
    banco = "BBVA"
    
    # ¿'X' es un cliente?
    try:
        if esCliente(banco, persona):
            print("La persona si es cliente del banco.")
        else:
            print("La persona no es cliente del banco.")
    except:
        print("El banco no existe para buscar clientes.")

    # ¿De que tipo de empresa es 'Y'?
    try:
        print(f"La empresa es de tipo: {tipoEmpresa(banco)}.")
    except:
        print("El banco no exsite para buscar su tipo.")

    # ¿En que bancos es cliente 'X'?
    listaBancos = bancosDeCliente(persona)
    if len(listaBancos):
        print(f"La persona es cliente de los bancos: {', '.join(listaBancos)}.")
    else:
        print(f"La persona {persona} no es cliente de ningún banco.")

    # ¿Qué tipos de prestamos tiene 'Y'?
    try:
        print(f"El banco tiene los siguientes tipos de prestamo: {', '.join(tiposPrestamos(banco))}.")
    except:
        print("El banco no existe y por ende no hay tipos de prestamos.")

    # ¿Cuanto monto recibio 'X'?
    try:
        print(f"El cliente recibio un monto de ${montoCliente(persona):,}.")
    except:
        print(f"La persona no es cliente de ningún banco.")

    # ¿Qué edad tiene 'X'?
    edad = edadCliente(persona)
    if edad:
        print(f"El cliente tiene {edad} años de edad.")
    else: print(f"La persona {persona} no existe.")