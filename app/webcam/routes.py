from flask import render_template, current_app, redirect, url_for, flash
from flask_login import login_required

from urllib.request import urlretrieve
from datetime import datetime
from time import strftime

from app.webcam import bp


@bp.route('/photo')
@login_required
def photo():
    img_url = current_app.config['IP_WEBCAM_PHOTO_URL']
    return render_template('webcam/photo.html', img_url=img_url)


@bp.route('/save_photo/')
@login_required
def save_photo():
    img_url = current_app.config['IP_WEBCAM_PHOTO_URL']
    img_dir = current_app.config['WEBCAM_IMAGE_DIR']
    img_file_name = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ".jpg"
    urlretrieve(img_url, img_dir + "/" + img_file_name)
    flash('Image was saved as: ' + img_file_name)
    return redirect(url_for('webcam.photo'))

