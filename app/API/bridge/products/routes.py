from fastapi import APIRouter
from app.API.bridge.products.service import sync_products, create_one_product_by_reference
from app.API.prestashop.utils import ps_success, ps_error
from app.Core.prestashop_client import prestashop_get, prestashop_put


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


@router.delete("/ref/{reference}")  #Aún no funciona, tengo que pasar la respuesta a un xml para poder hacer el put 👍
def deactivate_product(reference: str):
    try:
        data = prestashop_get("products", filters={"reference": reference})

        if not data:
            return ps_error("404", "No se encontró un producto con la referencia dada")
        
        id = data['products'][0]['id']

        product = prestashop_get(f"products/{id}")
        
        product['product']['active'] = "0"
        prestashop_put("products", product)

        return ps_success(product)
    
    except Exception as e:
        return ps_error("500",str(e) )