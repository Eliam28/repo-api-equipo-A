from pydantic import BaseModel, EmailStr
from typing import Optional

class Address(BaseModel):
    first_name: Optional[str] = ""
    last_name: Optional[str] = ""
    address_1: Optional[str] = ""
    city: Optional[str] = ""
    state: Optional[str] = ""
    postcode: Optional[str] = ""
    country: Optional[str] = ""

class CustomerCreate(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    billing: Optional[Address] = None
    shipping: Optional[Address] = None