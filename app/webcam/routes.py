from flask import render_template, current_app, redirect, url_for, flash
from flask_login import login_required
import os
from datetime import datetime

from urllib.request import urlopen, urlretrieve
from urllib.error import URLError, HTTPError

from app import db
from app.webcam import bp
from app.models import Photo


@bp.route('/photo')
@login_required
def photo():
    img_url = current_app.config['IP_WEBCAM_PHOTO_URL']
    try:
        response = urlopen(img_url, timeout=3).getcode()
    except URLError as e:
        flash('Error: {0}'.format(str(e.errno)), 'danger')
        return redirect(url_for('main.index'))
    else:
        print("All ok")

    return render_template('webcam/photo.html', img_url=img_url)


@bp.route('/save_photo/')
@login_required
def save_photo():
    filename = datetime.now().strftime("%Y%m%d-%H.%M.%S") + ".jpg"
    file_url = os.path.join(current_app.config['GALLERY_ROOT_DIR'], filename)
    try:
        p = Photo(filename=filename, file_path=file_url)
        p.save_photo()
        db.session.add(p)
        db.session.commit()
        flash('Image was saved as: ' + filename, 'success')
    except URLError as e:
        flash('Error: {0}'.format(str(e.errno)), 'warning')
        return redirect(url_for('main.index'))
    return redirect(url_for('webcam.photo'))


@bp.route('/delete_photo/<filename>')
@login_required
def delete_photo(filename):
    p = Photo.query.filter_by(filename=filename).first()
    if p is not None:
        p.delete_photo()
        db.session.delete(p)
        db.session.commit()
        flash('{} deleted.'.format(filename), 'success')
    else:
        flash('Could not delete photo.', 'warning')
    return redirect(url_for('webcam.show_gallery'))


@bp.route('/show_gallery/')
@login_required
def show_gallery():
    photos = Photo.query.all()
    return render_template('webcam/gallery.html', photos=photos)


