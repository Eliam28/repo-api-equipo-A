from fastapi import APIRouter
from app.API.providers_o.routes import router as providers_router
from app.API.stock.routes import router as stock_router


router = APIRouter()

router.include_router(
    providers_router,
    prefix="/providers",
    tags=["Providers"]
)

router.include_router(
    stock_router,
    prefix="/stock",
    tags=["Stock"]
)


