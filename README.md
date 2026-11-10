# API Calculadora · FastAPI + Docker

Aplicación web educativa de una calculadora construida con **FastAPI (Python)**, **HTML, CSS y JavaScript**, y ejecutada dentro de un contenedor **Docker**. También se ha probado el acceso remoto mediante **ngrok** y el consumo de la API desde **Google Colab**.

## ¿Qué hace?

- Calcula el doble de un entero mediante una petición **GET**.
- Suma dos números mediante una petición **POST** que envía un cuerpo JSON.
- Presenta una interfaz web responsive que utiliza `fetch()` para comunicarse con la API.
- Expone documentación interactiva con Swagger UI en `/docs`.

## Arquitectura

```text
Navegador / Google Colab
          |
       HTTP(S)
          |
     [ngrok]  (opcional para acceder desde Internet)
          |
 localhost:8001
          |
     Contenedor Docker
          |
     Uvicorn :8000
          |
       FastAPI
        /   \
GET /doble   POST /sumar
```

El HTML se sirve desde FastAPI en la ruta `/`, por lo que el frontend y la API comparten origen y no requieren configurar CORS para este ejemplo.

## Requisitos

- **Docker Desktop**, con el motor en ejecución, para la opción recomendada.
- Alternativamente, **Python 3.12+** para ejecutarla directamente sin Docker.

## Ejecutar con Docker (recomendado)

Desde la carpeta del proyecto:

```bash
docker build -t api-calculadora .
docker run --rm --name calculadora-api -p 8001:8000 api-calculadora
```

Abre:

- Interfaz gráfica: http://localhost:8001/
- Documentación Swagger: http://localhost:8001/docs
- Ejemplo GET: http://localhost:8001/doble/9

Para detener el contenedor, pulsa **Ctrl+C** en la terminal. Si el nombre ya está ocupado por un contenedor anterior, puedes detenerlo y eliminarlo con `docker rm -f calculadora-api` y volver a ejecutar `docker run`.

## Ejecutar sin Docker

En Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Abre http://127.0.0.1:8000/ y http://127.0.0.1:8000/docs.

## Endpoints

| Método | Ruta | Entrada | Respuesta de ejemplo |
| --- | --- | --- | --- |
| GET | `/` | Ninguna | Página HTML |
| GET | `/doble/{numero}` | Número entero en la ruta | `{"numero": 9, "doble": 18}` |
| POST | `/sumar` | JSON `{"a": 3, "b": 4}` | `{"resultado": 7.0}` |

**Ejemplo GET** (desde una terminal):

```bash
curl http://localhost:8001/doble/9
```

**Ejemplo POST** (desde PowerShell):

```powershell
Invoke-RestMethod -Uri http://localhost:8001/sumar -Method Post -ContentType 'application/json' -Body '{"a":3,"b":4}'
```

### Consumir desde Google Colab

Primero, con Docker en ejecución, crea un túnel local:

```bash
ngrok http 8001
```

Copia la URL HTTPS generada por ngrok y úsala en Colab:

```python
import requests

BASE_URL = "https://TU-DOMINIO.ngrok-free.dev"  # Sustituye por tu URL actual
headers = {"ngrok-skip-browser-warning": "true"}

get_response = requests.get(f"{BASE_URL}/doble/12", headers=headers, timeout=15)
get_response.raise_for_status()
print(get_response.json())  # {'numero': 12, 'doble': 24}

post_response = requests.post(
    f"{BASE_URL}/sumar",
    json={"a": 35, "b": 65},
    headers=headers,
    timeout=15,
)
post_response.raise_for_status()
print(post_response.json())  # {'resultado': 100.0}
```

> **Seguridad:** el túnel ngrok expone estos endpoints a Internet mientras esté activo. Este proyecto es una demostración sin autenticación: no lo utilices para procesar datos privados ni expongas tokens de ngrok en el repositorio. Detén el túnel cuando acabes.

## Estructura del proyecto

```text
api-calculadora-fastapi/
├── .dockerignore
├── .gitignore
├── Dockerfile
├── README.md
├── index.html
├── main.py
└── requirements.txt
```

## Qué se ha aprendido

1. Crear endpoints **GET** y **POST** en FastAPI.
2. Validar cuerpos JSON con **Pydantic**.
3. Probar la API con Swagger/OpenAPI.
4. Contenerizar una aplicación Python con Docker.
5. Exponer temporalmente un servidor local con ngrok.
6. Consumir una API con `requests` desde Colab.
7. Conectar una interfaz HTML/JavaScript a un backend mediante `fetch()`.

**Alcance:** proyecto didáctico. No incluye autenticación, persistencia de datos, despliegue permanente ni CI/CD.