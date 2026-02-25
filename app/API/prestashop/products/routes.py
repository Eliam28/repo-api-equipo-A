from fastapi import APIRouter
from app.Core.prestashop_client import prestashop_get
from app.API.prestashop.utils import ps_success, ps_error

router = APIRouter()

fieldsproducts = "id,name,price,wholesale_price,quantity,reference,active,id_category_default,date_add,date_upd"

@router.get("/")
def get_products():
    try:
        data = prestashop_get("products", fieldsproducts)

        if not data:
            return ps_error("404", "No se encontraron productos")
        
        return ps_success(data)
    
    except Exception as e:
        return ps_error("500",str(e) )
    
    
@router.get("/{reference}")
def get_orders_ref(reference: str):
    try:
        data = prestashop_get("products", fieldsproducts, filters={"reference": reference})

        if not data:
            return ps_error("404", "No se encontró un producto con la referencia dada")
        
        return ps_success(data)
    
    except Exception as e:
        return ps_error("500",str(e) )
        