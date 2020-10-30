import os
from datetime import timedelta

from flask import Flask, render_template, redirect, url_for, make_response, jsonify, session
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from Project.checking_test1 import fun
from Project.checking_test2 import check_test2
from Project.data import db_session
from Project.data.models import User, ProfessionsCategories
from Project.data.models.professions import Profession
from Project.forms import Test1Form, Test2Form
from Project.forms.login_form import LoginForm
from Project.forms.register_form import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very_secret_key_jwkjldjwkdjlkwdkwjdldwhifwifhwiuhiuefhwiufhiuehf0f9wwefw'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=365)

login_manager = LoginManager()
login_manager.init_app(app)
admin_index = 1

@login_manager.user_loader
def load_user(user_id):
    db = db_session.create_session()
    return db.query(User).get(user_id)


@app.route('/')
def index():
    return render_template('main.html', title='Твоя профессия')


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    if current_user.is_authenticated:
        return redirect('/')
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Твоя профессия',
                                   form=form,
                                   message="Passwords doesn`t match")
        if len(form.password.data) < 6:
            return render_template('register.html', title='Твоя профессия',
                                   form=form,
                                   message="Password is too short")
        if form.password.data.isdigit() or form.password.data.isalpha():
            return render_template('register.html', title='Твоя профессия',
                                   form=form,
                                   message="Password must contain letters and digits")
        db = db_session.create_session()
        if db.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Твоя профессия',
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
    return render_template('register.html', title='Твоя профессия', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/')
    login_form = LoginForm()
    if login_form.validate_on_submit():
        db = db_session.create_session()
        user = db.query(User).filter(User.email == login_form.email.data).first()
        if not user:
            return render_template('login.html', form=login_form, message="Такого пользователя нет", title='Твоя профессия')
        if user.check_password(login_form.password.data):
            login_user(user, remember=True)
            return redirect('/')
        else:
            return render_template('login.html', form=login_form, message="Неправильный пароль", title='Твоя профессия')
    else:
        return render_template('login.html', form=login_form, title='Твоя профессия')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/account_info')
@login_required
def account_info():
    return render_template('account.html', title='Твоя профессия', user=current_user,
                           useracc=(current_user.name + ' ' + current_user.surname))


@app.route('/professions/categories')
def professions_categories():
    db = db_session.create_session()
    categories = db.query(ProfessionsCategories).all()
    return render_template('professions_categories.html', title='Твоя профессия', categories=categories)


@app.route('/professions/<int:category_id>')
def professions(category_id):
    db = db_session.create_session()
    professions = db.query(Profession).filter(Profession.category_id == category_id).all()
    return render_template('professions.html', title='Твоя профессия', professions=professions)


@app.route('/profession_description/<int:profession_id>')
def profession_description(profession_id):
    db = db_session.create_session()
    profession = db.query(Profession).filter(Profession.id == profession_id).first()
    if profession:
        return render_template('profession_description.html', profession=profession,
                               title='Твоя профессия')
    return redirect('/')


@app.route('/psycho_test1/<int:user_id>', methods=['GET', 'POST'])
@login_required
def psycho_test1(user_id):
    form = Test1Form()
    if form.validate_on_submit():
        db = db_session.create_session()
        results = [
            form.question1.data,
            form.question2.data,
            form.question3.data,
            form.question4.data,
            form.question5.data,
            form.question6.data,
            form.question7.data,
            form.question8.data,
            form.question9.data,
            form.question10.data,

            form.question11.data,
            form.question12.data,
            form.question13.data,
            form.question14.data,
            form.question15.data,
            form.question16.data,
            form.question17.data,
            form.question18.data,
            form.question19.data,
            form.question20.data,

            form.question21.data,
            form.question22.data,
            form.question23.data,
            form.question24.data,
            form.question25.data,
            form.question26.data,
            form.question27.data,
            form.question28.data,
            form.question29.data,
            form.question30.data,

            form.question31.data,
            form.question32.data,
            form.question33.data,
            form.question34.data,
            form.question35.data,
            form.question36.data,
            form.question37.data,
            form.question38.data,
            form.question39.data,
            form.question40.data,

            form.question41.data,
            form.question42.data
        ]
        try:
            results = [int(el) for el in results]
            result = fun(results)
            current_user.test1_results = result
            print(result)
            db.merge(current_user)
            db.commit()
        except Exception:
            print('Error')
        return redirect('/test1_results')
    return render_template('test1.html', title='Твоя профессия', user_id=user_id, form=form)


@app.route('/test1_results')
@login_required
def test1_results():
    results = current_user.test1_results
    if results:
        return render_template('results_test.html', title='Результаты теста', results=results)
    return render_template('results_test.html', title='Результаты теста', results='Результатов еще нет. Пройдите наш тест')


@app.route('/psycho_test2/<int:user_id>', methods=['GET', 'POST'])
@login_required
def psycho_test2(user_id):
    form = Test2Form()
    if form.validate_on_submit():
        db = db_session.create_session()
        results = [
            form.question1.data,
            form.question2.data,
            form.question3.data,
            form.question4.data,
            form.question5.data,
            form.question6.data,
            form.question7.data,
            form.question8.data,
            form.question9.data,
            form.question10.data,

            form.question11.data,
            form.question12.data,
            form.question13.data,
            form.question14.data,
            form.question15.data,
            form.question16.data,
            form.question17.data,
            form.question18.data,
            form.question19.data,
            form.question20.data
        ]
        try:
            results = [int(el) for el in results]
            result = check_test2(results)
            current_user.test2_results = result
            print(result)
            db.merge(current_user)
            db.commit()
        except Exception:
            print('Error')
        return redirect('/test2_results')
    return render_template('test2.html', title='Твоя профессия', user_id=user_id, form=form)


@app.route('/test2_results')
@login_required
def test2_results():
    results = current_user.test2_results
    if results:
        return render_template('results_test2.html', title='Результаты теста', results=results)
    return render_template('results_test2.html', title='Результаты теста', results='Результатов еще нет. Пройдите наш тест')


@app.errorhandler(404)
def not_found(error):
    if current_user.is_authenticated:
        info = (current_user.name + ' ' + current_user.surname)
    else:
        info = 'Anonymous'
    er_txt = '404 not found: Такого адреса не существует'
    return render_template('error.html', title='Твоя профессия',
                           text=er_txt, useracc=info)


@app.errorhandler(401)
def unauth(error):
    er_txt = '401 not authorized: Пожалуйста, авторизуйтесь на сайте!'
    return render_template('error.html', title='Твоя профессия', text=er_txt)


@app.errorhandler(500)
def error_serv(error):
    er_text = 'Кажется, на сервере возникла ошибка. Выйдите на главную страницу и попробуйте снова'
    return render_template('error.html', title='Твоя профессия', text=er_text)


from os import path
db_session.global_init(path.join(path.dirname(__file__), './db/project.db'))


def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)