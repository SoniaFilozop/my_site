from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms import BooleanField, SubmitField, MultipleFileField, SelectMultipleField
from wtforms.validators import DataRequired


class NewsForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    address = TextAreaField("Адрес")
    plos = TextAreaField("Общая площадь")
    num_kom = TextAreaField("Количество комнат")
    etag = TextAreaField("Этаж")
    etag_home = TextAreaField("Этажей в доме")
    living = TextAreaField("Жилая")
    kitchen = TextAreaField("Кухня")
    remont = TextAreaField("Ремонт")
    type_home = TextAreaField("Тип дома")
    pass_lifts = TextAreaField("Пассажирских лифтов")
    gruz_lifts = TextAreaField("Грузовых лифтов")
    name = TextAreaField("Название")
    year = TextAreaField("Год постройки")
    height = TextAreaField("Высота потолков")
    pandus = TextAreaField("Пандус")
    parking = TextAreaField("Парковка")
    content = TextAreaField("Описание")
    is_private = BooleanField("Личное (не публикуется)")
    submit = SubmitField('Применить')
