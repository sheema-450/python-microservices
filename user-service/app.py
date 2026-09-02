from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "User Service is running"}

@app.get("/users")
def get_users():
    return {
        "users": [
            {"id": 1, "name": "Sheema"},
            {"id": 2, "name": "John"}
        ]
    }
