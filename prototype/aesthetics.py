import tkinter as tk
from tkinter import ttk

def apply_aesthetics(root):
    # Set the theme of the application
    style = ttk.Style(root)
    style.theme_use('clam')

    # Set the color of the background, buttons, and text
    style.configure('TFrame', background='white')
    style.configure('TButton', background='white', foreground='black')
    style.configure('TLabel', background='white', foreground='black')

    # Set the font of the buttons and labels
    style.configure('TButton', font=('Arial', 20))
    style.configure('TLabel', font=('Arial', 20))

    # Set the size of the buttons
    style.configure('TButton', width=20, height=2)

    # Set the layout of the buttons and labels
    style.layout('TButton', [
        ('Button.padding', {'children':
            [('Button.label', {'side': 'left', 'expand': 1})],
        })
    ])
    style.layout('TLabel', [
        ('Label.padding', {'children':
            [('Label.label', {'side': 'left', 'expand': 1})],
        })
    ])

    return style

def create_interface():
    # Create the root window
    root = tk.Tk()
    root.title('Scientific Data Analysis')

    # Apply aesthetics to the root window
    style = apply_aesthetics(root)

    # Create a frame for the data display
    data_display = ttk.Frame(root)
    data_display.pack(fill='both', expand=True)

    # Create a label for the data display
    data_label = ttk.Label(data_display, text='Data Display:')
    data_label.pack(side='top', fill='x')

    # Create a text box for the data display
    data_text = tk.Text(data_display)
    data_text.pack(side='top', fill='both', expand=True)

    # Create a frame for the user input
    input_frame = ttk.Frame(root)
    input_frame.pack(side='top', fill='x')

    # Create a label for the user input
    input_label = ttk.Label(input_frame, text='User Input:')
    input_label.pack(side='left')

    # Create an entry for the user input
    input_entry = ttk.Entry(input_frame)
    input_entry.pack(side='left', fill='x', expand=True)

    # Create a button for the user input
    input_button = ttk.Button(input_frame, text='Submit')
    input_button.pack(side='left')

    # Run the application
    root.mainloop()

if __name__ == '__main__':
    create_interface()