from flask import Flask, render_template, url_for, request, flash, redirect
from forms import FormCriarConta, FormLogin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

lista_usuarios = ['Tulio', 'Guido', 'Junior', 'Sandra', 'Pancho']

app.config['SECRET_KEY'] = '69ee7cc6816f314e0c9d5450992baeee'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/contatos")
def pagina_contatos():
    return render_template("contatos.html")


@app.route("/usuarios")
def pagina_usuarios():
    return render_template("usuarios.html", lista_usuarios=lista_usuarios)


@app.route("/login", methods=['GET', 'POST'])
def pagina_login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    if form_login.validate_on_submit() and 'button_submit_login' in request.form:
        flash(f'Login feito com sucesso para email: {form_login.email.data}', 'alert-success')
        return redirect(url_for('home'))
    if form_criarconta.validate_on_submit() and 'button_submit_criarconta' in request.form:
        flash(f'Conta criada com sucesso para email: {form_criarconta.email.data}', 'alert-success')
        return redirect(url_for('home'))
    return render_template("login.html", form_login=form_login, form_criarconta=form_criarconta)


if __name__ == '__main__':
    app.run(debug=True)
