dep_prestamos_santander = {"Prestamos": ["Perla"]}

def tiene_prestamo(cliente):
    for prestamo in dep_prestamos_santander:
        print(cliente + " tiene un prestamo?")
        if cliente in dep_prestamos_santander[prestamo]:
            return True
    return False


if __name__ == '__main__':
    print(tiene_prestamo("Perla"))
    print(tiene_prestamo("Noe"))