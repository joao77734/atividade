clientes = []

while True:
    print("\n--- Sistema de Clientes ---")
    print("1 - Cadastrar cliente")
    print("2 - Consultar cliente")
    print("3 - Excluir cliente")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do cliente: ")
        clientes.append(nome)
        print("Cliente cadastrado com sucesso!")

    elif opcao == "2":
        if len(clientes) == 0:
            print("Nenhum cliente cadastrado.")
        else:
            indice = int(input("Digite o índice do cliente: "))
            if 0 <= indice < len(clientes):
                print("Cliente:", clientes[indice])
            else:
                print("Índice inválido.")

    elif opcao == "3":
        if len(clientes) == 0:
            print("Nenhum cliente para excluir.")
        else:
            indice = int(input("Digite o índice do cliente para excluir: "))
            if 0 <= indice < len(clientes):
                removido = clientes.pop(indice)
                print(f"Cliente '{removido}' removido com sucesso!")
            else:
                print("Índice inválido.")

    elif opcao == "4":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida, tente novamente.")