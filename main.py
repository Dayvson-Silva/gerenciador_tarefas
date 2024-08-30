# gerenciamento_tarefas.py

def adicionar_tarefa(lista_tarefas, tarefa):
    """Adiciona uma nova tarefa à lista de tarefas."""
    # Implementar a função aqui

def listar_tarefas(lista_tarefas):
    """Lista todas as tarefas com seus índices."""
    # Implementar a função aqui

def remover_tarefa(lista_tarefas, indice):
    """Remove uma tarefa da lista pelo índice."""
    # Implementar a função aqui

def main():
    tarefas = []
    while True:
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Remover Tarefa")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            tarefa = input("Digite a tarefa: ")
            adicionar_tarefa(tarefas, tarefa)
        elif escolha == "2":
            listar_tarefas(tarefas)
        elif escolha == "3":
            indice = int(input("Digite o índice da tarefa a ser removida: "))
            remover_tarefa(tarefas, indice)
        elif escolha == "4":
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()



print('ola, mundo')