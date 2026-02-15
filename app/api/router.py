from fastapi import APIRouter
from app.API.providers_o.routes import router as providers_router
from app.API.products.routes import router as products_router

router = APIRouter()

router.include_router(
    providers_router,
    prefix="/providers",
    tags=["Providers"]
)
router.include_router(
    products_router,
    prefix="/products",
    tags=["Products"]
)