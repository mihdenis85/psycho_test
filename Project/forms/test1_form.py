from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField
from wtforms.validators import DataRequired


class Test1Form(FlaskForm):
    questions = [RadioField('Label', choices=[(0, 'Инженер-технолог'), (1, 'Инженер-конструктор')],
                           validators=[DataRequired(), ])]

    submit = SubmitField('Отправить')