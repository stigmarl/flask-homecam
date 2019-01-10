from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

from config import Config


app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app)
db = SQLAlchemy()
migrate = Migrate(app, db)
login = LoginManager(app)

from app import routes
