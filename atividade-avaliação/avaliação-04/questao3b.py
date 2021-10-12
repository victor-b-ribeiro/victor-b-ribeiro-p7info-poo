class Bilas():
    def _init_(self,num_Bilas):
       self._num_Bilas = num_Bilas

    def perder(self,quantidade):
        self._num_Bilas -= quantidade

    def ganhar(self,quantidade):
        self._quantidade += quantidade
    
    def getNum_Bilas(self):
        return self._num_Bilas

    def setNum_Bilas(self, atualizado):
        self._num_Bilas = atualizado

juninho = Bilas(50)

juninho.ganhar(10)
print(juninho.getNum_Bilas())

juninho.perder(5)
print(juninho.getNum_Bilas())
