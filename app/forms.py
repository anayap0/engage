from flask_wtf import FlaskForm
from wtforms import (BooleanField, FieldList, Form, FormField, PasswordField,
                     RadioField, SelectField, StringField, SubmitField,
                     TextAreaField)
from wtforms.fields.html5 import IntegerRangeField
from wtforms.widgets import html5 as widgets
from wtforms import core
from wtforms.validators import (DataRequired, Email, EqualTo, Length,
                                ValidationError)

from app.models import User


class LoginForm(FlaskForm): # Have to pass FLaskForm in as the default
    username = StringField("Username", validators=[DataRequired()]) # render_kw={"placeholder": "test"}
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm): 
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    role = SelectField('Teacher or Student?', choices=[(0, 'Teacher'), (1,'Student')], coerce=int)
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()]) # Username input field
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)]) # TextAreaField is a multi-line box where the user can enter text, has to be between 0 and 140 characters, 140 matches space in database (check models)
    submit = SubmitField('Submit') 

class TeacherRadioForm(FlaskForm):
    prompt = StringField('Prompt', validators=[DataRequired()])
    options = SelectField('Teacher or Student?', choices=[(0, 'Yes/Maybe/No'), (1,'Agree/Disagree'), (2, 'Rating')], coerce=int)
    submit = SubmitField('Distribute')

class StudentYesForm(FlaskForm):
    form_type_num = 0
    options = RadioField('RadioField',  coerce=int, choices=[(1, 'Yes'), (2, 'Maybe'), (3, 'No')], validators=[DataRequired()])
    submit = SubmitField('Submit')

class StudentAgreeForm(FlaskForm):
    form_type_num = 1
    options = RadioField('RadioField', coerce=int, choices=[(1, 'Agree'), (2, 'Disagree')], validators=[DataRequired()])
    submit = SubmitField('Submit')

class StudentRatingForm(FlaskForm):
    form_type_num = 2
    options = IntegerRangeField('IntRange')
    # options = widgets.RangeInput()
    submit = SubmitField('Submit')

class EditClassForm(FlaskForm):
    class_name = StringField('Change Class Name', validators=[DataRequired()])
    class_icon = RadioField('Class Icon', choices=[('/static/images/classes_art.png', 'Art'), 
                                                    ('/static/images/classes_atom.png', 'Atom'),
                                                    ('/static/images/classes_books.png', 'Books'),
                                                    ('/static/images/classes_calculator.png', 'Calculator'),
                                                    ('/static/images/classes_chemistry.png', 'Chemistry'),
                                                    ('/static/images/classes_dna.png', 'DNA'),
                                                    ('/static/images/classes_fishbowl.png', 'Fishbowl'),
                                                    ('/static/images/classes_language.png', 'Language'),
                                                    ('/static/images/classes_laptop.png', 'Laptop'),
                                                    ('/static/images/classes_laurel.png', 'Laurel'),
                                                    ('/static/images/classes_numbers.png', 'Numbers'),
                                                    ('/static/images/classes_operators.png', 'Operators'),
                                                    ('/static/images/classes_PE.png', 'PE')])
    class_color = RadioField('Class Color', choices = [(0, 'Red'),
                                                        (1, 'Yellow'),
                                                        (2, 'Blue'),
                                                        (3, 'Green'),
                                                        (4, 'Orange'),
                                                        (5, 'Purple')],
                                                        coerce=int)
    submit = SubmitField('Save Changes')

class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')

class ContactUs(FlaskForm):
    account_email = StringField('Email associated with your account.', validators=[DataRequired(), Email()])
    concern = TextAreaField('What is your concern/question/etc?', validators=[Length(min=10, max=250)])
    submit = SubmitField('submit')
