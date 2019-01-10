from flask import Blueprint

bp = Blueprint('webcam', __name__)

from app.webcam import routes