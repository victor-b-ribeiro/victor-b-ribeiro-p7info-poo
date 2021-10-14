
char = "-"
maior = ""
aux = 0

while True:
    print("Digite 0 para fechar o programa")
    print("Digite uma frase:")
    frase = input().split()
    tamanho_palavras = []
    if frase == ["0"]:
       print("Programa encerrado. Obrigado")
       break
    for i in frase:
        tamanho_palavras.append(str(len(i)))
        if len(i) >= aux:
            aux = len(i)
            maior = i
    print(char.join(tamanho_palavras))
    print("Maior palavra é: {}".format(maior))

