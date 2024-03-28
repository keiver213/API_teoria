from fastapi import FastAPI
from schemas.matriz import Matriz
from core.CodeElem import ejecutable

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the API to get the lineal code and the elements from a matrix"}

@app.post("/lineal_code")
async def codes(matriz: Matriz):
    return ejecutable(matriz.MatrisG, matriz.z)