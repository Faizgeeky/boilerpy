"""Items endpoint."""
from flask import Blueprint, request, jsonify
from typing import List, Dict

bp = Blueprint('items', __name__)

# In-memory storage (replace with database in production)
items_db: List[Dict] = [
    {"id": 1, "name": "Item 1", "description": "First item"},
    {"id": 2, "name": "Item 2", "description": "Second item"}
]


@bp.route('/', methods=['GET'])
def list_items():
    """Get all items."""
    return jsonify(items_db), 200


@bp.route('/<int:item_id>', methods=['GET'])
def get_item(item_id: int):
    """Get item by ID."""
    item = next((item for item in items_db if item['id'] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item), 200


@bp.route('/', methods=['POST'])
def create_item():
    """Create new item."""
    data = request.get_json()

    if not data or 'name' not in data:
        return jsonify({"error": "Name is required"}), 400

    new_item = {
        "id": max([item['id'] for item in items_db], default=0) + 1,
        "name": data['name'],
        "description": data.get('description', '')
    }

    items_db.append(new_item)
    return jsonify(new_item), 201


@bp.route('/<int:item_id>', methods=['PUT'])
def update_item(item_id: int):
    """Update item."""
    item = next((item for item in items_db if item['id'] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    data = request.get_json()
    item['name'] = data.get('name', item['name'])
    item['description'] = data.get('description', item['description'])

    return jsonify(item), 200


@bp.route('/<int:item_id>', methods=['DELETE'])
def delete_item(item_id: int):
    """Delete item."""
    global items_db
    item = next((item for item in items_db if item['id'] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    items_db = [item for item in items_db if item['id'] != item_id]
    return jsonify({"message": "Item deleted"}), 200
