## 🎯 Objetivo de la Practica
Aplicar la **descomposicion de reglas logicas** para analizar predicados y transformarlos en expresiones logicas, tablas de verdad y finalmente representarlos mediante **codigo en Python**.

---

## 📚 Enunciados a Resolver

1. **Un numero es multiplo de 6** si es divisible entre 2 y divisible entre 3.  
2. **Una persona puede votar** si tiene mas de 18 años, tiene credencial de elector y esta en la lista nominal.  
3. **Una computadora puede conectarse a internet** si tiene Wi-Fi activado o cable Ethernet conectado, y ademas el modem funciona.

---

## 📝 Desarrollo

### 1. Multiplo de 6
**Reglas:**
- r1: El numero es divisible entre 2  
- r2: El numero es divisible entre 3  

**Regla General:**
- Multiplo de 6 si (r1 ∧ r2)

**Tabla de Verdad:**

| r1   | r2   | r1 ∧ r2 | Multiplo de 6 |
|------|------|---------|---------------|
| T    | T    | T       | T             |
| T    | F    | F       | F             |
| F    | T    | F       | F             |
| F    | F    | F       | F             |

---

### 2. Derecho a Votar
**Reglas:**
- r1: La persona tiene mas de 18 años  
- r2: Tiene credencial de elector  
- r3: Esta en la lista nominal  

**Regla General:**
- Puede votar si (r1 ∧ r2 ∧ r3)

**Tabla de Verdad (8 combinaciones):**

| r1   | r2   | r3   | r1 ∧ r2 ∧ r3 | Puede Votar |
|------|------|------|--------------|-------------|
| T    | T    | T    | T            | T           |
| T    | T    | F    | F            | F           |
| T    | F    | T    | F            | F           |
| T    | F    | F    | F            | F           |
| F    | T    | T    | F            | F           |
| F    | T    | F    | F            | F           |
| F    | F    | T    | F            | F           |
| F    | F    | F    | F            | F           |

---

### 3. Conexion a Internet
**Reglas:**
- r1: La computadora tiene Wi-Fi activado  
- r2: Tiene cable Ethernet conectado  
- r3: El modem funciona  

**Regla General:**
- Conexion a Internet si ((r1 ∨ r2) ∧ r3)

**Tabla de Verdad (8 combinaciones):**

| r1   | r2   | r3   | r1 ∨ r2 | (r1 ∨ r2) ∧ r3 | Conexion |
|------|------|------|---------|----------------|----------|
| T    | T    | T    | T       | T              | T        |
| T    | T    | F    | T       | F              | F        |
| T    | F    | T    | T       | T              | T        |
| T    | F    | F    | T       | F              | F        |
| F    | T    | T    | T       | T              | T        |
| F    | T    | F    | T       | F              | F        |
| F    | F    | T    | F       | F              | F        |
| F    | F    | F    | F       | F              | F        |

---

## 💻 Codigo en Python

- Todos los predicados estan implementados en **archivos separados** dentro de la carpeta `practica3/`.
- Cada archivo imprime:
  1. Las **reglas**  
  2. La **expresion general**  
  3. La **tabla de verdad** generada automaticamente  