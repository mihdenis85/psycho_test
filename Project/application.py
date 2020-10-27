import os
from datetime import timedelta

from flask import Flask, render_template, redirect, url_for, make_response, jsonify, session
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from Project.data import db_session
from Project.data.models import User
from Project.forms.login_form import LoginForm
from Project.forms.register_form import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very_secret_key_jwkjldjwkdjlkwdkwjdldwhifwifhwiuhiuefhwiufhiuehf0f9wwefw'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=365)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db = db_session.create_session()
    return db.query(User).get(user_id)


@app.route('/')
def index():
    return render_template('main.html', title='Main')


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    if current_user.is_authenticated:
        return redirect('/')
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Register',
                                   form=form,
                                   message="Passwords doesn`t match")
        if len(form.password.data) < 6:
            return render_template('register.html', title='Register',
                                   form=form,
                                   message="Password is too short")
        if form.password.data.isdigit() or form.password.data.isalpha():
            return render_template('register.html', title='Register',
                                   form=form,
                                   message="Password must contain letters and digits")
        db = db_session.create_session()
        if db.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Register',
                                   form=form,
                                   message="User already exists")
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            country=form.country.data,
            city=form.city.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        db.add(user)
        db.commit()
        return redirect('/login')
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/')
    login_form = LoginForm()
    if login_form.validate_on_submit():
        db = db_session.create_session()
        user = db.query(User).filter(User.email == login_form.email.data).first()
        if not user:
            return render_template('login.html', form=login_form, message="No such user", title='Login')
        if user.check_password(login_form.password.data):
            login_user(user, remember=True)
            return redirect('/')
        else:
            return render_template('login.html', form=login_form, message="Wrong password", title='Login')
    else:
        return render_template('login.html', form=login_form, title='Login')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.errorhandler(404)
def not_found(error):
    if current_user.is_authenticated:
        info = (current_user.name + ' ' + current_user.surname)
    else:
        info = 'Anonymous'
    er_txt = '404 not found: Wrong request: no such web-address!'
    return render_template('error.html', title='Error',
                           text=er_txt, useracc=info)


@app.errorhandler(401)
def unauth(error):
    er_txt = '401 not authorized: Please log in or register!!!'
    return render_template('error.html', title='Error', text=er_txt)


@app.errorhandler(500)
def error_serv(error):
    er_text = 'You are trying to break down the server. Don`t do that thing!'
    return render_template('error.html', title='Error', text=er_text)


from os import path
db_session.global_init(path.join(path.dirname(__file__), './db/project.db'))


def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)