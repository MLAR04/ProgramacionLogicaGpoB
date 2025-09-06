# Diccionario de bancos, clientes y servicios
Banco = {
    "bbva": {
        "clientes": {
            "Maria": {"saldo": 1000},
            "Juan": {"saldo": 0}
        },
        "servicios": {
            "prestamos": ["hipotecario", "personal"],
            "depositos": True
        }
    },
    "santander": {
        "clientes": {
            "Pedro": {"saldo": 500}
        },
        "servicios": {
            "prestamos": ["personales"],
            "depositos": True
        }
    }
}


# Verifica si una persona es cliente de un banco.
def es_cliente(cliente):
    for i in Banco:
        if cliente in Banco[i]["clientes"]:
            print("Verdadero:", cliente, " es un cliente del banco", i)
            return True
    print(cliente, "no es cliente de ningún banco")


# Verificar si la institucion es un banco.
def es_banco(banco):
    if banco in Banco and "depositos" in Banco[banco]["servicios"]:
        print("Verdadero:", banco, "es un banco")
    else:
        print(banco, "NO es un banco")


# Verificar si un cliente tiene una cuenta en un banco.
def cuenta_cliente(cliente, banco):
    if cliente in Banco[banco]["clientes"]:
        print("Verdadero: ", cliente, "puede depositar dinero en su cuenta", banco)
    else:
        print(cliente, "NO es un cliente del banco", banco)


# Verificar si un banco puede generar un prestamo tipo w
def banco_prestamos(banco, w):
    if banco in Banco and w in Banco[banco]["servicios"]["prestamos"]:
        print("Verdadero:", banco, "puede generar prestamos", w)
    else:
        print(banco, "NO puede generar prestamos", w)


# Verificar si un cliente puede retirar dinero
def retiros(banco, cliente):
    if banco in Banco and cliente in Banco[banco]["clientes"]:
        saldo = Banco[banco]["clientes"][cliente]["saldo"]
        if saldo > 50:
            print("Verdadero: ", cliente, "puede retirar dinero (saldo:", saldo, ")")
        else:
            print(cliente, "NO puede retirar dinero (saldo:", saldo, ")")
    else:
        print("El banco o cliente no existe")


# Regla: Una persona es cliente si tiene una cuenta en un banco.
# Verdadero
print("\033[1m¿Maria es cliente?\033[0m")
es_cliente("Maria")
# Falso
print("\033[1m¿Pepito es cliente?\033[0m")
es_cliente("Pepito")

# Regla: Una institución es un banco si puede guardar dinero de clientes.
# Verdadero
print("\033[1m¿bbva es un banco?\033[0m")
es_banco("bbva")
# Falso
print("\033[1m¿Amazon es un banco?\033[0m")
es_banco("Amazon")

# Regla: Una persona puede depositar dinero si es cliente de un banco.
# Verdadero
print("\033[1m¿Maria puede depositar dinero en bbva?\033[0m")
cuenta_cliente("Maria", "bbva")
# Falso
print("\033[1m¿Lisa puede depositar dinero en bbva?\033[0m")
cuenta_cliente("Lisa", "bbva")

# Regla: Para que una institución genere prestamos tipo w tiene que ser un banco y tener disponible ese tipo de prestamos
# Verdadero
print("\033[1m¿bbva puede generar prestamos hipotecarios?\033[0m")
banco_prestamos("bbva", "hipotecario")
# Falso
print("\033[1m¿Santander puede generar prestamos hipotecarios?\033[0m")
banco_prestamos("santander", "hipotecario")

# Regla: si un cliente tiene un saldo mayor a 50, puede retirar dinero
# Verdadero
print("\033[1m¿Maria puede retirar dinero?\033[0m")
retiros("bbva", "Maria")
# Falso
print("\033[1m¿Juan puede retirar dinero?\033[0m")
retiros("bbva", "Juan")
