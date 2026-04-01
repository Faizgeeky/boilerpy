"""Flask application factory with MongoDB."""
from flask import Flask
from flask_cors import CORS
from app.core.config import get_settings
from app.core.database import init_db, mongo
from app.api.v1 import api_v1_bp


def create_app() -> Flask:
    """Create and configure Flask application."""
    settings = get_settings()

    app = Flask(__name__)
    app.config.from_object(settings)

    # Initialize extensions
    CORS(app, resources={r"/api/*": {"origins": settings.ALLOWED_ORIGINS}})

    # Initialize database
    init_db(app)

    # Register blueprints
    app.register_blueprint(api_v1_bp, url_prefix="/api/v1")

    @app.route("/")
    def root():
        return {
            "message": "{{project_name}} API with MongoDB",
            "version": "1.0.0"
        }

    @app.route("/health")
    def health():
        # Check MongoDB connection
        try:
            mongo.db.command('ping')
            db_status = "connected"
        except Exception:
            db_status = "disconnected"

        return {
            "status": "healthy",
            "database": db_status
        }

    return app
