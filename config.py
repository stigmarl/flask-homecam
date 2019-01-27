import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this is a secret key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    IP_WEBCAM_PHOTO_URL = "http://192.168.1.192:8080/photo.jpg"
    GALLERY_ROOT_DIR = os.path.join(basedir,'app', 'static', 'images')
