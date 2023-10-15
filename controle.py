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
                return redirect(url_for("/fazenda"))
            else:
                flash("Usuário ou senha incorretos")
                return redirect(url_for("/"))

        elif botaoSelecionado == 'cadastro':
            return redirect(url_for('/cadastro'))
    return render_template("login.html")

#página de cadastro das pessoas
@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['username']
        email = request.form['email']
        senha = request.form['password']
        modelo.Usuario(nome, email, senha).cadastrar()
        return redirect(url_for('/'))

    else:
       flash("Erro no cadastro")
       return render_template("cadastro.html")

#página principal da fazenda
@app.route('/fazenda', methods=['POST', 'GET'])
def login():
    if request.method=='POST':
    

        return render_template("fazenda.html")

#página de cadastro dos animais
@app.route('/rebanho', methods=['POST', 'GET'])
def rebanho():
    '''
    APENAS UM PROTÓTIPO###########!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if isVaca == 1:
            brinco = request.form['brinco']
            raça = request.form['raça']
            pasto = request.form['pasto']
            peso = request.form['peso']
            gestacao = request.form['gestacao']
            dataCria = request.form['dataCria']
            modelo.Animal.cadastrar(brinco, raça, pasto, peso)
            flash("Vaca cadastrada com sucesso")
            return redirect(url_for('/rebanho'))

    '''
    '''
        if isVaca == 0:
            brinco = request.form['brinco']
            raça = request.form['raça']
            pasto = request.form['pasto']
            peso = request.form['peso']
            x= modelo.Animal.cadastrar(brinco, raça, pasto, peso)
            modelo.Animal.touro(x)
            flash("Touro cadastrado com sucesso")
            return redirect(url_for('/rebanho'))
    
        else:
            prox= request.form['prox'](seria um botão que redireciona para a página de vizualização de vacas)########!!!!!!!!!!!!!!!!!!!!!!!!
            if prox == 'vizualizar':
                brinco = request.form['brinco']
                x= modelo.Vaca.vizualizarVacas(brinco)
                data= x['dataCrias']
                peso = x['peso']
                pasto = x['pasto']
                return render_template("vizualizar.html", data, peso, pasto)###########!!!!!!!!!!!!!!!!!!!!!!
            
    '''
    return render_template("rebanho.html")

@app.route('/veterinaria', methods=['POST', 'GET'])
def veterinaria():
    return render_template("veterinaria.html")

app.run(debug=True)