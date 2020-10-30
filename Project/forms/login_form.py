from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = TextField('E-mail', validators=[DataRequired()])
    password = PasswordField('Пароль')
    submit = SubmitField('Войти')