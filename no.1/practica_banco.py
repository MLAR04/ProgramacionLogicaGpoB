# Definicion de objetos
bancos = {
    "Santander": {
        "Prestamos": ["A plazo", "Rotario"],
        "Clientes": {
            "Pablo": { "Transacciones" : [200, -300, 400] },
            "Maria": { "Transacciones" : [200, -90, 100] },
            "Estevan": { "Transacciones" : [150, -30, 400] }, 
        }
    },
    "Banamex": {
        "Prestamos": ["A plazo",  "Rotario"],
        "Clientes": {
            "Juana": { "Transacciones" : [200, -100] },
            "Annyi": { "Transacciones" : [-200, -300, -400, 10] }, 
        }
    },
    "BanCoppel": {
        "Prestamos": ["A plazo"],
        "Clientes": {
            "Pablo": { "Transacciones" : [200, -300, 400] },
            "Juanita": { "Transacciones" : [2000, -900, 100] },
            "Juana": { "Transacciones" : [150, -30, 400] }, 
        }
    },
}

#Basicamente revisa si la persona se encuentra en algun banco sin especificar.
def es_cliente( persona ):
    #revisar en tdos los bancos
    for banco in bancos:
        if tiene_cuenta(persona, banco):
            return True
    
    return False

#Revisa si el input esta en la lista de bancos
def es_banco( banco ):
    return banco in bancos

#Revisa si una persona esta en un banco en especifico
def tiene_cuenta( persona, banco ):
    return banco in bancos and persona in bancos[banco]["Clientes"]

#Revisa si un banco puede generar un tipo de prestamo
def banco_puede_generar_prestamo ( banco, prestamo ):
    return prestamo in bancos[banco]["Prestamos"] 

#Revisa si existe un cargo especifico de una persona en un banco
def recibio_monto_especifico ( persona, prestamo ):
    for banco in bancos:
        if tiene_cuenta(persona, banco):
            if prestamo in bancos[banco]["Clientes"][persona]["Transacciones"]:
                return True
    return False


if __name__ == "__main__":
    persona = "Estevan"
    banco = "BanCoppel"
    prestamo = "Rotario"

    print(
        recibio_monto_especifico(persona, 150),
        recibio_monto_especifico(persona, 500)
    )