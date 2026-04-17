from fastapi import APIRouter
from app.Core.odoo_client import models, uid
from app.Core.woocommerce_client import wcapi
from app.Core.config import settings

router = APIRouter()

@router.get("/create-order")
def create_orders():
    orders = models.execute_kw(
        settings.ODOO_DB,
        uid,
        settings.ODOO_PASSWORD,
        'sale.order',
        'search_read',
        [[]],
        {'fields': ['id', 'name']}
    )

    created = []

    for order in orders:

        lines = models.execute_kw(
            settings.ODOO_DB,
            uid,
            settings.ODOO_PASSWORD,
            'sale.order.line',
            'search_read',
            [[['order_id', '=', order['id']]]],
            {'fields': ['product_id', 'product_uom_qty']}
        )

        line_items = []

        for line in lines:
            product_id_odoo = line['product_id'][0]
            qty = int(line['product_uom_qty'])

            product_data = models.execute_kw(
                settings.ODOO_DB,
                uid,
                settings.ODOO_PASSWORD,
                'product.product',
                'read',
                [[product_id_odoo]],
                {'fields': ['default_code']}
            )

            if not product_data or not product_data[0].get('default_code'):
                print(f"Producto sin SKU en Odoo: {line['product_id'][1]}")
                continue

            sku = product_data[0]['default_code']

            response = wcapi.get("products", params={"sku": sku})

            if response.status_code != 200:
                print(f"Error Woo buscando SKU: {sku}")
                continue

            products = response.json()

            if not products:
                print(f"Producto NO existe en Woo: {sku}")
                continue

            product_id_wc = products[0]['id']

            line_items.append({
                "product_id": product_id_wc,
                "quantity": qty
            })

        if not line_items:
            print(f"Orden {order['name']} sin productos válidos")
            continue

        data = {
            "payment_method": "cod",
            "set_paid": True,
            "line_items": line_items
        }

        response = wcapi.post("orders", data)

        print(f"ORDER: {order['name']}")
        print(f"STATUS: {response.status_code}")
        print(f"RESPONSE: {response.json()}")

        if response.status_code == 201:
            created.append(order['name'])

    return {"created": created}