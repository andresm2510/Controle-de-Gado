from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient
from flask_login import UserMixin
import time

banco = MongoClient("mongodb+srv://andre:GpGIBvmocawfazxa@cluster0.egthg3z.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp")

database = banco['controledegado']

gado_collection = database['gado']
vaca_collection = database['vaca']
usuarios_collection = database['usuarios']


gado_schema = {
    'Peso': int,
    'Raças': str,
    'Brincos': str,
    'Pastos': str,
    'Dono': str,
}

vaca_schema = {
    'Peso': int,
    'Peso1': int,
    'Peso2': int,
    'Peso3': int,
    'Raça': str,
    'Brinco': str,
    'Macho ou fêmea': bool,
    'Tempo prenha': int,
    'Tempo para parir': int,
    'Qual pasto está': int,
    'Qual touro está no pasto': str,
    'Qual o gasto total nessa gestação': float,
    'Qual o gasto total na vida': float,
    'Quantas crias já teve': int,
    'Tempo entre crias': int,
    'Complicações': str,
    'Vacinas': [str],
}

usuarios_schema = {
    'Nome': str,
    'E-mail': str,
    'Senha': str,
}

gado_collection.create_index('Brinco', unique=True)
vaca_collection.create_index('Brinco', unique=True)
usuarios_collection.create_index('E-mail', unique=True)
                                 
class Animal:
    def __init__ (self, _id, brinco, raça, pasto):
        self._id = _id
        self.brinco = brinco
        self.raça = raça
        self.pasto = pasto 
        self.peso = 0
        self.estado = 0 #0 = normal, se for gestante atualizaremos para 1 
        self.sexo = 1 # 1 = femea, 0 = macho

    def atualizarPeso (self, peso):
        self.peso = peso

    def mudarPasto (self, novoPasto):
        self.pasto = novoPasto

    def touro (self):
        self.sexo = 0

    def cadastrar(self,peso):
        self.peso = peso
        gado_collection.insert_one(self.__dict__)
        if self.sexo == 1:
            Vaca(self._id, self.raça, self.pasto).cadastrar()
        
        '''if self.sexo == 0:
            Touro(self._id, self.raça, self.pasto).cadastrar()'''


class Vaca(Animal):
    def __init__ (self, _id, raça, pasto, ):
        super().__init__(self, _id, raça, pasto)
        self.dataCrias = []
        
    def novaGestação (self, dataCrias):
        self.dataCrias.append(dataCrias)
    
    def get_self(self , _id):
        return gado_collection.find_one({'_id': _id})
    
    def cadastrar(self):
        get_self = gado_collection.find_one({'_id': self._id})################ Isso ta meio inutil
        vaca_collection.insert_one(self.__dict__)

    def vizualizarVacas(self,brinco):
        x= vaca_collection.find_one({'_id': brinco})
        data= x['dataCrias']
        peso = x['peso']
        pasto = x['pasto']

        return (data, peso, pasto)

    

class Usuario(UserMixin):
    def __init__ (self, nome, email, senha):
    
        self.nome = nome
        self.email = email
        self.senha = generate_password_hash(senha)
    

    def cadastrar(self):
        usuarios_collection.insert_one(self.__dict__)
    
    def get_user( email):
       a=  usuarios_collection.find_one({'email': email})
       return a
    

    def loginuser(email, senha): 
        x= usuarios_collection.find_one({'email': email})
        if x is not None:
            print('email ok')
            time.sleep(20)
            s = x['senha']
            s1 = check_password_hash(s, senha)
            if x and s1:
                print('senha ok')
                time.sleep(20)
                return True
            else:
                return False

        else:
            print('erro no email')
            return False    




'''teste database
x=Animal(1, 'Holandesa', 'Pasto 1')
x.atualizarPeso(500)
x.cadastrar()
'''


'''
class Touro(Animal):
    def __init__ (self, _id, raça, pasto, ):
        super().__init__(self, _id, raça, pasto)
        self.dataCobertura = []
        
    def novaCobertura (self, dataCobertura):
        self.dataCobertura.append(dataCobertura)

'''