from task import TodoList
from datetime import datetime

def main():
    todo_list = TodoList()

    while True:
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Complete Task")
        print("4. Show Tasks")
        print("5. Upcoming Tasks")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            task = input("Enter the task: ")
            deadline_str = input("Enter the deadline (YYYY-MM-DD HH:MM): ")
            try:
                deadline = datetime.strptime(deadline_str, "%Y-%m-%d %H:%M")
            except ValueError:
                print("Invalid date format. Deadline not set.")
                deadline = None
            todo_list.add_task(task, deadline)
        elif choice == "2":
            index = int(input("Enter the task index to delete: "))
            todo_list.delete_task(index)
        elif choice == "3":
            index = int(input("Enter the task index to complete: "))
            todo_list.complete_task(index)
        elif choice == "4":
            todo_list.show_tasks()
        elif choice == "5":
            todo_list.upcoming_tasks()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
