alunos = []

opcao = 0

while opcao != 4:

    print("\n===== SISTEMA ESCOLAR =====")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Consultar situação")
    print("4 - Encerrar sistema")

    try:
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:

            nome = input("Digite o nome do aluno: ")

            nota1 = float(input("Digite a nota 1: "))
            nota2 = float(input("Digite a nota 2: "))

            if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10:
                print("Notas inválidas! Digite valores entre 0 e 10.")
                continue

            media = (nota1 + nota2) / 2

            if media >= 7:
                situacao = "Aprovado"

            elif media >= 5:
                situacao = "Recuperação"

            else:
                situacao = "Reprovado"
            aluno = {
                "nome": nome,
                "nota1": nota1,
                "nota2": nota2,
                "media": media,
                "situacao": situacao
            }

            alunos.append(aluno)

            print("Aluno cadastrado com sucesso!")

        elif opcao == 2:

            if len(alunos) == 0:
                print("Nenhum aluno cadastrado.")

            else:
                print("\n===== LISTA DE ALUNOS =====")

                for aluno in alunos:
                    print("Nome:", aluno["nome"])
                    print("Média:", aluno["media"])
                    print("Situação:", aluno["situacao"])
                    print("-------------------")
        elif opcao == 3:

            busca = input("Digite o nome do aluno: ")

            encontrado = False

            for aluno in alunos:

                if aluno["nome"].lower() == busca.lower():

                    print("\n===== DADOS DO ALUNO =====")
                    print("Nome:", aluno["nome"])
                    print("Nota 1:", aluno["nota1"])
                    print("Nota 2:", aluno["nota2"])
                    print("Média:", aluno["media"])
                    print("Situação:", aluno["situacao"])

                    encontrado = True

            if encontrado == False:
                print("Aluno não encontrado.")
        elif opcao == 4:
            print("Sistema encerrado.")

        else:
            print("Opção inválida!")

    except ValueError:
        print("Erro: digite um valor válido!")