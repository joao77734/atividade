destinos = []
qtd = int(input("Quantos destinos deseja cadastrar? "))

for i in range(qtd):
    nome = input("Nome do destino: ")
    valor = float(input("Valor da passagem: "))
    vagas = int(input("Quantidade de vagas: "))

    destino = {
        "nome": nome,
        "valor": valor,
        "vagas": vagas
    }

    destinos.append(destino)

while True:
    print("\n--- AGÊNCIA DE VIAGENS ---")
    print("1 - Listar destinos")
    print("2 - Comprar passagem")
    print("3 - Consultar vagas")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        for i, d in enumerate(destinos):
            print(f"{i + 1} - {d['nome']} | R$ {d['valor']} | Vagas: {d['vagas']}")
    elif opcao == "2":
        numero = int(input("Digite o número do destino: "))

        if numero > 0 and numero <= len(destinos):
            destino = destinos[numero - 1]

            if destino["vagas"] > 0:
                destino["vagas"] -= 1
                print("Passagem comprada com sucesso!")
            else:
                print("Sem vagas disponíveis.")
        else:
            print("Destino inválido.")
    elif opcao == "3":
        for d in destinos:
            print(f"{d['nome']} possui {d['vagas']} vagas.")
    elif opcao == "4":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")