import datetime
# To-Do List
todo_list = []
def print_menu():
    print("==== To-Do List ====")
    print("1. Add a new task")
    print("2. Mark a task as complete")
    print("3. View incomplete tasks")
    print("4. View completed tasks")
    print("5. Exit")
def add_task():
    task = input("Enter the task: ")
    due_date = input("Enter the due date (YYYY-MM-DD): ")
    todo_list.append({"task": task, "due_date": due_date, "completed": False})
    print("Task added successfully!")
def mark_complete():
    for i, task in enumerate(todo_list):
        if not task["completed"]:
            print(f"{i+1}. {task['task']} - Due: {task['due_date']}")
    index = int(input("Enter the number of the task to mark as complete: "))
    if 1 <= index <= len(todo_list):
        todo_list[index-1]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Invalid task number.")
def view_incomplete():
    print("Incomplete Tasks:")
    for task in todo_list:
        if not task["completed"]:
            print(f"- {task['task']} - Due: {task['due_date']}")
def view_completed():
    print("Completed Tasks:")
    for task in todo_list:
        if task["completed"]:
            print(f"- {task['task']} - Due: {task['due_date']}")
def main():
    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            mark_complete()
        elif choice == "3":
            view_incomplete()
        elif choice == "4":
            view_completed()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
