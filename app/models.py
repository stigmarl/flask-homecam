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


class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(64))
    file_path = db.Column(db.String(128), unique=True)

    def save_photo(self):
        img_url = current_app.config['IP_WEBCAM_PHOTO_URL']

        urlretrieve(img_url, filename=self.file_path)

    def delete_photo(self):
        os.remove(self.file_path)