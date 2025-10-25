from collections import deque

# Queue for tasks
tasks = deque()
# Stack for undo operation
undo_stack = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"✅ '{task}' added successfully!\n")

def view_tasks():
    if not tasks:
        print("📭 No tasks in your To-Do List!\n")
    else:
        print("\n📋 Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print()

def delete_task():
    if not tasks:
        print("⚠️ No tasks to delete!\n")
        return
    view_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks[index]
            undo_stack.append(removed_task)
            tasks.remove(removed_task)
            print(f"❌ '{removed_task}' deleted successfully!\n")
        else:
            print("❗ Invalid task number!\n")
    except ValueError:
        print("❗ Please enter a valid number!\n")

def undo_delete():
    if not undo_stack:
        print("⚠️ No task to undo!\n")
    else:
        last_deleted = undo_stack.pop()
        tasks.append(last_deleted)
        print(f"🔄 '{last_deleted}' restored successfully!\n")

def main():
    print("\n🧩 Welcome to To-Do List (Using Stack & Queue)\n")

    while True:
        print("Choose an option:")
        print("➕ Add Task")
        print("📋 View All Tasks")
        print("❌ Delete Task")
        print("🔄 Undo Last Deleted Task")
        print("🚪 Exit")

        choice = input("\nEnter your choice (add/view/delete/undo/exit): ").lower()

        if choice == "add":
            add_task()
        elif choice == "view":
            view_tasks()
        elif choice == "delete":
            delete_task()
        elif choice == "undo":
            undo_delete()
        elif choice == "exit":
            print("👋 Exiting the To-Do List App. Have a productive day!")
            break
        else:
            print("❗ Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()
