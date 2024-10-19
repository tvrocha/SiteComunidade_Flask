from flask import Flask, render_template, url_for
from forms import FormCriarConta, FormLogin

app = Flask(__name__)

lista_usuarios = ['Tulio', 'Guido', 'Junior', 'Sandra', 'Pancho']

app.config['SECRET_KEY'] = '69ee7cc6816f314e0c9d5450992baeee'


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/contatos")
def pagina_contatos():
    return render_template("contatos.html")


@app.route("/usuarios")
def pagina_usuarios():
    return render_template("usuarios.html", lista_usuarios=lista_usuarios)


@app.route("/login")
def pagina_login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    return render_template("login.html", form_login=form_login, form_criarconta=form_criarconta)


if __name__ == '__main__':
    app.run(debug=True)
