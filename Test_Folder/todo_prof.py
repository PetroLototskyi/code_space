import os

# File to store tasks
file_name = "tasks.txt"

# Load tasks from file
def load_tasks():
    tasks = []
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            for line in file:
                task, status = line.strip().split(' | ')
                tasks.append({"task": task, "done": status == "Done"})
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(file_name, 'w') as file:
        for task in tasks:
            status = "Done" if task["done"] else "Pending"
            file.write(f"{task['task']} | {status}\n")

# Display all tasks
def show_tasks(tasks, only_pending=False):
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks, start=1):
        if only_pending and task["done"]:
            continue
        status = "✓" if task["done"] else "✗"
        print(f"{i}. {task['task']} [{status}]")

# Add a new task
def add_task(tasks):
    task_text = input("Enter the new task: ")
    tasks.append({"task": task_text, "done": False})
    print(f"Task '{task_text}' added!")

# Mark a task as done
def mark_done(tasks):
    show_tasks(tasks, only_pending=True)
    try:
        task_num = int(input("Enter the task number to mark as done: "))
        if 1 <= task_num <= len(tasks) and not tasks[task_num - 1]["done"]:
            tasks[task_num - 1]["done"] = True
            print(f"Task '{tasks[task_num - 1]['task']}' marked as done!")
        else:
            print("Invalid task number or task already completed.")
    except ValueError:
        print("Please enter a valid number.")

# Main program loop
def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Show all tasks")
        print("2. Show pending tasks")
        print("3. Add a task")
        print("4. Mark a task as done")
        print("5. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            show_tasks(tasks, only_pending=True)
        elif choice == "3":
            add_task(tasks)
        elif choice == "4":
            mark_done(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the program
if __name__ == "__main__":
    main()
