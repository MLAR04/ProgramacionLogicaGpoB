# Sistema de Detección de Enfermedades Comunes

## Base de Conocimiento

- **Gripe**: Tos y dolor de cabeza  
- **Covid**: Fiebre, tos, cansancio, pérdida del olfato  
- **Migraña**: Dolor de cabeza, náuseas  
- **Resfriado**: Congestión nasal, fiebre y tos  
- **No te puedo diagnosticar**: Cuando los síntomas no coinciden exactamente con ninguna enfermedad

## Reglas del Sistema

1. Si tienes **todos los sintomas** de una enfermedad → se diagnostica esa enfermedad.  
2. Si tienes **tos y dolor de cabeza** → tienes **Gripe**.  
3. Si tienes **fiebre, tos, cansancio y pérdida del olfato** → tienes **Covid**.  
4. Si tienes **dolor de cabeza y náuseas** → tienes **Migraña**.  
5. Si tienes **congestión nasal, fiebre y tos** → tienes **Resfriado**.  


## Función de Diagnostico Utilizada

```python

from Hechos import enfermedades

def diagnosticar(sintomas_usuario):
      
    sintomas_usuario = set(map(lambda s: s.strip().lower(), sintomas_usuario))

    enfermedad = next(
        (malestar for malestar, sintomas in enfermedades.items() if sintomas_usuario == sintomas),
        "No te puedo diagnosticar"
    )

    return enfermedad