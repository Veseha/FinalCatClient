from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class AddDepartForm(FlaskForm):
    title = StringField('Department Title', validators=[DataRequired()])
    chief = IntegerField('Chief ID', validators=[DataRequired()])
    members = StringField('Members', validators=[DataRequired()])
    email = EmailField('Department Email', validators=[DataRequired()])
    submit = SubmitField('Submit')
