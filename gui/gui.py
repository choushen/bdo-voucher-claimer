import tkinter as tk
from tkinter import ttk
import time

def bob():
    # This is just a placeholder function that waits for 5 seconds
    time.sleep(5)

def start():
    # Hide the username and password fields
    username_entry.grid_forget()
    password_entry.grid_forget()
    start_button.grid_forget()

    # Show the progress bar
    progress_bar.grid(row=1, column=0, padx=10, pady=10)

    # Call the bob function and update the progress bar
    for i in range(101):
        progress_bar['value'] = i
        progress_bar.update()
        time.sleep(0.05)

# Create the main window
root = tk.Tk()
root.title("Login")

# Create the username and password fields
username_label = ttk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=10)
username_entry = ttk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)

password_label = ttk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry = ttk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Create the start button
start_button = ttk.Button(root, text="Start", command=start)
start_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create the progress bar (hidden by default)
progress_bar = ttk.Progressbar(root, orient='horizontal', length=200, mode='determinate')
progress_bar.grid_forget()

# Start the main event loop
root.mainloop()