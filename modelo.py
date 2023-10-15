from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient

banco = MongoClient("mongodb+srv://andre:GpGIBvmocawfazxa@cluster0.egthg3z.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp")
db= banco['ControleGado']
collection = db['Gado']
collection2= db['Vacas']
collection3= db['usuarios']

class Animal:
    def __init__ (self, _id, raça, pasto):
        self._id = _id
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
        collection.insert_one(self.__dict__)
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
        return collection.find_one({'_id': _id})
    
    def cadastrar(self):
        get_self = collection.find_one({'_id': self._id})################
        collection2.insert_one(self.__dict__)

    def vizualizarVacas(self,brinco):
        x= collection2.find_one({'_id': brinco})
        data= x['dataCrias']
        peso = x['peso']
        pasto = x['pasto']

        return (data, peso, pasto)

    

class Usuario:
    def __init__ (self, nome, email, senha):
    
        self.nome = nome
        self.email = email
        self.senha = generate_password_hash(senha)

    def cadastrar(self):
        collection3.insert_one(self.__dict__)
    
    def get_id(self):
        return str(self._id)


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