print ("Calculadora Complexa")
opcao = 0
while opcao!=5:

    opcao=int(input("Digite sua opção: \n 1. Adição \n 2. Subtração \n 3. Multiplicação \n 4. Divisão \n"))
    if opcao ==1:
        print ("1. Adição")
        n1 = float(input("Insira um valor que gostaria de somar: "))
        n2 = float(input("Insira outro valor que gostaria de somar: "))
        total = n1+n2
        print("total = ", total)
    elif opcao ==2:
        print ("2. Subtração")
        n1 = float(input("Insira um valor que gostaria de subtrair: "))
        n2 = float(input("Insira outro valor que gostaria de subtrair: "))
        total = n1-n2
        print ("total: ", total)
    elif opcao ==3:
        print ("3. Multiplicação")
        n1 = float(input("Insira um valor que gostaria de multiplicar: "))
        n2 = float(input("Insira outro valor que gostaria de multiplicar: "))
        total = n1*n2
        print ("Total: ", total)
    elif opcao ==4:
        print ("4. Divisão")
        n1 = float(input("Insira um valor que gostaria de dividir: "))
        n2 = float(input("Insira outro valor que gostaria de dividir: "))
        total = n1/n2
        print ("Total: ", total)
    elif opcao ==0:
        print("Finalizando programa")
        break
    
    