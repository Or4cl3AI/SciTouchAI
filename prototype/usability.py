import tkinter as tk

# Shared variables
dataSet = None
userInput = None

# Shared DOM Element IDs
displayArea = None

def renderUI():
    """
    Function to render the user interface with usability in mind.
    """
    global displayArea

    # Create the main window
    window = tk.Tk()
    window.title("Scientific Data Analysis App")

    # Create a canvas for the display area
    displayArea = tk.Canvas(window, width=800, height=600)
    displayArea.pack()

    # Create a label for user instructions
    instructionLabel = tk.Label(window, text="Please input your data for analysis:")
    instructionLabel.pack()

    # Create a text box for user input
    global userInput
    userInput = tk.Entry(window)
    userInput.pack()

    # Create a button to submit the data
    submitButton = tk.Button(window, text="Submit", command=processData)
    submitButton.pack()

    # Run the application
    window.mainloop()

def processData():
    """
    Function to process the user input data.
    """
    global dataSet
    global userInput

    # Get the user input
    dataSet = userInput.get()

    # Clear the input field
    userInput.delete(0, tk.END)

    # Display the processed data
    displayData()

def displayData():
    """
    Function to display the processed data.
    """
    global displayArea
    global dataSet

    # Clear the display area
    displayArea.delete("all")

    # Display the data
    displayArea.create_text(400, 300, text=dataSet)

# Run the application
if __name__ == "__main__":
    renderUI()