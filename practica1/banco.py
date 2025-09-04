sistema = {
    "banamex" : {
        "juan":{ "prestamo":5000, "tipo":"personal"}
        },
    "bbva" : { 
        "sebastian":{ "prestamo":5000, "tipo":"hipotecario"}
         }
}
# "X" es un cliente 
def es_cliente(x):
    for banco in sistema:
        if x in sistema[banco]:
            print(f'{x} es cliente de {banco}')
            return True
    return False
#"y" es un banco, aqui confirmaremos si existe y como banco 
# y aparte en la consulta veremos si tiene clientes o no?
def es_banco(x):
    for banco in sistema:
        if x in sistema:
            clientes = len(sistema[banco])
            print(f'el banco {x} tiene {clientes} clientes.')
            return True
    return False
#ahora recibiremos el nombre del cliente y veremos en que banco tiene cuenta
def tiene_cuenta(x):
    for banco in sistema:
        if x in sistema[banco]:
            print(f'el cliente {x} tiene una cuenta en el banco {banco}')
            return True
    return False
#ahora preguntaremos si un banco maneja un tipo de prestamo en especifico 
# le mandaremos "x" como banco y "y" como el tipo de prestamo 
def tipo_prestamo(x, y):
    if x in sistema: 
        for cliente in sistema[x]:
            if sistema[x][cliente]["tipo"] == y:
                print(f"el banco {x} maneja prestamos de tipo {y}")
                return True
        print(f"el banco {x} no maneja prestamos de tipo {y}")
        return False
    else:
        print(f"el banco {x} no existe en el sistema")
        return False
#ahora verificaremos si un cliente tiene un prestamo 
# recibiremos el nombre x y el banco y 
def tiene_prestamo(x,y):
    if y in sistema: 
        for cliente in sistema[y]:
            if cliente == x:
                print(f'el cliente {x} tiene un prestamo en el banco {y} de tipo {sistema[y][cliente]["tipo"]} y el monto es {sistema[y][cliente]["prestamo"]}')
                return True
    return False
if __name__ == '__main__':
    #print(es_cliente("juan"))#EJERCICIO 1 VERDADERO
    #print(es_cliente("arturo"))#EJERCICIO 1 FALSE
    #print(es_banco("banamex"))#EJERCICIO 2 VERDADERO
    #print(es_banco("scotiabank"))#EJERCICIO 2 FALSE
    #print(tiene_cuenta("juan"))#EJERCICIO 3 VERDADERO
    #print(tiene_cuenta("esteban"))#EJERCICIO 3 FALSO
    #tipo_prestamo("banamex", "personal")# EJERCICIO 4 VERDADER
    #tipo_prestamo("banamex", "hipotecario")# ejercicio 4 FALSO
    #print(tiene_prestamo("juan","banamex"))# ejercico 5 verdadero
    print(tiene_prestamo("oscar","banamex"))# ejercico 5 falso