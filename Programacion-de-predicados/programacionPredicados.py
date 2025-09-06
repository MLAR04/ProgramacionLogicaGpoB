
# Predicado 1 "X" es un cliente
def es_cliente():
    clientes = ["Alex"]  
    
    def es_cliente(nombre):
        return nombre in clientes
    # Consultas
    print("¿Alex es cliente?", es_cliente("Alex"))   
    print("¿Linda es cliente?", es_cliente("Linda")) 


# Predicado 2 "X" es un banco
def es_banco():
    bancos = ["Banamex"]

    def es_banco(nombre):
        return nombre in bancos
    # Consultas
    print("¿Banamex es un banco?", es_banco("Banamex")) 
    print("¿Oxxo es banco?", es_banco("Oxxo"))          



# Predicado 3 "X" tiene una cuenta en el banco "Y"
def cuenta_banco():
    cuentas = {"Alex": "Banamex"}
   
    def cuenta_valida(nombre):
        return nombre in cuentas
    
    print("¿Es válida la cuenta de Alex?", cuenta_valida("Alex"))   
    print("¿Es válida la cuenta de Linda?", cuenta_valida("Linda")) 


# Predicado 4 "Y" puede generar un prestamo de tipo "W"
def prestamos():
    prestamos = {"Banamex": ["hipotecario"]}
   
    def puede_prestamo(banco, tipo):
        return banco in prestamos and tipo in prestamos[banco]
   
    print("¿Banamex puede generar un préstamo hipotecario?", puede_prestamo("Banamex", "hipotecario")) 
    print("¿Banamex puede generar un préstamo estudiantil?", puede_prestamo("Banamex", "estudiantil")) 


# Predicado 4 "X" recibio un monto "Z" de dinero

def montos_dinero():
    cuentas = {"Alex": "Banamex"}
    montos = {"Alex": 5000}

    def recibio_monto(nombre, monto):
        if nombre in cuentas:
            return montos.get(nombre) == monto
        return False

    print("¿Alex recibió 5000?", recibio_monto("Alex", 5000))  
    print("¿Alex recibió 15000?", recibio_monto("Alex", 15000)) 



print("Predicado 1")
es_cliente()
print("Predicado 2")
es_banco()
print("Predicado 3")
cuenta_banco()
print("Predicado 4")
prestamos()
print("Predicado 5")
montos_dinero()