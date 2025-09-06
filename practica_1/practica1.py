bancos = {
    "bbva":{
        "prestamos": {"estudiante","personal", "medico"},
        "empleados":{"pedro"},
        "clientes":{
            "guillermo": {"recibe":"1000", "cuenta": "activa"},
            "juan":{"deposito":"1000"}}
    },
    "santander":{
        "empleados":{},
        "clientes":{}
    }
}

#1.1
def es_cliente(x):
    for cliente in bancos["bbva"]["clientes"]:
        if x == cliente:
            print(x, "es un cliente?", True)
            return
    print(x, "es un cliente?", False)
#1.2
def es_empleado(x):
    for banco in bancos:
        for empleado in bancos[banco]['empleados']:
            if x == empleado:
                print(x,"es empleado?",True) 
    print(x,"es empleado?",False) 

#2.1 
def es_banco(x):
    for banco in bancos:
        if x == banco:
            print(x,"es un banco?", True)
            return
    print(x,"es un banco?", False)
#2.2
def es_cliente(x):
    for cliente in bancos["bbva"]["clientes"]:
        if x == cliente:
            print(x, "es un cliente?", True)
            return
    print(x, "es un cliente?", False)
#3.1
def varios_bancos(x):
    total = 0
    for banco in bancos:
        #print("revisa bancos")
        for cliente in bancos[banco]['clientes']:
            #print("revisa clientes")
            if x == cliente:
                total = total + 1
    if total > 1:
        print(x,"tiene cuneta en otros bancos?",True) 
    else: print(x,"tiene cuneta en otros bancos?",False) 

#3.2
def cuenta_activa(x, banco="bbva"):
    for cliente, datos in bancos[banco]["clientes"].items():
        if cliente == x and datos.get("cuenta") == "activa":
            print(x, "tiene una cuenta activa?", True)
            return
    print(x, "tiene una cuenta activa?", False)

#4.1
def tipo_prestamo(x):
    for prestamo in bancos["bbva"]["prestamos"]:
            if x in prestamo:
                print(x,"es un tipo de prestamo en bbva?",True) 
    print(x,"es un tipo de prestamo en bbva?",False) 
#4.2
def prestamos(x):
    for cliente, datos in bancos[x]["clientes"].items():
        if datos.get("prestamos"):  
            print(x, "tiene pretsamos activos?", True)      
    print(x, "tiene pretsamos activos?", False)   

#5.1
def recibio_2000(x):
    recibe = bancos['bbva']["clientes"][x].get("recibe",0)
    if int(recibe) == 2000:
        print(x,"recibio 2000?", True)
    else:
        print(x,"recibio 2000?", False)

#5.2
def recibio_1000(x):
    recibe = bancos['bbva']["clientes"][x].get("recibe",0)
    if int(recibe) == 1000:
        print(x,"recibio 1000?", True)
    else:
        print(x,"recibio 1000?", False)

if __name__ == '__main__':
    es_cliente("guillermo")#la respuesta sea true
    es_empleado('guillermo')#la respuesta sera false
 
    es_banco("bbva")#la respuesta sea true
    es_cliente("bbva")#la respuesta sera false

    varios_bancos("guilermo")#la respuesta sera false
    cuenta_activa("guillermo")#la respuesta sea true

    prestamos("bbva")#la respuesta sera false
    tipo_prestamo("personal")#la respuesta sea true

    recibio_2000("guillermo")#la respuesta sera false
    recibio_1000("guillermo")#la respuesta sea true
    