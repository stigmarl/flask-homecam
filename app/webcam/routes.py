from flask import render_template, current_app, redirect, url_for, flash
from flask_login import login_required
import os

from urllib.request import urlopen
from urllib.error import URLError, HTTPError

from app.webcam import bp
from app.models import Image


@bp.route('/photo')
@login_required
def photo():
    img_url = current_app.config['IP_WEBCAM_PHOTO_URL']
    try:
        response = urlopen(img_url, timeout=3).getcode()
    except URLError as e:
        #print('Error:', e.reason)
        flash('Error: {0}'.format(str(e.errno)), 'danger')
        return redirect(url_for('main.index'))
    else:
        print("All ok")

    return render_template('webcam/photo.html', img_url=img_url)


@bp.route('/save_photo/')
@login_required
def save_photo():
    image = Image(post=True)
    return redirect(url_for('webcam.photo'))


@bp.route('/delete_photo/<filename>')
@login_required
def delete_photo(filename):
    if filename in os.listdir(current_app.config['GALLERY_ROOT_DIR']):
        os.remove(os.path.join(current_app.config['GALLERY_ROOT_DIR'], filename))
        flash(filename + ' removed!', 'success')

    return redirect(url_for('webcam.show_gallery'))


@bp.route('/show_gallery/')
@login_required
def show_gallery():
    root_dir = current_app.config['GALLERY_ROOT_DIR']
    images = Image.all(root_dir)
    return render_template('webcam/gallery.html', images=images)


