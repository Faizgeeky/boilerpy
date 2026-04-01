"""API v1 blueprint."""
from flask import Blueprint
from app.api.v1.endpoints import users

api_v1_bp = Blueprint('api_v1', __name__)

# Register endpoint blueprints
api_v1_bp.register_blueprint(users.bp, url_prefix='/users')
