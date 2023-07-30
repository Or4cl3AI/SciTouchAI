import tkinter as tk
from tkinter import ttk
from prototype import touchscreen_input

class HCI:
    def __init__(self, root):
        self.root = root
        self.userInput = ""
        self.touchScreenInput = touchscreen_input.TouchScreenInput(self.root)

    def capture_user_input(self, event):
        self.userInput = self.touchScreenInput.get_input(event)
        self.process_user_input()

    def process_user_input(self):
        # Process the user input here
        # This is a placeholder and should be replaced with actual processing code
        print(self.userInput)

    def setup_ui(self):
        self.root.bind("<Button-1>", self.capture_user_input)

def main():
    root = tk.Tk()
    hci = HCI(root)
    hci.setup_ui()
    root.mainloop()

if __name__ == "__main__":
    main()