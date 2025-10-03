from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Enfermedad:
    nombre: str
    sintomas: List[str]

# Base de conocimiento
BASE_CONOCIMIENTO = [
    Enfermedad("Gripe", ["tos", "dolor de cabeza"]),
    Enfermedad("COVID-19", ["fiebre", "tos", "cansancio", "perdida del olfato"]),
    Enfermedad("Migrana", ["dolor de cabeza", "nauseas"]),
    Enfermedad("Resfriado", ["congestion nasal", "fiebre", "tos"])
]

def contiene_todos(sintomas_paciente: List[str], sintomas_enfermedad: List[str]) -> bool:
    """Revisa si el paciente tiene todos los sintomas de la enfermedad"""
    return all(s in sintomas_paciente for s in sintomas_enfermedad)

def diagnosticar(sintomas_paciente: List[str], enfermedades: List[Enfermedad]) -> str:
    """Recursivamente diagnostica la enfermedad solo si se tienen todos los sintomas"""
    if not enfermedades:
        return "No se puede diagnosticar"
    
    enfermedad_actual = enfermedades[0]
    if contiene_todos(sintomas_paciente, enfermedad_actual.sintomas) and len(sintomas_paciente) == len(enfermedad_actual.sintomas):
        return enfermedad_actual.nombre
    else:
        return diagnosticar(sintomas_paciente, enfermedades[1:])
