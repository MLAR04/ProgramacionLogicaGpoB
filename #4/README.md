# Base de Conocimiento: Diagnóstico de Enfermedades

Este archivo contiene los **hechos** (síntomas asociados a cada enfermedad) y las **leyes** (reglas de inferencia) que conforman la base de conocimiento del sistema experto de diagnóstico.

---

## Hechos (Base de Conocimiento)

- **Gripe**:  
  - tos  
  - dolor de cabeza  

- **COVID**:  
  - fiebre  
  - tos  
  - cansancio  
  - pérdida del olfato  

- **Migraña**:  
  - dolor de cabeza  
  - náuseas  

- **Resfriado**:  
  - congestión nasal  
  - tos  
  - fiebre  

---

## Leyes (Reglas de Inferencia)

1. **Si tienes todos los síntomas de cierta enfermedad, entonces la tienes.**

2. **Reglas específicas:**
   - Si tienes **tos** y **dolor de cabeza**, entonces tienes **gripe**.  
   - Si tienes **fiebre**, **tos**, **cansancio** y **pérdida del olfato**, entonces tienes **COVID**.  
   - Si tienes **dolor de cabeza** y **náuseas**, entonces tienes **migraña**.  
   - Si tienes **congestión nasal**, **fiebre** y **tos**, entonces tienes **resfriado**.  

---

## Funcionamiento del sistema


1. El usuario ingresa sus síntomas uno por uno.  
2. El motor de inferencia compara los síntomas del usuario con los hechos de la base de conocimiento.  
3. Si los síntomas coinciden **exactamente** con los de una enfermedad, se muestra el diagnóstico.  
4. En caso contrario, se devuelve:  
  **"No te puedo diagnosticar con esos síntomas."**
