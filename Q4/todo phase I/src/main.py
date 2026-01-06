from todo import Todo
from utils import print_line

def show_menu():
    print_line()
    print("Todo App")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Complete / Incomplete")
    print("6. Exit")
    print_line()

def main():
    todo = Todo()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo.add_task(title, description)

        elif choice == "2":
            todo.view_tasks()

        elif choice == "3":
            task_id = int(input("Enter task ID: "))
            new_title = input("Enter new title: ")
            new_description = input("Enter new description: ")
            todo.update_task(task_id, new_title, new_description)

        elif choice == "4":
            task_id = int(input("Enter task ID: "))
            todo.delete_task(task_id)

        elif choice == "5":
            task_id = int(input("Enter task ID: "))
            status = input("Mark complete? (yes/no): ").lower()
            completed = True if status == "yes" else False
            todo.mark_task(task_id, completed)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
