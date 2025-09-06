
clientes = {"Juan Pérez", "María García", "Carlos López"}

cuentas = {
    "María García": "Banco Global",
    "Juan Pérez": "Banco Nacional",
    "Carlos López": "Banco de Inversión"
}

bancos = {"Banco Nacional", "Banco Global", "Banco de Inversión"}
entidades_reguladas = {
    "Banco Central", "Banco Comercial", "Banco Nacional",
    "Banco Global", "Banco de Inversión", "Caja de Ahorros"
}

tarjetas_emitidas = {
    "Ana Silva": "Banco Central",
    "Roberto Díaz": "Banco Global",
    "María García": "Banco Global" 
}

montos_recibidos = {
    "Carlos López": 5000,
    "María García": 3000,
    "Juan Pérez": 10000
}
prestamos_aprobados = {
    "Ana Rodríguez": {"banco": "Banco Nacional", "monto": 7000, "tipo": "préstamo personal"},
    "Pedro Martínez": {"banco": "Banco Global", "monto": 12000, "tipo": "préstamo estudiantil"},
    "Carlos López": {"banco": "Banco de Inversión", "monto": 5000, "tipo": "préstamo hipotecario"}
}

prestamos_habilitados = {
    "Banco de Inversión": {"préstamo hipotecario"},
    "Banco Nacional": {"préstamo personal", "préstamo automotriz"},
    "Banco Global": {"préstamo estudiantil"}
}
departamentos_credito = {
    "Banco de Inversión": {"préstamo hipotecario", "préstamo comercial"},
    "Banco Nacional": {"préstamo personal", "préstamo automotriz", "préstamo hipotecario"},
    "Banco Central": {"préstamo personal", "préstamo automotriz"}
}

def es_cliente(x):
   
    print(f" '{x}' ¿Es un cliente?")
    
    if x in clientes:
        print(f"✓ Hecho directo: '{x}' es un cliente")
        return True
    
    if x in cuentas:
        banco = cuentas[x]
        print(f" '{x}' tiene cuenta en {banco}, por lo tanto es cliente")
        return True
    
    if x in tarjetas_emitidas:
        banco = tarjetas_emitidas[x]
        print(f" '{x}' tiene tarjeta de débito de {banco}, por lo tanto es cliente")
        return True
    
    print(f"✗ '{x}' no es un cliente")
    return False

def es_banco(y):
    
    print(f"'{y}' ¿Es un banco?")
    if y in bancos:
        print(f" '{y}' es un banco")
        return True
    
    
    if y in entidades_reguladas:
        print(f"'{y}' está regulado, por lo tanto es banco")
        return True
    
    print(f"✗ '{y}' no es un banco")
    return False


def tiene_cuenta_en(x, y):
    
    print(f"¿'{x}' tiene cuenta en '{y}'?")
    

    if x in cuentas and cuentas[x] == y:
        print(f"✓  '{x}' tiene cuenta en {y}")
        return True
    
    if x in tarjetas_emitidas and tarjetas_emitidas[x] == y:
        print(f"✓ '{x}' tiene tarjeta de {y}, por lo tanto tiene cuenta")
        return True
    
    print(f"✗ '{x}' no tiene cuenta en {y}")
    return False

def recibio_monto(x, z):
   
    print(f"¿ '{x}' recibió ${z}?")
    
    if x in montos_recibidos and montos_recibidos[x] == z:
        print(f"✓ Hecho directo: '{x}' recibió ${z}")
        return True
    
    if x in prestamos_aprobados and prestamos_aprobados[x]["monto"] == z:
        banco = prestamos_aprobados[x]["banco"]
        tipo = prestamos_aprobados[x]["tipo"]
        print(f"✓  '{x}' tiene {tipo} aprobado de ${z} en {banco}, por lo tanto recibió el dinero")
        return True
    
    print(f"✗ '{x}' no recibió ${z}")
    return False

def puede_generar_prestamo(y, w):
    
    print(f"¿ '{y}' puede generar un '{w}'?")

    if y in prestamos_habilitados and w in prestamos_habilitados[y]:
        print(f"✓ '{y}' puede generar {w}")
        return True
    
    if y in departamentos_credito and w in departamentos_credito[y]:
        print(f"✓  '{y}' tiene departamento para {w}, por lo tanto puede generarlo")
        return True
    
    print(f"✗ '{y}' no puede generar {w}")
    return False

if __name__ == "__main__":
    
    print("\nX es cliente (V):")
    resultado1 = es_cliente("Juan Pérez")
    
    print("\nX es cliente (F):")
    resultado2 = es_cliente("Banco Central")

    print("\nY es un banco (V):")
    resultado1 = es_banco("Banco Nacional")
    
    print("\nY es un banco (F):")
    resultado2 = es_banco("Juan Pérez")
    
    print("\nX tiene cuenta en Y (V):")
    resultado1 = tiene_cuenta_en("María García", "Banco Global")
    
    print("\nX tiene cuenta en Y (F):")
    resultado2 = tiene_cuenta_en("Banco Nacional", "Banco Global")
    
    print("\nX hizo un monto de Z (V):")
    resultado1 = recibio_monto("Carlos López", 5000)
    
    print("\nX hizo un monto de Z (F):")
    resultado2 = recibio_monto("Carlos López", 15000)

    print("\nY dio un prestamo a W (V):")
    resultado1 = puede_generar_prestamo("Banco de Inversión", "préstamo hipotecario")
    
    print("\nY dio un prestamo a W (F):")
    resultado2 = puede_generar_prestamo("Banco de Inversión", "préstamo automotriz")
    

  


    
   
