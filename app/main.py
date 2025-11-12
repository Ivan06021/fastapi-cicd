from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}


def add_numbers(a: int, b: int) -> int:
    return a + b


def multiply_numbers(a: int, b: int) -> int:
    return a * b


@app.post("/calculate")
def calculate(a: int, b: int, operation: str = "add"):
    if operation == "add":
        return {"result": add_numbers(a, b)}
    elif operation == "multiply":
        return {"result": multiply_numbers(a, b)}
    return {"error": "Invalid operation"}
