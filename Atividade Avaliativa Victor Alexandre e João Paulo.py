lista_produto = [["Maça",19.90,"0123"],["Banana",2.90,"1234"],["Pera",8.90,"123234"]]

atualizar_produto = True

#nome_do_produto ; valor_do_produto ; codigo_do_produto

if atualizar_produto == True:


    while atualizar_produto == True:

        print("====================================================================")
        print("                     ATUALIZANDO PRODUTOS                           ")
        print("====================================================================")
        print("Quantidade de produtos: ")
        print(len(lista_produto))
        print("====================================================================\n")

        for i, produto in enumerate(lista_produto):
            print(f"{i} - Nome: {produto[0]}, Preço:R$ {produto[1]},Código:{produto[2]}")

        indice = int(input("Digite o número do produto que deseja atualizar: "))

        print("1- Nome")
        print("2- Preço")
        print("1- Código")

        opcao = input("O que deseja atualizar?")

        if opcao == "1":
            novo_nome = input("Novo Nome:")
            lista_produto[indice][0] = novo_nome
        elif opcao == "2":
            novo_preco = float(input("Novo Preço:"))
            lista_produto[indice][1] = novo_preco
        elif opcao == "3":
            novo_codigo = input("Novo Código:")
            lista_produto[indice][2] = novo_codigo

        else:
            print("Opção inválida")
        print("Produto Atualizado!")