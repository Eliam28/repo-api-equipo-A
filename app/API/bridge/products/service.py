from app.Core.odoo_client import models, uid
from app.Core.config import settings
from app.Core.prestashop_client import prestashop_get, prestashop_post
from app.API.bridge.products.mapper import odoo_to_prestashop

def sync_products():
  odoo_products = models.execute_kw(
    settings.ODOO_DB,
    uid,
    settings.ODOO_PASSWORD,
    'product.template',
    'search_read',
    [[]],
    {'fields':['id','name','list_price','default_code']}
  )

  for p in odoo_products:
    if p.get("default_code") is False:
      p["default_code"] = None

  prestashop_data = prestashop_get("products",fields="id,reference")

  existing_refs = set()

  if "products" in prestashop_data:
    for prod in prestashop_data["products"]:
      if prod.get("reference"):
        existing_refs.add(prod["reference"])

  creados = 0
  saltados = 0

  for product in odoo_products:
    ref = product.get("default_code")

    if not ref:
      saltados += 1
      continue

    if ref in existing_refs:
      saltados += 1
      continue

    xml = odoo_to_prestashop(product)

    prestashop_post("products", xml)

    creados +=1
  
  return {
    "Creados": creados,
    "Saltados": saltados
  }

def create_one_product_by_reference(reference: str):

  # Buscar en Odoo por default_code
  rows = models.execute_kw(
    settings.ODOO_DB,
    uid,
    settings.ODOO_PASSWORD,
    'product.product',
    'search_read',
    [[['default_code', '=', reference]]],
    {'fields':['id','name','list_price','default_code','qty_available']}
  )

  if not rows:
    raise Exception("Producto no encontrado en Odoo con esa referencia")

  product = rows[0]

  if product.get("default_code") is False:
    product["default_code"] = None

  ref = product.get("default_code")
  if not ref:
    raise Exception("El producto no tiene referencia (default_code)")

  price = float(product.get("list_price") or 0)
  stock = float(product.get("qty_available") or 0)

  # No crear si precio 0 y stock 0
  if price == 0 and stock == 0:
    return {
      "created": False,
      "skipped": True,
      "message": "No se crea: precio 0 y stock 0",
      "reference": ref,
      "price": price,
      "stock": stock
    }

  # No duplicar en PrestaShop
  ps = prestashop_get("products", fields="id,reference", filters={"reference": ref})

  if "products" in ps and ps["products"]:
    return {
      "created": False,
      "message": "Ya existe en PrestaShop",
      "reference": ref
    }

  xml = odoo_to_prestashop(product)
  prestashop_post("products", xml)

  return {
    "created": True,
    "message": "Producto creado en PrestaShop",
    "reference": ref,
    "price": price,
    "stock": stock
  }