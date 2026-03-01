from pydantic import BaseModel
from typing import Optional


class ProductUpdate(BaseModel):
    price: Optional[float] = None
    active: Optional[int] = None
    wholesale_price: Optional[float] = None