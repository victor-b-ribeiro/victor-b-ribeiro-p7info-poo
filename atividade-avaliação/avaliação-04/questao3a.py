class Roupa():
    def _init_(self, tecido, cor, tipo):
       self.tecido = tecido
       self.cor = cor
       self.tipo = tipo
    def printar(self):
        print("Tecido:", self.tecido)
        print("Cor:", self.cor)
        print("Tipo:", self.tipo)

class Batina(Roupa):
    def _init_(self, tecido, cor, tipo, botoes):
        super(Batina, self)._init_(tecido, cor, tipo)
        self.botoes = botoes

    def printar(self):
        super(Batina,self).printar()
        print("Botões:", self.botoes)
        
batina_do_joão = Batina("Gabardine","Preta","Talar","33")
batina_do_joão.printar()