# 🌎 Proyecto Turismo – API con FastAPI

Este proyecto implementa una **API REST** para un sistema de turismo que permite consultar hoteles, lugares turísticos y actividades cercanas según ubicación, tipo de lugar y presupuesto.  
Está desarrollado con **Python 3**, **FastAPI** y **Uvicorn**, e incluye datos simulados de hoteles y puntos de interés.

---

## 🚀 Características principales

- Listado de **hoteles** con información de ciudad, precio, etiquetas y coordenadas.
- Consulta de **actividades cercanas** a un hotel dentro de un radio configurable.
- Filtros dinámicos por:
  - Presupuesto
  - Ciudad
  - Etiquetas de hotel
  - Tipos de actividad
- Cálculo de **distancias geográficas** usando la fórmula de Haversine.
- API totalmente compatible con **CORS** para acceso desde aplicaciones web.
- Servidor de contenido estático (carpeta `/html`).

---

## 📁 Estructura del proyecto

├── api.py # Archivo principal con los endpoints de la API
├── config.py # Configuración general: tipos de lugares, etiquetas, distancias
├── data.py # Datos simulados de hoteles y lugares turísticos
├── logic.py # Lógica de filtrado, distancia y validaciones
├── install.txt # Dependencias del proyecto (FastAPI y Uvicorn)
└── html/ # Carpeta para archivos estáticos (HTML, imágenes, etc.)


---

## ⚙️ Instalación

### 1️⃣ Requisitos
- Python 3.8 o superior
- pip instalado

### 2️⃣ Instalación de dependencias
Ejecuta el siguiente comando en la raíz del proyecto:

```bash
pip install -r install.txt


## ▶️ Ejecución

Inicia el servidor con:

uvicorn api:app --reload


Luego abre tu navegador en:

http://127.0.0.1:8000


La documentación interactiva (Swagger UI) estará disponible en:

http://127.0.0.1:8000/docs

## 💡 Ejemplo de uso
Filtrar hoteles (POST /hoteles/filtrados)

Cuerpo del request (JSON):

{
  "presupuesto": 1200,
  "modo": "por_noche",
  "ciudad": "Tijuana",
  "tags_incluir": ["familiar"],
  "tags_excluir": ["negocios"]
}


Respuesta:

[
  {
    "id": "h_001",
    "nom": "Hotel Bahía Azul",
    "ciudad": "Tijuana",
    "precio_noche": 1200.0,
    "costo_calculado": 1200.0,
    "tags": ["familiar", "playa", "pet"],
    "lat": 32.5149,
    "lon": -117.0382
  }
]

## 🧩 Archivos principales
logic.py

Contiene las funciones que calculan distancias, filtran hoteles y aplican reglas de coincidencia de etiquetas.

config.py

Define las constantes globales del sistema:

DEFAULT_DIST → distancia por defecto (km)

PLACE_TYPE → tipos de actividades (con emojis)

HOTEL_TAGS → categorías para los hoteles

data.py

Incluye listas de:

Hoteles → nombre, ciudad, coordenadas, precio y etiquetas

Lugares → tipo, ubicación y nivel de precio

##🧠 Funcionalidades técnicas destacadas

Cálculo geográfico: utiliza la fórmula Haversine para medir distancia entre dos puntos (lat/lon).

Filtros personalizados: los usuarios pueden incluir o excluir etiquetas para refinar los resultados.

Estructura modular: permite fácilmente reemplazar los datos estáticos por una base de datos real en el futuro.

FastAPI CORS: compatible con cualquier frontend o cliente HTTP.

