class Todo:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title, description):
        task = {
            "id": self.next_id,
            "title": title,
            "description": description,
            "completed": False
        }
        self.tasks.append(task)
        self.next_id += 1
        print("Task added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return

        for task in self.tasks:
            status = "✔" if task["completed"] else "✘"
            print(f'ID: {task["id"]} | {status}')
            print(f'Title: {task["title"]}')
            print(f'Description: {task["description"]}')
            print()

    def update_task(self, task_id, new_title, new_description):
        for task in self.tasks:
            if task["id"] == task_id:
                task["title"] = new_title
                task["description"] = new_description
                print("Task updated successfully.")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                print("Task deleted successfully.")
                return
        print("Task not found.")

    def mark_task(self, task_id, completed):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = completed
                print("Task status updated.")
                return
        print("Task not found.")
