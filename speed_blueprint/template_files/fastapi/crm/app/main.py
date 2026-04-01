"""Main application module."""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import api_router
from app.core.config import settings
from app.core.database import engine
from app.models import base  # noqa: F401 - Import to register models


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handle application lifespan events."""
    # Startup
    print("Application starting up...")
    yield
    # Shutdown
    print("Application shutting down...")
    engine.dispose()


app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Complete CRM API with users, customers, products, and orders",
    version="1.0.0",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan
)

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Welcome to {{project_name}} CRM API",
        "docs": "/docs",
        "version": "1.0.0",
        "features": [
            "User Authentication",
            "Customer Management",
            "Product Management",
            "Order Management"
        ]
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "application": settings.PROJECT_NAME
    }
