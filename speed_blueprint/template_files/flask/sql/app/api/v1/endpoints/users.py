"""User CRUD endpoints."""
from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from app.crud import user as crud_user
from app.schemas.user import UserCreate, UserUpdate

bp = Blueprint('users', __name__)


@bp.route('/', methods=['GET'])
def list_users():
    """List all users with pagination."""
    skip = request.args.get('skip', 0, type=int)
    limit = request.args.get('limit', 100, type=int)

    # Validate pagination parameters
    if skip < 0:
        return jsonify({"error": "Skip must be non-negative"}), 400
    if limit < 1 or limit > 100:
        return jsonify({"error": "Limit must be between 1 and 100"}), 400

    users = crud_user.get_users(skip=skip, limit=limit)

    return jsonify({
        "users": [user.to_dict() for user in users],
        "skip": skip,
        "limit": limit,
        "total": len(users)
    }), 200


@bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id: int):
    """Get a specific user by ID."""
    user = crud_user.get_user(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user.to_dict()), 200


@bp.route('/', methods=['POST'])
def create_user():
    """Create a new user."""
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    # Create and validate schema
    try:
        user_data = UserCreate(
            email=data.get('email'),
            username=data.get('username'),
            password=data.get('password'),
            full_name=data.get('full_name')
        )
    except TypeError as e:
        return jsonify({"error": f"Invalid data format: {str(e)}"}), 400

    # Validate
    is_valid, error_msg = user_data.validate()
    if not is_valid:
        return jsonify({"error": error_msg}), 400

    # Check if user already exists
    if crud_user.get_user_by_email(user_data.email):
        return jsonify({"error": "Email already registered"}), 400

    if crud_user.get_user_by_username(user_data.username):
        return jsonify({"error": "Username already taken"}), 400

    # Create user
    try:
        user = crud_user.create_user(user_data)
        return jsonify(user.to_dict()), 201
    except IntegrityError:
        return jsonify({"error": "User with this email or username already exists"}), 400
    except Exception as e:
        return jsonify({"error": f"Failed to create user: {str(e)}"}), 500


@bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id: int):
    """Update a user."""
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    # Create and validate schema
    try:
        user_data = UserUpdate(
            email=data.get('email'),
            username=data.get('username'),
            full_name=data.get('full_name'),
            password=data.get('password'),
            is_active=data.get('is_active')
        )
    except TypeError as e:
        return jsonify({"error": f"Invalid data format: {str(e)}"}), 400

    # Validate
    is_valid, error_msg = user_data.validate()
    if not is_valid:
        return jsonify({"error": error_msg}), 400

    # Check if email/username is already taken by another user
    if user_data.email:
        existing_user = crud_user.get_user_by_email(user_data.email)
        if existing_user and existing_user.id != user_id:
            return jsonify({"error": "Email already in use"}), 400

    if user_data.username:
        existing_user = crud_user.get_user_by_username(user_data.username)
        if existing_user and existing_user.id != user_id:
            return jsonify({"error": "Username already taken"}), 400

    # Update user
    try:
        user = crud_user.update_user(user_id, user_data)

        if not user:
            return jsonify({"error": "User not found"}), 404

        return jsonify(user.to_dict()), 200
    except IntegrityError:
        return jsonify({"error": "Email or username already in use"}), 400
    except Exception as e:
        return jsonify({"error": f"Failed to update user: {str(e)}"}), 500


@bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id: int):
    """Delete a user."""
    success = crud_user.delete_user(user_id)

    if not success:
        return jsonify({"error": "User not found"}), 404

    return jsonify({"message": "User deleted successfully"}), 200


@bp.route('/authenticate', methods=['POST'])
def authenticate():
    """Authenticate a user."""
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    user = crud_user.authenticate_user(username, password)

    if not user:
        return jsonify({"error": "Invalid credentials"}), 401

    if not user.is_active:
        return jsonify({"error": "User account is inactive"}), 403

    return jsonify({
        "message": "Authentication successful",
        "user": user.to_dict()
    }), 200
