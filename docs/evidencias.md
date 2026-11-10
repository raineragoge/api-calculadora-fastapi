## Evidencias de Swagger y Colab

Las siguientes salidas se obtuvieron durante la práctica. El [notebook original](../Cliente_API_Calculadora.ipynb) conserva los resultados de ambas peticiones a través del túnel de ngrok.

### Swagger UI: GET

- Endpoint: `GET /doble/8`
- URL de prueba: `http://127.0.0.1:8000/doble/8`
- Estado HTTP: **200**
- Respuesta JSON:

```json
{"numero": 8, "doble": 16}
```

### Swagger UI: POST

- Endpoint: `POST /sumar`
- Body: `{"a": 15, "b": 25}`
- Estado HTTP: **200**
- Respuesta JSON:

```json
{"resultado": 40.0}
```

### Google Colab: GET a través de ngrok

```text
Código HTTP: 200
Resultado: {'numero': 12, 'doble': 24}
```

### Google Colab: POST a través de ngrok

```text
Código HTTP: 200
Resultado: {'resultado': 100.0}
```

Las salidas de Colab se conservan tal como fueron generadas en el cuaderno entregado. La URL del túnel utilizada en la práctica puede haber caducado; para repetirlas, arranca Docker, lanza `ngrok http 8001` y cambia el dominio HTTPS en el notebook.
