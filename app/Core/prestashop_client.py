import requests
from app.Core.config import settings

def prestashop_get(endpoint: str, fields: str|None = None):

  url = f"{settings.PRESTASHOP_URL}/{endpoint}"

  params = {
      "ws_key": settings.API_KEY,
      "output_format": "JSON"
  }

  if fields:
    params["display"] = f"[{fields}]"
  else:
    params["display"] = "full"
    
  response = requests.get(url, params=params)

  response.raise_for_status()

  return response.json()