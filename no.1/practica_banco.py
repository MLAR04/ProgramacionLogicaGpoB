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

def es_cliente( persona ):
    pass

def es_banco( banco ):
    pass

def tiene_cuenta( persona, banco ):
    pass

def puede_generar_perstamo ( banco, prestamo ):
    pass

def recibio_monto_especifico ( banco, prestamo ):
    pass


