# Definicion de objetos
Bancos = {
    "Santander": {
        "Transacciones": ["A plazo", "Rotario"],
        "Clientes": {
            "Pablo": { "Transacciones" : [200, -300, 400] },
            "Maria": { "Transacciones" : [200, -90, 100] },
            "Estevan": { "Transacciones" : [150, -30, 400] }, 
        }
    },
    "Banamex": {
        "Transacciones": ["A plazo",  "Rotario"],
        "Clientes": {
            "Juana": { "Transacciones" : [200, -100] },
            "Annyi": { "Transacciones" : [-200, -300, -400, 10] }, 
        }
    },
    "BanCoppel": {
        "Transacciones": ["A plazo"],
        "Clientes": {
            "Pablo": { "Transacciones" : [200, -300, 400] },
            "Juanita": { "Transacciones" : [2000, -900, 100] },
            "Juana": { "Transacciones" : [150, -30, 400] }, 
        }
    },
}

#Basicamente revisa si la persona se encuentra en algun banco sin especificar.
def es_cliente( persona ):
    pass

#Revisa si el input esta en la lista de bancos
def es_banco( banco ):
    pass

#Revisa si una persona esta en un banco en especifico
def tiene_cuenta( persona, banco ):
    pass

#Revisa si un banco puede generar un tipo de prestamo
def banco_puede_generar_perstamo ( banco, prestamo ):
    pass

#Revisa si existe un cargo especifico de una persona en un banco
def recibio_monto_especifico ( persona, prestamo ):
    pass


