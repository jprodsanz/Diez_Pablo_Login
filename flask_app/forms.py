#this would be your models 
# this method relies on py classes to represent forms
# below are your validations, flaskform makes this so much easier 

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,  BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_app.models import User


#these classes are your reg and login fields <3

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name',
                            validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('Last Name',
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', 
                            validators=[DataRequired(), Email()]) 
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                        validators =[DataRequired(), EqualTo('password')])
    submit =SubmitField('Register')

    def validate_email(self, email):
        
        user = User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('email is already taken')

class LoginForm(FlaskForm):
    email = StringField('Email', 
                            validators=[DataRequired(), Email()]) 
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit =SubmitField('Login')


