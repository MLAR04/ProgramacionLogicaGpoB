# Tablas de Verdad en Python

Este programa genera **tablas de verdad** a partir de reglas lógicas descompuestas en proposiciones.  

Se incluyen tres casos como ejemplos prácticos:

1. **Número múltiplo de 6**  
   - Regla general:  
     ```
     Rg ↔ (R1 ∧ R2)
     ```
   - R1: El número es divisible entre 2  
   - R2: El número es divisible entre 3  
   - Rg: El número es múltiplo de 6  

2. **Persona puede votar**  
   - Regla general:  
     ```
     Rg ↔ (R1 ∧ R2 ∧ R3)
     ```
   - R1: Tiene más de 18 años  
   - R2: Tiene credencial de elector  
   - R3: Está en la lista nominal  
   - Rg: La persona puede votar  

3. **Conexión a Internet**  
   - Regla general:  
     ```
     Rg ↔ (R1 ∨ R2) ∧ R3
     ```
   - R1: Tiene Wi-Fi activado  
   - R2: Tiene cable Ethernet conectado  
   - R3: El módem funciona  
   - Rg: La computadora puede conectarse a Internet  

---

## Contenido del proyecto

- `reglas.py` → Código en Python que genera las tablas de verdad automáticamente.  
- `README.md` → Este archivo con explicación y guía de uso.

---

## Instrucciones de uso

1. Descarga o copia el archivo `reglas.py`.  
2. Abre una terminal en la carpeta donde se encuentra el archivo.  
3. Ejecuta el programa con:  

```bash
python reglas.py
