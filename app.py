"""Run the Flask app and provide routing."""
from flask import Flask
from config import DB_FILE_PATH

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{str(DB_FILE_PATH)}"
