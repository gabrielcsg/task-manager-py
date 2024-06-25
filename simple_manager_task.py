def add_task(task_list, task_name):
    task = {
        "name": task_name,
        "completed": False
    }
    task_list.append(task)
    print(f"A tarefa {task_name} foi adicionada com sucesso")
    return


def list_tasks(task_list):
    print("\nLista de tarefas:")
    for index, task in enumerate(task_list, start=1):
        status = "✓" if task["completed"] else " "
        task_name = task["name"]
        print(f"{index}. [{status}] {task_name}")
    return


def update_task_name(task_list, task_index, task_name):
    fixed_index = int(task_index)-1
    if fixed_index >= 0 and fixed_index < len(task_list):
        task_list[fixed_index]['name'] = task_name
        print(f"Tarefa {task_index} atualizada com sucesso para {task_name}")
    else:
        print("Indice de tarefa inválido")
    return


def complete_task(task_list, task_index):
    fixed_index = int(task_index)-1
    if fixed_index >= 0 and fixed_index < len(task_list):
        task_list[fixed_index]['completed'] = True
        print(f"Tarefa {task_index} completada")
    else:
        print("Indice de tarefa inválido")
    return


def remove_completed_tasks(task_list):
    for task in task_list:
        if task["completed"]:
            task_list.remove(task)
    print("Tarefas completadas removidas com sucesso")
    return


tasks = []
while True:
    print("\nMenu do gerenciador de lista de tarefas")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    option = input("Digite sua escolha: ")

    if option == "1":
        task_name = input('Digite o nome da tarefa que deseja adicionar: ')
        add_task(tasks, task_name)
    elif option == "2":
        list_tasks(tasks)
    elif option == "3":
        list_tasks(tasks)
        selected_index = input(
            "Digite o número da tarefa que deseja atualizar o nome: ")
        name = input("Digite o novo nome da tarefa: ")
        update_task_name(tasks, selected_index, name)
    elif option == "4":
        list_tasks(tasks)
        selected_index = input(
            "Digite o número da tarefa que deseja finalizar: ")
        complete_task(tasks, selected_index)
    elif option == "6":
        break

print("Programa finalizado")
