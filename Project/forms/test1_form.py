from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField
from wtforms.validators import DataRequired


class Test1Form(FlaskForm):
    question1 = RadioField('Label', choices=[(0, 'Инженер-технолог'), (1, 'Инженер-конструктор')],
                           validators=[DataRequired(), ])
    question2 = RadioField('Label', choices=[(0, 'Электрорадиотехник'), (1, 'Врач-терапевт')],
                           validators=[DataRequired(), ])
    question3 = RadioField('Label', choices=[(0, 'Инженер-программист'), (1, 'Мехатроник')],
                           validators=[DataRequired(), ])
    question4 = RadioField('Label', choices=[(0, 'Фотограф'), (1, 'Маркетолог')],
                           validators=[DataRequired(), ])
    question5 = RadioField('Label', choices=[(0, 'Спасатель МЧС'), (1, 'Дизайнер')],
                           validators=[DataRequired(), ])

    question6 = RadioField('Label', choices=[(0, 'Политолог'), (1, 'Психиатр')],
                           validators=[DataRequired(), ])
    question7 = RadioField('Label', choices=[(0, 'Ученый химик'), (1, 'Бухгалтер')],
                           validators=[DataRequired(), ])
    question8 = RadioField('Label', choices=[(0, 'Философ'), (1, 'Предприниматель')],
                           validators=[DataRequired(), ])
    question9 = RadioField('Label', choices=[(0, 'Лингвист'), (1, 'Модельер')],
                           validators=[DataRequired(), ])
    question10 = RadioField('Label', choices=[(0, 'Инспектор службы занятости населения'),
                                              (1, 'SEO-специалист')],
                           validators=[DataRequired(), ])

    question11 = RadioField('Label', choices=[(0, 'Социальный педагог'), (1, 'Работник банка')],
                           validators=[DataRequired(), ])
    question12 = RadioField('Label', choices=[(0, 'Тренер'), (1, 'Нотариус')],
                           validators=[DataRequired(), ])
    question13 = RadioField('Label', choices=[(0, 'Инженер-технолог'), (1, 'Инженер-конструктор')],
                           validators=[DataRequired(), ])
    question14 = RadioField('Label', choices=[(0, 'Инженер-технолог'), (1, 'Инженер-конструктор')],
                           validators=[DataRequired(), ])
    question15 = RadioField('Label', choices=[(0, 'Инженер-технолог'), (1, 'Инженер-конструктор')],
                           validators=[DataRequired(), ])

    question16 = RadioField('Label', choices=[(0, 'Инженер-технолог'), (1, 'Инженер-конструктор')],
                           validators=[DataRequired(), ])
    question17 = RadioField('Label', choices=[(0, 'Инженер-технолог'), (1, 'Инженер-конструктор')],
                           validators=[DataRequired(), ])
    question18 = RadioField('Label', choices=[(0, 'Инженер-технолог'), (1, 'Инженер-конструктор')],
                           validators=[DataRequired(), ])
    question19 = RadioField('Label', choices=[(0, 'Инженер-технолог'), (1, 'Инженер-конструктор')],
                           validators=[DataRequired(), ])
    question20 = RadioField('Label', choices=[(0, 'Инженер-технолог'), (1, 'Инженер-конструктор')],
                           validators=[DataRequired(), ])

    question21 = RadioField('Label', choices=[(0, 'Инженер-технолог'), (1, 'Инженер-конструктор')],
                           validators=[DataRequired(), ])
    question22 = RadioField('Label', choices=[(0, 'Инженер-технолог'), (1, 'Инженер-конструктор')],
                           validators=[DataRequired(), ])
    question23 = RadioField('Label', choices=[(0, 'Инженер-технолог'), (1, 'Инженер-конструктор')],
                           validators=[DataRequired(), ])
    question24 = RadioField('Label', choices=[(0, 'Инженер-технолог'), (1, 'Инженер-конструктор')],
                           validators=[DataRequired(), ])
    question25 = RadioField('Label', choices=[(0, 'Инженер-технолог'), (1, 'Инженер-конструктор')],
                           validators=[DataRequired(), ])

    question26 = RadioField('Label', choices=[(0, 'Инженер-технолог'), (1, 'Инженер-конструктор')],
                            validators=[DataRequired(), ])
    question27 = RadioField('Label', choices=[(0, 'Инженер-технолог'), (1, 'Инженер-конструктор')],
                            validators=[DataRequired(), ])
    question28 = RadioField('Label', choices=[(0, 'Инженер-технолог'), (1, 'Инженер-конструктор')],
                            validators=[DataRequired(), ])
    question29 = RadioField('Label', choices=[(0, 'Инженер-технолог'), (1, 'Инженер-конструктор')],
                            validators=[DataRequired(), ])
    question30 = RadioField('Label', choices=[(0, 'Инженер-технолог'), (1, 'Инженер-конструктор')],
                            validators=[DataRequired(), ])

    question31 = RadioField('Label', choices=[(0, 'Инженер-технолог'), (1, 'Инженер-конструктор')],
                            validators=[DataRequired(), ])
    question22 = RadioField('Label', choices=[(0, 'Инженер-технолог'), (1, 'Инженер-конструктор')],
                            validators=[DataRequired(), ])
    question23 = RadioField('Label', choices=[(0, 'Инженер-технолог'), (1, 'Инженер-конструктор')],
                            validators=[DataRequired(), ])
    question24 = RadioField('Label', choices=[(0, 'Инженер-технолог'), (1, 'Инженер-конструктор')],
                            validators=[DataRequired(), ])
    question25 = RadioField('Label', choices=[(0, 'Инженер-технолог'), (1, 'Инженер-конструктор')],
                            validators=[DataRequired(), ])

    question21 = RadioField('Label', choices=[(0, 'Инженер-технолог'), (1, 'Инженер-конструктор')],
                            validators=[DataRequired(), ])
    question22 = RadioField('Label', choices=[(0, 'Инженер-технолог'), (1, 'Инженер-конструктор')],
                            validators=[DataRequired(), ])
    question23 = RadioField('Label', choices=[(0, 'Инженер-технолог'), (1, 'Инженер-конструктор')],
                            validators=[DataRequired(), ])
    question24 = RadioField('Label', choices=[(0, 'Инженер-технолог'), (1, 'Инженер-конструктор')],
                            validators=[DataRequired(), ])
    question25 = RadioField('Label', choices=[(0, 'Инженер-технолог'), (1, 'Инженер-конструктор')],
                            validators=[DataRequired(), ])

    question21 = RadioField('Label', choices=[(0, 'Инженер-технолог'), (1, 'Инженер-конструктор')],
                            validators=[DataRequired(), ])
    question22 = RadioField('Label', choices=[(0, 'Инженер-технолог'), (1, 'Инженер-конструктор')],
                            validators=[DataRequired(), ])
    question23 = RadioField('Label', choices=[(0, 'Инженер-технолог'), (1, 'Инженер-конструктор')],
                            validators=[DataRequired(), ])
    question24 = RadioField('Label', choices=[(0, 'Инженер-технолог'), (1, 'Инженер-конструктор')],
                            validators=[DataRequired(), ])
    question25 = RadioField('Label', choices=[(0, 'Инженер-технолог'), (1, 'Инженер-конструктор')],
                            validators=[DataRequired(), ])

    submit = SubmitField('Отправить')