from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField, SelectField, FormField, Form
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from jasonsite.models import User


class SignUpForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(message="First name required"), Length(max=64, message="Max limit reached")])
    last_name = StringField('Last Name', validators=[DataRequired(message="Last name required"), Length(max=64, message="Max limit reached")])
    email = StringField('Email', validators=[DataRequired(message="Email required"), Email(), Length(max=64)])
    password = PasswordField('Password', validators=[DataRequired(message="Password required"), Length(min=8, max=32, message="Password has to be between a minimum of 8 characters")])
    resubmit_password = PasswordField('Confirm Password', validators=[DataRequired(message="Resubmit same password"), EqualTo('password', message="Passwords did not match")])
    submit = SubmitField('Submit')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email in use.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Submit')

class AdminToolForm(FlaskForm):
    user            = StringField("Email", validators=[DataRequired("Please Input Email")])
    submit          = SubmitField('Submit')

class ExtendedPost(Form):
    post            = TextAreaField('Post Text')
    fig_caption     = StringField('Fig caption...') 
    alt_title       = StringField("Accessibility description")
    post_image      = FileField('File', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'pdf'])])
    submit          = SubmitField('Submit')


class PostForm(FlaskForm):
    title           = StringField('Title')
    post            = TextAreaField('Post Text')
    blurb           = StringField('Blurb')
    category_post   = SelectField('Category', choices=[('web_development','Web Development'), ('web_design','Web Design'), ('graphic_design','Graphic Design') ])
    post_image      = FileField('File', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'pdf'])])
    alt_title       = StringField("Accessibility description", validators=[DataRequired(message="For accessibility")])
    tag1            = StringField('Tag one...')
    tag2            = StringField('Tag two...')
    tag3            = StringField('Tag three...')
    tag4            = StringField('Tag four...')
    tag5            = StringField('Tag five...')
    fig_caption     = StringField('Fig caption...')
    ext_post1       = FormField(ExtendedPost)
    ext_post2       = FormField(ExtendedPost)
    ext_post3       = FormField(ExtendedPost)
    ext_post4       = FormField(ExtendedPost)
    ext_post5       = FormField(ExtendedPost)
    submit          = SubmitField('Submit')
