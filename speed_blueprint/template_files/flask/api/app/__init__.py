"""Flask application factory."""
from flask import Flask
from flask_cors import CORS
from app.core.config import get_settings
from app.api.v1 import api_v1_bp


def create_app() -> Flask:
    """Create and configure Flask application."""
    settings = get_settings()

    app = Flask(__name__)
    app.config.from_object(settings)

    # Configure CORS
    CORS(app, resources={
        r"/api/*": {
            "origins": settings.ALLOWED_ORIGINS,
            "methods": ["GET", "POST", "PUT", "DELETE", "PATCH"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    })

    # Register blueprints
    app.register_blueprint(api_v1_bp, url_prefix="/api/v1")

    # Root route
    @app.route("/")
    def root():
        return {
            "message": "Welcome to {{project_name}} API",
            "version": "1.0.0",
            "docs": "/api/v1/docs"
        }

    # Health check
    @app.route("/health")
    def health():
        return {"status": "healthy"}

    return app
