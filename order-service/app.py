from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Order Service is running"}

@app.get("/orders")
def get_orders():
    return {
        "orders": [
            {"id": 101, "item": "Laptop"},
            {"id": 102, "item": "Keyboard"}
        ]
    }
