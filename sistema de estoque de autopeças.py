pecas = []
opcao = 0

while opcao != 5:
    print("\n=====Controle de Estoque=====")
    print("1 -  Cadastrar Peça")
    print("2 - Listar Estoque")
    print("3 - Realizar Venda")
    print("4 - Repor Estoque")
    print("5 - Encerrar Sistema")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = str (input("Digite o nome da peça: "))
        codigo = str (input("Digite o código da peça: "))
        quantidade = int(input("Digite a quantidade em estoque: "))
        valor = float(input("Digite o valor: "))

        produto = {"nome": nome, "codigo": codigo, "quantidade": quantidade, "valor":valor}
        pecas.append(produto)

        print("Peça cadastrada com sucesso!")

    elif opcao == 2:
        if len (pecas)==0:
            print("Nenhuma peça cadastrada.")
        else:
            print("\n=====Estoque=====")

            for produto in pecas:

                print("Nome", produto["nome"])
                print("Código",codigo["codigo"])
                print("Quantidade",quantidade["quantidade"])
                print("Valor",valor["valor"])

    elif opcao == 3:
        codigo_venda = input("Digite o código da peça: ")

        encontrado = False

        for produto in pecas:

            if produto["codigo"] == codigo_venda:

                encontrado = True

            quantidade_venda = int(input("Digite a quantidade da venda: "))

            if quantidade_venda > produto["quantidade"]:
                        print("Estoque insuficiente!")

            elif quantidade_venda <= 0:
                        print("Quantidade inválida!")

            else:
                produto["quantidade"] = produto["quantidade"] - quantidade_venda

                total = quantidade_venda * produto["valor"]
                print("Venda Realizada com sucesso!")
                print("Valor total:",total,"R$")
    elif opcao == 4:

            codigo_repor = input("Digite o código da peça: ")

            encontrado = False

            for produto in pecas:

                if produto["codigo"] == codigo_repor:

                    encontrado = True

                    reposicao = int(input("Digite a quantidade para reposição: "))

                    if reposicao <= 0:
                        print("Quantidade inválida!")

                    else:
                        produto["quantidade"] = produto["quantidade"] + reposicao

                        print("Estoque atualizado com sucesso!")

            if encontrado == False:
                print("Peça não encontrada.")

    elif opcao == 5:
            print("Sistema encerrado.")

    else:
            print("Opção inválida!")

