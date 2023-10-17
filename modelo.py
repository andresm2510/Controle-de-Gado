from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient
from flask_login import UserMixin
import time

banco = MongoClient("mongodb+srv://andre:GpGIBvmocawfazxa@cluster0.egthg3z.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp")

database = banco['controledegado']

gado_collection = database['gado']
vaca_collection = database['vaca']
usuarios_collection = database['users']
fazenda_collection = database['fazenda']

''' talvez funcao para matar vacas'''

'''#so pra comecar
fazenda_collection.insert_one({'cabecasGado': 0 , 'vacasGestantes': 0 ,  'consumoRacao': 0, 'consultas': 0})
'''

gado_schema = {
    'peso': int,
    'racas': str,
    'brincos': int,
    'pastos': str,
    'dono': str,
}

vaca_schema = {
    'peso': int,
    'raca': str,
    'brinco': str,
    'sexo': bool,
    'prenha': bool,
    'tempo_parto': int,
    'pasto': int,
    'gasto_gestacao': float,
    'gasto_vida': float,
    'crias': int,
    'tempo_entre_crias': int,
    'complicações': str,
    'vacinas': bool,
}

usuarios_schema = {
    'Nome': str,
    'E-mail': str,
    'Senha': str,
}

gado_collection.create_index('brinco', unique=True)
vaca_collection.create_index('brinco', unique=True)
usuarios_collection.create_index('email', unique=True)

class Animal:
    def __init__ (self, peso, raca, brinco,sexo,prenha,tempo_parto, pasto, gasto_gestacao, gasto_vida, crias, tempo_entre_crias, complicacoes, vacinas):
        self.brinco = brinco
        self.raca = raca
        self.pasto = pasto 
        self.peso = peso
        self.sexo = sexo
        if sexo == 1:
            self.prenha = prenha
            self.tempo_parto = tempo_parto
            self.gasto_gestacao = gasto_gestacao
            self.crias = crias
            tempo_entre_crias = tempo_entre_crias
        
        else:
            self.prenha = 0
            self.tempo_parto = 0
            self.gasto_gestacao = 0
            self.crias = 0
            tempo_entre_crias = 0

        self.complicacoes = complicacoes
        self.gasto_vida = gasto_vida   
        self.vacinas = vacinas

    def atualizarPeso (self, peso):
        self.peso = peso

    def get_sexo(self):
        return self.sexo

    def mudarPasto (self, novoPasto):
        self.pasto = novoPasto

    def touro (self):
        self.sexo = 0

    def cadastrar(self):
        gado_collection.insert_one(self.__dict__)
        fazenda_collection.update_one({}, {'$inc': {'cabecasGado': 1}})
        if self.sexo == 1:
            Vaca.cadastrar(self)
        

class Vaca(Animal):
    def __init__ (self, peso, raca, brinco,sexo,prenha,tempo_parto, pasto, gasto_gestacao, gasto_vida, crias, tempo_entre_crias, complicacoes, vacinas ):
        super().__init__(self, peso, raca, brinco,sexo,prenha,tempo_parto, pasto, gasto_gestacao, gasto_vida, crias, tempo_entre_crias, complicacoes, vacinas)
        self.dataCrias = []
        
    def novaGestação (self, dataCrias):
        self.dataCrias.append(dataCrias)
    
    def get_self(self , brinco):
        return gado_collection.find_one({'_id': brinco})
    
    def cadastrar(self):
        vaca_collection.insert_one(self.__dict__)
        if self.prenha == 1:
            fazenda_collection.update_one({}, {'$inc': {'vacasGestantes': 1}})

    def vizualizarVacas(brinco):
        x= vaca_collection.find_one({'brinco': brinco})
        if x is not None:
            peso = x['peso']
            raca = x['raca']
            brinco = x['brinco']
            sexo = x['sexo']
            tempo_prenha = x['prenha']
            tempo_parto = x['tempo_parto']
            pasto = x['pasto']
            gasto_gestação = x['gasto_gestacao']
            gasto_vida = x['gasto_vida']
            crias = x['crias']
            tempo_entre_crias = x['tempo_entre_crias']
            complicações = x['complicacoes']
            vacinas = x['vacinas']
            
            return (peso, raca, brinco, sexo, tempo_prenha, tempo_parto, pasto, gasto_gestação, gasto_vida, crias, tempo_entre_crias, complicações, vacinas)
        

class Usuario:
    def __init__ (self, nome, email, senha):
    
        self.nome = nome
        self.email = email
        self.senha = generate_password_hash(senha)
    

    def cadastrar(self):
        
        
        
        usuarios_collection.insert_one({'nome': self.nome, 'email': self.email, 'senha': self.senha})

        
        '''usuarios_collection.insert_one(self.__dict__)'''
    
    def get_user( self):
        a=  usuarios_collection.find_one({'email': self.email})
        b= a['nome']
        return b
    

    def loginuser(email, senha): 
        x= usuarios_collection.find_one({'email': email})
        if x is not None:
            print(email, 'ok')
    
            s = x['senha']
            s1 = check_password_hash(s, senha)
            if x and s1:
                print(senha ,'ok')
          
                return True
            else:
                return False

        else:
            print('erro no email')
            return False    

def retornaFazenda():
    x = fazenda_collection.find_one({})
    cabecasGado = x['cabecasGado']
    vacasGestantes = x['vacasGestantes']
    consumoRacao = x['consumoRacao']
    consultas = x['consultas']
    return (cabecasGado, vacasGestantes, consumoRacao, consultas)


'''teste database
x=Animal(1, 'Holandesa', 'Pasto 1')
x.atualizarPeso(500)
x.cadastrar()
'''


'''
class Touro(Animal):
    def __init__ (self, _id, raca, pasto, ):
        super().__init__(self, _id, raca, pasto)
        self.dataCobertura = []
        
    def novaCobertura (self, dataCobertura):
        self.dataCobertura.append(dataCobertura)

'''