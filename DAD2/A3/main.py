class No:
    def __init__(self, tarefa):
        self.tarefa = tarefa
        self.proximo = None

class ListaDeTarefas:
    def __init__(self):
        self.cabeca = None

    def adicionar_tarefa(self, tarefa):
        novo_no = No(tarefa)
        if self.cabeca is None:
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no

    def remover_tarefa(self, tarefa):
        atual = self.cabeca
        anterior = None
        while atual:
            if atual.tarefa == tarefa:
                if anterior:
                    anterior.proximo = atual.proximo
                else:
                    self.cabeca = atual.proximo
                return True
            anterior = atual
            atual = atual.proximo
        return False

    def listar_tarefas(self):
        atual = self.cabeca
        tarefas = []
        while atual:
            tarefas.append(atual.tarefa)
            atual = atual.proximo
        return tarefas

if __name__ == "__main__":
    lista_de_tarefas = ListaDeTarefas()

    while True:
        print("\nLista de Tarefas:")
        tarefas = lista_de_tarefas.listar_tarefas()
        if not tarefas:
            print("Nenhuma tarefa na lista.")
        else:
            for i, tarefa in enumerate(tarefas):
                print(f"{i + 1}. {tarefa}")

        print("\nOpções:")
        print("1. Adicionar Tarefa")
        print("2. Remover Tarefa")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            tarefa = input("Digite a tarefa a ser adicionada: ")
            lista_de_tarefas.adicionar_tarefa(tarefa)
            print(f"Tarefa '{tarefa}' adicionada à lista.")

        elif escolha == "2":
            tarefa = input("Digite a tarefa a ser removida: ")
            if lista_de_tarefas.remover_tarefa(tarefa):
                print(f"Tarefa '{tarefa}' removida da lista.")
            else:
                print(f"Tarefa '{tarefa}' não encontrada na lista.")

        elif escolha == "3":
            print("Saindo da aplicação.")
            break

        else:
            print("Opção inválida. Tente novamente.")