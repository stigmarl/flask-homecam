from flask import render_template, current_app, redirect, url_for, flash
from flask_login import login_required

from urllib.request import urlretrieve
from datetime import datetime
from time import strftime

from app.webcam import bp
from app.models import Image

@bp.route('/photo')
@login_required
def photo():
    img_url = current_app.config['IP_WEBCAM_PHOTO_URL']
    return render_template('webcam/photo.html', img_url=img_url)


@bp.route('/save_photo/')
@login_required
def save_photo():
    image = Image(post=True)
    flash('Image was saved as: ' + image.filename)
    return redirect(url_for('webcam.photo'))


@bp.route('/show_gallery/')
@login_required
def show_gallery():
    root_dir = current_app.config['GALLERY_ROOT_DIR']
    images = Image.all(root_dir)
    for image in images:
        print(image.filename)
    return render_template('webcam/gallery.html', images=images)


