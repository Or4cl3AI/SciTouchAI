```python
import tkinter as tk
from tkinter import messagebox
from prototype import data_analysis, machine_learning, ai_module, natural_language_processing

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Scientific Data Analysis App")
        self.geometry("500x500")

        self.data_set = None
        self.user_input = None

        self.create_widgets()

    def create_widgets(self):
        self.input_label = tk.Label(self, text="Enter your query:")
        self.input_label.pack()

        self.user_input_field = tk.Entry(self)
        self.user_input_field.pack()

        self.submit_button = tk.Button(self, text="Submit", command=self.process_input)
        self.submit_button.pack()

        self.data_display = tk.Label(self, text="")
        self.data_display.pack()

    def process_input(self):
        self.user_input = self.user_input_field.get()
        if self.user_input:
            self.data_set = data_analysis.analyze_data(self.user_input)
            machine_learning.analyze_data(self.data_set)
            ai_module.analyze_data(self.data_set)
            natural_language_processing.analyze_data(self.data_set)
            self.data_display.config(text=str(self.data_set))
        else:
            messagebox.showerror("Error", "Input field is empty")

    def run(self):
        self.mainloop()

if __name__ == "__main__":
    app = Application()
    app.run()
```