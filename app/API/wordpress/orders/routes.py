from fastapi import APIRouter, HTTPException
from app.Core.woocommerce_client import wcapi

router = APIRouter()

@router.get("/")
def get_orders(per_page: int = 10):
    try:
        response = wcapi.get("orders", params={"per_page": per_page})

        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail=response.text
            )

        orders = response.json()

        clean_orders = []

        for order in orders:
            clean_orders.append({
                "id": order["id"],
                "status": order["status"],
                "total": order["total"],
                "currency": order["currency"],
                "date_created": order["date_created"],
                "customer_id": order["customer_id"],
                "created_via": order["created_via"],
                "products": [
                    {
                        "name": item["name"],
                        "quantity": item["quantity"],
                        "price": item["price"]
                    }
                    for item in order["line_items"]
                ]
            })

        return clean_orders

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))