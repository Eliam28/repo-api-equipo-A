from fastapi import APIRouter
from app.API.bridge.products.service import sync_products
from app.API.prestashop.utils import ps_success, ps_error

router = APIRouter()

@router.get("/")
def sync():

    try:
        result = sync_products()
        return ps_success(result)

    except Exception as e:
        return ps_error("500", str(e))