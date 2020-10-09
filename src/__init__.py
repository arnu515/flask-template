from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.py"))
    db.init_app(app)
    Migrate(app, db)

    with app.app_context():
        from . import routes
        db.create_all()

        return app
