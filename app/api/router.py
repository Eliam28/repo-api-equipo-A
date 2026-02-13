from fastapi import APIRouter
from app.api.providers_o.routes import router as providers_router

router = APIRouter()

router.include_router(
    providers_router,
    prefix="/providers",
    tags=["Providers"]
)