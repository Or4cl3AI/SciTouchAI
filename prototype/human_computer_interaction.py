```python
import tkinter as tk
from tkinter import messagebox

class HCI:
    def __init__(self, root):
        self.root = root
        self.root.title('Scientific Data Analyzer')
        self.root.geometry('500x500')

        self.data_display = tk.Text(self.root, height=20, width=50)
        self.data_display.pack()

        self.input_field = tk.Entry(self.root)
        self.input_field.pack()

        self.login_button = tk.Button(self.root, text="Login", command=self.authenticate_user)
        self.login_button.pack()

        self.encryption_toggle = tk.Checkbutton(self.root, text="Enable Encryption", command=self.encrypt_data)
        self.encryption_toggle.pack()

    def authenticate_user(self):
        user_input = self.input_field.get()
        authenticated_user = authenticate_user(user_input)
        if authenticated_user:
            messagebox.showinfo("Authentication Successful", "You are now logged in.")
        else:
            messagebox.showerror("Authentication Failed", "Invalid credentials. Please try again.")

    def encrypt_data(self):
        data_set = self.data_display.get('1.0', 'end-1c')
        encrypted_data = encrypt_data(data_set)
        self.data_display.delete('1.0', tk.END)
        self.data_display.insert(tk.END, encrypted_data)
        messagebox.showinfo("Encryption Enabled", "Your data is now encrypted.")

root = tk.Tk()
app = HCI(root)
root.mainloop()
```