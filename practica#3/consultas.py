from reglas import *
from tablas import generar_tabla_verdad

def tabla_multiplo_de_6():
    generar_tabla_verdad(
        nombre="Múltiplo de 6",
        funcion=es_multiplo_de_6,
        nombres_parametros=["R1", "R2"]
    )

def tabla_puede_votar():
    generar_tabla_verdad(
        nombre="Puede Votar",
        funcion=puede_votar,
        nombres_parametros=["R1", "R2", "R3"]
    )

def tabla_conexion_internet():
    generar_tabla_verdad(
        nombre="Conectarse a Internet",
        funcion=puede_conectarse_internet,
        nombres_parametros=["R1", "R2", "R3"]
    )



