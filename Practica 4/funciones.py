
from Hechos import enfermedades

def diagnosticar(sintomas_usuario):
      
    sintomas_usuario = set(map(lambda s: s.strip().lower(), sintomas_usuario))

    enfermedad = next(
        (malestar for malestar, sintomas in enfermedades.items() if sintomas_usuario == sintomas),
        "No te puedo diagnosticar"
    )

    return enfermedad
