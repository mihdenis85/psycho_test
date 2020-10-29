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
    question13 = RadioField('Label', choices=[(0, 'Нотариус'), (1, 'Менеджер')],
                           validators=[DataRequired(), ])
    question14 = RadioField('Label', choices=[(0, 'Перфораторщик'), (1, 'Художник')],
                           validators=[DataRequired(), ])
    question15 = RadioField('Label', choices=[(0, 'Политический деятель'), (1, 'Писатель')],
                           validators=[DataRequired(), ])

    question16 = RadioField('Label', choices=[(0, 'Дизайнер интерфейсов'), (1, 'Метеоролог')],
                           validators=[DataRequired(), ])
    question17 = RadioField('Label', choices=[(0, 'Водитель'), (1, 'Работник пресс-службы')],
                           validators=[DataRequired(), ])
    question18 = RadioField('Label', choices=[(0, 'Проектировщик'), (1, 'Риэлтор')],
                           validators=[DataRequired(), ])
    question19 = RadioField('Label', choices=[(0, 'Специалист по ремонту компьютеров и оргтехники'),
                                              (1, 'Секретарь-референт')],
                           validators=[DataRequired(), ])
    question20 = RadioField('Label', choices=[(0, 'Микробиолог'), (1, 'Психолог')],
                           validators=[DataRequired(), ])

    question21 = RadioField('Label', choices=[(0, 'Видеооператор'), (1, 'Режиссер')],
                           validators=[DataRequired(), ])
    question22 = RadioField('Label', choices=[(0, 'Экономист'), (1, 'Фармацевт')],
                           validators=[DataRequired(), ])
    question23 = RadioField('Label', choices=[(0, 'Зоолог'), (1, 'Главный инженер')],
                           validators=[DataRequired(), ])
    question24 = RadioField('Label', choices=[(0, 'Программист'), (1, 'Архитектор')],
                           validators=[DataRequired(), ])
    question25 = RadioField('Label', choices=[(0, 'Работник инспекции по делам несовершеннолетних'),
                                              (1, 'Сетевой маркетинг')],
                           validators=[DataRequired(), ])

    question26 = RadioField('Label', choices=[(0, 'Преподаватель'), (1, 'Банкир')],
                            validators=[DataRequired(), ])
    question27 = RadioField('Label', choices=[(0, 'Воспитатель'), (1, 'Декоратор')],
                            validators=[DataRequired(), ])
    question28 = RadioField('Label', choices=[(0, 'Реставратор'), (1, 'Зав. отделом предприятия')],
                            validators=[DataRequired(), ])
    question29 = RadioField('Label', choices=[(0, 'Корректор'), (1, 'Литератор и кинокритик')],
                            validators=[DataRequired(), ])
    question30 = RadioField('Label', choices=[(0, 'Журналист'), (1, 'Визажист')],
                            validators=[DataRequired(), ])

    question31 = RadioField('Label', choices=[(0, 'Парикмахер'), (1, 'Социолог')],
                            validators=[DataRequired(), ])
    question32 = RadioField('Label', choices=[(0, 'Экспедитор'), (1, 'Редактор')],
                            validators=[DataRequired(), ])
    question33 = RadioField('Label', choices=[(0, 'Ветеринар'), (1, 'Финансист')],
                            validators=[DataRequired(), ])
    question34 = RadioField('Label', choices=[(0, 'Автомеханик'), (1, 'Стилист')],
                            validators=[DataRequired(), ])
    question35 = RadioField('Label', choices=[(0, 'Археолог'), (1, 'Эксперт')],
                            validators=[DataRequired(), ])

    question36 = RadioField('Label', choices=[(0, 'Специалист в области кибербезопасности'),
                                              (1, 'Корреспондент')],
                            validators=[DataRequired(), ])
    question37 = RadioField('Label', choices=[(0, 'Эколог'), (1, 'Актер')],
                            validators=[DataRequired(), ])
    question38 = RadioField('Label', choices=[(0, 'Логопед'), (1, 'Контролер')],
                            validators=[DataRequired(), ])
    question39 = RadioField('Label', choices=[(0, 'Адвокат'), (1, 'Директор')],
                            validators=[DataRequired(), ])
    question40 = RadioField('Label', choices=[(0, 'Налоговый инспектор'), (1, 'Продюсер')],
                            validators=[DataRequired(), ])

    question41 = RadioField('Label', choices=[(0, 'Поэт, писатель'), (1, 'Продавец')],
                            validators=[DataRequired(), ])
    question42 = RadioField('Label', choices=[(0, 'Криминалист'), (1, 'Композитор')],
                            validators=[DataRequired(), ])

    submit = SubmitField('Отправить')