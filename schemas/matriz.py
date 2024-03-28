from pydantic import BaseModel

class Matriz(BaseModel):
    z: int
    MatrisG: list[list[int]]