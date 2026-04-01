"""Items endpoints."""
from typing import List, Optional
from fastapi import APIRouter, HTTPException, Query, status

from app.crud import item as item_crud
from app.schemas.item import ItemCreate, ItemUpdate, ItemResponse

router = APIRouter()


@router.post("/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemCreate):
    """Create a new item."""
    created_item = await item_crud.create_item(item)
    return created_item


@router.get("/", response_model=List[ItemResponse])
async def read_items(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    is_active: Optional[bool] = Query(None)
):
    """Get all items with pagination."""
    items = await item_crud.get_items(skip=skip, limit=limit, is_active=is_active)
    return items


@router.get("/count")
async def count_items(is_active: Optional[bool] = Query(None)):
    """Count items."""
    count = await item_crud.count_items(is_active=is_active)
    return {"count": count}


@router.get("/{item_id}", response_model=ItemResponse)
async def read_item(item_id: str):
    """Get an item by ID."""
    item = await item_crud.get_item(item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )
    return item


@router.put("/{item_id}", response_model=ItemResponse)
async def update_item(item_id: str, item_update: ItemUpdate):
    """Update an item."""
    updated_item = await item_crud.update_item(item_id, item_update)
    if not updated_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )
    return updated_item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: str):
    """Delete an item."""
    deleted = await item_crud.delete_item(item_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )
    return None
