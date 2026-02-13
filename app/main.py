from fastapi import FastAPI
from app.api.router import router as api_router

app = FastAPI()

@app.get("/")
def root():
    return {"mensaje": "api funcionado nene"}

app.include_router(api_router, prefix="/api")