from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient

banco = MongoClient("mongodb+srv://andre:GpGIBvmocawfazxa@cluster0.egthg3z.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp")
db= banco['ControleGado']
collection = db['Gado']
collection2=['Vacas']
collection3=['usuarios']

class Animal:
    def __init__ (self, _id, raça, pasto):
        self._id = _id
        self.raça = raça
        self.pasto = pasto 
        self.peso = 0

    def atualizarPeso (self, peso):
        self.peso = peso

    def mudarPasto (self, novoPasto):
        self.pasto = novoPasto

    def cadastrar(self):
        collection.insert_one(self.__dict__)


class Vaca(Animal):
    def __init__ (self, _id, raça, pasto, ):
        super().__init__(self, _id, raça, pasto)
        self.dataCrias = []
        
    def novaGestação (self, dataCrias):
        self.dataCrias.append(dataCrias)
    pass

class Usuario:
    def __init__ (self, _id, nome, email, senha):
        self._id = _id
        self.nome = nome
        self.email = email
        self.senha = generate_password_hash(senha)

    def cadastrar(self):
        collection3.insert_one(self.__dict__)

    def login(self, nome, senha): 
        x= collection3.find_one({'nome': nome})
        if x and check_password_hash(x['senha'], senha):
              return True
        
        else:
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