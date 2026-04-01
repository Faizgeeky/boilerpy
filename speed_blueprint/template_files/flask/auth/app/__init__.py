"""Flask application factory with authentication."""
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from app.core.config import get_settings
from app.api.v1 import api_v1_bp


def create_app() -> Flask:
    """Create and configure Flask application."""
    settings = get_settings()

    app = Flask(__name__)
    app.config.from_object(settings)

    # JWT Configuration
    app.config['JWT_SECRET_KEY'] = settings.SECRET_KEY
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60

    # Initialize extensions
    CORS(app, resources={r"/api/*": {"origins": settings.ALLOWED_ORIGINS}})
    JWTManager(app)

    # Register blueprints
    app.register_blueprint(api_v1_bp, url_prefix="/api/v1")

    @app.route("/")
    def root():
        return {
            "message": "{{project_name}} API with Authentication",
            "version": "1.0.0"
        }

    @app.route("/health")
    def health():
        return {"status": "healthy"}

    return app
