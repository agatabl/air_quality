from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class RegistrationForm(FlaskForm):
    email =  StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=3, max=20)])
    reenter_password = PasswordField('Confirm password', validators=[EqualTo('password', message ="The password doesn't match")])
    submit = SubmitField('SignUp')


class LoginForm(FlaskForm):
    email =  StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=3, max=20)])
    submit = SubmitField('LogIn')
