import tkinter as tk
from tkinter import messagebox
import random

# Task list
tasks = []

# Motivation quotes
quotes = [
    "Indeed, Allah is with the patient. (2:153)",
    "Do not despair of the mercy of Allah. (39:53)",
    "Verily, with hardship comes ease. (94:6)",
    "Your task today is your ladder to tomorrow. Keep climbing."
]

# Salah times
salah_times = {
    "Fajr": "05:20 AM",
    "Dhuhr": "12:15 PM",
    "Asr": "03:45 PM",
    "Maghrib": "07:10 PM",
    "Isha": "08:30 PM"
}

def add_task():
    task = task_entry.get()
    if task:
        tasks.append({"task": task, "done": False})
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def update_task_list():
    task_listbox.delete(0, tk.END)
    for i, t in enumerate(tasks):
        status = "✅" if t["done"] else "❌"
        task_listbox.insert(tk.END, f"{i+1}. {t['task']} - {status}")

def mark_task_done():
    try:
        index = task_listbox.curselection()[0]
        tasks[index]["done"] = True
        update_task_list()
    except IndexError:
        messagebox.showinfo("Selection Error", "Select a task to mark as done.")

def show_quote():
    quote = random.choice(quotes)
    quote_label.config(text=f"✨ {quote}")

def show_salah():
    times = "\n".join([f"{k}: {v}" for k, v in salah_times.items()])
    salah_label.config(text=f"🕌 Salah Times 🕌\n{times}")

# Create the main window
root = tk.Tk()
root.title("Prayer & Productivity Planner")
root.geometry("600x400")

# Title
title_label = tk.Label(root, text="🗓️ Prayer & Productivity Planner", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Task entry
task_frame = tk.Frame(root)
task_frame.pack(side="left", padx=20)

task_entry = tk.Entry(task_frame, width=30)
task_entry.pack(pady=5)

add_btn = tk.Button(task_frame, text="Add Task", command=add_task)
add_btn.pack(pady=5)

done_btn = tk.Button(task_frame, text="Mark as Done", command=mark_task_done)
done_btn.pack(pady=5)

task_listbox = tk.Listbox(task_frame, width=40, height=10)
task_listbox.pack(pady=10)

# Right panel
right_frame = tk.Frame(root)
right_frame.pack(side="right", padx=20)

quote_btn = tk.Button(right_frame, text="Show Motivation", command=show_quote)
quote_btn.pack(pady=5)

quote_label = tk.Label(right_frame, text="", wraplength=200, justify="left")
quote_label.pack(pady=5)

salah_btn = tk.Button(right_frame, text="Show Salah Times", command=show_salah)
salah_btn.pack(pady=5)

salah_label = tk.Label(right_frame, text="", justify="left")
salah_label.pack(pady=5)

# Start the GUI event loop
root.mainloop()
