"""Item CRUD endpoints with MongoDB."""
from flask import Blueprint, request, jsonify
from bson import ObjectId
from bson.errors import InvalidId
from datetime import datetime
from app.core.database import get_db
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate

bp = Blueprint('items', __name__)


@bp.route('/', methods=['GET'])
def list_items():
    """List all items with pagination and filtering."""
    db = get_db()

    # Pagination
    skip = request.args.get('skip', 0, type=int)
    limit = request.args.get('limit', 100, type=int)

    # Validate pagination parameters
    if skip < 0:
        return jsonify({"error": "Skip must be non-negative"}), 400
    if limit < 1 or limit > 100:
        return jsonify({"error": "Limit must be between 1 and 100"}), 400

    # Filtering
    query = {}
    if category := request.args.get('category'):
        query['category'] = category

    if min_price := request.args.get('min_price', type=float):
        query.setdefault('price', {})['$gte'] = min_price

    if max_price := request.args.get('max_price', type=float):
        query.setdefault('price', {})['$lte'] = max_price

    # Search by title
    if search := request.args.get('search'):
        query['title'] = {'$regex': search, '$options': 'i'}

    try:
        # Query items
        cursor = db.items.find(query).skip(skip).limit(limit).sort('created_at', -1)
        items = [Item.from_mongo(doc).to_dict() for doc in cursor]

        # Get total count
        total = db.items.count_documents(query)

        return jsonify({
            "items": items,
            "skip": skip,
            "limit": limit,
            "total": total
        }), 200
    except Exception as e:
        return jsonify({"error": f"Failed to fetch items: {str(e)}"}), 500


@bp.route('/<item_id>', methods=['GET'])
def get_item(item_id: str):
    """Get a specific item by ID."""
    db = get_db()

    try:
        object_id = ObjectId(item_id)
    except InvalidId:
        return jsonify({"error": "Invalid item ID format"}), 400

    try:
        doc = db.items.find_one({"_id": object_id})

        if not doc:
            return jsonify({"error": "Item not found"}), 404

        item = Item.from_mongo(doc)
        return jsonify(item.to_dict()), 200
    except Exception as e:
        return jsonify({"error": f"Failed to fetch item: {str(e)}"}), 500


@bp.route('/', methods=['POST'])
def create_item():
    """Create a new item."""
    db = get_db()
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    # Create and validate schema
    try:
        item_data = ItemCreate(
            title=data.get('title'),
            description=data.get('description'),
            price=data.get('price', 0.0),
            quantity=data.get('quantity', 0),
            category=data.get('category')
        )
    except (TypeError, ValueError) as e:
        return jsonify({"error": f"Invalid data format: {str(e)}"}), 400

    # Validate
    is_valid, error_msg = item_data.validate()
    if not is_valid:
        return jsonify({"error": error_msg}), 400

    # Create item
    try:
        item = Item(
            title=item_data.title,
            description=item_data.description,
            price=item_data.price,
            quantity=item_data.quantity,
            category=item_data.category
        )

        result = db.items.insert_one(item.to_mongo())
        item._id = result.inserted_id

        return jsonify(item.to_dict()), 201
    except Exception as e:
        return jsonify({"error": f"Failed to create item: {str(e)}"}), 500


@bp.route('/<item_id>', methods=['PUT'])
def update_item(item_id: str):
    """Update an item."""
    db = get_db()

    try:
        object_id = ObjectId(item_id)
    except InvalidId:
        return jsonify({"error": "Invalid item ID format"}), 400

    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    # Create and validate schema
    try:
        item_data = ItemUpdate(
            title=data.get('title'),
            description=data.get('description'),
            price=data.get('price'),
            quantity=data.get('quantity'),
            category=data.get('category')
        )
    except (TypeError, ValueError) as e:
        return jsonify({"error": f"Invalid data format: {str(e)}"}), 400

    # Validate
    is_valid, error_msg = item_data.validate()
    if not is_valid:
        return jsonify({"error": error_msg}), 400

    # Build update document
    update_doc = {"updated_at": datetime.utcnow()}

    if item_data.title is not None:
        update_doc["title"] = item_data.title
    if item_data.description is not None:
        update_doc["description"] = item_data.description
    if item_data.price is not None:
        update_doc["price"] = item_data.price
    if item_data.quantity is not None:
        update_doc["quantity"] = item_data.quantity
    if item_data.category is not None:
        update_doc["category"] = item_data.category

    try:
        result = db.items.update_one(
            {"_id": object_id},
            {"$set": update_doc}
        )

        if result.matched_count == 0:
            return jsonify({"error": "Item not found"}), 404

        # Fetch and return updated item
        doc = db.items.find_one({"_id": object_id})
        item = Item.from_mongo(doc)

        return jsonify(item.to_dict()), 200
    except Exception as e:
        return jsonify({"error": f"Failed to update item: {str(e)}"}), 500


@bp.route('/<item_id>', methods=['DELETE'])
def delete_item(item_id: str):
    """Delete an item."""
    db = get_db()

    try:
        object_id = ObjectId(item_id)
    except InvalidId:
        return jsonify({"error": "Invalid item ID format"}), 400

    try:
        result = db.items.delete_one({"_id": object_id})

        if result.deleted_count == 0:
            return jsonify({"error": "Item not found"}), 404

        return jsonify({"message": "Item deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to delete item: {str(e)}"}), 500


@bp.route('/bulk', methods=['POST'])
def create_bulk_items():
    """Create multiple items at once."""
    db = get_db()
    data = request.get_json()

    if not data or not isinstance(data, list):
        return jsonify({"error": "Expected a list of items"}), 400

    if len(data) > 100:
        return jsonify({"error": "Cannot create more than 100 items at once"}), 400

    # Validate all items
    items = []
    for idx, item_dict in enumerate(data):
        try:
            item_data = ItemCreate(
                title=item_dict.get('title'),
                description=item_dict.get('description'),
                price=item_dict.get('price', 0.0),
                quantity=item_dict.get('quantity', 0),
                category=item_dict.get('category')
            )
        except (TypeError, ValueError) as e:
            return jsonify({"error": f"Invalid data at index {idx}: {str(e)}"}), 400

        is_valid, error_msg = item_data.validate()
        if not is_valid:
            return jsonify({"error": f"Validation error at index {idx}: {error_msg}"}), 400

        item = Item(
            title=item_data.title,
            description=item_data.description,
            price=item_data.price,
            quantity=item_data.quantity,
            category=item_data.category
        )
        items.append(item.to_mongo())

    try:
        result = db.items.insert_many(items)

        return jsonify({
            "message": f"Successfully created {len(result.inserted_ids)} items",
            "count": len(result.inserted_ids)
        }), 201
    except Exception as e:
        return jsonify({"error": f"Failed to create items: {str(e)}"}), 500
