class Veiculo():
    def _init_(self, cor, rodas, marca):
       self.cor = cor
       self.rodas = rodas
       self.marca= marca
    def printar(self):
        print("Cor:", self.cor)
        print("Rodas:", self.rodas)
        print("Marca:", self.marca)

class Moto(Veiculo):
    def _init_(self, cor, rodas, marca, tamanho):
        super(Moto, self)._init_(cor, rodas, marca)
        self.tamanho = tamanho

    def printar(self):  # Polimorfismo
        super(Moto,self).printar()
        print("Tamanho:", self.tamanho)
        
moto1 = Moto("Azul","2","Yamaha","2")