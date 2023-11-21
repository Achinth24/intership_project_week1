import datetime
class ToDoList:
    def __init__(self):
        self.tasks = {}
        self.completed_tasks = {}
        self.task_id_counter = 1

    def add_task(self, description, due_date=None, priority=None):
        task_id = self.task_id_counter
        self.tasks[task_id] = {
            'description': description,
            'due_date': due_date,
            'priority': priority,
            'completed': False
        }
        self.task_id_counter += 1
        print(f"Task added with ID {task_id}")

    def display_tasks(self):
        print("\nCurrent Tasks:")
        for task_id, task in self.tasks.items():
            print(f"ID: {task_id}, Description: {task['description']}, Due Date: {task['due_date']}, Priority: {task['priority']}, Completed: {task['completed']}")

    def mark_task_completed(self, task_id):
        if task_id in self.tasks:
            self.completed_tasks[task_id] = self.tasks.pop(task_id)
            self.completed_tasks[task_id]['completed'] = True
            print(f"Task with ID {task_id} marked as completed.")
        else:
            print(f"Task with ID {task_id} not found.")

    def update_task(self, task_id, description=None, due_date=None, priority=None):
        if task_id in self.tasks:
            task = self.tasks[task_id]
            if description is not None:
                task['description'] = description
            if due_date is not None:
                task['due_date'] = due_date
            if priority is not None:
                task['priority'] = priority
            print(f"Task with ID {task_id} updated.")
        else:
            print(f"Task with ID {task_id} not found.")

    def remove_task(self, task_id):
        if task_id in self.tasks:
            self.tasks.pop(task_id)
            print(f"Task with ID {task_id} removed.")
        elif task_id in self.completed_tasks:
            self.completed_tasks.pop(task_id)
            print(f"Completed task with ID {task_id} removed.")
        else:
            print(f"Task with ID {task_id} not found.")

def main():
    todo_list = ToDoList()

    while True:
        print("\n=== To-Do List Menu ===")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Mark Task as Completed")
        print("4. Update Task")
        print("5. Remove Task")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            description = input("Enter task description: ")
            due_date = input("Enter due date (optional): ")
            priority = input("Enter priority (optional): ")
            todo_list.add_task(description, due_date, priority)

        elif choice == '2':
            todo_list.display_tasks()

        elif choice == '3':
            task_id = int(input("Enter the ID of the task to mark as completed: "))
            todo_list.mark_task_completed(task_id)

        elif choice == '4':
            task_id = int(input("Enter the ID of the task to update: "))
            description = input("Enter new description (press Enter to keep existing): ")
            due_date = input("Enter new due date (press Enter to keep existing): ")
            priority = input("Enter new priority (press Enter to keep existing): ")
            todo_list.update_task(task_id, description, due_date, priority)

        elif choice == '5':
            task_id = int(input("Enter the ID of the task to remove: "))
            todo_list.remove_task(task_id)

        elif choice == '6':
            print("Exiting the To-Do List Application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
