from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize database and migration
    db.init_app(app)
    migrate.init_app(app, db)

    # Register routes from urls.py
    from .urls import register_routes
    register_routes(app)

    return app
