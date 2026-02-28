from fastapi import FastAPI
from app.API.router_odoo import router as api_router_odoo
from app.API.router_prestashop import router as api_router_prestashop
from app.API.router_bridge import router as api_router_bridge

app = FastAPI()

@app.get("/")
def root():
    return {"mensaje": "api funcionado nene"}

app.include_router(api_router_odoo, prefix="/api/odoo")

app.include_router(api_router_prestashop, prefix="/api/prestashop")

app.include_router(api_router_bridge, prefix="/api/bridge")