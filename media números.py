qtde = 0
soma = 0
n = int(input("Digite um número: "))
while n != 0:
    soma += n
    qtde += 1
    n = int(input("Digite um número: "))

media = soma / qtde
print(media)