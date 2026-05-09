from pydantic import BaseModel, EmailStr
from typing import Optional

class Address(BaseModel):
    first_name: str
    last_name: str
    company: Optional[str] = ""
    address_1: str
    address_2: Optional[str] = ""
    city: str
    state: str
    postcode: str
    country: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = ""         

class CustomerCreate(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    username: Optional[str] = None
    billing: Address
    shipping: Address