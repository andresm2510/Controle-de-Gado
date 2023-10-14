# Incluindo as bibliotecas
from flask import Flask, render_template, request, redirect, url_for , flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
# Incluindo o arquivo de modelo
import modelo

app = Flask(__name__)
app.secret_key = 'chave'  

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

def load_user(x):
    user_data = modelo.Usuario(x)
    user = modelo.Usuario(user_data)
    user._id = x
    return user

@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        botaoSelecionado = request.form['botao']
        loginNome = request.form['username']
        loginSenha = request.form['password']
        if botaoSelecionado == 'logar':
            if modelo.Usuario.login(loginNome, loginSenha):
                x= modelo.Usuario.get_id(loginNome)
                user = load_user(x)
                login_user(user)
                return redirect("/fazenda")
            else:
                flash("Usuário ou senha incorretos")
                return redirect("/")

        elif botaoSelecionado == 'cadastro':
            return redirect('/cadastro')
    return render_template("login.html")

#página de cadastro das pessoas
@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    return render_template("cadastro.html")

#página principal da fazenda
@app.route('/fazenda', methods=['POST', 'GET'])
def login():
    return render_template("fazenda.html")

#página de cadastro dos animais
@app.route('/rebanho', methods=['POST', 'GET'])
def rebanho():
    return render_template("rebanho.html")

@app.route('/veterinaria', methods=['POST', 'GET'])
def veterinaria():
    return render_template("veterinaria.html")

app.run(debug=True)