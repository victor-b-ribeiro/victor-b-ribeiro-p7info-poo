n = int(input('Número inteiro positivo: '))
soma = 0
conta = 0
num = 2
while conta < n:
    primo = True
    for i in range(2, num):
        if num % i == 0:
           primo = False
           break
    if primo:
        print(num)
        soma += num
        conta += 1
    num += 1

if (conta==n):
  print(soma)