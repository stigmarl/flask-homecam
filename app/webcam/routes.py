from flask import render_template, current_app
from flask_login import login_required
from app.webcam import bp


@bp.route('/photo')
@login_required
def photo():
    img_url = current_app.config['IP_WEBCAM_PHOTO_URL']
    return render_template('webcam/photo.html', img_url=img_url)

