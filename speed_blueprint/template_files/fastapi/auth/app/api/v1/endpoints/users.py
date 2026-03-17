"""User endpoints."""
from fastapi import APIRouter, Depends

from app.core.dependencies import get_current_user
from app.schemas.user import User

router = APIRouter()


@router.get("/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    """Get current user information."""
    return current_user
