opcao = "s"

while opcao == "s":

    try:
        print("\n===== VENDA DE INGRESSOS =====")
        nome = input("Digite o nome do cliente: ")

        print("\nTipos de ingresso:")
        print("Pista: R$ 50")
        print("VIP: R$ 120")
        print("Camarote: R$ 250")

        tipo = input("Escolha o tipo de ingresso: ").lower()

        quantidade = int(input("Digite a quantidade de ingressos: "))

        if tipo == "pista":
            valor = 50

        elif tipo == "vip":
            valor = 120

        elif tipo == "camarote":
            valor = 250

        else:
            print("Tipo de ingresso inválido!")
            continue

        if quantidade <= 0:
            print("Quantidade inválida!")
            continue
        total = valor * quantidade
        print("\n===== RESUMO DA COMPRA =====")
        print("Cliente:", nome)
        print("Ingresso:", tipo)
        print("Quantidade:", quantidade)
        print("Valor total: R$", total)

    except ValueError:
        print("Erro: digite um número válido!")
    opcao = input("\nDeseja fazer outra compra? (s/n): ").lower()

print("\nSistema encerrado.")