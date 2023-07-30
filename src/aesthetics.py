```python
import matplotlib.pyplot as plt
from matplotlib import style

def applyAesthetics(dataDisplay):
    """
    Function to apply aesthetic design principles to the data display.
    """
    # Set the style to be 'ggplot' for better aesthetics
    style.use('ggplot')

    # Set the title, labels, and legend for the plot
    dataDisplay.set_title('Scientific Data Analysis')
    dataDisplay.set_xlabel('Data Points')
    dataDisplay.set_ylabel('Values')
    dataDisplay.legend()

    # Set the grid for better readability
    dataDisplay.grid(True)

    # Show the plot
    plt.show()

def applyColorScheme(dataDisplay):
    """
    Function to apply a color scheme to the data display.
    """
    # Set the color map to be 'viridis' for better aesthetics
    cmap = plt.get_cmap('viridis')

    # Apply the color map to the data display
    dataDisplay.set_cmap(cmap)

def applyTypography(dataDisplay):
    """
    Function to apply typography principles to the data display.
    """
    # Set the font to be 'Arial' for better readability
    font = {'family' : 'Arial',
            'weight' : 'bold',
            'size'   : 12}

    # Apply the font settings to the data display
    plt.rc('font', **font)
```