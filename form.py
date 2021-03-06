from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SignUp(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])

    submit = SubmitField('Submit')
