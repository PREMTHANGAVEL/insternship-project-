

import os
import sys

TASKS_FILE = "tasks.txt"

def load_tasks():
    
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def save_tasks(tasks):
    
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task + "\n")

def view_tasks(tasks):
   
    if not tasks:
        print("\nNo tasks available.\n")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()

def add_task(tasks):
    """Add a new task."""
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"Task added: {task}")
    else:
        print("Task cannot be empty!")

def remove_task(tasks):
   
    if not tasks:
        print("No tasks to remove.")
        return
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def clear_tasks(tasks):
   
    confirm = input("Are you sure you want to clear all tasks? (y/n): ").lower()
    if confirm == "y":
        tasks.clear()
        save_tasks(tasks)
        print("All tasks cleared.")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Clear all tasks")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            clear_tasks(tasks)
        elif choice == "5":
            print("Goodbye! Your tasks are saved in tasks.txt")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting... Goodbye!")
        sys.exit(0)
