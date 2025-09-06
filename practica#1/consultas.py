from data import *
from typing import Optional

def esta_vivo(persona: str) -> bool:
    """
    Predicado 5: "X recibió un monto Z de dinero"
    Consulta verdadera
    """
    return persona in vivos


def es_banco(entidad: str) -> bool:
    """
    Predicado 2: "Y es un banco"
    Consulta verdadera
    """
    return entidad in bancos or ("abrir_cuentas_debito" in servicios.get(entidad, set()))


def es_institucion_medica(entidad: str) -> bool:
    """
    Predicado 2: "Y es un banco"
    Consulta falsa
    """
    return entidad in instituciones_medicas


def esta_registrado(persona: str, banco: str) -> bool:
    """
    Predicado 3: "X tiene una cuenta en el banco Y"
    """
    return banco in cuentas.get(persona, set())


def es_cliente(persona: str) -> bool:
    """
    Predicado 1: "X es un cliente"
    """
    return persona in clientes and len(cuentas.get(persona, set())) > 0


def es_cliente_de(persona: str, banco: str) -> bool:
    """
    Predicado 1 + 3 combinados
    """
    return persona in clientes and esta_registrado(persona, banco)


def es_cliente_de_todos(persona: str) -> bool:
    """
    Predicado 1: "X es un cliente"
    Consulta falsa o bien puede resultar verdadera si asi es el caso
    """
    if not bancos:
        return False
    return all(esta_registrado(persona, b) for b in bancos)


def puede_generar_prestamo(banco: str, tipo: str, persona: Optional[str] = None) -> bool:
    """
    Predicado 4: "Y puede generar un préstamo de tipo W"
    """
    if banco not in bancos:
        return False
    if tipo not in prestamos_ofrecidos.get(banco, set()):
        return False
    if banco in politica_clientes_prestamos and persona is not None:
        return es_cliente_de(persona, banco)
    return True


def recibio_dinero(persona: str, monto: int | None = None) -> bool:
    """
    Predicado 5: "X recibió un monto Z de dinero"
    Consulta verdadera
    """
    if not esta_vivo(persona):
        return False
    if monto is None:
        return bool(dinero_recibido.get(persona, []))
    return monto in dinero_recibido.get(persona, [])


def recibio_mas_que(persona: str, monto: int) -> bool:
    """
    Predicado 5: "X recibió un monto Z de dinero"
    Consulta falsa
    """
    cantidades = dinero_recibido.get(persona, [])
    return any(c != monto for c in cantidades)
