# Diagrama de arquitectura y flujo de la API

El cliente remoto (Google Colab) realiza peticiones HTTP/HTTPS al dominio temporal de ngrok. El túnel redirige la petición al puerto **8001** del equipo Windows; Docker publica ese puerto hacia el **8000** del contenedor Linux, donde Uvicorn sirve la aplicación FastAPI. FastAPI ejecuta el endpoint y devuelve JSON por el mismo camino, en sentido contrario.

```mermaid
flowchart LR
    C["Google Colab<br/>Python + requests"]
    N["ngrok<br/>URL HTTPS pública"]
    D["Docker Desktop<br/>Windows :8001 → Linux :8000"]
    A["Uvicorn / FastAPI<br/>:8000"]
    E["GET /doble/{numero}<br/>POST /sumar"]
    L["Navegador local<br/>localhost:8001"]
    S["Swagger UI<br/>GET /docs"]

    C -- "1. Petición HTTPS GET / POST" --> N
    N -- "2. Túnel a localhost:8001" --> D
    D -- "3. Redirección al puerto 8000" --> A
    A -- "4. Ejecutar endpoint" --> E
    E -. "5. JSON de respuesta" .-> A
    A -. "6. HTTP 200 + JSON" .-> D
    D -. "7. Respuesta HTTP" .-> N
    N -. "8. Respuesta HTTPS" .-> C
    L <-- "Acceso local sin ngrok" --> D
    L --> S
    S -. "Documentación generada por FastAPI" .-> A

    classDef client fill:#eef1ff,stroke:#6e7caa,color:#202646;
    classDef network fill:#e6f7f3,stroke:#39947b,color:#173b33;
    classDef container fill:#fff2e3,stroke:#cc8b3e,color:#50300e;
    class C,L client;
    class N network;
    class D,A,E,S container;
```

**Convenciones:** líneas continuas = envío/uso de la API; líneas discontinuas = recorrido de la respuesta JSON.

## Pruebas de esta entrega

- `GET /doble/12`: HTTP `200` → `{"numero": 12, "doble": 24}`.
- `POST /sumar` con `{"a": 35, "b": 65}`: HTTP `200` → `{"resultado": 100.0}`.
- Ambas respuestas están guardadas en [Cliente_API_Calculadora.ipynb](../Cliente_API_Calculadora.ipynb).
