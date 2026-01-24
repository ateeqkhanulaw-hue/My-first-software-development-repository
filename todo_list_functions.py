# Global list to store tasks
todo_list = []


def add_task(name):
    """Adds a new task to the list."""
    if name.strip():
        todo_list.append({"name": name, "completed": False})
        print(f"Task '{name}' added!")
    else:
        print("Error: Task name cannot be empty.")


def display_tasks():
    """Displays all tasks."""
    if not todo_list:
        print("\nNo tasks found.")
        return
    
    print("\n--- Your Tasks ---")
    for i, task in enumerate(todo_list, 1):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. [{status}] {task['name']}")


def mark_completed(task_num):
    """Marks a task as completed."""
    if 1 <= task_num <= len(todo_list):
        todo_list[task_num - 1]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Error: Invalid task number.")


def delete_task(task_num):
    """Deletes a task from the list."""
    if 1 <= task_num <= len(todo_list):
        removed = todo_list.pop(task_num - 1)
        print(f"Task '{removed['name']}' deleted!")
    else:
        print("Error: Invalid task number.")


def main():
    """Main function - runs the program."""
    print("\n=== TO-DO LIST MANAGER ===")
    
    while True:
        print("\n1. Add  2. View  3. Complete  4. Delete  5. Exit")
        choice = input("Choice: ").strip()
        
        if choice == "1":
            add_task(input("Task name: "))
        elif choice == "2":
            display_tasks()
        elif choice == "3":
            display_tasks()
            try:
                mark_completed(int(input("Task number: ")))
            except ValueError:
                print("Enter a valid number.")
        elif choice == "4":
            display_tasks()
            try:
                delete_task(int(input("Task number: ")))
            except ValueError:
                print("Enter a valid number.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()