from typing import List, Callable, Optional
#Hechos
Enfermedades: dict[str, List[str]] = {
    'gripe': ['tos', 'dolor de cabeza'],
    'covid': ['fiebre', 'tos', 'cansancio', 'perdida del olfato'],
    'migraña': ['dolor de cabeza', 'nauseas'],
    'resfriado': ['congestion nasal', 'fiebre', 'tos'],
}

#Reglas
def tiene_gripe(sintomas: List[str]) -> Optional[str]: 
    return "gripe" if set(sintomas) == set(Enfermedades['gripe']) else None

def tiene_covid(sintomas: List[str]) -> Optional[str]: 
    return "covid" if set(sintomas) == set(Enfermedades['covid']) else None

def tiene_migraña(sintomas: List[str]) -> Optional[str]: 
    return "migraña" if set(sintomas) == set(Enfermedades['migraña']) else None

def tiene_resfriado(sintomas: List[str]) -> Optional[str]: 
    return "resfriado" if set(sintomas) == set(Enfermedades['resfriado']) else None

Reglas: List[Callable[[List[str]], Optional[str]]] = [
    tiene_gripe, tiene_covid, tiene_migraña, tiene_resfriado
]

def generar_diagnostico(sintomas: List[str], reglas: List[Callable[[List[str]], Optional[str]]] = Reglas) -> str:
    if not reglas:
        return "No se puede diagnosticar"
    
    regla = reglas[0]
    resultado = regla(sintomas)
    if resultado:  
        return f"Diagnóstico: {resultado.capitalize()}"
    else:
        return generar_diagnostico(sintomas, reglas[1:])
