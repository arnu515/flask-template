import os

# Flask config goes here

SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL", "sqlite:///db.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False
