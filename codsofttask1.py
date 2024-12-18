import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task.strip():
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete!")

def update_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        new_task = task_entry.get()
        if new_task.strip():
            task_listbox.delete(selected_task_index)
            task_listbox.insert(selected_task_index, new_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Updated task cannot be empty!")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to update!")

def clear_all_tasks():
    task_listbox.delete(0, tk.END)

# Create the main application window
app = tk.Tk()
app.title("To-Do List Application")
app.geometry("400x400")

# Input field and buttons
frame = tk.Frame(app)
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=30)
task_entry.pack(side=tk.LEFT, padx=5)

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT, padx=5)

update_button = tk.Button(frame, text="Update Task", command=update_task)
update_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(frame, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(app, text="Clear All Tasks", command=clear_all_tasks)
clear_button.pack(pady=10)

# Listbox to display tasks
task_listbox = tk.Listbox(app, width=50, height=15)
task_listbox.pack(pady=10)

# Start the Tkinter main loop
app.mainloop()
