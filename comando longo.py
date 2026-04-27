# sistema_tarefas.py

import json
import os
from datetime import datetime

ARQUIVO = "tarefas.json"


class Tarefa:
    def __init__(self, titulo, descricao, prioridade, concluida=False, data=None):
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.concluida = concluida
        self.data = data if data else datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def concluir(self):
        self.concluida = True

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(d):
        return Tarefa(**d)


class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []
        self.carregar()

    def adicionar(self, tarefa):
        self.tarefas.append(tarefa)
        self.salvar()

    def listar(self):
        if not self.tarefas:
            print("Nenhuma tarefa.")
            return

        for i, t in enumerate(self.tarefas):
            status = "✔" if t.concluida else "✘"
            print(f"{i} - [{status}] {t.titulo} (Prioridade: {t.prioridade})")

    def detalhes(self, indice):
        try:
            t = self.tarefas[indice]
            print("\n--- DETALHES ---")
            print(f"Título: {t.titulo}")
            print(f"Descrição: {t.descricao}")
            print(f"Prioridade: {t.prioridade}")
            print(f"Concluída: {t.concluida}")
            print(f"Criada em: {t.data}")
        except IndexError:
            print("Índice inválido.")

    def concluir(self, indice):
        try:
            self.tarefas[indice].concluir()
            self.salvar()
            print("Tarefa concluída.")
        except IndexError:
            print("Índice inválido.")

    def remover(self, indice):
        try:
            del self.tarefas[indice]
            self.salvar()
            print("Tarefa removida.")
        except IndexError:
            print("Índice inválido.")

    def salvar(self):
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in self.tarefas], f, indent=4)

    def carregar(self):
        if not os.path.exists(ARQUIVO):
            return
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            dados = json.load(f)
            self.tarefas = [Tarefa.from_dict(d) for d in dados]

    def relatorio(self):
        total = len(self.tarefas)
        concluidas = sum(1 for t in self.tarefas if t.concluida)
        pendentes = total - concluidas

        print("\n--- RELATÓRIO ---")
        print(f"Total: {total}")
        print(f"Concluídas: {concluidas}")
        print(f"Pendentes: {pendentes}")

        prioridades = {}
        for t in self.tarefas:
            prioridades[t.prioridade] = prioridades.get(t.prioridade, 0) + 1

        print("\nPor prioridade:")
        for p, q in prioridades.items():
            print(f"{p}: {q}")


def menu():
    print("""
1 - Adicionar tarefa
2 - Listar tarefas
3 - Ver detalhes
4 - Concluir tarefa
5 - Remover tarefa
6 - Relatório
0 - Sair
""")


def main():
    sistema = GerenciadorTarefas()

    while True:
        menu()
        opcao = input("Escolha: ")

        if opcao == "1":
            titulo = input("Título: ")
            descricao = input("Descrição: ")
            prioridade = input("Prioridade (baixa/média/alta): ")
            sistema.adicionar(Tarefa(titulo, descricao, prioridade))

        elif opcao == "2":
            sistema.listar()

        elif opcao == "3":
            i = int(input("Índice: "))
            sistema.detalhes(i)

        elif opcao == "4":
            i = int(input("Índice: "))
            sistema.concluir(i)

        elif opcao == "5":
            i = int(input("Índice: "))
            sistema.remover(i)

        elif opcao == "6":
            sistema.relatorio()

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()