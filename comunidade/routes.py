from comunidade import app, database, bcrypt
from comunidade.forms import FormLogin, FormCriarConta
from comunidade.models import Usuario
from flask import render_template, redirect, url_for, flash, request

lista_usuarios = ['Tulio', 'Guido', 'Junior', 'Sandra', 'Pancho']

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
        # criar o usuario
        # adicionar a sessão e commitar
        with app.app_context():
            password_bcrypt = bcrypt.generate_password_hash(form_criarconta.password.data)
            usuario = Usuario(username=form_criarconta.username.data, email=form_criarconta.email.data, password=password_bcrypt)
            database.session.add(usuario)
            database.session.commit()
        flash(f'Conta criada com sucesso para email: {form_criarconta.email.data}', 'alert-success')
        return redirect(url_for('home'))
    return render_template("login.html", form_login=form_login, form_criarconta=form_criarconta)
