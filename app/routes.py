from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/photo')
def photo():
    img_url = app.config['IP_WEBCAM_PHOTO_URL']
    return render_template('photo.html', img_url=img_url)
