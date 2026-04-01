"""Authentication endpoints."""
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.core.security import hash_password, verify_password, create_tokens

bp = Blueprint('auth', __name__)

# In-memory user storage (replace with database)
users_db = {}


@bp.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.get_json()

    if not data or 'email' not in data or 'password' not in data:
        return jsonify({"error": "Email and password required"}), 400

    email = data['email']
    if email in users_db:
        return jsonify({"error": "User already exists"}), 400

    # Create user
    users_db[email] = {
        "email": email,
        "password": hash_password(data['password']),
        "full_name": data.get('full_name', '')
    }

    tokens = create_tokens(email)

    return jsonify({
        "message": "User created successfully",
        "user": {"email": email, "full_name": users_db[email]['full_name']},
        **tokens
    }), 201


@bp.route('/login', methods=['POST'])
def login():
    """Login user."""
    data = request.get_json()

    if not data or 'email' not in data or 'password' not in data:
        return jsonify({"error": "Email and password required"}), 400

    email = data['email']
    user = users_db.get(email)

    if not user or not verify_password(data['password'], user['password']):
        return jsonify({"error": "Invalid credentials"}), 401

    tokens = create_tokens(email)

    return jsonify({
        "message": "Login successful",
        "user": {"email": email, "full_name": user['full_name']},
        **tokens
    }), 200


@bp.route('/me', methods=['GET'])
@jwt_required()
def get_current_user():
    """Get current user info."""
    current_user_email = get_jwt_identity()
    user = users_db.get(current_user_email)

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify({
        "email": current_user_email,
        "full_name": user.get('full_name', '')
    }), 200
