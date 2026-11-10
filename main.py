from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI(title="API Calculadora", version="1.0.0")
BASE_DIR = Path(__file__).resolve().parent


class Suma(BaseModel):
    a: float
    b: float


@app.get("/doble/{numero}")
def calcular_doble(numero: int):
    return {"numero": numero, "doble": numero * 2}


@app.post("/sumar")
def sumar(datos: Suma):
    return {"resultado": datos.a + datos.b}


@app.get("/", include_in_schema=False)
def mostrar_interfaz():
    return FileResponse(BASE_DIR / "index.html")
