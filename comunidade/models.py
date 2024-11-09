from comunidade import database, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_usuario(id_usuario):
    # método get busca a primary_key da tabela
    # int para garantir que o id seja inteiro
    return Usuario.query.get(int(id_usuario))


# UserMixin atribui a classe tudo que precisa pro login (se manter logado, etc...)
class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    password = database.Column(database.String, nullable=False)
    profile_picture = database.Column(database.String, default='default.jpg')
    courses = database.Column(database.String, nullable=False, default='Não informado')
    posts = database.relationship('Post', backref='autor', lazy=True)


class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String, nullable=False)
    body = database.Column(database.Text, nullable=False)
    creation_date = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    id_user = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
