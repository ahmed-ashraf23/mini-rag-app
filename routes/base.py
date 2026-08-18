from fastapi import FastAPI, APIRouter
import os

base_router = APIRouter(
    prefix="/api/v1",
)

@base_router.get("/", tags=['General'])
async def welcome():
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")
    return{
        "message":f"Welcome to {app_name} App version {app_version}"
    }
