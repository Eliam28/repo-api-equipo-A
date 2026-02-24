import requests
from app.Core.config import settings

def get_prestashop_payments():
    url = f"{settings.PRESTASHOP_URL}/api/order_payments"

    response = requests.get(
        url,
        auth=(settings.PRESTASHOP_API_KEY, ""),
        headers={"Output-Format": "JSON"}
    )

    response.raise_for_status()
    return response.json()

        

        