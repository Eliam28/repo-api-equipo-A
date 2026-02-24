from fastapi import APIRouter
from app.API.prestashop.products.routes import router as products_router
from app.API.prestashop.orders.routes import router as orders_router

router = APIRouter()

router.include_router(
    products_router,
    prefix="/products",
    tags=["Products"]
)

router.include_router(
    orders_router,
    prefix="/orders",
    tags=["orders"]
)