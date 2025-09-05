Banco = {

"Pedro":["mayor de edad","30 años","Humano"],
"inBanco":["Tiene dinero","Presta dinero","500 dolares"],
"cuenta":["Tiene dinero","tiene cuenta"],
"pedro": ["tiene dinero","no debe"],
"osvaldo": ["recibio dinero" , "tiene 1000 pesos "]

}
 
def  edad (x,y):
    
    for cliente in Banco:
        if x in Banco[cliente] and y in Banco[cliente]:
            print(f"pedro es {x} y tiene {y}")
            return True
        else: 
            print(" no se aceptan meores de edad")
            return False

def raza (z):
    for cliente in Banco:
        if z in Banco[cliente]:
            print(f"pedro es {z}")
            return True
        else:
            print(f"pedro es {z} ") 
            return False

def Prestamo(x,y):
    for dinero in Banco:
        if y in Banco[dinero]:  
            if y == "Presta dinero":
                print(f"El banco sí {y}")
                return True
            else:
                print(f"El banco no regala dinero")
                return False
    
    print("El banco no tiene ese servicio")
    return False

def estado_cuenta(x):
    for cuenta in Banco:
        if x in Banco[cuenta]:
            print(f"{x}")
            return True  
    print("No tiene nada")
    return False

def ecomomia (x,y):
    for genera in Banco:
        if x in Banco[genera] and y in Banco[genera]:
            print(f"{x} ademas {y}")
            return True
        elif  y in Banco[genera]:
            print(f" el {y}")
            return True
    return False

def osvaldo(x=None, y=None):
    datos = Banco.get("osvaldo", [])
    
    for valor in datos:
        if x and y and x in datos and y in datos:
            print(f"Osvaldo tiene {x} y {y}")
            return True
        elif x and x in datos:
            print(f"Osvaldo  {x} y recibio 1000")
            return True
        elif y and y in datos:
            print(f"Osvaldo tiene {y}")
            return True
    
    print("Osvaldo no tiene esos valores")
    return False

 

if __name__ == '__main__':
    print(edad("menor de edad " , "30 años"))
    print(raza("Humano"))
    print (Prestamo("Tiene dinero","regala dinero"))
    print (Prestamo("Tiene dinero","Presta dinero"))
    print(estado_cuenta("no tiene dinero"))
    print (estado_cuenta("tiene dinero"))
    print(ecomomia("tiene dinero","no debe"))
    print(ecomomia("no tiene dinero", "debe"))     
    print(osvaldo("recibio dinero", "cuanto dinero tiene"))
    print(osvaldo("no tiene dinero"))