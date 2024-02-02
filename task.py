from datetime import datetime, timedelta

class TodoList:
    def _init_(self):
        self.tasks = []

    def add_task(self, task, deadline=None):
        task_info = {"task": task, "completed": False, "deadline": deadline}
        self.tasks.append(task_info)
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
                deadline = task.get("deadline", "No deadline")
                print(f"{i}. {task['task']} - {status} - Deadline: {deadline}")

    def upcoming_tasks(self):
        now = datetime.now()
        upcoming_tasks = [task for task in self.tasks if task.get("deadline") and task["deadline"] > now]
        if not upcoming_tasks:
            print("No upcoming tasks.")
        else:
            print("Upcoming Tasks:")
            for i, task in enumerate(upcoming_tasks):
                print(f"{i}. {task['task']} - Deadline: {task['deadline']}")
