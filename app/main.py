from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Day 1 Workshop API", version="1.0")

class SumRequest(BaseModel):
    a: float
    b: float


def add_numbers(a: float, b: float) -> float:
    return a + b


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}


@app.post("/add")
def add(payload: SumRequest):
    return {"result": add_numbers(payload.a, payload.b)}
