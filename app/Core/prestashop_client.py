import requests
from app.Core.config import settings

def prestashop_get(endpoint: str):
  url = f"{settings.PRESTASHOP_URL}/{endpoint}"
  response = requests.get(url, auth=(settings.API_KEY,''))
  response.raise_for_status()
  return response.json