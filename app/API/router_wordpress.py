from fastapi import APIRouter
from app.API.wordpress.products.routes import router as products_router

router = APIRouter()

router.include_router(
    products_router,
    prefix="/products",
    tags=["Products"]
)