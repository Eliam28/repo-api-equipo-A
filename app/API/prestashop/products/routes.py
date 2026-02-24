from fastapi import APIRouter
from app.Core.prestashop_client import prestashop_get

router = APIRouter()

fieldsproducts = "id,name,price,wholesale_price,quantity,reference,active,id_category_default,date_add,date_upd"

@router.get("/")
def get_products():
    products = prestashop_get("products", fieldsproducts)
    return products