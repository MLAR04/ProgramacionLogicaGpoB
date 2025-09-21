def es_multiplo_de_6(r1: bool, r2: bool) -> bool:
    """
    Rg: un número es múltiplo de 6.

    Parámetros:
    r1: El número es divisible entre 2.
    r2: El número es divisible entre 3.

    """
    return r1 and r2


def puede_votar(r1: bool, r2: bool, r3: bool) -> bool:
    """
    Rg: Una persona puede votar.

    Parámetros:
    r1: La persona tiene más de 18 años.
    r2: La persona tiene credencial de elector.
    r3: La persona está en la lista nominal.

    """
    return (r1 and r2 )and r3


def puede_conectarse_internet(r1: bool, r2: bool, r3: bool) -> bool:
    """
    Rg: una computadora puede conectarse a internet.

    Parámetros:
    r1: Tiene Wi-Fi activado.
    r2: Tiene cable Ethernet conectado.
    r3: El módem funciona.

    """
    return (r1 or r2) and r3