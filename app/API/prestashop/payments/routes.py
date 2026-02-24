from fastapi import APIRouter
from typing import List
from app.API.prestashop.payments.schema_json import Payment
from app.Core.prestashop_client import prestashop_get

router = APIRouter()

@router.get("/", response_model=List[Payment])
def get_payments():

    data = prestashop_get(
        "api/order_payments",
        fields="id,order_reference,amount,payment_method,transaction_id,date_add"
    )

    payments = data["order_payments"]

    return [
        Payment(
            id=int(p["id"]),
            order_reference=p.get("order_reference"),
            amount=float(p.get("amount", 0)),
            payment_method=p.get("payment_method"),
            transaction_id=p.get("transaction_id"),
            date_add=p.get("date_add"),
        )
        for p in payments
    ]