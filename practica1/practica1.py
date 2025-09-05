banco = { "clientes":[ {"nombre": "pedro", "edad": 20, "vivienda": "propia", "monto_prestamo": 700000,} ],
         "tipo_prestamo":["hipotecario"]}

def es_cliente(nombre): #Es cliente?
    for cliente in banco["clientes"]:
        if nombre == cliente["nombre"]:
            print("Si es cliente")
        else:
            print("No es cliente")

def tiene_clientes(): #Tiene clientes?
    if len(banco["clientes"]) > 0:
        print("El banco tiene clientes")
    else:
        print("El banco no tiene clientes")   

def es_mayor_edad(nombre): #Es mayor de edad?
    for cliente in banco["clientes"]:
        if nombre == cliente["nombre"]:
            if cliente["edad"] >= 18:
                print("Es mayor de edad")
            else:
                print("No es mayor de edad")

def es_menor_edad(nombre): #Es menor de edad?
    for cliente in banco["clientes"]:
        if nombre == cliente["nombre"]:
            if cliente["edad"] < 18:
                print("Es menor de edad")
            else:
                print("No es menor de edad")

def vivienda_propia(nombre): #Tiene vivienda propia (tiene casa)?
    for cliente in banco["clientes"]:
        if nombre == cliente["nombre"]:
            if cliente["vivienda"] == "propia":
                print("Tiene vivienda propia")
            else:
                print("No tiene vivienda propia")

def tiene_prestamo(tipo): #Tiene prestamos de ese tipo?
    for prestamo in banco["tipo_prestamo"]:
        if tipo == prestamo:
            print("El banco tiene prestamos de este tipo")
        else:
            print("El banco no tiene prestamos de este tipo")

def prestamo_alto_monto(nombre): #Es de monto alto el prestamo?
    for cliente in banco["clientes"]:
        if cliente["nombre"] == nombre:
            if cliente["monto_prestamo"] > 500000:
                print("Si recibió un monto alto de prestamo")
            else:
                print("No recibió un monto alto de prestamo")
        else:
            print("El cliente no existe")

def recibio_esa_cantidad(nombre, cantidad): #Recibio esa cantidad?
    for cliente in banco["clientes"]:
        if cliente["nombre"] == nombre:
            if cliente["monto_prestamo"] == cantidad:
                print("Si")
            else:
                print("No")
        else:
            print("El cliente no existe")

if __name__ == '__main__':
    es_cliente("pedro") #Pedro es cliente?(TRUE)
    es_cliente("maria") #Maria es cliente?(FALSE)
    tiene_clientes() #Tiene clientes BBVA?(TRUE)
    es_cliente("juan") #Juan es cliente de BBVA?(FALSE)
    es_mayor_edad("pedro") #Pedro es mayor de edad?(TRUE)
    es_menor_edad("pedro") #Pedro es menor de edad?(FALSE)
    vivienda_propia("pedro") #Pedro tiene vivienda propia?(TRUE)
    tiene_prestamo("estudiantil") #El banco tiene prestamos estudiantiles?(FALSE)
    prestamo_alto_monto("pedro") #Pedro recibió un prestamo alto?(TRUE)
    recibio_esa_cantidad("pedro", 100000) #Pedro recibió 100000?(FALSE)