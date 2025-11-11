"""Run the Flask app and provide routing."""
from flask import Flask
from config import DB_FILE_PATH
from data_models import db, Author, Book

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{str(DB_FILE_PATH)}"

db.init_app(app)

with app.app_context():
    db.create_all()