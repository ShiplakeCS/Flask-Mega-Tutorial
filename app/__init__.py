from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)  # Use the Config class within config.py to provide the app's config settings
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models

