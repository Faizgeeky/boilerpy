"""API v1 Blueprint with auth endpoints."""
from flask import Blueprint
from app.api.v1.endpoints import auth, users

api_v1_bp = Blueprint('api_v1', __name__)

# Register endpoints
api_v1_bp.register_blueprint(auth.bp, url_prefix='/auth')
api_v1_bp.register_blueprint(users.bp, url_prefix='/users')
