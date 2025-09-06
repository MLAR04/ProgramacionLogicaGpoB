# Se especifica cada hecho 

clientes = {"Paula"}
bancos = {"Santander"}
cuentas = {("Paula", "Santander")}
prestamos = {"personal"}
cliente_por_tiempo = {("Paula", "Santander"): 2}

# Reglas
# aqui se revisa si la x esta dentro del conjunto que es de clientes
def es_cliente(x):
    return x in clientes
# aqui se revisa si la y esta dentro del conjunto que es de bancos
def es_banco(y):
    return y in bancos
# aqui revisa si el cliente (X = Paula) tiene cuenta en el banco (y = Santamder)
def tiene_cuenta(x, y):
    return (x, y) in cuentas
# Se especifica que el banco puede generar spñp si es de tipo personal y si tiene mas de 1 año siendo cliente en el banco
def genera_prestamo(y, tipo, cliente, tiempo):
    return tipo == "personal" and tiempo > 1 and (cliente, y) in cliente_por_tiempo

def puede_recibir_monto(x, monto):
    return monto <= 10000

# Consultas verdaderas y falsas
def main():

    print("¿Paula es cliente?", es_cliente("Paula"))  # Si x (Paula) es un cliente            
    print("¿Santander es cliente?", es_cliente("Santander"))      
# 
    print("¿Santander es banco?", es_banco("Santander"))     # Si y (Santander) es un banco         
    print("¿Escuela es banco?", es_banco("escuela"))                
# 
    print("¿Paula tiene cuenta en Santander?", tiene_cuenta("Paula", "Santander"))  # Si x (Paula) tiene una cuenta en y (Santander)    
    print("¿Paula tiene cuenta en BBVA?", tiene_cuenta("Paula", "Bbva"))           
# 

    print("¿Santander puede generar préstamo personal (2 años)?", # Si y puede generar prestamos personales    
        genera_prestamo("Santander", "personal", "Paula", 2))            
    print("¿Santander puede generar préstamo personal (0.5 años)?",
        genera_prestamo("Santander", "personal", "Paula", 0.5))          

#   
    print("¿Paula puede recibir 6500?", puede_recibir_monto("Paula", 6500))       
    print("¿Paula puede recibir 15000?", puede_recibir_monto("Paula", 15000))     

if __name__ == "__main__":
    main()    
