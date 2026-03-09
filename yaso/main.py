from fastapi import FastAPI
from services.base import ServiceManager

app = FastAPI()
manager = ServiceManager()

@app.post("/services/{service_name}")
async def create_service(service_name: str, data: dict):
    return manager.create_service(service_name, data)
