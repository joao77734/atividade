print("=== SISTEMA BANCÁRIO ===")

nome = input("Digite o nome do cliente: ")

while True:
    try:
        saldo = float(input("Digite o saldo inicial: R$ "))

        if saldo < 0:
            print("O saldo não pode ser negativo.")
        else:
            break

    except ValueError:
        print("Digite apenas números.")
quantidade_operacoes = 0
extrato = []
while True:

    print("\n=== MENU ===")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Consultar saldo")
    print("4 - Mostrar extrato")
    print("5 - Encerrar sistema")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        try:
            valor = float(input("Digite o valor do depósito: R$ "))

            if valor <= 0:
                print("O valor deve ser positivo.")

            else:
                saldo += valor
                quantidade_operacoes += 1
                extrato.append(f"Depósito: +R$ {valor:.2f}")

                print("Depósito realizado com sucesso!")

        except ValueError:
            print("Digite apenas números.")
    elif opcao == "2":
        try:
            valor = float(input("Digite o valor do saque: R$ "))

            if valor <= 0:
                print("O valor deve ser positivo.")

            elif valor > saldo:
                print("Saldo insuficiente.")

            else:
                saldo -= valor
                quantidade_operacoes += 1
                extrato.append(f"Saque: -R$ {valor:.2f}")

                print("Saque realizado com sucesso!")

        except ValueError:
            print("Digite apenas números.")
    elif opcao == "3":
        print(f"\nSaldo atual: R$ {saldo:.2f}")
    elif opcao == "4":
        print("\n=== EXTRATO ===")

        if len(extrato) == 0:
            print("Nenhuma movimentação realizada.")

        else:
            for movimentacao in extrato:
                print(movimentacao)

        print(f"\nTotal de operações: {quantidade_operacoes}")
    elif opcao == "5":
        print(f"\nSistema encerrado. Até logo, {nome}!")
        break
    else:
        print("Opção inválida.")