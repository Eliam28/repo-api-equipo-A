from fastapi import APIRouter, HTTPException
from app.Core.woocommerce_client import wcapi
from app.Core.config import settings
from app.API.wordpress.clientes.schema_json import CustomerCreate, Address

router = APIRouter()

@app.post("/")
async def create_woocommerce_customer(customer: CustomerCreate):
    # Convertimos el modelo de Pydantic a un diccionario de Python
    customer_data = customer.model_dump() 
    
    # Enviamos a WooCommerce
    response = wcapi.post("customers", customer_data)
    
    # Validamos si WooCommerce aceptó la creación
    if response.status_code == 201:
        return response.json()
    else:
        # Si algo falla (ej. el email ya existe), lanzamos error
        raise HTTPException(
            status_code=response.status_code, 
            detail=response.json()
        )