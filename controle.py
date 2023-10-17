# Incluindo as bibliotecas
from flask import Flask, render_template, request, redirect, url_for , flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import time
# Incluindo o arquivo de modelo
from modelo import * 

app = Flask(__name__)
app.secret_key = 'chave'  

'''login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(email):
    user_data = modelo.Usuario.get_user(email)
    print('userdata ok')
    time.sleep(10)
    if user_data:
        try:
            user = modelo.Usuario(user_data['nome'], user_data['email'], user_data['senha'])
            return user
        except Exception as e:
            print(f"Error creating user object: {e}")
    return None
'''
'''def cadastrarUsuario(nome, email, senha):
    x = modelo.Usuario(nome, email, senha)
    Usuario.cadastrar(nome, email, senha)
'''
@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        loginEmail = request.form['email']
        loginSenha = request.form['password']
        '''print(loginEmail, loginSenha)'''
        teste = Usuario.loginuser(loginEmail, loginSenha)
        global u
        if teste:
            '''x= "loginEmail"
            user = load_user(x)
            login_user(user)'''
            return redirect(url_for("fazenda"))
        else:
            flash("Usuário ou senha incorretos")
            print("Usuário ou senha incorretos")
            return redirect("/")
    return render_template("login.html")

#página de cadastro das pessoas
@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['username']
        email = request.form['email']
        senha = request.form['password']
        print('teste',email)
        '''cadastrarUsuario(nome, email, senha)'''
        global u
        u = Usuario(nome=nome, email=email, senha=senha)
        u.cadastrar()
        return redirect('/')

    return render_template('cadastro.html')

@app.route('/config_conta', methods=['POST','GET'])
def config_conta():
    if request.method == 'POST':
        nome = request.form['username']
        email = request.form['email']
        senha = request.form['password']
        return redirect('/config_conta')
    return render_template('config_conta.html')

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    return render_template('contato.html')

@app.route('/suporte', methods=['GET','POST'])
def ajuda():
    return render_template('ajuda_suporte.html')

#página principal da fazenda
@app.route('/fazenda', methods=['POST', 'GET'])
def fazenda():
    if request.method=='POST':
        return("/rebanho.html")
    
    a = retornaFazenda()
    cabecasGado = a[0]
    vacasGestantes = a[1]
    consumoRacao = a[2]
    consultas = a[3]
    return render_template("fazenda.html", cabecasGado=cabecasGado, vacasGestantes=vacasGestantes, consumoRacao=consumoRacao, consultas=consultas)

#página de cadastro dos animais
@app.route('/rebanho', methods=['POST', 'GET'])
def rebanho():
    '''
    x = db

    animais = 
    '''
    return render_template("rebanho.html")

@app.route('/veterinaria', methods=['POST', 'GET'])
def veterinaria():
    a = Vaca.vizualizarVacas(brinco)
    peso = a[0]
    raca = a[1]
    brinco = a[2]
    sexo = a[3]
    tempo_prenha = a[4]
    tempo_parto = a[5]
    pasto = a[6]
    gasto_gestacao = a[7]
    gasto_vida = a[8]
    crias = a[9]
    tempo_entre_crias =a[10]
    complicacoes = a[11]
    vacinas = a[12]

    usuario = Usuario.get_user()

    return render_template("veterinaria.html", usuario=usuario, peso=peso, raca=raca, brinco=brinco, sexo=sexo, tempo_prenha=tempo_prenha, tempo_parto=tempo_parto, pasto=pasto, gasto_gestacao=gasto_gestacao, gasto_vida=gasto_vida, crias=crias, tempo_entre_crias=tempo_entre_crias, complicacoes=complicacoes, vacinas=vacinas)

@app.route("/cadastro_animais", methods=['POST', 'GET'])
def cadastro_animais():
    if request.method == 'POST':
        peso = request.form['peso']
        raca = request.form['raca']
        brinco = request.form['brinco']
        sexo = request.form['sexo']
        tempo_parto = request.form['tempo_parto']
        pasto = request.form['pasto']
        gasto_gestacao = request.form['gasto_gestacao']	
        gasto_vida = request.form['gasto_vida']
        crias = request.form['crias']
        tempo_entre_crias = request.form['tempo_entre_crias']
        complicacoes = request.form['complicacoes']
        vacinas = request.form['vacinas']
        if tempo_parto != 0:
            prenha = True
            
        x = Animal(peso , raca,brinco,sexo, prenha,tempo_parto , pasto , gasto_gestacao ,gasto_vida, crias, tempo_entre_crias, complicacoes, vacinas)
        x.cadastrar()
        flash("Vaca cadastrada com sucesso")
        return redirect("/cadastro_animais")
    return render_template("cadastro_animais.html")

@app.route('/detalhes_gado/<int:gado_id>', methods=['GET'])
def detalhes_gado(gado_id):
    # Use o gado_id para buscar os detalhes do gado no MongoDB
    # Substitua esta parte com as consultas reais ao banco de dados
    '''detalhes_gado = consulta_detalhes_gado_no_mongodb(gado_id)'''
    
    # Renderize um template para exibir os detalhes do gado
    return render_template('detalhes_gado.html', detalhes_gado=detalhes_gado)

app.run(debug=True)