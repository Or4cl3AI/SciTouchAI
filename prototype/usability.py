```python
import tkinter as tk
from tkinter import messagebox
from prototype import human_computer_interaction, touchscreen_input

class Usability:
    def __init__(self, root):
        self.root = root
        self.root.title('Scientific Data Analysis')
        self.root.geometry('500x500')

        self.user_input_field = tk.Entry(self.root, textvariable=user_input)
        self.user_input_field.pack()

        self.submit_button = tk.Button(self.root, text="Submit", command=self.process_input)
        self.submit_button.pack()

        self.data_display = tk.Label(self.root, text="")
        self.data_display.pack()

    def process_input(self):
        input_data = self.user_input_field.get()
        if not input_data:
            messagebox.showerror("Error", "Input field is empty")
            return

        try:
            processed_data = human_computer_interaction.process_input(input_data)
            touchscreen_input.capture_input(processed_data)
            self.data_display.config(text=processed_data)
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = Usability(root)
    root.mainloop()
```