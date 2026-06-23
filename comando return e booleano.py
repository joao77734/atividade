def par(x):
    if(x%2)==0:
        return True
    else:
        return False
    
while True:
    num = int(input("Digite um número: "))
    if par(num):
        print("É par")
    else:
        print("É impar")
#comando simplificado para saber se um número é par ou ímpar