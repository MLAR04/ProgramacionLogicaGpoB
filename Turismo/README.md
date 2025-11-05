# 🧠 Sistema de Inferencia para Turismo Inteligente

## 🔹 Introducción o Descripción General

### 📌 Propósito del sistema
El presente proyecto implementa un **motor de inferencia para recomendaciones turísticas**, desarrollado en **Python** utilizando el framework **FastAPI**.  
Su propósito es **sugerir hoteles y actividades turísticas** basándose en información geográfica, preferencias del usuario (presupuesto, ciudad, tipo de actividad) y etiquetas asociadas a cada hotel o lugar.

El sistema actúa como una **API inteligente** capaz de analizar datos (hechos) y aplicar reglas lógicas (inferencia) para determinar los hoteles más adecuados y las actividades cercanas según criterios definidos.

### 🧭 Tipo de inferencia
El sistema utiliza una **inferencia hacia adelante (forward chaining)**.  
Esto significa que parte de los **hechos existentes** (hoteles, precios, coordenadas, etiquetas, etc.) y **aplica reglas de filtrado** definidas en el motor lógico (`logic.py`) para **deducir nuevos hechos** o resultados (por ejemplo, qué hoteles cumplen con el presupuesto y las preferencias del usuario).

En el proceso:
1. Se leen los datos base (hechos) desde `data.py`.  
2. El usuario ingresa parámetros como presupuesto, ciudad o etiquetas.  
3. El motor lógico aplica las reglas de inferencia para filtrar resultados válidos.  
4. La API devuelve la lista de hoteles o actividades que cumplen esas condiciones.

### 🌍 Alcance y limitaciones
**Alcance:**
- Permite consultar hoteles por ciudad, presupuesto y etiquetas.
- Calcula distancias geográficas reales entre hoteles y actividades.
- Sugiere actividades cercanas en un radio configurable (por defecto, 5 km).
- Compatible con aplicaciones web mediante CORS.

**Limitaciones:**
- La base de conocimientos es estática (almacenada localmente en `data.py`).
- No incluye persistencia en base de datos ni aprendizaje automático.
- Las reglas de inferencia están definidas de forma explícita en código (no dinámicas).
- El sistema no actualiza hechos automáticamente; requiere reinicio para incorporar nuevos datos.
---
⚙️ Lógica de Inferencia (Reglas y Filtros) 
El motor utiliza una lógica de Inferencia Hacia Adelante (Forward Chaining) basada en filtros secuenciales:

Filtro de Ciudad (Si se proporciona el parámetro ciudad). 

Filtro de Costo (Si se proporciona el presupuesto): 
El hotel pasa solo si su costo_calculado (basado en modo/noches) es $\le$ presupuesto.

Filtro de Tags: El hotel pasa si cumple:tags_incluir: Debe contener TODOS los tags solicitados (AND lógico).tags_excluir: No debe contener NINGÚN tag de la lista (NOT ANY lógico).Los hoteles que superan los filtros se ordenan finalmente por costo_calculado de menor a mayor.

---
## Casos prueba
<img width="1918" height="978" alt="image" src="https://github.com/user-attachments/assets/5ca77bf4-73cf-4dcf-b922-7c0430b7a4a0" />

<img width="1913" height="963" alt="image" src="https://github.com/user-attachments/assets/fab42ec5-f328-4a55-b53b-dfbe40b09773" />



--
## 🧩 Base de Conocimientos

La base de conocimientos del sistema está constituida por **hechos y reglas** que permiten realizar inferencias sobre los datos turísticos.

### 🧱 Hechos
Los **hechos** se encuentran definidos en el archivo `data.py` e incluyen dos estructuras principales:

#### 1️⃣ Hoteles
Cada hotel tiene los siguientes atributos:
- `id`: Identificador único.  
- `nom`: Nombre del hotel.  
- `ciudad`: Ciudad donde se ubica.  
- `lat`, `lon`: Coordenadas geográficas.  
- `precio_noche`: Precio promedio por noche.  
- `tags`: Lista de etiquetas (por ejemplo: “familiar”, “negocios”, “romántico”).  

Ejemplo:
```python
{"id": "h_001", "nom": "Hotel Bahía Azul", "ciudad": "Tijuana", "lat": 32.5149, "lon": -117.0382, "precio_noche": 1200.0, "tags": ["familiar", "playa", "pet"]}






