class pilha:
    def __init__(self):
        self.itens = list()
    def adicionar(self,adicionado):
        self.itens.append(adicionado)
    def remover(self):
        del self.itens[-1]
    def printpilha(self):
        print(*self.itens)
# Criando lista
pilhaTeste = pilha()
# Adicionando itens
print("Adicionando item: \n")
pilhaTeste.adicionar("Trigo")
pilhaTeste.adicionar("Joio")
pilhaTeste.printpilha()
# Removendo item
pilhaTeste.remover()
print("Removendo item: \n")
pilhaTeste.printpilha()


