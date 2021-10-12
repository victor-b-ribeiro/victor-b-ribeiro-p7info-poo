class Ponto():
    def __init__(self, x , y):
        self.x = x
        self.y = y
    def setX(self,atualizado):
        self.x = atualizado
    def setY(self,atualizado):
        self.y = atualizado
    def getX(self):
        return self.x
    def getY(self):
        return self.y
class Reta():
    def __init__(self,ponto1,ponto2):
        self.ponto1 = ponto1
        self.ponto2 = ponto2
    def setPonto1(self,atualizado):
        self.ponto1 = atualizado
    def setPonto2(self,atualizado):
        self.ponto2 = atualizado
    def getPonto1(self):
        return self.ponto1
    def getPonto2(self):
        return self.ponto2
    def distancia(self):
        componenteX = (self.getPonto2().getX() - self.getPonto1().getX()) **2
        componenteY = (self.getPonto2().getY() - self.getPonto1().getY()) **2
        resultado = (componenteX + componenteY)/2

        return resultado

ponto1 = Ponto(0,1)
ponto2 = Ponto(8,1)

reta = Reta(ponto1,ponto2) 

print("Distância:", reta.distancia())