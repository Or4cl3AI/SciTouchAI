```python
import tkinter as tk
from src import touchscreen_input

class HCI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Scientific Data Analyzer")
        self.root.geometry("400x600")

        self.dataDisplay = tk.Label(self.root, text="")
        self.dataDisplay.pack()

        self.inputField = tk.Entry(self.root)
        self.inputField.pack()

        self.loginButton = tk.Button(self.root, text="Login", command=self.authenticateUser)
        self.loginButton.pack()

        self.encryptionToggle = tk.Checkbutton(self.root, text="Enable Encryption", command=self.encryptData)
        self.encryptionToggle.pack()

    def applyHCI(self):
        self.root.mainloop()

    def authenticateUser(self):
        userInput = self.inputField.get()
        authenticatedUser = touchscreen_input.authenticateUser(userInput)
        if authenticatedUser:
            self.dataDisplay.config(text="User Authenticated")
        else:
            self.dataDisplay.config(text="Authentication Failed")

    def encryptData(self):
        dataSet = self.inputField.get()
        encryptedData = touchscreen_input.encryptData(dataSet)
        if encryptedData:
            self.dataDisplay.config(text="Data Encrypted")
        else:
            self.dataDisplay.config(text="Encryption Failed")

if __name__ == "__main__":
    hci = HCI()
    hci.applyHCI()
```