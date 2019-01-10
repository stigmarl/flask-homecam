from app import app
from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_user

from app.forms import LoginForm
from app.models import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/photo')
def photo():
    img_url = app.config['IP_WEBCAM_PHOTO_URL']
    return render_template('photo.html', img_url=img_url)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)