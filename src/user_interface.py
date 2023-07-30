import tkinter as tk
from src import responsive_design, touchscreen_input, human_computer_interaction, aesthetics, usability, mobile_optimization

class UserInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Scientific Data Analyzer")
        mobile_optimization.optimizeForMobile(self.root)

        self.dataDisplay = tk.Text(self.root)
        self.dataDisplay.pack()

        self.inputField = tk.Entry(self.root)
        self.inputField.pack()

        self.loginButton = tk.Button(self.root, text="Login", command=self.authenticateUser)
        self.loginButton.pack()

        self.encryptionToggle = tk.Checkbutton(self.root, text="Encrypt Data", command=self.toggleEncryption)
        self.encryptionToggle.pack()

        responsive_design.applyResponsiveDesign(self.root)
        aesthetics.applyAesthetics(self.root)
        usability.optimizeUsability(self.root)

    def authenticateUser(self):
        userInput = self.inputField.get()
        authenticatedUser = authenticateUser(userInput)
        if authenticatedUser:
            self.dataDisplay.insert(tk.END, "User Authenticated\n")
        else:
            self.dataDisplay.insert(tk.END, "Authentication Failed\n")

    def toggleEncryption(self):
        if self.encryptionToggle.var.get():
            self.dataDisplay.insert(tk.END, "Encryption Enabled\n")
        else:
            self.dataDisplay.insert(tk.END, "Encryption Disabled\n")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    ui = UserInterface()
    ui.run()