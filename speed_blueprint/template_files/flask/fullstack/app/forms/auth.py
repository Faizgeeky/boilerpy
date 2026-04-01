"""Authentication forms using Flask-WTF."""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
import re
from app.models.user import User


class LoginForm(FlaskForm):
    """Login form."""
    username = StringField('Username', validators=[
        DataRequired(message='Username is required'),
        Length(min=3, max=50, message='Username must be between 3 and 50 characters')
    ])
    password = PasswordField('Password', validators=[
        DataRequired(message='Password is required')
    ])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    """Registration form."""
    username = StringField('Username', validators=[
        DataRequired(message='Username is required'),
        Length(min=3, max=50, message='Username must be between 3 and 50 characters')
    ])
    email = StringField('Email', validators=[
        DataRequired(message='Email is required'),
        Email(message='Invalid email address')
    ])
    full_name = StringField('Full Name', validators=[
        Length(max=100, message='Full name must be less than 100 characters')
    ])
    password = PasswordField('Password', validators=[
        DataRequired(message='Password is required'),
        Length(min=8, message='Password must be at least 8 characters')
    ])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(message='Please confirm your password'),
        EqualTo('password', message='Passwords must match')
    ])
    submit = SubmitField('Register')

    def validate_username(self, username):
        """Validate username format and uniqueness."""
        # Check format (alphanumeric and underscore only)
        pattern = r'^[a-zA-Z0-9_]+$'
        if not re.match(pattern, username.data):
            raise ValidationError('Username can only contain letters, numbers, and underscores')

        # Check if username exists
        user = User.get_by_username(username.data)
        if user:
            raise ValidationError('Username already taken. Please choose a different one.')

    def validate_email(self, email):
        """Validate email uniqueness."""
        user = User.get_by_email(email.data)
        if user:
            raise ValidationError('Email already registered. Please use a different one.')
