from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#Primeira página. Login das pessoas
@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        botaoSelecionado = request.form['botao']
        loginNome = request.form['username']
        loginSenha = request.form['password']
        if botaoSelecionado == 'logar':
            return redirect("/indicadores")
        elif botaoSelecionado == 'cadastro':
            return redirect('/cadastro')
    return render_template("login.html")

#página principal
@app.route('/indicadores', methods=['POST', 'GET'])
def login():
    return render_template("indicadores.html")

#página de cadastro das pessoas
@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    return render_template("cadastro.html")

#página de cadastro dos animais
@app.route('/cadastro_animais', methods=['POST', 'GET'])
def cadastro_animais():
    return render_template("cadastro_animais")

app.run(debug=True)