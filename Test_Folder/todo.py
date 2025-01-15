tasks = []
while True:
    command = input("Add/Show/Exit: ").lower()
    if command == 'add':
        tasks.append(input("Enter task: "))
    elif command == 'show':
        print("\n".join(tasks))
    elif command == 'exit':
        break