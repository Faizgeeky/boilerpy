"""Database configuration and session management."""
from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base class for SQLAlchemy models."""
    pass


db = SQLAlchemy(model_class=Base)


def init_db(app: Flask) -> None:
    """Initialize database with Flask app."""
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config['DATABASE_URL']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = app.config['SQLALCHEMY_TRACK_MODIFICATIONS']
    app.config['SQLALCHEMY_ECHO'] = app.config['SQLALCHEMY_ECHO']
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = app.config['SQLALCHEMY_ENGINE_OPTIONS']

    db.init_app(app)

    with app.app_context():
        # Import all models here to ensure they are registered
        from app.models import user  # noqa: F401
        db.create_all()


def get_db():
    """Get database session for current request context."""
    if 'db' not in g:
        g.db = db.session
    return g.db
