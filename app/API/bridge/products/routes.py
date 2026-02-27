from fastapi import APIRouter
from app.API.bridge.products.service import sync_products, create_one_product_by_reference
from app.API.prestashop.utils import ps_success, ps_error


router = APIRouter()

@router.get("/")
def sync():

    try:
        result = sync_products()
        return ps_success(result)

    except Exception as e:
        return ps_error("500", str(e))
    
@router.get("/create-one/{reference}")
def create_one(reference: str):
  try:
    result = create_one_product_by_reference(reference)
    return ps_success(result)
  except Exception as e:
    return ps_error("500", str(e))