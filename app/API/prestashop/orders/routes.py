from fastapi import APIRouter
from app.Core.prestashop_client import prestashop_get

router = APIRouter()

fieldsorders = "id,id_customer,total_paid,date_add,reference"

@router.get("/")
def get_products():
    products = prestashop_get("orders", fieldsorders)
    return products