from fastapi import APIRouter
from app.Core.prestashop_client import prestashop_get

router = APIRouter()

@router.get("/")
def get_products():
    products = prestashop_get("orders")
    return products