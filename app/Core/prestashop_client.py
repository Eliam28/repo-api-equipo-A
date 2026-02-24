import requests
from app.Core.config import settings

def prestashop_get(endpoint: str):

  url = f"{settings.PRESTASHOP_URL}/{endpoint}"

  params = {
      "ws_key": settings.API_KEY,
      "output_format": "JSON",
      "display": "full"
  }
  
  response = requests.get(url, params=params)

  response.raise_for_status()

  return response.json()