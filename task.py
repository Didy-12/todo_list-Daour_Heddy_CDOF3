class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print("Task added successfully.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            print("Task deleted successfully.")
        else:
            print("Invalid index. No task deleted.")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid index. No task marked as completed.")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks):
                status = "Completed" if task["completed"] else "Not Completed"
                print(f"{i}. {task['task']} - {status}")
