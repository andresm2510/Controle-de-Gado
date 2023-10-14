class Animal:
    def __init__ (self, _id, raça, pasto):
        self._id = _id
        self.raça = raça
        self.pasto = pasto 
        self.peso = []

    def atualizarPeso (self, peso):
        self.peso.append(peso)

    def mudarPasto (self, novoPasto):
        self.pasto = novoPasto

    

class Vaca(Animal):
    def __init__ (self, _id, raça, pasto, ):
        super(). __init__(self, _id, raça, pasto)
        self.dataCrias = []
        
    def novaGestação (self, dataCrias):
        self.dataCrias.append(dataCrias)
