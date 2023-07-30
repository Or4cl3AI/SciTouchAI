import tkinter as tk
from tkinter import ttk

def create_interface():
    root = tk.Tk()
    root.title("Scientific Data Analyzer")

    # Create a frame for the data display
    data_display = ttk.Frame(root, padding="10")
    data_display.grid(row=0, column=0, sticky=(tk.W, tk.E))

    # Create a frame for the input field
    input_field = ttk.Frame(root, padding="10")
    input_field.grid(row=1, column=0, sticky=(tk.W, tk.E))

    # Create a frame for the login button
    login_button = ttk.Frame(root, padding="10")
    login_button.grid(row=2, column=0, sticky=(tk.W, tk.E))

    # Create a frame for the encryption toggle
    encryption_toggle = ttk.Frame(root, padding="10")
    encryption_toggle.grid(row=3, column=0, sticky=(tk.W, tk.E))

    # Create a text widget for displaying data
    data_text = tk.Text(data_display, width=50, height=10)
    data_text.pack()

    # Create an entry widget for user input
    user_entry = ttk.Entry(input_field, width=50)
    user_entry.pack()

    # Create a button for user login
    login_btn = ttk.Button(login_button, text="Login")
    login_btn.pack()

    # Create a checkbutton for encryption toggle
    encryption_check = ttk.Checkbutton(encryption_toggle, text="Enable Encryption")
    encryption_check.pack()

    root.mainloop()

if __name__ == "__main__":
    create_interface()