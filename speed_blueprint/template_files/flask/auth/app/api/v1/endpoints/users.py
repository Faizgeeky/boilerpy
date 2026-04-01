"""User management endpoints."""
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint('users', __name__)


@bp.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    """Get user profile."""
    current_user = get_jwt_identity()
    return jsonify({
        "email": current_user,
        "message": "This is a protected route"
    }), 200
