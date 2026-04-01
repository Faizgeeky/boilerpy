"""MongoDB configuration and connection management."""
from flask import Flask
from flask_pymongo import PyMongo
from pymongo.errors import ConnectionFailure

mongo = PyMongo()


def init_db(app: Flask) -> None:
    """Initialize MongoDB with Flask app."""
    app.config['MONGO_URI'] = app.config['MONGO_URI']

    mongo.init_app(app)

    # Test connection
    try:
        mongo.db.command('ping')
        print("MongoDB connection successful!")
    except ConnectionFailure as e:
        print(f"MongoDB connection failed: {e}")


def get_db():
    """Get MongoDB database instance."""
    return mongo.db
