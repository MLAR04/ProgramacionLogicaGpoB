# Base de Conocimiento: Enfermedades y Sintomas

## Hechos
- **Gripe**: tos, dolor de cabeza
- **COVID-19**: fiebre, tos, cansancio, perdida del olfato
- **Migraña**: dolor de cabeza, nauseas
- **Resfriado**: congestion nasal, fiebre, tos
- **Sin diagnostico**: cuando los sintomas no coinciden con ninguna enfermedad conocida

## Reglas
1. **Regla general**:
   - Si un paciente presenta **todos los sintomas de una enfermedad**, entonces se diagnostica esa enfermedad.

2. **Reglas especificas**:
   - Si un paciente tiene **tos y dolor de cabeza**, entonces tiene **Gripe**.
   - Si un paciente tiene **fiebre, tos, cansancio y perdida del olfato**, entonces tiene **COVID-19**.
   - Si un paciente tiene **dolor de cabeza y nauseas**, entonces tiene **Migraña**.
   - Si un paciente tiene **congestion nasal, fiebre y tos**, entonces tiene **Resfriado**.
   - Si los sintomas no cumplen ninguna de las reglas, entonces **No se puede diagnosticar**.

## Archivos

- **motor_inferencia.py**: Contiene el motor de inferencia y la base de conocimiento.
- **interfaz.py**: Contiene la interfaz grafica en Tkinter para ingresar los sintomas.
- **main.py**: Archivo principal para ejecutar la interfaz del programa. (este es el que se corre)

