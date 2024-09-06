def adicionar_tarefa(lista_tarefas, tarefa):
    """Adiciona uma nova tarefa à lista de tarefas."""
    lista_tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso.")

def listar_tarefas(lista_tarefas):
    """Lista todas as tarefas com seus índices."""
    if not lista_tarefas:
        print("Nenhuma tarefa para listar.")
    else:
        print("Tarefas:")
        for i, tarefa in enumerate(lista_tarefas):
            print(f"{i}. {tarefa}")

def remover_tarefa(lista_tarefas, indice):
    """Remove uma tarefa da lista pelo índice."""
    if 0 <= indice < len(lista_tarefas):
        tarefa_removida = lista_tarefas.pop(indice)
        print(f"Tarefa '{tarefa_removida}' removida com sucesso.")
    else:
        print("Índice inválido. Não há tarefa para remover.")

def main():
    tarefas = []
    while True:
        print("\n1. Adicionar Tarefa")
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
            try:
                indice = int(input("Digite o índice da tarefa a ser removida: "))
                remover_tarefa(tarefas, indice)
            except ValueError:
                print("Por favor, digite um número válido.")
        elif escolha == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")

if __name__ == "__main__":
    main()
