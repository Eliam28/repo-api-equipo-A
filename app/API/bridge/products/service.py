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

