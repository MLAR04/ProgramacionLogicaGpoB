from BC import hechos
#primer ley que dice cada subtema pertenece a un tema 
# como consulta entonces tenemos que 
# pertenece(diseno_funciones, diseno_algoritmico)


#----------------PRIMERA CLAUSULA SIN RECURSIVIDAD------------------------------------------------------------------------
# ley: si existe un  subtema → pertenece a un tema 
"""
def pertenece(subtema, tema):
    # Recorremos la tupla de hechos
    for hecho in hechos:
        # Verificamos que sea un subtema
        if hecho[0] == "subtema":
            # comprobamos si coincide con la consulta
            if hecho[1] == subtema and hecho[2] == tema:
                return True
    return False 
"""
#----------------PRIMERA CLAUSULA CON RECURSIVIDAD----------------------------------------------------------------------------------------
def pertenece(subtema, tema, i=0):
    print(f'UNIFICACION Y SUSTITUCION \n subtema = {subtema}\n tema = {tema}')
    if i >= len(hechos):
        return False
    hecho = hechos[i]
    
    if hecho[0] == "subtema" and hecho[1] == subtema:
        if hecho[2] == tema:
            return True
        else:
            return False

    return pertenece(subtema, tema, i + 1)
#--------------------SEGUNDA CLAUSULA SIN RECURSIVIDAD----------------------------------------------------------------
"""
#Si el usuario envía una respuesta incorrecta de un SUBTEMA → requiere apoyo en el TEMA 
def necesita_refuerzo(usuario, subtema, i=0):
    for hecho in hechos:
        if hecho[0] == "respuesta_incorrecta":
            if hecho[1] == usuario and hecho[2] == subtema:
                for h in hechos:
                    if h[0] == "subtema" and h[1] == subtema:
                        tema = h[2]
                        print(f"el usuario {usuario} necesita refuerzo en el tema {tema}")
                        return True
    return False
"""
#---------------SEGUNDA CLAUSULA CON RECURSIVIDAD----------------------------------------------------
def necesita_refuerzo(usuario, subtema, i=0, j=0):
    if i >= len(hechos):
        return False
    hecho = hechos[i]
    if hecho[0] == "respuesta_incorrecta":
        if hecho[1] == usuario and hecho[2] == subtema:
            return buscar_tema(subtema, 0, usuario)
    return necesita_refuerzo(usuario, subtema, i + 1, 0)

def buscar_tema(subtema, j=0, usuario=None):

    if j >= len(hechos):
        return False
    hecho = hechos[j]
    if hecho[0] == "subtema" and hecho[1] == subtema:
        tema = hecho[2]
        print(f'UNIFICACION Y SUSTITUCION \n subtema = {subtema}\n tema = {tema}')
        print(f"el usuario {usuario} necesita refuerzo en el tema {tema}")
        return True
    return buscar_tema(subtema, j + 1, usuario)
#-------------------------------------------------------------------------------------------
if __name__ == '__main__':
    print(f'RESULTADO: {pertenece("conceptos_basicos","diseno_algoritmico")}')
    print(necesita_refuerzo("usuario1", "diseno_algoritmos"))


