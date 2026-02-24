from fastapi import APIRouter
from app.API.prestashop.products.routes import router as products_router

router = APIRouter()

router.include_router(
    products_router,
    prefix="/products",
    tags=["Products"]
)