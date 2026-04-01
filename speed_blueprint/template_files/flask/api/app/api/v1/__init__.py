"""API v1 Blueprint."""
from flask import Blueprint
from app.api.v1.endpoints import items

api_v1_bp = Blueprint('api_v1', __name__)

# Register endpoint blueprints
api_v1_bp.register_blueprint(items.bp, url_prefix='/items')


@api_v1_bp.route('/docs')
def docs():
    """API documentation endpoint."""
    return {
        "message": "API Documentation",
        "version": "1.0.0",
        "endpoints": {
            "items": "/api/v1/items - Manage items",
            "health": "/health - Health check"
        }
    }
