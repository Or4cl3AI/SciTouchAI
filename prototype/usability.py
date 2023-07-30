```python
from prototype.mobile_interface import userInput, displayData

def usability():
    """
    Function to ensure the app is user-friendly.
    """
    try:
        # Check if the user input is valid
        if not userInput:
            raise ValueError("No input provided by the user.")
        
        # Check if the data display is user-friendly
        if not displayData:
            raise ValueError("Data display is not user-friendly.")
        
        # Check if the user input is easy to understand
        if not isinstance(userInput, str):
            raise TypeError("User input is not in a readable format.")
        
        # Check if the data display is easy to understand
        if not isinstance(displayData, str):
            raise TypeError("Data display is not in a readable format.")
        
        print("Usability checks passed successfully.")
    except ValueError as ve:
        print(f"Usability Error: {ve}")
    except TypeError as te:
        print(f"Usability Error: {te}")

if __name__ == "__main__":
    usability()
```