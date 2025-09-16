cliente = {
    'Pedro':{"banco": "Santander", "saldo": 50},
    'Sebastian': {"banco": "HSBC" , "saldo": 20 },
    'Felipe': {"banco": "HSBC" , "saldo": 35}
}

banco = {'Santander', 'HSBC'}

cuentas_banco = {
    'Felipe': {"cuenta:": "Santander"}
}

prestamos = {
    "Santander": {"prestamo:": "tipo Estudiantil"},
    "HSBC":{"prestamo:": "tipo Medico"}
}

dinero_recibido = {
    'Sebastian': 1000,
    'Felipe' : 0,
    'Pedro' : 500
}

#REGLAS
#clientes aquellos que tienen una cuenta con mas de 15 pesos dentro de ella
def cliente_de(nombre):
    if nombre in cliente:
        if cliente[nombre]["saldo"] > 15:
            return True
        else:
            return False
    else: return False

#Es un banco todo aquel que pueda realizar prestamos
def es_banco(nombre):
    if nombre in banco:
        prestamos_del_banco = prestamos.get(nombre, [])
        return len(prestamos_del_banco) > 0
    return False

#Cliente que se encuentre registrado (Santander HSBC)
def cuenta_de(nombre, banco_nombre):
    if nombre in cliente:
        if cliente[nombre]["banco"] == banco_nombre:
            return True
    # Si está en cuentas_banco adicional
    if nombre in cuentas_banco:
        if cuentas_banco[nombre] == banco_nombre:
            return True
    return False

#Puedes generar un prestamo si eres cliente
def dar_prestamo(banco, tipo, cliente):
    if cliente_de(cliente):
        if banco in prestamos:
            if tipo in prestamos[banco]:
                return True
            return False

#Recibió dinero
def recibio_dinero(nombre):
    if nombre in dinero_recibido:
        return dinero_recibido[nombre] > 0
    return False

# ===== CONSULTAS =====
print("¿Felipe es un cliente?", cliente_de("Felipe"))
print("¿Mariana es un cliente?", cliente_de("Mariana"))

print("¿Santander es un Banco?", es_banco("Santander"))
print("¿BBVA es un Banco?", es_banco("BBVA"))

print("¿Felipe tiene una cuenta en el banco HSBC?", cuenta_de("Felipe", "HSBC"))
print("¿Bernardo tiene cuenta en Santander?", cuenta_de("Bernardo", "Santander"))

print("¿Santander otorga el préstamo estudiantil a Pedro?", dar_prestamo("Santander", "Estudiantil", "Pedro"))
print("¿HSBC otorga el préstamo estudiantil a Pedro?", dar_prestamo("HSBC", "Estudiantil", "Pedro"))

print("¿Felipe recibió dinero?", recibio_dinero("Felipe"))
print("¿Pedro recibió dinero?", recibio_dinero("Pedro"))
