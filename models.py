from flask_wtf import FlaskForm
from flask_material import Material  
from wtforms import StringField, PasswordField, SubmitField

class LoginForm(FlaskForm):
    namaUser = StringField('Nama user: ')
    kataSandi = PasswordField('Password :')
    submit = SubmitField('Login')

