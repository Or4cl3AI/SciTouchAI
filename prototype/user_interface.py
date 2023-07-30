```python
import tkinter as tk
from tkinter import messagebox
from prototype.data_analysis import analyze_data
from prototype.authentication import authenticate_user
from prototype.process_input import process_input

class UserInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Scientific Data Analyzer")
        self.data_set = None
        self.user_input = None

    def create_widgets(self):
        self.user_input_field = tk.Entry(self.window, id="user-input-field")
        self.user_input_field.pack()

        self.submit_button = tk.Button(self.window, text="Submit", command=self.submit, id="submit-button")
        self.submit_button.pack()

        self.data_display = tk.Label(self.window, id="data-display")
        self.data_display.pack()

    def submit(self):
        self.user_input = self.user_input_field.get()
        if authenticate_user(self.user_input):
            messagebox.showinfo("User_Authenticated", "User authenticated successfully.")
            self.data_set = process_input(self.user_input)
            analyzed_data = analyze_data(self.data_set)
            self.data_display.config(text=str(analyzed_data))
            messagebox.showinfo("Data_Analysis_Complete", "Data analysis is complete.")
        else:
            messagebox.showerror("Authentication Failed", "User authentication failed. Please try again.")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    ui = UserInterface()
    ui.create_widgets()
    ui.run()
```