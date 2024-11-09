from comunidade import app, database, bcrypt
from comunidade.forms import FormLogin, FormCriarConta
from comunidade.models import Usuario
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required

lista_usuarios = ['Tulio', 'Guido', 'Junior', 'Sandra', 'Pancho']

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/contatos")
def pagina_contatos():
    return render_template("contatos.html")


@app.route("/usuarios")
@login_required
def pagina_usuarios():
    return render_template("usuarios.html", lista_usuarios=lista_usuarios)


@app.route("/login", methods=['GET', 'POST'])
def pagina_login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    if form_login.validate_on_submit() and 'button_submit_login' in request.form:
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.password, form_login.password.data):
            login_user(usuario, remember=form_login.remember_data.data)
            flash(f'Login feito com sucesso para email: {form_login.email.data}', 'alert-success')
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
        else:
            flash('Falha no login. E-mail ou senha incorreto.', 'alert-danger')
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

@app.route('/sair')
@login_required
def pagina_sair():
    logout_user()
    flash('Logout feito com sucesso', 'alert-success')
    return redirect(url_for('home'))

@app.route('/perfil')
@login_required
def pagina_perfil():
    return render_template('perfil.html')

@app.route('/post/criar')
@login_required
def pagina_criar_post():
    return render_template('criar_post.html')
