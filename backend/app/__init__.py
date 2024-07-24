# app/__init__.py
from flask import Flask
from flask_cors import CORS
import logging

def create_app():
    app = Flask(__name__)
    # Enable CORS for your frontend
    CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})
    logging.basicConfig(level=logging.DEBUG)

    # Register blueprints
    from .routes import routes_bp
    from .auth import auth_bp
    app.register_blueprint(routes_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app