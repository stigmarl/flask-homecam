from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

from config import Config


app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app)
db = SQLAlchemy()
migrate = Migrate(app, db)

from app import routes
