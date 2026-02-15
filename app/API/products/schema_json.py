from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    list_price: float
    default_code: str | None = None