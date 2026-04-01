"""User CRUD operations."""
from typing import Optional, List
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import select
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.database import db


def get_password_hash(password: str) -> str:
    """Hash a password."""
    return generate_password_hash(password, method='pbkdf2:sha256')


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against its hash."""
    return check_password_hash(hashed_password, plain_password)


def get_user(user_id: int) -> Optional[User]:
    """Get a user by ID."""
    return db.session.get(User, user_id)


def get_user_by_email(email: str) -> Optional[User]:
    """Get a user by email."""
    stmt = select(User).where(User.email == email)
    return db.session.execute(stmt).scalar_one_or_none()


def get_user_by_username(username: str) -> Optional[User]:
    """Get a user by username."""
    stmt = select(User).where(User.username == username)
    return db.session.execute(stmt).scalar_one_or_none()


def get_users(skip: int = 0, limit: int = 100) -> List[User]:
    """Get list of users with pagination."""
    stmt = select(User).offset(skip).limit(limit)
    return list(db.session.execute(stmt).scalars())


def create_user(user_data: UserCreate) -> User:
    """Create a new user."""
    hashed_password = get_password_hash(user_data.password)

    db_user = User(
        email=user_data.email,
        username=user_data.username,
        full_name=user_data.full_name,
        hashed_password=hashed_password,
    )

    db.session.add(db_user)
    db.session.commit()
    db.session.refresh(db_user)

    return db_user


def update_user(user_id: int, user_data: UserUpdate) -> Optional[User]:
    """Update a user."""
    db_user = get_user(user_id)

    if not db_user:
        return None

    update_data = {}

    if user_data.email is not None:
        update_data["email"] = user_data.email
    if user_data.username is not None:
        update_data["username"] = user_data.username
    if user_data.full_name is not None:
        update_data["full_name"] = user_data.full_name
    if user_data.password is not None:
        update_data["hashed_password"] = get_password_hash(user_data.password)
    if user_data.is_active is not None:
        update_data["is_active"] = user_data.is_active

    for key, value in update_data.items():
        setattr(db_user, key, value)

    db.session.commit()
    db.session.refresh(db_user)

    return db_user


def delete_user(user_id: int) -> bool:
    """Delete a user."""
    db_user = get_user(user_id)

    if not db_user:
        return False

    db.session.delete(db_user)
    db.session.commit()

    return True


def authenticate_user(username: str, password: str) -> Optional[User]:
    """Authenticate a user."""
    user = get_user_by_username(username)

    if not user:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    return user
