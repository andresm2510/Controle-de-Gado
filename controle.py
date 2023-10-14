# Incluindo as bibliotecas
from flask import Flask, render_template, request, redirect, url_for
# Incluindo o arquivo de modelo
from modelo import Animal, Vaca

app = Flask(__name__)

#Primeira página. Login das pessoas
@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        botaoSelecionado = request.form['botao']
        loginNome = request.form['username']
        loginSenha = request.form['password']
        if botaoSelecionado == 'logar':
            return redirect("/fazenda")
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
def cadastro_animais():
    return render_template("rebanho.html")

@app.route('/veterinaria', methods=['POST', 'GET'])
def cadastro_animais():
    return render_template("veterinaria.html")

app.run(debug=True)