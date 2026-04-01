"""User model for authentication."""
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from typing import Optional, Dict


# In-memory user storage (replace with database in production)
users_db: Dict[int, 'User'] = {}
username_index: Dict[str, int] = {}
email_index: Dict[str, int] = {}
next_user_id = 1


class User(UserMixin):
    """User model for Flask-Login."""

    def __init__(
        self,
        user_id: int,
        username: str,
        email: str,
        password_hash: str,
        full_name: Optional[str] = None,
    ):
        """Initialize user instance."""
        self.id = user_id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.full_name = full_name

    @staticmethod
    def create_user(username: str, email: str, password: str, full_name: Optional[str] = None) -> 'User':
        """Create a new user."""
        global next_user_id

        if username in username_index:
            raise ValueError("Username already exists")

        if email in email_index:
            raise ValueError("Email already exists")

        user_id = next_user_id
        next_user_id += 1

        password_hash = generate_password_hash(password, method='pbkdf2:sha256')
        user = User(user_id, username, email, password_hash, full_name)

        users_db[user_id] = user
        username_index[username] = user_id
        email_index[email] = user_id

        return user

    @staticmethod
    def get_by_id(user_id: int) -> Optional['User']:
        """Get user by ID."""
        return users_db.get(user_id)

    @staticmethod
    def get_by_username(username: str) -> Optional['User']:
        """Get user by username."""
        user_id = username_index.get(username)
        return users_db.get(user_id) if user_id else None

    @staticmethod
    def get_by_email(email: str) -> Optional['User']:
        """Get user by email."""
        user_id = email_index.get(email)
        return users_db.get(user_id) if user_id else None

    def check_password(self, password: str) -> bool:
        """Check if password matches."""
        return check_password_hash(self.password_hash, password)

    def to_dict(self) -> dict:
        """Convert user to dictionary."""
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "full_name": self.full_name,
        }


def load_user(user_id: int):
    """Load user for Flask-Login."""
    return User.get_by_id(int(user_id))
