# Todo_list
A Simple Python-based project designed to manage daily tasks efficiently.

---

## Project Overview
The **To-Do List Application** is a simple yet powerful Python program designed to manage your daily tasks efficiently.  
It demonstrates how **Queue (FIFO)** and **Stack (LIFO)** data structures can be used in a real-world task management system.  
Users can add, view, complete, and undo completed tasks through a clean and user-friendly command-line interface.

---

## Key Features
- ➕ **Add Task** – Add new tasks to the to-do list.  
- 📋 **View All Tasks** – View all your pending tasks in the order they were added.  
- ❌ **Complete Task** – Mark the earliest added task as completed (FIFO).  
- 🔄 **Undo Last Completed Task** – Restore the last completed task using a stack.  
- 🚪 **Exit** – Exit the application gracefully.

---

## Data Structures Used
- **Queue (FIFO)** → For managing pending tasks in the order they were added.  
- **Stack (LIFO)** → For handling undo functionality of completed tasks.  
- **Deque (from collections module)** → Used for efficient queue operations.  

---

## How It Works
1. When a task is added, it goes to the end of the **Queue**.  
2. Completing a task removes it from the front of the **Queue** (FIFO order).  
3. The removed task is pushed into the **Stack**, enabling the **Undo** operation.  
4. Undoing a task pops it from the **Stack** and adds it back to the **Queue**.

---

## How to Run
1. Make sure you have **Python 3** installed.  
2. Save the file as `todo_list.py`.  
3. Open your terminal or command prompt.  
4. Run the program:
   ```bash
   python todo_list.py

---

## Technologies Used

Python 3

Queue (FIFO)

Stack (LIFO)

Collections Module

---

## License
This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

---

## Contact
If you have any questions or feedback, feel free to reach out:
* **GitHub:** [LuckyG05](https://github.com/LuckyG05)

---

