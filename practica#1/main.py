from utils import mostrar_tabla
from consultas import *

def main():
    mostrar_tabla("CONSULTAS DE CLIENTES", [
        ("¿Manuel es cliente del banco HSBC?", es_cliente_de("Manuel", "HSBC")),
        ("¿Manuel es cliente de todos los bancos?", es_cliente_de_todos("Manuel")),
    ])

    mostrar_tabla("CONSULTAS DE BANCOS", [
        ("¿Es Nu un banco?", es_banco("Nu")),
        ("¿Nu es una institución médica?", es_institucion_medica("Nu")),
    ])

    mostrar_tabla("CONSULTAS DE CUENTAS", [
        ("¿Mario esta registrado en Nu?", es_cliente_de("Mario", "Nu")),
        ("¿Mario tiene cuenta en HSBC?", es_cliente_de("Mario", "HSBC")),
    ])

    mostrar_tabla("CONSULTAS DE PRÉSTAMOS", [
        ("¿Nu puede generar préstamos estudiantiles?", puede_generar_prestamo("Nu", "estudiantil")),
        ("¿Nu puede prestar a Ana sin ser cliente?", puede_generar_prestamo("Nu", "estudiantil", persona="Ana")),
    ])

    mostrar_tabla("CONSULTAS DE DINERO", [
        ("¿Lionel está vivo?", esta_vivo("Lionel")),
        ("¿Lionel recibió más dinero además de 100,000?", recibio_mas_que("Lionel", 100000)),
    ])

if __name__ == "__main__":
    main()
