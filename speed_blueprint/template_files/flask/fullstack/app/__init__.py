"""Flask application factory with fullstack support."""
from flask import Flask
from flask_login import LoginManager
from app.core.config import get_settings
from app.routes import main, auth

# Initialize Flask-Login
login_manager = LoginManager()


def create_app() -> Flask:
    """Create and configure Flask application."""
    settings = get_settings()

    app = Flask(__name__)
    app.config.from_object(settings)

    # Configure Flask-Login
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access this page.'
    login_manager.login_message_category = 'info'

    # Import user loader
    from app.models.user import load_user
    login_manager.user_loader(load_user)

    # Register blueprints
    app.register_blueprint(main.bp)
    app.register_blueprint(auth.bp)

    # Error handlers
    @app.errorhandler(404)
    def not_found_error(error):
        from flask import render_template
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        from flask import render_template
        return render_template('errors/500.html'), 500

    return app
