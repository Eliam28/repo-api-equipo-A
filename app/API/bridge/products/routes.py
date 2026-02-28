from fastapi import APIRouter
from app.API.bridge.products.service import sync_products, create_one_product_by_reference
from app.API.prestashop.utils import ps_success, ps_error
from app.Core.prestashop_client import prestashop_get, prestashop_put
from app.API.bridge.products.mapper_product_update import product_update


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


@router.delete("/ref/{reference}")  
def deactivate_product(reference: str):
    try:
        data = prestashop_get("products", filters={"reference": reference})

        if not data:
            return ps_error("404", "No se encontró un producto con la referencia dada")
        
        product = data['products'][0]
        id = product['id']

        if (isinstance(product['name'], list)):
           name = product['name'][0]['value']
        else:
           name = product['name']
        
        if (isinstance(product['link_rewrite'], list)):
           slug = product['link_rewrite'][0]['value']
        else:
           slug = product['link_rewrite']

        xml = product_update(
          id = id,
          active = "0",
          name = name,
          slug = slug,
          reference = reference
        )

        prestashop_put(f"products/{id}", xml)

        return ps_success(data)
    
    except Exception as e:
        return ps_error("500",str(e) )