from flask.ext.wtf import Form
from wtforms import SelectField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateTimeField


TIME_FMT = '%d/%m/%Y %I:%M %p'
TIME_LABEL = 'Time (format is day/month/year hour:minutes AM/PM/am/pm)'
TIME = DateTimeField(TIME_LABEL, validators=[DataRequired()], format=TIME_FMT)


class FeedingForm(Form):
    side = SelectField('Breast used', validators=[DataRequired()], coerce=str, choices=[('left', 'Left Breast'), ('right', 'Right Breast')])
    time = TIME


class DiaperForm(Form):
    diaper_type = SelectField('Type of Diaper', validators=[DataRequired()], coerce=str, choices=[('wet', 'Wet'), ('stinky', 'Stinky')])
    time = TIME

