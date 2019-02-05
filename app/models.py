import os
from urllib.request import urlretrieve
from time import strftime
from datetime import datetime

from app import db, login

from flask import current_app, flash
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Image(object):
    def __init__(self, filename=None, post=False):
        self.root = current_app.config['GALLERY_ROOT_DIR']

        self.filename = filename

        if filename is None:
            self.filename = datetime.now().strftime("%Y%m%d-%H.%M.%S") + ".jpg"

        if post:
            print('Uploading image')
            self.upload(self.filename)

    def upload(self, filename):
        img_url = current_app.config['IP_WEBCAM_PHOTO_URL']
        file_url = os.path.join(self.root, filename)
        try:
            urlretrieve(img_url, filename=file_url)
            flash('Image was saved as: ' + filename, 'success')
        except OSError as err:
            print(err)
            flash('Could not save image!', 'danger')

    @classmethod
    def all(cls, root):
        """Return a list of all files contained in directory root"""
        return [cls(x) for x in os.listdir(root)]