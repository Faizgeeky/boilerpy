"""Main application module."""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import api_router
from app.core.config import settings
from app.core.database import mongodb


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handle application lifespan events."""
    # Startup: Connect to MongoDB
    await mongodb.connect_to_database()
    yield
    # Shutdown: Close MongoDB connection
    await mongodb.close_database_connection()


app = FastAPI(
    title=settings.PROJECT_NAME,
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
        "message": "Welcome to {{project_name}} API",
        "docs": "/docs",
        "version": "1.0.0",
        "database": "MongoDB"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    db_status = "connected" if mongodb.client is not None else "disconnected"
    return {
        "status": "healthy",
        "database": db_status
    }
