"""CRUD operations for items."""
from datetime import datetime
from typing import List, Optional
from bson import ObjectId

from app.core.database import mongodb
from app.core.config import settings
from app.schemas.item import ItemCreate, ItemUpdate


async def create_item(item: ItemCreate) -> dict:
    """Create a new item."""
    collection = mongodb.get_collection(settings.ITEMS_COLLECTION)
    item_dict = item.model_dump()
    item_dict["created_at"] = datetime.utcnow()
    item_dict["updated_at"] = datetime.utcnow()

    result = await collection.insert_one(item_dict)
    created_item = await collection.find_one({"_id": result.inserted_id})
    created_item["_id"] = str(created_item["_id"])
    return created_item


async def get_item(item_id: str) -> Optional[dict]:
    """Get an item by ID."""
    collection = mongodb.get_collection(settings.ITEMS_COLLECTION)
    if not ObjectId.is_valid(item_id):
        return None

    item = await collection.find_one({"_id": ObjectId(item_id)})
    if item:
        item["_id"] = str(item["_id"])
    return item


async def get_items(skip: int = 0, limit: int = 100, is_active: Optional[bool] = None) -> List[dict]:
    """Get all items with pagination."""
    collection = mongodb.get_collection(settings.ITEMS_COLLECTION)

    query = {}
    if is_active is not None:
        query["is_active"] = is_active

    cursor = collection.find(query).skip(skip).limit(limit)
    items = await cursor.to_list(length=limit)

    for item in items:
        item["_id"] = str(item["_id"])

    return items


async def update_item(item_id: str, item_update: ItemUpdate) -> Optional[dict]:
    """Update an item."""
    collection = mongodb.get_collection(settings.ITEMS_COLLECTION)
    if not ObjectId.is_valid(item_id):
        return None

    # Only update fields that are provided
    update_data = {k: v for k, v in item_update.model_dump(exclude_unset=True).items()}
    if not update_data:
        return await get_item(item_id)

    update_data["updated_at"] = datetime.utcnow()

    result = await collection.update_one(
        {"_id": ObjectId(item_id)},
        {"$set": update_data}
    )

    if result.modified_count == 0:
        return None

    return await get_item(item_id)


async def delete_item(item_id: str) -> bool:
    """Delete an item."""
    collection = mongodb.get_collection(settings.ITEMS_COLLECTION)
    if not ObjectId.is_valid(item_id):
        return False

    result = await collection.delete_one({"_id": ObjectId(item_id)})
    return result.deleted_count > 0


async def count_items(is_active: Optional[bool] = None) -> int:
    """Count items."""
    collection = mongodb.get_collection(settings.ITEMS_COLLECTION)

    query = {}
    if is_active is not None:
        query["is_active"] = is_active

    return await collection.count_documents(query)
