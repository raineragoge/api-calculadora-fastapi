"""Pruebas de integración de la API calculadora."""

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_interfaz_se_sirve_en_la_raiz():
    respuesta = client.get("/")
    assert respuesta.status_code == 200
    assert "text/html" in respuesta.headers["content-type"]
    assert "Calculadora." in respuesta.text
    assert 'id="formulario"' in respuesta.text


def test_get_doble():
    respuesta = client.get("/doble/9")
    assert respuesta.status_code == 200
    assert respuesta.json() == {"numero": 9, "doble": 18}


def test_get_doble_negativo_y_cero():
    assert client.get("/doble/-4").json()["doble"] == -8
    assert client.get("/doble/0").json()["doble"] == 0


def test_get_doble_rechaza_decimales():
    assert client.get("/doble/1.5").status_code == 422


def test_post_suma():
    respuesta = client.post("/sumar", json={"a": 3, "b": 4})
    assert respuesta.status_code == 200
    assert respuesta.json() == {"resultado": 7.0}


def test_post_suma_decimales_y_negativos():
    respuesta = client.post("/sumar", json={"a": 3.5, "b": -1.2})
    assert respuesta.status_code == 200
    assert abs(respuesta.json()["resultado"] - 2.3) < 1e-9


def test_post_suma_requiere_los_dos_operandos():
    assert client.post("/sumar", json={"a": 3}).status_code == 422


def test_post_suma_rechaza_texto_invalido():
    assert client.post("/sumar", json={"a": "texto", "b": 4}).status_code == 422


def test_documentacion_openapi():
    respuesta = client.get("/openapi.json")
    assert respuesta.status_code == 200
    esquema = respuesta.json()
    assert "/doble/{numero}" in esquema["paths"]
    assert "/sumar" in esquema["paths"]
    assert "/" not in esquema["paths"]  # La interfaz no figura como operación de API
