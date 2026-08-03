"""
Project 1: To-Do List Application
----------------------------------
A simple console-based To-Do List built using Python Lists.

Core concepts demonstrated:
- Lists and .append()
- Loops (for/while)
- User input handling
- Input -> Process -> Output logic
- Functions for code organization
"""


# Global task list

# Each task is stored as a dictionary inside a list, like:
# {"name": "Buy groceries", "done": False}
# We chose a list of dictionaries so we can store BOTH the
# task text AND whether it is completed, using one collection.
tasks = []



# Display functions

def show_banner():
    print("=" * 40)
    print("        PYTHON TO-DO LIST MANAGER")
    print("=" * 40)


def show_menu():
    print("\n----------- MENU -----------")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit")
    print("-----------------------------")



# Core features

def add_task():
    """Asks the user for a task and adds it to the tasks list."""
    task_name = input("Enter the new task: ").strip()

    # Prevent empty task input
    if task_name == "":
        print("⚠  Task cannot be empty. Please enter some text.")
        return

    # A new task always starts as "not completed"
    new_task = {"name": task_name, "done": False}
    tasks.append(new_task)  # .append() adds the task to the end of the list
    print(f"✔  Task added: \"{task_name}\"")


def view_tasks():
    print("\n------------ YOUR TASKS ------------")

    if len(tasks) == 0:
        print("No tasks yet. Add one from the menu!")
    else:
        # enumerate() gives us both the position (index) and the task
        # start=1 so the list looks natural to a human (1, 2, 3, ...)
        for position, task in enumerate(tasks, start=1):
            status = "[✓]" if task["done"] else "[ ]"
            print(f"{position}. {status} {task['name']}")

    print("-------------------------------------")


def get_valid_task_number(prompt):
    """
    Asks the user for a task number and makes sure it is valid.
    Returns the LIST INDEX of the chosen task, or None if invalid.
    This function is reused by both 'complete' and 'delete'.
    """
    if len(tasks) == 0:
        print("⚠  There are no tasks to select.")
        return None

    view_tasks()
    user_input = input(prompt).strip()

    # Make sure the user typed a number, not text
    if not user_input.isdigit():
        print("⚠  Please enter a valid number.")
        return None

    task_number = int(user_input)
    index = task_number - 1  # convert human-friendly number to list index

    # Make sure the number is within range of the list
    if index < 0 or index >= len(tasks):
        print("⚠  That task number does not exist.")
        return None

    return index


def complete_task():
    """Marks a chosen task as completed."""
    index = get_valid_task_number("Enter the task number to mark as completed: ")
    if index is not None:
        tasks[index]["done"] = True
        print(f"✔  Marked as completed: \"{tasks[index]['name']}\"")


def delete_task():
    """Removes a chosen task from the list."""
    index = get_valid_task_number("Enter the task number to delete: ")
    if index is not None:
        removed_task = tasks.pop(index)  # .pop() removes and returns the item
        print(f"🗑  Deleted task: \"{removed_task['name']}\"")



# Main program loop

def main():
    show_banner()

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("\nThank you for using the To-Do List Manager. Goodbye! 👋")
            break
        else:
            print("⚠  Invalid choice. Please enter a number from 1 to 5.")



# Program entry point

if __name__ == "__main__":
    main()