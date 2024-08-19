from fastapi import APIRouter
from app import routes as app_routes


routes = APIRouter()


routes.include_router(
    app_routes.router,
    prefix="/app",
    tags=["app"]
)
