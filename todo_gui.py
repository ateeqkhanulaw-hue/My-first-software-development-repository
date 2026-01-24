import tkinter as tk
from tkinter import messagebox


class TodoApp:
    """Simple To-Do List GUI Application."""
    
    def __init__(self, root):
        """Initialize the application."""
        self.root = root
        self.root.title("To-Do List Manager")
        self.root.geometry("400x500")
        self.root.config(bg="#f0f0f0")
        
        # Task list storage
        self.tasks = []
        
        # Create GUI elements
        self.create_widgets()
    
    def create_widgets(self):
        """Create all GUI widgets."""
        # Title Label
        title = tk.Label(
            self.root,
            text="📝 My To-Do List",
            font=("Arial", 20, "bold"),
            bg="#f0f0f0",
            fg="#333"
        )
        title.pack(pady=15)
        
        # Input Frame
        input_frame = tk.Frame(self.root, bg="#f0f0f0")
        input_frame.pack(pady=10)
        
        # Task Entry
        self.task_entry = tk.Entry(
            input_frame,
            font=("Arial", 12),
            width=25,
            bd=2,
            relief="groove"
        )
        self.task_entry.pack(side=tk.LEFT, padx=5)
        self.task_entry.bind("<Return>", lambda e: self.add_task())
        
        # Add Button
        add_btn = tk.Button(
            input_frame,
            text="Add",
            font=("Arial", 11, "bold"),
            bg="#4CAF50",
            fg="white",
            width=8,
            command=self.add_task
        )
        add_btn.pack(side=tk.LEFT, padx=5)
        
        # Task Listbox with Scrollbar
        list_frame = tk.Frame(self.root)
        list_frame.pack(pady=10, fill=tk.BOTH, expand=True, padx=20)
        
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.task_listbox = tk.Listbox(
            list_frame,
            font=("Arial", 12),
            width=35,
            height=12,
            selectmode=tk.SINGLE,
            bd=2,
            relief="groove",
            yscrollcommand=scrollbar.set
        )
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.task_listbox.yview)
        
        # Buttons Frame
        btn_frame = tk.Frame(self.root, bg="#f0f0f0")
        btn_frame.pack(pady=15)
        
        # Complete Button
        complete_btn = tk.Button(
            btn_frame,
            text="✓ Complete",
            font=("Arial", 10),
            bg="#2196F3",
            fg="white",
            width=10,
            command=self.complete_task
        )
        complete_btn.pack(side=tk.LEFT, padx=5)
        
        # Delete Button
        delete_btn = tk.Button(
            btn_frame,
            text="🗑 Delete",
            font=("Arial", 10),
            bg="#f44336",
            fg="white",
            width=10,
            command=self.delete_task
        )
        delete_btn.pack(side=tk.LEFT, padx=5)
        
        # Clear All Button
        clear_btn = tk.Button(
            btn_frame,
            text="Clear All",
            font=("Arial", 10),
            bg="#FF9800",
            fg="white",
            width=10,
            command=self.clear_all
        )
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Status Label
        self.status_label = tk.Label(
            self.root,
            text="Tasks: 0",
            font=("Arial", 10),
            bg="#f0f0f0",
            fg="#666"
        )
        self.status_label.pack(pady=10)
    
    def add_task(self):
        """Add a new task."""
        task = self.task_entry.get().strip()
        
        if not task:
            messagebox.showwarning("Warning", "Please enter a task!")
            return
        
        self.tasks.append({"name": task, "completed": False})
        self.task_listbox.insert(tk.END, f"☐ {task}")
        self.task_entry.delete(0, tk.END)
        self.update_status()
    
    def complete_task(self):
        """Mark selected task as completed."""
        try:
            index = self.task_listbox.curselection()[0]
            task = self.tasks[index]
            
            if not task["completed"]:
                task["completed"] = True
                self.task_listbox.delete(index)
                self.task_listbox.insert(index, f"✓ {task['name']}")
                self.task_listbox.itemconfig(index, fg="green")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task!")
    
    def delete_task(self):
        """Delete selected task."""
        try:
            index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(index)
            self.tasks.pop(index)
            self.update_status()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task!")
    
    def clear_all(self):
        """Clear all tasks."""
        if self.tasks:
            if messagebox.askyesno("Confirm", "Delete all tasks?"):
                self.task_listbox.delete(0, tk.END)
                self.tasks.clear()
                self.update_status()
    
    def update_status(self):
        """Update the status label."""
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks if t["completed"])
        self.status_label.config(text=f"Tasks: {total} | Completed: {completed}")


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()