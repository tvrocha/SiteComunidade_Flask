from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirm_pass = PasswordField('Confirmação da Senha',
                                 validators=[DataRequired(), EqualTo('password')])
    button_submit_criarconta = SubmitField('Criar Conta')


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    remember_data = BooleanField('Lembrar dados de acesso')
    button_submit_login = SubmitField('Login')
