import tkinter as tk
from tkinter import ttk
import time

def bob():
    # This is just a placeholder function that waits for 5 seconds
    time.sleep(5)

def start():
        # Hide the username and password fields and the start button
    username_label.grid_remove()
    username_entry.grid_remove()
    password_label.grid_remove()
    password_entry.grid_remove()
    start_button.grid_remove()

    
    # Create the progress bar (hidden by default)
    progress_bar = ttk.Progressbar(root, orient='horizontal', length=200, mode='determinate')
    # Call the bob function and update the progress bar
    for i in range(101):
        # Show the progress bar and center it
        progress_bar.place(relx=0.5, rely=0.5, anchor="center")
        progress_bar['value'] = i
        progress_bar.update()
        time.sleep(0.05)

    # Hide the progress bar after the loop is completed
    progress_bar.place_forget()

    # Create a new frame for the table and center it
    table_frame = ttk.Frame(root)
    table_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Create a treeview (table) widget
    table = ttk.Treeview(table_frame, columns=("result", "code"), show="headings")
    table.heading("result", text="Result")
    table.heading("code", text="Code")

    # Add dummy data (20 rows) to the table
    for i in range(20):
        table.insert("", "end", values=("Could not add coupon", "ABC-EFG"))

    # Add a vertical scrollbar to the table
    scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
    table.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    table.pack(fill="both", expand=True)

# Create the main window
root = tk.Tk()
root.title("Login")
root.geometry("600x400")  # Set the default size of the app (width x height)
root.resizable(False, False)


# Create a container frame and center it
container = ttk.Frame(root)
container.grid(row=0, column=0, padx=10, pady=10)

# Set container frame's column weight to 1
container.columnconfigure(0, weight=1)

# Create the username and password fields
username_label = ttk.Label(container, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
username_entry = ttk.Entry(container)
username_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

password_label = ttk.Label(container, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
password_entry = ttk.Entry(container, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

# Create the start button
start_button = ttk.Button(container, text="Start", command=start)
start_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# Start the main event loop
root.mainloop()
