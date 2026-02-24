from pydantic import BaseModel
from typing import Optional

class Payment(BaseModel):
    id: int
    order_reference: Optional[str]
    amount: float
    payment_method: Optional[str]
    transaction_id: Optional[str]
    date_add: Optional[str]